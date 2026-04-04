# Source: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/llms.txt

# AWS Billing and Cost Management API Reference

## [AWS Cost Explorer](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Cost_Explorer_Service.html)

You can use the Cost Explorer API to programmatically query your cost and usage data. You can query for aggregated data such as total monthly costs or total daily usage. You can also query for granular data. This might include the number of daily write operations for Amazon DynamoDB database tables in your production environment.

Service Endpoint

The Cost Explorer API provides the following endpoint:

- `https://ce.us-east-1.amazonaws.com`

For information about the costs that are associated with the Cost Explorer API, see [AWS Cost Management Pricing](http://aws.amazon.com/aws-cost-management/pricing/).

### Actions

- [CreateAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateAnomalyMonitor.html): Creates a new cost anomaly detection monitor with the requested type and monitor specification.
- [CreateAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateAnomalySubscription.html): Adds an alert subscription to a cost anomaly detection monitor.
- [CreateCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CreateCostCategoryDefinition.html): Creates a new cost category with the requested name and rules.
- [DeleteAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalyMonitor.html): Deletes a cost anomaly monitor.
- [DeleteAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteAnomalySubscription.html): Deletes a cost anomaly subscription.
- [DeleteCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DeleteCostCategoryDefinition.html): Deletes a cost category.
- [DescribeCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DescribeCostCategoryDefinition.html): Returns the name, Amazon Resource Name (ARN), rules, definition, and effective dates of a cost category that's defined in the account.
- [GetAnomalies](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalies.html): Retrieves all of the cost anomalies detected on your account during the time period that's specified by the DateInterval object.
- [GetAnomalyMonitors](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalyMonitors.html): Retrieves the cost anomaly monitor definitions for your account.
- [GetAnomalySubscriptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalySubscriptions.html): Retrieves the cost anomaly subscription objects for your account.
- [GetApproximateUsageRecords](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetApproximateUsageRecords.html): Retrieves estimated usage records for hourly granularity or resource-level data at daily granularity.
- [GetCommitmentPurchaseAnalysis](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCommitmentPurchaseAnalysis.html): Retrieves a commitment purchase analysis result based on the AnalysisId.
- [GetCostAndUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsage.html): Retrieves cost and usage metrics for your account.
- [GetCostAndUsageComparisons](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsageComparisons.html): Retrieves cost and usage comparisons for your account between two periods within the last 13 months.
- [GetCostAndUsageWithResources](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostAndUsageWithResources.html): Retrieves cost and usage metrics with resources for your account.
- [GetCostCategories](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostCategories.html): Retrieves an array of cost category names and values incurred cost.
- [GetCostComparisonDrivers](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostComparisonDrivers.html): Retrieves key factors driving cost changes between two time periods within the last 13 months, such as usage changes, discount changes, and commitment-based savings.
- [GetCostForecast](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetCostForecast.html): Retrieves a forecast for how much Amazon Web Services predicts that you will spend over the forecast time period that you select, based on your past costs.
- [GetDimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetDimensionValues.html): Retrieves all available filter values for a specified filter over a period of time.
- [GetReservationCoverage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationCoverage.html): Retrieves the reservation coverage for your account, which you can use to see how much of your Amazon Elastic Compute Cloud, Amazon ElastiCache, Amazon Relational Database Service, or Amazon Redshift usage is covered by a reservation.
- [GetReservationPurchaseRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationPurchaseRecommendation.html): Gets recommendations for reservation purchases.
- [GetReservationUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetReservationUtilization.html): Retrieves the reservation utilization for your account.
- [GetRightsizingRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetRightsizingRecommendation.html): Creates recommendations that help you save cost by identifying idle and underutilized Amazon EC2 instances.
- [GetSavingsPlanPurchaseRecommendationDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlanPurchaseRecommendationDetails.html): Retrieves the details for a Savings Plan recommendation.
- [GetSavingsPlansCoverage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansCoverage.html): Retrieves the Savings Plans covered for your account.
- [GetSavingsPlansPurchaseRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansPurchaseRecommendation.html): Retrieves the Savings Plans recommendations for your account.
- [GetSavingsPlansUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilization.html): Retrieves the Savings Plans utilization for your account across date ranges with daily or monthly granularity.
- [GetSavingsPlansUtilizationDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetSavingsPlansUtilizationDetails.html): Retrieves attribute data along with aggregate utilization and savings data for a given time period.
- [GetTags](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetTags.html): Queries for available tag keys and tag values for a specified period.
- [GetUsageForecast](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetUsageForecast.html): Retrieves a forecast for how much Amazon Web Services predicts that you will use over the forecast time period that you select, based on your past usage.
- [ListCommitmentPurchaseAnalyses](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCommitmentPurchaseAnalyses.html): Lists the commitment purchase analyses for your account.
- [ListCostAllocationTagBackfillHistory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostAllocationTagBackfillHistory.html): Retrieves a list of your historical cost allocation tag backfill requests.
- [ListCostAllocationTags](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostAllocationTags.html): Get a list of cost allocation tags.
- [ListCostCategoryDefinitions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostCategoryDefinitions.html): Returns the name, Amazon Resource Name (ARN), NumberOfRules and effective dates of all cost categories defined in the account.
- [ListCostCategoryResourceAssociations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListCostCategoryResourceAssociations.html): Returns resource associations of all cost categories defined in the account.
- [ListSavingsPlansPurchaseRecommendationGeneration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListSavingsPlansPurchaseRecommendationGeneration.html): Retrieves a list of your historical recommendation generations within the past 30 days.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ListTagsForResource.html): Returns a list of resource tags associated with the resource specified by the Amazon Resource Name (ARN).
- [ProvideAnomalyFeedback](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ProvideAnomalyFeedback.html): Modifies the feedback property of a given cost anomaly.
- [StartCommitmentPurchaseAnalysis](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartCommitmentPurchaseAnalysis.html): Specifies the parameters of a planned commitment purchase and starts the generation of the analysis.
- [StartCostAllocationTagBackfill](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartCostAllocationTagBackfill.html): Request a cost allocation tag backfill.
- [StartSavingsPlansPurchaseRecommendationGeneration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_StartSavingsPlansPurchaseRecommendationGeneration.html): Requests a Savings Plans recommendation generation.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TagResource.html): An API operation for adding one or more tags (key-value pairs) to a resource.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UntagResource.html): Removes one or more tags from a resource.
- [UpdateAnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalyMonitor.html): Updates an existing cost anomaly monitor.
- [UpdateAnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateAnomalySubscription.html): Updates an existing cost anomaly subscription.
- [UpdateCostAllocationTagsStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatus.html): Updates status for cost allocation tags in bulk, with maximum batch size of 20.
- [UpdateCostCategoryDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostCategoryDefinition.html): Updates an existing cost category.

### Data Types

