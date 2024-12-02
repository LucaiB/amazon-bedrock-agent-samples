#!/usr/bin/env python

# Copyright 2024 Amazon.com and its affiliates; all rights reserved.
# This file is AWS Content and may not be duplicated or distributed without permission
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent.parent))

import datetime
import traceback
import argparse
import yaml
import os

from src.utils.bedrock_agent import Agent, SupervisorAgent, Task, region, account_id, agents_helper

current_dir = os.path.dirname(os.path.abspath(__file__))
task_yaml_path = os.path.join(current_dir, "tasks.yaml")
agent_yaml_path = os.path.join(current_dir, "agents.yaml")


def create_agent(agent_name, agent_content, tools=None):
    agent = Agent(agent_name, agent_content, tools)
    print(f"Created agent: {agent_name}")
    return agent


def main(args):
    if args.recreate_agents == "false":
        Agent.set_force_recreate_default(False)
    else:
        Agent.set_force_recreate_default(True)
        agents_helper.delete_agent(agent_name="trip_planner", delete_role_flag=True, verbose=True)

    if args.clean_up == "true":        
        agents_helper.delete_agent(agent_name="trip_planner", delete_role_flag=True, verbose=True)
        agents_helper.delete_agent(agent_name="itinerary_compiler", delete_role_flag=True, verbose=True)
        agents_helper.delete_agent(agent_name="activity_finder", delete_role_flag=True, verbose=True)
        agents_helper.delete_agent(agent_name="restaurant_scout", delete_role_flag=True, verbose=True)
    else:
        inputs = {
            "origin": args.origin,
            "destination": args.destination,
            "age": args.age,
            "hotel_location": args.hotel_location,
            "arrival": args.arrival,
            "departure": args.departure,
        }

        with open(task_yaml_path, "r") as file:
            yaml_task_content = yaml.safe_load(file)

        activity_planning_task = Task("activity_planning_task", yaml_task_content, inputs)
        restaurant_scout_task = Task("restaurant_scout_task", yaml_task_content, inputs)
        itinerary_compilation_task = Task(
            "itinerary_compilation_task", yaml_task_content, inputs
        )

        with open(agent_yaml_path, "r") as file:
            yaml_agent_content = yaml.safe_load(file)

        activity_finder = Agent(
            "activity_finder",
            yaml_agent_content,
            tool_code=f"arn:aws:lambda:{region}:{account_id}:function:web_search",
            tool_defs=[
                {
                    "name": "web_search",
                    "description": "Searches the web for information",
                    "parameters": {
                        "search_query": {
                            "description": "The query to search the web with",
                            "type": "string",
                            "required": True,
                        },
                        "target_website": {
                            "description": "The specific website to search including its domain name. If not provided, the most relevant website will be used",
                            "type": "string",
                            "required": False,
                        },
                        "topic": {
                            "description": "The topic being searched. 'news' or 'general'. Helps narrow the search when news is the focus.",
                            "type": "string",
                            "required": False,
                        },
                        "days": {
                            "description": "The number of days of history to search. Helps when looking for recent events or news.",
                            "type": "string",
                            "required": False,
                        },
                    },
                }
            ],
        )
        restaurant_scout = Agent(
            "restaurant_scout",
            yaml_agent_content,
            tool_code=f"arn:aws:lambda:{region}:{account_id}:function:web_search",
            tool_defs=[
                {
                    "name": "web_search",
                    "description": "Searches the web for information",
                    "parameters": {
                        "search_query": {
                            "description": "The query to search the web with",
                            "type": "string",
                            "required": True,
                        },
                        "target_website": {
                            "description": "The specific website to search including its domain name. If not provided, the most relevant website will be used",
                            "type": "string",
                            "required": False,
                        },
                        "topic": {
                            "description": "The topic being searched. 'news' or 'general'. Helps narrow the search when news is the focus.",
                            "type": "string",
                            "required": False,
                        },
                        "days": {
                            "description": "The number of days of history to search. Helps when looking for recent events or news.",
                            "type": "string",
                            "required": False,
                        },
                    },
                }
            ],
        )
        itinerary_compiler = Agent("itinerary_compiler", yaml_agent_content)

        print("\n\nCreating supervisor agent...\n\n")
        trip_planner = SupervisorAgent(
            "trip_planner",
            yaml_agent_content,
            [activity_finder, restaurant_scout, itinerary_compiler],
        )

        if args.recreate_agents == "false":
            print("\n\nInvoking supervisor agent...\n\n")

            time_before_call = datetime.datetime.now()
            print(f"time before call: {time_before_call}\n")
            try:
                print(
                    trip_planner.invoke_with_tasks(
                        [
                            activity_planning_task,
                            restaurant_scout_task,
                            itinerary_compilation_task,
                        ],
                        additional_instructions="For the final response, please only return the final itinerary.",
                        processing_type="sequential",
                        enable_trace=True,
                        trace_level=args.trace_level,
                    )
                )
            except Exception as e:
                print(e)
                traceback.print_exc()
                pass

            duration = datetime.datetime.now() - time_before_call
            print(f"\nTime taken: {duration.total_seconds():,.1f} seconds")

        else:
            print("Recreated agents.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--recreate_agents",
        required=False,
        default="true",
        help="False if reusing existing agents.",
    )
    parser.add_argument(
        "--trace_level",
        required=False,
        default="core",
        help="The level of trace, 'core', 'outline', 'all'.",
    )
    parser.add_argument(
        "--clean_up",
        required=False,
        default="false",
        help="Cleanup all infrastructure.",
    )
    parser.add_argument(
        "--origin",
        required=False,
        default="Boston, BOS",
        help="Origin of the trip.",
    )
    parser.add_argument(
        "--destination",
        required=False,
        default="New York, JFK",
        help="Destination of the trip..",
    )
    parser.add_argument(
        "--age",
        required=False,
        default="25",
        help="Age of the traveller.",
    )
    parser.add_argument(
        "--hotel_location",
        required=False,
        default="Times Square",
        help="Preferred Hotel location.",
    )
    parser.add_argument(
        "--arrival",
        required=False,
        default="Dec 26, 11:00",
        help="Preferred arrival time.",
    )
    parser.add_argument(
        "--departure",
        required=False,
        default="Jan 1, 17:00",
        help="Preferred departure time.",
    )
    args = parser.parse_args()

    main(args)
