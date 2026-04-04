# Source: https://docs.aws.amazon.com/security-lake/latest/APIReference/llms.txt

# Amazon Security Lake API Reference

> Amazon Security Lake is a fully managed security data lake service. You can use Security Lake to automatically centralize security data from cloud, on-premises, and custom sources into a data lake that's stored in your AWS account. AWS Organizations is an account management service that lets you consolidate multiple AWS accounts into an organization that you create and centrally manage. With Organizations, you can create member accounts and invite existing accounts to join your organization. Security Lake helps you analyze security data for a more complete understanding of your security posture across the entire organization. It can also help you improve the protection of your workloads, applications, and data.

- [Welcome](https://docs.aws.amazon.com/security-lake/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/security-lake/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/security-lake/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_Operations.html)

- [CreateAwsLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateAwsLogSource.html): Adds a natively supported AWS service as an Amazon Security Lake source.
- [CreateCustomLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateCustomLogSource.html): Adds a third-party custom source in Amazon Security Lake, from the AWS Region where you want to create a custom source.
- [CreateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html): Initializes an Amazon Security Lake instance with the provided (or default) configuration.
- [CreateDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLakeExceptionSubscription.html): Creates the specified notification subscription in Amazon Security Lake for the organization you specify.
- [CreateDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLakeOrganizationConfiguration.html): Automatically enables Amazon Security Lake for new member accounts in your organization.
- [CreateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriber.html): Creates a subscriber for accounts that are already enabled in Amazon Security Lake.
- [CreateSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateSubscriberNotification.html): Notifies the subscriber when new data is written to the data lake for the sources that the subscriber consumes in Security Lake.
- [DeleteAwsLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteAwsLogSource.html): Removes a natively supported AWS service as an Amazon Security Lake source.
- [DeleteCustomLogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteCustomLogSource.html): Removes a custom log source from Amazon Security Lake, to stop sending data from the custom source to Security Lake.
- [DeleteDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLake.html): When you disable Amazon Security Lake from your account, Security Lake is disabled in all AWS Regions and it stops collecting data from your sources.
- [DeleteDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeExceptionSubscription.html): Deletes the specified notification subscription in Amazon Security Lake for the organization you specify.
- [DeleteDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteDataLakeOrganizationConfiguration.html): Turns off automatic enablement of Amazon Security Lake for member accounts that are added to an organization in AWS Organizations.
- [DeleteSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteSubscriber.html): Deletes the subscription permission and all notification settings for accounts that are already enabled in Amazon Security Lake.
- [DeleteSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeleteSubscriberNotification.html): Deletes the specified subscription notification in Amazon Security Lake for the organization you specify.
- [DeregisterDataLakeDelegatedAdministrator](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DeregisterDataLakeDelegatedAdministrator.html): Deletes the Amazon Security Lake delegated administrator account for the organization.
- [GetDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeExceptionSubscription.html): Retrieves the protocol and endpoint that were provided when subscribing to Amazon SNS topics for exception notifications.
- [GetDataLakeOrganizationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeOrganizationConfiguration.html): Retrieves the configuration that will be automatically set up for accounts added to the organization after the organization has onboarded to Amazon Security Lake.
- [GetDataLakeSources](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetDataLakeSources.html): Retrieves a snapshot of the current Region, including whether Amazon Security Lake is enabled for those accounts and which sources Security Lake is collecting data from.
- [GetSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetSubscriber.html): Retrieves the subscription information for the specified subscription ID.
- [ListDataLakeExceptions](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakeExceptions.html): Lists the Amazon Security Lake exceptions that you can use to find the source of problems and fix them.
- [ListDataLakes](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListDataLakes.html): Retrieves the Amazon Security Lake configuration object for the specified AWS Regions.
- [ListLogSources](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListLogSources.html): Retrieves the log sources.
- [ListSubscribers](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListSubscribers.html): Lists all subscribers for the specific Amazon Security Lake account ID.
- [ListTagsForResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListTagsForResource.html): Retrieves the tags (keys and values) that are associated with an Amazon Security Lake resource: a subscriber, or the data lake configuration for your AWS account in a particular AWS Region.
- [RegisterDataLakeDelegatedAdministrator](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_RegisterDataLakeDelegatedAdministrator.html): Designates the Amazon Security Lake delegated administrator account for the organization.
- [TagResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_TagResource.html): Adds or updates one or more tags that are associated with an Amazon Security Lake resource: a subscriber, or the data lake configuration for your AWS account in a particular AWS Region.
- [UntagResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UntagResource.html): Removes one or more tags (keys and values) from an Amazon Security Lake resource: a subscriber, or the data lake configuration for your AWS account in a particular AWS Region.
- [UpdateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html): You can use UpdateDataLake to specify where to store your security data, how it should be encrypted at rest and for how long.
- [UpdateDataLakeExceptionSubscription](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLakeExceptionSubscription.html): Updates the specified notification subscription in Amazon Security Lake for the organization you specify.
- [UpdateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriber.html): Updates an existing subscription for the given Amazon Security Lake account ID.
- [UpdateSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriberNotification.html): Updates an existing notification method for the subscription (SQS or HTTPs endpoint) or switches the notification subscription endpoint for a subscriber.


## [Data Types](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_Types.html)

- [AwsIdentity](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_AwsIdentity.html): The AWS identity.
- [AwsLogSourceConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_AwsLogSourceConfiguration.html): To add a natively-supported AWS service as a log source, use these parameters to specify the configuration settings for the log source.
- [AwsLogSourceResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_AwsLogSourceResource.html): Amazon Security Lake can collect logs and events from natively-supported AWS services.
- [CustomLogSourceAttributes](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceAttributes.html): The attributes of a third-party custom source.
- [CustomLogSourceConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceConfiguration.html): The configuration used for the third-party custom source.
- [CustomLogSourceCrawlerConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceCrawlerConfiguration.html): The configuration used for the Glue Crawler for a third-party custom source.
- [CustomLogSourceProvider](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceProvider.html): The details of the log provider for a third-party custom source.
- [CustomLogSourceResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceResource.html): Amazon Security Lake can collect logs and events from third-party custom sources.
- [DataLakeAutoEnableNewAccountConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeAutoEnableNewAccountConfiguration.html): Automatically enable new organization accounts as member accounts from an Amazon Security Lake administrator account.
- [DataLakeConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeConfiguration.html): Provides details of Amazon Security Lake object.
- [DataLakeEncryptionConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeEncryptionConfiguration.html): Provides encryption details of Amazon Security Lake object.
- [DataLakeException](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeException.html): The details for an Amazon Security Lake exception.
- [DataLakeLifecycleConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeLifecycleConfiguration.html): Provides lifecycle details of Amazon Security Lake object.
- [DataLakeLifecycleExpiration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeLifecycleExpiration.html): Provide expiration lifecycle details of Amazon Security Lake object.
- [DataLakeLifecycleTransition](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeLifecycleTransition.html): Provide transition lifecycle details of Amazon Security Lake object.
- [DataLakeReplicationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeReplicationConfiguration.html): Provides replication details for objects stored in the Amazon Security Lake data lake.
- [DataLakeResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeResource.html): Provides details of Amazon Security Lake object.
- [DataLakeSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeSource.html): Amazon Security Lake collects logs and events from supported AWS services and custom sources.
- [DataLakeSourceStatus](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeSourceStatus.html): Retrieves the Logs status for the Amazon Security Lake account.
- [DataLakeUpdateException](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeUpdateException.html): The details of the last UpdateDataLake or DeleteDataLake API request which failed.
- [DataLakeUpdateStatus](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeUpdateStatus.html): The status of the last UpdateDataLake or DeleteDataLake API request.
- [HttpsNotificationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_HttpsNotificationConfiguration.html): The configurations used for HTTPS subscriber notification.
- [LogSource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_LogSource.html): Amazon Security Lake can collect logs and events from natively-supported AWS services and custom sources.
- [LogSourceResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_LogSourceResource.html): The supported source types from which logs and events are collected in Amazon Security Lake.
- [NotificationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_NotificationConfiguration.html): Specify the configurations you want to use for subscriber notification to notify the subscriber when new data is written to the data lake for sources that the subscriber consumes in Security Lake.
- [SqsNotificationConfiguration](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_SqsNotificationConfiguration.html): The configurations used for EventBridge subscriber notification.
- [SubscriberResource](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_SubscriberResource.html): Provides details about the Amazon Security Lake account subscription.
- [Tag](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_Tag.html): A tag is a label that you can define and associate with AWS resources, including certain types of Amazon Security Lake resources.
