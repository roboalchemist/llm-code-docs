# Source: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/llms.txt

# AWS Compute Optimizer API Reference

## [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/Welcome_AWS_Compute_Optimizer.html)

AWS Compute Optimizer is a service that analyzes the configuration and utilization metrics of your AWS compute resources, such as Amazon EC2 instances, Amazon EC2 Auto Scaling groups, AWS Lambda functions, Amazon EBS volumes, and Amazon ECS services on Fargate. It reports whether your resources are optimal, and generates optimization recommendations to reduce the cost and improve the performance of your workloads. Compute Optimizer also provides recent utilization metric data, in addition to projected utilization metric data for the recommendations, which you can use to evaluate which recommendation provides the best price-performance trade-off. The analysis of your usage patterns can help you decide when to move or resize your running resources, and still meet your performance and capacity requirements. For more information about Compute Optimizer, including the required permissions to use the service, see the [AWS Compute Optimizer User Guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/).

### Actions

- [DeleteRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DeleteRecommendationPreferences.html): Deletes a recommendation preference, such as enhanced infrastructure metrics.
- [DescribeRecommendationExportJobs](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DescribeRecommendationExportJobs.html): Describes recommendation export jobs created in the last seven days.
- [ExportAutoScalingGroupRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportAutoScalingGroupRecommendations.html): Exports optimization recommendations for Auto Scaling groups.
- [ExportEBSVolumeRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportEBSVolumeRecommendations.html): Exports optimization recommendations for Amazon EBS volumes.
- [ExportEC2InstanceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportEC2InstanceRecommendations.html): Exports optimization recommendations for Amazon EC2 instances.
- [ExportECSServiceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportECSServiceRecommendations.html): Exports optimization recommendations for Amazon ECS services on Fargate.
- [ExportIdleRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportIdleRecommendations.html): Export optimization recommendations for your idle resources.
- [ExportLambdaFunctionRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLambdaFunctionRecommendations.html): Exports optimization recommendations for AWS Lambda functions.
- [ExportLicenseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportLicenseRecommendations.html): Export optimization recommendations for your licenses.
- [ExportRDSDatabaseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportRDSDatabaseRecommendations.html): Export optimization recommendations for your Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases.
- [GetAutoScalingGroupRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetAutoScalingGroupRecommendations.html): Returns Auto Scaling group recommendations.
- [GetEBSVolumeRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEBSVolumeRecommendations.html): Returns Amazon Elastic Block Store (Amazon EBS) volume recommendations.
- [GetEC2InstanceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2InstanceRecommendations.html): Returns Amazon EC2 instance recommendations.
- [GetEC2RecommendationProjectedMetrics](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEC2RecommendationProjectedMetrics.html): Returns the projected utilization metrics of Amazon EC2 instance recommendations.
- [GetECSServiceRecommendationProjectedMetrics](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetECSServiceRecommendationProjectedMetrics.html): Returns the projected metrics of Amazon ECS service recommendations.
- [GetECSServiceRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetECSServiceRecommendations.html): Returns Amazon ECS service recommendations.
- [GetEffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEffectiveRecommendationPreferences.html): Returns the recommendation preferences that are in effect for a given resource, such as enhanced infrastructure metrics.
- [GetEnrollmentStatus](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEnrollmentStatus.html): Returns the enrollment (opt in) status of an account to the AWS Compute Optimizer service.
- [GetEnrollmentStatusesForOrganization](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetEnrollmentStatusesForOrganization.html): Returns the AWS Compute Optimizer enrollment (opt-in) status of organization member accounts, if your account is an organization management account.
- [GetIdleRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetIdleRecommendations.html): Returns idle resource recommendations.
- [GetLambdaFunctionRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetLambdaFunctionRecommendations.html): Returns AWS Lambda function recommendations.
- [GetLicenseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetLicenseRecommendations.html): Returns license recommendations for Amazon EC2 instances that run on a specific license.
- [GetRDSDatabaseRecommendationProjectedMetrics](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRDSDatabaseRecommendationProjectedMetrics.html): Returns the projected metrics of Aurora and RDS database recommendations.
- [GetRDSDatabaseRecommendations](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRDSDatabaseRecommendations.html): Returns Amazon Aurora and RDS database recommendations.
- [GetRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationPreferences.html): Returns existing recommendation preferences, such as enhanced infrastructure metrics.
- [GetRecommendationSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationSummaries.html): Returns the optimization findings for an account.
- [PutRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_PutRecommendationPreferences.html): Creates a new recommendation preference or updates an existing recommendation preference, such as enhanced infrastructure metrics.
- [UpdateEnrollmentStatus](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_UpdateEnrollmentStatus.html): Updates the enrollment (opt in and opt out) status of an account to the AWS Compute Optimizer service.

