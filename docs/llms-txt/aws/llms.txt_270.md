# Source: https://docs.aws.amazon.com/datasync/latest/userguide/llms.txt

# AWS DataSync User Guide

> AWS DataSync is a data transfer service that simplifies, automates, and accelerates moving and replicating data between self-managed storage systems and AWS storage services over the internet or AWS Direct Connect. As a fully managed service, DataSync removes the need to modify applications, develop scripts, or manage infrastructure.

- [What is AWS DataSync?](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [How it works](https://docs.aws.amazon.com/datasync/latest/userguide/how-datasync-transfer-works.html)
- [Quotas](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-limits.html)
- [Document history](https://docs.aws.amazon.com/datasync/latest/userguide/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/datasync/latest/userguide/glossary.html)

## [Getting started](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html)

- [Do I need an agent?](https://docs.aws.amazon.com/datasync/latest/userguide/do-i-need-datasync-agent.html): Determine whether you need to deploy a AWS DataSync agent in your storage environment for your data transfer.
- [Agent requirements](https://docs.aws.amazon.com/datasync/latest/userguide/agent-requirements.html): Learn about hypervisor, virtual machine (VM), and Amazon EC2 instance requirements for AWS DataSync agents.
- [Deploying your agent](https://docs.aws.amazon.com/datasync/latest/userguide/deploy-agents.html): Learn how to deploy an AWS DataSync agent on a VMware ESXi, Linux Kernel-based Virtual Machine (KVM), or Microsoft Hyper-V hypervisor.
- [Choosing a service endpoint for your agent](https://docs.aws.amazon.com/datasync/latest/userguide/choose-service-endpoint.html): Learn how to choose a service endpoint that your AWS DataSync agent uses to communicate with the DataSync service.
- [Activating your agent](https://docs.aws.amazon.com/datasync/latest/userguide/activate-agent.html): Learn how to activate your AWS DataSync agent.
- [Verifying your agent's network connections](https://docs.aws.amazon.com/datasync/latest/userguide/test-agent-connections.html): Learn how to test your AWS DataSync agent's network connections to your storage system and the DataSync service.


## [Connecting your network](https://docs.aws.amazon.com/datasync/latest/userguide/networking-datasync.html)

- [Network requirements](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-network.html): Learn about network requirements for your AWS DataSync data transfer, including the ports and protocols that DataSync uses for connecting to self-managed storage, AWS storage, service endpoints, and more.
- [Network interfaces for data transfers](https://docs.aws.amazon.com/datasync/latest/userguide/required-network-interfaces.html): AWS DataSync automatically creates network interfaces to manage data transfer traffic.
- [Architecture and routing examples with Direct Connect](https://docs.aws.amazon.com/datasync/latest/userguide/direct-connect-architecture.html): See example network architectures for routing your AWS DataSync transfers through Direct Connect.
- [Configuring your agent for multiple NICs](https://docs.aws.amazon.com/datasync/latest/userguide/configure-agent-multinic.html): Configure your AWS DataSync agent for multiple network adapters (NICs), so that more than one IP address can access your agent.


## [Transferring data](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-data-datasync.html)

- [Where can I transfer my data?](https://docs.aws.amazon.com/datasync/latest/userguide/working-with-locations.html): Learn where you can transfer your data to and from with AWS DataSync.

### [Transferring to or from on-premises storage](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-on-premises-storage.html)

Learn how to configure AWS DataSync transfers to or from your on-premises or self-managed storage system.

- [Configuring transfers with an NFS file server](https://docs.aws.amazon.com/datasync/latest/userguide/create-nfs-location.html): Learn how to configure an AWS DataSync transfer to or from your Network File System (NFS) file server.
- [Configuring transfers with an SMB file server](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html): Learn how to configure an AWS DataSync transfer to or from your Server Message Block (SMB) file server.
- [Configuring transfers with an HDFS cluster](https://docs.aws.amazon.com/datasync/latest/userguide/create-hdfs-location.html): Learn how to configure an AWS DataSync transfer to or from your Hadoop Distributed File System (HDFS) cluster.
- [Configuring transfers with an object storage system](https://docs.aws.amazon.com/datasync/latest/userguide/create-object-location.html): Learn how to configure an AWS DataSync transfer to or from an on-premises or in-cloud object storage system.

### [Transferring to or from AWS storage](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-aws-storage.html)

Learn how to configure AWS DataSync transfers to or from AWS storage services.

- [Configuring transfers with Amazon S3](https://docs.aws.amazon.com/datasync/latest/userguide/create-s3-location.html): Learn how to configure an AWS DataSync transfer to or from an Amazon S3 bucket.
- [Configuring transfers with Amazon EFS](https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html): Learn how to configure an AWS DataSync transfer to or from an Amazon EFS file system, including security, network, and performance considerations.
- [Configuring transfers with FSx for Windows File Server](https://docs.aws.amazon.com/datasync/latest/userguide/create-fsx-location.html): Learn how to configure an AWS DataSync transfer to or from an Amazon FSx for Windows File Server file system.
- [Configuring transfers with FSx for Lustre](https://docs.aws.amazon.com/datasync/latest/userguide/create-lustre-location.html): Learn how to configure AWS DataSync for transferring data to or from an Amazon FSx for Lustre file system.
- [Configuring transfers with FSx for OpenZFS](https://docs.aws.amazon.com/datasync/latest/userguide/create-openzfs-location.html): Learn how to set up and configure an AWS DataSync transfer to or from an Amazon FSx for OpenZFS file system.
- [Configuring transfers with FSx for ONTAP](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html): Learn how to configure an AWS DataSync transfer to or from an Amazon FSx for NetApp ONTAP file system.

### [Transferring to or from other cloud storage](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-other-cloud-storage.html)

Learn how to transfer data between some other cloud providers and AWS storage services

- [Planning transfers to or from third-party cloud storage systems](https://docs.aws.amazon.com/datasync/latest/userguide/third-party-cloud-transfer-considerations.html): Learn about tips, best practices, and things to consider when planning a DataSync transfer to or from third-party storage systems, such as Google Cloud Storage or Microsoft Azure Blob.
- [Configuring transfers with Google Cloud Storage](https://docs.aws.amazon.com/datasync/latest/userguide/tutorial_transfer-google-cloud-storage.html): Learn how AWS DataSync can help you migrate object data from a Google Cloud Storage bucket to an Amazon S3 bucket.
- [Configuring transfers with Microsoft Azure Blob Storage](https://docs.aws.amazon.com/datasync/latest/userguide/creating-azure-blob-location.html): Learn how to transfer data between Microsoft Azure Blob Storage and AWS storage services like Amazon S3 by using AWS DataSync.
- [Configuring transfers with Microsoft Azure Files](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-azure-files.html): Learn how to transfer data between Microsoft Azure Files and AWS storage services using AWS DataSync.
- [Configuring transfers with other cloud object storage](https://docs.aws.amazon.com/datasync/latest/userguide/creating-other-cloud-object-location.html): Learn how to transfer objects between another cloud storage provider and an AWS storage service by using AWS DataSync.

### [Creating a task for transferring data](https://docs.aws.amazon.com/datasync/latest/userguide/create-task-how-to.html)

Learn how to create a AWS DataSync task with your source location, destination location, and preferences for how you want your data transferred.

- [Choosing a task mode for your transfer](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html): Learn about the differences between AWS DataSync task modes and how to configure your task to use Enhanced mode.

### [Choosing what data to transfer](https://docs.aws.amazon.com/datasync/latest/userguide/task-options.html)

Learn how to configure AWS DataSync to transfer your data the way you want, such as copying subset of files on a recurring schedule.

- [Using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html): Learn how to transfer specific files or objects with AWS DataSync by using a manifest.
- [Using filters](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html): Learn how filters can help you include or exclude specific files, objects, and directories that AWS DataSync transfers from your source location.
- [Understanding how DataSync handles metadata](https://docs.aws.amazon.com/datasync/latest/userguide/metadata-copied.html): Learn how AWS DataSync copies file and object metadata between storage systems with similar and different metadata structures.
- [Links and directories copied by DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/special-files-copied.html): Learn how AWS DataSync copies hard links, symbolic links, and directories depending on the storage systems in your transfer.
- [Configuring how to handle files, objects, and metadata](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html): Learn how to configure your AWS DataSync task to handle files, objects, and metadata during a transfer.
- [Verifying data integrity](https://docs.aws.amazon.com/datasync/latest/userguide/configure-data-verification-options.html): Learn how AWS DataSync verifies data integrity during a transfer.
- [Setting bandwidth limits](https://docs.aws.amazon.com/datasync/latest/userguide/configure-bandwidth.html): Learn how to configure network bandwidth limits for your AWS DataSync task.
- [Scheduling your task](https://docs.aws.amazon.com/datasync/latest/userguide/task-scheduling.html): Configure your AWS DataSync transfer task to run on a schedule.
- [Tagging your tasks](https://docs.aws.amazon.com/datasync/latest/userguide/tagging-tasks.html): Learn how to apply tags to your AWS DataSync tasks.
- [Starting a task to transfer data](https://docs.aws.amazon.com/datasync/latest/userguide/run-task.html): Learn how to start an AWS DataSync transfer task for copying data to or from on-premises and cloud storage.


## [Monitoring data transfers](https://docs.aws.amazon.com/datasync/latest/userguide/monitoring-overview.html)

- [Understanding data transfer performance counters](https://docs.aws.amazon.com/datasync/latest/userguide/transfer-performance-counters.html): Learn about AWS DataSync transfer counters so that you can track your data transfer's performance and progress.
- [Monitoring data transfers with CloudWatch metrics](https://docs.aws.amazon.com/datasync/latest/userguide/monitor-datasync.html): Learn how to monitor AWS DataSync activity by using Amazon CloudWatch for readable, near real-time metrics about your data transfer.

### [Monitoring data transfers with task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html)

Learn how task reports can help you monitor and audit your AWS DataSync transfers.

- [Creating your task reports](https://docs.aws.amazon.com/datasync/latest/userguide/creating-task-report.html): Learn about how create to different types of AWS DataSync task reports.
- [Viewing your task reports](https://docs.aws.amazon.com/datasync/latest/userguide/task-report-viewing.html): Learn how to viewing your AWS DataSync task reports by using Amazon S3 Select, AWS Glue, and more.
- [Monitoring data transfers with CloudWatch Logs](https://docs.aws.amazon.com/datasync/latest/userguide/configure-logging.html): Learn how to monitor your AWS DataSync transfer by using CloudWatch Logs.
- [Logging with CloudTrail](https://docs.aws.amazon.com/datasync/latest/userguide/logging-using-cloudtrail.html): Learn how to log and analyze AWS DataSync API operations data with automated AWS CloudTrail notifications.
- [Monitoring with EventBridge](https://docs.aws.amazon.com/datasync/latest/userguide/events.html): Learn how you can track changes to AWS DataSync resources, such as when your task execution completes, with Amazon EventBridge.
- [Monitoring with manual tools](https://docs.aws.amazon.com/datasync/latest/userguide/monitoring-task-manually.html): Learn how you can monitor your AWS DataSync transfers from the DataSync console or command line.


## [Managing resources](https://docs.aws.amazon.com/datasync/latest/userguide/managing-datasync.html)

- [Managing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/managing-agent.html): Learn how AWS manages your AWS DataSync agent for you, including the agent's software updates.
- [Performing maintenance on your agent](https://docs.aws.amazon.com/datasync/latest/userguide/local-console-vm.html): Learn how to check your AWS DataSync agent's system resources and perform maintenance on the agent if needed.
- [Replacing your agent](https://docs.aws.amazon.com/datasync/latest/userguide/replacing-agent.html): Learn how to replace your AWS DataSync agent.
- [Filtering DataSync resources](https://docs.aws.amazon.com/datasync/latest/userguide/query-resources.html): Learn how to use the ListLocations and ListTasks API operations to filter your AWS DataSync locations and tasks.
- [Cleaning up DataSync resources](https://docs.aws.amazon.com/datasync/latest/userguide/clean-up.html): Learn how to delete AWS DataSync resources when you're done with your data transfer.


## [Security](https://docs.aws.amazon.com/datasync/latest/userguide/security.html)

### [Data protection](https://docs.aws.amazon.com/datasync/latest/userguide/data-protection.html)

Learn how AWS DataSync protects your data during transfers.

- [Encryption in transit](https://docs.aws.amazon.com/datasync/latest/userguide/encryption-in-transit.html): Learn about encryption in transit during the three network connections that AWS DataSync requires for a data transfer.
- [Encryption at rest](https://docs.aws.amazon.com/datasync/latest/userguide/encrypting-data.html): Learn about encryption at rest with DataSync.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/datasync/latest/userguide/internetwork-traffic-privacy.html): Learn about internetwork traffic privacy and AWS DataSync.

### [Identity and access management](https://docs.aws.amazon.com/datasync/latest/userguide/iam.html)

Authenticate requests and manage permissions to access your AWS DataSync resources through the API.

- [Access management](https://docs.aws.amazon.com/datasync/latest/userguide/managing-access-overview.html): Attach permissions policies to AWS Identity and Access Management (IAM) identities, users, groups, roles, services, and resources.
- [AWS managed policies](https://docs.aws.amazon.com/datasync/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS DataSync and recent changes to those policies.
- [Customer managed policies](https://docs.aws.amazon.com/datasync/latest/userguide/using-identity-based-policies.html): Attach custom identity-based policies to IAM identities (users, groups, and roles) or service roles.

### [Using service-linked roles](https://docs.aws.amazon.com/datasync/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give DataSync access to resources in your AWS account.

- [DataSync role](https://docs.aws.amazon.com/datasync/latest/userguide/using-service-linked-roles-service-action-2.html): How to use service-linked roles to give DataSync access to resources in your AWS account.
- [Tagging resources during creation](https://docs.aws.amazon.com/datasync/latest/userguide/supported-iam-actions-tagging.html): Create IAM policies to enable users to tag AWS DataSync resources on creation.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/datasync/latest/userguide/cross-service-confused-deputy-prevention.html): When using AWS DataSync, learn how to prevent cross-service impersonation because of confused deputy issues.
- [Compliance validation](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/datasync/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS DataSync features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/datasync/latest/userguide/infrastructure-security.html): Learn about AWS DataSync infrastructure security.
- [Securing storage location credentials](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html): Learn about the different ways you can provide credentials, such as access keys and secret keys, or usernames and passwords, that DataSync uses to authenticate to your storage locations.


## [Troubleshooting](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync.html)

- [Troubleshooting agent issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-datasync-agents.html): Troubleshoot common issues with AWS DataSync agents, including connection problems, activation key retrieval failures, and offline agents.
- [Troubleshooting location issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-storage-issues.html): Learn how to troubleshoot common issues with AWS DataSync locations, including NFS permissions, mount errors, file ownership problems, and access issues with object storage services.
- [Troubleshooting task issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-tasks.html): Learn how to troubleshoot common issues with AWS DataSync tasks, including errors related to task options, network interfaces, memory allocation, and task execution statuses.
- [Troubleshooting data verification issues](https://docs.aws.amazon.com/datasync/latest/userguide/troubleshooting-task-verification.html): Learn how to troubleshoot common data verification issues with AWS DataSync, including file content mismatches, SMB metadata discrepancies, and source file deletions during transfers.
- [Troubleshooting S3 storage costs with DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/multipart-upload-policy.html): Learn how to analyze and troubleshoot issues related to Amazon S3 storage costs when using AWS DataSync.


## [Tutorials](https://docs.aws.amazon.com/datasync/latest/userguide/tutorials.html)

- [Transferring from on-premises to S3 across accounts](https://docs.aws.amazon.com/datasync/latest/userguide/s3-cross-account-transfer.html): Learn how to transfer data from an on-premises storage system to an Amazon S3 bucket that's associated with a different AWS account.
- [Transferring between S3 buckets across accounts](https://docs.aws.amazon.com/datasync/latest/userguide/tutorial_s3-s3-cross-account-transfer.html): Learn how to transfer data between Amazon S3 buckets that are associated with different AWS accounts and Regions.


## [Performing a large migration](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migration.html)

### [Stage 1: Planning your migration](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migraton-stage-1.html)

Learn how to plan a large data migration using AWS DataSync, including gathering requirements, running a proof of concept, and estimating timelines.

- [Gathering requirements](https://docs.aws.amazon.com/datasync/latest/userguide/gathering-migration-requirements.html): Learn how to gather requirements for migrating large datasets to AWS using DataSync.
- [Running a proof of concept](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migration-poc.html): Learn how to run a proof of concept with AWS DataSync to validate your data migration planning, including network connectivity, task configuration, and performance metrics.
- [Estimating migration timelines](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migration-timelines.html): Learn how to estimate data transfer and cutover timelines for large-scale migrations using AWS DataSync, considering factors like network bandwidth, storage utilization, and performance metrics.

### [Stage 2: Implementing your migration](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migraton-stage-2.html)

Learn how to implement a large data migration using AWS DataSync, including configuring tasks, running transfers, and monitoring progress.

- [Accelerating your migration with partitioning](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migration-data-partitioning.html): Learn how to accelerate large data migrations using AWS DataSync by partitioning your dataset across multiple transfer tasks.
- [Running your DataSync tasks](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migration-running-tasks.html): Learn how to run AWS DataSync transfer tasks, including initial and incremental data transfers, and perform a cutover to your destination location during migration waves.
- [Monitoring your transfers](https://docs.aws.amazon.com/datasync/latest/userguide/datasync-large-migration-monitoring.html): Learn how to monitor AWS DataSync transfers using Amazon CloudWatch metrics, task reports, and CloudWatch logs to validate and debug your data migrations effectively.


## [DataSync API](https://docs.aws.amazon.com/datasync/latest/userguide/API_Reference.html)

### [Actions](https://docs.aws.amazon.com/datasync/latest/userguide/API_Operations.html)

The following actions are supported:

- [CancelTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_CancelTaskExecution.html): Stops an AWS DataSync task execution that's in progress.
- [CreateAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateAgent.html): Activates an AWS DataSync agent that you deploy in your storage environment.
- [CreateLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationAzureBlob.html): Creates a transfer location for a Microsoft Azure Blob Storage container.
- [CreateLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationEfs.html): Creates a transfer location for an Amazon EFS file system.
- [CreateLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxLustre.html): Creates a transfer location for an Amazon FSx for Lustre file system.
- [CreateLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html): Creates a transfer location for an Amazon FSx for NetApp ONTAP file system.
- [CreateLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOpenZfs.html): Creates a transfer location for an Amazon FSx for OpenZFS file system.
- [CreateLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxWindows.html): Creates a transfer location for an Amazon FSx for Windows File Server file system.
- [CreateLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationHdfs.html): Creates a transfer location for a Hadoop Distributed File System (HDFS).
- [CreateLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationNfs.html): Creates a transfer location for a Network File System (NFS) file server.
- [CreateLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationObjectStorage.html): Creates a transfer location for an object storage system.
- [CreateLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationS3.html): Creates a transfer location for an Amazon S3 bucket.
- [CreateLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationSmb.html): Creates a transfer location for a Server Message Block (SMB) file server.
- [CreateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateTask.html): Configures a task, which defines where and how AWS DataSync transfers your data.
- [DeleteAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_DeleteAgent.html): Removes an AWS DataSync agent resource from your AWS account.
- [DeleteLocation](https://docs.aws.amazon.com/datasync/latest/userguide/API_DeleteLocation.html): Deletes a transfer location resource from AWS DataSync.
- [DeleteTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_DeleteTask.html): Deletes a transfer task resource from AWS DataSync.
- [DescribeAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeAgent.html): Returns information about an AWS DataSync agent, such as its name, service endpoint type, and status.
- [DescribeLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationAzureBlob.html): Provides details about how an AWS DataSync transfer location for Microsoft Azure Blob Storage is configured.
- [DescribeLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationEfs.html): Provides details about how an AWS DataSync transfer location for an Amazon EFS file system is configured.
- [DescribeLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxLustre.html): Provides details about how an AWS DataSync transfer location for an Amazon FSx for Lustre file system is configured.
- [DescribeLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxOntap.html): Provides details about how an AWS DataSync transfer location for an Amazon FSx for NetApp ONTAP file system is configured.
- [DescribeLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxOpenZfs.html): Provides details about how an AWS DataSync transfer location for an Amazon FSx for OpenZFS file system is configured.
- [DescribeLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationFsxWindows.html): Provides details about how an AWS DataSync transfer location for an Amazon FSx for Windows File Server file system is configured.
- [DescribeLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationHdfs.html): Provides details about how an AWS DataSync transfer location for a Hadoop Distributed File System (HDFS) is configured.
- [DescribeLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationNfs.html): Provides details about how an AWS DataSync transfer location for a Network File System (NFS) file server is configured.
- [DescribeLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationObjectStorage.html): Provides details about how an AWS DataSync transfer location for an object storage system is configured.
- [DescribeLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationS3.html): Provides details about how an AWS DataSync transfer location for an S3 bucket is configured.
- [DescribeLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeLocationSmb.html): Provides details about how an AWS DataSync transfer location for a Server Message Block (SMB) file server is configured.
- [DescribeTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTask.html): Provides information about a task, which defines where and how AWS DataSync transfers your data.
- [DescribeTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_DescribeTaskExecution.html): Provides information about an execution of your AWS DataSync task.
- [ListAgents](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListAgents.html): Returns a list of AWS DataSync agents that belong to an AWS account in the AWS Region specified in the request.
- [ListLocations](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListLocations.html): Returns a list of source and destination locations.
- [ListTagsForResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTagsForResource.html): Returns all the tags associated with an AWS resource.
- [ListTaskExecutions](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTaskExecutions.html): Returns a list of executions for an AWS DataSync transfer task.
- [ListTasks](https://docs.aws.amazon.com/datasync/latest/userguide/API_ListTasks.html): Returns a list of the AWS DataSync tasks you created.
- [StartTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_StartTaskExecution.html): Starts an AWS DataSync transfer task.
- [TagResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_TagResource.html): Applies a tag to an AWS resource.
- [UntagResource](https://docs.aws.amazon.com/datasync/latest/userguide/API_UntagResource.html): Removes tags from an AWS resource.
- [UpdateAgent](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateAgent.html): Updates the name of an AWS DataSync agent.
- [UpdateLocationAzureBlob](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationAzureBlob.html): Modifies the following configurations of the Microsoft Azure Blob Storage transfer location that you're using with AWS DataSync.
- [UpdateLocationEfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationEfs.html): Modifies the following configuration parameters of the Amazon EFS transfer location that you're using with AWS DataSync.
- [UpdateLocationFsxLustre](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxLustre.html): Modifies the following configuration parameters of the Amazon FSx for Lustre transfer location that you're using with AWS DataSync.
- [UpdateLocationFsxOntap](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxOntap.html): Modifies the following configuration parameters of the Amazon FSx for NetApp ONTAP transfer location that you're using with AWS DataSync.
- [UpdateLocationFsxOpenZfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxOpenZfs.html): Modifies the following configuration parameters of the Amazon FSx for OpenZFS transfer location that you're using with AWS DataSync.
- [UpdateLocationFsxWindows](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationFsxWindows.html): Modifies the following configuration parameters of the Amazon FSx for Windows File Server transfer location that you're using with AWS DataSync.
- [UpdateLocationHdfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationHdfs.html): Modifies the following configuration parameters of the Hadoop Distributed File System (HDFS) transfer location that you're using with AWS DataSync.
- [UpdateLocationNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationNfs.html): Modifies the following configuration parameters of the Network File System (NFS) transfer location that you're using with AWS DataSync.
- [UpdateLocationObjectStorage](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationObjectStorage.html): Modifies the following configuration parameters of the object storage transfer location that you're using with AWS DataSync.
- [UpdateLocationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationS3.html): Modifies the following configuration parameters of the Amazon S3 transfer location that you're using with AWS DataSync.
- [UpdateLocationSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateLocationSmb.html): Modifies the following configuration parameters of the Server Message Block (SMB) transfer location that you're using with AWS DataSync.
- [UpdateTask](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTask.html): Updates the configuration of a task, which defines where and how AWS DataSync transfers your data.
- [UpdateTaskExecution](https://docs.aws.amazon.com/datasync/latest/userguide/API_UpdateTaskExecution.html): Updates the configuration of a running AWS DataSync task execution.

### [Data Types](https://docs.aws.amazon.com/datasync/latest/userguide/API_Types.html)

The following data types are supported:

- [AgentListEntry](https://docs.aws.amazon.com/datasync/latest/userguide/API_AgentListEntry.html): Represents a single entry in a list (or array) of AWS DataSync agents when you call the ListAgents operation.
- [AzureBlobSasConfiguration](https://docs.aws.amazon.com/datasync/latest/userguide/API_AzureBlobSasConfiguration.html): The shared access signature (SAS) configuration that allows AWS DataSync to access your Microsoft Azure Blob Storage.
- [CmkSecretConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_CmkSecretConfig.html): Specifies configuration information for a DataSync-managed secret, such as an authentication token, secret key, password, or Kerberos keytab that DataSync uses to access a specific storage location, with a customer-managed AWS KMS key.
- [CustomSecretConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_CustomSecretConfig.html): Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab).
- [Ec2Config](https://docs.aws.amazon.com/datasync/latest/userguide/API_Ec2Config.html): The subnet and security groups that AWS DataSync uses to connect to one of your Amazon EFS file system's mount targets.
- [FilterRule](https://docs.aws.amazon.com/datasync/latest/userguide/API_FilterRule.html): Specifies which files, folders, and objects to include or exclude when transferring files from source to destination.
- [FsxProtocol](https://docs.aws.amazon.com/datasync/latest/userguide/API_FsxProtocol.html): Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.
- [FsxProtocolNfs](https://docs.aws.amazon.com/datasync/latest/userguide/API_FsxProtocolNfs.html): Specifies the Network File System (NFS) protocol configuration that DataSync uses to access your FSx for OpenZFS file system or FSx for ONTAP file system's storage virtual machine (SVM).
- [FsxProtocolSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_FsxProtocolSmb.html): Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access your Amazon FSx for NetApp ONTAP file system's storage virtual machine (SVM).
- [FsxUpdateProtocol](https://docs.aws.amazon.com/datasync/latest/userguide/API_FsxUpdateProtocol.html): Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.
- [FsxUpdateProtocolSmb](https://docs.aws.amazon.com/datasync/latest/userguide/API_FsxUpdateProtocolSmb.html): Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access your Amazon FSx for NetApp ONTAP file system's storage virtual machine (SVM).
- [HdfsNameNode](https://docs.aws.amazon.com/datasync/latest/userguide/API_HdfsNameNode.html): The NameNode of the Hadoop Distributed File System (HDFS).
- [LocationFilter](https://docs.aws.amazon.com/datasync/latest/userguide/API_LocationFilter.html): Narrow down the list of resources returned by ListLocations.
- [LocationListEntry](https://docs.aws.amazon.com/datasync/latest/userguide/API_LocationListEntry.html): Represents a single entry in a list of locations.
- [ManagedSecretConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_ManagedSecretConfig.html): Specifies configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location.
- [ManifestConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_ManifestConfig.html): Configures a manifest, which is a list of files or objects that you want AWS DataSync to transfer.
- [NfsMountOptions](https://docs.aws.amazon.com/datasync/latest/userguide/API_NfsMountOptions.html): Specifies how DataSync can access a location using the NFS protocol.
- [OnPremConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_OnPremConfig.html): The AWS DataSync agents that can connect to your Network File System (NFS) file server.
- [Options](https://docs.aws.amazon.com/datasync/latest/userguide/API_Options.html): Indicates how your transfer task is configured.
- [Platform](https://docs.aws.amazon.com/datasync/latest/userguide/API_Platform.html): The platform-related details about the AWS DataSync agent, such as the version number.
- [PrivateLinkConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_PrivateLinkConfig.html): Specifies how your AWS DataSync agent connects to AWS using a virtual private cloud (VPC) service endpoint.
- [QopConfiguration](https://docs.aws.amazon.com/datasync/latest/userguide/API_QopConfiguration.html): The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS) cluster.
- [ReportDestination](https://docs.aws.amazon.com/datasync/latest/userguide/API_ReportDestination.html): Specifies where DataSync uploads your task report.
- [ReportDestinationS3](https://docs.aws.amazon.com/datasync/latest/userguide/API_ReportDestinationS3.html): Specifies the Amazon S3 bucket where DataSync uploads your task report.
- [ReportOverride](https://docs.aws.amazon.com/datasync/latest/userguide/API_ReportOverride.html): Specifies the level of detail for a particular aspect of your DataSync task report.
- [ReportOverrides](https://docs.aws.amazon.com/datasync/latest/userguide/API_ReportOverrides.html): The level of detail included in each aspect of your DataSync task report.
- [ReportResult](https://docs.aws.amazon.com/datasync/latest/userguide/API_ReportResult.html): Indicates whether DataSync created a complete task report for your transfer.
- [S3Config](https://docs.aws.amazon.com/datasync/latest/userguide/API_S3Config.html): Specifies the Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that DataSync uses to access your S3 bucket.
- [S3ManifestConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_S3ManifestConfig.html): Specifies the S3 bucket where you're hosting the manifest that you want AWS DataSync to use.
- [SmbMountOptions](https://docs.aws.amazon.com/datasync/latest/userguide/API_SmbMountOptions.html): Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.
- [SourceManifestConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_SourceManifestConfig.html): Specifies the manifest that you want AWS DataSync to use and where it's hosted.
- [TagListEntry](https://docs.aws.amazon.com/datasync/latest/userguide/API_TagListEntry.html): A key-value pair representing a single tag that's been applied to an AWS resource.
- [TaskExecutionFilesFailedDetail](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionFilesFailedDetail.html): The number of files or objects that DataSync fails to prepare, transfer, verify, and delete during your task execution.
- [TaskExecutionFilesListedDetail](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionFilesListedDetail.html): The number of files or objects that DataSync finds at your locations.
- [TaskExecutionFoldersFailedDetail](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionFoldersFailedDetail.html): The number of directories that DataSync fails to list, prepare, transfer, verify, and delete during your task execution.
- [TaskExecutionFoldersListedDetail](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionFoldersListedDetail.html): The number of directories that DataSync finds at your locations.
- [TaskExecutionListEntry](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionListEntry.html): Represents a single entry in a list of AWS DataSync task executions that's returned with the ListTaskExecutions operation.
- [TaskExecutionResultDetail](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskExecutionResultDetail.html): Provides detailed information about the result of your AWS DataSync task execution.
- [TaskFilter](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskFilter.html): You can use API filters to narrow down the list of resources returned by ListTasks.
- [TaskListEntry](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskListEntry.html): Represents a single entry in a list of tasks.
- [TaskReportConfig](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskReportConfig.html): Specifies how you want to configure a task report, which provides detailed information about for your AWS DataSync transfer.
- [TaskSchedule](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskSchedule.html): Configures your AWS DataSync task to run on a schedule (at a minimum interval of 1 hour).
- [TaskScheduleDetails](https://docs.aws.amazon.com/datasync/latest/userguide/API_TaskScheduleDetails.html): Provides information about your AWS DataSync task schedule.
- [Common Errors](https://docs.aws.amazon.com/datasync/latest/userguide/CommonErrors.html): This section lists the errors common to the API actions of all AWS services.
- [Common Parameters](https://docs.aws.amazon.com/datasync/latest/userguide/CommonParameters.html): The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string.
