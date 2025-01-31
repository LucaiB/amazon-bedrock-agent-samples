# Creating Agent with Knowledge Base and an Action Group connection

In this folder, we provide an example of creating an agent with Amazon Bedrock and integrating it with a 
Knowledge Base for Amazon Bedrock and with an Action Group. 
With this integration, the agent will be able to respond to a user query by taking a sequence of actions, 
consulting the knowledge base to obtain more information, and/or executing tasks using the lambda function 
connected with an Action Group.

## Agent Architecture

This agent contains instructions on how to install and to do maintenance on Solar Panels, where customers can ask the agent to return these information from an [Amazon Bedrock Knowledge Base](https://aws.amazon.com/bedrock/knowledge-bases/).

![architecture](./img/solar_panel_agent.png)
