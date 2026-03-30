# Source: https://docs.aws.amazon.com/supportapp/latest/APIReference/llms.txt

# AWS Support App in Slack API Reference

> You can use the Support App in Slack API to manage your support cases in Slack for your AWS account. After you configure your Slack workspace and channel with the Support App, you can perform the following tasks directly in your Slack channel:

- [Welcome](https://docs.aws.amazon.com/supportapp/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/supportapp/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/supportapp/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_Operations.html)

- [CreateSlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_CreateSlackChannelConfiguration.html): Creates a Slack channel configuration for your AWS account.
- [DeleteAccountAlias](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteAccountAlias.html): Deletes an alias for an AWS account ID.
- [DeleteSlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteSlackChannelConfiguration.html): Deletes a Slack channel configuration from your AWS account.
- [DeleteSlackWorkspaceConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteSlackWorkspaceConfiguration.html): Deletes a Slack workspace configuration from your AWS account.
- [GetAccountAlias](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_GetAccountAlias.html): Retrieves the alias from an AWS account ID.
- [ListSlackChannelConfigurations](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_ListSlackChannelConfigurations.html): Lists the Slack channel configurations for an AWS account.
- [ListSlackWorkspaceConfigurations](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_ListSlackWorkspaceConfigurations.html): Lists the Slack workspace configurations for an AWS account.
- [PutAccountAlias](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_PutAccountAlias.html): Creates or updates an individual alias for each AWS account ID.
- [RegisterSlackWorkspaceForOrganization](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.html): Registers a Slack workspace for your AWS account.
- [UpdateSlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_UpdateSlackChannelConfiguration.html): Updates the configuration for a Slack channel, such as case update notifications.


## [Data Types](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_Types.html)

- [SlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_SlackChannelConfiguration.html): The configuration for a Slack channel that you added for your AWS account.
- [SlackWorkspaceConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_SlackWorkspaceConfiguration.html): The configuration for a Slack workspace that you added to an AWS account.
