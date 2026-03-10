# Source: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/llms.txt

# Amazon Pinpoint Email Service API Reference

> Welcome to the Amazon Pinpoint Email API Reference. This guide provides information about the Amazon Pinpoint Email API (version 1.0), including supported operations, data types, parameters, and schemas.

- [Welcome](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Operations.html)

- [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSet.html): Create a configuration set.
- [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateConfigurationSetEventDestination.html): Create an event destination.
- [CreateDedicatedIpPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateDedicatedIpPool.html): Create a new pool of dedicated IP addresses.
- [CreateDeliverabilityTestReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateDeliverabilityTestReport.html): Create a new predictive inbox placement test.
- [CreateEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CreateEmailIdentity.html): Verifies an email identity for use with Amazon Pinpoint.
- [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteConfigurationSet.html): Delete an existing configuration set.
- [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteConfigurationSetEventDestination.html): Delete an event destination.
- [DeleteDedicatedIpPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteDedicatedIpPool.html): Delete a dedicated IP pool.
- [DeleteEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeleteEmailIdentity.html): Deletes an email identity that you previously verified for use with Amazon Pinpoint.
- [GetAccount](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetAccount.html): Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.
- [GetBlacklistReports](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetBlacklistReports.html): Retrieve a list of the blacklists that your dedicated IP addresses appear on.
- [GetConfigurationSet](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetConfigurationSet.html): Get information about an existing configuration set, including the dedicated IP pool that it's associated with, whether or not it's enabled for sending email, and more.
- [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetConfigurationSetEventDestinations.html): Retrieve a list of event destinations that are associated with a configuration set.
- [GetDedicatedIp](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIp.html): Get information about a dedicated IP address, including the name of the dedicated IP pool that it's associated with, as well information about the automatic warm-up process for the address.
- [GetDedicatedIps](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDedicatedIps.html): List the dedicated IP addresses that are associated with your Amazon Pinpoint account.
- [GetDeliverabilityDashboardOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDeliverabilityDashboardOptions.html): Retrieve information about the status of the Deliverability dashboard for your Amazon Pinpoint account.
- [GetDeliverabilityTestReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDeliverabilityTestReport.html): Retrieve the results of a predictive inbox placement test.
- [GetDomainDeliverabilityCampaign](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDomainDeliverabilityCampaign.html): Retrieve all the deliverability data for a specific campaign.
- [GetDomainStatisticsReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetDomainStatisticsReport.html): Retrieve inbox placement and engagement rates for the domains that you use to send email.
- [GetEmailIdentity](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_GetEmailIdentity.html): Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity's verification status, its DKIM authentication status, and its custom Mail-From settings.
- [ListConfigurationSets](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListConfigurationSets.html): List all of the configuration sets associated with your Amazon Pinpoint account in the current region.
- [ListDedicatedIpPools](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDedicatedIpPools.html): List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.
- [ListDeliverabilityTestReports](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDeliverabilityTestReports.html): Show a list of the predictive inbox placement tests that you've performed, regardless of their statuses.
- [ListDomainDeliverabilityCampaigns](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListDomainDeliverabilityCampaigns.html): Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range.
- [ListEmailIdentities](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListEmailIdentities.html): Returns a list of all of the email identities that are associated with your Amazon Pinpoint account.
- [ListTagsForResource](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ListTagsForResource.html): Retrieve a list of the tags (keys and values) that are associated with a specified resource.
- [PutAccountDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountDedicatedIpWarmupAttributes.html): Enable or disable the automatic warm-up feature for dedicated IP addresses.
- [PutAccountSendingAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutAccountSendingAttributes.html): Enable or disable the ability of your account to send email.
- [PutConfigurationSetDeliveryOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetDeliveryOptions.html): Associate a configuration set with a dedicated IP pool.
- [PutConfigurationSetReputationOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetReputationOptions.html): Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.
- [PutConfigurationSetSendingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetSendingOptions.html): Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.
- [PutConfigurationSetTrackingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutConfigurationSetTrackingOptions.html): Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.
- [PutDedicatedIpInPool](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDedicatedIpInPool.html): Move a dedicated IP address to an existing dedicated IP pool.
- [PutDedicatedIpWarmupAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDedicatedIpWarmupAttributes.html)
- [PutDeliverabilityDashboardOption](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutDeliverabilityDashboardOption.html): Enable or disable the Deliverability dashboard for your Amazon Pinpoint account.
- [PutEmailIdentityDkimAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityDkimAttributes.html): Used to enable or disable DKIM authentication for an email identity.
- [PutEmailIdentityFeedbackAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityFeedbackAttributes.html): Used to enable or disable feedback forwarding for an identity.
- [PutEmailIdentityMailFromAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PutEmailIdentityMailFromAttributes.html): Used to enable or disable the custom Mail-From domain configuration for an email identity.
- [SendEmail](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SendEmail.html): Sends an email message.
- [TagResource](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_TagResource.html): Add one or more tags (keys and values) to a specified resource.
- [UntagResource](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_UntagResource.html): Remove one or more tags (keys and values) from a specified resource.
- [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_UpdateConfigurationSetEventDestination.html): Update the configuration of an event destination for a configuration set.


