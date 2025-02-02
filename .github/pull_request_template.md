# Amazon Bedrock Agent Samples Pull Request

<!-- Do not erase any parts of this template not applicable to your Pull Request. -->
<!-- If a section does not apply to you, provide reasoning. -->

## Instructions

- Do not erase any parts of this template that are not applicable to your pull request.
- If a section is not applicable, explicitly state the reason.
- * [x] Tick the checkboxes for the items you have completed.
- These are mandatory requirements, not mere suggestions.

<hr/>

## Describe your changes

* [ ] Concise description of the PR

```
Changes to ..., because ...
```

<hr/>

## Issue ticket number and link

* [ ] Issue # (if applicable)

<hr/>

### All Submissions:

* [ ] Have you followed the guidelines in our Contributing document?
* [ ] Have you checked to ensure there aren't other open [Pull Requests](https://github.com/awslabs/amazon-bedrock-agent-samples/pulls) for the same update/change?
* [ ] Are you uploading a dataset?
* [ ] Have you added contributions to [RELEASE NOTES](/RELEASE_NOTES.md)?

<hr/>

### New Example Submissions:

* [ ] Have you tested your code, and made sure the functionality runs successfully? Provide screenshots. 
* [ ] Have you linted your Python code with [black](https://github.com/psf/black)?
* [ ] Does this implementation use the shared tools `src/utils/*`. List them here:

```
1. web_search
2. ...
```

* [ ] Does this implementation use the helper functions `src/utils/*`. List them here:

```
1. bedrock_agent_helper.py
2. ...
```

* [ ] Have you included your Agent Example name and introduction in [README.md](/README.md) and [examples/agents/README.md](/examples/agents/README.md)?
* [ ] Have you included your Multi-Agent Example name and introduction in [README.md](/README.md) and [examples/multi_agent_collaboration/README.md](/examples/multi_agent_collaboration/README.md)?
* [ ] Have you documented **Introduction**, **Architecture Diagram**, **Prerequisites**, **Usage**, **Sample Prompts**, and **Clean Up** steps in your example README?
* [ ] I agree to resolve any [issues](https://github.com/awslabs/amazon-bedrock-agent-samples/issues) created for this example in the future.

<hr/>

### src/utils Submissions:

Changes to the utils folder won't be accepted. Instead, open a new [issue](https://github.com/awslabs/amazon-bedrock-agent-samples/issues).

<hr/>

### src/shared tool Submissions:

Changes to existing tools won't be accepted. Instead, open a new [issue](https://github.com/awslabs/amazon-bedrock-agent-samples/issues).

* [ ] Business justification for including a new tool

```
This tool is necessary because ...
```

* How is this tool implemented?
    - * [ ] AWS CDK
    - * [ ] AWS CloudFormation (recommended)

<hr/>

* [ ] Add your name to [CONTRIBUTORS.md](/CONTRIBUTORS.md) :D