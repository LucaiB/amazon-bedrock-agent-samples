# Sports Team Poet Agent

This is a fun example for sports fans. The Sports Team Poet is a supervisor with a Sports Researcher and a Sports Poetry Writer. Pick your favorite team (go Celtics!) and see multi-agents collaborate to conduct web search about your team and make a fun poem with those insights. Have fun!

![architecture](/examples/amazon-bedrock-multi-agent-collaboration/team_poems_agent/architecture.png)


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

## Usage & Sample Prompts

1. Deploy Amazon Bedrock Agents

```bash
python3 examples/amazon-bedrock-multi-agent-collaboration/team_poems_agent/main.py \
--recreate_agents "true"
```

2. Invoke

```bash
python3 examples/amazon-bedrock-multi-agent-collaboration/team_poems_agent/main.py \
--recreate_agents "false" \
--team_name "New England Patriots"
```

3. Cleanup

```bash
python3 examples/amazon-bedrock-multi-agent-collaboration/team_poems_agent/main.py \
--clean_up "true"
```

## License

This project is licensed under the Apache-2.0 License.