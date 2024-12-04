# Devops Agent

## Introduction

The DevOps assistant helps DevOps engineerings by acting as the coordinator between code changes and system status by correlating GitHub activities with real-time infrastructure metrics from Grafana. By orchestrating between these two domains, it can proactively identify potential issues (like a problematic PR that might impact system health) and suggest preventive actions, essentially providing end-to-end visibility and automated decision support across the development and operations lifecycle.

![architecure](/examples/amazon-bedrock-multi-agent-collaboration/devops_agent/architecture.png)

## Prerequisite

Make sure to provide appropriate values for [grafana.url, grafana.token, and github.token](/examples/amazon-bedrock-multi-agent-collaboration/devops_agent/devops.properties.template)


## Get Started

```bash
├── 01_create_grafana_assistant/01_create_grafana_assistant.ipynb
├── 02_Create_GitHub_Assistant_Agent/02_create_github_assistant.ipynb
├── 03_Create_Supervisor_Devops_Agent/03_create_supervisor_devops_agent.ipynb
└── invoke_agent.ipynb
```

## License

This project is licensed under the Apache-2.0 License.