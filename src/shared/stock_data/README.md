# Stock Data Lookup Tool

This tool consists of an AWS Lambda function named "stock_data_lookup" to retrieve stock data using the yfinance Python library. The "stock_data_lookup" Lambda function can then be invoked to retrieve stock data for a given ticker symbol. Here's a breakdown:

- **AgentLambdaFunction**: This is the AWS Lambda function that implements the "stock_data_lookup" functionality. It uses the Python 3.11 runtime and attaches two layers: a custom layer, and the AWSSDKPandas layer managed by AWS.
- **AgentLambdaRole**: This is an AWS Identity and Access Management (IAM) role that grants the Lambda function the necessary permissions to execute.
- **AgentAliasLambdaPermission** and **AgentLambdaPermission**: These resources grant permissions for Amazon Bedrock Agents to invoke the Lambda function.

![architecture](/src/shared/stock_data/architecture.png)

## Deploy [stock_data_stack.yaml](/src/shared/stock_data/cfn_stacks/stock_data_stack.yaml)

|   Region   | development.yaml |
| ---------- | ----------------- |
| us-east-1  | [![launch-stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=StockDataLookup&templateURL=)|
| us-west-2  | [![launch-stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=StockDataLookup&templateURL=)|


## Usage

```python
from src.utils.bedrock_agent import (
    Agent,
    region,
    account_id,
)
import uuid

stock_data_agent = Agent.direct_create(
    name="stock_data_agent",
    role="Financial Data Collector",
    goal="Retrieve accurate stock trends for a given ticker.",
    instructions="Specialist in real-time financial data extraction.",
    tool_code=f"arn:aws:lambda:{region}:{account_id}:function:stock_data_lookup",
    tool_defs=[
        {  # lambda_layers: yfinance_layer.zip, numpy_layer.zip
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
response = stock_data_agent.invoke(
    input_text="What is the stock trend for AMZN?",
    session_id: str = str(uuid.uuid1()),
    enable_trace: bool = False,
)
print(response)
```

## Clean Up

- Open the CloudFormation console.
- Select the stack `StockDataLookup` you created, then click **Delete**. Wait for the stack to be deleted.

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.s

