# Create Agents with Custom Orchestration

In this folder, we provide an example of creating an agent with custom orchestration.

[Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/) streamlines the development of generative AI applications 
by offering a fully managed solution that uses [foundation models (FMs)](https://aws.amazon.com/what-is/foundation-models/) and augmenting tools to autonomously run tasks and 
achieve objectives through orchestrated, multistep workflows. Using the default orchestration strategy, [reasoning and 
action (ReAct)](https://arxiv.org/abs/2210.03629), users can quickly build and deploy agentic solutions. ReAct is a general problem-solving approach that 
uses the FM’s planning capabilities to dynamically adjust actions at each step. Although ReAct offers flexibility by 
allowing agents to continually reevaluate their decisions based on shifting requirements, its iterative approach can lead 
to higher latency when many tools are involved.

For greater orchestration control, Amazon Bedrock Agents has launched the 
[custom orchestrator](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-custom-orchestration.html) feature, which users can 
use to fine-tune agent behavior and manage tool interactions at each workflow step. This customization allows organizations 
to tailor agent functionality to their specific operational needs, improving precision, adaptability, and efficiency. 


In this folder we provide a reasoning without observation ([ReWoo](https://arxiv.org/abs/2305.18323)) orchestration example.

## Agent Architecture

For this example we will use the restaurant assistant agent that connects with an Amazon Bedrock Knowledge Base and an Amazon DynamoDB as can be seen in the architecture below:

![architecture](./images/architecture.png)

We will then compare the agent with a default ReAct orchestrator with the agent using custom orchestrator to implement ReWoo.

For more information about the custom orchestrator functionality, check out our [blog post](https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-bedrock-agents-custom-orchestrator/)