## [Data Types](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Types.html)

- [BlacklistEntry](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_BlacklistEntry.html): An object that contains information about a blacklisting event that impacts one of the dedicated IP addresses that is associated with your account.
- [Body](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Body.html): Represents the body of the email message.
- [CloudWatchDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CloudWatchDestination.html): An object that defines an Amazon CloudWatch destination for email events.
- [CloudWatchDimensionConfiguration](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_CloudWatchDimensionConfiguration.html): An object that defines the dimension configuration to use when you send Amazon Pinpoint email events to Amazon CloudWatch.
- [Content](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Content.html): An object that represents the content of the email, and optionally a character set specification.
- [DailyVolume](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DailyVolume.html): An object that contains information about the volume of email sent on each day of the analysis period.
- [DedicatedIp](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DedicatedIp.html): Contains information about a dedicated IP address that is associated with your Amazon Pinpoint account.
- [DeliverabilityTestReport](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeliverabilityTestReport.html): An object that contains metadata related to a predictive inbox placement test.
- [DeliveryOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DeliveryOptions.html): Used to associate a configuration set with a dedicated IP pool.
- [Destination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Destination.html): An object that describes the recipients for an email.
- [DkimAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DkimAttributes.html): An object that contains information about the DKIM configuration for an email identity.
- [DomainDeliverabilityCampaign](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DomainDeliverabilityCampaign.html): An object that contains the deliverability data for a specific campaign.
- [DomainDeliverabilityTrackingOption](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DomainDeliverabilityTrackingOption.html): An object that contains information about the Deliverability dashboard subscription for a verified domain that you use to send email and currently has an active Deliverability dashboard subscription.
- [DomainIspPlacement](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DomainIspPlacement.html): An object that contains inbox placement data for email sent from one of your email domains to a specific email provider.
- [EmailContent](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_EmailContent.html): An object that defines the entire content of the email, including the message headers and the body content.
- [EventDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_EventDestination.html): In Amazon Pinpoint, events include message sends, deliveries, opens, clicks, bounces, and complaints.
- [EventDestinationDefinition](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_EventDestinationDefinition.html): An object that defines the event destination.
- [IdentityInfo](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IdentityInfo.html): Information about an email identity.
- [InboxPlacementTrackingOption](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_InboxPlacementTrackingOption.html): An object that contains information about the inbox placement data settings for a verified domain thatâs associated with your AWS account.
- [IspPlacement](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_IspPlacement.html): An object that describes how email sent during the predictive inbox placement test was handled by a certain email provider.
- [KinesisFirehoseDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_KinesisFirehoseDestination.html): An object that defines an Amazon Kinesis Data Firehose destination for email events.
- [MailFromAttributes](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_MailFromAttributes.html): A list of attributes that are associated with a MAIL FROM domain.
- [Message](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Message.html): Represents the email message that you're sending.
- [MessageTag](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_MessageTag.html): Contains the name and value of a tag that you apply to an email.
- [OverallVolume](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_OverallVolume.html): An object that contains information about email that was sent from the selected domain.
- [PinpointDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PinpointDestination.html): An object that defines a Amazon Pinpoint destination for email events.
- [PlacementStatistics](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_PlacementStatistics.html): An object that contains inbox placement data for an email provider.
- [RawMessage](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_RawMessage.html): The raw email message.
- [ReputationOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_ReputationOptions.html): Enable or disable collection of reputation metrics for emails that you send using this configuration set in the current AWS Region.
- [SendingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SendingOptions.html): Used to enable or disable email sending for messages that use this configuration set in the current AWS Region.
- [SendQuota](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SendQuota.html): An object that contains information about the per-day and per-second sending limits for your Amazon Pinpoint account in the current AWS Region.
- [SnsDestination](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_SnsDestination.html): An object that defines an Amazon SNS destination for email events.
- [Tag](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Tag.html): An object that defines the tags that are associated with a resource.
- [Template](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_Template.html): An object that defines the email template to use for an email message, and the values to use for any message variables in that template.
- [TrackingOptions](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_TrackingOptions.html): An object that defines the tracking options for a configuration set.
- [VolumeStatistics](https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_VolumeStatistics.html): An object that contains information about the amount of email that was delivered to recipients.
