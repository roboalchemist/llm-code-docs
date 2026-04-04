# Source: https://docs.aws.amazon.com/codecatalyst/latest/adk/llms.txt

# Amazon CodeCatalyst Developer Guide

> With the Amazon CodeCatalyst Action Development Kit, you can can build, test, and publish actions to the CodeCatalyst actions catalog, where other users can add them to workflows.

- [Developing workflow actions for Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/adk/action-development-intro.html)
- [Custom actions concepts](https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-concepts.html)
- [Getting started](https://docs.aws.amazon.com/codecatalyst/latest/adk/getting-started.html)
- [Configuring custom actions for third-party integrations](https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-configure-third-party.html)
- [Creating secrets](https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-create-secrets.html)
- [Accessing data](https://docs.aws.amazon.com/codecatalyst/latest/adk/accessing-data.html)
- [Action reference](https://docs.aws.amazon.com/codecatalyst/latest/adk/action-ref.html)
- [ADK API and CLI reference](https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-cli-reference.html)
- [Troubleshooting](https://docs.aws.amazon.com/codecatalyst/latest/adk/troubleshooting.html)
- [Contribute](https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-contribute.html)
- [Document history](https://docs.aws.amazon.com/codecatalyst/latest/adk/doc-history.html)

## [Working with custom actions](https://docs.aws.amazon.com/codecatalyst/latest/adk/amh-actions.html)

- [Setting up your project on a local machine](https://docs.aws.amazon.com/codecatalyst/latest/adk/set-up-workspace-local.html): While it's recommended that you create a Dev Environment and build your action within a CodeCatalyst-supported IDE, you can also set up your project and build your action on your local machine.
- [Testing an action](https://docs.aws.amazon.com/codecatalyst/latest/adk/testing-action.html): Use the following instructions to add unit tests and also test your custom actions in CodeCatalyst workflows.
- [Publishing an action](https://docs.aws.amazon.com/codecatalyst/latest/adk/actions-publishing.html): In CodeCatalyst, you can publish multiple versions of an action, retrieve action metadata, and manage your actions.
- [Publishing a new action version](https://docs.aws.amazon.com/codecatalyst/latest/adk/actions-update.html): After publishing your initial action version, you can update your action definition and publish a new version to the Amazon CodeCatalyst actions catalog.
- [Deleting an action version](https://docs.aws.amazon.com/codecatalyst/latest/adk/deleting-action-version.html): Learn how to delete a version of an action from the CodeCatalyst action catalog.


## [Examples](https://docs.aws.amazon.com/codecatalyst/latest/adk/adk-examples.html)

- [AWS CodeBuild action using ADK](https://docs.aws.amazon.com/codecatalyst/latest/adk/codebuild-action-adk.html): The following example action initiates a build in AWS CodeBuild.
- [Outgoing webhook action using ADK](https://docs.aws.amazon.com/codecatalyst/latest/adk/outgoing-webhook-action.html): The outgoing webhook action can initiate an outgoing webhook (OW) and make a POST request to a provided URL.