- [AnalysisDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnalysisDetails.html): Details about the analysis.
- [AnalysisSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnalysisSummary.html): A summary of the analysis.
- [Anomaly](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Anomaly.html): An unusual cost pattern.
- [AnomalyDateInterval](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyDateInterval.html): The time period for an anomaly.
- [AnomalyMonitor](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html): This object continuously inspects your account's cost data for anomalies.
- [AnomalyScore](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyScore.html): Quantifies the anomaly.
- [AnomalySubscription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalySubscription.html): An AnomalySubscription resource (also referred to as an alert subscription) sends notifications about specific anomalies that meet an alerting criteria defined by you.
- [CommitmentPurchaseAnalysisConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CommitmentPurchaseAnalysisConfiguration.html): The configuration for the commitment purchase analysis.
- [ComparisonMetricValue](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ComparisonMetricValue.html): Contains cost or usage metric values for comparing two time periods.
- [CostAllocationTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAllocationTag.html): The cost allocation tag structure.
- [CostAllocationTagBackfillRequest](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAllocationTagBackfillRequest.html): The cost allocation tag backfill request structure that contains metadata and details of a certain backfill.
- [CostAllocationTagStatusEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAllocationTagStatusEntry.html): The cost allocation tag status.
- [CostAndUsageComparison](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostAndUsageComparison.html): Represents a comparison of cost and usage metrics between two time periods.
- [CostCategory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategory.html): The structure of Cost Categories.
- [CostCategoryInheritedValueDimension](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryInheritedValueDimension.html): When you create or update a cost category, you can define the CostCategoryRule rule type as INHERITED_VALUE.
- [CostCategoryProcessingStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryProcessingStatus.html): The list of processing statuses for Cost Management products for a specific cost category.
- [CostCategoryReference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryReference.html): A reference to a cost category containing only enough information to identify the Cost Category.
- [CostCategoryResourceAssociation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryResourceAssociation.html): A reference to a cost category association that contains information on an associated resource.
- [CostCategoryRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html): Rules are processed in order.
- [CostCategorySplitChargeRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategorySplitChargeRule.html): Use the split charge rule to split the cost of one cost category value across several other target values.
- [CostCategorySplitChargeRuleParameter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategorySplitChargeRuleParameter.html): The parameters for a split charge method.
- [CostCategoryValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryValues.html): The Cost Categories values used for filtering the costs.
- [CostComparisonDriver](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostComparisonDriver.html): Represents a collection of cost drivers and their associated metrics for cost comparison analysis.
- [CostDriver](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostDriver.html): Represents factors that contribute to cost variations between the baseline and comparison time periods, including the type of driver, an identifier of the driver, and associated metrics.
- [Coverage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Coverage.html): The amount of instance usage that a reservation covered.
- [CoverageByTime](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageByTime.html): Reservation coverage for a specified period, in hours.
- [CoverageCost](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageCost.html): How much it costs to run an instance.
- [CoverageHours](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageHours.html): How long a running instance either used a reservation or was On-Demand.
- [CoverageNormalizedUnits](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CoverageNormalizedUnits.html): The amount of instance usage, in normalized units.
- [CurrentInstance](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CurrentInstance.html): Context about the current instance.
- [DateInterval](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DateInterval.html): The time period of the request.
- [DimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValues.html): The metadata that you can use to filter and group your results.
- [DimensionValuesWithAttributes](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DimensionValuesWithAttributes.html): The metadata of a specific type that you can use to filter and group your results.
- [DiskResourceUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DiskResourceUtilization.html): The field that contains a list of disk (local storage) metrics that are associated with the current instance.
- [DynamoDBCapacityDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DynamoDBCapacityDetails.html): The DynamoDB reservations that AWS recommends that you purchase.
- [EBSResourceUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EBSResourceUtilization.html): The EBS field that contains a list of EBS metrics that are associated with the current instance.
- [EC2InstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2InstanceDetails.html): Details about the Amazon EC2 reservations that AWS recommends that you purchase.
- [EC2ResourceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2ResourceDetails.html): Details on the Amazon EC2 Resource.
- [EC2ResourceUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2ResourceUtilization.html): Utilization metrics for the instance.
- [EC2Specification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_EC2Specification.html): The Amazon EC2 hardware specifications that you want AWS to provide recommendations for.
- [ElastiCacheInstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ElastiCacheInstanceDetails.html): Details about the Amazon ElastiCache reservations that AWS recommends that you purchase.
- [ESInstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ESInstanceDetails.html): Details about the Amazon OpenSearch Service reservations that AWS recommends that you purchase.
- [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html): Use Expression to filter in various Cost Explorer APIs.
- [ForecastResult](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ForecastResult.html): The forecast that's created for your query.
- [GenerationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GenerationSummary.html): The summary of the Savings Plans recommendation generation.
- [Group](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Group.html): One level of grouped data in the results.
- [GroupDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GroupDefinition.html): Represents a group when you specify a group by criteria or in the response to a query with a specific grouping.
- [Impact](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Impact.html): The dollar value of the anomaly.
- [InstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_InstanceDetails.html): Details about the reservations that AWS recommends that you purchase.
- [MemoryDBInstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_MemoryDBInstanceDetails.html): Details about the MemoryDB reservations that AWS recommends that you purchase.
- [MetricValue](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_MetricValue.html): The aggregated value for a metric.
- [ModifyRecommendationDetail](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ModifyRecommendationDetail.html): Details for the modification recommendation.
- [NetworkResourceUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_NetworkResourceUtilization.html): The network field that contains a list of network metrics that are associated with the current instance.
- [RDSInstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RDSInstanceDetails.html): Details about the Amazon RDS reservations that AWS recommends that you purchase.
- [RecommendationDetailData](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RecommendationDetailData.html): The details and metrics for the given recommendation.
- [RecommendationDetailHourlyMetrics](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RecommendationDetailHourlyMetrics.html): Contains the hourly metrics for the given recommendation over the lookback period.
- [RedshiftInstanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RedshiftInstanceDetails.html): Details about the Amazon Redshift reservations that AWS recommends that you purchase.
- [ReservationAggregates](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationAggregates.html): The aggregated numbers for your reservation usage.
- [ReservationCoverageGroup](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationCoverageGroup.html): A group of reservations that share a set of attributes.
- [ReservationPurchaseRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendation.html): A specific reservation that AWS recommends for purchase.
- [ReservationPurchaseRecommendationDetail](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationDetail.html): Details about your recommended reservation purchase.
- [ReservationPurchaseRecommendationMetadata](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationMetadata.html): Information about a recommendation, such as the timestamp for when AWS made a specific recommendation.
- [ReservationPurchaseRecommendationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationPurchaseRecommendationSummary.html): A summary about this recommendation, such as the currency code, the amount that AWS estimates that you could save, and the total amount of reservation to purchase.
- [ReservationUtilizationGroup](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservationUtilizationGroup.html): A group of reservations that share a set of attributes.
- [ReservedCapacityDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ReservedCapacityDetails.html): Details about the reservations that AWS recommends that you purchase.
- [ResourceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceDetails.html): Details for the resource.
- [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html): The tag structure that contains a tag key and value.
- [ResourceUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceUtilization.html): Resource utilization of current resource.
- [ResultByTime](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResultByTime.html): The result that's associated with a time period.
- [RightsizingRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendation.html): Recommendations to rightsize resources.
- [RightsizingRecommendationConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendationConfiguration.html): You can use RightsizingRecommendationConfiguration to customize recommendations across two attributes.
- [RightsizingRecommendationMetadata](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendationMetadata.html): Metadata for a recommendation set.
- [RightsizingRecommendationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RightsizingRecommendationSummary.html): The summary of rightsizing recommendations
- [RootCause](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RootCause.html): The combination of AWS service, linked account, linked account name, Region, and usage type where a cost anomaly is observed, along with the dollar and percentage amount of the anomaly impact.
- [RootCauseImpact](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_RootCauseImpact.html): The dollar value of the root cause.
- [SavingsPlans](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlans.html): The Savings Plans commitment details.
- [SavingsPlansAmortizedCommitment](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansAmortizedCommitment.html): The amortized amount of Savings Plans purchased in a specific account during a specific time interval.
- [SavingsPlansCoverage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansCoverage.html): The amount of Savings Plans eligible usage that's covered by Savings Plans.
- [SavingsPlansCoverageData](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansCoverageData.html): Specific coverage percentage, On-Demand costs, and spend covered by Savings Plans, and total Savings Plans costs for an account.
- [SavingsPlansDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansDetails.html): The attribute details on a specific Savings Plan.
- [SavingsPlansPurchaseAnalysisConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseAnalysisConfiguration.html): The configuration for the Savings Plans purchase analysis.
- [SavingsPlansPurchaseAnalysisDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseAnalysisDetails.html): Details about the Savings Plans purchase analysis.
- [SavingsPlansPurchaseRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendation.html): Contains your request parameters, Savings Plan Recommendations Summary, and Details.
- [SavingsPlansPurchaseRecommendationDetail](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendationDetail.html): Details for your recommended Savings Plans.
- [SavingsPlansPurchaseRecommendationMetadata](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendationMetadata.html): Metadata about your Savings Plans Purchase Recommendations.
- [SavingsPlansPurchaseRecommendationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansPurchaseRecommendationSummary.html): Summary metrics for your Savings Plans Purchase Recommendations.
- [SavingsPlansSavings](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansSavings.html): The amount of savings that you're accumulating, against the public On-Demand rate of the usage accrued in an account.
- [SavingsPlansUtilization](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansUtilization.html): The measurement of how well you're using your existing Savings Plans.
- [SavingsPlansUtilizationAggregates](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansUtilizationAggregates.html): The aggregated utilization metrics for your Savings Plans usage.
- [SavingsPlansUtilizationByTime](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansUtilizationByTime.html): The amount of Savings Plans utilization (in hours).
- [SavingsPlansUtilizationDetail](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SavingsPlansUtilizationDetail.html): A single daily or monthly Savings Plans utilization rate and details for your account.
- [ServiceSpecification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ServiceSpecification.html): Hardware specifications for the service that you want recommendations for.
- [SortDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_SortDefinition.html): The details for how to sort the data.
- [Subscriber](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Subscriber.html): The recipient of AnomalySubscription notifications.
- [TagValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TagValues.html): The values that are available for a tag.
- [TargetInstance](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TargetInstance.html): Details on recommended instance.
- [TerminateRecommendationDetail](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TerminateRecommendationDetail.html): Details on termination recommendation.
- [TotalImpactFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_TotalImpactFilter.html): Filters cost anomalies based on the total impact.
- [UpdateCostAllocationTagsStatusError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UpdateCostAllocationTagsStatusError.html): Gives a detailed description of the result of an action.
- [UtilizationByTime](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_UtilizationByTime.html): The amount of utilization, in hours.

## [AWS Billing and Cost Management Dashboards](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Billing_and_Cost_Management_Dashboards.html)

AWS Billing and Cost Management Dashboards is a service that enables you to create, manage, and share dashboards that combine multiple visualizations of your AWS cost and usage data. You can combine multiple data sources including Cost Explorer, Savings Plans, and Reserved Instance metrics into unified dashboards, helping you analyze spending patterns and share cost insights across your organization.

You can use the AWS Billing and Cost Management Dashboards API to programmatically create, manage, and share dashboards. This includes creating custom dashboards, configuring widgets, managing dashboard permissions, and sharing dashboards across accounts in your organization.

### Actions

