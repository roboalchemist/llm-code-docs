# Source: https://docs.aws.amazon.com/drs/latest/APIReference/llms.txt

# AWS Elastic Disaster Recovery AWS Elastic Disaster Recovery Api Docs

> AWS Elastic Disaster Recovery Service.

- [Welcome](https://docs.aws.amazon.com/drs/latest/APIReference/Welcome.html)
- [Common Parameters](https://docs.aws.amazon.com/drs/latest/APIReference/CommonParameters.html)
- [Common Errors](https://docs.aws.amazon.com/drs/latest/APIReference/CommonErrors.html)

## [Actions](https://docs.aws.amazon.com/drs/latest/APIReference/API_Operations.html)

- [AssociateSourceNetworkStack](https://docs.aws.amazon.com/drs/latest/APIReference/API_AssociateSourceNetworkStack.html): Associate a Source Network to an existing CloudFormation Stack and modify launch templates to use this network.
- [CreateExtendedSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateExtendedSourceServer.html): Create an extended source server in the target Account based on the source server in staging account.
- [CreateLaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateLaunchConfigurationTemplate.html): Creates a new Launch Configuration Template.
- [CreateReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateReplicationConfigurationTemplate.html): Creates a new ReplicationConfigurationTemplate.
- [CreateSourceNetwork](https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateSourceNetwork.html): Create a new Source Network resource for a provided VPC ID.
- [DeleteJob](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteJob.html): Deletes a single Job by ID.
- [DeleteLaunchAction](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteLaunchAction.html): Deletes a resource launch action.
- [DeleteLaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteLaunchConfigurationTemplate.html): Deletes a single Launch Configuration Template by ID.
- [DeleteRecoveryInstance](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteRecoveryInstance.html): Deletes a single Recovery Instance by ID.
- [DeleteReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteReplicationConfigurationTemplate.html): Deletes a single Replication Configuration Template by ID
- [DeleteSourceNetwork](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteSourceNetwork.html): Delete Source Network resource.
- [DeleteSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteSourceServer.html): Deletes a single Source Server by ID.
- [DescribeJobLogItems](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobLogItems.html): Retrieves a detailed Job log with pagination.
- [DescribeJobs](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobs.html): Returns a list of Jobs.
- [DescribeLaunchConfigurationTemplates](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeLaunchConfigurationTemplates.html): Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs
- [DescribeRecoveryInstances](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoveryInstances.html): Lists all Recovery Instances or multiple Recovery Instances by ID.
- [DescribeRecoverySnapshots](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoverySnapshots.html): Lists all Recovery Snapshots for a single Source Server.
- [DescribeReplicationConfigurationTemplates](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeReplicationConfigurationTemplates.html): Lists all ReplicationConfigurationTemplates, filtered by Source Server IDs.
- [DescribeSourceNetworks](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceNetworks.html): Lists all Source Networks or multiple Source Networks filtered by ID.
- [DescribeSourceServers](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceServers.html): Lists all Source Servers or multiple Source Servers filtered by ID.
- [DisconnectRecoveryInstance](https://docs.aws.amazon.com/drs/latest/APIReference/API_DisconnectRecoveryInstance.html): Disconnect a Recovery Instance from Elastic Disaster Recovery.
- [DisconnectSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_DisconnectSourceServer.html): Disconnects a specific Source Server from Elastic Disaster Recovery.
- [ExportSourceNetworkCfnTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_ExportSourceNetworkCfnTemplate.html): Export the Source Network CloudFormation template to an S3 bucket.
- [GetFailbackReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetFailbackReplicationConfiguration.html): Lists all Failback ReplicationConfigurations, filtered by Recovery Instance ID.
- [GetLaunchConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetLaunchConfiguration.html): Gets a LaunchConfiguration, filtered by Source Server IDs.
- [GetReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_GetReplicationConfiguration.html): Gets a ReplicationConfiguration, filtered by Source Server ID.
- [InitializeService](https://docs.aws.amazon.com/drs/latest/APIReference/API_InitializeService.html): Initialize Elastic Disaster Recovery.
- [ListExtensibleSourceServers](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListExtensibleSourceServers.html): Returns a list of source servers on a staging account that are extensible, which means that: a.
- [ListLaunchActions](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListLaunchActions.html): Lists resource launch actions.
- [ListStagingAccounts](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListStagingAccounts.html): Returns an array of staging accounts for existing extended source servers.
- [ListTagsForResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_ListTagsForResource.html): List all tags for your Elastic Disaster Recovery resources.
- [PutLaunchAction](https://docs.aws.amazon.com/drs/latest/APIReference/API_PutLaunchAction.html): Puts a resource launch action.
- [RetryDataReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_RetryDataReplication.html): WARNING: RetryDataReplication is deprecated.
- [ReverseReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_ReverseReplication.html): Start replication to origin / target region - applies only to protected instances that originated in EC2.
- [StartFailbackLaunch](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartFailbackLaunch.html): Initiates a Job for launching the machine that is being failed back to from the specified Recovery Instance.
- [StartRecovery](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecovery.html): Launches Recovery Instances for the specified Source Servers.
- [StartReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartReplication.html): Starts replication for a stopped Source Server.
- [StartSourceNetworkRecovery](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartSourceNetworkRecovery.html): Deploy VPC for the specified Source Network and modify launch templates to use this network.
- [StartSourceNetworkReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartSourceNetworkReplication.html): Starts replication for a Source Network.
- [StopFailback](https://docs.aws.amazon.com/drs/latest/APIReference/API_StopFailback.html): Stops the failback process for a specified Recovery Instance.
- [StopReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StopReplication.html): Stops replication for a Source Server.
- [StopSourceNetworkReplication](https://docs.aws.amazon.com/drs/latest/APIReference/API_StopSourceNetworkReplication.html): Stops replication for a Source Network.
- [TagResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_TagResource.html): Adds or overwrites only the specified tags for the specified Elastic Disaster Recovery resource or resources.
- [TerminateRecoveryInstances](https://docs.aws.amazon.com/drs/latest/APIReference/API_TerminateRecoveryInstances.html): Initiates a Job for terminating the EC2 resources associated with the specified Recovery Instances, and then will delete the Recovery Instances from the Elastic Disaster Recovery service.
- [UntagResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_UntagResource.html): Deletes the specified set of tags from the specified set of Elastic Disaster Recovery resources.
- [UpdateFailbackReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateFailbackReplicationConfiguration.html): Allows you to update the failback replication configuration of a Recovery Instance by ID.
- [UpdateLaunchConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateLaunchConfiguration.html): Updates a LaunchConfiguration by Source Server ID.
- [UpdateLaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateLaunchConfigurationTemplate.html): Updates an existing Launch Configuration Template by ID.
- [UpdateReplicationConfiguration](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateReplicationConfiguration.html): Allows you to update a ReplicationConfiguration by Source Server ID.
- [UpdateReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateReplicationConfigurationTemplate.html): Updates a ReplicationConfigurationTemplate by ID.


## [Data Types](https://docs.aws.amazon.com/drs/latest/APIReference/API_Types.html)

- [Account](https://docs.aws.amazon.com/drs/latest/APIReference/API_Account.html): AWS account.
- [ConversionProperties](https://docs.aws.amazon.com/drs/latest/APIReference/API_ConversionProperties.html): Properties of a conversion job
- [CPU](https://docs.aws.amazon.com/drs/latest/APIReference/API_CPU.html): Information about a server's CPU.
- [DataReplicationError](https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationError.html): Error in data replication.
- [DataReplicationInfo](https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInfo.html): Information about Data Replication
- [DataReplicationInfoReplicatedDisk](https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInfoReplicatedDisk.html): A disk that should be replicated.
- [DataReplicationInitiation](https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInitiation.html): Data replication initiation.
- [DataReplicationInitiationStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInitiationStep.html): Data replication initiation step.
- [DescribeJobsRequestFilters](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeJobsRequestFilters.html): A set of filters by which to return Jobs.
- [DescribeRecoveryInstancesRequestFilters](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoveryInstancesRequestFilters.html): A set of filters by which to return Recovery Instances.
- [DescribeRecoverySnapshotsRequestFilters](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeRecoverySnapshotsRequestFilters.html): A set of filters by which to return Recovery Snapshots.
- [DescribeSourceNetworksRequestFilters](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceNetworksRequestFilters.html): A set of filters by which to return Source Networks.
- [DescribeSourceServersRequestFilters](https://docs.aws.amazon.com/drs/latest/APIReference/API_DescribeSourceServersRequestFilters.html): A set of filters by which to return Source Servers.
- [Disk](https://docs.aws.amazon.com/drs/latest/APIReference/API_Disk.html): An object representing a data storage device on a server.
- [EventResourceData](https://docs.aws.amazon.com/drs/latest/APIReference/API_EventResourceData.html): Properties of resource related to a job event.
- [IdentificationHints](https://docs.aws.amazon.com/drs/latest/APIReference/API_IdentificationHints.html): Hints used to uniquely identify a machine.
- [Job](https://docs.aws.amazon.com/drs/latest/APIReference/API_Job.html): A job is an asynchronous workflow.
- [JobLog](https://docs.aws.amazon.com/drs/latest/APIReference/API_JobLog.html): A log outputted by a Job.
- [JobLogEventData](https://docs.aws.amazon.com/drs/latest/APIReference/API_JobLogEventData.html): Metadata associated with a Job log.
- [LaunchAction](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchAction.html): Launch action.
- [LaunchActionParameter](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchActionParameter.html): Launch action parameter.
- [LaunchActionRun](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchActionRun.html): Launch action run.
- [LaunchActionsRequestFilters](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchActionsRequestFilters.html): Resource launch actions filter.
- [LaunchActionsStatus](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchActionsStatus.html): Launch actions status.
- [LaunchConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchConfigurationTemplate.html): Account level Launch Configuration Template.
- [LaunchIntoInstanceProperties](https://docs.aws.amazon.com/drs/latest/APIReference/API_LaunchIntoInstanceProperties.html): Launch into existing instance.
- [Licensing](https://docs.aws.amazon.com/drs/latest/APIReference/API_Licensing.html): Configuration of a machine's license.
- [LifeCycle](https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycle.html): An object representing the Source Server Lifecycle.
- [LifeCycleLastLaunch](https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycleLastLaunch.html): An object containing information regarding the last launch of a Source Server.
- [LifeCycleLastLaunchInitiated](https://docs.aws.amazon.com/drs/latest/APIReference/API_LifeCycleLastLaunchInitiated.html): An object containing information regarding the initiation of the last launch of a Source Server.
- [NetworkInterface](https://docs.aws.amazon.com/drs/latest/APIReference/API_NetworkInterface.html): Network interface.
- [OS](https://docs.aws.amazon.com/drs/latest/APIReference/API_OS.html): Operating System.
- [ParticipatingResource](https://docs.aws.amazon.com/drs/latest/APIReference/API_ParticipatingResource.html): Represents a resource participating in an asynchronous Job.
- [ParticipatingResourceID](https://docs.aws.amazon.com/drs/latest/APIReference/API_ParticipatingResourceID.html): ID of a resource participating in an asynchronous Job.
- [ParticipatingServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_ParticipatingServer.html): Represents a server participating in an asynchronous Job.
- [PITPolicyRule](https://docs.aws.amazon.com/drs/latest/APIReference/API_PITPolicyRule.html): A rule in the Point in Time (PIT) policy representing when to take snapshots and how long to retain them for.
- [RecoveryInstance](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstance.html): A Recovery Instance is a replica of a Source Server running on EC2.
- [RecoveryInstanceDataReplicationError](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationError.html): Error in data replication.
- [RecoveryInstanceDataReplicationInfo](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInfo.html): Information about Data Replication
- [RecoveryInstanceDataReplicationInfoReplicatedDisk](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInfoReplicatedDisk.html): A disk that should be replicated.
- [RecoveryInstanceDataReplicationInitiation](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInitiation.html): Data replication initiation.
- [RecoveryInstanceDataReplicationInitiationStep](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDataReplicationInitiationStep.html): Data replication initiation step.
- [RecoveryInstanceDisk](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceDisk.html): An object representing a block storage device on the Recovery Instance.
- [RecoveryInstanceFailback](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceFailback.html): An object representing failback related information of the Recovery Instance.
- [RecoveryInstanceProperties](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryInstanceProperties.html): Properties of the Recovery Instance machine.
- [RecoveryLifeCycle](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryLifeCycle.html): An object representing the Source Network recovery Lifecycle.
- [RecoverySnapshot](https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoverySnapshot.html): A snapshot of a Source Server used during recovery.
- [ReplicationConfigurationReplicatedDisk](https://docs.aws.amazon.com/drs/latest/APIReference/API_ReplicationConfigurationReplicatedDisk.html): The configuration of a disk of the Source Server to be replicated.
- [ReplicationConfigurationTemplate](https://docs.aws.amazon.com/drs/latest/APIReference/API_ReplicationConfigurationTemplate.html)
- [SourceCloudProperties](https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceCloudProperties.html): Properties of the cloud environment where this Source Server originated from.
- [SourceNetwork](https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceNetwork.html): The ARN of the Source Network.
- [SourceNetworkData](https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceNetworkData.html): Properties of Source Network related to a job event.
- [SourceProperties](https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceProperties.html): Properties of the Source Server machine.
- [SourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_SourceServer.html)
- [StagingArea](https://docs.aws.amazon.com/drs/latest/APIReference/API_StagingArea.html): Staging information related to source server.
- [StagingSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_StagingSourceServer.html): Source server in staging account that extended source server connected to.
- [StartRecoveryRequestSourceServer](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartRecoveryRequestSourceServer.html): An object representing the Source Server to recover.
- [StartSourceNetworkRecoveryRequestNetworkEntry](https://docs.aws.amazon.com/drs/latest/APIReference/API_StartSourceNetworkRecoveryRequestNetworkEntry.html): An object representing the Source Network to recover.
- [ValidationExceptionField](https://docs.aws.amazon.com/drs/latest/APIReference/API_ValidationExceptionField.html): Validate exception field.
