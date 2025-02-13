#!/usr/bin/env python

# Copyright 2024 Amazon.com and its affiliates; all rights reserved.
# This file is AWS Content and may not be duplicated or distributed without permission
import sys
from pathlib import Path
import botocore
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
import boto3
from src.utils.bedrock_agent import (
    Agent,
    SupervisorAgent,
    Task,
    Guardrail,
    region,
    account_id,
    agents_helper
)
import argparse

from src.utils.knowledge_base_helper import KnowledgeBasesForAmazonBedrock

bedrock_client = boto3.client("bedrock")



def main(args):
    inputs = {"ticker": args.ticker}

    if args.recreate_agents == "false":
        Agent.set_force_recreate_default(False)
    else:
        Agent.set_force_recreate_default(True)
        agents_helper.delete_agent(agent_name="portfolio_assistant", delete_role_flag=True, verbose=True)
    if args.clean_up == "true":
        agents_helper.delete_agent(agent_name="portfolio_assistant", delete_role_flag=True, verbose=True)
        agents_helper.delete_agent(agent_name="news_agent", delete_role_flag=True, verbose=True)
        agents_helper.delete_agent(agent_name="stock_data_agent", delete_role_flag=True, verbose=True)
        agents_helper.delete_agent(agent_name="analyst_agent", delete_role_flag=True, verbose=True)
        response = bedrock_client.list_guardrails()
        for _gr in response["guardrails"]:
            if _gr["name"] == "no_bitcoin_guardrail":
                print(f"Found guardrail: {_gr['id']}")
                guardrail_identifier = _gr["id"]
                bedrock_client.delete_guardrail(guardrailIdentifier=guardrail_identifier)
    else:
        # Define a new Guardrail
        no_bitcoin_guardrail = Guardrail(
            "no_bitcoin_guardrail",
            "bitcoin_topic",
            "No Bitcoin or cryptocurrency allowed in the analysis.",
            denied_topics=["bitcoin", "crypto", "cryptocurrency"],
            blocked_input_response="Sorry, this agent cannot discuss bitcoin.",
            verbose=True,
        )

        # Define News Agent
        news_agent = Agent.direct_create(
            name="news_agent",
            role="Market News Researcher",
            goal="Fetch latest relevant news for a given stock based on a ticker.",
            instructions="""You are a Market News Researcher responsible for retrieving and summarizing financial news relevant to a specific stock. 
                            Fetch and summarize the latest financial news, regulatory filings, and market commentary related to the given ticker.
                            Extract key insights from earnings calls, SEC filings (10-K, 10-Q), and corporate press releases.
                            Structure news summaries clearly, including headline, source, timestamp, and key takeaways.
                            Avoid speculation, financial advice, or opinion-based conclusions.
                            Present findings objectively, ensuring accuracy and neutrality in reporting.""",
            tool_code=f"arn:aws:lambda:{region}:{account_id}:function:web_search",
            tool_defs=[
                {
                    "name": "web_search",
                    "description": "Searches the web for information, focus on high-quality resources that inform you about investment choices",
                    "parameters": {
                        "search_query": {
                            "description": "The query to search the web with",
                            "type": "string",
                            "required": True,
                        },
                        "target_website": {
                            "description": "The specific website to search including its domain name. If not provided, the most relevant website will be used",
                            "type": "string",
                            "required": False,
                        },
                        "topic": {
                            "description": "The topic being searched. 'news' or 'general'. Helps narrow the search when news is the focus.",
                            "type": "string",
                            "required": False,
                        },
                        "days": {
                            "description": "The number of days of history to search. Helps when looking for recent events or news.",
                            "type": "string",
                            "required": False,
                        },
                    },
                }
            ],
        )

        # Define Stock Data Agent
        stock_data_agent = Agent.direct_create(
            name="stock_data_agent",
            role="Financial Data Collector",
            goal="Retrieve real time and hostric stock prices as well as optimizing a portfolio given tickers.",
            instructions="""Specialist in real-time financial data extraction and portfloio optimization. Use the stock_data_agent for stock price retrieval. 
                            Use the portfolio optimization action if the user requests portflio optimization. The portfolio_optimization_action_group will always come sequentially after the stock_data_lookup if given three or more stock tickers.
                            Do not invoke the portfolio_optimization_action_group unless there are at least three tickers in the query.""",
            tool_code=f"arn:aws:lambda:{region}:{account_id}:function:stock_data_lookup",
            tool_defs=[
                {
                    "name": "stock_data_lookup",
                    "description": "Gets the 1 month stock price history for a given stock ticker, formatted as JSON",
                    "parameters": {
                        "ticker": {
                            "description": "The ticker to retrieve price history for",
                            "type": "string",
                            "required": True,
                        }
                    },
                }
            ],
        )
        # Define action group name
        portfolio_action_group_name = "portfolio_optimization_action_group"

        try:
            # Attempt to create the action group
            agents_helper.add_action_group_with_lambda(
                stock_data_agent.name,  # Attach to the stock_data_agent
                "portfolio_optimization_ag",  # Action Group Name
                f"arn:aws:lambda:{region}:{account_id}:function:FSI-PortfolioTool-BedrockAgent",  # Lambda function ARN
                [{
                    "name": "portfolio_optimization",
                    "description": "Optimizes a stock portfolio given a list of tickers and historical prices.",
                    "parameters": {
                        "tickers": {
                            "description": "A comma-separated list of stock tickers to include in the portfolio",
                            "type": "string",
                            "required": True
                        },
                        "prices": {
                            "description": "A JSON object with dates as keys and stock prices as values",
                            "type": "string",
                            "required": True
                        }
                    }
                }],
                portfolio_action_group_name,
                "Action group for portfolio optimization",
                verbose=True
            )
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "ConflictException":
                print(f"Action group '{portfolio_action_group_name}' already exists. Skipping creation.")
            else:
                raise  # Re-raise other unexpected errors


        # Initialize the Knowledge Base helper
        kb_helper = KnowledgeBasesForAmazonBedrock()

        # Create or retrieve the Knowledge Base for analyst_agent
        kb_name = "financial_analysis_kb"
        kb_description = "Useful for when you need to look up financial information like 10K reports, revenues, sales, net sales, loss and risks. Contains earnings calls"
        kb_s3_bucket = args.kb_s3_bucket  # Get the bucket name from CLI args

        kb_id, ds_id = kb_helper.create_or_retrieve_knowledge_base(
            kb_name=kb_name,
            kb_description=kb_description,
            data_bucket_name=kb_s3_bucket,
            embedding_model="amazon.titan-embed-text-v2:0",
        )

        # Define Analyst Agent
        analyst_agent = Agent.direct_create(
            name="analyst_agent",
            role="A financial analyst specializing in synthesizing stock market trends and financial news into structured investment insights. The agent produces fact-based summaries to support strategic decision-making.",
            goal="Analyze stock trends and market news to generate insights.",
            instructions="""You are a Financial Analyst, responsible for analyzing stock trends and financial news to generate structured insights.
                            Combine stock price trends with financial news to identify key patterns.
                            Use your expertise to analyze macroeconomic indicators, company earnings, and market sentiment.
                            Ensure responses are fact-driven, clearly structured, and cite sources where applicable.
                            Do not generate financial advice—your role is to analyze and summarize available data objectively.
                            Keep analyses concise and insightful, focusing on major trends and anomalies.""",
        )

        try:
            agents_helper.associate_kb_with_agent(
                agent_id=news_agent.agent_id,  # Correct way to reference the agent ID
                kb_id=kb_id,
                description="Financial reports, including ewarnings calls, 10k, 10Q, etc."
            )
        except botocore.exceptions.ClientError as e:
            if e.response["Error"]["Code"] == "ConflictException":
                print(f"Knowledge Base already exists. Skipping creation.")
            else:
                raise  # Re-raise other unexpected errors

        kb_helper.synchronize_data(kb_id, ds_id)

        # Create Tasks
        news_task = Task.direct_create(
            name="news_task",
            description=f"Retrieve latest news about the given stock ticker: {inputs['ticker']}.",
            expected_output="List of 5 relevant news articles.",
            inputs=inputs,
        )

        stock_data_task = Task.direct_create(
            name="stock_data_task",
            description=f"Retrieve stock price history for the given stock ticker: {inputs['ticker']}",
            expected_output="JSON object containing stock price history.",
            inputs=inputs,
        )

        analysis_task = Task.direct_create(
            name="analysis_task",
            description=(
                f"""
                Analyze the news and stock trends, 
                to provide actionable insights on {inputs['ticker']}, 
                including news highlights and recommendations for the future. 
                Be sure to state the high and low price of the stock in the analysis.
                """
            ),
            expected_output="A summary report with market trends and insights.",
            inputs=inputs,
        )

        portfolio_assistant = SupervisorAgent.direct_create(
            "portfolio_assistant",
            role="Portfolio Assistant",
            goal="A seasoned investment research expert responsible for orchestrating subagents to conduct a comprehensive stock analysis. This agent synthesizes market news, stock data, and analyst insights into a structured investment report.",
            collaboration_type="SUPERVISOR",
            instructions="""
                    You are a Portfolio Assistant, a financial research supervisor overseeing multiple specialized agents. Your goal is to coordinate and synthesize their outputs to create a structured stock investment analysis.
                    Orchestrate collaboration between subagents:
                    news_agent: Retrieves and summarizes latest financial news for a stock. Includes a knowledge base with SEC filings, earning calls, etc.
                    stock_data_agent: Provides historic and realt ime stock prices. Also has a portfolio optimization function that should only be used if the user asks for it specifically.
                    analyst_agent: Synthesizes financial data and market trends into a structured, fact-based investment insight.
                    Do not provide direct investment advice—instead, deliver a well-structured report with key observations, risks, and considerations.
                    Ensure findings are comprehensive, well-organized, and relevant to investor decision-making.
                    Format responses clearly, distinguishing between financial news, technical stock analysis, and synthesized insights.
            """,
            collaborator_agents=[
                {
                    "agent": "news_agent",
                    "instructions": """
                            Use this collaborator for finding news about specific stocks.
                    """,
                },
                {
                    "agent": "stock_data_agent",
                    "instructions": """
                            Use this collaborator for finding price history for specific stocks.
                    """,
                },
                {
                    "agent": "analyst_agent",
                    "instructions": """
                            Use this collaborator for taking the raw research—including news, stock data, 
                            and sentiment analysis—and writing a detailed report with investment considerations.
                    """,
                },
            ],
            collaborator_objects=[news_agent, stock_data_agent, analyst_agent],
            guardrail=no_bitcoin_guardrail,
            llm="us.anthropic.claude-3-5-sonnet-20241022-v2:0",
            verbose=False,
        )

        if args.recreate_agents == "false":
            result = portfolio_assistant.invoke_with_tasks(
                [news_task, stock_data_task, analysis_task],
                processing_type="sequential",
                enable_trace=True,
                trace_level=args.trace_level,
            )
            print(result)

            # now demonstrate using the same supervisor directly with an overall task expressed
            # as a single request.
            print("\n\n***************************\n")
            print(
                "Now demonstrating using the same supervisor directly with an overall task expressed as a single request.\n\n"
            )

            request = f"""
                Analyze the news and stock trends for both GOOG and AMZN. Provide a clear analysis 
                of investment prospects for each, and give a final set of considerations on the 
                tradeoffs of potential investments. """
            request = "what's AMZN stock price doing over the last week and relate that to recent news"
            print(f"Request:\n{request}\n")

            result = portfolio_assistant.invoke(
                request,
                enable_trace=True,
                trace_level=args.trace_level,
            )
            print(f"Final answer:\n{result}")

        else:
            print("Recreated agents.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recreate_agents",
        required=False,
        default='true',
        help="False if reusing existing agents.",
    )
    parser.add_argument(
        "--kb_s3_bucket",
        required=False,
        help="S3 bucket used for the knowledge base source.",
    )
    parser.add_argument(
        "--ticker", required=False, default="AMZN", help="The stock ticker to analyze"
    )
    parser.add_argument(
        "--trace_level",
        required=False,
        default="core",
        help="The level of trace, 'core', 'outline', 'all'.",
    )
    parser.add_argument(
        "--clean_up",
        required=False,
        default="false",
        help="Cleanup all infrastructure.",
    )
    args = parser.parse_args()
    main(args)
