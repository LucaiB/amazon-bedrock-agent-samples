import os
import time
import boto3
import logging
import pprint
import json
import uuid

from knowledge_base import BedrockKnowledgeBase
from agent_utility import create_agent_role_and_policies, create_lambda_role, delete_agent_roles_and_policies
from agent_utility import create_dynamodb, create_lambda, clean_up_resources

#Clients
s3_client = boto3.client('s3')
sts_client = boto3.client('sts')
session = boto3.session.Session()
region = session.region_name
account_id = sts_client.get_caller_identity()["Account"]
bedrock_agent_client = boto3.client('bedrock-agent')
lambda_client = boto3.client('lambda')
bedrock_agent_runtime_client = boto3.client('bedrock-agent-runtime')
logging.basicConfig(format='[%(asctime)s] p%(process)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
region, account_id


suffix = str(uuid.uuid4())[:4]
agent_name = f'booking-agent-{suffix}'
knowledge_base_name = f'{agent_name}-kb-{suffix}'
knowledge_base_description = "Knowledge Base containing the restaurant menu's collection"
agent_alias_name = "booking-agent-alias"
bucket_name = f'{agent_name}-{suffix}'
agent_bedrock_allow_policy_name = f"{agent_name}-ba-{suffix}"
agent_role_name = f'AmazonBedrockExecutionRoleForAgents_{agent_name}_{suffix}'
agent_foundation_model = "anthropic.claude-3-5-sonnet-20240620-v1:0"

agent_description = "Agent in charge of a restaurants table bookings"
agent_instruction = """
You are a restaurant agent, helping clients retrieve information from their booking, 
create a new booking or delete an existing booking
"""

agent_action_group_description = """
Actions for getting table booking information, create a new booking or delete an existing booking"""

agent_action_group_name = "TableBookingsActionGroup"
lambda_function_name = f'{agent_name}-lambda-{suffix}'

table_name = f'restaurant_bookings'

agent_functions = [
    {
        'name': 'get_booking_details',
        'description': 'Retrieve details of a restaurant booking',
        'parameters': {
            "booking_id": {
                "description": "The ID of the booking to retrieve",
                "required": True,
                "type": "string"
            }
        }
    },
    {
        'name': 'create_booking',
        'description': 'Create a new restaurant booking',
        'parameters': {
            "date": {
                "description": "The date of the booking",
                "required": True,
                "type": "string"
            },
            "name": {
                "description": "Name to idenfity your reservation",
                "required": True,
                "type": "string"
            },
            "hour": {
                "description": "The hour of the booking",
                "required": True,
                "type": "string"
            },
            "num_guests": {
                "description": "The number of guests for the booking",
                "required": True,
                "type": "integer"
            }
        }
    },
    {
        'name': 'delete_booking',
        'description': 'Delete an existing restaurant booking',
        'parameters': {
            "booking_id": {
                "description": "The ID of the booking to delete",
                "required": True,
                "type": "string"
            }
        }
    },
]


def create_kb():
    knowledge_base = BedrockKnowledgeBase(
        kb_name=knowledge_base_name,
        kb_description=knowledge_base_description,
        data_bucket_name=bucket_name
    )

    def upload_directory(path, bucket_name):
            for root,dirs,files in os.walk(path):
                for file in files:
                    file_to_upload = os.path.join(root,file)
                    print(f"uploading file {file_to_upload} to {bucket_name}")
                    s3_client.upload_file(file_to_upload,bucket_name,file)
    
    upload_directory("dataset", bucket_name)

    # ensure that the kb is available
    time.sleep(30)
    # sync knowledge base
    knowledge_base.start_ingestion_job()

    kb_id = knowledge_base.get_knowledge_base_id()

    return kb_id, knowledge_base

def create_restaurant_agent(kb_id):
    create_dynamodb(table_name)

    lambda_iam_role = create_lambda_role(agent_name, table_name)
    lambda_function = create_lambda(lambda_function_name, lambda_iam_role)
    agent_role = create_agent_role_and_policies(agent_name, agent_foundation_model, kb_id=kb_id)
                                               
    response = bedrock_agent_client.create_agent(
        agentName=agent_name,
        agentResourceRoleArn=agent_role['Role']['Arn'],
        description=agent_description,
        idleSessionTTLInSeconds=1800,
        foundationModel=agent_foundation_model,
        instruction=agent_instruction,
    )
    agent_id = response['agent']['agentId']

    # Pause to make sure agent is created
    time.sleep(30)
    
    # Now, we can configure and create an action group here:
    agent_action_group_response = bedrock_agent_client.create_agent_action_group(
        agentId=agent_id,
        agentVersion='DRAFT',
        actionGroupExecutor={
            'lambda': lambda_function['FunctionArn']
        },
        actionGroupName=agent_action_group_name,
        functionSchema={
            'functions': agent_functions
        },
        description=agent_action_group_description
    )

    # Create allow to invoke permission on lambda
    response = lambda_client.add_permission(
        FunctionName=lambda_function_name,
        StatementId='allow_bedrock',
        Action='lambda:InvokeFunction',
        Principal='bedrock.amazonaws.com',
        SourceArn=f"arn:aws:bedrock:{region}:{account_id}:agent/{agent_id}",
    )

    response = bedrock_agent_client.associate_agent_knowledge_base(
        agentId=agent_id,
        agentVersion='DRAFT',
        description='Access the knowledge base when customers ask about the plates in the menu.',
        knowledgeBaseId=kb_id,
        knowledgeBaseState='ENABLED'
    )

    response = bedrock_agent_client.prepare_agent(
        agentId=agent_id
    )
    print(response)
    # Pause to make sure agent is prepared
    time.sleep(30)

    response = bedrock_agent_client.create_agent_alias(
        agentAliasName='TestAlias',
        agentId=agent_id,
        description='Test alias',
    )
    
    alias_id = response["agentAlias"]["agentAliasId"]
    print("The Agent alias is:",alias_id)
    time.sleep(30)

    return agent_id, alias_id, lambda_function, agent_action_group_response

def cleanup(agent_id, alias_id, kb_id, lambda_function, agent_action_group_response, knowledge_base):
    clean_up_resources(
        table_name, lambda_function, lambda_function_name, agent_action_group_response, agent_functions, agent_id, kb_id, alias_id
    )
    delete_agent_roles_and_policies(agent_name)
    knowledge_base.delete_kb(delete_s3_bucket=True, delete_iam_roles_and_policies=True)


