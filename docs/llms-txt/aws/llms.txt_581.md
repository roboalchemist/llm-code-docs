# Source: https://docs.aws.amazon.com/mgn/latest/ug/llms.txt

# Application Migration Service User Guide

- [What Is AWS Application Migration Service?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
- [Network requirements](https://docs.aws.amazon.com/mgn/latest/ug/preparing-environments.html)
- [Release notes](https://docs.aws.amazon.com/mgn/latest/ug/mgn-release-notes.html)
- [Document history](https://docs.aws.amazon.com/mgn/latest/ug/doc-history.html)

## [Quick start guide](https://docs.aws.amazon.com/mgn/latest/ug/quick-start-guide-gs.html)

- [First time setup](https://docs.aws.amazon.com/mgn/latest/ug/first-time-setup-gs.html): The first setup step for AWS Application Migration Service is creating the replication template.
- [Adding source servers](https://docs.aws.amazon.com/mgn/latest/ug/adding-servers-gs.html): Add source servers to AWS Application Migration Service by installing the AWS Replication Agent (the Agent) on them.
- [Configuring launch settings](https://docs.aws.amazon.com/mgn/latest/ug/configuring-target-gs.html): After you have added your source servers to the AWS Application Migration Service console, you will need to configure the launch settings for each server.
- [Launching a test instance](https://docs.aws.amazon.com/mgn/latest/ug/launching-test-gs.html): After you have added all of your source servers and configured their launch settings, you are ready to launch a test instance.
- [Launching a cutover instance](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover-gs.html): Once you have finalized the testing of all of your source servers, you are ready for cutover.


## [Getting started](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html)

- [Migration workflow](https://docs.aws.amazon.com/mgn/latest/ug/migration-workflow-gs.html): The general process is:
- [Initializing with the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-console.html): In order to use AWS Application Migration Service (Application Migration Service), the service must first be initialized for any AWS Region in which you plan to use Application Migration Service.
- [Initializing with the API](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialize-api.html): In order to use AWS Application Migration Service (Application Migration Service), the service must first be initialized for any AWS Region in which you plan to use Application Migration Service.
- [Configuring the templates](https://docs.aws.amazon.com/mgn/latest/ug/mgn-initialization-templates.html): As part of the initialization of AWS Application Migration Service, you have the opportunity to configure three templates.
- [Using the console](https://docs.aws.amazon.com/mgn/latest/ug/mgn-console.html): AWS Application Migration Service is AWS Region-specific.
- [Best practices](https://docs.aws.amazon.com/mgn/latest/ug/best_practices_mgn.html)
- [Migration at scale](https://docs.aws.amazon.com/mgn/latest/ug/migration_at_scale.html)
- [Service quota limits](https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html): The following are the AWS MGN service quota limits:


## [Settings](https://docs.aws.amazon.com/mgn/latest/ug/settings.html)

### [Replication settings](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings-template.html)

Replication settings determine how data is replicated from your source servers to AWS.

- [Replication server settings reference](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html): Replication servers are lightweight Amazon EC2 instances that are used to replicate data between your source servers and AWS.
- [Launch template settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-template.html): The Launch template allows you to control the way AWS Application Migration Service launches instances in AWS.

### [Post-launch settings](https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings.html)

Post-launch settings allow you to control and automate actions performed after the server has been launched in AWS.

- [Predefined post-launch actions reference](https://docs.aws.amazon.com/mgn/latest/ug/predefined-post-launch-actions.html): AWS Application Migration Service allows you to execute various predefined post-launch actions on your Amazon EC2 launch instance.


## [Source servers](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html)

### [Adding source servers](https://docs.aws.amazon.com/mgn/latest/ug/adding-servers.html)

Add source servers to AWS Application Migration Service by installing the AWS Replication Agent (also referred to as "the Agent") on them.

- [Installation requirements](https://docs.aws.amazon.com/mgn/latest/ug/installation-requirements.html): Before installing the AWS Replication Agent on your source servers, ensure that they meet these requirements:
- [Supported operating systems](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html): AWS Application Migration Service supports replication of physical, virtual or cloud-based source servers for multiple versions of Window and Linux operating systems.

### [Installing the AWS Replication Agent](https://docs.aws.amazon.com/mgn/latest/ug/agent-installation.html)

You must install the AWS Replication Agent on each source server that you want to add to AWS Application Migration Service.

- [Generating the required AWS credentials](https://docs.aws.amazon.com/mgn/latest/ug/credentials.html): In order to install the AWS Replication Agent, you must first generate the required AWS credentials.
- [Installing the agent on Linux servers](https://docs.aws.amazon.com/mgn/latest/ug/linux-agent.html): Complete these steps to install the AWS Replication Agent on Linux source servers.
- [Installing the agent on Windows servers](https://docs.aws.amazon.com/mgn/latest/ug/windows-agent.html): Complete these steps to install the AWS Replication Agent on Windows source servers.
- [Installing the Agent on a secured network](https://docs.aws.amazon.com/mgn/latest/ug/installing-agent-blocked.html): The AWS Application Migration Service AWS Replication Agent installer needs network access to Application Migration Service and Amazon S3 endpoints.
- [Uninstalling the Agent](https://docs.aws.amazon.com/mgn/latest/ug/uninstalling-agent.html): Uninstalling the AWS Replication Agent from a source server stops the replication of that server.
- [Reinstalling the Agent](https://docs.aws.amazon.com/mgn/latest/ug/reinstalling-agent.html): To reinstall the AWS Replication Agent, download the latest version of the agent and follow the installation instructions.

### [Installing the vCenter Client](https://docs.aws.amazon.com/mgn/latest/ug/agentless-mgn.html)

Learn how to install the Application Migration Service vCenter client to set up agentless snapshot-based replication on vCenter source environments.

- [Agentless replication overview](https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-overview-mgn.html): Agentless snapshot-based replication allows you to replicate source servers on your vCenter environment into AWS without installing the AWS Replication Agent.
- [VMware limitations](https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-reques-mgn.html): Application Migration Service supports VMC on AWS for agentless replication.
- [Generating vCenter Client IAM credentials](https://docs.aws.amazon.com/mgn/latest/ug/vcenter-credentials-mgn.html): In order to use the Application Migration Service vCenter Client, you must first generate the correct IAM credentials.

### [Installing the Application Migration Service vCenter Client](https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-appliance-mgn.html)

The first step to deploying the agentless solution is installing the Application Migration Service vCenter Client on your vCenter environment.

- [Application Migration Service vCenter Client installation instructions](https://docs.aws.amazon.com/mgn/latest/ug/client-installation-instructions-mgn.html): To install the Application Migration Service vCenter Client, follow these steps:
- [Replicating servers from vCenter to AWS](https://docs.aws.amazon.com/mgn/latest/ug/replicating-vcenter-aws-mgn.html): Once you have successfully installed the AWS vCenter client, all of your vCenter VMs are added to Application Migration Service in the DISCOVERED state.
- [Updating the vCenter or AWS Credentials](https://docs.aws.amazon.com/mgn/latest/ug/updating-vcenter-or-aws-credentials.html): Users who want to change the vCenter or AWS credentials used by the Application Migration Service appliance should follow these steps.
- [Differentiating agentless and agent-based servers](https://docs.aws.amazon.com/mgn/latest/ug/differences-vcenter-aws.html): You can differentiate an agentless vCenter VM that's replicating through snapshot shipping and an agent-based server (from any source infrastructure) through several ways:

### [Manage source servers](https://docs.aws.amazon.com/mgn/latest/ug/server-list.html)

The Source servers page lists all of the source servers that have been added to AWS Application Migration Service (AWS MGN).

- [Add a source server](https://docs.aws.amazon.com/mgn/latest/ug/add-server-server-page.html): To add a server, simply click Add server.
- [Manage data replication](https://docs.aws.amazon.com/mgn/latest/ug/server-replication-main.html): You can manage data replication for the source server through these actions on the Replication drop-down menu:
- [Manage test and cutover instances](https://docs.aws.amazon.com/mgn/latest/ug/server-test-cutover-main.html): The Test and cutover menu allows you to manage your test and cutover instances.
- [Source server migration metrics](https://docs.aws.amazon.com/mgn/latest/ug/source-server-migration-metrics.html): The source server migration metrics present an aggregated overview of your source servers, focused on three topics: Alerts, Data replication status, and Migration status.
- [Filtering the source servers list](https://docs.aws.amazon.com/mgn/latest/ug/list-filtering.html): You can customize the Source servers page through filtering.

### [Server details](https://docs.aws.amazon.com/mgn/latest/ug/server-details.html)

You can access the server details view by clicking on the Source server name of any server on the Source servers page.

- [Migration dashboard](https://docs.aws.amazon.com/mgn/latest/ug/migration-dashboard.html): The Migration dashboard tab allows you to monitor the server in relation to the migration lifecycle.
- [Server info](https://docs.aws.amazon.com/mgn/latest/ug/source-server-info.html): The Server info tab displays general server information, hardware, and network information:
- [Tags](https://docs.aws.amazon.com/mgn/latest/ug/Cirrus_tags.html): The Tags section shows any tags that have been assigned to the server.
- [Disk settings](https://docs.aws.amazon.com/mgn/latest/ug/disk-settings.html): The Disk settings tab shows a list of all of the disks on the source server and information for each disk.
- [Change staging disk type](https://docs.aws.amazon.com/mgn/latest/ug/staging-disk.html): You can change the EBS volume disk type for each disk or for a group of disks.
- [Replication settings](https://docs.aws.amazon.com/mgn/latest/ug/replication-settings.html): The Replication settings tab allows you to edit the replication settings for an individual source server.
- [Launch settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-settings-source.html): The launch settings are a set of instructions that comprise an EC2 launch template and other settings, which determine how a test or cutover instance is launched for each source server on AWS.
- [Post-launch settings](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings.html): Post-launch settings allow you to control and automate actions performed after the server has been launched in AWS.
- [Editing the post-launch settings](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings-editing.html): To edit the post-launch settings for a single source servers, check the box to the left of the Hostname of each source server for which you want to edit the post-launch settings, open the Replication menu, and choose Edit post-launch settings.
- [Activating and deactivating post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings-actions.html): This setting controls whether post-launch actions are active or inactive.
- [Deploying post-launch actions](https://docs.aws.amazon.com/mgn/latest/ug/source-post-launch-settings-deployment.html): Use this setting to choose whether to deploy the post-launch actions only on your cutover instances or on both cutover and test instances.


## [Applications](https://docs.aws.amazon.com/mgn/latest/ug/applications.html)

### [Applications page](https://docs.aws.amazon.com/mgn/latest/ug/applications-list.html)

The Applications page lists all the applications that have been added to AWS Application Migration Service.

- [Add application](https://docs.aws.amazon.com/mgn/latest/ug/add-application.html): To add an application, click Add application.
- [Edit application](https://docs.aws.amazon.com/mgn/latest/ug/edit-application.html): To edit an application, click Edit.
- [Delete application](https://docs.aws.amazon.com/mgn/latest/ug/delete-application.html): To delete an application, click Delete.
- [Manage applications](https://docs.aws.amazon.com/mgn/latest/ug/application-actions-menu.html): The Actions menu allows you to perform actions on selected applications.
- [Filtering](https://docs.aws.amazon.com/mgn/latest/ug/applications-filtering.html): You can customize the Applications page through filtering.

### [Application details](https://docs.aws.amazon.com/mgn/latest/ug/application-details.html)

There are several ways you can access the Application details view.

- [Overview dashboard](https://docs.aws.amazon.com/mgn/latest/ug/application-overview-dashboard.html): The Overview dashboard provides an overview of the overall application status, including:

### [Review aggregated source server migration metrics](https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics.html)

The source server migration metrics show an aggregated overview of the application associated servers on three topics: Alerts, Data replication status and Migration status.

- [Alerts](https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics-alerts.html): The source server Alerts migration metric presents an aggregated overview of the application associated servers alerts.
- [Data replication status](https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics-drs.html): The source server Data replication status migration metric presents an aggregated overview of the application associated servers data replication status.
- [Migration lifecycle](https://docs.aws.amazon.com/mgn/latest/ug/application-source-server-migration-metrics-migration.html): The source server Migration lifecycle metric shows an aggregated overview of the application associated servers migration lifecycle.
- [Source servers table](https://docs.aws.amazon.com/mgn/latest/ug/application-source-servers-table.html): The Source servers table lists all the servers that are associated with the application.
- [Tags](https://docs.aws.amazon.com/mgn/latest/ug/application-cirrus_tags.html): The Tags section shows any tags that have been assigned to the application.


## [Waves](https://docs.aws.amazon.com/mgn/latest/ug/waves.html)

### [Waves page](https://docs.aws.amazon.com/mgn/latest/ug/waves-list.html)

The Waves page lists all the waves that have been added to AWS Application Migration Service (AWS MGN).

- [Add wave](https://docs.aws.amazon.com/mgn/latest/ug/add-wave.html): To add a wave, click the Add wave button.
- [Edit wave](https://docs.aws.amazon.com/mgn/latest/ug/edit-wave.html): To edit a wave, click Edit wave.
- [Delete wave](https://docs.aws.amazon.com/mgn/latest/ug/delete-wave.html): To delete a wave, click the Delete wave button and the Delete wave prompt will open.
- [Actions menu](https://docs.aws.amazon.com/mgn/latest/ug/wave-actions-menu.html): The Actions menu allows you to perform actions on selected waves.
- [Filtering](https://docs.aws.amazon.com/mgn/latest/ug/waves-filtering.html): Use filtering to easily filter your waves by one or multiple properties.

### [Wave details](https://docs.aws.amazon.com/mgn/latest/ug/wave-details.html)

There are several ways you can access the Wave details view.

- [Overview dashboard](https://docs.aws.amazon.com/mgn/latest/ug/wave-overview-dashboard.html): The Overview dashboard provides an overview of the overall wave status, including:

### [Applications](https://docs.aws.amazon.com/mgn/latest/ug/wave-applications.html)

The Applications tab shows migration metrics aggregating statuses as well as a list of all the wave associated applications.

- [Alerts](https://docs.aws.amazon.com/mgn/latest/ug/wave-application-migration-metrics-alerts.html): The application Alerts metric provides an aggregated overview of the alerts related to the wave's associated applications.
- [Migration status](https://docs.aws.amazon.com/mgn/latest/ug/wave-application-migration-metrics-migration.html): The application Migration status metric provides an aggregated overview of the migration status of the wave's associated applications.
- [Applications table](https://docs.aws.amazon.com/mgn/latest/ug/wave-applications-table.html): The Applications table lists all the applications that are associated with the wave.

### [Source servers](https://docs.aws.amazon.com/mgn/latest/ug/wave-source-servers.html)

The Source servers tab shows migration metrics aggregating statuses as well as a list of all the wave's associated applications.

- [Alerts](https://docs.aws.amazon.com/mgn/latest/ug/wave-source-server-migration-metrics-alerts.html): The source server Alerts metric provides an aggregated overview of the alerts related to the wave's associated servers.
- [Data replication status](https://docs.aws.amazon.com/mgn/latest/ug/wave-source-server-migration-metrics-drs.html): The source server Data replication status metric provides an aggregated overview of the data replication status of the wave's associated servers.
- [Migration lifecycle](https://docs.aws.amazon.com/mgn/latest/ug/wave-source-server-migration-metrics-migration.html): The source server's Migration lifecycle metric provides an aggregated overview of the migration lifecycle of the wave's associated servers .
- [Source servers table](https://docs.aws.amazon.com/mgn/latest/ug/wave-source-servers-table.html): The Source servers table lists all the servers that are associated with the wave.
- [Tags](https://docs.aws.amazon.com/mgn/latest/ug/wave-cirrus_tags.html): The Tags section shows any tags that have been assigned to the wave.


## [MGN Connectors](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector.html)

- [Prerequisites](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-prerequisites.html): To use the Application Migration Service connector you must meet these prerequisites.
- [Architecture overview](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-architecture.html): The following is the architecture overview when using AWS MGN with MGN connector.

### [IAM roles for connector](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-permissions.html)

To use MGN connector you must have these required IAM roles for individual accounts and AWS Organizations networks:

- [Create roles manually](https://docs.aws.amazon.com/mgn/latest/ug/create-permissions-manually.html): To create permissions manually, you create the MGNConnectorInstallerRole to install the MGN Connector and the AWSApplicationMigrationConnectorManagementRole needed to enable the connector to run.
- [Deploy role using CloudFormation template](https://docs.aws.amazon.com/mgn/latest/ug/CloudFormation_Template.html): See the Create roles manually to deploy these permissions manually.
- [Setup instructions](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-setup-instructions.html): In order to set up your MGN connector, take the following steps:
- [Installing the MGN connector on a secured network](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-installing-secured-network.html): The MGN connector and the AWS Replication Agents that the MGN connector installs, require network access to various AWS endpoints.

### [MGN Connectors management](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector-main.html)

The MGN Connectors page lists all the installed MGN connectors, providing a quick overview of your MGN connectors and their status and allowing you to quickly perform actions.

- [Add MGN connector](https://docs.aws.amazon.com/mgn/latest/ug/add-connector.html): To add an MGN connector, click Add MGN connector, to open the Add MGN connector page.
- [Edit connector](https://docs.aws.amazon.com/mgn/latest/ug/edit-connector.html): To edit an MGN connector, click Edit.
- [Delete MGN connector](https://docs.aws.amazon.com/mgn/latest/ug/delete-connector.html): To delete an MGN connector, click Delete.
- [Register server credentials](https://docs.aws.amazon.com/mgn/latest/ug/connector-register-server-credentials.html): Once you have the MGN connector set up and ready to use, you can register source servers to the MGN connector.
- [Verify source server prerequisites](https://docs.aws.amazon.com/mgn/latest/ug/connector-verify-prereqs.html): The Verify prerequisites action ensures the AWS replication agent can be installed on each of the source servers.
- [Install the replication agent](https://docs.aws.amazon.com/mgn/latest/ug/connector-install-agent.html): Following the prerequisite check, you can proceed to install the replication agent, to start your migration execution.
- [View command history](https://docs.aws.amazon.com/mgn/latest/ug/connector-view-command-history.html): After performing an action, you can view the command history for information on the command status.
- [Review details about your MGN connectors](https://docs.aws.amazon.com/mgn/latest/ug/connector-details.html): Click the MGN connector name of any MGN connector to open its details page.


## [Import and export](https://docs.aws.amazon.com/mgn/latest/ug/import-export.html)

### [Importing your data inventory](https://docs.aws.amazon.com/mgn/latest/ug/import-main.html)

The Import feature allows you to easily import your inventory of servers, applications, and waves from a CSV file that is saved in your local disk or an S3 bucket.

- [Import from a local disk](https://docs.aws.amazon.com/mgn/latest/ug/import-local-disk.html): To import your inventory from a local disk, take the following steps:
- [Importing from an S3 bucket](https://docs.aws.amazon.com/mgn/latest/ug/import-s3.html): To import your inventory from an S3 bucket, take the following steps:
- [Import history](https://docs.aws.amazon.com/mgn/latest/ug/import-history.html): Select the Import history tab to view the files imported in the last 7 days, including their status and the taskâs start and end time.

### [Exporting your data inventory](https://docs.aws.amazon.com/mgn/latest/ug/export-main.html)

The Export feature allows you to easily export your inventory of servers, applications, and waves to a CSV file that is saved in your local disk or an S3 bucket.

- [Export to a local disk](https://docs.aws.amazon.com/mgn/latest/ug/export-local-disk.html): To export your inventory to a local disk, take the following steps:
- [Exporting to an S3 bucket](https://docs.aws.amazon.com/mgn/latest/ug/export-s3.html): To export your inventory to an S3 bucket, take the following steps:
- [Configuration editing](https://docs.aws.amazon.com/mgn/latest/ug/configuration-editing.html): You can use the Import and Export feature to edit your server configuration, including bulk changes:
- [Export history](https://docs.aws.amazon.com/mgn/latest/ug/export-history.html): Select the Export history tab to view the files exported in the last 7 days, including their status, progress, and the taskâs start and end time.


## [Global view](https://docs.aws.amazon.com/mgn/latest/ug/global-view.html)

- [Setting up your AWS Organization](https://docs.aws.amazon.com/mgn/latest/ug/setting-up-organizations.html): The AWS Organizations service enables you to consolidate multiple AWS accounts into a single organization that you create and manage.
- [Activate trusted access](https://docs.aws.amazon.com/mgn/latest/ug/activate-trusted-access.html): To use global view, you must activate trusted access to AWS Application Migration Service (AWS MGN) for your organization.
- [Setting up StackSets](https://docs.aws.amazon.com/mgn/latest/ug/setting-up-stacksets.html): After you set up your organization, you need to configure CloudFormation StackSets to create the required role per management account: AWSApplicationMigrationSharingRole_<MANAGEMENT_ACCOUNT_ID>.
- [Using an AWS KMS customer managed key for encryption](https://docs.aws.amazon.com/mgn/latest/ug/global-ebs-encryption-kms.html): If you decide to use a customer managed key, or if your default Amazon EBS encryption key is a customer managed key in member account, you must add permissions to the AWSApplicationMigrationSharingRole_<MANAGEMENT_ACCOUNT_ID> to allow management account to use it.
- [Inviting other accounts](https://docs.aws.amazon.com/mgn/latest/ug/global-inviting-other-accounts.html): After you create an organization and verify the email address associated with the management account, you can invite existing AWS accounts to join your organization.
- [Using global view](https://docs.aws.amazon.com/mgn/latest/ug/global-view-main.html): Use the global view feature to see source servers across various member accounts and to perform various actions such as installing the SSM Agent.


## [Launching test and cutover instances](https://docs.aws.amazon.com/mgn/latest/ug/launching-target-servers.html)

- [Preparing for test and cutover instance launch](https://docs.aws.amazon.com/mgn/latest/ug/launch-preparation.html): Prior to launching your instances, you must ensure that your environment is set up properly to ensure successful launches.

### [Launch settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-settings.html)

The launch settings include two sections: the general launch settings, and the EC2 launch template, which determine how a test or cutover instance is launched for each source server in AWS.

### [General launch settings](https://docs.aws.amazon.com/mgn/latest/ug/launch-general-settings.html)

The General launch settings section allows you to control a variety of server-specific settings.

- [Instance type right-sizing](https://docs.aws.amazon.com/mgn/latest/ug/right-sizing.html): AWS Application Migration Service launches a new instance type after every change of configuration on the source server, for example, added/removed disks, and added/removed RAM.
- [Start instance upon launching](https://docs.aws.amazon.com/mgn/latest/ug/start-launch.html): Choose whether you want to start your test and cutover instances automatically upon launch or whether you want to launch them in a stopped state.
- [Copy Private IP](https://docs.aws.amazon.com/mgn/latest/ug/copy-private.html): Choose whether you want AWS Application Migration Service to ensure that the private IP used by the test or cutover instance matches the private IP used by the source server.
- [Operating system licensing](https://docs.aws.amazon.com/mgn/latest/ug/os-licensing.html): Choose whether you want to Bring Your Own Licenses (BYOL) from the source server into the test or cutover instance.
- [Transfer server tags](https://docs.aws.amazon.com/mgn/latest/ug/transfer-tags.html): Choose whether you want AWS Application Migration Service to transfer any user-configured custom tags from your source servers onto your test or cutover instance.
- [Boot mode](https://docs.aws.amazon.com/mgn/latest/ug/boot-mode.html): Choose the boot mode for the test or cutover instance.

### [EC2 launch template](https://docs.aws.amazon.com/mgn/latest/ug/ec2-launch.html)

AWS Application Migration Service utilizes EC2 launch templates to launch test and cutover EC2 instances for each source server.

- [Selecting the default template](https://docs.aws.amazon.com/mgn/latest/ug/ec2-selecting.html): AWS MGN uses the version of the Launch template that is marked as default.
- [Launch template cleanup and fixing](https://docs.aws.amazon.com/mgn/latest/ug/ec2-considerations.html): AWS Application Migration Service (AWS MGN) runs a mechanism every hour to ensure that the settings selected are correct.
- [Launch template key considerations](https://docs.aws.amazon.com/mgn/latest/ug/key-considerations.html): There are several key considerations when configuring your EC2 launch template.
- [Full launch template setting review](https://docs.aws.amazon.com/mgn/latest/ug/detailed-considerations.html): This section reviews the entire EC2 launch template and identifies which fields should and should not be changed in order for the EC2 launch template to work with Application Migration Service.
- [Saving your EC2 launch template](https://docs.aws.amazon.com/mgn/latest/ug/ec2-saving.html): Once you have finished editing your template, save it by choosing Create template version at the bottom of the template.

### [Launching test instances](https://docs.aws.amazon.com/mgn/latest/ug/launching-test-servers.html)

After you have added all of your source servers and configured their launch settings, you are ready to launch a test instance.

- [Ready for testing indicators](https://docs.aws.amazon.com/mgn/latest/ug/ready-for-testing.html): Prior to launching a Test instance, ensure that your source servers are ready for testing by looking for the following indicators on the Source servers page:
- [Starting a test](https://docs.aws.amazon.com/mgn/latest/ug/starting-test.html): To launch a test instance for a single source server or multiple source servers:
- [Reverting a test](https://docs.aws.amazon.com/mgn/latest/ug/revert-finalize-test.html): After you have launched your test instances, open the Amazon EC2 console and SSH or RDP into your test instances in order to ensure that they function correctly.
- [Marking as Ready for cutover](https://docs.aws.amazon.com/mgn/latest/ug/finalizing-test.html): If you are completely done with your testing and are ready for cutover, you can finalize the test.

### [Launching cutover instances](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover.html)

Once you have finalized the testing of all of your source servers, you are ready for cutover.

- [Ready for cutover indicators](https://docs.aws.amazon.com/mgn/latest/ug/ready-for-cutover.html): Prior to launching a cutover instance, ensure that your source servers are ready for cutover by looking for the following indicators on the Source servers page:
- [Starting a cutover](https://docs.aws.amazon.com/mgn/latest/ug/starting-cutover.html): To launch a cutover instance for a single source server or multiple source servers, go to the Source servers page and check the box to the left of each server you want to cutover.
- [Reverting a cutover](https://docs.aws.amazon.com/mgn/latest/ug/revert-finalize-cutover.html): Once you have launched your cutover instances, open the Amazon EC2 console and SSH or RDP into your cutover instances in order to ensure that they function correctly.
- [Finalizing a cutover](https://docs.aws.amazon.com/mgn/latest/ug/finalizing-cutover-2.html): If you are completely done with your migration and performed a successful cutover, you can finalize the cutover.
- [Launch history](https://docs.aws.amazon.com/mgn/latest/ug/jobs.html): The Launch history tab allows you to track and manage all of the operation performed in AWS Application Migration Service.


## [Monitoring Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/monitoring-overview.html)

- [Monitoring with CloudWatch](https://docs.aws.amazon.com/mgn/latest/ug/monitoring-cloudwatch.html): You can monitor Application Migration Service using CloudWatch, which collects raw data and processes it into readable, near real-time metrics.

### [MGN and EventBridge](https://docs.aws.amazon.com/mgn/latest/ug/cloudwatch-events.html)

Application Migration Service sends events to Amazon EventBridge whenever a Source server launch has completed, a Source server reaches the READY_FOR_TEST lifecycle state for the first time, and when the data replication state becomes Stalled or when the data replication state is no longer Stalled .

- [Event samples](https://docs.aws.amazon.com/mgn/latest/ug/eventbridge-events.html): The following are sample MGN events in EventBridge:
- [Registering event rules](https://docs.aws.amazon.com/mgn/latest/ug/eventbridge-event-rule.html): You create CloudWatch Events event rules that capture events coming from your Application Migration Service resources.
- [Logging AWS Application Migration Service with AWS CloudTrail](https://docs.aws.amazon.com/mgn/latest/ug/logging-using-cloudtrail.html): AWS Application Migration Service is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Application Migration Service.


## [Security](https://docs.aws.amazon.com/mgn/latest/ug/security.html)

### [Identity and access management](https://docs.aws.amazon.com/mgn/latest/ug/identity-access-management.html)

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.

- [Authenticating with identities](https://docs.aws.amazon.com/mgn/latest/ug/security_iam_authentication.html): Authentication is how you sign in to AWS using your identity credentials.
- [Grant permission to tag resources during creation](https://docs.aws.amazon.com/mgn/latest/ug/supported-iam-actions-tagging.html): Some resource-creating Amazon MGN API actions enable you to specify tags when you create the resource.

### [AWS managed policies](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol.html)

Learn about AWS managed policies for AWS Application Migration Service that you can use to grant permissions.

- [AWSApplicationMigrationServiceRolePolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationServiceRolePolicy.html)
- [AWSApplicationMigrationConversionServerPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationConversionServerPolicy.html)
- [AWSApplicationMigrationReplicationServerPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationReplicationServerPolicy.html)
- [AWSApplicationMigrationAgentPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationAgentPolicy.html)
- [AWSApplicationMigrationMGHAccess](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationMGHAccess.html)
- [AWSApplicationMigrationFullAccess](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationFullAccess.html): You can attach the AWSApplicationMigrationFullAccess policy to your IAM identities.
- [AWSApplicationMigrationEC2Access](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationEC2Access.html)
- [AWSApplicationMigrationSSMAccess](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationSSMAccess.html)
- [AWSApplicationMigrationReadOnlyAccess](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationReadOnlyAccess.html)
- [AWSApplicationMigrationVCenterClientPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationVCenterClientPolicy.html)
- [AWSApplicationMigrationAgentInstallationPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.html)
- [AWSApplicationMigrationAgentPolicy_v2](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationAgentPolicy_v2.html)
- [AWSApplicationMigrationServiceEc2InstancePolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationServiceEc2InstancePolicy.html)
- [AWSApplicationMigrationNetworkMigrationMultiAccount](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationNetworkMigrationMultiAccount.html): You can attach the AWSApplicationMigrationNetworkMigrationMultiAccount policy to your IAM identities.
- [AWSApplicationMigrationNetworkMigrationCustomResource](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationNetworkMigrationCustomResource.html): Allows modification of Transit Gateway resources created by Application Migration Service.

### [Managing access using policies](https://docs.aws.amazon.com/mgn/latest/ug/security_iam_access-manage.html)

You control access in AWS by creating policies and attaching them to AWS identities or resources.

### [Using identity-based policies](https://docs.aws.amazon.com/mgn/latest/ug/Using_Identity_based_policies.html)

By default, users and roles don't have permission to create or modify AWS Application Migration Service resources.

- [Customer-managed policies in AWS MGN](https://docs.aws.amazon.com/mgn/latest/ug/customer_managed_policies_mgn.html): You can create your own custom IAM policies to allow permissions for AWS Application Migration Service actions and resources.
- [Restrict permission to act on a source server associated with given AWS vCenter client](https://docs.aws.amazon.com/mgn/latest/ug/restrict-to-vcenter-client.html): To restrict access to source servers associated with a given AWS vCenter client, use the condition element mgn:VcenterClientId condition key.
- [Using service-linked roles](https://docs.aws.amazon.com/mgn/latest/ug/using-service-linked-roles.html): How to use service-linked roles to give AWS Application Migration Service access to resources in your AWS account.
- [Resilience](https://docs.aws.amazon.com/mgn/latest/ug/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Application Migration Service features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/mgn/latest/ug/infrastructure-security.html): Learn how AWS Application Migration Service isolates service traffic.
- [Compliance validation](https://docs.aws.amazon.com/mgn/latest/ug/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/mgn/latest/ug/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.


## [Troubleshooting](https://docs.aws.amazon.com/mgn/latest/ug/troubleshooting.html)

- [Troubleshooting launch errors](https://docs.aws.amazon.com/mgn/latest/ug/Troubleshooting-Launch-Errors.html): Use the information in this section to troubleshoot launch errors.
- [Troubleshooting communication errors](https://docs.aws.amazon.com/mgn/latest/ug/Troubleshooting-Communication-Errors.html): Use the information in this section to troubleshoot communication errors.
- [Troubleshooting agent issues](https://docs.aws.amazon.com/mgn/latest/ug/Troubleshooting-Agent-Issues.html): Use the information in this section to troubleshoot issues with installing the replication agent.
- [Troubleshooting agentless replication issues](https://docs.aws.amazon.com/mgn/latest/ug/agentless-troubleshooting.html): Discovery related troubleshooting
- [Common replication errors](https://docs.aws.amazon.com/mgn/latest/ug/common-replication-errors.html): This section describes common replication errors, possible explanations, and potential mitigations.
- [Other troubleshooting topics](https://docs.aws.amazon.com/mgn/latest/ug/Other-Troubleshooting-Topics.html): Use the information in this section to help you with other troubleshooting.


## [FAQ](https://docs.aws.amazon.com/mgn/latest/ug/FAQ.html)

- [General questions](https://docs.aws.amazon.com/mgn/latest/ug/General-Questions-FAQ.html): This section contains answers to general questions about AWS Application Migration Service.
- [Agent related](https://docs.aws.amazon.com/mgn/latest/ug/Agent-Related-FAQ.html): This section contains answers to questions about the AWS Replication Agent.
- [Agentless replication related](https://docs.aws.amazon.com/mgn/latest/ug/Agentless-Replication-Related-FAQ.html): This section contains answers to questions about agentless replication.
- [Replication related](https://docs.aws.amazon.com/mgn/latest/ug/Replication-Related-FAQ.html): This section contains answers to questions about data replication.
- [AWS related](https://docs.aws.amazon.com/mgn/latest/ug/AWS-Related-FAQ.html): This section contains answers to questions about AWS and AWS Application Migration Service.
- [Does AWS MGN work with...?](https://docs.aws.amazon.com/mgn/latest/ug/does-mgn.html): This section contains answers to questions about what AWS Application Migration Service works with.
- [Post-launch actions related](https://docs.aws.amazon.com/mgn/latest/ug/Post-Launch-Actions-FAQ.html): This section contains answers to questions about post-launch actions.
