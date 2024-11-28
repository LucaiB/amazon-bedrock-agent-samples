# Amazon Bedrock Utilities

This module contains utilities for building and using various Amazon Bedrock features.

## �� Table of Contents ��

- [Create and Manage Amazon Bedrock Agents](#create-and-manage-amazon-bedrock-agents)
- [Create and Manage Amazon Bedrock KnowledgeBase](#create-and-manage-amazon-bedrock-knowledgebase)
- [Create and Manage Amazon Bedrock Multi-Agent Collaboration](#create-and-manage-amazon-bedrock-multi-agent-collaboration)

## Create and Manage Amazon Bedrock Agents

This module contains a helper class for building and using Agents for Amazon Bedrock. The AgentsForAmazonBedrock class provides a convenient interface for working with Agents. It includes methods for creating, updating, and invoking Agents, as well as managing IAM roles and Lambda functions for action groups.

```python
from src.utils.bedrock_agent_helper import AgentsForAmazonBedrock

agents = AgentsForAmazonBedrock()

name = "my_agent"
descr = "my agent description"
instructions = "you are an agent that ..."
model_id = "...haiku..."

# Create Agent
agent_id = agents.create_agent(name, descr, instructions, model_id)

# Create and Associate Action Groups

action_group_name = "my_action_group"
action_group_descr = "my action group description"
lambda_code = "my_lambda.py"

function_defs = [{ ... }]

action_group_arn = agents.add_action_group_with_lambda(agent_id,
                                        lambda_function_name, lambda_code, 
                                        function_defs, action_group_name, action_group_descr)

# Invoke Agent
agents.simple_agent_invoke("when's my next payment due?", agent_id)
```

Here is a summary of the most important methods:

- create_agent: Creates a new Agent.
- add_action_group_with_lambda: Creates a new Action Group for an Agent, backed by Lambda.
- simple_invoke_agent: Invokes an Agent with a given input.

## Create and Manage Amazon Bedrock KnowledgeBase

This module contains a helper class for building and using Knowledge Bases for Amazon Bedrock. The KnowledgeBasesForAmazonBedrock class provides a convenient interface for working with Knowledge Bases. It includes methods for creating, updating, and invoking Knowledge Bases, as well as managing IAM roles and OpenSearch Serverless. Here is a quick example of using the class:

```python
from src.utils.knowledge_base_helper import KnowledgeBasesForAmazonBedrock

kb = KnowledgeBasesForAmazonBedrock()

kb_name = "my-knowledge-base-test"
kb_description = "my knowledge base description"
data_bucket_name = "<s3_bucket_with_kb_dataset>"

# Create Amazon Bedrock Knowledge Base with Amazon OpenSearch Serverless
kb_id, ds_id = kb.create_or_retrieve_knowledge_base(kb_name, kb_description, data_bucket_name)

# Ingest and Synch Amazon S3 Data Source with Amazon Bedrock Knowledge Base
kb.synchronize_data(kb_id, ds_id)
```

Here is a summary of the most important methods:

- create_or_retrieve_knowledge_base: Creates a new Knowledge Base or retrieves an existent one.
- synchronize_data: Syncronize the Knowledge Base with the

## Create and Manage Amazon Bedrock Multi-Agent Collaboration

Check out `Hello World` example [here](/src/examples/00_hello_world_agent/).

```python
from src.utils.bedrock_agent import Agent, SupervisorAgent, Task

# Create a Sub-Agent
hello_world_sub_agent = Agent.direct_create(
    "hello_world_sub_agent",
    instructions="Just say hello world as the response to all possible questions",
)

# Create a Supervisor Agent
hello_world_supervisor = SupervisorAgent.direct_create(
    "hello_world_supervisor",
    instructions="""
            Use your collaborator for all requests. Always pass its response back to the user.
            Ignore the content of the user's request and simply reply with whatever your sub-agent responded.""",
    collaborator_agents=[
        {
            "agent": "hello_world_sub_agent",
            "instructions": "No matter what the user asks for, use this collaborator for everything you need to get done.",
        }
    ],
    collaborator_objects=[hello_world_sub_agent],
)
```