- [CreateDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CreateDashboard.html): Creates a new dashboard that can contain multiple widgets displaying cost and usage data.
- [DeleteDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DeleteDashboard.html): Deletes a specified dashboard.
- [GetDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetDashboard.html): Retrieves the configuration and metadata of a specified dashboard, including its widgets and layout settings.
- [GetResourcePolicy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GetResourcePolicy.html): Retrieves the resource-based policy attached to a dashboard, showing sharing configurations and permissions.
- [ListDashboards](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListDashboards.html): Returns a list of all dashboards in your account.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ListTagsForResource.html): Returns a list of all tags associated with a specified dashboard resource.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_TagResource.html): Adds or updates tags for a specified dashboard resource.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UntagResource.html): Removes specified tags from a dashboard resource.
- [UpdateDashboard](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_UpdateDashboard.html): Updates an existing dashboard's properties, including its name, description, and widget configurations.

### Data Types

- [CostAndUsageQuery](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CostAndUsageQuery.html): Defines the parameters for retrieving AWS cost and usage data.
- [CostCategoryValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_CostCategoryValues.html): Specifies the values and match options for cost category-based filtering in cost and usage queries.
- [DashboardReference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DashboardReference.html): Contains basic information about a dashboard, including its ARN, name, type, and timestamps.
- [DateTimeRange](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DateTimeRange.html): Defines a time period with explicit start and end times for data queries.
- [DateTimeValue](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DateTimeValue.html): Represents a point in time that can be specified as either an absolute date (for example, "2025-07-01") or a relative time period using ISO 8601 duration format (for example, "-P3M" for three months ago).
- [DimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DimensionValues.html): Specifies the values and match options for dimension-based filtering in cost and usage queries.
- [DisplayConfig](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DisplayConfig.html): Defines how the widget's data should be visualized, including chart type, color schemes, axis configurations, and other display preferences.
- [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_Expression.html): Defines complex filtering conditions using logical operators (AND, OR, NOT) and various filter types.
- [GraphDisplayConfig](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GraphDisplayConfig.html): Defines the visual representation settings for widget data, including the visualization type, styling options, and display preferences for different metric types.
- [GroupDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_GroupDefinition.html): Specifies how to group cost and usage data.
- [QueryParameters](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_QueryParameters.html): Defines the data retrieval parameters for a widget.
- [ReservationCoverageQuery](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ReservationCoverageQuery.html): Defines the parameters for querying Reserved Instance coverage data, including grouping options, metrics, and sorting preferences.
- [ReservationUtilizationQuery](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ReservationUtilizationQuery.html): Defines the parameters for querying Reserved Instance utilization data, including grouping options and time granularity.
- [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_ResourceTag.html): A key-value pair that can be attached to a dashboard for organization and management purposes.
- [SavingsPlansCoverageQuery](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_SavingsPlansCoverageQuery.html): Defines the parameters for querying Savings Plans coverage data, including metrics, grouping options, and time granularity.
- [SavingsPlansUtilizationQuery](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_SavingsPlansUtilizationQuery.html): Defines the parameters for querying Savings Plans utilization data, including time granularity and sorting preferences.
- [TableDisplayConfigStruct](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_TableDisplayConfigStruct.html): Configuration structure for customizing the tabular display of widget data.
- [TagValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_TagValues.html): Specifies tag-based filtering options for cost and usage queries.
- [Widget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_Widget.html): A configurable visualization component within a dashboard that displays specific cost and usage metrics.
- [WidgetConfig](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_WidgetConfig.html): Defines the complete configuration for a widget, including data retrieval settings and visualization preferences.

## [AWS Data Exports](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Billing_and_Cost_Management_Data_Exports.html)

You can use the Data Exports API to create customized exports from multiple AWS cost management and billing datasets, such as cost and usage data and cost optimization recommendations.

The Data Exports API provides the following endpoint:

- https://bcm-data-exports.us-east-1.api.aws

### Actions

- [CreateExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_CreateExport.html): Creates a data export and specifies the data query, the delivery preference, and any optional resource tags.
- [DeleteExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_DeleteExport.html): Deletes an existing data export.
- [GetExecution](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetExecution.html): Exports data based on the source data update.
- [GetExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetExport.html): Views the definition of an existing data export.
- [GetTable](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_GetTable.html): Returns the metadata for the specified table and table properties.
- [ListExecutions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListExecutions.html): Lists the historical executions for the export.
- [ListExports](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListExports.html): Lists all data export definitions.
- [ListTables](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListTables.html): Lists all available tables in data exports.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListTagsForResource.html): List tags associated with an existing data export.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_TagResource.html): Adds tags for an existing data export definition.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_UntagResource.html): Deletes tags associated with an existing data export definition.
- [UpdateExport](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_UpdateExport.html): Updates an existing data export by overwriting all export parameters.

### Data Types

- [Column](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Column.html): Includes basic information for a data column such as its description, name, and type.
- [DataQuery](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_DataQuery.html): The SQL query of column selections and row filters from the data table you want.
- [DestinationConfigurations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_DestinationConfigurations.html): The destinations used for data exports.
- [ExecutionReference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExecutionReference.html): The reference for the data export update.
- [ExecutionStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExecutionStatus.html): The status of the execution.
- [Export](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Export.html): The details that are available for an export.
- [ExportReference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExportReference.html): The reference details for a given export.
- [ExportStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExportStatus.html): The status of the data export.
- [RefreshCadence](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_RefreshCadence.html): The cadence for AWS to update the data export in your S3 bucket.
- [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ResourceTag.html): The tag structure that contains a tag key and value.
- [S3Destination](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_S3Destination.html): Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a data exports file.
- [S3OutputConfigurations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_S3OutputConfigurations.html): The compression type, file format, and overwrite preference for the data export.
- [Table](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_Table.html): The details for the data export table.
- [TablePropertyDescription](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_TablePropertyDescription.html): The properties for the data export table.
- [ValidationExceptionField](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ValidationExceptionField.html): The input failed to meet the constraints specified by the AWS service in a specified field.

## [AWS Pricing Calculator](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Billing_and_Cost_Management_Pricing_Calculator.html)

You can use the Pricing Calculator API to programmatically create estimates for your planned cloud use. You can model usage and commitments such as Savings Plans and Reserved Instances, and generate estimated costs using your discounts and benefit sharing preferences.

The Pricing Calculator API provides the following endpoint:

- `https://bcm-pricing-calculator.us-east-1.api.aws`

### Actions

- [BatchCreateBillScenarioCommitmentModification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModification.html): Create Compute Savings Plans, EC2 Instance Savings Plans, or EC2 Reserved Instances commitments that you want to model in a Bill Scenario.
- [BatchCreateBillScenarioUsageModification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModification.html): Create AWS service usage that you want to model in a Bill Scenario.
- [BatchCreateWorkloadEstimateUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsage.html): Create AWS service usage that you want to model in a Workload Estimate.
- [BatchDeleteBillScenarioCommitmentModification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModification.html): Delete commitment that you have created in a Bill Scenario.
- [BatchDeleteBillScenarioUsageModification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteBillScenarioUsageModification.html): Delete usage that you have created in a Bill Scenario.
- [BatchDeleteWorkloadEstimateUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsage.html): Delete usage that you have created in a Workload estimate.
- [BatchUpdateBillScenarioCommitmentModification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModification.html): Update a newly added or existing commitment.
- [BatchUpdateBillScenarioUsageModification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModification.html): Update a newly added or existing usage lines.
- [BatchUpdateWorkloadEstimateUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsage.html): Update a newly added or existing usage lines.
- [CreateBillEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CreateBillEstimate.html): Create a Bill estimate from a Bill scenario.
- [CreateBillScenario](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CreateBillScenario.html): Creates a new bill scenario to model potential changes to AWS usage and costs.
- [CreateWorkloadEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CreateWorkloadEstimate.html): Creates a new workload estimate to model costs for a specific workload.
- [DeleteBillEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_DeleteBillEstimate.html): Deletes an existing bill estimate.
- [DeleteBillScenario](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_DeleteBillScenario.html): Deletes an existing bill scenario.
- [DeleteWorkloadEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_DeleteWorkloadEstimate.html): Deletes an existing workload estimate.
- [GetBillEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetBillEstimate.html): Retrieves details of a specific bill estimate.
- [GetBillScenario](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetBillScenario.html): Retrieves details of a specific bill scenario.
- [GetPreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetPreferences.html): Retrieves the current preferences for AWS Pricing Calculator.
- [GetWorkloadEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_GetWorkloadEstimate.html): Retrieves details of a specific workload estimate.
- [ListBillEstimateCommitments](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimateCommitments.html): Lists the commitments associated with a bill estimate.
- [ListBillEstimateInputCommitmentModifications](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimateInputCommitmentModifications.html): Lists the input commitment modifications associated with a bill estimate.
- [ListBillEstimateInputUsageModifications](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimateInputUsageModifications.html): Lists the input usage modifications associated with a bill estimate.
- [ListBillEstimateLineItems](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimateLineItems.html): Lists the line items associated with a bill estimate.
- [ListBillEstimates](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimates.html): Lists all bill estimates for the account.
- [ListBillScenarioCommitmentModifications](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillScenarioCommitmentModifications.html): Lists the commitment modifications associated with a bill scenario.
- [ListBillScenarios](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillScenarios.html): Lists all bill scenarios for the account.
- [ListBillScenarioUsageModifications](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillScenarioUsageModifications.html): Lists the usage modifications associated with a bill scenario.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListTagsForResource.html): Lists all tags associated with a specified resource.
- [ListWorkloadEstimates](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListWorkloadEstimates.html): Lists all workload estimates for the account.
- [ListWorkloadEstimateUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListWorkloadEstimateUsage.html): Lists the usage associated with a workload estimate.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_TagResource.html): Adds one or more tags to a specified resource.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UntagResource.html): Removes one or more tags from a specified resource.
- [UpdateBillEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdateBillEstimate.html): Updates an existing bill estimate.
- [UpdateBillScenario](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdateBillScenario.html): Updates an existing bill scenario.
- [UpdatePreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdatePreferences.html): Updates the preferences for AWS Pricing Calculator.
- [UpdateWorkloadEstimate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UpdateWorkloadEstimate.html): Updates an existing workload estimate.

