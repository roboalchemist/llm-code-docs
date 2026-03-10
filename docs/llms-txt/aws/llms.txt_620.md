# Source: https://docs.aws.amazon.com/notifications/latest/APIReference/llms.txt

# AWS User Notifications API Reference

> The AWS User Notifications API Reference provides descriptions, API request parameters, and the JSON response for each of the User Notifications API actions.

- [Welcome](https://docs.aws.amazon.com/notifications/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/notifications/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/notifications/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/notifications/latest/APIReference/API_Operations.html)

- [AssociateChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateChannel.html): Associates a delivery Channel with a particular NotificationConfiguration.
- [AssociateManagedNotificationAccountContact](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateManagedNotificationAccountContact.html): Associates an Account Contact with a particular ManagedNotificationConfiguration.
- [AssociateManagedNotificationAdditionalChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateManagedNotificationAdditionalChannel.html): Associates an additional Channel with a particular ManagedNotificationConfiguration.
- [AssociateOrganizationalUnit](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AssociateOrganizationalUnit.html): Associates an organizational unit with a notification configuration.
- [CreateEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_CreateEventRule.html): Creates an EventRule that is associated with a specified NotificationConfiguration.
- [CreateNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_CreateNotificationConfiguration.html): Creates a new NotificationConfiguration.
- [DeleteEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeleteEventRule.html): Deletes an EventRule.
- [DeleteNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeleteNotificationConfiguration.html): Deletes a NotificationConfiguration.
- [DeregisterNotificationHub](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DeregisterNotificationHub.html): Deregisters a NotificationConfiguration in the specified Region.
- [DisableNotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisableNotificationsAccessForOrganization.html): Disables service trust between AWS User Notifications and AWS Organizations.
- [DisassociateChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateChannel.html): Disassociates a Channel from a specified NotificationConfiguration.
- [DisassociateManagedNotificationAccountContact](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateManagedNotificationAccountContact.html): Disassociates an Account Contact with a particular ManagedNotificationConfiguration.
- [DisassociateManagedNotificationAdditionalChannel](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateManagedNotificationAdditionalChannel.html): Disassociates an additional Channel from a particular ManagedNotificationConfiguration.
- [DisassociateOrganizationalUnit](https://docs.aws.amazon.com/notifications/latest/APIReference/API_DisassociateOrganizationalUnit.html): Removes the association between an organizational unit and a notification configuration.
- [EnableNotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_EnableNotificationsAccessForOrganization.html): Enables service trust between AWS User Notifications and AWS Organizations.
- [GetEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetEventRule.html): Returns a specified EventRule.
- [GetManagedNotificationChildEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationChildEvent.html): Returns the child event of a specific given ManagedNotificationEvent.
- [GetManagedNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationConfiguration.html): Returns a specified ManagedNotificationConfiguration.
- [GetManagedNotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetManagedNotificationEvent.html): Returns a specified ManagedNotificationEvent.
- [GetNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationConfiguration.html): Returns a specified NotificationConfiguration.
- [GetNotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationEvent.html): Returns a specified NotificationEvent.
- [GetNotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_GetNotificationsAccessForOrganization.html): Returns the AccessStatus of Service Trust Enablement for AWS User Notifications and AWS Organizations.
- [ListChannels](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListChannels.html): Returns a list of Channels for a NotificationConfiguration.
- [ListEventRules](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListEventRules.html): Returns a list of EventRules according to specified filters, in reverse chronological order (newest first).
- [ListManagedNotificationChannelAssociations](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationChannelAssociations.html): Returns a list of Account contacts and Channels associated with a ManagedNotificationConfiguration, in paginated format.
- [ListManagedNotificationChildEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationChildEvents.html): Returns a list of ManagedNotificationChildEvents for a specified aggregate ManagedNotificationEvent, ordered by creation time in reverse chronological order (newest first).
- [ListManagedNotificationConfigurations](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationConfigurations.html): Returns a list of Managed Notification Configurations according to specified filters, ordered by creation time in reverse chronological order (newest first).
- [ListManagedNotificationEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListManagedNotificationEvents.html): Returns a list of Managed Notification Events according to specified filters, ordered by creation time in reverse chronological order (newest first).
- [ListMemberAccounts](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListMemberAccounts.html): Returns a list of member accounts associated with a notification configuration.
- [ListNotificationConfigurations](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationConfigurations.html): Returns a list of abbreviated NotificationConfigurations according to specified filters, in reverse chronological order (newest first).
- [ListNotificationEvents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationEvents.html): Returns a list of NotificationEvents according to specified filters, in reverse chronological order (newest first).
- [ListNotificationHubs](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListNotificationHubs.html): Returns a list of NotificationHubs.
- [ListOrganizationalUnits](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListOrganizationalUnits.html): Returns a list of organizational units associated with a notification configuration.
- [ListTagsForResource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ListTagsForResource.html): Returns a list of tags for a specified Amazon Resource Name (ARN).
- [RegisterNotificationHub](https://docs.aws.amazon.com/notifications/latest/APIReference/API_RegisterNotificationHub.html): Registers a NotificationConfiguration in the specified Region.
- [TagResource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_TagResource.html): Tags the resource with a tag key and value.
- [UntagResource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UntagResource.html): Untags a resource with a specified Amazon Resource Name (ARN).
- [UpdateEventRule](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateEventRule.html): Updates an existing EventRule.
- [UpdateNotificationConfiguration](https://docs.aws.amazon.com/notifications/latest/APIReference/API_UpdateNotificationConfiguration.html): Updates a NotificationConfiguration.


## [Data Types](https://docs.aws.amazon.com/notifications/latest/APIReference/API_Types.html)

- [AggregationDetail](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AggregationDetail.html): Provides detailed information about the dimensions used for aggregation.
- [AggregationKey](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AggregationKey.html): Key-value collection that indicate how notifications are grouped.
- [AggregationSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_AggregationSummary.html): Provides additional information about the aggregation key.
- [Dimension](https://docs.aws.amazon.com/notifications/latest/APIReference/API_Dimension.html): The key-value pair of properties for an event.
- [EventRuleStatusSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_EventRuleStatusSummary.html): Provides additional information about the current EventRule status.
- [EventRuleStructure](https://docs.aws.amazon.com/notifications/latest/APIReference/API_EventRuleStructure.html): Contains a complete list of fields related to an EventRule.
- [ManagedNotificationChannelAssociationSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChannelAssociationSummary.html): Provides a summary of channel associations for a managed notification configuration.
- [ManagedNotificationChildEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChildEvent.html): A notification-focused representation of an event.
- [ManagedNotificationChildEventOverview](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChildEventOverview.html): Describes an overview and metadata for a ManagedNotificationChildEvent.
- [ManagedNotificationChildEventSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationChildEventSummary.html): Describes a short summary and metadata for a ManagedNotificationChildEvent.
- [ManagedNotificationConfigurationStructure](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationConfigurationStructure.html): Describes the basic structure and properties of a ManagedNotificationConfiguration.
- [ManagedNotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationEvent.html): A notification-focused representation of an event.
- [ManagedNotificationEventOverview](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationEventOverview.html): Describes an overview and metadata for a ManagedNotificationEvent.
- [ManagedNotificationEventSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedNotificationEventSummary.html): A short summary of a ManagedNotificationEvent.
- [ManagedSourceEventMetadataSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ManagedSourceEventMetadataSummary.html): A short summary and metadata for a managed notification event.
- [MediaElement](https://docs.aws.amazon.com/notifications/latest/APIReference/API_MediaElement.html): Describes a media element.
- [MemberAccount](https://docs.aws.amazon.com/notifications/latest/APIReference/API_MemberAccount.html): Contains information about a member account.
- [MessageComponents](https://docs.aws.amazon.com/notifications/latest/APIReference/API_MessageComponents.html): Describes the components of a notification message.
- [MessageComponentsSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_MessageComponentsSummary.html): Contains the headline message component.
- [NotificationConfigurationStructure](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationConfigurationStructure.html): Contains the complete list of fields for a NotificationConfiguration.
- [NotificationEvent](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEvent.html): A NotificationEvent is a notification-focused representation of an event.
- [NotificationEventOverview](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEventOverview.html): Describes a short summary of a NotificationEvent.
- [NotificationEventSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationEventSummary.html): Describes a short summary and metadata for a NotificationEvent.
- [NotificationHubOverview](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationHubOverview.html): Describes an overview of a NotificationHub.
- [NotificationHubStatusSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationHubStatusSummary.html): Provides additional information about the current NotificationHub status.
- [NotificationsAccessForOrganization](https://docs.aws.amazon.com/notifications/latest/APIReference/API_NotificationsAccessForOrganization.html): Orgs Service trust for AWS User Notifications.
- [Resource](https://docs.aws.amazon.com/notifications/latest/APIReference/API_Resource.html): A resource affected by or closely linked to an event.
- [SourceEventMetadata](https://docs.aws.amazon.com/notifications/latest/APIReference/API_SourceEventMetadata.html): Describes the metadata for a source event.
- [SourceEventMetadataSummary](https://docs.aws.amazon.com/notifications/latest/APIReference/API_SourceEventMetadataSummary.html): Contains metadata about the event that caused the NotificationEvent.
- [SummarizationDimensionDetail](https://docs.aws.amazon.com/notifications/latest/APIReference/API_SummarizationDimensionDetail.html): Provides detailed information about the dimensions used for event summarization and aggregation.
- [SummarizationDimensionOverview](https://docs.aws.amazon.com/notifications/latest/APIReference/API_SummarizationDimensionOverview.html): Provides an overview of how data is summarized across different dimensions.
- [TextPartValue](https://docs.aws.amazon.com/notifications/latest/APIReference/API_TextPartValue.html): Describes text information objects containing fields that determine how text part objects are composed.
- [ValidationExceptionField](https://docs.aws.amazon.com/notifications/latest/APIReference/API_ValidationExceptionField.html): Stores information about a field passed inside a request that resulted in an exception.
