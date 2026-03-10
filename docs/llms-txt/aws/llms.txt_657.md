# Source: https://docs.aws.amazon.com/pcs/latest/APIReference/llms.txt

# AWS PCS API Reference

> AWS Parallel Computing Service (AWS PCS) is a managed service that makes it easier for you to run and scale your high performance computing (HPC) workloads, and build scientific and engineering models on AWS using Slurm. For more information, see the AWS Parallel Computing Service User Guide.

- [Welcome](https://docs.aws.amazon.com/pcs/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/pcs/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/pcs/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Operations.html)

- [CreateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateCluster.html): Creates a cluster in your account.
- [CreateComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateComputeNodeGroup.html): Creates a managed set of compute nodes.
- [CreateQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CreateQueue.html): Creates a job queue.
- [DeleteCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeleteCluster.html): Deletes a cluster and all its linked resources.
- [DeleteComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeleteComputeNodeGroup.html): Deletes a compute node group.
- [DeleteQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_DeleteQueue.html): Deletes a job queue.
- [GetCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetCluster.html): Returns detailed information about a running cluster in your account.
- [GetComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetComputeNodeGroup.html): Returns detailed information about a compute node group.
- [GetQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_GetQueue.html): Returns detailed information about a queue.
- [ListClusters](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListClusters.html): Returns a list of running clusters in your account.
- [ListComputeNodeGroups](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListComputeNodeGroups.html): Returns a list of all compute node groups associated with a cluster.
- [ListQueues](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListQueues.html): Returns a list of all queues associated with a cluster.
- [ListTagsForResource](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ListTagsForResource.html): Returns a list of all tags on an AWS PCS resource.
- [RegisterComputeNodeGroupInstance](https://docs.aws.amazon.com/pcs/latest/APIReference/API_RegisterComputeNodeGroupInstance.html)
- [TagResource](https://docs.aws.amazon.com/pcs/latest/APIReference/API_TagResource.html): Adds or edits tags on an AWS PCS resource.
- [UntagResource](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UntagResource.html): Deletes tags from an AWS PCS resource.
- [UpdateCluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateCluster.html): Updates a cluster configuration.
- [UpdateComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateComputeNodeGroup.html): Updates a compute node group.
- [UpdateQueue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateQueue.html): Updates the compute node group configuration of a queue.


## [Data Types](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Types.html)

- [Accounting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Accounting.html): The accounting configuration includes configurable settings for Slurm accounting.
- [AccountingRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_AccountingRequest.html): The accounting configuration includes configurable settings for Slurm accounting.
- [Cluster](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Cluster.html): The cluster resource and configuration.
- [ClusterSlurmConfiguration](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSlurmConfiguration.html): Additional options related to the Slurm scheduler.
- [ClusterSlurmConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSlurmConfigurationRequest.html): Additional options related to the Slurm scheduler.
- [ClusterSummary](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ClusterSummary.html): The object returned by the ListClusters API action.
- [ComputeNodeGroup](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroup.html): A compute node group associated with a cluster.
- [ComputeNodeGroupConfiguration](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroupConfiguration.html): The compute node group configuration for a queue.
- [ComputeNodeGroupSlurmConfiguration](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroupSlurmConfiguration.html): Additional options related to the Slurm scheduler.
- [ComputeNodeGroupSlurmConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroupSlurmConfigurationRequest.html): Additional options related to the Slurm scheduler.
- [ComputeNodeGroupSummary](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ComputeNodeGroupSummary.html): The object returned by the ListComputeNodeGroups API action.
- [CustomLaunchTemplate](https://docs.aws.amazon.com/pcs/latest/APIReference/API_CustomLaunchTemplate.html): An Amazon EC2 launch template AWS PCS uses to launch compute nodes.
- [Endpoint](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Endpoint.html): An endpoint available for interaction with the scheduler.
- [ErrorInfo](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ErrorInfo.html): An error that occurred during resource creation.
- [InstanceConfig](https://docs.aws.amazon.com/pcs/latest/APIReference/API_InstanceConfig.html): An EC2 instance configuration AWS PCS uses to launch compute nodes.
- [JwtAuth](https://docs.aws.amazon.com/pcs/latest/APIReference/API_JwtAuth.html): The JWT authentication configuration for Slurm REST API access.
- [JwtKey](https://docs.aws.amazon.com/pcs/latest/APIReference/API_JwtKey.html): The JWT key stored in AWS Secrets Manager for Slurm REST API authentication.
- [Networking](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Networking.html): The networking configuration for the cluster's control plane.
- [NetworkingRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_NetworkingRequest.html): The networking configuration for the cluster's control plane.
- [Queue](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Queue.html): A queue resource.
- [QueueSlurmConfiguration](https://docs.aws.amazon.com/pcs/latest/APIReference/API_QueueSlurmConfiguration.html): Additional options related to the Slurm scheduler.
- [QueueSlurmConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_QueueSlurmConfigurationRequest.html): Additional options related to the Slurm scheduler.
- [QueueSummary](https://docs.aws.amazon.com/pcs/latest/APIReference/API_QueueSummary.html): The object returned by the ListQueues API action.
- [ScalingConfiguration](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ScalingConfiguration.html): Specifies the boundaries of the compute node group auto scaling.
- [ScalingConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ScalingConfigurationRequest.html): Specifies the boundaries of the compute node group auto scaling.
- [Scheduler](https://docs.aws.amazon.com/pcs/latest/APIReference/API_Scheduler.html): The cluster management and job scheduling software associated with the cluster.
- [SchedulerRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SchedulerRequest.html): The cluster management and job scheduling software associated with the cluster.
- [SlurmAuthKey](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmAuthKey.html): The shared Slurm key for authentication, also known as the cluster secret.
- [SlurmCustomSetting](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmCustomSetting.html): Additional settings that directly map to Slurm settings.
- [SlurmRest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmRest.html): The Slurm REST API configuration includes settings for enabling and configuring the Slurm REST API.
- [SlurmRestRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SlurmRestRequest.html): The Slurm REST API configuration includes settings for enabling and configuring the Slurm REST API.
- [SpotOptions](https://docs.aws.amazon.com/pcs/latest/APIReference/API_SpotOptions.html): Additional configuration when you specify SPOT as the purchaseOption for the CreateComputeNodeGroup API action.
- [UpdateAccountingRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateAccountingRequest.html): The accounting configuration includes configurable settings for Slurm accounting.
- [UpdateClusterSlurmConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateClusterSlurmConfigurationRequest.html): Additional options related to the Slurm scheduler.
- [UpdateComputeNodeGroupSlurmConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateComputeNodeGroupSlurmConfigurationRequest.html): Additional options related to the Slurm scheduler.
- [UpdateQueueSlurmConfigurationRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateQueueSlurmConfigurationRequest.html): Additional options related to the Slurm scheduler.
- [UpdateSlurmRestRequest](https://docs.aws.amazon.com/pcs/latest/APIReference/API_UpdateSlurmRestRequest.html): The Slurm REST API configuration includes settings for enabling and configuring the Slurm REST API.
- [ValidationExceptionField](https://docs.aws.amazon.com/pcs/latest/APIReference/API_ValidationExceptionField.html): Stores information about a field in a request that caused an exception.
