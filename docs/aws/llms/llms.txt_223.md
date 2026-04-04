# Source: https://docs.aws.amazon.com/codeguru/latest/profiler-api/llms.txt

# Amazon CodeGuru Profiler API Reference

> This section provides documentation for the Amazon CodeGuru Profiler API operations.

- [Welcome](https://docs.aws.amazon.com/codeguru/latest/profiler-api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/codeguru/latest/profiler-api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/codeguru/latest/profiler-api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Operations.html)

- [AddNotificationChannels](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AddNotificationChannels.html): Add up to 2 anomaly notifications channels for a profiling group.
- [BatchGetFrameMetricData](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_BatchGetFrameMetricData.html): Returns the time series of values for a requested list of frame metrics from a time period.
- [ConfigureAgent](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html): Used by profiler agents to report their current state and to receive remote configuration updates.
- [CreateProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_CreateProfilingGroup.html): Creates a profiling group.
- [DeleteProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_DeleteProfilingGroup.html): Deletes a profiling group.
- [DescribeProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_DescribeProfilingGroup.html): Returns a ProfilingGroupDescription object that contains information about the requested profiling group.
- [GetFindingsReportAccountSummary](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetFindingsReportAccountSummary.html): Returns a list of FindingsReportSummary objects that contain analysis results for all profiling groups in your AWS account.
- [GetNotificationConfiguration](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetNotificationConfiguration.html): Get the current configuration for anomaly notifications for a profiling group.
- [GetPolicy](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetPolicy.html): Returns the JSON-formatted resource-based policy on a profiling group.
- [GetProfile](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html): Gets the aggregated profile of a profiling group for a specified time range.
- [GetRecommendations](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetRecommendations.html): Returns a list of Recommendation objects that contain recommendations for a profiling group for a given time period.
- [ListFindingsReports](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListFindingsReports.html): List the available reports for a given profiling group and time range.
- [ListProfileTimes](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html): Lists the start times of the available aggregated profiles of a profiling group for an aggregation period within the specified time range.
- [ListProfilingGroups](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfilingGroups.html): Returns a list of profiling groups.
- [ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListTagsForResource.html): Returns a list of the tags that are assigned to a specified resource.
- [PostAgentProfile](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html): Submits profiling data to an aggregated profile of a profiling group.
- [PutPermission](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PutPermission.html): Adds permissions to a profiling group's resource-based policy that are provided using an action group.
- [RemoveNotificationChannel](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_RemoveNotificationChannel.html): Remove one anomaly notifications channel for a profiling group.
- [RemovePermission](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_RemovePermission.html): Removes permissions from a profiling group's resource-based policy that are provided using an action group.
- [SubmitFeedback](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_SubmitFeedback.html): Sends feedback to CodeGuru Profiler about whether the anomaly detected by the analysis is useful or not.
- [TagResource](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_TagResource.html): Use to assign one or more tags to a resource.
- [UntagResource](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_UntagResource.html): Use to remove one or more tags from a resource.
- [UpdateProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_UpdateProfilingGroup.html): Updates a profiling group.


## [Data Types](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Types.html)

- [AgentConfiguration](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentConfiguration.html): The response of ConfigureAgent that specifies if an agent profiles or not and for how long to return profiling data.
- [AgentOrchestrationConfig](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig.html): Specifies whether profiling is enabled or disabled for a profiling group.
- [AggregatedProfileTime](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html): Specifies the aggregation period and aggregation start time for an aggregated profile.
- [Anomaly](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly.html): Details about an anomaly in a specific metric of application profile.
- [AnomalyInstance](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html): The specific duration in which the metric is flagged as anomalous.
- [Channel](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Channel.html): Notification medium for users to get alerted for events that occur in application profile.
- [FindingsReportSummary](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html): Information about potential recommendations that might be created from the analysis of profiling data.
- [FrameMetric](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FrameMetric.html): The frame name, metric type, and thread states.
- [FrameMetricDatum](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FrameMetricDatum.html): Information about a frame metric and its values.
- [Match](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Match.html): The part of a profile that contains a recommendation found during analysis.
- [Metric](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Metric.html): Details about the metric that the analysis used when it detected the anomaly.
- [NotificationConfiguration](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_NotificationConfiguration.html): The configuration for notifications stored for each profiling group.
- [Pattern](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Pattern.html): A set of rules used to make a recommendation during an analysis.
- [ProfileTime](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfileTime.html): Contains the start time of a profile.
- [ProfilingGroupDescription](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html): Contains information about a profiling group.
- [ProfilingStatus](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus.html): Profiling status includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.
- [Recommendation](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html): A potential improvement that was found from analyzing the profiling data.
- [TimestampStructure](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_TimestampStructure.html): A data type that contains a Timestamp object.
- [UserFeedback](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_UserFeedback.html): Feedback that can be submitted for each instance of an anomaly by the user.