### Data Types

- [AddReservedInstanceAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_AddReservedInstanceAction.html): Represents an action to add a Reserved Instance to a bill scenario.
- [AddSavingsPlanAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_AddSavingsPlanAction.html): Represents an action to add a Savings Plan to a bill scenario.
- [BatchCreateBillScenarioCommitmentModificationEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationEntry.html): Represents an entry object in the batch operation to create bill scenario commitment modifications.
- [BatchCreateBillScenarioCommitmentModificationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationError.html): Represents an error that occurred during a batch create operation for bill scenario commitment modifications.
- [BatchCreateBillScenarioCommitmentModificationItem](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioCommitmentModificationItem.html): Represents a successfully created item in a batch operation for bill scenario commitment modifications.
- [BatchCreateBillScenarioUsageModificationEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationEntry.html): Represents an entry in a batch operation to create bill scenario usage modifications.
- [BatchCreateBillScenarioUsageModificationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationError.html): Represents an error that occurred during a batch create operation for bill scenario usage modifications.
- [BatchCreateBillScenarioUsageModificationItem](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateBillScenarioUsageModificationItem.html): Represents a successfully created item in a batch operation for bill scenario usage modifications.
- [BatchCreateWorkloadEstimateUsageEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageEntry.html): Represents an entry in a batch operation to create workload estimate usage.
- [BatchCreateWorkloadEstimateUsageError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageError.html): Represents an error that occurred during a batch create operation for workload estimate usage.
- [BatchCreateWorkloadEstimateUsageItem](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchCreateWorkloadEstimateUsageItem.html): Represents a successfully created item in a batch operation for workload estimate usage.
- [BatchDeleteBillScenarioCommitmentModificationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteBillScenarioCommitmentModificationError.html): Represents an error that occurred when deleting a commitment in a Bill Scenario.
- [BatchDeleteBillScenarioUsageModificationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteBillScenarioUsageModificationError.html): Represents an error that occurred when deleting usage in a Bill Scenario.
- [BatchDeleteWorkloadEstimateUsageError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchDeleteWorkloadEstimateUsageError.html): Represents an error that occurred when deleting usage in a workload estimate.
- [BatchUpdateBillScenarioCommitmentModificationEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationEntry.html): Represents an entry in a batch operation to update bill scenario commitment modifications.
- [BatchUpdateBillScenarioCommitmentModificationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioCommitmentModificationError.html): Represents an error that occurred when updating a commitment in a Bill Scenario.
- [BatchUpdateBillScenarioUsageModificationEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationEntry.html): Represents an entry in a batch operation to update bill scenario usage modifications.
- [BatchUpdateBillScenarioUsageModificationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateBillScenarioUsageModificationError.html): Represents an error that occurred when updating usage in a Bill Scenario.
- [BatchUpdateWorkloadEstimateUsageEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageEntry.html): Represents an entry in a batch operation to update workload estimate usage.
- [BatchUpdateWorkloadEstimateUsageError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BatchUpdateWorkloadEstimateUsageError.html): Represents an error that occurred when updating usage in a workload estimate.
- [BillEstimateCommitmentSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateCommitmentSummary.html): Provides a summary of commitment-related information for a bill estimate.
- [BillEstimateCostSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateCostSummary.html): Provides a summary of cost-related information for a bill estimate.
- [BillEstimateInputCommitmentModificationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateInputCommitmentModificationSummary.html): Summarizes an input commitment modification for a bill estimate.
- [BillEstimateInputUsageModificationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateInputUsageModificationSummary.html): Summarizes an input usage modification for a bill estimate.
- [BillEstimateLineItemSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateLineItemSummary.html): Provides a summary of a line item in a bill estimate.
- [BillEstimateSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateSummary.html): Provides a summary of a bill estimate.
- [BillInterval](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillInterval.html): Represents a time interval for a bill or estimate.
- [BillScenarioCommitmentModificationAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationAction.html): Represents an action to modify commitments in a bill scenario.
- [BillScenarioCommitmentModificationItem](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioCommitmentModificationItem.html): Represents a commitment modification item in a bill scenario.
- [BillScenarioSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioSummary.html): Provides a summary of a bill scenario.
- [BillScenarioUsageModificationItem](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioUsageModificationItem.html): Represents a usage modification item in a bill scenario.
- [CostAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CostAmount.html): Represents a monetary amount with associated currency.
- [CostDifference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_CostDifference.html): Represents the difference between historical and estimated costs.
- [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_Expression.html): Represents a complex filtering expression for cost and usage data.
- [ExpressionFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ExpressionFilter.html): Represents a filter used within an expression.
- [FilterTimestamp](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_FilterTimestamp.html): Represents a time-based filter.
- [HistoricalUsageEntity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_HistoricalUsageEntity.html): Represents historical usage data for a specific entity.
- [ListBillEstimateLineItemsFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimateLineItemsFilter.html): Represents a filter for listing bill estimate line items.
- [ListBillEstimatesFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillEstimatesFilter.html): Represents a filter for listing bill estimates.
- [ListBillScenariosFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListBillScenariosFilter.html): Represents a filter for listing bill scenarios.
- [ListUsageFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListUsageFilter.html): Represents a filter for listing usage data.
- [ListWorkloadEstimatesFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ListWorkloadEstimatesFilter.html): Represents a filter for listing workload estimates.
- [NegateReservedInstanceAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_NegateReservedInstanceAction.html): Represents an action to remove a Reserved Instance from a bill scenario.
- [NegateSavingsPlanAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_NegateSavingsPlanAction.html): Represents an action to remove a Savings Plan from a bill scenario.
- [UsageAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UsageAmount.html): Represents a usage amount for a specific time period.
- [UsageQuantity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UsageQuantity.html): Represents a usage quantity with associated unit and time period.
- [UsageQuantityResult](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_UsageQuantityResult.html): Represents the result of a usage quantity calculation.
- [ValidationExceptionField](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_ValidationExceptionField.html): Represents a field that failed validation in a request.
- [WorkloadEstimateSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_WorkloadEstimateSummary.html): Provides a summary of a workload estimate.
- [WorkloadEstimateUsageItem](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_WorkloadEstimateUsageItem.html): Represents a usage item in a workload estimate.
- [WorkloadEstimateUsageQuantity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_WorkloadEstimateUsageQuantity.html): Represents a usage quantity for a workload estimate.

## [AWS Billing and Cost Management Recommended Actions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Billing_and_Cost_Management_Recommended_Actions.html)

You can use the AWS Billing and Cost Management Recommended Actions API to programmatically query your best practices and recommendations to optimize your costs.

The AWS Billing and Cost Management Recommended Actions API provides the following endpoint:

- https://bcm-recommended-actions.us-east-1.api.aws

### Actions

- [ListRecommendedActions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ListRecommendedActions.html): Returns a list of recommended actions that match the filter criteria.

### Data Types

- [ActionFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ActionFilter.html): Describes a filter that returns a more specific list of recommended actions.
- [RecommendedAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_RecommendedAction.html): Describes a specific recommended action.
- [RequestFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_RequestFilter.html): Enables filtering of results based on specified action criteria.
- [ValidationExceptionField](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_BillingAndCostManagementRecommendedActions_ValidationExceptionField.html): Provides specific details about why a particular field failed validation.

## [AWS Billing](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Billing.html)

You can use the Billing API to programatically list the billing views available to you for a given time period. A billing view represents a set of billing data.

The Billing API provides the following endpoint:

`https://billing.us-east-1.api.aws`

### Actions

- [AssociateSourceViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_AssociateSourceViews.html): Associates one or more source billing views with an existing billing view.
- [CreateBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CreateBillingView.html): Creates a billing view with the specified billing view attributes.
- [DeleteBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DeleteBillingView.html): Deletes the specified billing view.
- [DisassociateSourceViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DisassociateSourceViews.html): Removes the association between one or more source billing views and an existing billing view.
- [GetBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetBillingView.html): Returns the metadata associated to the specified billing view ARN.
- [GetResourcePolicy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_GetResourcePolicy.html): Returns the resource-based policy document attached to the resource in JSON format.
- [ListBillingViews](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListBillingViews.html): Lists the billing views available for a given time period.
- [ListSourceViewsForBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListSourceViewsForBillingView.html): Lists the source views (managed AWS billing views) associated with the billing view.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ListTagsForResource.html): Lists tags associated with the billing view resource.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_TagResource.html): An API operation for adding one or more tags (key-value pairs) to a resource.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_UntagResource.html): Removes one or more tags from a resource.
- [UpdateBillingView](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_UpdateBillingView.html): An API to update the attributes of the billing view.

