# Trip Planner Agent

The Trip Planner uses three sub-agents to help you build a robust itinerary. It leverages a Restaurant Scout and an Activity Finder to get great ideas, and an Intinerary Compiler to finish the job. Try it out for your next trip.

![architecture](./architecture.png)

## Prerequisites

1. Clone and install repository

```bash
git clone https://github.com/awslabs/amazon-bedrock-agent-samples

cd amazon-bedrock-agent-samples

python3 -m venv .venv

source .venv/bin/activate

pip3 install -r src/requirements.txt
```

2. Deploy Web Search tool

Follow instructions [here](/src/shared/web_search/).

3. Deploy Working Memory tool

Follow instructions [here](/src/shared/working_memory/).

## Usage & Sample Prompts

1. Deploy Amazon Bedrock Agents

```bash
python3 examples/multi_agent_collaboration/trip_planner_agent/main.py --recreate_agents "true"
```

2. Invoke

```bash
python3 examples/multi_agent_collaboration/trip_planner_agent/main.py --recreate_agents "false"
```

3. Cleanup

```bash
python3 examples/multi_agent_collaboration/trip_planner_agent/main.py --clean_up "true"
```

## License

This project is licensed under the Apache-2.0 License.
