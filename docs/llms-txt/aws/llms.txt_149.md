# Source: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/llms.txt

# AWS CloudTrail API Reference

> This is the CloudTrail API Reference. It provides descriptions of actions, data types, common parameters, and common errors for CloudTrail.

- [Welcome](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Operations.html)

- [AddTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AddTags.html): Adds one or more tags to a trail, event data store, dashboard, or channel, up to a limit of 50.
- [CancelQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CancelQuery.html): Cancels a query if the query is not in a terminated state, such as CANCELLED, FAILED, TIMED_OUT, or FINISHED.
- [CreateChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateChannel.html): Creates a channel for CloudTrail to ingest events from a partner or external source.
- [CreateDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateDashboard.html): Creates a custom dashboard or the Highlights dashboard.
- [CreateEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateEventDataStore.html): Creates a new event data store.
- [CreateTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_CreateTrail.html): Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket.
- [DeleteChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteChannel.html): Deletes a channel.
- [DeleteDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteDashboard.html): Deletes the specified dashboard.
- [DeleteEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteEventDataStore.html): Disables the event data store specified by EventDataStore, which accepts an event data store ARN.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteResourcePolicy.html): Deletes the resource-based policy attached to the CloudTrail event data store, dashboard, or channel.
- [DeleteTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeleteTrail.html): Deletes a trail.
- [DeregisterOrganizationDelegatedAdmin](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DeregisterOrganizationDelegatedAdmin.html): Removes CloudTrail delegated administrator permissions from a member account in an organization.
- [DescribeQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeQuery.html): Returns metadata about a query, including query run time in milliseconds, number of events scanned and matched, and query status.
- [DescribeTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DescribeTrails.html): Retrieves settings for one or more trails associated with the current Region for your account.
- [DisableFederation](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DisableFederation.html): Disables Lake query federation on the specified event data store.
- [EnableFederation](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_EnableFederation.html): Enables Lake query federation on the specified event data store.
- [GenerateQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GenerateQuery.html): Generates a query from a natural language prompt.
- [GetChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetChannel.html): Returns information about a specific channel.
- [GetDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetDashboard.html): Returns the specified dashboard.
- [GetEventConfiguration](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventConfiguration.html): Retrieves the current event configuration settings for the specified event data store or trail.
- [GetEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventDataStore.html): Returns information about an event data store specified as either an ARN or the ID portion of the ARN.
- [GetEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetEventSelectors.html): Describes the settings for the event selectors that you configured for your trail.
- [GetImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetImport.html): Returns information about a specific import.
- [GetInsightSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetInsightSelectors.html): Describes the settings for the Insights event selectors that you configured for your trail or event data store.
- [GetQueryResults](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetQueryResults.html): Gets event data results of a query.
- [GetResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetResourcePolicy.html): Retrieves the JSON text of the resource-based policy document attached to the CloudTrail event data store, dashboard, or channel.
- [GetTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetTrail.html): Returns settings information for a specified trail.
- [GetTrailStatus](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_GetTrailStatus.html): Returns a JSON-formatted list of information about the specified trail.
- [ListChannels](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListChannels.html): Lists the channels in the current account, and their source names.
- [ListDashboards](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListDashboards.html): Returns information about all dashboards in the account, in the current Region.
- [ListEventDataStores](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListEventDataStores.html): Returns information about all event data stores in the account, in the current Region.
- [ListImportFailures](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListImportFailures.html): Returns a list of failures for the specified import.
- [ListImports](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListImports.html): Returns information on all imports, or a select set of imports by ImportStatus or Destination.
- [ListInsightsData](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListInsightsData.html): Returns Insights events generated on a trail that logs data events.
- [ListInsightsMetricData](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListInsightsMetricData.html): Returns Insights metrics data for trails that have enabled Insights.
- [ListPublicKeys](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListPublicKeys.html): Returns all public keys whose private keys were used to sign the digest files within the specified time range.
- [ListQueries](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListQueries.html): Returns a list of queries and query statuses for the past seven days.
- [ListTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTags.html): Lists the tags for the specified trails, event data stores, dashboards, or channels in the current Region.
- [ListTrails](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListTrails.html): Lists trails that are in the current account.
- [LookupEvents](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html): Looks up management events or CloudTrail Insights events that are captured by CloudTrail.
- [PutEventConfiguration](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutEventConfiguration.html): Updates the event configuration settings for the specified event data store or trail.
- [PutEventSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutEventSelectors.html): Configures event selectors (also referred to as basic event selectors) or advanced event selectors for your trail.
- [PutInsightSelectors](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutInsightSelectors.html): Lets you enable Insights event logging on specific event categories by specifying the Insights selectors that you want to enable on an existing trail or event data store.
- [PutResourcePolicy](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutResourcePolicy.html): Attaches a resource-based permission policy to a CloudTrail event data store, dashboard, or channel.
- [RegisterOrganizationDelegatedAdmin](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RegisterOrganizationDelegatedAdmin.html): Registers an organizationâs member account as the CloudTrail delegated administrator.
- [RemoveTags](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RemoveTags.html): Removes the specified tags from a trail, event data store, dashboard, or channel.
- [RestoreEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RestoreEventDataStore.html): Restores a deleted event data store specified by EventDataStore, which accepts an event data store ARN.
- [SearchSampleQueries](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_SearchSampleQueries.html): Searches sample queries and returns a list of sample queries that are sorted by relevance.
- [StartDashboardRefresh](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartDashboardRefresh.html): Starts a refresh of the specified dashboard.
- [StartEventDataStoreIngestion](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartEventDataStoreIngestion.html): Starts the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN.
- [StartImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartImport.html): Starts an import of logged trail events from a source S3 bucket to a destination event data store.
- [StartLogging](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartLogging.html): Starts the recording of AWS API calls and log file delivery for a trail.
- [StartQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StartQuery.html): Starts a CloudTrail Lake query.
- [StopEventDataStoreIngestion](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopEventDataStoreIngestion.html): Stops the ingestion of live events on an event data store specified as either an ARN or the ID portion of the ARN.
- [StopImport](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopImport.html): Stops a specified import.
- [StopLogging](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_StopLogging.html): Suspends the recording of AWS API calls and log file delivery for the specified trail.
- [UpdateChannel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateChannel.html): Updates a channel specified by a required channel ARN or UUID.
- [UpdateDashboard](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateDashboard.html): Updates the specified dashboard.
- [UpdateEventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateEventDataStore.html): Updates an event data store.
- [UpdateTrail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_UpdateTrail.html): Updates trail settings that control what events you are logging, and how to handle log files.