### Data Types

- [ActiveTimeRange](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ActiveTimeRange.html): A time range with a start and end time.
- [BillingViewElement](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewElement.html): The metadata associated to the billing view.
- [BillingViewHealthStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewHealthStatus.html): Represents the health status of a billing view, including a status code and optional reasons for the status.
- [BillingViewListElement](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_BillingViewListElement.html): A representation of a billing view.
- [CostCategoryValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_CostCategoryValues.html): The Cost Categories values used for filtering the costs.
- [DimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_DimensionValues.html): The metadata that you can use to filter and group your results.
- [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html): See Expression.
- [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ResourceTag.html): The tag structure that contains a tag key and value.
- [StringSearch](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_StringSearch.html): A structure that defines how to search for string values.
- [TagValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_TagValues.html): The values that are available for a tag.
- [TimeRange](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_TimeRange.html): Specifies a time range with inclusive begin and end dates.
- [ValidationExceptionField](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ValidationExceptionField.html): The field's information of a request that resulted in an exception.

## [AWS Budgets](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Budgets.html)

Use the AWS Budgets API to plan your service usage, service costs, and instance reservations. This API reference provides descriptions, syntax, and usage examples for each of the actions and data types for the AWS Budgets feature.

Budgets provide you with a way to see the following information:

- How close your plan is to your budgeted amount or to the free tier limits
- Your usage-to-date, including how much you've used of your Reserved Instances (RIs)
- Your current estimated charges from AWS, and how much your predicted usage will accrue in charges by the end of the month
- How much of your budget has been used

AWS updates your budget status several times a day. Budgets track your unblended costs, subscriptions, refunds, and RIs. You can create the following types of budgets:

- Cost budgets- Plan how much you want to spend on a service.
- Usage budgets- Plan how much you want to use one or more services.
- RI utilization budgets- Define a utilization threshold, and receive alerts when your RI usage falls below that threshold. This lets you see if your RIs are unused or under-utilized.
- RI coverage budgets- Define a coverage threshold, and receive alerts when the number of your instance hours that are covered by RIs fall below that threshold. This lets you see how much of your instance usage is covered by a reservation.

Service Endpoint

The AWS Budgets API provides the following endpoint:

- https://budgets.amazonaws.com

For information about costs that are associated with the AWS Budgets API, see [AWS Cost Management Pricing](https://aws.amazon.com/aws-cost-management/pricing/).

### Actions

- [CreateBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudget.html): Creates a budget and, if included, notifications and subscribers.
- [CreateBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateBudgetAction.html): Creates a budget action.
- [CreateNotification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateNotification.html): Creates a notification.
- [CreateSubscriber](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CreateSubscriber.html): Creates a subscriber.
- [DeleteBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DeleteBudget.html): Deletes a budget.
- [DeleteBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DeleteBudgetAction.html): Deletes a budget action.
- [DeleteNotification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DeleteNotification.html): Deletes a notification.
- [DeleteSubscriber](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DeleteSubscriber.html): Deletes a subscriber.
- [DescribeBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudget.html): Describes a budget.
- [DescribeBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetAction.html): Describes a budget action detail.
- [DescribeBudgetActionHistories](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionHistories.html): Describes a budget action history detail.
- [DescribeBudgetActionsForAccount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionsForAccount.html): Describes all of the budget actions for an account.
- [DescribeBudgetActionsForBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetActionsForBudget.html): Describes all of the budget actions for a budget.
- [DescribeBudgetNotificationsForAccount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetNotificationsForAccount.html): Lists the budget names and notifications that are associated with an account.
- [DescribeBudgetPerformanceHistory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgetPerformanceHistory.html): Describes the history for DAILY, MONTHLY, and QUARTERLY budgets.
- [DescribeBudgets](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeBudgets.html): Lists the budgets that are associated with an account.
- [DescribeNotificationsForBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeNotificationsForBudget.html): Lists the notifications that are associated with a budget.
- [DescribeSubscribersForNotification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_DescribeSubscribersForNotification.html): Lists the subscribers that are associated with a notification.
- [ExecuteBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ExecuteBudgetAction.html): Executes a budget action.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ListTagsForResource.html): Lists tags associated with a budget or budget action resource.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_TagResource.html): Creates tags for a budget or budget action resource.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UntagResource.html): Deletes tags associated with a budget or budget action resource.
- [UpdateBudget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudget.html): Updates a budget.
- [UpdateBudgetAction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateBudgetAction.html): Updates a budget action.
- [UpdateNotification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateNotification.html): Updates a notification.
- [UpdateSubscriber](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_UpdateSubscriber.html): Updates a subscriber.

### Data Types

- [Action](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Action.html): A budget action resource.
- [ActionHistory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ActionHistory.html): The historical records for a budget action.
- [ActionHistoryDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ActionHistoryDetails.html): The description of the details for the event.
- [ActionThreshold](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ActionThreshold.html): The trigger threshold of the action.
- [AutoAdjustData](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_AutoAdjustData.html): The parameters that determine the budget amount for an auto-adjusting budget.
- [Budget](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Budget.html): Represents the output of the CreateBudget operation.
- [BudgetedAndActualAmounts](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_BudgetedAndActualAmounts.html): The amount of cost or usage that you created the budget for, compared to your actual costs or usage.
- [BudgetNotificationsForAccount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_BudgetNotificationsForAccount.html): The budget name and associated notifications for an account.
- [BudgetPerformanceHistory](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_BudgetPerformanceHistory.html): A history of the state of a budget at the end of the budget's specified time period.
- [CalculatedSpend](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CalculatedSpend.html): The spend objects that are associated with this budget.
- [CostCategoryValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CostCategoryValues.html): The cost category values used for filtering the costs.
- [CostTypes](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_CostTypes.html): The types of cost that are included in a COST budget, such as tax and subscriptions.
- [Definition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Definition.html): Specifies all of the type-specific parameters.
- [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Expression.html): Use Expression to filter in various Budgets APIs.
- [ExpressionDimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ExpressionDimensionValues.html): Contains the specifications for the filters to use for your request.
- [HealthStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_HealthStatus.html): Provides information about the current operational state of a billing view resource, including its ability to access and update based on its associated billing view.
- [HistoricalOptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_HistoricalOptions.html): The parameters that define or describe the historical data that your auto-adjusting budget is based on.
- [IamActionDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_IamActionDefinition.html): The AWS Identity and Access Management (IAM) action definition details.
- [Notification](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Notification.html): A notification that's associated with a budget.
- [NotificationWithSubscribers](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_NotificationWithSubscribers.html): A notification with subscribers.
- [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ResourceTag.html): The tag structure that contains a tag key and value.
- [ScpActionDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_ScpActionDefinition.html): The service control policies (SCP) action definition details.
- [Spend](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Spend.html): The amount of cost or usage that's measured for a budget.
- [SsmActionDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_SsmActionDefinition.html): The AWS Systems Manager (SSM) action definition details.
- [Subscriber](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Subscriber.html): The subscriber to a budget notification.
- [TagValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_TagValues.html): The values that are available for a tag.
- [TimePeriod](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_TimePeriod.html): The period of time that's covered by a budget.

## [AWS Cost Optimization Hub](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_Cost_Optimization_Hub.html)

You can use the Cost Optimization Hub API to programmatically identify, filter, aggregate, and quantify savings for your cost optimization recommendations across multiple AWS Regions and AWS accounts in your organization.

The Cost Optimization Hub API provides the following endpoint:

- https://cost-optimization-hub.us-east-1.amazonaws.com

### Actions

- [GetPreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetPreferences.html): Returns a set of preferences for an account in order to add account-specific preferences into the service.
- [GetRecommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetRecommendation.html): Returns both the current and recommended resource configuration and the estimated cost impact for a recommendation.
- [ListEfficiencyMetrics](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEfficiencyMetrics.html): Returns cost efficiency metrics aggregated over time and optionally grouped by a specified dimension.
- [ListEnrollmentStatuses](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListEnrollmentStatuses.html): Retrieves the enrollment status for an account.
- [ListRecommendations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendations.html): Returns a list of recommendations.
- [ListRecommendationSummaries](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ListRecommendationSummaries.html): Returns a concise representation of savings estimates for resources.
- [UpdateEnrollmentStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdateEnrollmentStatus.html): Updates the enrollment (opt in and opt out) status of an account to the Cost Optimization Hub service.
- [UpdatePreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_UpdatePreferences.html): Updates a set of preferences for an account in order to add account-specific preferences into the service.

### Data Types

