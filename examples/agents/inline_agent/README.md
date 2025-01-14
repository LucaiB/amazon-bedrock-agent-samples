# Inline Agents

In this folder, we’ll walk through the process of setting up and invoking an inline agent, showcasing its flexibility and power in creating dynamic AI assistants. By following our progressive approach, you will gain a comprehensive understanding of how to use inline agents for various use cases and complexity levels. Throughout a single interactive conversation, we will demonstrate how the agent can be enhanced on the fly with new tools and instructions while maintaining context of our ongoing discussion.

## What are Inline Agents?
Inline agents are a powerful feature of Amazon Bedrock that allow developers to create flexible and adaptable AI assistants.
Unlike traditional static agents, inline agents can be dynamically configured at runtime, enabling real time adjustments to their behavior, capabilities, and knowledge base.
Key features of inline agents include:
* **Dynamic configuration**: Modify the agent’s instructions, action groups, and other parameters on the fly.
* **Flexible integration**: Easily incorporate external APIs and services as needed for each interaction.
* **Contextual adaptation**: Adjust the agent’s responses based on user roles, preferences, or specific scenarios.

## Why Use Inline Agents?
Inline agents offer several advantages for building AI applications:
* **Rapid prototyping**: Quickly experiment with different configurations without redeploying your application.
* **Personalization**: Tailor the agent’s capabilities to individual users or use cases in real time.
* **Scalability**: Efficiently manage a single agent that can adapt to multiple roles or functions.
* **Cost-effectiveness**: Optimize resource usage by dynamically selecting only the necessary tools and knowledge for each interaction.

## Use case example

For this example we will use an HR assistant use case where managers and ICs have different level of access.
