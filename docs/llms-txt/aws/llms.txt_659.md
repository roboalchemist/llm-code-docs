# Source: https://docs.aws.amazon.com/performance-insights/latest/APIReference/llms.txt

# Amazon RDS Performance Insights API Reference

> Amazon RDS Performance Insights enables you to monitor and explore different dimensions of database load based on data captured from a running DB instance. The guide provides detailed information about Performance Insights data types, parameters and errors.

- [Welcome](https://docs.aws.amazon.com/performance-insights/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/performance-insights/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/performance-insights/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Operations.html)

- [CreatePerformanceAnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_CreatePerformanceAnalysisReport.html): Creates a new performance analysis report for a specific time period for the DB instance.
- [DeletePerformanceAnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DeletePerformanceAnalysisReport.html): Deletes a performance analysis report.
- [DescribeDimensionKeys](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DescribeDimensionKeys.html): For a specific time period, retrieve the top N dimension keys for a metric.
- [GetDimensionKeyDetails](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetDimensionKeyDetails.html): Get the attributes of the specified dimension group for a DB instance or data source.
- [GetPerformanceAnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetPerformanceAnalysisReport.html): Retrieves the report including the report ID, status, time details, and the insights with recommendations.
- [GetResourceMetadata](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetadata.html): Retrieve the metadata for different features.
- [GetResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_GetResourceMetrics.html): Retrieve Performance Insights metrics for a set of data sources over a time period.
- [ListAvailableResourceDimensions](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceDimensions.html): Retrieve the dimensions that can be queried for each specified metric type on a specified DB instance.
- [ListAvailableResourceMetrics](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListAvailableResourceMetrics.html): Retrieve metrics of the specified types that can be queried for a specified DB instance.
- [ListPerformanceAnalysisReports](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListPerformanceAnalysisReports.html): Lists all the analysis reports created for the DB instance.
- [ListTagsForResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ListTagsForResource.html): Retrieves all the metadata tags associated with Amazon RDS Performance Insights resource.
- [TagResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_TagResource.html): Adds metadata tags to the Amazon RDS Performance Insights resource.
- [UntagResource](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_UntagResource.html): Deletes the metadata tags from the Amazon RDS Performance Insights resource.


## [Data Types](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Types.html)

- [AnalysisReport](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_AnalysisReport.html): Retrieves the summary of the performance analysis report created for a time period.
- [AnalysisReportSummary](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_AnalysisReportSummary.html): Retrieves the details of the performance analysis report.
- [Data](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Data.html): List of data objects which provide details about source metrics.
- [DataPoint](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DataPoint.html): A timestamp, and a single numerical value, which together represent a measurement at a particular point in time.
- [DimensionDetail](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionDetail.html): The information about a dimension.
- [DimensionGroup](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionGroup.html): A logical grouping of Performance Insights metrics for a related subject area.
- [DimensionGroupDetail](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionGroupDetail.html): Information about dimensions within a dimension group.
- [DimensionKeyDescription](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionKeyDescription.html): An object that includes the requested dimension key values and aggregated metric values within a dimension group.
- [DimensionKeyDetail](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionKeyDetail.html): An object that describes the details for a specified dimension.
- [FeatureMetadata](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_FeatureMetadata.html): The metadata for a feature.
- [Insight](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Insight.html): Retrieves the list of performance issues which are identified.
- [MetricDimensionGroups](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_MetricDimensionGroups.html): The available dimension information for a metric type.
- [MetricKeyDataPoints](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_MetricKeyDataPoints.html): A time-ordered series of data points, corresponding to a dimension of a Performance Insights metric.
- [MetricQuery](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_MetricQuery.html): A single query to be processed.
- [PerformanceInsightsMetric](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_PerformanceInsightsMetric.html): This data type helps to determine Performance Insights metric to render for the insight.
- [Recommendation](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Recommendation.html): The list of recommendations for the insight.
- [ResponsePartitionKey](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ResponsePartitionKey.html): If PartitionBy was specified in a DescribeDimensionKeys request, the dimensions are returned in an array.
- [ResponseResourceMetric](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ResponseResourceMetric.html): An object that contains the full name, description, and unit of a metric.
- [ResponseResourceMetricKey](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_ResponseResourceMetricKey.html): An object describing a Performance Insights metric and one or more dimensions for that metric.
- [Tag](https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_Tag.html): Metadata assigned to an Amazon RDS resource consisting of a key-value pair.
