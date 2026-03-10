# Source: https://docs.aws.amazon.com/ses/latest/APIReference/llms.txt

# Amazon Simple Email Service API Reference

> This document contains reference information for the Amazon Simple Email Service (Amazon SES) API, version 2010-12-01. This document is best used in conjunction with the Amazon SES Developer Guide.

- [Welcome](https://docs.aws.amazon.com/ses/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/ses/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/ses/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/ses/latest/APIReference/API_Operations.html)

- [CloneReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CloneReceiptRuleSet.html): Creates a receipt rule set by cloning an existing one.
- [CreateConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSet.html): Creates a configuration set.
- [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetEventDestination.html): Creates a configuration set event destination.
- [CreateConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateConfigurationSetTrackingOptions.html): Creates an association between a configuration set and a custom domain for open and click event tracking.
- [CreateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateCustomVerificationEmailTemplate.html): Creates a new custom verification email template.
- [CreateReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptFilter.html): Creates a new IP address filter.
- [CreateReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRule.html): Creates a receipt rule.
- [CreateReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateReceiptRuleSet.html): Creates an empty receipt rule set.
- [CreateTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CreateTemplate.html): Creates an email template.
- [DeleteConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSet.html): Deletes a configuration set.
- [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetEventDestination.html): Deletes a configuration set event destination.
- [DeleteConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteConfigurationSetTrackingOptions.html): Deletes an association between a configuration set and a custom domain for open and click event tracking.
- [DeleteCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteCustomVerificationEmailTemplate.html): Deletes an existing custom verification email template.
- [DeleteIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentity.html): Deletes the specified identity (an email address or a domain) from the list of verified identities.
- [DeleteIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteIdentityPolicy.html): Deletes the specified sending authorization policy for the given identity (an email address or a domain).
- [DeleteReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptFilter.html): Deletes the specified IP address filter.
- [DeleteReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRule.html): Deletes the specified receipt rule.
- [DeleteReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteReceiptRuleSet.html): Deletes the specified receipt rule set and all of the receipt rules it contains.
- [DeleteTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteTemplate.html): Deletes an email template.
- [DeleteVerifiedEmailAddress](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeleteVerifiedEmailAddress.html): Deprecated.
- [DescribeActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeActiveReceiptRuleSet.html): Returns the metadata and receipt rules for the receipt rule set that is currently active.
- [DescribeConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeConfigurationSet.html): Returns the details of the specified configuration set.
- [DescribeReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRule.html): Returns the details of the specified receipt rule.
- [DescribeReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_DescribeReceiptRuleSet.html): Returns the details of the specified receipt rule set.
- [GetAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetAccountSendingEnabled.html): Returns the email sending status of the Amazon SES account for the current Region.
- [GetCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetCustomVerificationEmailTemplate.html): Returns the custom email verification template for the template name you specify.
- [GetIdentityDkimAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityDkimAttributes.html): Returns the current status of Easy DKIM signing for an entity.
- [GetIdentityMailFromDomainAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityMailFromDomainAttributes.html): Returns the custom MAIL FROM attributes for a list of identities (email addresses : domains).
- [GetIdentityNotificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityNotificationAttributes.html): Given a list of verified identities (email addresses and/or domains), returns a structure describing identity notification attributes.
- [GetIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityPolicies.html): Returns the requested sending authorization policies for the given identity (an email address or a domain).
- [GetIdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetIdentityVerificationAttributes.html): Given a list of identities (email addresses and/or domains), returns the verification status and (for domain identities) the verification token for each identity.
- [GetSendQuota](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendQuota.html): Provides the sending limits for the Amazon SES account.
- [GetSendStatistics](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendStatistics.html): Provides sending statistics for the current AWS Region.
- [GetTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_GetTemplate.html): Displays the template object (which includes the Subject line, HTML part and text part) for the template you specify.
- [ListConfigurationSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListConfigurationSets.html): Provides a list of the configuration sets associated with your Amazon SES account in the current AWS Region.
- [ListCustomVerificationEmailTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListCustomVerificationEmailTemplates.html): Lists the existing custom verification email templates for your account in the current AWS Region.
- [ListIdentities](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html): Returns a list containing all of the identities (email addresses and domains) for your AWS account in the current AWS Region, regardless of verification status.
- [ListIdentityPolicies](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentityPolicies.html): Returns a list of sending authorization policies that are attached to the given identity (an email address or a domain).
- [ListReceiptFilters](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptFilters.html): Lists the IP address filters associated with your AWS account in the current AWS Region.
- [ListReceiptRuleSets](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListReceiptRuleSets.html): Lists the receipt rule sets that exist under your AWS account in the current AWS Region.
- [ListTemplates](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListTemplates.html): Lists the email templates present in your Amazon SES account in the current AWS Region.
- [ListVerifiedEmailAddresses](https://docs.aws.amazon.com/ses/latest/APIReference/API_ListVerifiedEmailAddresses.html): Deprecated.
- [PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html): Adds or updates the delivery options for a configuration set.
- [PutIdentityPolicy](https://docs.aws.amazon.com/ses/latest/APIReference/API_PutIdentityPolicy.html): Adds or updates a sending authorization policy for the specified identity (an email address or a domain).
- [ReorderReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReorderReceiptRuleSet.html): Reorders the receipt rules within a receipt rule set.
- [SendBounce](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBounce.html): Generates and sends a bounce message to the sender of an email you received through Amazon SES.
- [SendBulkTemplatedEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBulkTemplatedEmail.html): Composes an email message to multiple destinations.
- [SendCustomVerificationEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendCustomVerificationEmail.html): Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it.
- [SendEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendEmail.html): Composes an email message and immediately queues it for sending.
- [SendRawEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendRawEmail.html): Composes an email message and immediately queues it for sending.
- [SendTemplatedEmail](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html): Composes an email message using an email template and immediately queues it for sending.
- [SetActiveReceiptRuleSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetActiveReceiptRuleSet.html): Sets the specified receipt rule set as the active receipt rule set.
- [SetIdentityDkimEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityDkimEnabled.html): Enables or disables Easy DKIM signing of email sent from an identity.
- [SetIdentityFeedbackForwardingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityFeedbackForwardingEnabled.html): Given an identity (an email address or a domain), enables or disables whether Amazon SES forwards bounce and complaint notifications as email.
- [SetIdentityHeadersInNotificationsEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityHeadersInNotificationsEnabled.html): Given an identity (an email address or a domain), sets whether Amazon SES includes the original email headers in the Amazon Simple Notification Service (Amazon SNS) notifications of a specified type.
- [SetIdentityMailFromDomain](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html): Enables or disables the custom MAIL FROM domain setup for a verified identity (an email address or a domain).
- [SetIdentityNotificationTopic](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityNotificationTopic.html): Sets an Amazon Simple Notification Service (Amazon SNS) topic to use when delivering notifications.
- [SetReceiptRulePosition](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetReceiptRulePosition.html): Sets the position of the specified receipt rule in the receipt rule set.
- [TestRenderTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_TestRenderTemplate.html): Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.
- [UpdateAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html): Enables or disables email sending across your entire Amazon SES account in the current AWS Region.
- [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetEventDestination.html): Updates the event destination of a configuration set.
- [UpdateConfigurationSetReputationMetricsEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetReputationMetricsEnabled.html): Enables or disables the publishing of reputation metrics for emails sent using a specific configuration set in a given AWS Region.
- [UpdateConfigurationSetSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html): Enables or disables email sending for messages sent using a specific configuration set in a given AWS Region.
- [UpdateConfigurationSetTrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetTrackingOptions.html): Modifies an association between a configuration set and a custom domain for open and click event tracking.
- [UpdateCustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateCustomVerificationEmailTemplate.html): Updates an existing custom verification email template.
- [UpdateReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateReceiptRule.html): Updates a receipt rule.
- [UpdateTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateTemplate.html): Updates an email template.
- [VerifyDomainDkim](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainDkim.html): Returns a set of DKIM tokens for a domain identity.
- [VerifyDomainIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyDomainIdentity.html): Adds a domain to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it.
- [VerifyEmailAddress](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailAddress.html): Deprecated.
- [VerifyEmailIdentity](https://docs.aws.amazon.com/ses/latest/APIReference/API_VerifyEmailIdentity.html): Adds an email address to the list of identities for your Amazon SES account in the current AWS Region and attempts to verify it.


## [Data Types](https://docs.aws.amazon.com/ses/latest/APIReference/API_Types.html)

- [AddHeaderAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_AddHeaderAction.html): When included in a receipt rule, this action adds a header to the received email.
- [Body](https://docs.aws.amazon.com/ses/latest/APIReference/API_Body.html): Represents the body of the message.
- [BounceAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_BounceAction.html): When included in a receipt rule, this action rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
- [BouncedRecipientInfo](https://docs.aws.amazon.com/ses/latest/APIReference/API_BouncedRecipientInfo.html): Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
- [BulkEmailDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_BulkEmailDestination.html): An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.
- [BulkEmailDestinationStatus](https://docs.aws.amazon.com/ses/latest/APIReference/API_BulkEmailDestinationStatus.html): An object that contains the response from the SendBulkTemplatedEmail operation.
- [CloudWatchDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_CloudWatchDestination.html): Contains information associated with an Amazon CloudWatch event destination to which email sending events are published.
- [CloudWatchDimensionConfiguration](https://docs.aws.amazon.com/ses/latest/APIReference/API_CloudWatchDimensionConfiguration.html): Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.
- [ConfigurationSet](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConfigurationSet.html): The name of the configuration set.
- [ConnectAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_ConnectAction.html): When included in a receipt rule, this action parses the received message and starts an email contact in Amazon Connect on your behalf.
- [Content](https://docs.aws.amazon.com/ses/latest/APIReference/API_Content.html): Represents textual data, plus an optional character set specification.
- [CustomVerificationEmailTemplate](https://docs.aws.amazon.com/ses/latest/APIReference/API_CustomVerificationEmailTemplate.html): Contains information about a custom verification email template.
- [DeliveryOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_DeliveryOptions.html): Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).
- [Destination](https://docs.aws.amazon.com/ses/latest/APIReference/API_Destination.html): Represents the destination of the message, consisting of To:, CC:, and BCC: fields.
- [EventDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_EventDestination.html): Contains information about an event destination.
- [ExtensionField](https://docs.aws.amazon.com/ses/latest/APIReference/API_ExtensionField.html): Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
- [IdentityDkimAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityDkimAttributes.html): Represents the DKIM attributes of a verified email address or a domain.
- [IdentityMailFromDomainAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityMailFromDomainAttributes.html): Represents the custom MAIL FROM domain attributes of a verified identity (email address or domain).
- [IdentityNotificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityNotificationAttributes.html): Represents the notification attributes of an identity, including whether an identity has Amazon Simple Notification Service (Amazon SNS) topics set for bounce, complaint, and/or delivery notifications, and whether feedback forwarding is enabled for bounce and complaint notifications.
- [IdentityVerificationAttributes](https://docs.aws.amazon.com/ses/latest/APIReference/API_IdentityVerificationAttributes.html): Represents the verification attributes of a single identity.
- [KinesisFirehoseDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_KinesisFirehoseDestination.html): Contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
- [LambdaAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_LambdaAction.html): When included in a receipt rule, this action calls an AWS Lambda function and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
- [Message](https://docs.aws.amazon.com/ses/latest/APIReference/API_Message.html): Represents the message to be sent, composed of a subject and a body.
- [MessageDsn](https://docs.aws.amazon.com/ses/latest/APIReference/API_MessageDsn.html): Message-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
- [MessageTag](https://docs.aws.amazon.com/ses/latest/APIReference/API_MessageTag.html): Contains the name and value of a tag that you can provide to SendEmail or SendRawEmail to apply to an email.
- [RawMessage](https://docs.aws.amazon.com/ses/latest/APIReference/API_RawMessage.html): Represents the raw data of the message.
- [ReceiptAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptAction.html): An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own.
- [ReceiptFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptFilter.html): A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.
- [ReceiptIpFilter](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptIpFilter.html): A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.
- [ReceiptRule](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptRule.html): Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.
- [ReceiptRuleSetMetadata](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReceiptRuleSetMetadata.html): Information about a receipt rule set.
- [RecipientDsnFields](https://docs.aws.amazon.com/ses/latest/APIReference/API_RecipientDsnFields.html): Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.
- [ReputationOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_ReputationOptions.html): Contains information about the reputation settings for a configuration set.
- [S3Action](https://docs.aws.amazon.com/ses/latest/APIReference/API_S3Action.html): When included in a receipt rule, this action saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
- [SendDataPoint](https://docs.aws.amazon.com/ses/latest/APIReference/API_SendDataPoint.html): Represents sending statistics data.
- [SNSAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_SNSAction.html): When included in a receipt rule, this action publishes a notification to Amazon Simple Notification Service (Amazon SNS).
- [SNSDestination](https://docs.aws.amazon.com/ses/latest/APIReference/API_SNSDestination.html): Contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.
- [StopAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_StopAction.html): When included in a receipt rule, this action terminates the evaluation of the receipt rule set and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
- [Template](https://docs.aws.amazon.com/ses/latest/APIReference/API_Template.html): The content of the email, composed of a subject line and either an HTML part or a text-only part.
- [TemplateMetadata](https://docs.aws.amazon.com/ses/latest/APIReference/API_TemplateMetadata.html): Contains information about an email template.
- [TrackingOptions](https://docs.aws.amazon.com/ses/latest/APIReference/API_TrackingOptions.html): A domain that is used to redirect email recipients to an Amazon SES-operated domain.
- [WorkmailAction](https://docs.aws.amazon.com/ses/latest/APIReference/API_WorkmailAction.html): When included in a receipt rule, this action calls Amazon WorkMail and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
