# Amazon Bedrock Multi-Agent Collaboration Examples

This repository is designed to get you started with Amazon Bedrock Multi-Agent collaboration by providing a set of examples that demonstrate how it works and showcases some of its core capabilities. The field of multi-agent systems is still in the early days, and our goal is to give you some off the shelf starter examples that inspire you as you being to tackle real world scenarios.

## Getting started

1. To get started navigate to the example you want to deploy in `src/examples/*` directory.
2. Follow the deployment steps in the `src/examples/*/README.md` file of the example.

## Examples

To get you started working with Bedrock multi-agent processes, we provide the following examples:

- **[Hello World Agent](/src/examples/00_hello_world_agent/README.md)**: This example is a great way to get started! 
- **[DevOps Agent](/src/examples/devops_agent/README.md)**: In this repository, we will create a Dev Ops Agent that allows you to communicate with a grafana dashboard and github repositories. We will create 2 sub-agent: Grafana assistant and Github assistant, and we will orchestrate between those agents using a supervisor multi-agent.
- **[Energy Efficiency Management Agent](/src/examples/energy_efficiency_management_agent/README.md)**: This example showcases [Amazon Bedrock Multi-agent collaboration capabilities](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agents-collaboration.html) through an Energy Efficiency Management System. The system consists of a supervisor agent that orchestrates three specialized sub-agents, each handling specific aspects of energy management ansd customer service.
- **[Portfolio Assistant Agent](/src/examples/portfolio_assistant_agent/README.md)** Stock Analysis supervisor agent has three collaborators, a News agent, a Stock Data agent, and a Financial Analyst agent. These specialists are orchestrated to perform investment analysis for a given stock ticker based on the latest news and recent stock price movements.
- **[Startup Advisor Agent](/src/examples/startup_advisor_agent/README.md)** Have a new startup in mind, but haven't quite hired your marketing staff? Use this Startup Advisrt agent to do your market research, come up with campaign ideas, and write effective campaign copy. It uses a set of 5 sub-agents to get the job done these include Lead Market Analyst, Content Creator, Chief Conent Creator, Chief Stategist, and Agent Storage Manager.
- **[Sports Team Poet Agent](/src/examples/team_poems_agent/README.md)** This is a fun example for sports fans. The Sports Team Poet is a supervisor with a Sports Researcher and a Sports Poetry Writer. Pick your favorite team (go Celtics!) and see multi-agents collaborate to conduct web search about your team and make a fun poem with those insights. Have fun!
- **[Trip Planner Agent](/src/examples/trip_planner_agent/README.md)** The Trip Planner uses three sub-agents to help you build a robust itinerary. It leverages a Restaurant Scout and an Activity Finder to get great ideas, and an Intinerary Compiler to finish the job. Try it out for your next trip.
- **[Voyage Vituoso Agent](/src/examples/voyage_virtuoso_agent/README.md)** Dream big with the Voyage Virtuoso, a supervisor agent that is built for high net worth individuals that need help picking the most expensive and elaborate destinations given a theme ("I want to ski on expert slopes, but need ski-on/ski-off resort with great night life").