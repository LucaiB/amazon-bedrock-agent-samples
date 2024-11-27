<h2 align="center">Amazon Bedrock Multi-Agent Collaboration&nbsp;</h2>

Amazon Bedrock multi-agent collaboration enables unfied conversational experiences as well as new ways to deliver complex process automation. Customers now have a modular, secure, and scalable way to leverage a collection of specialized AI agents to adress more complicated scenarios. Development teams can independently build AI agents with deep expertise at a very specific set of outcomes, and these agents can be flexibly assembled into a multi-agent nsystem to execute a set of tasks. Supervisor agents dynamically plan and execute across their available collaborators and knowledge bases, completing complex requests. This addresses the scalability challenges of single-agent systems by allowing greater accuracy without the complexity associated with more complicated coding and prompt engineering. Multi-level agent hierarchies are also supported, and agent processing can be both sequential and parallel. Bedrock agent tracing gives you the transparency needed for auditing and troubleshooting multi-agent flows by giving step by step information about the chain of agent calls, and the inputs and outputs to every sub-agent and tool along the way.

## �� Table of Contents ��

- [Prerequisites](#prerequisites)
- [Build Amazon Bedrock Multi-Agent Collaboration using bedrock_agent_helper.py](#build-amazon-bedrock-multi-agent-collaboration-using-boto3)
- [Build Amazon Bedrock Multi-Agent Collaboration using bedrock_agent.py](#build-amazon-bedrock-multi-agent-collaboration-using-bedrock_agent.py)

## Prerequisites

- AWS Account with Bedrock access
- Python 3.8 or later
- Required Python packages (specified in [`requirements.txt`](/requirements.txt))

Make sure to run the following commands:

```
git clone https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop

cd bedrock-multi-agents-collaboration-workshop

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r src/requirements.txt
```

> [!TIP]   
> Run the `deactivate` command to deactivate the virtual environment.

## Build Amazon Bedrock Multi-Agent Collaboration using [bedrock_agent_helper.py](/src/utils/bedrock_agent_helper.py)

<p align="center">
  <a href="/src/examples/energy_efficiency_management_agent/"><img src="https://img.shields.io/badge/Example-Energy_Efficiency_Management_Agent-blue" /></a>
  <a href="/src/examples/devops_agent/"><img src="https://img.shields.io/badge/Example-DevOps_Agent_Agent-blue" /></a>
</p>

```
from src.utils.bedrock_agent_helper import AgentsForAmazonBedrock
import uuid

agent_foundation_model = [
    'anthropic.claude-3-sonnet-20240229-v1:0',
    'anthropic.claude-3-5-sonnet-20240620-v1:0',
    'anthropic.claude-3-haiku-20240307-v1:0'
]

hello_world_sub_agent = agents.create_agent(
    agent_name="hello_world_sub_agent",
    agent_description="Hello World Agent",
    agent_instructions="Just say hello world as the response to all possible questions",
    model_ids=agent_foundation_model, # IDs of the foundation models this agent is allowed to use, the first one will be used
                                      # to create the agent, and the others will also be captured in the agent IAM role for future use
    code_interpretation=False
)

sub_agent_alias_id, sub_agent_alias_arn = agents.create_agent_alias(
    agent_id=hello_world_sub_agent[0], alias_name='v1'
)

hello_world_supervisor = agents.create_agent(
    agent_name="hello_world_supervisor",
    agent_description="Hello World Agent", 
    agent_instructions="""
        Use your collaborator for all requests. Always pass its response back to the user.
        Ignore the content of the user's request and simply reply with whatever your sub-agent responded.
    """,
    agent_foundation_model,
    agent_collaboration='SUPERVISOR_ROUTER'
)

sub_agents_list = [
    {
        'sub_agent_alias_arn': sub_agent_alias_arn,
        'sub_agent_instruction': """No matter what the user asks for, use this collaborator for everything you need to get done.""",
        'sub_agent_association_name': 'hello_world_sub_agent',
    }
]

supervisor_agent_alias_id, supervisor_agent_alias_arn = agents.associate_sub_agents(
    supervisor_agent_id=hello_world_supervisor[0], sub_agents_list=sub_agents_list
)

session_id:str = str(uuid.uuid1())

agents.invoke(
    input_text="What is Amazon Bedrock?", 
    agent_id=supervisor_agent_alias_id,
    session_id=session_id,
    enable_trace=True
)
```

## Build Amazon Bedrock Multi-Agent Collaboration using [bedrock_agent.py](/src/utils/bedrock_agent.py)

<p align="center">
  <a href="/src/examples/00_hello_world_agent/"><img src="https://img.shields.io/badge/Example-00_Hello_World_Agent-blue" /></a>
  <a href="/src/examples/devops_agent/"><img src="https://img.shields.io/badge/Example-Portfolio_Assistant_Agent-blue" /></a>
</p>


```
from src.utils.bedrock_agent import Agent, SupervisorAgent
import uuid

hello_world_sub_agent = Agent.direct_create(
    name="hello_world_sub_agent",
    instructions="Just say hello world as the response to all possible questions",
)

hello_world_supervisor = SupervisorAgent.direct_create(
    name="hello_world_supervisor",
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

session_id:str = str(uuid.uuid1())


hello_world_supervisor.invoke(
    input_text="What is Amazon Bedrock?",
    enable_trace=True,
    session_id=session_id
)
```