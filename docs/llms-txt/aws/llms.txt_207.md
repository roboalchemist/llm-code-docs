# Source: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/llms.txt

# CloudWatch RUM API Reference

> With Amazon CloudWatch RUM, you can perform real-user monitoring to collect client-side data about your web application performance from actual user sessions in real time. The data collected includes page load times, client-side errors, and user behavior. When you view this data, you can see it all aggregated together and also see breakdowns by the browsers and devices that your customers use.

- [Welcome](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_Operations.html)

- [BatchCreateRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitions.html): Specifies the extended metrics and custom metrics that you want a CloudWatch RUM app monitor to send to a destination.
- [BatchDeleteRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitions.html): Removes the specified metrics from being sent to an extended metrics destination.
- [BatchGetRumMetricDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchGetRumMetricDefinitions.html): Retrieves the list of metrics and dimensions that a RUM app monitor is sending to a single destination.
- [CreateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CreateAppMonitor.html): Creates a Amazon CloudWatch RUM app monitor, which collects telemetry data from your application and sends that data to RUM.
- [DeleteAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteAppMonitor.html): Deletes an existing app monitor.
- [DeleteResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteResourcePolicy.html): Removes the association of a resource-based policy from an app monitor.
- [DeleteRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeleteRumMetricsDestination.html): Deletes a destination for CloudWatch RUM extended metrics, so that the specified app monitor stops sending extended metrics to that destination.
- [GetAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitor.html): Retrieves the complete configuration information for one app monitor.
- [GetAppMonitorData](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetAppMonitorData.html): Retrieves the raw performance events that RUM has collected from your web application, so that you can do your own processing or analysis of this data.
- [GetResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_GetResourcePolicy.html): Use this operation to retrieve information about a resource-based policy that is attached to an app monitor.
- [ListAppMonitors](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListAppMonitors.html): Returns a list of the Amazon CloudWatch RUM app monitors in the account.
- [ListRumMetricsDestinations](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListRumMetricsDestinations.html): Returns a list of destinations that you have created to receive RUM extended metrics, for the specified app monitor.
- [ListTagsForResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_ListTagsForResource.html): Displays the tags associated with a CloudWatch RUM resource.
- [PutResourcePolicy](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutResourcePolicy.html): Use this operation to assign a resource-based policy to a CloudWatch RUM app monitor to control access to it.
- [PutRumEvents](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumEvents.html): Sends telemetry events about your application performance and user behavior to CloudWatch RUM.
- [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html): Creates or updates a destination to receive extended metrics from CloudWatch RUM.
- [TagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified CloudWatch RUM resource.
- [UntagResource](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.
- [UpdateAppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateAppMonitor.html): Updates the configuration of an existing app monitor.
- [UpdateRumMetricDefinition](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UpdateRumMetricDefinition.html): Modifies one existing metric definition for CloudWatch RUM extended metrics.


## [Data Types](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_Types.html)

- [AppMonitor](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitor.html): A RUM app monitor collects telemetry data from your application and sends that data to RUM.
- [AppMonitorConfiguration](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitorConfiguration.html): This structure contains much of the configuration data for the app monitor.
- [AppMonitorDetails](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitorDetails.html): A structure that contains information about the RUM app monitor.
- [AppMonitorSummary](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_AppMonitorSummary.html): A structure that includes some data about app monitors and their settings.
- [BatchCreateRumMetricDefinitionsError](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitionsError.html): A structure that defines one error caused by a BatchCreateRumMetricsDefinitions operation.
- [BatchDeleteRumMetricDefinitionsError](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitionsError.html): A structure that defines one error caused by a BatchCreateRumMetricsDefinitions operation.
- [CustomEvents](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CustomEvents.html): A structure that contains information about custom events for this app monitor.
- [CwLog](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_CwLog.html): A structure that contains the information about whether the app monitor stores copies of the data that RUM collects in CloudWatch Logs.
- [DataStorage](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DataStorage.html): A structure that contains information about whether this app monitor stores a copy of the telemetry data that RUM collects using CloudWatch Logs.
- [DeobfuscationConfiguration](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_DeobfuscationConfiguration.html): A structure that contains the configuration for how an app monitor can deobfuscate stack traces.
- [JavaScriptSourceMaps](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_JavaScriptSourceMaps.html): A structure that contains the configuration for how an app monitor can unminify JavaScript error stack traces using source maps.
- [MetricDefinition](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_MetricDefinition.html): A structure that displays the definition of one extended metric that RUM sends to CloudWatch or CloudWatch Evidently.
- [MetricDefinitionRequest](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_MetricDefinitionRequest.html): Use this structure to define one extended metric or custom metric that RUM will send to CloudWatch or CloudWatch Evidently.
- [MetricDestinationSummary](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_MetricDestinationSummary.html): A structure that displays information about one destination that CloudWatch RUM sends extended metrics to.
- [QueryFilter](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_QueryFilter.html): A structure that defines a key and values that you can use to filter the results.
- [RumEvent](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_RumEvent.html): A structure that contains the information for one performance event that RUM collects from a user session with your application.
- [TimeRange](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TimeRange.html): A structure that defines the time range that you want to retrieve results from.
- [UserDetails](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_UserDetails.html): A structure that contains information about the user session that this batch of events was collected from.
