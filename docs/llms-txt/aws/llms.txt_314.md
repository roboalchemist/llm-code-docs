# Source: https://docs.aws.amazon.com/drs/latest/userguide/llms.txt

# AWS Elastic Disaster Recovery User Guide

- [What is Elastic Disaster Recovery?](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)
- [Recovery job history](https://docs.aws.amazon.com/drs/latest/userguide/recovery-job.html)
- [Using multiple staging accounts with AWS DRS](https://docs.aws.amazon.com/drs/latest/userguide/multi-account.html)
- [Working with AWS DRS and AWS Outposts](https://docs.aws.amazon.com/drs/latest/userguide/outposts.html)
- [Troubleshooting](https://docs.aws.amazon.com/drs/latest/userguide/troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/drs/latest/userguide/doc-history.html)

## [Getting started](https://docs.aws.amazon.com/drs/latest/userguide/getting-started.html)

- [Initialization and permissions](https://docs.aws.amazon.com/drs/latest/userguide/getting-started-initializing.html): In order to use AWS Elastic Disaster Recovery, the service must first be initialized for any AWS Region in which you plan to use Elastic Disaster Recovery.
- [Accessing the console](https://docs.aws.amazon.com/drs/latest/userguide/accessing-console.html): You can access AWS Elastic Disaster Recovery directly through the AWS Console or through the following links.
- [Supported AWS Regions](https://docs.aws.amazon.com/drs/latest/userguide/supported-regions.html): The following AWS Regions are supported by AWS Elastic Disaster Recovery.
- [Using the console](https://docs.aws.amazon.com/drs/latest/userguide/drs-console.html): AWS Elastic Disaster Recovery is AWS Region-specific.
- [Best practices](https://docs.aws.amazon.com/drs/latest/userguide/best_practices_drs.html): Best practices for planning, implementing, and maintaining disaster recovery for on-premises applications using AWS Elastic Disaster Recovery.
- [Quick start guide](https://docs.aws.amazon.com/drs/latest/userguide/quick-start-guide-gs.html): First time Elastic Disaster Recovery quick start instructions for adding source servers, configuring launch settings, launching recovery instance, and performing a failback.


## [Replication network requirements](https://docs.aws.amazon.com/drs/latest/userguide/preparing-environments.html)

- [Network diagrams](https://docs.aws.amazon.com/drs/latest/userguide/Network-diagrams.html): The reference architecture network diagrams for AWS Elastic Disaster Recovery show examples of network architectures for on-premises, failback, and other examples.
- [Network setting preparations](https://docs.aws.amazon.com/drs/latest/userguide/Network-Settings-Preparations.html): Before setting up AWS Elastic Disaster Recovery (AWS DRS), you should create a subnet which will be used by Elastic Disaster Recovery as a staging area for data replicated from your source servers to AWS.
- [Network requirements](https://docs.aws.amazon.com/drs/latest/userguide/Network-Requirements.html): To prepare your network for running Elastic Disaster Recovery, set the following connectivity settings so that you can communicate over TCP port 443 and TCP port 1500.


## [AWS DRS settings](https://docs.aws.amazon.com/drs/latest/userguide/settings.html)

### [Replication settings](https://docs.aws.amazon.com/drs/latest/userguide/replication-settings.html)

Replication Settings govern how data is replicated from Source Servers and stored within AWS.

- [Default replication](https://docs.aws.amazon.com/drs/latest/userguide/default-replication-settings.html): Default replication settings are created during the DRS Service Initialization within a Region.

### [Individual replication settings](https://docs.aws.amazon.com/drs/latest/userguide/individual-replication-settings.html)

Elastic Disaster Recovery consolidates the replication of source servers on the same Replication Server from the individual Source Server Replication Settings.

- [Amazon EBS volumes](https://docs.aws.amazon.com/drs/latest/userguide/volumes-drs.html): Set the default Amazon EBS volume type used by the replication servers and whether to use Amazon EBS encryption.
- [Security groups](https://docs.aws.amazon.com/drs/latest/userguide/drs-security-group.html): Security groups act as a virtual firewall, controlling the inbound and outbound traffic of the staging area.
- [Data routing and throttling](https://docs.aws.amazon.com/drs/latest/userguide/data-routing.html): Elastic Disaster Recovery lets you control how data is routed from your source servers to the replication servers through Data routing and throttling settings.
- [Point in time (PIT) policy](https://docs.aws.amazon.com/drs/latest/userguide/point-in-time.html): AWS Elastic Disaster Recovery allows you to select the number of days for which point in time snapshots are retained through the Point in time (PIT) policy field.
- [Tags](https://docs.aws.amazon.com/drs/latest/userguide/replication-tags.html): Add custom tags to resources created by Elastic Disaster Recovery in your account.
- [MAP program tagging](https://docs.aws.amazon.com/drs/latest/userguide/map-program-tagging.html): The AWS Migration Acceleration Program (MAP) provides tools that are designed to reduce costs, boost productivity, improve operational resilience and increase business agility.

### [Launch settings](https://docs.aws.amazon.com/drs/latest/userguide/launch-settings-overview.html)

Launch settings are a set of instructions (general launch settings and the EC2 launch template) that determine how drill or recovery instances are launched in AWS.

### [Default AWS DRS launch settings](https://docs.aws.amazon.com/drs/latest/userguide/default-drs-launch-settings.html)

Elastic Disaster Recovery allows you to configure and change default launch settings.

- [Editing the default AWS DRS launch settings](https://docs.aws.amazon.com/drs/latest/userguide/editing-launch-settings.html): The default launch settings are applied to every newly launched source server in AWS DRS.
- [Launch into source instance](https://docs.aws.amazon.com/drs/latest/userguide/default-drs-launch-into-source-instance.html): The launch into source instance setting is only valid when the replication and recovery are done in AWS, between two AWS Regions or Availability Zones.

### [Default Amazon Elastic Compute Cloud (Amazon EC2) launch template](https://docs.aws.amazon.com/drs/latest/userguide/default-ec2-launch-template.html)

The default Amazon EC2 launch template sets the default values that are copied to EC2 templates created for newly added source servers.

- [Editing the default EC2 launch template](https://docs.aws.amazon.com/drs/latest/userguide/edit-default-ec2-launch-template.html): AWS DRS Amazon EC2 launch settings are divided into basic and advanced settings.

### [Post-launch actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-overview.html)

After finishing the initialization process, configure your default post-launch actions settings to control which post-launch actions run when launching new instances.

- [Install the required IAM roles if needed](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-roles.html): To operate post-launch actions and allow SSM documents to run on launched instances, install certain IAM roles into an AWS account when AWS DRS is initialized.
- [Activating post-launch actions default settings](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-activation-default.html): Activate post-launch actions in the default settings, to make it active by default for newly added source servers, and to allow to update the default list of actions.
- [Adding custom actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-adding-custom-default.html): AWS Elastic Disaster Recovery (AWS DRS) allows you to run any SSM document that you like â public SSM documents or ones you created and uploaded to your account.
- [Activating, deactivating and editing predefined or custom actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-editing-default.html): You can activate, deactivate and edit predefined or custom actions available in the default post-launch actions settings. to newly added servers.
- [Deleting custom actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-deleting-default.html): Deleting a custom action in the default settings removes it from the default settings and means the action is no longer added to newly added servers.
- [Predefined post-launch actions](https://docs.aws.amazon.com/drs/latest/userguide/predefined-post-launch-actions-default.html): AWS Elastic Disaster Recovery allows you to run various predefined post-launch actions on your EC2 launched instance to validate or improve your launch flexibility.


## [Source servers](https://docs.aws.amazon.com/drs/latest/userguide/source-servers.html)

### [Adding source servers to AWS DRS](https://docs.aws.amazon.com/drs/latest/userguide/adding-servers.html)

Add source servers to AWS Elastic Disaster Recovery by installing the AWS Replication Agent (also referred to as "the Agent") on them.

- [Installation requirements](https://docs.aws.amazon.com/drs/latest/userguide/installation-requirements.html): Before installing the AWS Replication Agent on your source servers, ensure that they meet the following general and source server requirements for Linux or Windows.
- [Supported Windows operating systems](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Windows.html): AWS Elastic Disaster Recovery supports replication of physical, virtual or cloud-based source servers to the AWS Cloud for a variety of Windows versions.
- [Supported Linux operating systems](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html): AWS Elastic Disaster Recovery supports replication of physical, virtual or cloud-based source servers to the AWS Cloud for a variety of Linux operating systems.

### [Installing the AWS Replication Agent](https://docs.aws.amazon.com/drs/latest/userguide/agent-installation.html)

You must install the AWS Replication Agent on each source server that you want to add to AWS Elastic Disaster Recovery.

- [Generating the required AWS credentials](https://docs.aws.amazon.com/drs/latest/userguide/credentials.html): In order to install the AWS account Replication Agent, you must first generate the required AWS credentials.
- [Installing the AWS Replication Agent in AWS](https://docs.aws.amazon.com/drs/latest/userguide/agent-installations-in-aws.html): When installing an AWS account Replication Agent on an Amazon EC2 instance (source and recovery servers are both in AWS Regions), you don't need to generate credentials.

### [Installation instructions](https://docs.aws.amazon.com/drs/latest/userguide/agent-installation-instructions.html)

After generating AWS credentials, install the AWS Replication Agent on your source servers.

- [Linux](https://docs.aws.amazon.com/drs/latest/userguide/linux-agent.html): To install the agent on a Linux source server, you should ensure that your source meets all the requirements list in the supported Windows operating systems and supported Linux operating systems documentation.
- [Windows](https://docs.aws.amazon.com/drs/latest/userguide/windows-agent.html): To install the AWS Replication Agent on a Windows source server, ensure that your source meets all the requirements listed in the supported Windows operating systems documentation.
- [AWS Replication Agent Installer parameters](https://docs.aws.amazon.com/drs/latest/userguide/installer-parameters.html): The AWS Replication Agent Installer supports the following command line parameters.
- [Installing the agent on a secured network](https://docs.aws.amazon.com/drs/latest/userguide/installing-agent-blocked.html): The AWS DRS AWS Replication Agent installer needs network access to AWS Elastic Disaster Recovery and S3 endpoints.
- [Uninstalling the agent](https://docs.aws.amazon.com/drs/latest/userguide/uninstalling-agent.html): Uninstalling the AWS Replication Agent from a source server stops the replication of that server.
- [Reinstalling the agent](https://docs.aws.amazon.com/drs/latest/userguide/reinstalling-agent.html): To reinstall the AWS Replication Agent, download the latest version of the agent and follow the installation instructions.
- [Supporting marketplace licenses](https://docs.aws.amazon.com/drs/latest/userguide/marketplace-license-requirements.html): Installing the AWS replication agent on an EC2 instance on AWS that has one or more active subscriptions to a marketplace license requires taking the following points into consideration:
- [Adding instances from the Amazon EC2 Console](https://docs.aws.amazon.com/drs/latest/userguide/adding-servers-from-aws-instances.html): New or existing instances can be added by selecting the appropriate action on the Amazon EC2 console, sending you to theAWS focused page allowing to install the AWS replication agent used by DRS on the selected instances.

### [Source servers page](https://docs.aws.amazon.com/drs/latest/userguide/server-list.html)

The Source servers page lists all of the source servers that have been added to AWS DRS, and you can manage and perform a variety of commands for one or more servers.

- [Interacting with the Source Servers page](https://docs.aws.amazon.com/drs/latest/userguide/interracting.html): The Source servers page shows a list of source servers.
- [Command menus](https://docs.aws.amazon.com/drs/latest/userguide/command-menus.html): You can perform a variety of actions, control data replication, and manage your drill and recovery instances for one or more source servers through the command menu buttons.
- [Filtering](https://docs.aws.amazon.com/drs/latest/userguide/list-filtering.html): You can customize the Source servers page through filtering by recovery readiness.

### [Server details](https://docs.aws.amazon.com/drs/latest/userguide/server-details.html)

To access the server details view, click the Hostname of any server on the Source servers page.

- [Recovery dashboard](https://docs.aws.amazon.com/drs/latest/userguide/recovery-dashboard.html): The Recovery dashboard tab allows you to monitor the server, its data replication status, and view events and metrics in CloudTrail.
- [Server info](https://docs.aws.amazon.com/drs/latest/userguide/source-server-info.html): The Server info tab shows a variety of general server information, hardware, and network information.
- [Tags](https://docs.aws.amazon.com/drs/latest/userguide/drs_tags-new.html): The Tags section shows any tags that have been assigned to the server.
- [Disk settings](https://docs.aws.amazon.com/drs/latest/userguide/disk-settings.html): The Disk settings tab shows a list of all of the disks on the source server and information for each disk.
- [Replication settings](https://docs.aws.amazon.com/drs/latest/userguide/source-server-replication-settings.html): The Replication settings tab allows you to edit the replication settings for an individual source server.
- [AWS DRS launch settings](https://docs.aws.amazon.com/drs/latest/userguide/launch-settings-source.html): The launch settings are a set of instructions that comprise an Amazon EC2 launch template and other settings, which determine how a recovery instance is launched for each source server on AWS.

### [Post-launch settings](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-settings-source.html)

Post-launch settings allow you to control and automate actions performed after a recovery instance has been launched for the source server in AWS.

- [Adding custom actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-adding-custom-source.html): AWS Elastic Disaster Recovery allows you to run any SSM document that you like â public SSM documents, SSM documents that you created and uploaded to your account or SSM documents that are shared with you.
- [Activating, deactivating, and editing predefined or custom actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-editing-source.html): You can activate, deactivate and edit actions available for this source server.
- [Deleting custom actions](https://docs.aws.amazon.com/drs/latest/userguide/post-launch-action-settings-deleting-source.html): Deleting a custom action for a source server removes it from that source server and means the action is no longer available to that source server.
- [Predefined post-launch actions](https://docs.aws.amazon.com/drs/latest/userguide/predefined-post-launch-actions-source.html): AWS Elastic Disaster Recovery allows you to run various predefined post-launch actions on your EC2 launched instance.


## [Source networks](https://docs.aws.amazon.com/drs/latest/userguide/source-networks.html)

### [Adding source networks](https://docs.aws.amazon.com/drs/latest/userguide/adding-source-network-page.html)

Available source networks are presented automatically on the Source networks page, along with their details: replication status, pending action, CloudFormation stack name, and more.

- [Installing the AWS Replication Agent](https://docs.aws.amazon.com/drs/latest/userguide/network-agent-installation.html): In order to use the network replication feature, you must first install the AWS Replication Agent on each source server that you want to add to AWS Elastic Disaster Recovery.
- [Creating the required role](https://docs.aws.amazon.com/drs/latest/userguide/network-required-role.html): To replicate network configurations between different accounts, you need to go to the source account and create the Network role from the Trusted accounts page.
- [Replicating your network configurations in Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/replicating-network-configurations.html): Once you install your agent and created the required role, go to the Source networks page and take the following steps:


## [Trusted accounts](https://docs.aws.amazon.com/drs/latest/userguide/trusted-accounts.html)

- [Adding a trusted account](https://docs.aws.amazon.com/drs/latest/userguide/adding-trusted-account.html): To add a trusted account in AWS DRS, create the staging role, create the network role, and create the failback and in-AWS right-sizing roles.


## [Configuring launch settings](https://docs.aws.amazon.com/drs/latest/userguide/launching-target-servers.html)

- [DRS launch settings](https://docs.aws.amazon.com/drs/latest/userguide/launch-general-settings.html): The DRS launch settings section allows you to control server-specific settings.
- [EC2 launch template](https://docs.aws.amazon.com/drs/latest/userguide/ec2-launch.html): AWS DRS uses Amazon EC2 launch templates to launch drill and recovery Amazon EC2 instances for each source server.
- [Flexible Instance Types](https://docs.aws.amazon.com/drs/latest/userguide/flexible-instance-types.html): Flexible instance type definitions can help reduce the risk of not finding enough resources to support recovery which results in an Insufficient Capacity Error (ICE).


## [Using Elastic Disaster Recovery for recovery and failback](https://docs.aws.amazon.com/drs/latest/userguide/failback.html)

- [Preparing for failover](https://docs.aws.amazon.com/drs/latest/userguide/preparing-failover.html): We recommend validating your Source Server settings and testing (drilling) frequently in preperation of a failover event.
- [Performing a failover](https://docs.aws.amazon.com/drs/latest/userguide/failback-preparing-failover.html): A failover is the redirection of traffic from a primary system to a secondary system.

### [Performing a failback](https://docs.aws.amazon.com/drs/latest/userguide/failback-performing-main.html)

Failback is the act of redirecting traffic from your recovery system to your primary system.

### [Failback to on-premises environment](https://docs.aws.amazon.com/drs/latest/userguide/failback-performing.html)

Failback replication is performed by booting the Failback Client on the source server into which you want to replicate your data from AWS.

- [Failback with DRSFA Client](https://docs.aws.amazon.com/drs/latest/userguide/failback-failover-drsfa.html): DRS allows you to perform a scalable failback for vCenter with the DRS Mass Failback Automation Client (DRSFA Client).
- [Performing a cross-Region failback](https://docs.aws.amazon.com/drs/latest/userguide/failback-failover-region-region.html): AWS DRS allows you to perform failover and failback your EC2-based applications from one AWS Region to another AWS Region.
- [Performing a cross-account failback](https://docs.aws.amazon.com/drs/latest/userguide/failback-failover-cross-account.html): AWS DRS allows you to perform failover and failback your EC2-based applications.
- [Cross Availability Zone recovery](https://docs.aws.amazon.com/drs/latest/userguide/failback-failover-cross-availability-zone-failback.html): To replicate an EC2 instance across Availability Zones, set the replication and launch settings to a different Availability Zone than the one hosting your EC2 instance.


## [Recovery Instances page](https://docs.aws.amazon.com/drs/latest/userguide/recovery-instances.html)

- [Monitoring recovery instances](https://docs.aws.amazon.com/drs/latest/userguide/monitoring-recovery-instances.html): You can fully monitor your recovery instances on the Recovery instances page.
- [Recovery instance details view](https://docs.aws.amazon.com/drs/latest/userguide/recovery-instances-details.html): The recovery instance details view provides an in-depth overview of the recovery instance, including the instance's reversed direction launch process.


## [Security](https://docs.aws.amazon.com/drs/latest/userguide/security.html)

### [Identity and access management](https://docs.aws.amazon.com/drs/latest/userguide/identity-access-management.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.

- [Authenticating with identities](https://docs.aws.amazon.com/drs/latest/userguide/security_iam_authentication.html): Authentication is how you sign in to AWS using your identity credentials.
- [Grant permission to tag resources during creation](https://docs.aws.amazon.com/drs/latest/userguide/supported-iam-actions-tagging.html): Some resource-creating AWS DRS API actions allow you to specify tags when you create the resource.

### [AWS managed policies](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol.html)

AWS managed policies cover common use cases and are available in your AWS account.

- [AWSElasticDisasterRecoveryAgentPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentPolicy.html): This policy gives the AWS Replication Agent, which is used with AWS Elastic Disaster Recovery (AWS DRS) to replicate source servers to AWS, permissions to communicate with AWS DRS to receive instructions and to send logs and metrics.
- [AWSElasticDisasterRecoveryAgentInstallationPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.html): This policy allows installing the AWS Replication Agent, which is used with AWS Elastic Disaster Recovery (AWS DRS) to recover external servers to AWS.
- [AWSElasticDisasterRecoveryConversionServerPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryConversionServerPolicy.html): This policy is attached to the AWS Elastic Disaster Recovery conversion serverâs instance role.
- [AWSElasticDisasterRecoveryFailbackPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryFailbackPolicy.html): This policy allows using the AWS Elastic Disaster Recovery Failback Client, which is used to failback recovery instances back to your original source infrastructure.
- [AWSElasticDisasterRecoveryFailbackInstallationPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryFailbackInstallationPolicy.html): You can attach this policy to your IAM identities.
- [AWSElasticDisasterRecoveryConsoleFullAccess](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryConsoleFullAccess.html): This policy provides full access to all public APIs of AWS Elastic Disaster Recovery (AWS DRS), as well as permissions to read KMS key, License Manager, Resource Groups, Elastic Load Balancing, IAM, and EC2 information.
- [AWSElasticDisasterRecoveryReadOnlyAccess](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryReadOnlyAccess.html): This policy provides permissions to all read-only public APIs of AWS Elastic Disaster Recovery (AWS DRS), as well as some read-only APIs of IAM, EC2 and SSM in order to list and view installed roles Recovery Instances, Source Servers and post-launch actions.
- [AWSElasticDisasterRecoveryReplicationServerPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryReplicationServerPolicy.html): This policy allows the AWS Elastic Disaster Recovery (AWS DRS) replication servers, which are Amazon EC2 instances launched by Elastic Disaster Recovery, to communicate with the DRS service, and to create EBS snapshots in your AWS account.
- [AWSElasticDisasterRecoveryRecoveryInstancePolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryRecoveryInstancePolicy.html): This policy allows the AWS Elastic Disaster Recovery (AWS DRS) recovery instance, which are EC2 instances launched by AWS DRS - to communicate with the AWS DRS service, and to be able to failback to their original source infrastructure.
- [AWSElasticDisasterRecoveryServiceRolePolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryServiceRolePolicy.html): This policy allows AWS Elastic Disaster Recovery to manage AWS resources on your behalf.
- [AWSElasticDisasterRecoveryStagingAccountPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryStagingAccountPolicy.html): his policy allows read-only access to AWS Elastic Disaster Recovery (AWS DRS) resources such as source servers and jobs.
- [AWSElasticDisasterRecoveryStagingAccountPolicy_v2](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryStagingAccountPolicy_v2.html): This policy is used by AWS Elastic Disaster Recovery (AWS DRS) to recover source servers into a separate target account and to allow failing back.
- [AWSElasticDisasterRecoveryEc2InstancePolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.html): This policy allows installing and using the AWS Replication Agent, which is used by AWS Elastic Disaster Recovery (AWS DRS) to recover source servers that run on EC2 (cross-Region, cross-AZ or cross-Account).
- [AWSElasticDisasterRecoveryCrossAccountReplicationPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryCrossAccountReplicationPolicy.html): This policy allows AWS Elastic Disaster Recovery (DRS) to support cross-account replication and cross-account failback.
- [AWSElasticDisasterRecoveryNetworkReplicationPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryNetworkReplicationPolicy.html): This policy allows AWS Elastic Disaster Recovery (DRS) to support network replication.
- [AWSElasticDisasterRecoveryLaunchActionsPolicy](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryLaunchActionsPolicy.html): This policy allows you to use SSM and additional services required permissions to run post-launch actions in AWS Elastic Disaster Recovery (AWS DRS).
- [AWSElasticDisasterRecoveryConsoleFullAccess_v2](https://docs.aws.amazon.com/drs/latest/userguide/security-iam-awsmanpol-AWSElasticDisasterRecoveryConsoleFullAccess_v2.html): Allows full administrative access to AWS Elastic Disaster Recovery (AWS DRS) Console.

### [Managing access using policies](https://docs.aws.amazon.com/drs/latest/userguide/security_iam_access-manage.html)

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as a user, role, or group.

### [Using identity-based policies](https://docs.aws.amazon.com/drs/latest/userguide/Using_Identity_based_policies.html)

By default, IAM users and roles don't have permission to create or modify AWS Elastic Disaster Recovery resources.

- [Customer-managed policies in AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/customer_managed_policies_drs.html): You can create your own custom IAM policies to allow permissions for AWS Elastic Disaster Recovery actions and resources.
- [Console Full Access Policy - AWSElasticDisasterRecoveryConsoleFullAccess](https://docs.aws.amazon.com/drs/latest/userguide/customer_managed_policies_drs_full_access.html): This policy provides full access to all public APIs of AWS Elastic Disaster Recovery (AWS DRS), as well as permissions to read KMS key, License Manager, Resource Groups, Elastic Load Balancing, IAM, and Amazon EC2 information.
- [Console Full Access Policy - AWSElasticDisasterRecoveryConsoleFullAccess_v2](https://docs.aws.amazon.com/drs/latest/userguide/customer_managed_policies_drs_full_access_v2.html): Allows full administrative access to AWS Elastic Disaster Recovery (AWS DRS) Console.
- [Launch Actions Policy - AWSElasticDisasterRecoveryLaunchActionsPolicy](https://docs.aws.amazon.com/drs/latest/userguide/customer_managed_policies_launch_actions.html): This policy allows you to use SSM and additional services required permissions to run post-launch actions in AWS Elastic Disaster Recovery (AWS DRS).
- [Console Read-Only Access Policy - AWSElasticDisasterRecoveryReadOnlyAccess](https://docs.aws.amazon.com/drs/latest/userguide/customer_managed_policies_drs_readonly.html): This policy provides permissions to all read-only public APIs of AWS Elastic Disaster Recovery (AWS DRS), as well as some read-only APIs of IAM, Amazon EC2 and SSM in order to list and view installed roles Recovery Instances, Source Servers and post-launch actions.
- [Using service-linked roles](https://docs.aws.amazon.com/drs/latest/userguide/using-service-linked-roles.html): How to use service-linked roles to give AWS Elastic Disaster Recovery access to resources in your AWS account.
- [Resilience](https://docs.aws.amazon.com/drs/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Elastic Disaster Recovery features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/drs/latest/userguide/infrastructure-security.html): As a managed service, AWS Elastic Disaster Recovery is protected by the AWS global network security procedures that are described in the Amazon Web Services: Overview of Security Processes whitepaper.
- [Compliance validation](https://docs.aws.amazon.com/drs/latest/userguide/compliance-validation.html): Third-party auditors assess the security and compliance of AWS Elastic Disaster Recovery as part of multiple AWS compliance programs.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/drs/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [Monitoring](https://docs.aws.amazon.com/drs/latest/userguide/logging-using-cloudtrail.html)

- [CloudWatch Metrics for DRS](https://docs.aws.amazon.com/drs/latest/userguide/monitoring-event-bridge-metrics.html): Learn about the following CloudWatch Metrics for AWS Elastic Disaster Recovery.
- [Alarm events and EventBridge](https://docs.aws.amazon.com/drs/latest/userguide/monitoring-event-bridge.html): The following are sample events for Elastic Disaster Recovery.


## [FAQ](https://docs.aws.amazon.com/drs/latest/userguide/FAQ.html)

- [Elastic Disaster Recovery Concepts](https://docs.aws.amazon.com/drs/latest/userguide/CloudEndure-Concepts.html): You can view the following answers to Elastic Disaster Recovery concepts frequently asked questions (FAQs) related to RTO, RPO, and PIT.
- [Agent related](https://docs.aws.amazon.com/drs/latest/userguide/Agent-Related-FAQ.html): You can view the following frequently asked questions (FAQs) related to the AWS Replication Agent on Elastic Disaster Recovery.
- [Replication related](https://docs.aws.amazon.com/drs/latest/userguide/Replication-Related-FAQ.html): You can view the following frequently asked questions (FAQs) related to replication on AWS Elastic Disaster Recovery.
- [AWS related](https://docs.aws.amazon.com/drs/latest/userguide/Target-Related-FAQ.html): You can view the following frequently asked questions (FAQs) related to the AWS and AWS Elastic Disaster Recovery.
- [Advanced FAQ](https://docs.aws.amazon.com/drs/latest/userguide/drs-advancved-faq.html): You can view the following advanced frequently asked questions (FAQs) related to AWS Elastic Disaster Recovery.


## [Release Notes](https://docs.aws.amazon.com/drs/latest/userguide/drs-release-notes.html)

- [AWS Elastic Disaster Recovery Service Release Notes](https://docs.aws.amazon.com/drs/latest/userguide/drs-service-release-notes.html)

### [AWS Elastic Disaster Recovery Client Release Notes](https://docs.aws.amazon.com/drs/latest/userguide/drs-client-release-notes.html)

AWS Elastic Disaster Recovery is constantly releasing new agent versions; the versions have major and minor version numbers.

- [Agent Version History](https://docs.aws.amazon.com/drs/latest/userguide/drs-agent-release-notes.html): The following table describes the released versions of the AWS Elastic Disaster Recovery Agent.
- [Failback Client Version History](https://docs.aws.amazon.com/drs/latest/userguide/drs-failback-release-notes.html): The following table describes the released versions of the AWS Elastic Disaster Recovery Failback Client.
- [DRSFA Version History](https://docs.aws.amazon.com/drs/latest/userguide/drs-drsfa-release-notes.html): The following table describes the released versions of the DRSFA Client.
- [CEDR Upgrade Tool Version History](https://docs.aws.amazon.com/drs/latest/userguide/drs-cedr-release-notes.html): The following table describes the released versions of the CloudEndure to DRS Upgrade Tool.
