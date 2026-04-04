# Source: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/llms.txt

# Amazon CloudWatch API Reference

> Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are the variables you want to measure for your resources and applications.

- [Welcome](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/Welcome.html)
- [Dashboard Body Structure and Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html)
- [GetMetricWidgetImage: Metric Widget Structure and Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Metric-Widget-Structure.html)
- [Making API Requests](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/making-api-requests.html)
- [Common Parameters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Operations.html)

- [DeleteAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarmMuteRule.html): Deletes a specific alarm mute rule.
- [DeleteAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAlarms.html): Deletes the specified alarms.
- [DeleteAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteAnomalyDetector.html): Deletes the specified anomaly detection model from your account.
- [DeleteDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteDashboards.html): Deletes all dashboards that you specify.
- [DeleteInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteInsightRules.html): Permanently deletes the specified Contributor Insights rules.
- [DeleteMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DeleteMetricStream.html): Permanently deletes the metric stream that you specify.
- [DescribeAlarmContributors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmContributors.html): Returns the information of the current alarm contributors that are in ALARM state.
- [DescribeAlarmHistory](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html): Retrieves the history for the specified alarm.
- [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html): Retrieves the specified alarms.
- [DescribeAlarmsForMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmsForMetric.html): Retrieves the alarms for the specified metric.
- [DescribeAnomalyDetectors](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAnomalyDetectors.html): Lists the anomaly detection models that you have created in your account.
- [DescribeInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html): Returns a list of all the Contributor Insights rules in your account.
- [DisableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableAlarmActions.html): Disables the actions for the specified alarms.
- [DisableInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableInsightRules.html): Disables the specified Contributor Insights rules.
- [EnableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html): Enables the actions for the specified alarms.
- [EnableInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableInsightRules.html): Enables the specified Contributor Insights rules.
- [GetAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetAlarmMuteRule.html): Retrieves details for a specific alarm mute rule.
- [GetDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetDashboard.html): Displays the details of the dashboard that you specify.
- [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html): This operation returns the time series data collected by a Contributor Insights rule.
- [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html): You can use the GetMetricData API to retrieve CloudWatch metric values.
- [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html): Gets statistics for the specified metric.
- [GetMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStream.html): Returns information about the metric stream that you specify.
- [GetMetricWidgetImage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricWidgetImage.html): You can use the GetMetricWidgetImage API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image.
- [ListAlarmMuteRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListAlarmMuteRules.html): Lists alarm mute rules in your AWS account and region.
- [ListDashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListDashboards.html): Returns a list of the dashboards for your account.
- [ListManagedInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListManagedInsightRules.html): Returns a list that contains the number of managed Contributor Insights rules in your account.
- [ListMetrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html): List the specified metrics.
- [ListMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetricStreams.html): Returns a list of metric streams in this account.
- [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListTagsForResource.html): Displays the tags associated with a CloudWatch resource.
- [PutAlarmMuteRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutAlarmMuteRule.html): Creates or updates an alarm mute rule.
- [PutAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutAnomalyDetector.html): Creates an anomaly detection model for a CloudWatch metric.
- [PutCompositeAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutCompositeAlarm.html): Creates or updates a composite alarm.
- [PutDashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutDashboard.html): Creates a dashboard if it does not already exist, or updates an existing dashboard.
- [PutInsightRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutInsightRule.html): Creates a Contributor Insights rule.
- [PutManagedInsightRules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutManagedInsightRules.html): Creates a managed Contributor Insights rule for a specified AWS resource.
- [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html): Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, or Metrics Insights query.
- [PutMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricData.html): Publishes metric data to Amazon CloudWatch.
- [PutMetricStream](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricStream.html): Creates or updates a metric stream.
- [SetAlarmState](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SetAlarmState.html): Temporarily sets the state of an alarm for testing purposes.
- [StartMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartMetricStreams.html): Starts the streaming of metrics for one or more of your metric streams.
- [StopMetricStreams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StopMetricStreams.html): Stops the streaming of metrics for one or more of your metric streams.
- [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html): Assigns one or more tags (key-value pairs) to the specified CloudWatch resource.
- [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html): Removes one or more tags from the specified resource.


## [Data Types](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Types.html)

