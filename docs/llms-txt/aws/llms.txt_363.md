# Source: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/llms.txt

# Amazon EMR on EKS Amazon EMR on EKS API Reference

> Amazon EMR on EKS provides a deployment option for Amazon EMR that allows you to run open-source big data frameworks on Amazon Elastic Kubernetes Service (Amazon EKS). With this deployment option, you can focus on running analytics workloads while Amazon EMR on EKS builds, configures, and manages containers for open-source applications. For more information about Amazon EMR on EKS concepts and tasks, see What is Amazon EMR on EKS.

- [Welcome](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Operations.html)

- [CancelJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CancelJobRun.html): Cancels a job run.
- [CreateJobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateJobTemplate.html): Creates a job template.
- [CreateManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateManagedEndpoint.html): Creates a managed endpoint.
- [CreateSecurityConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateSecurityConfiguration.html): Creates a security configuration.
- [CreateVirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CreateVirtualCluster.html): Creates a virtual cluster.
- [DeleteJobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteJobTemplate.html): Deletes a job template.
- [DeleteManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteManagedEndpoint.html): Deletes a managed endpoint.
- [DeleteVirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DeleteVirtualCluster.html): Deletes a virtual cluster.
- [DescribeJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeJobRun.html): Displays detailed information about a job run.
- [DescribeJobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeJobTemplate.html): Displays detailed information about a specified job template.
- [DescribeManagedEndpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeManagedEndpoint.html): Displays detailed information about a managed endpoint.
- [DescribeSecurityConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeSecurityConfiguration.html): Displays detailed information about a specified security configuration.
- [DescribeVirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_DescribeVirtualCluster.html): Displays detailed information about a specified virtual cluster.
- [GetManagedEndpointSessionCredentials](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_GetManagedEndpointSessionCredentials.html): Generate a session token to connect to a managed endpoint.
- [ListJobRuns](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListJobRuns.html): Lists job runs based on a set of parameters.
- [ListJobTemplates](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListJobTemplates.html): Lists job templates based on a set of parameters.
- [ListManagedEndpoints](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListManagedEndpoints.html): Lists managed endpoints based on a set of parameters.
- [ListSecurityConfigurations](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListSecurityConfigurations.html): Lists security configurations based on a set of parameters.
- [ListTagsForResource](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListTagsForResource.html): Lists the tags assigned to the resources.
- [ListVirtualClusters](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ListVirtualClusters.html): Lists information about the specified virtual cluster.
- [StartJobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_StartJobRun.html): Starts a job run.
- [TagResource](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_TagResource.html): Assigns tags to resources.
- [UntagResource](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_UntagResource.html): Removes tags from resources.


## [Data Types](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Types.html)

- [AuthorizationConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_AuthorizationConfiguration.html): Authorization-related configuration inputs for the security configuration.
- [Certificate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Certificate.html): The entity representing certificate data generated for managed endpoint.
- [CloudWatchMonitoringConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_CloudWatchMonitoringConfiguration.html): A configuration for CloudWatch monitoring.
- [Configuration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Configuration.html): A configuration specification to be used when provisioning virtual clusters, which can include configurations for applications and software bundled with Amazon EMR on EKS.
- [ConfigurationOverrides](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ConfigurationOverrides.html): A configuration specification to be used to override existing configurations.
- [ContainerInfo](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ContainerInfo.html): The information about the container used for a job run or a managed endpoint.
- [ContainerLogRotationConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ContainerLogRotationConfiguration.html): The settings for container log rotation.
- [ContainerProvider](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ContainerProvider.html): The information about the container provider.
- [Credentials](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Credentials.html): The structure containing the session token being returned.
- [EksInfo](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_EksInfo.html): The information about the Amazon EKS cluster.
- [EncryptionConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_EncryptionConfiguration.html): Configurations related to encryption for the security configuration.
- [Endpoint](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_Endpoint.html): This entity represents the endpoint that is managed by Amazon EMR on EKS.
- [InTransitEncryptionConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_InTransitEncryptionConfiguration.html): Configurations related to in-transit encryption for the security configuration.
- [JobDriver](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobDriver.html): Specify the driver that the job runs on.
- [JobRun](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobRun.html): This entity describes a job run.
- [JobTemplate](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobTemplate.html): This entity describes a job template.
- [JobTemplateData](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_JobTemplateData.html): The values of StartJobRun API requests used in job runs started using the job template.
- [LakeFormationConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_LakeFormationConfiguration.html): AWS Lake Formation related configuration inputs for the security configuration.
- [ManagedLogs](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ManagedLogs.html): The entity that provides configuration control over managed logs.
- [MonitoringConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_MonitoringConfiguration.html): Configuration setting for monitoring.
- [ParametricCloudWatchMonitoringConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricCloudWatchMonitoringConfiguration.html): A configuration for CloudWatch monitoring.
- [ParametricConfigurationOverrides](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricConfigurationOverrides.html): A configuration specification to be used to override existing configurations.
- [ParametricMonitoringConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricMonitoringConfiguration.html): Configuration setting for monitoring.
- [ParametricS3MonitoringConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricS3MonitoringConfiguration.html): Amazon S3 configuration for monitoring log publishing.
- [RetryPolicyConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_RetryPolicyConfiguration.html): The configuration of the retry policy that the job runs on.
- [RetryPolicyExecution](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_RetryPolicyExecution.html): The current status of the retry policy executed on the job.
- [S3MonitoringConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_S3MonitoringConfiguration.html): Amazon S3 configuration for monitoring log publishing.
- [SecureNamespaceInfo](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SecureNamespaceInfo.html): Namespace inputs for the system job.
- [SecurityConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SecurityConfiguration.html): Inputs related to the security configuration.
- [SecurityConfigurationData](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SecurityConfigurationData.html): Configurations related to the security configuration for the request.
- [SparkSqlJobDriver](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SparkSqlJobDriver.html): The job driver for job type.
- [SparkSubmitJobDriver](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_SparkSubmitJobDriver.html): The information about job driver for Spark submit.
- [TemplateParameterConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_TemplateParameterConfiguration.html): The configuration of a job template parameter.
- [TLSCertificateConfiguration](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_TLSCertificateConfiguration.html): Configurations related to the TLS certificate for the security configuration.
- [VirtualCluster](https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_VirtualCluster.html): This entity describes a virtual cluster.