- [AccountEnrollmentStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_AccountEnrollmentStatus.html): Describes the enrollment status of an organization's member accounts in Cost Optimization Hub.
- [AuroraDbClusterStorage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_AuroraDbClusterStorage.html): Contains the details of an Aurora DB cluster storage.
- [AuroraDbClusterStorageConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_AuroraDbClusterStorageConfiguration.html): The Aurora DB cluster storage configuration used for recommendations.
- [BlockStoragePerformanceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_BlockStoragePerformanceConfiguration.html): Describes the Amazon Elastic Block Store performance configuration of the current and recommended resource configuration for a recommendation.
- [ComputeConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ComputeConfiguration.html): Describes the performance configuration for compute services such as Amazon EC2, Lambda, and ECS.
- [ComputeSavingsPlans](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ComputeSavingsPlans.html): The Compute Savings Plans recommendation details.
- [ComputeSavingsPlansConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ComputeSavingsPlansConfiguration.html): The Compute Savings Plans configuration used for recommendations.
- [DbInstanceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_DbInstanceConfiguration.html): The DB instance configuration used for recommendations.
- [DynamoDbReservedCapacity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_DynamoDbReservedCapacity.html): The DynamoDB reserved capacity recommendation details.
- [DynamoDbReservedCapacityConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_DynamoDbReservedCapacityConfiguration.html): The DynamoDB reserved capacity configuration used for recommendations.
- [EbsVolume](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EbsVolume.html): Describes the Amazon Elastic Block Store volume configuration of the current and recommended resource configuration for a recommendation.
- [EbsVolumeConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EbsVolumeConfiguration.html): The Amazon Elastic Block Store volume configuration used for recommendations.
- [Ec2AutoScalingGroup](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2AutoScalingGroup.html): The EC2 Auto Scaling group recommendation details.
- [Ec2AutoScalingGroupConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2AutoScalingGroupConfiguration.html): The EC2 Auto Scaling group configuration used for recommendations.
- [Ec2Instance](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2Instance.html): Describes the EC2 instance configuration of the current and recommended resource configuration for a recommendation.
- [Ec2InstanceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2InstanceConfiguration.html): The EC2 instance configuration used for recommendations.
- [Ec2InstanceSavingsPlans](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2InstanceSavingsPlans.html): The EC2 instance Savings Plans recommendation details.
- [Ec2InstanceSavingsPlansConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2InstanceSavingsPlansConfiguration.html): The EC2 instance Savings Plans configuration used for recommendations.
- [Ec2ReservedInstances](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2ReservedInstances.html): The EC2 reserved instances recommendation details.
- [Ec2ReservedInstancesConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Ec2ReservedInstancesConfiguration.html): The EC2 reserved instances configuration used for recommendations.
- [EcsService](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EcsService.html): The ECS service recommendation details.
- [EcsServiceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EcsServiceConfiguration.html): The ECS service configuration used for recommendations.
- [EfficiencyMetricsByGroup](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EfficiencyMetricsByGroup.html): Contains cost efficiency metrics for a specific group over time.
- [ElastiCacheReservedInstances](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ElastiCacheReservedInstances.html): The ElastiCache reserved instances recommendation details.
- [ElastiCacheReservedInstancesConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ElastiCacheReservedInstancesConfiguration.html): The ElastiCache reserved instances configuration used for recommendations.
- [EstimatedDiscounts](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_EstimatedDiscounts.html): Estimated discount details of the current and recommended resource configuration for a recommendation.
- [Filter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Filter.html): Describes a filter that returns a more specific list of recommendations.
- [InstanceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_InstanceConfiguration.html): The instance configuration used for recommendations.
- [LambdaFunction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_LambdaFunction.html): The Lambda function recommendation details.
- [LambdaFunctionConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_LambdaFunctionConfiguration.html): The Lambda function configuration used for recommendations.
- [MemoryDbReservedInstances](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_MemoryDbReservedInstances.html): The MemoryDB reserved instances recommendation details.
- [MemoryDbReservedInstancesConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_MemoryDbReservedInstancesConfiguration.html): The MemoryDB reserved instances configuration used for recommendations.
- [MetricsByTime](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_MetricsByTime.html): Contains efficiency metrics for a specific point in time, including an efficiency score, potential savings, optimizable spend, and timestamp.
- [MixedInstanceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_MixedInstanceConfiguration.html): The configuration for the EC2 Auto Scaling group with mixed instance types.
- [OpenSearchReservedInstances](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_OpenSearchReservedInstances.html): The OpenSearch reserved instances recommendation details.
- [OpenSearchReservedInstancesConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_OpenSearchReservedInstancesConfiguration.html): The OpenSearch reserved instances configuration used for recommendations.
- [OrderBy](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_OrderBy.html): Defines how rows will be sorted in the response.
- [PreferredCommitment](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_PreferredCommitment.html): The preferred configuration for Reserved Instances and Savings Plans commitment-based discounts, consisting of a payment option and a commitment duration.
- [RdsDbInstance](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RdsDbInstance.html): Contains the details of an Amazon RDS DB instance.
- [RdsDbInstanceConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RdsDbInstanceConfiguration.html): The Amazon RDS DB instance configuration used for recommendations.
- [RdsDbInstanceStorage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RdsDbInstanceStorage.html): Contains the details of an Amazon RDS DB instance storage.
- [RdsDbInstanceStorageConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RdsDbInstanceStorageConfiguration.html): The Amazon RDS DB instance storage configuration used for recommendations.
- [RdsReservedInstances](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RdsReservedInstances.html): The RDS reserved instances recommendation details.
- [RdsReservedInstancesConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RdsReservedInstancesConfiguration.html): The RDS reserved instances configuration used for recommendations.
- [Recommendation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Recommendation.html): Describes a recommendation.
- [RecommendationSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RecommendationSummary.html): The summary of rightsizing recommendations, including de-duped savings from all types of recommendations.
- [RedshiftReservedInstances](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RedshiftReservedInstances.html): The Redshift reserved instances recommendation details.
- [RedshiftReservedInstancesConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_RedshiftReservedInstancesConfiguration.html): The Redshift reserved instances configuration used for recommendations.
- [ReservedInstancesCostCalculation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ReservedInstancesCostCalculation.html): Cost impact of the purchase recommendation.
- [ReservedInstancesPricing](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ReservedInstancesPricing.html): Pricing details for your recommended reserved instance.
- [ResourceCostCalculation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ResourceCostCalculation.html): Cost impact of the resource recommendation.
- [ResourceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ResourceDetails.html): Contains detailed information about the specified resource.
- [ResourcePricing](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ResourcePricing.html): Contains pricing information about the specified resource.
- [SageMakerSavingsPlans](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_SageMakerSavingsPlans.html): The SageMaker Savings Plans recommendation details.
- [SageMakerSavingsPlansConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_SageMakerSavingsPlansConfiguration.html): The SageMaker Savings Plans configuration used for recommendations.
- [SavingsPlansCostCalculation](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_SavingsPlansCostCalculation.html): Cost impact of the purchase recommendation.
- [SavingsPlansPricing](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_SavingsPlansPricing.html): Pricing information about a Savings Plans.
- [StorageConfiguration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_StorageConfiguration.html): The storage configuration used for recommendations.
- [SummaryMetricsResult](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_SummaryMetricsResult.html): The results or descriptions for the additional metrics, based on whether the metrics were or were not requested.
- [Tag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Tag.html): The tag structure that contains a tag key and value.
- [TimePeriod](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_TimePeriod.html): Specifies a date range for retrieving efficiency metrics.
- [Usage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Usage.html): Details about the usage.
- [ValidationExceptionDetail](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ValidationExceptionDetail.html): The input failed to meet the constraints specified by the AWS service in a specified field.

## [AWS Cost and Usage Report](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Cost_and_Usage_Report_Service.html)

You can use the AWS Cost and Usage Report API to programmatically create, query, and delete AWS Cost and Usage Report definitions.

AWS Cost and Usage Report track the monthly AWS costs and usage associated with your AWS account. The report contains line items for each unique combination of AWS product, usage type, and operation that your AWS account uses. You can configure the AWS Cost and Usage Report to show only the data that you want, using the AWS Cost and Usage Report API.

Service Endpoint

The AWS Cost and Usage Report API provides the following endpoint:

- cur.us-east-1.amazonaws.com

### Actions

- [DeleteReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_DeleteReportDefinition.html): Deletes the specified report.
- [DescribeReportDefinitions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_DescribeReportDefinitions.html): Lists the AWS Cost and Usage Report available to this account.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ListTagsForResource.html): Lists the tags associated with the specified report definition.
- [ModifyReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ModifyReportDefinition.html): Allows you to programmatically update your report preferences.
- [PutReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_PutReportDefinition.html): Creates a new report using the description that you provide.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_TagResource.html): Associates a set of tags with a report definition.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_UntagResource.html): Disassociates a set of tags from a report definition.

### Data Types

- [ReportDefinition](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ReportDefinition.html): The definition of AWS Cost and Usage Report.
- [ReportStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_ReportStatus.html): A two element dictionary with a lastDelivery and lastStatus key whose values describe the date and status of the last delivered report for a particular report definition.
- [Tag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_cur_Tag.html): Describes a tag.

## [AWS Free Tier](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Free_Tier.html)

You can use the AWS Free Tier API to query programmatically your Free Tier usage data.

Free Tier tracks your monthly usage data for all free tier offers that are associated with your AWS account. You can use the Free Tier API to filter and show only the data that you want.

Service endpoint

The Free Tier API provides the following endpoint:

- https://freetier.us-east-1.api.aws

For more information, see [Using the AWS Free Tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html)in the AWS Billing User Guide.

### Actions