### Data Types

- [AccountEnrollmentStatus](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AccountEnrollmentStatus.html): Describes the enrollment status of an organization's member accounts in AWS Compute Optimizer.
- [AutoScalingGroupConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupConfiguration.html): Describes the configuration of an EC2 Auto Scaling group.
- [AutoScalingGroupEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupEstimatedMonthlySavings.html): An object that describes the estimated monthly savings possible by adopting Compute Optimizerâs Auto Scaling group recommendations.
- [AutoScalingGroupRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupRecommendation.html): Describes an Auto Scaling group recommendation.
- [AutoScalingGroupRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupRecommendationOption.html): Describes a recommendation option for an Auto Scaling group.
- [AutoScalingGroupSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for Auto Scaling group recommendations after applying the Savings Plans and Reserved Instances discounts.
- [ContainerConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ContainerConfiguration.html): Describes the container configurations within the tasks of your Amazon ECS service.
- [ContainerRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ContainerRecommendation.html): The CPU and memory recommendations for a container within the tasks of your Amazon ECS service.
- [CurrentPerformanceRiskRatings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_CurrentPerformanceRiskRatings.html): Describes the performance risk ratings for a given resource type.
- [CustomizableMetricParameters](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_CustomizableMetricParameters.html): Defines the various metric parameters that can be customized, such as threshold and headroom.
- [DBStorageConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_DBStorageConfiguration.html): The configuration of the recommended RDS storage.
- [EBSEffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSEffectiveRecommendationPreferences.html): Describes the effective recommendation preferences for Amazon EBS volumes.
- [EBSEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSEstimatedMonthlySavings.html): An object that describes the estimated monthly savings possible by adopting Compute Optimizerâs Amazon EBS volume recommendations.
- [EBSFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSFilter.html): Describes a filter that returns a more specific list of Amazon Elastic Block Store (Amazon EBS) volume recommendations.
- [EBSSavingsEstimationMode](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSSavingsEstimationMode.html): Describes the savings estimation mode used for calculating savings opportunity for Amazon EBS volumes.
- [EBSSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for Amazon EBS volume recommendations after applying specific discounts.
- [EBSUtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EBSUtilizationMetric.html): Describes a utilization metric of an Amazon Elastic Block Store (Amazon EBS) volume.
- [ECSEffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSEffectiveRecommendationPreferences.html): Describes the effective recommendation preferences for Amazon ECS services.
- [ECSEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSEstimatedMonthlySavings.html): Describes the estimated monthly savings possible for Amazon ECS services by adopting Compute Optimizer recommendations.
- [ECSSavingsEstimationMode](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSSavingsEstimationMode.html): Describes the savings estimation mode used for calculating savings opportunity for Amazon ECS services.
- [ECSSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for Amazon ECS service recommendations after applying Savings Plans discounts.
- [ECSServiceProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceProjectedMetric.html): Describes the projected metrics of an Amazon ECS service recommendation option.
- [ECSServiceProjectedUtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceProjectedUtilizationMetric.html): Describes the projected utilization metrics of an Amazon ECS service recommendation option.
- [ECSServiceRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendation.html): Describes an Amazon ECS service recommendation.
- [ECSServiceRecommendationFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendationFilter.html): Describes a filter that returns a more specific list of Amazon ECS service recommendations.
- [ECSServiceRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendationOption.html): Describes the recommendation options for an Amazon ECS service.
- [ECSServiceRecommendedOptionProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendedOptionProjectedMetric.html): Describes the projected metrics of an Amazon ECS service recommendation option.
- [ECSServiceUtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceUtilizationMetric.html): Describes the utilization metric of an Amazon ECS service.
- [EffectivePreferredResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EffectivePreferredResource.html): Describes the effective preferred resources that Compute Optimizer considers as rightsizing recommendation candidates.
- [EffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EffectiveRecommendationPreferences.html): Describes the effective recommendation preferences for a resource.
- [EnrollmentFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EnrollmentFilter.html): Describes a filter that returns a more specific list of account enrollment statuses.
- [EstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_EstimatedMonthlySavings.html): Describes the estimated monthly savings amount possible, based on On-Demand instance pricing, by adopting Compute Optimizer recommendations for a given resource.
- [ExportDestination](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExportDestination.html): Describes the destination of the recommendations export and metadata files.
- [ExternalMetricsPreference](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExternalMetricsPreference.html): Describes the external metrics preferences for EC2 rightsizing recommendations.
- [ExternalMetricStatus](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ExternalMetricStatus.html): Describes Compute Optimizer's integration status with your chosen external metric provider.
- [Filter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Filter.html): Describes a filter that returns a more specific list of recommendations.
- [GetRecommendationError](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GetRecommendationError.html): Describes an error experienced when getting recommendations.
- [Gpu](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Gpu.html): Describes the GPU accelerators for the instance type.
- [GpuInfo](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_GpuInfo.html): Describes the GPU accelerator settings for the instance type.
- [IdleEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleEstimatedMonthlySavings.html): Describes the estimated monthly savings possible for idle resources by adopting Compute Optimizer recommendations.
- [IdleRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleRecommendation.html): Describes an Idle resource recommendation.
- [IdleRecommendationError](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleRecommendationError.html): Returns of list of resources that doesn't have idle recommendations.
- [IdleRecommendationFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleRecommendationFilter.html): Describes a filter that returns a more specific list of idle resource recommendations.
- [IdleSavingsOpportunity](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleSavingsOpportunity.html): Describes the savings opportunity for idle resource recommendations.
- [IdleSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for idle resource recommendations after applying discounts.
- [IdleSummary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleSummary.html): Describes the findings summary of the idle resources.
- [IdleUtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleUtilizationMetric.html): Describes the utilization metric of an idle resource.
- [InferredWorkloadSaving](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InferredWorkloadSaving.html): The estimated monthly savings after you adjust the configurations of your instances running on the inferred workload types to the recommended configurations.
- [InstanceEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InstanceEstimatedMonthlySavings.html): An object that describes the estimated monthly savings possible by adopting Compute Optimizerâs Amazon EC2 instance recommendations.
- [InstanceRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InstanceRecommendation.html): Describes an Amazon EC2 instance recommendation.
- [InstanceRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InstanceRecommendationOption.html): Describes a recommendation option for an Amazon EC2 instance.
- [InstanceSavingsEstimationMode](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InstanceSavingsEstimationMode.html): Describes the savings estimation mode used for calculating savings opportunity for Amazon EC2 instances.
- [InstanceSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_InstanceSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for instance recommendations after applying the Savings Plans and Reserved Instances discounts.
- [JobFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_JobFilter.html): Describes a filter that returns a more specific list of recommendation export jobs.
- [LambdaEffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaEffectiveRecommendationPreferences.html): Describes the effective recommendation preferences for Lambda functions.
- [LambdaEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaEstimatedMonthlySavings.html): Describes the estimated monthly savings possible for Lambda functions by adopting Compute Optimizer recommendations.
- [LambdaFunctionMemoryProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionMemoryProjectedMetric.html): Describes a projected utilization metric of an AWS Lambda function recommendation option.
- [LambdaFunctionMemoryRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionMemoryRecommendationOption.html): Describes a recommendation option for an AWS Lambda function.
- [LambdaFunctionRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionRecommendation.html): Describes an AWS Lambda function recommendation.
- [LambdaFunctionRecommendationFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionRecommendationFilter.html): Describes a filter that returns a more specific list of AWS Lambda function recommendations.
- [LambdaFunctionUtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionUtilizationMetric.html): Describes a utilization metric of an AWS Lambda function.
- [LambdaSavingsEstimationMode](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaSavingsEstimationMode.html): Describes the savings estimation used for calculating savings opportunity for Lambda functions.
- [LambdaSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for Lambda functions recommendations after applying Savings Plans discounts.
- [LicenseConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseConfiguration.html): Describes the configuration of a license for an Amazon EC2 instance.
- [LicenseRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseRecommendation.html): Describes a license recommendation for an EC2 instance.
- [LicenseRecommendationFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseRecommendationFilter.html): Describes a filter that returns a more specific list of license recommendations.
- [LicenseRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LicenseRecommendationOption.html): Describes the recommendation options for licenses.
- [MemorySizeConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_MemorySizeConfiguration.html): The memory size configurations of a container.
- [MetricSource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_MetricSource.html): The list of metric sources required to generate recommendations for commercial software licenses.
- [OrderBy](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_OrderBy.html): Describes how the recommendations are ordered.
- [PreferredResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_PreferredResource.html): The preference to control which resource type values are considered when generating rightsizing recommendations.
- [ProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ProjectedMetric.html): Describes a projected utilization metric of a recommendation option, such as an Amazon EC2 instance.
- [RDSDatabaseProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDatabaseProjectedMetric.html): Describes the projected metrics of an Amazon Aurora and RDS database recommendation option.
- [RDSDatabaseRecommendedOptionProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDatabaseRecommendedOptionProjectedMetric.html): Describes the projected metrics of an Amazon Aurora and RDS database recommendation option.
- [RDSDBInstanceRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBInstanceRecommendationOption.html): Describes the recommendation options for a DB instance.
- [RDSDBRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBRecommendation.html): Describes an Amazon Aurora and RDS database recommendation.
- [RDSDBRecommendationFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBRecommendationFilter.html): Describes a filter that returns a more specific list of DB instance recommendations.
- [RDSDBStorageRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBStorageRecommendationOption.html): Describes the recommendation options for DB storage.
- [RDSDBUtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSDBUtilizationMetric.html): Describes the utilization metric of an Amazon Aurora and RDS database.
- [RDSEffectiveRecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSEffectiveRecommendationPreferences.html): Describes the effective recommendation preferences for Amazon Aurora and RDS databases.
- [RDSInstanceEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSInstanceEstimatedMonthlySavings.html): Describes the estimated monthly savings possible for DB instances by adopting Compute Optimizer recommendations.
- [RDSInstanceSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSInstanceSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for DB instance recommendations after applying Savings Plans discounts.
- [RDSSavingsEstimationMode](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSSavingsEstimationMode.html): Describes the savings estimation mode used for calculating savings opportunity for DB instances.
- [RDSStorageEstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSStorageEstimatedMonthlySavings.html): Describes the estimated monthly savings possible for DB instance storage by adopting Compute Optimizer recommendations.
- [RDSStorageSavingsOpportunityAfterDiscounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RDSStorageSavingsOpportunityAfterDiscounts.html): Describes the savings opportunity for Amazon RDS storage recommendations after applying Savings Plans discounts.
- [ReasonCodeSummary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ReasonCodeSummary.html): A summary of a finding reason code.
- [RecommendationExportJob](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationExportJob.html): Describes a recommendation export job.
- [RecommendationPreferences](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationPreferences.html): Describes the recommendation preferences to return in the response of a , , , , and request.
- [RecommendationPreferencesDetail](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationPreferencesDetail.html): Describes a recommendation preference.
- [RecommendationSource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationSource.html): Describes the source of a recommendation, such as an Amazon EC2 instance or Auto Scaling group.
- [RecommendationSummary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationSummary.html): A summary of a recommendation.
- [RecommendedOptionProjectedMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendedOptionProjectedMetric.html): Describes a projected utilization metric of a recommendation option.
- [S3Destination](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_S3Destination.html): Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and object keys of a recommendations export file, and its associated metadata file.
- [S3DestinationConfig](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_S3DestinationConfig.html): Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name and key prefix for a recommendations export job.
- [SavingsOpportunity](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_SavingsOpportunity.html): Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.
- [Scope](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Scope.html): Describes the scope of a recommendation preference.
- [ServiceConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ServiceConfiguration.html): The Amazon ECS service configurations used for recommendations.
- [Summary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Summary.html): The summary of a recommendation.
- [Tag](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_Tag.html): A list of tag key and value pairs that you define.
- [UtilizationMetric](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_UtilizationMetric.html): Describes a utilization metric of a resource, such as an Amazon EC2 instance.
- [UtilizationPreference](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_UtilizationPreference.html): The preference to control the resourceâs CPU utilization threshold, CPU utilization headroom, and memory utilization headroom.
- [VolumeConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_VolumeConfiguration.html): Describes the configuration of an Amazon Elastic Block Store (Amazon EBS) volume.
- [VolumeRecommendation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_VolumeRecommendation.html): Describes an Amazon Elastic Block Store (Amazon EBS) volume recommendation.
- [VolumeRecommendationOption](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_VolumeRecommendationOption.html): Describes a recommendation option for an Amazon Elastic Block Store (Amazon EBS) instance.

## [Compute Optimizer Automation](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/Welcome_Compute_Optimizer_Automation.html)

Automation is a feature within AWS Compute Optimizer that enables you to apply optimization recommendations to your AWS resources, reducing costs and improving performance. You can apply recommended actions directly or create automation rules that implement recommendations on a recurring schedule when they match your specified criteria. With automation rules, set criteria such as AWS Region and Resource Tags to target specific geographies and workloads. Configure rules to run daily, weekly, or monthly, and Compute Optimizer continuously evaluates new recommendations against your criteria. Track automation events over time, examine detailed step history, estimate savings achieved, and reverse actions directly from Compute Optimizer when needed.

### Actions

- [AssociateAccounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AssociateAccounts.html): Associates one or more member accounts with your organization's management account, enabling centralized implementation of optimization actions across those accounts.
- [CreateAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_CreateAutomationRule.html): Creates a new automation rule to apply recommended actions to resources based on specified criteria.
- [DeleteAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DeleteAutomationRule.html): Deletes an existing automation rule.
- [DisassociateAccounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DisassociateAccounts.html): Disassociates member accounts from your organization's management account, removing centralized automation capabilities.
- [GetAutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetAutomationEvent.html): Retrieves details about a specific automation event.
- [GetAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetAutomationRule.html): Retrieves details about a specific automation rule.
- [GetEnrollmentConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetEnrollmentConfiguration.html): Retrieves the current enrollment configuration for Compute Optimizer Automation.
- [ListAccounts](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAccounts.html): Lists the accounts in your organization that are enrolled in Compute Optimizer and whether they have enabled Automation.
- [ListAutomationEvents](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEvents.html): Lists automation events based on specified filters.
- [ListAutomationEventSteps](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEventSteps.html): Lists the steps for a specific automation event.
- [ListAutomationEventSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationEventSummaries.html): Provides a summary of automation events based on specified filters.
- [ListAutomationRulePreview](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRulePreview.html): Returns a preview of the recommended actions that match your Automation rule's configuration and criteria.
- [ListAutomationRulePreviewSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRulePreviewSummaries.html): Returns a summary of the recommended actions that match your rule preview configuration and criteria.
- [ListAutomationRules](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAutomationRules.html): Lists the automation rules that match specified filters.
- [ListRecommendedActions](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListRecommendedActions.html): Lists the recommended actions based that match specified filters.
- [ListRecommendedActionSummaries](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListRecommendedActionSummaries.html): Provides a summary of recommended actions based on specified filters.
- [ListTagsForResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListTagsForResource.html): Lists the tags for a specified resource.
- [RollbackAutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RollbackAutomationEvent.html): Initiates a rollback for a completed automation event.
- [StartAutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_StartAutomationEvent.html): Initiates a one-time, on-demand automation for the specified recommended action.
- [TagResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_TagResource.html): Adds tags to the specified resource.
- [UntagResource](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UntagResource.html): Removes tags from the specified resource.
- [UpdateAutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UpdateAutomationRule.html): Updates an existing automation rule.
- [UpdateEnrollmentConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UpdateEnrollmentConfiguration.html): Updates your accountâs Compute Optimizer Automation enrollment configuration.

### Data Types

- [AccountInfo](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AccountInfo.html): Contains information about an AWS account's enrollment and association status with Compute Optimizer Automation.
- [AutomationEvent](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEvent.html): Contains information about an automation event.
- [AutomationEventFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEventFilter.html): A filter to apply when listing automation events.
- [AutomationEventStep](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEventStep.html): Contains information about a step in an automation event.
- [AutomationEventSummary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationEventSummary.html): A summary of automation events grouped by specified dimensions.
- [AutomationRule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_AutomationRule.html): Represents a complete automation rule configuration including criteria, schedule, and execution settings.
- [Criteria](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Criteria.html): A set of conditions that specify which recommended action qualify for implementation.
- [DoubleCriteriaCondition](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DoubleCriteriaCondition.html): Defines a condition for filtering based on double/floating-point numeric values with comparison operators.
- [EbsVolume](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_EbsVolume.html): Represents an Amazon EBS volume with its configuration and snapshot usage information.
- [EbsVolumeConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_EbsVolumeConfiguration.html): Configuration details for an Amazon EBS volume.
- [EstimatedMonthlySavings](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_EstimatedMonthlySavings.html): Contains information about estimated monthly cost savings.
- [Filter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Filter.html): A filter used to narrow down results based on specific criteria.
- [IntegerCriteriaCondition](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_IntegerCriteriaCondition.html): Defines a condition for filtering based on integer values with comparison operators.
- [OrganizationConfiguration](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationConfiguration.html): Configuration settings for organization-wide automation rules.
- [OrganizationScope](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_OrganizationScope.html): Defines the scope for organization-level rules when previewing matching actions.
- [PreviewResult](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_PreviewResult.html): Contains the results of previewing an automation rule against available recommendations.
- [PreviewResultSummary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_PreviewResultSummary.html): Contains a summary of preview results for an automation rule.
- [RecommendedAction](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedAction.html): Contains information about a recommended action that can be applied to optimize an AWS resource.
- [RecommendedActionFilter](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedActionFilter.html): A filter used to narrow down recommended action results based on specific criteria.
- [RecommendedActionSummary](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedActionSummary.html): Summary information about recommended actions, grouped by specific criteria with totals and counts.
- [RecommendedActionTotal](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RecommendedActionTotal.html): Aggregate totals for a group of recommended actions, including count and estimated monthly savings.
- [ResourceDetails](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ResourceDetails.html): Detailed configuration information for a specific AWS resource, with type-specific details.
- [ResourceTagsCriteriaCondition](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ResourceTagsCriteriaCondition.html): Criteria condition for filtering resources based on their tags, including comparison operators and values.
- [RulePreviewTotal](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_RulePreviewTotal.html): Aggregate totals for automation rule preview results, including count and estimated savings.
- [Schedule](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Schedule.html): Configuration for scheduling when automation rules should execute, including timing and execution windows.
- [StringCriteriaCondition](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_StringCriteriaCondition.html): Criteria condition for filtering based on string values, including comparison operators and target values.
- [SummaryDimension](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_SummaryDimension.html): A key-value pair used to categorize and group summary data for analysis and reporting.
- [SummaryTotals](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_SummaryTotals.html): Aggregate totals for automation events, including counts and estimated savings.
- [Tag](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_Tag.html): A key-value pair used to categorize and organize AWS resources and automation rules.
- [TimePeriod](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_TimePeriod.html): Defines a time range with inclusive start time and exclusive end time for filtering and analysis.

## Common

- [Common Parameters](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/CommonErrors.html)