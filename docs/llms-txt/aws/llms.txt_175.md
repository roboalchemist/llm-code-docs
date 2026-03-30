# Source: https://docs.aws.amazon.com/chatbot/latest/APIReference/llms.txt

# Amazon Q Developer in chat applications API Reference

> The Amazon Q Developer in chat applications API Reference provides descriptions, API request parameters, and the XML response for each of the Amazon Q Developer API actions.

- [Welcome](https://docs.aws.amazon.com/chatbot/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/chatbot/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/chatbot/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html)

- [AssociateToConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_AssociateToConfiguration.html): Links a resource (for example, a custom action) to a channel configuration.
- [CreateChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateChimeWebhookConfiguration.html): Creates an Amazon Q Developer configuration for Amazon Chime.
- [CreateCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateCustomAction.html): Creates a custom action that can be invoked as an alias or as a button on a notification.
- [CreateMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateMicrosoftTeamsChannelConfiguration.html): Creates an Amazon Q Developer configuration for Microsoft Teams.
- [CreateSlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateSlackChannelConfiguration.html): Creates an Amazon Q Developer configuration for Slack.
- [DeleteChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteChimeWebhookConfiguration.html): Deletes a Amazon Chime webhook configuration for Amazon Q Developer.
- [DeleteCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteCustomAction.html): Deletes a custom action.
- [DeleteMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsChannelConfiguration.html): Deletes a Microsoft Teams channel configuration for Amazon Q Developer.
- [DeleteMicrosoftTeamsConfiguredTeam](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsConfiguredTeam.html): Deletes the Microsoft Teams team authorization allowing for channels to be configured in that Microsoft Teams team.
- [DeleteMicrosoftTeamsUserIdentity](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsUserIdentity.html): Identifes a user level permission for a channel configuration.
- [DeleteSlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackChannelConfiguration.html): Deletes a Slack channel configuration for Amazon Q Developer.
- [DeleteSlackUserIdentity](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackUserIdentity.html): Deletes a user level permission for a Slack channel configuration.
- [DeleteSlackWorkspaceAuthorization](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackWorkspaceAuthorization.html): Deletes the Slack workspace authorization that allows channels to be configured in that workspace.
- [DescribeChimeWebhookConfigurations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeChimeWebhookConfigurations.html): Lists Amazon Chime webhook configurations optionally filtered by ChatConfigurationArn.
- [DescribeSlackChannelConfigurations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackChannelConfigurations.html): Lists Slack channel configurations optionally filtered by ChatConfigurationArn
- [DescribeSlackUserIdentities](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackUserIdentities.html): Lists all Slack user identities with a mapped role.
- [DescribeSlackWorkspaces](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackWorkspaces.html): List all authorized Slack workspaces connected to the AWS Account onboarded with Amazon Q Developer.
- [DisassociateFromConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DisassociateFromConfiguration.html): Unlink a resource, for example a custom action, from a channel configuration.
- [GetAccountPreferences](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetAccountPreferences.html): Returns Amazon Q Developer account preferences.
- [GetCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetCustomAction.html): Returns a custom action.
- [GetMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetMicrosoftTeamsChannelConfiguration.html): Returns a Microsoft Teams channel configuration in an AWS account.
- [ListAssociations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListAssociations.html): Lists resources associated with a channel configuration.
- [ListCustomActions](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListCustomActions.html): Lists custom actions defined in this account.
- [ListMicrosoftTeamsChannelConfigurations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsChannelConfigurations.html): Lists all Amazon Q Developer Microsoft Teams channel configurations in an AWS account.
- [ListMicrosoftTeamsConfiguredTeams](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsConfiguredTeams.html): Lists all authorized Microsoft Teams for an AWS Account
- [ListMicrosoftTeamsUserIdentities](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsUserIdentities.html): A list all Microsoft Teams user identities with a mapped role.
- [ListTagsForResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListTagsForResource.html): Lists all of the tags associated with the Amazon Resource Name (ARN) that you specify.
- [TagResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TagResource.html): Attaches a key-value pair to a resource, as identified by its Amazon Resource Name (ARN).
- [UntagResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UntagResource.html): Detaches a key-value pair from a resource, as identified by its Amazon Resource Name (ARN).
- [UpdateAccountPreferences](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateAccountPreferences.html): Updates Amazon Q Developer account preferences.
- [UpdateChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateChimeWebhookConfiguration.html): Updates a Amazon Chime webhook configuration.
- [UpdateCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateCustomAction.html): Updates a custom action.
- [UpdateMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateMicrosoftTeamsChannelConfiguration.html): Updates an Microsoft Teams channel configuration.
- [UpdateSlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateSlackChannelConfiguration.html): Updates a Slack channel configuration.


## [Data Types](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Types.html)

- [AccountPreferences](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_AccountPreferences.html): Preferences related to Amazon Q Developer usage in the calling AWS account.
- [AssociationListing](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_AssociationListing.html): A listing of an association with a channel configuration.
- [ChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ChimeWebhookConfiguration.html): An Amazon Q Developer configuration for Amazon Chime.
- [ConfiguredTeam](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ConfiguredTeam.html): A Microsoft Teams team that is authorized with Amazon Q Developer.
- [CustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomAction.html): Represents a parameterized command that can be invoked as an alias or as a notification button in the chat client.
- [CustomActionAttachment](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomActionAttachment.html): Defines when a custom action button should be attached to a notification.
- [CustomActionAttachmentCriteria](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomActionAttachmentCriteria.html): A criteria for when a button should be shown based on values in the notification
- [CustomActionDefinition](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CustomActionDefinition.html): The definition of the command to run when invoked as an alias or as an action button.
- [SlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_SlackChannelConfiguration.html): An Amazon Q Developer configuration for Slack.
- [SlackUserIdentity](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_SlackUserIdentity.html): Identifes a user level permission for a channel configuration.
- [SlackWorkspace](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_SlackWorkspace.html): A Slack workspace.
- [Tag](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Tag.html): A key-value pair.
- [TeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TeamsChannelConfiguration.html): An Amazon Q Developer configuration for Microsoft Teams.
- [TeamsUserIdentity](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TeamsUserIdentity.html): Identifes a user level permission for a channel configuration.