- [AlarmContributor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmContributor.html): Represents an individual contributor to a multi-timeseries alarm, containing information about a specific time series and its contribution to the alarm's state.
- [AlarmHistoryItem](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmHistoryItem.html): Represents the history of a specific alarm.
- [AlarmMuteRuleSummary](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AlarmMuteRuleSummary.html): Summary information about an alarm mute rule, including its name, status, and configuration details.
- [AnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AnomalyDetector.html): An anomaly detection model associated with a particular CloudWatch metric, statistic, or metric math expression.
- [AnomalyDetectorConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AnomalyDetectorConfiguration.html): The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude from use for training the model and the time zone to use for the metric.
- [CompositeAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CompositeAlarm.html): The details about a composite alarm.
- [DashboardEntry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DashboardEntry.html): Represents a specific dashboard.
- [DashboardValidationMessage](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DashboardValidationMessage.html): An error or warning for the operation.
- [Datapoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Datapoint.html): Encapsulates the statistical data that CloudWatch computes from metric data.
- [Dimension](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Dimension.html): A dimension is a name/value pair that is part of the identity of a metric.
- [DimensionFilter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DimensionFilter.html): Represents filters for a dimension.
- [Entity](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Entity.html): An entity associated with metrics, to allow for finding related telemetry.
- [EntityMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EntityMetricData.html): A set of metrics that are associated with an entity, such as a specific service or resource.
- [InsightRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRule.html): This structure contains the definition for a Contributor Insights rule.
- [InsightRuleContributor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleContributor.html): One of the unique contributors found by a Contributor Insights rule.
- [InsightRuleContributorDatapoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleContributorDatapoint.html): One data point related to one contributor.
- [InsightRuleMetricDatapoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleMetricDatapoint.html): One data point from the metric time series returned in a Contributor Insights rule report.
- [LabelOptions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_LabelOptions.html): This structure includes the Timezone parameter, which you can use to specify your time zone so that the labels that are associated with returned metrics display the correct time for your time zone.
- [ManagedRule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ManagedRule.html): Contains the information that's required to enable a managed Contributor Insights rule for an AWS resource.
- [ManagedRuleDescription](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ManagedRuleDescription.html): Contains information about managed Contributor Insights rules, as returned by ListManagedInsightRules.
- [ManagedRuleState](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ManagedRuleState.html): The status of a managed Contributor Insights rule.
- [MessageData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MessageData.html): A message returned by the GetMetricDataAPI, including a code and a description.
- [Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Metric.html): Represents a specific metric.
- [MetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricAlarm.html): The details about a metric alarm.
- [MetricCharacteristics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricCharacteristics.html): This object includes parameters that you can use to provide information to CloudWatch to help it build more accurate anomaly detection models.
- [MetricDataQuery](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataQuery.html): This structure is used in both GetMetricData and PutMetricAlarm.
- [MetricDataResult](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataResult.html): A GetMetricData call returns an array of MetricDataResult structures.
- [MetricDatum](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html): Encapsulates the information sent to either create a metric or add new values to be aggregated into an existing metric.
- [MetricMathAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricMathAnomalyDetector.html): Indicates the CloudWatch math expression that provides the time series the anomaly detector uses as input.
- [MetricStat](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStat.html): This structure defines the metric to be returned, along with the statistics, period, and units.
- [MetricStreamEntry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStreamEntry.html): This structure contains the configuration information about one metric stream.
- [MetricStreamFilter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStreamFilter.html): This structure contains a metric namespace and optionally, a list of metric names, to either include in a metric stream or exclude from a metric stream.
- [MetricStreamStatisticsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStreamStatisticsConfiguration.html): By default, a metric stream always sends the MAX, MIN, SUM, and SAMPLECOUNT statistics for each metric that is streamed.
- [MetricStreamStatisticsMetric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStreamStatisticsMetric.html): This object contains the information for one metric that is to be streamed with additional statistics.
- [MuteTargets](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MuteTargets.html): Specifies which alarms an alarm mute rule applies to.
- [PartialFailure](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PartialFailure.html): This array is empty if the API operation was successful for all the rules specified in the request.
- [Range](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Range.html): Specifies one range of days or times to exclude from use for training an anomaly detection model.
- [Rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Rule.html): Defines the schedule configuration for an alarm mute rule.
- [Schedule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Schedule.html): Specifies when and how long an alarm mute rule is active.
- [SingleMetricAnomalyDetector](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SingleMetricAnomalyDetector.html): Designates the CloudWatch metric and statistic that provides the time series the anomaly detector uses as input.
- [StatisticSet](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StatisticSet.html): Represents a set of statistics that describes a specific metric.
- [Tag](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_Tag.html): A key-value pair associated with a CloudWatch resource.
