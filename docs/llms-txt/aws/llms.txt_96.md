# Source: https://docs.aws.amazon.com/appintegrations/latest/APIReference/llms.txt

# Amazon AppIntegrations API Reference

> The Amazon AppIntegrations service enables you to configure and reuse connections to external applications.

- [Welcome](https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/appintegrations/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/appintegrations/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_Operations.html)

- [CreateApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateApplication.html): Creates and persists an Application resource.
- [CreateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html): Creates and persists a DataIntegration resource.
- [CreateDataIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegrationAssociation.html): Creates and persists a DataIntegrationAssociation resource.
- [CreateEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateEventIntegration.html): Creates an EventIntegration, given a specified name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that pushes events to that bus.
- [DeleteApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteApplication.html): Deletes the Application.
- [DeleteDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html): Deletes the DataIntegration.
- [DeleteEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteEventIntegration.html): Deletes the specified existing event integration.
- [GetApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetApplication.html): Get an Application resource.
- [GetDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetDataIntegration.html): Returns information about the DataIntegration.
- [GetEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_GetEventIntegration.html): Returns information about the event integration.
- [ListApplicationAssociations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListApplicationAssociations.html): Returns a paginated list of application associations for an application.
- [ListApplications](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListApplications.html): Lists applications in the account.
- [ListDataIntegrationAssociations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrationAssociations.html): Returns a paginated list of DataIntegration associations in the account.
- [ListDataIntegrations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListDataIntegrations.html): Returns a paginated list of DataIntegrations in the account.
- [ListEventIntegrationAssociations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListEventIntegrationAssociations.html): Returns a paginated list of event integration associations in the account.
- [ListEventIntegrations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListEventIntegrations.html): Returns a paginated list of event integrations in the account.
- [ListTagsForResource](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ListTagsForResource.html): Lists the tags for the specified resource.
- [TagResource](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_TagResource.html): Adds the specified tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UntagResource.html): Removes the specified tags from the specified resource.
- [UpdateApplication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateApplication.html): Updates and persists an Application resource.
- [UpdateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateDataIntegration.html): Updates the description of a DataIntegration.
- [UpdateDataIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateDataIntegrationAssociation.html): Updates and persists a DataIntegrationAssociation resource.
- [UpdateEventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_UpdateEventIntegration.html): Updates the description of an event integration.


## [Data Types](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_Types.html)

- [ApplicationAssociationSummary](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationAssociationSummary.html): Summary information about the Application Association.
- [ApplicationConfig](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationConfig.html): The configuration settings for the application.
- [ApplicationSourceConfig](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationSourceConfig.html): The configuration for where the application should be loaded from.
- [ApplicationSummary](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationSummary.html): Summary information about the Application.
- [ContactHandling](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ContactHandling.html): The contact handling configuration for the application.
- [DataIntegrationAssociationSummary](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationAssociationSummary.html): Summary information about the DataIntegration association.
- [DataIntegrationSummary](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DataIntegrationSummary.html): Summary information about the DataIntegration.
- [EventFilter](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventFilter.html): The event filter.
- [EventIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegration.html): The event integration.
- [EventIntegrationAssociation](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_EventIntegrationAssociation.html): The event integration association.
- [ExecutionConfiguration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ExecutionConfiguration.html): The configuration for how the files should be pulled from the source.
- [ExternalUrlConfig](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ExternalUrlConfig.html): The external URL source for the application.
- [FileConfiguration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_FileConfiguration.html): The configuration for what files should be pulled from the source.
- [IframeConfig](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_IframeConfig.html): The iframe configuration for the application.
- [LastExecutionStatus](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_LastExecutionStatus.html): The execution status of the last job.
- [OnDemandConfiguration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_OnDemandConfiguration.html): The start and end time for data pull from the source.
- [Publication](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_Publication.html): The configuration of an event that the application publishes.
- [ScheduleConfiguration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ScheduleConfiguration.html): The name of the data and how often it should be pulled from the source.
- [Subscription](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_Subscription.html): The configuration of an event that the application subscribes.
