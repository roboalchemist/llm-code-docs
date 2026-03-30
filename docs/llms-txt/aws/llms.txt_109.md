# Source: https://docs.aws.amazon.com/arc-region-switch/latest/api/llms.txt

# Amazon Application Recovery Controller API Reference Guide for Region Switch

> Amazon Application Recovery Controller (ARC) Region switch helps you to quickly and reliably shift traffic away from an impaired AWS Region to a healthy Region. With Region switch, you can create plans that define the steps to shift traffic for your application from one AWS Region to another.

- [Welcome](https://docs.aws.amazon.com/arc-region-switch/latest/api/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/arc-region-switch/latest/api/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/arc-region-switch/latest/api/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Operations.html)

- [ApprovePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ApprovePlanExecutionStep.html): Approves a step in a plan execution that requires manual approval.
- [CancelPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CancelPlanExecution.html): Cancels an in-progress plan execution.
- [CreatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CreatePlan.html): Creates a new Region switch plan.
- [DeletePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DeletePlan.html): Deletes a Region switch plan.
- [GetPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlan.html): Retrieves detailed information about a Region switch plan.
- [GetPlanEvaluationStatus](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanEvaluationStatus.html): Retrieves the evaluation status of a Region switch plan.
- [GetPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanExecution.html): Retrieves detailed information about a specific plan execution.
- [GetPlanInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GetPlanInRegion.html): Retrieves information about a Region switch plan in a specific AWS Region.
- [ListPlanExecutionEvents](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutionEvents.html): Lists the events that occurred during a plan execution.
- [ListPlanExecutions](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlanExecutions.html): Lists the executions of a Region switch plan.
- [ListPlans](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlans.html): Lists all Region switch plans in your AWS account.
- [ListPlansInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListPlansInRegion.html): Lists all Region switch plans in your AWS account that are available in the current AWS Region.
- [ListRoute53HealthChecks](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecks.html): List the Amazon Route 53 health checks.
- [ListRoute53HealthChecksInRegion](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListRoute53HealthChecksInRegion.html): List the Amazon Route 53 health checks in a specific AWS Region.
- [ListTagsForResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ListTagsForResource.html): Lists the tags attached to a Region switch resource.
- [StartPlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_StartPlanExecution.html): Starts the execution of a Region switch plan.
- [TagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TagResource.html): Adds or updates tags for a Region switch resource.
- [UntagResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UntagResource.html): Removes tags from a Region switch resource.
- [UpdatePlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlan.html): Updates an existing Region switch plan.
- [UpdatePlanExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecution.html): Updates an in-progress plan execution.
- [UpdatePlanExecutionStep](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_UpdatePlanExecutionStep.html): Updates a specific step in an in-progress plan execution.


## [Data Types](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Types.html)

- [AbbreviatedExecution](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AbbreviatedExecution.html): A summarized representation of a plan execution.
- [AbbreviatedPlan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AbbreviatedPlan.html): A summarized representation of a Region switch plan.
- [ArcRoutingControlConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ArcRoutingControlConfiguration.html): Configuration for ARC routing controls used in a Region switch plan.
- [ArcRoutingControlState](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ArcRoutingControlState.html): Represents the state of an ARC routing control.
- [Asg](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Asg.html): Configuration for an Amazon EC2 Auto Scaling group used in a Region switch plan.
- [AssociatedAlarm](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_AssociatedAlarm.html): An Amazon CloudWatch alarm associated with a Region switch plan.
- [CustomActionLambdaConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_CustomActionLambdaConfiguration.html): Configuration for AWS Lambda functions that perform custom actions during a Region switch.
- [DocumentDbConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DocumentDbConfiguration.html): Configuration for Amazon DocumentDB global clusters used in a Region switch plan.
- [DocumentDbUngraceful](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_DocumentDbUngraceful.html): Configuration for handling failures when performing operations on DocumentDB global clusters.
- [Ec2AsgCapacityIncreaseConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Ec2AsgCapacityIncreaseConfiguration.html): Configuration for increasing the capacity of Amazon EC2 Auto Scaling groups during a Region switch.
- [Ec2Ungraceful](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Ec2Ungraceful.html): Configuration for handling failures when performing operations on EC2 resources.
- [EcsCapacityIncreaseConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EcsCapacityIncreaseConfiguration.html): The configuration for an AWS ECS capacity increase.
- [EcsUngraceful](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EcsUngraceful.html): The settings for ungraceful execution.
- [EksCluster](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EksCluster.html): The AWS EKS cluster execution block configuration.
- [EksResourceScalingConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EksResourceScalingConfiguration.html): The AWS EKS resource scaling configuration.
- [EksResourceScalingUngraceful](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_EksResourceScalingUngraceful.html): The ungraceful settings for AWS EKS resource scaling.
- [ExecutionApprovalConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ExecutionApprovalConfiguration.html): Configuration for approval steps in a Region switch plan execution.
- [ExecutionBlockConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ExecutionBlockConfiguration.html): Execution block configurations for a workflow in a Region switch plan.
- [ExecutionEvent](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ExecutionEvent.html): Represents an event that occurred during a plan execution.
- [FailedReportOutput](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_FailedReportOutput.html): Information about a report generation that failed.
- [GeneratedReport](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GeneratedReport.html): Information about a generated execution report.
- [GlobalAuroraConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GlobalAuroraConfiguration.html): Configuration for Amazon Aurora global databases used in a Region switch plan.
- [GlobalAuroraUngraceful](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_GlobalAuroraUngraceful.html): Configuration for handling failures when performing operations on Aurora global databases.
- [KubernetesResourceType](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_KubernetesResourceType.html): Defines the type of Kubernetes resource to scale in an Amazon EKS cluster.
- [KubernetesScalingResource](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_KubernetesScalingResource.html): Defines a Kubernetes resource to scale in an Amazon EKS cluster.
- [Lambdas](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Lambdas.html): Configuration for AWS Lambda functions used in a Region switch plan.
- [LambdaUngraceful](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_LambdaUngraceful.html): Configuration for handling failures when invoking Lambda functions.
- [MinimalWorkflow](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_MinimalWorkflow.html): A simplified representation of a workflow in a Region switch plan.
- [ParallelExecutionBlockConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ParallelExecutionBlockConfiguration.html): Configuration for steps that should be executed in parallel during a Region switch.
- [Plan](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Plan.html): Represents a Region switch plan.
- [RdsCreateCrossRegionReplicaConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_RdsCreateCrossRegionReplicaConfiguration.html): Configuration for creating an Amazon RDS cross-Region read replica during post-recovery in a Region switch.
- [RdsPromoteReadReplicaConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_RdsPromoteReadReplicaConfiguration.html): Configuration for promoting an Amazon RDS read replica to a standalone database instance during a Region switch.
- [RegionSwitchPlanConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_RegionSwitchPlanConfiguration.html): Configuration for nested Region switch plans.
- [ReportConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ReportConfiguration.html): Configuration for automatic report generation for plan executions.
- [ReportOutput](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ReportOutput.html): The output location or cause of a failure in report generation.
- [ReportOutputConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ReportOutputConfiguration.html): Configuration for report output destinations used in a Region switch plan.
- [ResourceWarning](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ResourceWarning.html): Represents a warning about a resource in a Region switch plan.
- [Route53HealthCheck](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Route53HealthCheck.html): The Amazon Route 53 health check.
- [Route53HealthCheckConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Route53HealthCheckConfiguration.html): The Amazon Route 53 health check configuration.
- [Route53ResourceRecordSet](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Route53ResourceRecordSet.html): The Amazon Route 53 record set.
- [S3ReportOutput](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_S3ReportOutput.html): Information about a report delivered to Amazon S3.
- [S3ReportOutputConfiguration](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_S3ReportOutputConfiguration.html): Configuration for delivering generated reports to an Amazon S3 bucket.
- [Service](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Service.html): The service for a cross account role.
- [Step](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Step.html): Represents a step in a Region switch plan workflow.
- [StepState](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_StepState.html): Represents the state of a step in a plan execution.
- [Trigger](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Trigger.html): Defines a condition that can automatically trigger the execution of a Region switch plan.
- [TriggerCondition](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_TriggerCondition.html): Defines a condition that must be met for a trigger to fire.
- [Workflow](https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Workflow.html): Represents a workflow in a Region switch plan.
