<h2 align="center">Amazon Bedrock Agent Samples&nbsp;</h2>
<p align="center">
  :wave: :wave: Welcome to the Amazon Bedrock Agent Samples repository :wave: :wave:
</p>

This repository provides examples and best practices for working with [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/). 

🔄 **Actively Maintained**: This repository is regularly updated to include the latest Amazon Bedrock Agent features and functionalities.🔄

![architecture](https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop/blob/main/img/architecture.gif?raw=true)

<p align="center">
  <a href="/src/examples/amazon-bedrock-multi-agent-collaboration/00_hello_world_agent/"><img src="https://img.shields.io/badge/Example-00_Hello_World_Agent-blue" /></a>
</p>

## �� Table of Contents ��

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Amazon Bedrock Multi-agent collaboration examples](#amazon-bedrock-multi-agent-collaboration-examples)
- [Amazon Bedrock Agents examples](#amazon-bedrock-agents-examples)
- [Best Practices](#best-practices)
- [Security](#security)
- [License](#license)

## Overview

Amazon Bedrock Agents enables you to create AI-powered assistants that can perform complex tasks and interact with various APIs and services. 

This repository provides practical examples to help you understand and implement agentic solutions.

The solutions presented here use the [boto3 SDK in Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html), however, you can create Bedrock Agents solutions using any of the AWS SDKs for [C++](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-bedrock-agent/html/annotated.html), [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/bedrockagent/), [Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/bedrockagent/package-summary.html), [JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/bedrock-agent/), [Kotlin](https://sdk.amazonaws.com/kotlin/api/latest/bedrockagent/index.html), [.NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/BedrockAgent/NBedrockAgent.html), [PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.BedrockAgent.html), [Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/BedrockAgent.html), [Rust](https://docs.rs/aws-sdk-bedrockagent/latest/aws_sdk_bedrockagent/), [SAP ABAP](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/bdr/index.html) or [Swift](https://sdk.amazonaws.com/swift/api/awsbedrockruntime/0.34.0/documentation/awsbedrockruntime)

## Repository Structure

```bash
├── src/examples/amazon-bedrock-multi-agent-collaboration/
│   ├── devops_agent/
│   ├── energy_efficiency_management_agent/
│   ├── startup_advisor_agent/
|   └── ....
├── src/examples/amazon-bedrock-agents/
│   ├── devops_agent/
│   ├── energy_efficiency_management_agent/
│   ├── startup_advisor_agent/
|   └── ....
├── src/shared
│   ├── file_store/
│   ├── stock_data/
│   ├── web_search/
|   └── ....
├── src/utils
│   ├── bedrock_agent_helper.py
|   ├── bedrock_agent.py
|   └── ....
```

- [src/examples/amazon-bedrock-multi-agent-collaboration/](/src/examples/amazon-bedrock-multi-agent-collaboration/): Shows Amazon Bedrock Multi-agent collaboration examples.

- [src/examples/amazon-bedrock-agent/](/src/examples/amazon-bedrock-agent/): Shows Amazon Bedrock Agents examples.

- [src/shared](/src/shared/): This module consists of shared tools that connect to Amazon Bedrock Agents via Action Groups. They provide functionality like [web search](/src/shared/file_store/), [file storage](/src/shared/file_store/), and [stock data lookup](/src/shared/stock_data/).

- [src/utils](/src/utils/): This module contains utilities for building and using various Amazon Bedrock features.

## Getting Started

1. Navigate to [`src/`](/src/) for more details.
2. To get started navigate to the example you want to deploy in [`src/examples/*`](/src/examples/) directory. 
3. Follow the deployment steps in the `src/examples/*/*/README.md` file of the example. 

## Amazon Bedrock Multi-agent collaboration examples

- [00_hello_world_agent](/src/examples/00_hello_world_agent/)
- [DevOps Agent](/src/examples/devops_agent/)
- [Energy Efficiency Management Agent](/src/examples/energy_efficiency_management_agent/)
- [Portfolio Assistant Agent](/src/examples/portfolio_assistant_agent/)
- [Startup Advisor Agent](/src/examples/startup_advisor_agent/)
- [Team Poems Agent](/src/examples/team_poems_agent/)
- [Trip Planner Agent](/src/examples/trip_planner_agent/)
- [Voyage Virtuso Agent](/src/examples/voyage_virtuoso_agent/)

## Amazon Bedrock Agents examples

- [Booking Agent using AWS CDK](/src/examples/amazon-bedrock-agents/booking_cdk_agent/)
- [Code Assistant Agent using code Interpretation](/src/examples/amazon-bedrock-agents/code_assistant_agent/)
- [Human Resource Agent using return of control and user confirmation](/src/examples/amazon-bedrock-agents/human_resources_agent/)
- [Configure an inline agent at runtime](/src/examples/amazon-bedrock-agents/inline_agent/)
- [Insurance Claim Agent using OpenAPI schema](/src/examples/amazon-bedrock-agents/insurance_claims_agent/)
- [Online Banking Agent using Amazon Bedrock Guardrails](/src/examples/amazon-bedrock-agents/online_banking_agent/)
- [Restaurant Booking Agent using Amazon Bedrock Knowledge Bases](/src/examples/amazon-bedrock-agents/restaurant_agent/)
- [Restaurant Booking Agent using custom orchestration](/src/examples/amazon-bedrock-agents/restaurant_booking_custom_orchestration_agent/)
- [Restaurant Booking Agent using non-optimized models](/src/examples/amazon-bedrock-agents/restaurant_booking_mistral_agent/)
- [Travel Assistant Agent with memory](/src/examples/amazon-bedrock-agents/travel_assistant_agent/)

## Best Practices

The code samples highlighted in this repository focus on showcasing different Amazon Bedrock Agents capabilities.

Please check out our two-part blog series for best practices around building generative AI applications with Amazon Bedrock Agents: 

- [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)


🔗 **Related Links**:

- [Amazon Bedrock Agents Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Boto3 Python SDK Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html)
- [Amazon Bedrock Samples](https://github.com/aws-samples/amazon-bedrock-samples/tree/main)


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.

> [!IMPORTANT]
> Examples in this repository are for demonstration purposes. 
> Ensure proper security and testing when deploying to production environments.