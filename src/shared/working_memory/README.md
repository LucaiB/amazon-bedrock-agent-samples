# Working Memory Tool

![architecture](/src/shared/working_memory/architecture.png)

## Deploy [working_memory_stack.yaml](/src/shared/working_memory/cfn_stacks/working_memory_stack.yaml)

|   Region   | development.yaml |
| ---------- | ----------------- |
| us-east-1  | [![launch-stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=WorkingMemory&templateURL=)|
| us-west-2  | [![launch-stack](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=WorkingMemory&templateURL=)|

## Usage

For a detailed example checkout [startup_advisor_agent](/examples/amazon-bedrock-multi-agent-collaboration/startup_advisor_agent/)

## Clean Up

- Open the CloudFormation console.
- Select the stack `WorkingMemory` you created, then click **Delete**. Wait for the stack to be deleted.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.

