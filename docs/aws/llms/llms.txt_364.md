# Source: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/llms.txt

# Amazon EMR Serverless EMR Serverless API Reference

> Amazon EMR Serverless is a new deployment option for Amazon EMR. Amazon EMR Serverless provides a serverless runtime environment that simplifies running analytics applications using the latest open source frameworks such as Apache Spark and Apache Hive. With Amazon EMR Serverless, you donât have to configure, optimize, secure, or operate clusters to run applications with these frameworks.

- [Welcome](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Operations.html)

- [CancelJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CancelJobRun.html): Cancels a job run.
- [CreateApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CreateApplication.html): Creates an application.
- [DeleteApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_DeleteApplication.html): Deletes an application.
- [GetApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetApplication.html): Displays detailed information about a specified application.
- [GetDashboardForJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetDashboardForJobRun.html): Creates and returns a URL that you can use to access the application UIs for a job run.
- [GetJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetJobRun.html): Displays detailed information about a job run.
- [ListApplications](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListApplications.html): Lists applications based on a set of parameters.
- [ListJobRunAttempts](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRunAttempts.html): Lists all attempt of a job run.
- [ListJobRuns](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListJobRuns.html): Lists job runs based on a set of parameters.
- [ListTagsForResource](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ListTagsForResource.html): Lists the tags assigned to the resources.
- [StartApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartApplication.html): Starts a specified application and initializes initial capacity if configured.
- [StartJobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StartJobRun.html): Starts a job run.
- [StopApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_StopApplication.html): Stops a specified application and releases initial capacity if configured.
- [TagResource](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_TagResource.html): Assigns tags to resources.
- [UntagResource](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_UntagResource.html): Removes tags from resources.
- [UpdateApplication](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_UpdateApplication.html): Updates a specified application.


## [Data Types](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Types.html)

- [Application](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Application.html): Information about an application.
- [ApplicationSummary](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ApplicationSummary.html): The summary of attributes associated with an application.
- [AutoStartConfig](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_AutoStartConfig.html): The configuration for an application to automatically start on job submission.
- [AutoStopConfig](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_AutoStopConfig.html): The configuration for an application to automatically stop after a certain amount of time being idle.
- [CloudWatchLoggingConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_CloudWatchLoggingConfiguration.html): The Amazon CloudWatch configuration for monitoring logs.
- [Configuration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Configuration.html): A configuration specification to be used when provisioning an application.
- [ConfigurationOverrides](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ConfigurationOverrides.html): A configuration specification to be used to override existing configurations.
- [DiskEncryptionConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_DiskEncryptionConfiguration.html): The configuration object that allows encrypting local disks.
- [Hive](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_Hive.html): The configurations for the Hive job driver.
- [IdentityCenterConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_IdentityCenterConfiguration.html): The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation.
- [IdentityCenterConfigurationInput](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_IdentityCenterConfigurationInput.html): The IAM Identity Center Configuration accepts the Identity Center instance parameter required to enable trusted identity propagation.
- [ImageConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ImageConfiguration.html): The applied image configuration.
- [ImageConfigurationInput](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ImageConfigurationInput.html): The image configuration.
- [InitialCapacityConfig](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_InitialCapacityConfig.html): The initial capacity configuration per worker.
- [InteractiveConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_InteractiveConfiguration.html): The configuration to use to enable the different types of interactive use cases in an application.
- [JobDriver](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobDriver.html): The driver that the job runs on.
- [JobLevelCostAllocationConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobLevelCostAllocationConfiguration.html): The configuration object that enables job level cost allocation.
- [JobRun](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRun.html): Information about a job run.
- [JobRunAttemptSummary](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRunAttemptSummary.html): The summary of attributes associated with a job run attempt.
- [JobRunExecutionIamPolicy](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRunExecutionIamPolicy.html): Optional IAM policy.
- [JobRunSummary](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRunSummary.html): The summary of attributes associated with a job run.
- [ManagedPersistenceMonitoringConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ManagedPersistenceMonitoringConfiguration.html): The managed log persistence configuration for a job run.
- [MaximumAllowedResources](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_MaximumAllowedResources.html): The maximum allowed cumulative resources for an application.
- [MonitoringConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_MonitoringConfiguration.html): The configuration setting for monitoring.
- [NetworkConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_NetworkConfiguration.html): The network configuration for customer VPC connectivity.
- [PrometheusMonitoringConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_PrometheusMonitoringConfiguration.html): The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.
- [ResourceUtilization](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_ResourceUtilization.html): The resource utilization for memory, storage, and vCPU for jobs.
- [RetryPolicy](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_RetryPolicy.html): The retry policy to use for a job run.
- [S3MonitoringConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_S3MonitoringConfiguration.html): The Amazon S3 configuration for monitoring log publishing.
- [SchedulerConfiguration](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_SchedulerConfiguration.html): The scheduler configuration for batch and streaming jobs running on this application.
- [SparkSubmit](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_SparkSubmit.html): The configurations for the Spark submit job driver.
- [TotalResourceUtilization](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_TotalResourceUtilization.html): The aggregate vCPU, memory, and storage resources used from the time job start executing till the time job is terminated, rounded up to the nearest second.
- [WorkerResourceConfig](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_WorkerResourceConfig.html): The cumulative configuration requirements for every worker instance of the worker type.
- [WorkerTypeSpecification](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_WorkerTypeSpecification.html): The specifications for a worker type.
- [WorkerTypeSpecificationInput](https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_WorkerTypeSpecificationInput.html): The specifications for a worker type.