- [GetAccountActivity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetAccountActivity.html): Returns a specific activity record that is available to the customer.
- [GetAccountPlanState](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetAccountPlanState.html): This returns all of the information related to the state of the account plan related to Free Tier.
- [GetFreeTierUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_GetFreeTierUsage.html): Returns a list of all Free Tier usage objects that match your filters.
- [ListAccountActivities](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_ListAccountActivities.html): Returns a list of activities that are available.
- [UpgradeAccountPlan](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_UpgradeAccountPlan.html): The account plan type for the AWS account.

### Data Types

- [ActivityReward](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_ActivityReward.html): The summary of the rewards granted as a result of activities completed.
- [ActivitySummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_ActivitySummary.html): The summary of activities.
- [DimensionValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_DimensionValues.html): Contains the specifications for the filters to use for your request.
- [Expression](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_Expression.html): Use Expression to filter in the GetFreeTierUsage API operation.
- [FreeTierUsage](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_FreeTierUsage.html): Consists of a AWS Free Tier offerâs metadata and your data usage for the offer.
- [MonetaryAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_freetier_MonetaryAmount.html): The monetary amount of the credit.

## [AWS Invoicing](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Invoicing.html)

AWS Invoice Configuration

You can use AWS Invoice Configuration APIs to programmatically create, update, delete, get, and list invoice units. You can also programmatically fetch the information of the invoice receiver. For example, business legal name, address, and invoicing contacts.

You can use AWS Invoice Configuration to receive separate AWS invoices based your organizational needs. By using AWS Invoice Configuration, you can configure invoice units that are groups of AWS accounts that represent your business entities, and receive separate invoices for each business entity. You can also assign a unique member or payer account as the invoice receiver for each invoice unit. As you create new accounts within your Organizations using AWS Invoice Configuration APIs, you can automate the creation of new invoice units and subsequently automate the addition of new accounts to your invoice units.

AWS Procurement Portal Preferences

You can use AWS Procurement Portal Preferences APIs to programmatically create, update, delete, get, and list procurement portal connections and e-invoice delivery settings. You can also programmatically fetch and modify the status of procurement portal configurations. For example, SAP Business Network or Coupa connections, configure e-invoice delivery and purchase order retrieval features.

You can use AWS Procurement Portal Preferences to connect e-invoice delivery to your procurement portals based on your organizational needs. By using AWS Procurement Portal Preferences, you can configure connections to SAP Business Network and Coupa procurement portals that retrieve purchase orders and deliver AWS invoices on the same day they are generated. You can also set up testing environments to validate invoice delivery without affecting live transactions, and manage contact information for portal setup and support.

Administrative users should understand that billing read-only policies will show all procurement portal connection details. Review your IAM policies to ensure appropriate access controls are in place for procurement portal preferences.

AWS Invoice Management

You can use AWS Invoice Management APIs to programmatically list invoice summaries and get invoice documents. You can also programmatically fetch invoice documents with S3 pre-signed URLs.

You can use AWS Invoice Management to access invoice information based on your organizational needs. By using AWS Invoice Management, you can retrieve paginated lists of invoice summaries that include invoice metadata such as invoice IDs, amounts, and currencies without downloading documents. You can also download invoice documents in PDF format using S3 pre-signed URLs with built-in expiration. As you manage invoices across your organization using AWS Invoice Management APIs, you can create invoice retrieval processes and integrate invoice data into your financial systems.

Service endpoint

You can use the following endpoints for AWS Invoice Configuration, AWS Procurement Portal Preferences, and AWS Invoice Management:

- `https://invoicing.us-east-1.api.aws`

### Actions

- [BatchGetInvoiceProfile](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_BatchGetInvoiceProfile.html): This gets the invoice profile associated with a set of accounts.
- [CreateInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CreateInvoiceUnit.html): This creates a new invoice unit with the provided definition.
- [CreateProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CreateProcurementPortalPreference.html): This feature API is subject to changing at any time.
- [DeleteInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DeleteInvoiceUnit.html): This deletes an invoice unit with the provided invoice unit ARN.
- [DeleteProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DeleteProcurementPortalPreference.html): This feature API is subject to changing at any time.
- [GetInvoicePDF](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetInvoicePDF.html): Returns a URL to download the invoice document and supplemental documents associated with an invoice.
- [GetInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetInvoiceUnit.html): This retrieves the invoice unit definition.
- [GetProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_GetProcurementPortalPreference.html): This feature API is subject to changing at any time.
- [ListInvoiceSummaries](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListInvoiceSummaries.html): Retrieves your invoice details programmatically, without line item details.
- [ListInvoiceUnits](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListInvoiceUnits.html): This fetches a list of all invoice unit definitions for a given account, as of the provided AsOf date.
- [ListProcurementPortalPreferences](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListProcurementPortalPreferences.html): This feature API is subject to changing at any time.
- [ListTagsForResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ListTagsForResource.html): Lists the tags for a resource.
- [PutProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_PutProcurementPortalPreference.html): This feature API is subject to changing at any time.
- [TagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TagResource.html): Adds a tag to a resource.
- [UntagResource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UntagResource.html): Removes a tag from a resource.
- [UpdateInvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UpdateInvoiceUnit.html): You can update the invoice unit configuration at any time, and AWS will use the latest configuration at the end of the month.
- [UpdateProcurementPortalPreferenceStatus](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_UpdateProcurementPortalPreferenceStatus.html): This feature API is subject to changing at any time.

### Data Types

- [AmountBreakdown](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_AmountBreakdown.html): Details about how the total amount was calculated and categorized.
- [BillingPeriod](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_BillingPeriod.html): The billing period for which you want to retrieve invoice-related documents.
- [Contact](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_Contact.html): Represents contact information for a person or role associated with the procurement portal preference.
- [CurrencyExchangeDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_CurrencyExchangeDetails.html): The details of currency exchange.
- [DateInterval](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DateInterval.html): The time period that you want invoice-related documents for.
- [DiscountsBreakdown](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DiscountsBreakdown.html): The discounts details.
- [DiscountsBreakdownAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_DiscountsBreakdownAmount.html): The discounted amount.
- [EinvoiceDeliveryPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_EinvoiceDeliveryPreference.html): Specifies the preferences for e-invoice delivery, including document types, attachment types, and customization settings.
- [Entity](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_Entity.html): The organization name providing AWS services.
- [FeesBreakdown](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_FeesBreakdown.html): The details of fees.
- [FeesBreakdownAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_FeesBreakdownAmount.html): The fee amount.
- [Filters](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_Filters.html): An optional input to the list API.
- [InvoiceCurrencyAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceCurrencyAmount.html): The amount charged after taxes, in the preferred currency.
- [InvoicePDF](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoicePDF.html): Invoice document data.
- [InvoiceProfile](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceProfile.html): Contains high-level information about the invoice receiver.
- [InvoiceSummariesFilter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceSummariesFilter.html): Filters for your invoice summaries.
- [InvoiceSummariesSelector](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceSummariesSelector.html): Specifies the invoice summary.
- [InvoiceSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceSummary.html): The invoice that the API retrieved.
- [InvoiceUnit](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceUnit.html): An invoice unit is a set of mutually exclusive accounts that correspond to your business entity.
- [InvoiceUnitRule](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_InvoiceUnitRule.html): This is used to categorize the invoice unit.
- [ProcurementPortalPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreference.html): Represents the full configuration of a procurement portal preference, including settings for e-invoice delivery and purchase order retrieval.
- [ProcurementPortalPreferenceSelector](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreferenceSelector.html): Specifies criteria for selecting which invoices should be processed using a particular procurement portal preference.
- [ProcurementPortalPreferenceSummary](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ProcurementPortalPreferenceSummary.html): Provides a summary of a procurement portal preference, including key identifiers and status information.
- [PurchaseOrderDataSource](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_PurchaseOrderDataSource.html): Specifies the source configuration for retrieving purchase order data.
- [ReceiverAddress](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ReceiverAddress.html): The details of the address associated with the receiver.
- [ResourceTag](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ResourceTag.html): The tag structure that contains a tag key and value.
- [SupplementalDocument](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_SupplementalDocument.html): Supplemental document associated with the invoice.
- [TaxesBreakdown](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TaxesBreakdown.html): The details of the taxes.
- [TaxesBreakdownAmount](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TaxesBreakdownAmount.html): The tax amount.
- [TestEnvPreference](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TestEnvPreference.html): Contains configuration settings for testing the procurement portal integration in a non-production environment.
- [TestEnvPreferenceInput](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TestEnvPreferenceInput.html): Input parameters for configuring test environment preferences for a procurement portal.
- [ValidationExceptionField](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_ValidationExceptionField.html): The input fails to satisfy the constraints specified by an AWS service.

## [AWS Price List](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_AWS_Price_List_Service.html)

The AWS Price List API is a centralized and convenient way to programmatically query AWS for services, products, and pricing information. The AWS Price List uses standardized product attributes such as `Location`, `Storage Class`, and `Operating System`, and provides prices at the SKU level. You can use the AWS Price List to do the following:

- Build cost control and scenario planning tools
- Reconcile billing data
- Forecast future spend for budgeting purposes
- Provide cost benefit analysis that compare your internal workloads with AWS

