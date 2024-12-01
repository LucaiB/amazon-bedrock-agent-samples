# Devops Agent

## Introduction

In this repository, we will create a Dev Ops Agent that allows you to communicate with a grafana dashboard and github repositories. We will create 2 sub-agent: Grafana assistant and Github assistant, and we will orchestrate between those agents using a supervisor multi-agent. The architecture will look as following:

[architecure](/src/examples/amazon-bedrock-multi-agent-collaboration/devops_agent/architecure.png)

## Get Started

```bash
├── 01_create_grafana_assistant/01_create_grafana_assistant.ipynb
├── 02_Create_GitHub_Assistant_Agent/02_create_github_assistant.ipynb
├── 03_Create_Supervisor_Devops_Agent/03_create_supervisor_devops_agent.ipynb
└── invoke_agent.ipynb
```

## License

This project is licensed under the Apache-2.0 License.