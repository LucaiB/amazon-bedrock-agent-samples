import os
import json
import requests


def get_git_hub_pull_requests(owner, repo):
    url = "https://api.github.com/repos/"+owner+"/"+repo+"/pulls"
    print(url)
    token = os.environ.get("github_token")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers)
    print(response.json())
    return 1


def lambda_handler(event, context):
    actionGroup = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])
    print(parameters)
    responseBody = {
        "TEXT": {
            "body": "Error, no function was called"
        }
    }
    owner = None
    repos = None
    if function == 'get_git_hub_pull_requests':
        print("found function")
        for param in parameters:
            if param["name"] == "owner":
                owner = param["value"]
            if param["name"] == "repo":
                repos = param["value"]

    if not owner:
        raise Exception("Missing mandatory parameter: owner")
    if not repos:
        raise Exception("Missing mandatory parameter: repos")
    pull_req = get_git_hub_pull_requests(owner, repos)
    responseBody = {
            'TEXT': {
                "body": f"Total pull requests : {pull_req}"
            }
        }
    action_response = {
        'actionGroup': actionGroup,
        'function': function,
        'functionResponse': {
            'responseBody': responseBody
        }

    }

    function_response = {
        'response': action_response,
        'messageVersion': event['messageVersion']
    }
    print("Response: {}".format(function_response))
    return function_response
