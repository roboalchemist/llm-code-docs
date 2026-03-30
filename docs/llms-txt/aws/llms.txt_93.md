# Source: https://docs.aws.amazon.com/appfabric/latest/api/llms.txt

# AWS AppFabric API Reference

> AWS AppFabric quickly connects software as a service (SaaS) applications across your organization. This allows IT and security teams to easily manage and secure applications using a standard schema, and employees can complete everyday tasks faster using generative artificial intelligence (AI). You can use these APIs to complete AppFabric tasks, such as setting up audit log ingestions or viewing user access. For more information about AppFabric, including the required permissions to use the service, see the AWS AppFabric Administration Guide. For more information about using the AWS Command Line Interface (AWS CLI) to manage your AppFabric resources, see the AppFabric section of the AWS CLI Reference.

- [Welcome](https://docs.aws.amazon.com/appfabric/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/appfabric/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/appfabric/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/appfabric/latest/api/API_Operations.html)

- [BatchGetUserAccessTasks](https://docs.aws.amazon.com/appfabric/latest/api/API_BatchGetUserAccessTasks.html): Gets user access details in a batch request.
- [ConnectAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_ConnectAppAuthorization.html): Establishes a connection between AWS AppFabric and an application, which allows AppFabric to call the APIs of the application.
- [CreateAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateAppAuthorization.html): Creates an app authorization within an app bundle, which allows AppFabric to connect to an application.
- [CreateAppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateAppBundle.html): Creates an app bundle to collect data from an application using AppFabric.
- [CreateIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateIngestion.html): Creates a data ingestion for an application.
- [CreateIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_CreateIngestionDestination.html): Creates an ingestion destination, which specifies how an application's ingested data is processed by AWS AppFabric and where it's delivered.
- [DeleteAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteAppAuthorization.html): Deletes an app authorization.
- [DeleteAppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteAppBundle.html): Deletes an app bundle.
- [DeleteIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteIngestion.html): Deletes an ingestion.
- [DeleteIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_DeleteIngestionDestination.html): Deletes an ingestion destination.
- [GetAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_GetAppAuthorization.html): Returns information about an app authorization.
- [GetAppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_GetAppBundle.html): Returns information about an app bundle.
- [GetIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_GetIngestion.html): Returns information about an ingestion.
- [GetIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_GetIngestionDestination.html): Returns information about an ingestion destination.
- [ListAppAuthorizations](https://docs.aws.amazon.com/appfabric/latest/api/API_ListAppAuthorizations.html): Returns a list of all app authorizations configured for an app bundle.
- [ListAppBundles](https://docs.aws.amazon.com/appfabric/latest/api/API_ListAppBundles.html): Returns a list of app bundles.
- [ListIngestionDestinations](https://docs.aws.amazon.com/appfabric/latest/api/API_ListIngestionDestinations.html): Returns a list of all ingestion destinations configured for an ingestion.
- [ListIngestions](https://docs.aws.amazon.com/appfabric/latest/api/API_ListIngestions.html): Returns a list of all ingestions configured for an app bundle.
- [ListTagsForResource](https://docs.aws.amazon.com/appfabric/latest/api/API_ListTagsForResource.html): Returns a list of tags for a resource.
- [StartIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_StartIngestion.html): Starts (enables) an ingestion, which collects data from an application.
- [StartUserAccessTasks](https://docs.aws.amazon.com/appfabric/latest/api/API_StartUserAccessTasks.html): Starts the tasks to search user access status for a specific email address.
- [StopIngestion](https://docs.aws.amazon.com/appfabric/latest/api/API_StopIngestion.html): Stops (disables) an ingestion.
- [TagResource](https://docs.aws.amazon.com/appfabric/latest/api/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/appfabric/latest/api/API_UntagResource.html): Removes a tag or tags from a resource.
- [UpdateAppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_UpdateAppAuthorization.html): Updates an app authorization within an app bundle, which allows AppFabric to connect to an application.
- [UpdateIngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_UpdateIngestionDestination.html): Updates an ingestion destination, which specifies how an application's ingested data is processed by AWS AppFabric and where it's delivered.


## [Data Types](https://docs.aws.amazon.com/appfabric/latest/api/API_Types.html)

- [ApiKeyCredential](https://docs.aws.amazon.com/appfabric/latest/api/API_ApiKeyCredential.html): Contains API key credential information.
- [AppAuthorization](https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorization.html): Contains information about an app authorization.
- [AppAuthorizationSummary](https://docs.aws.amazon.com/appfabric/latest/api/API_AppAuthorizationSummary.html): Contains a summary of an app authorization.
- [AppBundle](https://docs.aws.amazon.com/appfabric/latest/api/API_AppBundle.html): Contains information about an app bundle.
- [AppBundleSummary](https://docs.aws.amazon.com/appfabric/latest/api/API_AppBundleSummary.html): Contains a summary of an app bundle.
- [AuditLogDestinationConfiguration](https://docs.aws.amazon.com/appfabric/latest/api/API_AuditLogDestinationConfiguration.html): Contains information about an audit log destination configuration.
- [AuditLogProcessingConfiguration](https://docs.aws.amazon.com/appfabric/latest/api/API_AuditLogProcessingConfiguration.html): Contains information about an audit log processing configuration.
- [AuthRequest](https://docs.aws.amazon.com/appfabric/latest/api/API_AuthRequest.html): Contains authorization request information, which is required for AWS AppFabric to get the OAuth2 access token for an application.
- [Credential](https://docs.aws.amazon.com/appfabric/latest/api/API_Credential.html): Contains credential information for an application.
- [Destination](https://docs.aws.amazon.com/appfabric/latest/api/API_Destination.html): Contains information about an audit log destination.
- [DestinationConfiguration](https://docs.aws.amazon.com/appfabric/latest/api/API_DestinationConfiguration.html): Contains information about the destination of ingested data.
- [FirehoseStream](https://docs.aws.amazon.com/appfabric/latest/api/API_FirehoseStream.html): Contains information about an Amazon Data Firehose delivery stream.
- [Ingestion](https://docs.aws.amazon.com/appfabric/latest/api/API_Ingestion.html): Contains information about an ingestion.
- [IngestionDestination](https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionDestination.html): Contains information about an ingestion destination.
- [IngestionDestinationSummary](https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionDestinationSummary.html): Contains a summary of an ingestion destination.
- [IngestionSummary](https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionSummary.html): Contains a summary of an ingestion.
- [Oauth2Credential](https://docs.aws.amazon.com/appfabric/latest/api/API_Oauth2Credential.html): Contains OAuth2 client credential information.
- [ProcessingConfiguration](https://docs.aws.amazon.com/appfabric/latest/api/API_ProcessingConfiguration.html): Contains information about how ingested data is processed.
- [S3Bucket](https://docs.aws.amazon.com/appfabric/latest/api/API_S3Bucket.html): Contains information about an Amazon S3 bucket.
- [Tag](https://docs.aws.amazon.com/appfabric/latest/api/API_Tag.html): The key or keys of the key-value pairs for the tag or tags assigned to a resource.
- [TaskError](https://docs.aws.amazon.com/appfabric/latest/api/API_TaskError.html): Contains information about an error returned from a user access task.
- [Tenant](https://docs.aws.amazon.com/appfabric/latest/api/API_Tenant.html): Contains information about an application tenant.
- [UserAccessResultItem](https://docs.aws.amazon.com/appfabric/latest/api/API_UserAccessResultItem.html): Contains information about a user's access to an application.
- [UserAccessTaskItem](https://docs.aws.amazon.com/appfabric/latest/api/API_UserAccessTaskItem.html): Contains information about a user access task.
- [ValidationExceptionField](https://docs.aws.amazon.com/appfabric/latest/api/API_ValidationExceptionField.html): The input failed to meet the constraints specified by the AWS service in a specified field.
