# Provide conversation history to Amazon Bedrock Agents

In this [module](./conversation_history.ipynb), we will create an Amazon Bedrock Agent and understand how to initialize the Agent with Conversation History. This feature enables you to continue a conversation with an Agent even if the session has expired. Additionally, we will explore the benefits of overriding Conversation History at each turn of Agent invocation, which can lead to lower latency and reduced cost. 

In this example we will create a restaurant assistant agent that connects with a Knowledge Base for Amazon Bedrock containing the restaurant's different menus. This agent also connects to an action group that provides functionalities for handling the table booking in this restaurant.

![architecture](./architecture.png)

## Conversation History - Usage

The `conversationHistory` can be passed into the sessionState parameter of the invokeAgent API in the following format:

```python
sessionState={
    'conversationHistory': {
        'messages': [
            {
                'content': [
                    {
                        'text': 'string'
                    },
                ],
                'role': 'user'|'assistant'
            },
            // Additional message objects...
        ]
    },
}
```

Each item in the messages array represents a single turn in the conversation, where the content field contains the message text, and the role field specifies whether the message is from the 'user' or the 'assistant'. Passing the conversationHistory in the sessionState appends the provided messages to existing messages in the current session.

## Conversation History - Example

```python
import uuid
import boto3

# Make sure boto3 is updated to latest version
bedrock_agent_runtime_client = boto3.client("bedrock-agent-runtime")

# Start a new sesssion
session_id:str = str(uuid.uuid1())

# Agent details
agent_id = "XXXXXX"
alias_id = "XXXXXX"

# User query
query = "Can you get information about the most recent booking?"

# Stored conversation history from past interactions
conversation_history = [
    {
        "content": [{"text": """
            Excellent, Anna! I've successfully created a booking for you. Here are the details:
                - Booking ID: 68bc08cf
                - Date: May 5, 2024
                - Time: 8:00 PM
                - Number of guests: 2
                - Name: Anna
            Your reservation is confirmed. 
            Is there anything else you'd like to know about your booking?
        """}], "role": "assistant"
    },
    {
        "content": [{"text": "Hi, I am Anna. I want to create a booking for 2 people, at 8pm on the 5th of May 2024."}], "role": "user"
    },
    {
        "content": [{"text": """
            According to the knowledge base, the children's menu at The Regrettable Experience does not have a separate "starters" section. However, some of the entree options could be considered starters or appetizers, such as:
                
                - Chicken nuggets (allergens: gluten, possible soy)
                - Macaroni and cheese (allergens: dairy, gluten)  
                - Mini cheese quesadillas (allergens: dairy, gluten)
                - Peanut butter and banana sandwich (allergens: nuts, gluten)
                - Veggie pita pockets (allergens: gluten, possible soy)
                - Mini cheeseburgers (allergens: dairy, gluten)
                - Fish sticks (allergens: gluten, possible soy)
                - Grilled cheese sandwich (allergens: dairy, gluten)
                - Spaghetti with marinara sauce (allergens: gluten)
        """}], "role": "assistant"
    },
    {
        "content": [{"text": "What are the starters in the childrens menu?"}], "role": "user"
    },
]

# Invoke the agent with conversation history
agentResponse = bedrock_agent_runtime_client.invoke_agent(
        inputText=query,
        agentId=agent_id,
        agentAliasId=alias_id,
        sessionId=session_id,
        enableTrace=False,
        endSession=False,
        sessionState={'conversationHistory': {'messages': conversation_history}}
    )

# Process the agent response stream
event_stream = agentResponse['completion']
agent_answer = str()

try:
    for event in event_stream:        
        if 'chunk' in event:
            data = event['chunk']['bytes']
            agent_answer = data.decode('utf8')
except Exception as e:
    raise Exception("unexpected event.", e)

print(agent_answer)

# Insert into conversation history
conversation_history.insert(0, {"content": [{"text": query}], "role": "user"})
conversation_history.insert(0, {"content": [{"text": response}], "role": "assistant"})
```

## License

This project is licensed under the Apache-2.0 License.