## [Data Types](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Types.html)

- [AdvancedEventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedEventSelector.html): Advanced event selectors let you create fine-grained selectors for AWS CloudTrail management, data, and network activity events.
- [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html): A single selector statement in an advanced event selector.
- [AggregationConfiguration](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AggregationConfiguration.html): An object that contains configuration settings for aggregating events.
- [Channel](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Channel.html): Contains information about a returned CloudTrail channel.
- [ContextKeySelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ContextKeySelector.html): An object that contains information types to be included in CloudTrail enriched events.
- [DashboardDetail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DashboardDetail.html): Provides information about a CloudTrail Lake dashboard.
- [DataResource](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_DataResource.html): You can configure the DataResource in an EventSelector to log data events for the following three resource types:
- [Destination](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Destination.html): Contains information about the destination receiving events.
- [Event](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Event.html): Contains information about an event that was returned by a lookup request.
- [EventDataStore](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_EventDataStore.html): A storage lake of event data against which you can run complex SQL-based queries.
- [EventSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_EventSelector.html): Use event selectors to further specify the management and data event settings for your trail.
- [ImportFailureListItem](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ImportFailureListItem.html): Provides information about an import failure.
- [ImportsListItem](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ImportsListItem.html): Contains information about an import that was returned by a lookup request.
- [ImportSource](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ImportSource.html): The import source.
- [ImportStatistics](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ImportStatistics.html): Provides statistics for the specified ImportID.
- [IngestionStatus](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_IngestionStatus.html): A table showing information about the most recent successful and failed attempts to ingest events.
- [InsightSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_InsightSelector.html): A JSON string that contains a list of Insights types that are logged on a trail or event data store.
- [LookupAttribute](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupAttribute.html): Specifies an attribute and value that filter the events returned.
- [PartitionKey](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PartitionKey.html): Contains information about a partition key for an event data store.
- [PublicKey](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PublicKey.html): Contains information about a returned public key.
- [Query](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Query.html): A SQL string of criteria about events that you want to collect in an event data store.
- [QueryStatistics](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_QueryStatistics.html): Metadata about a query, such as the number of results.
- [QueryStatisticsForDescribeQuery](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_QueryStatisticsForDescribeQuery.html): Gets metadata about a query, including the number of events that were matched, the total number of events scanned, the query run time in milliseconds, and the query's creation time.
- [RefreshSchedule](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RefreshSchedule.html): The schedule for a dashboard refresh.
- [RefreshScheduleFrequency](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RefreshScheduleFrequency.html): Specifies the frequency for a dashboard refresh schedule.
- [RequestWidget](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_RequestWidget.html): Contains information about a widget on a CloudTrail Lake dashboard.
- [Resource](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Resource.html): Specifies the type and name of a resource referenced by an event.
- [ResourceTag](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ResourceTag.html): A resource tag.
- [S3ImportSource](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_S3ImportSource.html): The settings for the source S3 bucket.
- [SearchSampleQueriesSearchResult](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_SearchSampleQueriesSearchResult.html): A search result returned by the SearchSampleQueries operation.
- [SourceConfig](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_SourceConfig.html): Contains configuration information about the channel.
- [Tag](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Tag.html): A custom key-value pair associated with a resource such as a CloudTrail trail, event data store, dashboard, or channel.
- [Trail](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Trail.html): The settings for a trail.
- [TrailInfo](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_TrailInfo.html): Information about a CloudTrail trail, including the trail's name, home Region, and Amazon Resource Name (ARN).
- [Widget](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_Widget.html): A widget on a CloudTrail Lake dashboard.
