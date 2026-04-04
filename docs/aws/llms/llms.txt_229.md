# Source: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/llms.txt

# AWS CodeStar Notifications Welcome

> This AWS CodeStar Notifications API Reference provides descriptions and usage examples of the operations and data types for the AWS CodeStar Notifications API. You can use the AWS CodeStar Notifications API to work with the following objects:

- [Welcome](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Operations.html)

- [CreateNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_CreateNotificationRule.html): Creates a notification rule for a resource.
- [DeleteNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DeleteNotificationRule.html): Deletes a notification rule for a resource.
- [DeleteTarget](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DeleteTarget.html): Deletes a specified target for notifications.
- [DescribeNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_DescribeNotificationRule.html): Returns information about a specified notification rule.
- [ListEventTypes](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListEventTypes.html): Returns information about the event types available for configuring notifications.
- [ListNotificationRules](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListNotificationRules.html): Returns a list of the notification rules for an AWS account.
- [ListTagsForResource](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTagsForResource.html): Returns a list of the tags associated with a notification rule.
- [ListTargets](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTargets.html): Returns a list of the notification rule targets for an AWS account.
- [Subscribe](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Subscribe.html): Creates an association between a notification rule and an Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client so that the associated target can receive notifications when the events described in the rule are triggered.
- [TagResource](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_TagResource.html): Associates a set of provided tags with a notification rule.
- [Unsubscribe](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Unsubscribe.html): Removes an association between a notification rule and an Amazon Q Developer in chat applications topic so that subscribers to that topic stop receiving notifications when the events described in the rule are triggered.
- [UntagResource](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_UntagResource.html): Removes the association between one or more provided tags and a notification rule.
- [UpdateNotificationRule](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_UpdateNotificationRule.html): Updates a notification rule for a resource.


## [Data Types](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Types.html)

- [EventTypeSummary](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_EventTypeSummary.html): Returns information about an event that has triggered a notification rule.
- [ListEventTypesFilter](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListEventTypesFilter.html): Information about a filter to apply to the list of returned event types.
- [ListNotificationRulesFilter](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListNotificationRulesFilter.html): Information about a filter to apply to the list of returned notification rules.
- [ListTargetsFilter](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListTargetsFilter.html): Information about a filter to apply to the list of returned targets.
- [NotificationRuleSummary](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_NotificationRuleSummary.html): Information about a specified notification rule.
- [Target](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_Target.html): Information about the Amazon Q Developer in chat applications topics or Amazon Q Developer in chat applications clients associated with a notification rule.
- [TargetSummary](https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_TargetSummary.html): Information about the targets specified for a notification rule.