Use `GetServices`without a service code to retrieve the service codes for all AWS services, then `GetServices`with a service code to retrieve the attribute names for that service. After you have the service code and attribute names, you can use `GetAttributeValues`to see what values are available for an attribute. With the service code and an attribute name and value, you can use `GetProducts`to find specific products that you're interested in, such as an `AmazonEC2`instance, with a `Provisioned IOPS``volumeType`.

You can use the following endpoints for the AWS Price List API:

- https://api.pricing.us-east-1.amazonaws.com
- https://api.pricing.ap-south-1.amazonaws.com
- https://api.pricing.eu-central-1.amazonaws.com

For more information, see [Using the AWS Price List API](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/price-changes.html)in the AWS Billing User Guide.

For more information about AWS Billing and Cost Management endpoints, see [AWS Billing and Cost Management endpoints](https://docs.aws.amazon.com/general/latest/gr/billing.html)in the Amazon Web Services General Reference.

For more information about AWS Billing and Cost Management quotas, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html)in the AWS Billing User Guideand [Quotas and restrictions](https://docs.aws.amazon.com/cost-management/latest/userguide/management-limits.html)in the AWS Cost Management User Guide.

### Actions

- [DescribeServices](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_DescribeServices.html): Returns the metadata for one service or a list of the metadata for all services.
- [GetAttributeValues](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetAttributeValues.html): Returns a list of attribute values.
- [GetPriceListFileUrl](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetPriceListFileUrl.html): This feature is in preview release and is subject to change.
- [GetProducts](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_GetProducts.html): Returns a list of all products that match the filter criteria.
- [ListPriceLists](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_ListPriceLists.html): This feature is in preview release and is subject to change.

### Data Types

- [AttributeValue](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_AttributeValue.html): The values of a given attribute, such as Throughput Optimized HDD or Provisioned IOPS for the Amazon EC2 volumeType attribute.
- [Filter](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_Filter.html): The constraints that you want all returned products to match.
- [PriceList](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_PriceList.html): This feature is in preview release and is subject to change.
- [Service](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_pricing_Service.html): The metadata for a service, such as the service code and available attribute names.

## [Tax Settings](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/Welcome_Tax_Settings.html)

You can use the tax setting API to programmatically set, modify, and delete the tax registration number (TRN), associated business legal name, and address (Collectively referred to as "TRN information"). You can also programmatically view TRN information and tax addresses ("Tax profiles").

You can use this API to automate your TRN information settings instead of manually using the console.

Service Endpoint

- https://tax.us-east-1.amazonaws.com

### Actions

- [BatchDeleteTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchDeleteTaxRegistration.html): Deletes tax registration for multiple accounts in batch.
- [BatchGetTaxExemptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchGetTaxExemptions.html): Get the active tax exemptions for a given list of accounts.
- [BatchPutTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchPutTaxRegistration.html): Adds or updates tax registration for multiple accounts in batch.
- [DeleteSupplementalTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_DeleteSupplementalTaxRegistration.html): Deletes a supplemental tax registration for a single account.
- [DeleteTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_DeleteTaxRegistration.html): Deletes tax registration for a single account.
- [GetTaxExemptionTypes](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxExemptionTypes.html): Get supported tax exemption types.
- [GetTaxInheritance](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxInheritance.html): The get account tax inheritance status.
- [GetTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxRegistration.html): Retrieves tax registration for a single account.
- [GetTaxRegistrationDocument](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GetTaxRegistrationDocument.html): Downloads your tax documents to the Amazon S3 bucket that you specify in your request.
- [ListSupplementalTaxRegistrations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ListSupplementalTaxRegistrations.html): Retrieves supplemental tax registrations for a single account.
- [ListTaxExemptions](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ListTaxExemptions.html): Retrieves the tax exemption of accounts listed in a consolidated billing family.
- [ListTaxRegistrations](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ListTaxRegistrations.html): Retrieves the tax registration of accounts listed in a consolidated billing family.
- [PutSupplementalTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutSupplementalTaxRegistration.html): Stores supplemental tax registration for a single account.
- [PutTaxExemption](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutTaxExemption.html): Adds the tax exemption for a single account or all accounts listed in a consolidated billing family.
- [PutTaxInheritance](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutTaxInheritance.html): The updated tax inheritance status.
- [PutTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PutTaxRegistration.html): Adds or updates tax registration for a single account.

### Data Types

- [AccountDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AccountDetails.html): An object with your accountId and TRN information.
- [AccountMetaData](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AccountMetaData.html): The meta data information associated with the account.
- [AdditionalInfoRequest](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AdditionalInfoRequest.html): Additional tax information associated with your tax registration number (TRN).
- [AdditionalInfoResponse](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_AdditionalInfoResponse.html): Additional tax information associated with your TRN.
- [Address](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_Address.html): The details of the address associated with the TRN information.
- [Authority](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_Authority.html): The address domain associate with the tax information.
- [BatchDeleteTaxRegistrationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchDeleteTaxRegistrationError.html): The error object for representing failures in the BatchDeleteTaxRegistration operation.
- [BatchPutTaxRegistrationError](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BatchPutTaxRegistrationError.html): The error object for representing failures in the BatchPutTaxRegistration operation.
- [BrazilAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_BrazilAdditionalInfo.html): Additional tax information associated with your TRN in Brazil.
- [CanadaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_CanadaAdditionalInfo.html): Additional tax information associated with your TRN in Canada .
- [DestinationS3Location](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_DestinationS3Location.html): The location of the Amazon S3 bucket that you specify to download your tax documents to.
- [EgyptAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_EgyptAdditionalInfo.html): Additional tax information to specify for a TRN in Egypt.
- [EstoniaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_EstoniaAdditionalInfo.html): Additional tax information associated with your TRN in Estonia.
- [ExemptionCertificate](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ExemptionCertificate.html): The exemption certificate.
- [GeorgiaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GeorgiaAdditionalInfo.html): Additional tax information associated with your TRN in Georgia.
- [GreeceAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_GreeceAdditionalInfo.html): Additional tax information to specify for a TRN in Greece.
- [IndiaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_IndiaAdditionalInfo.html): Additional tax information in India.
- [IndonesiaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_IndonesiaAdditionalInfo.html): Additional tax information associated with your TRN in Indonesia.
- [IsraelAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_IsraelAdditionalInfo.html): Additional tax information associated with your TRN in Israel.
- [ItalyAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ItalyAdditionalInfo.html): Additional tax information associated with your TRN in Italy.
- [Jurisdiction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_Jurisdiction.html): The jurisdiction details of the TRN information of the customers.
- [KenyaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_KenyaAdditionalInfo.html): Additional tax information associated with your TRN in Kenya.
- [MalaysiaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_MalaysiaAdditionalInfo.html): Additional tax information associated with your TRN in Malaysia.
- [PolandAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_PolandAdditionalInfo.html): Additional tax information associated with your TRN in Poland.
- [RomaniaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_RomaniaAdditionalInfo.html): Additional tax information to specify for a TRN in Romania.
- [SaudiArabiaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SaudiArabiaAdditionalInfo.html): Additional tax information associated with your TRN in Saudi Arabia.
- [SourceS3Location](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SourceS3Location.html): The Amazon S3 bucket in your account where your tax document is located.
- [SouthKoreaAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SouthKoreaAdditionalInfo.html): Additional tax information associated with your TRN in South Korea.
- [SpainAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SpainAdditionalInfo.html): Additional tax information associated with your TRN in Spain.
- [SupplementalTaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SupplementalTaxRegistration.html): Supplemental TRN details.
- [SupplementalTaxRegistrationEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_SupplementalTaxRegistrationEntry.html): The supplemental TRN information to provide when adding or updating a supplemental TRN.
- [TaxDocumentMetadata](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxDocumentMetadata.html): The metadata for your tax document.
- [TaxExemption](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxExemption.html): The tax exemption.
- [TaxExemptionDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxExemptionDetails.html): The tax exemption details.
- [TaxExemptionType](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxExemptionType.html): The tax exemption type.
- [TaxInheritanceDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxInheritanceDetails.html): Tax inheritance information associated with the account.
- [TaxRegistration](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistration.html): Your TRN information.
- [TaxRegistrationDocFile](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationDocFile.html): The tax registration document.
- [TaxRegistrationDocument](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationDocument.html): Tax registration document information.
- [TaxRegistrationEntry](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationEntry.html): The TRN information you provide when you add a new TRN, or update.
- [TaxRegistrationWithJurisdiction](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TaxRegistrationWithJurisdiction.html): Your TRN information with jurisdiction details.
- [TurkeyAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_TurkeyAdditionalInfo.html): Additional tax information associated with your TRN in Turkey.
- [UkraineAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_UkraineAdditionalInfo.html): Additional tax information associated with your TRN in Ukraine.
- [UzbekistanAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_UzbekistanAdditionalInfo.html): Additional tax information to specify for a TRN in Uzbekistan.
- [ValidationExceptionField](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_ValidationExceptionField.html): The information about the specified parameter in the request that caused an error.
- [VerificationDetails](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_VerificationDetails.html): Required information to verify your TRN.
- [VietnamAdditionalInfo](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_taxSettings_VietnamAdditionalInfo.html): Additional tax information to specify for a TRN in Vietnam.

## Common

- [Common Parameters](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/CommonErrors.html)