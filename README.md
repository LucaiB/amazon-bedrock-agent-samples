<h2 align="center">Amazon Bedrock Agent Samples&nbsp;</h2>
<p align="center">
  :wave: :wave: Welcome to the Amazon Bedrock Agent Samples repository :wave: :wave:
</p>

This repository provides examples and best practices for working with [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/). 

Amazon Bedrock Agents enables you to automate complex workflows, build robust and scalable end-to-end solutions from experimentation to production and quickly adapt to new models and experiments.

With the [multi-agent collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agents-collaboration.html) feature you can plan and execute complex tasks across different agents using the supervisor collaboration mode. As well as have an unified conversation across agents with built-in intent classification using the supervisor with routing collaboration mode and fallback to the supervisor mode when an intention cannot be detected. Amazon Bedrock Agents will provide you with traces to observe your agents behavior across multi-agent flows and with the guardrails, security and privacy that are standard across Amazon Bedrock features.

![architecture](https://github.com/awslabs/amazon-bedrock-agent-samples/blob/main/images/architecture.gif?raw=true)

<p align="center">
  <a href="/examples/amazon-bedrock-multi-agent-collaboration/startup_advisor_agent/"><img src="https://img.shields.io/badge/Example-Startup_Advisor_Agent-blue" /></a>
</p>

## �� Table of Contents ��

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Amazon Bedrock Agents examples](#amazon-bedrock-agents-examples)
- [Amazon Bedrock Multi-agent collaboration examples](#amazon-bedrock-multi-agent-collaboration-examples)
- [Best Practices](#best-practices)
- [Security](#security)
- [License](#license)

## Overview

Amazon Bedrock Agents enables you to create AI-powered assistants that can perform complex tasks and interact with various APIs and services. 

This repository provides practical examples to help you understand and implement agentic solutions.

The solutions presented here use the [boto3 SDK in Python](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html), however, you can create Bedrock Agents solutions using any of the AWS SDKs for [C++](https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-bedrock-agent/html/annotated.html), [Go](https://docs.aws.amazon.com/sdk-for-go/api/service/bedrockagent/), [Java](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/bedrockagent/package-summary.html), [JavaScript](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/bedrock-agent/), [Kotlin](https://sdk.amazonaws.com/kotlin/api/latest/bedrockagent/index.html), [.NET](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/BedrockAgent/NBedrockAgent.html), [PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/namespace-Aws.BedrockAgent.html), [Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/BedrockAgent.html), [Rust](https://docs.rs/aws-sdk-bedrockagent/latest/aws_sdk_bedrockagent/), [SAP ABAP](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/bdr/index.html) or [Swift](https://sdk.amazonaws.com/swift/api/awsbedrockruntime/0.34.0/documentation/awsbedrockruntime)

## Repository Structure

```bash
├── examples/amazon-bedrock-agents/
│   ├── code_assistant_agent/
│   ├── human_resources_agent/
│   ├── inline_agent/
|   └── ....
├── examples/amazon-bedrock-multi-agent-collaboration/
│   ├── 00_hello_world_agent/
│   ├── devops_agent/
│   ├── energy_efficiency_management_agent/
|   └── ....
├── src/shared
│   ├── working_memory/
│   ├── stock_data/
│   ├── web_search/
|   └── ....
├── src/utils
│   ├── bedrock_agent_helper.py
|   ├── bedrock_agent.py
|   ├── knowledge_base_helper.py
|   └── ....
```

- [examples/amazon-bedrock-agent/](/examples/amazon-bedrock-agent/): Shows Amazon Bedrock Agents examples.

- [examples/amazon-bedrock-multi-agent-collaboration/](/examples/amazon-bedrock-multi-agent-collaboration/): Shows Amazon Bedrock Multi-agent collaboration examples.

- [src/shared](/src/shared/): This module consists of shared tools that connect to Amazon Bedrock Agents via Action Groups. They provide functionality like [Web Search](/src/shared/file_store/), [Working Memory](/src/shared/working_memory/), and [Stock Data Lookup](/src/shared/stock_data/).

- [src/utils](/src/utils/): This module contains utilities for building and using various Amazon Bedrock features, providing a higher level of abstraction than the underlying APIs.

## Getting Started

1. Navigate to [`src/`](/src/) for more details.
2. To get started, navigate to the example you want to deploy in the [`examples/*`](/examples/) directory. 
3. Follow the deployment steps in the `examples/*/*/README.md` file of the example. 

## Amazon Bedrock Agents examples

- [Code Assistant Agent using code Interpretation](/examples/amazon-bedrock-agents/code_assistant_agent/)
- [Human Resource Agent using return of control and user confirmation](/examples/amazon-bedrock-agents/human_resources_agent/)
- [Configure an inline agent at runtime](/examples/amazon-bedrock-agents/inline_agent/)
- [Insurance Claim Agent using OpenAPI schema](/examples/amazon-bedrock-agents/insurance_claims_agent/)
- [Online Banking Agent using Amazon Bedrock Guardrails](/examples/amazon-bedrock-agents/online_banking_agent/)
- [Restaurant Booking Agent using Amazon Bedrock Knowledge Bases](/examples/amazon-bedrock-agents/restaurant_agent/)
- [Restaurant Booking Agent using AWS CDK](/examples/amazon-bedrock-agents/booking_cdk_agent/)
- [Restaurant Booking Agent using custom orchestration](/examples/amazon-bedrock-agents/restaurant_booking_custom_orchestration_agent/)
- [Restaurant Booking Agent using non-optimized models](/examples/amazon-bedrock-agents/restaurant_booking_mistral_agent/)
- [Travel Assistant Agent with memory](/examples/amazon-bedrock-agents/travel_assistant_agent/)

## Amazon Bedrock Multi-agent collaboration examples

- [00_hello_world_agent](/examples/amazon-bedrock-multi-agent-collaboration/00_hello_world_agent/)
- [DevOps Agent](/examples/amazon-bedrock-multi-agent-collaboration/devops_agent/)
- [Energy Efficiency Management Agent](/examples/amazon-bedrock-multi-agent-collaboration/energy_efficiency_management_agent/)
- [Portfolio Assistant Agent](/examples/amazon-bedrock-multi-agent-collaboration/portfolio_assistant_agent/)
- [Startup Advisor Agent](/examples/amazon-bedrock-multi-agent-collaboration/startup_advisor_agent/)
- [Team Poems Agent](/examples/amazon-bedrock-multi-agent-collaboration/team_poems_agent/)
- [Trip Planner Agent](/examples/amazon-bedrock-multi-agent-collaboration/trip_planner_agent/)
- [Voyage Virtuso Agent](/examples/amazon-bedrock-multi-agent-collaboration/voyage_virtuoso_agent/)

## Best Practices

The code samples highlighted in this repository focus on showcasing different Amazon Bedrock Agents capabilities.

Please check out our two-part blog series for best practices around building generative AI applications with Amazon Bedrock Agents: 

- [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [Best practices for building robust generative AI applications with Amazon Bedrock Agents – Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)


🔗 **Related Links**:

- [Amazon Bedrock Agents Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Amazon Bedrock Multi-Agent Collaboration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agents-collaboration.html)
- [Boto3 Python SDK Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-agent.html)
- [Amazon Bedrock Samples](https://github.com/aws-samples/amazon-bedrock-samples/tree/main)


## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.

> [!IMPORTANT]
> Examples in this repository are for demonstration purposes. 
> Ensure proper security and testing when deploying to production environments.