# Source: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/llms.txt

# Amazon Relational Database Service User Guide

> Amazon Web Services (AWS) documentation to help you set up, operate, and scale a relational database in the AWS Cloud using Amazon Relational Database Service (Amazon RDS). You can create DB instances that run Amazon Aurora, MariaDB, Microsoft SQL Server, MySQL, Oracle, and PostgreSQL.

- [Setting up](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SettingUp.html)
- [Tutorials and sample code](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.html)
- [Best practices for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.html)
- [Quotas and constraints](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html)
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/WhatsNew.html)
- [AWS Glossary](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/glossary.html)

## [What is Amazon RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

- [DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.html): Learn Amazon Relational Database Service (RDS) terminology and concepts surrounding DB instances.

### [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)

Determine the computation and memory capacity of an Amazon RDS DB instance by its DB instance class.

- [DB instance class types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Types.html): A reference of DB instance class types.
- [Supported DB engines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Support.html): A reference of supported DB engines for DB instance classes.
- [Determining DB instance class support in AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.RegionSupport.html): Determine the DB instance classes Amazon RDS supports for a DB engine in an AWS Region.
- [Configuring the processor for RDS for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConfigureProcessor.html): Configure the processor for the DB instance class of an RDS for Oracle DB instance by using the AWS Management Console, AWS CLI, or API.
- [Hardware specifications](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.Summary.html): A reference of hardware specifications for DB instance class types.
- [DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html): Work with the different storage types available for a DB instance on Amazon RDS.
- [Regions, Availability Zones, and Local Zones](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html): Learn how Amazon cloud computing resources are hosted in multiple locations world-wide, including AWS Regions and Availability Zones.

### [Supported Amazon RDS features by Region and engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDSFeaturesRegionsDBEngines.grids.html)

Learn which features are supported in each AWS Region for different Amazon RDS DB engines.

- [Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.html): View the AWS Region and Amazon RDS DB engine version availability for Blue/Green Deployments.
- [Cross-Region automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionAutomatedBackups.html): View the AWS Region and Amazon RDS DB engine version availability for the cross-Region automated backups feature.
- [Cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.CrossRegionReadReplicas.html): View the AWS Region and Amazon RDS DB engine version support for the cross-region read replicas feature.
- [Database activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.DBActivityStreams.html): View the AWS Region and Amazon RDS DB engine version support for the database activity streams feature.
- [Dual-stack mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.DualStackMode.html): View the AWS Region and Amazon RDS DB engine version support for the dual-stack mode feature.
- [Export snapshots to S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.html): View the AWS Region and Amazon RDS DB engine version availability for the export snapshots to S3 feature.
- [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.IamDatabaseAuthentication.html): View the AWS Region and Amazon RDS DB engine version availability for the IAM database authentication feature.
- [Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.KerberosAuthentication.html): View the AWS Region and Amazon RDS DB engine version availability for the Kerberos authentication feature.
- [Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.MultiAZDBClusters.html): View the AWS Region and Amazon RDS DB engine version availability for Multi-AZ DB clusters.
- [Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.PerformanceInsights.html): View the AWS Region and Amazon RDS DB engine version availability for the Performance Insights feature.
- [RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.html): View the AWS Region and Amazon RDS DB engine version availability for the RDS Custom feature.
- [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSProxy.html): View the AWS Region and Amazon RDS DB engine version availability for the Amazon RDS Proxy feature.
- [Secrets Manager integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.SecretsManager.html): View the AWS Region and Amazon RDS DB engine version availability for AWS Secrets Manager integration.
- [Zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.ZeroETL.html): View the AWS Region and Amazon RDS DB engine version support for zero-ETL integrations with Amazon Redshift and Amazon SageMaker.
- [Engine-native features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.html): Learn which engine-native features are supported for Amazon RDS DB engines.

### [DB instance billing for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_DBInstanceBilling.html)

Understand how Amazon RDS DB instances are billed.

- [On-Demand DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_OnDemandDBInstances.html): Get on-demand DB instances by purchasing DB instance resources by the second.

### [Reserved DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)

Get reserved DB instances by purchasing DB instances up front at a significantly lower cost.

- [Purchasing reserved DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.WorkingWith.html): Purchase reserved DB instances with the Amazon RDS console, the AWS CLI, or the Amazon RDS API.
- [Viewing the billing for reserved DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/reserved-instances-billing.html): View the billing for your reserved DB instances in the AWS Management Console.


## [Getting started](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.html)

- [Creating and connecting to a MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MariaDB.html): Create and connect to an Amazon RDS DB instance running MariaDB.
- [Creating and connecting to a Microsoft SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.SQLServer.html): Create and connect to an Amazon RDS DB instance running Microsoft SQL Server.
- [Creating and connecting to a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html): Create and connect to an Amazon RDS DB instance running MySQL
- [Creating and connecting to an Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.Oracle.html): Create and connect to an Amazon RDS DB instance running Oracle
- [Creating and connecting to a PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html): Create and connect to an Amazon RDS DB instance running PostgreSQL

### [Tutorial: Create a web server and an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TUT_WebAppWithRDS.html)

Follow this tutorial to create a web server and an Amazon RDS DB instance using Amazon RDS and other AWS services.

- [Launch an EC2 instance to connect with your DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.LaunchEC2.html): Create an Amazon EC2 instance in the public subnet of your VPC.
- [Create a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html): Create an Amazon RDS DB instance to use with a web server.
- [Install a web server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html): Install a web server to serve public content and connect to the private Amazon RDS DB Instance.
- [Tutorial: Create a Lambda function to access your Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-lambda-tutorial.html): Learn how to use AWS Lambda to write data from an Amazon Simple Queue Service message queue to an Amazon RDS database in your AWS account's Amazon Virtual Private Cloud


## [Programmatic access to Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ProgrammaticAccess.html)

- [Console-to-Code](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Using_C2C.html): Learn about using Amazon Q Developer Console-to-Code to generate code for use in other Amazon RDS programming interfaces.


## [Configuring a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_RDS_Configuring.html)

### [Creating a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)

Create an Amazon RDS DB instance that runs your specific database engine.

- [Available settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.Settings.html): In the following table, you can find details about settings that you choose when you create a DB instance.
- [Creating resources with AWS CloudFormation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon RDS using an AWS CloudFormation template.

### [Connecting to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html)

Learn how to connect to an Amazon RDS DB instance.

- [Finding the connection information](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.EndpointAndPort.html): Find the connection information to connect to an Amazon RDS DB instance.
- [Scenarios for accessing a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.ScenariosForAccess.html): Describes scenarios for accessing a DB instance in a VPC
- [Working with option groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithOptionGroups.html): Enable and configure option groups to manage data and databases and provide security for your database.

### [Parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.html)

Manage the DB engine configuration through the use of parameter groups.

- [Overview of parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/parameter-groups-overview.html): A conceptual overview of parameter groups and types of parameter groups.

### [DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithDBInstanceParamGroups.html)

Manage the DB instance configuration through the use of DB parameter groups.

- [Creating a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Creating.html): Create a new DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Associating a DB parameter group to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Associating.html): Associate a DB parameter group to a DB instance using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Modifying parameters in a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Modifying.html): Modify a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Resetting parameters in a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Resetting.html): Reset parameters in a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Copying a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Copying.html): Copy a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Listing DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Listing.html): List DB parameter groups using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [View parameter values for a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Viewing.html): View parameter values for a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Deleting a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Deleting.html): Delete a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.

### [DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithDBClusterParamGroups.html)

Manage the Multi-AZ DB cluster configuration through the use of DB cluster parameter groups.

- [Creating a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.CreatingCluster.html): Create a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Modifying parameters in a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html): Modifying parameters in a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Resetting parameters in a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.ResettingCluster.html): Reset parameters in a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Copying a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.CopyingCluster.html): Copy a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Listing DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.ListingCluster.html): List DB cluster parameter groups using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Viewing parameter values for a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.ViewingCluster.html): View parameter values for a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Deleting a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.DeletingCluster.html): Delete a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Comparing DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithParamGroups.Comparing.html): Use the AWS Management Console to compare two DB parameter groups.
- [Specifying DB parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ParamValuesRef.html): Specify the values for an Amazon RDS or Aurora DB parameter using formulas or functions in the values.
- [Creating an ElastiCache cache from Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/creating-elasticache-cluster-with-RDS-settings.html): Learn how to create an ElastiCache cache from Amazon RDS using settings from an .

### [Auto-migrating EC2 databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration.html)

You can use the RDS console to migrate an EC2 database to RDS.

### [Creating IAM resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration-IAM.html)

RDS uses AWS DMS to migrate your data.

- [Secret access policy and role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration-IAM.secret-iam-role-policy.html): Follow the procedures below to create your secret access policy and role which allow DMS to access the user credentials for your source and target databases.
- [Creating IAM role for DMS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration-IAM.dms-vpc-role.html): You must create an IAM role for AWS DMS to manage the VPC settings for your resources.
- [Set up data migration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration-SetUp.html): To begin migrating data from your EC2 source database, you must create an equivalent RDS database.
- [Managing migrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration.Managing.html): After using the Migrate data from EC2 database action from the RDS console, RDS starts the migration automatically.
- [Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DMS_migration.Monitoring.html): After the data migrations starts, you can monitor its status and progress.
- [Tutorial: Creating a MySQL DB instance with a custom parameter and new option group](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/tutorial-creating-custom-OPG.html): Create a MySQL DB instance on Amazon Relational Database Service with a custom parameter and new option group for password expiration policies and auditing capabilities.


## [Managing a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_RDS_Managing.html)

- [Stopping a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html): Stopping an Amazon RDS DB instance
- [Starting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StartInstance.html): Starting an Amazon RDS DB instance that you previously stopped
- [Rebooting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html): Reboot an Amazon RDS DB instance to apply pending changes to your DB instance.
- [Connecting an EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ec2-rds-connect.html): Connect an EC2 instance and a DB instance.
- [Connecting a Lambda function](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/lambda-rds-connect.html): Connect a Lambda function and a DB instance.

### [Modifying a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

Modify an Amazon RDS DB instance and choose when to apply the changes.

- [Scheduling modifications](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.ApplyImmediately.html): Choose when you want modifications to occur when you modify your DB instance.
- [Available settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Settings.html): Find settings you can modify for your DB instance.

### [Maintaining a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Maintenance.html)

Learn about how Amazon RDS periodically performs maintenance on Amazon RDS resources such as a DB instance.

- [AWS Organizations upgrade rollout](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/RDS.Maintenance.AMVU.UpgradeRollout.html): Amazon RDS supports AWS Organizations upgrade rollout policy to manage automatic minor version upgrades across multiple database resources and AWS accounts.
- [Upgrading the engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Upgrading.html): Find information on upgrading your database engine version.
- [Renaming a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RenameInstance.html): Rename an Amazon RDS DB instance.

### [Working with DB instance read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html)

Create a read replica from a source Amazon RDS DB instance to scale out read operations.

- [Differences between DB engines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Overview.Differences.html): Learn about the differences in read replica behavior and functionality for different database engines on Amazon RDS.
- [Creating a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Create.html): You can create a read replica from an existing DB instance using the AWS Management Console, AWS CLI, or RDS API.
- [Promoting a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Promote.html): You can promote a read replica into a standalone DB instance.
- [Monitoring read replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Monitoring.html): Learn how to check the status of a read replica and how to monitor replication lag.
- [Cross-Region read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.XRgn.html): With Amazon RDS, you can create a read replica in a different AWS Region from the source DB instance.

### [Tagging RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html)

Use tags to manage access, control what actions can be applied to resources, and track costs by adding metadata to your Amazon RDS resources.

- [Tutorial: Specify which DB instances to stop by using tags](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Tagging.RDS.Autostop.html): Add tags to DB instances and then stop DB instances with the assigned tag.

### [ARNs in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html)

Get the format for the Amazon Resource Name, or ARN, for Amazon RDS resources.

- [Constructing an ARN](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.Constructing.html): Construct an ARN for your Amazon RDS resource.
- [Getting an existing ARN](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.Getting.html): Get an ARN for your Amazon RDS resource.

### [Working with storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html)

Specify how you want your data stored in Amazon RDS by choosing a storage type and providing a storage size when you create or modify a DB instance.

### [Viewing storage volume details for your DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-storage-viewing.html)

You can view your storage volume configuration from the AWS Management Console or AWS CLI.

- [Console](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-storage-viewing.console.html): To view your storage volume configuration from the console:
- [CLI](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-storage-viewing.cli.html): To view your storage volume configuration from the AWS CLI, use the describe-db-instances command.

### [Increasing DB instance storage capacity](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.ModifyingExisting.html)

Modify a DB instance to increase storage capacity using the Amazon RDS console, AWS CLI, or Amazon RDS API.

- [Scaling up DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.ModifyingExisting.ScalingUp.html): You can scale up the storage of an existing DB instance by increasing the allocated storage for the primary volume.
- [Adding storage volumes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.ModifyingExisting.AdditionalVolumes.html): For RDS for Oracle and RDS for SQL Server DB instances, you can add up to three storage volumes to increase your total storage capacity up to 256 TiB per instance.
- [Removing additional storage volumes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.RemovingAdditionalVolumes.html): Remove additional storage volumes from RDS for Oracle and RDS for SQL Server DB instances using the Amazon RDS console, AWS CLI, or Amazon RDS API.
- [Managing capacity automatically with storage autoscaling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.Autoscaling.html): Enable Amazon RDS to automatically modify a DB instance to increase storage capacity using the Amazon RDS console, AWS CLI, or Amazon RDS API.
- [Upgrading the storage file system](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.UpgradeFileSystem.html): Most RDS DB instances offer a maximum storage size of 64 TiB for RDS for MariaDB, MySQL, and PostgreSQL databases.
- [Modifying Provisioned IOPS settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_PIOPS.Increase.html): Modify the settings for Provisioned IOPS SSD storage using the Amazon RDS console, AWS CLI, or API.
- [I/O-intensive storage modifications](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.IOIntensive.html): Amazon RDS DB instances use Amazon Elastic Block Store (EBS) volumes for database and log storage.
- [Modifying General Purpose (gp3) settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.gp3.html): Modify the settings for General Purpose SSD (gp3) storage using the Amazon RDS console, AWS CLI, or API.
- [Using a dedicated log volume (DLV)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.dlv.html): Use a dedicated log volume (DLV) using the Amazon RDS console, AWS CLI, or API.
- [Deleting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html): Delete a DB instance by specifying the name of the DB instance.
- [Tutorial: Managing a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/tutorial-managing-MySQL-DB.html): Manage a MySQL DB instance lifecycle encompassing development through production by performing tasks like adding tags, expanding storage, creating read replicas, and deleting resources as needed.


## [Configuring and managing a Multi-AZ deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

### [Multi-AZ DB instance deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

Get high availability and failover support for Amazon RDS DB instances by using Multi-AZ deployments with a single standby DB instance.

- [Converting a DB instance to a Multi-AZ deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Migrating.html): Improve availability by modifying an Amazon RDS DB instance to a Multi-AZ deployment.
- [Failing over a Multi-AZ DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.Failover.html): Manually fail over an Amazon RDS Multi-AZ DB instance.
- [Multi-AZ failover with additional storage volumes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MultiAZ.AdditionalStorageVolumes.html): Multi-AZ deployments support DB instances with additional storage volumes.

### [Multi-AZ DB cluster deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.html)

Get high availability, failover support, and more read capacity for your DB instances with Amazon RDS using a Multi-AZ DB cluster.

- [Creating a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-multi-az-db-cluster.html): Create a Multi-AZ DB cluster using Amazon RDS.

### [Connecting to a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts-connection-management.html)

Create a read replica from a source Multi-AZ DB cluster to scale out read operations.

- [Connecting with the AWS drivers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/maz-cluster-connect-drivers.html): Connect to Amazon RDS Multi-AZ DB clusters with the AWS drivers.

### [Connecting an AWS compute resource and a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-compute-rds-connect.html)

Connect an AWS compute resource and a Multi-AZ DB cluster.

- [Connecting an EC2 instance and a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multiaz-ec2-rds-connect.html): Connect an EC2 instance and a Multi-AZ DB cluster.
- [Connecting a Lambda function and a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multiaz-lambda-rds-connect.html): Connect a Lambda function and a Multi-AZ DB cluster.
- [Modifying a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/modify-multi-az-db-cluster.html): Modify a Multi-AZ DB cluster using Amazon RDS.
- [Upgrading a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-upgrading.html): Amazon RDS provides newer versions of each supported database engine so that you can keep your Multi-AZ DB cluster up to date.
- [Renaming a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-cluster-rename.html): Rename an Amazon RDS Multi-AZ DB cluster.
- [Rebooting a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts-rebooting.html): Reboot your Multi-AZ DB clusters and reader DB instances, such as for maintenance reasons.
- [Failing over a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts-failover.html): If there is a planned or unplanned outage of your writer DB instance in a Multi-AZ DB cluster, Amazon RDS automatically fails over to a reader DB instance in different Availability Zone.
- [PostgreSQL logical replication with Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MultiAZDBCluster_LogicalRepl.html): Set up logical replication for an RDS for PostgreSQL Multi-AZ DB cluster.

### [Working with Multi-AZ DB cluster read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MultiAZDBCluster_ReadRepl.html)

Create a read replica from a source Multi-AZ DB cluster, or migrate to a Multi-AZ DB cluster using a read replica.

- [Migrating to a Multi-AZ DB cluster using a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-migrating-to-with-read-replica.html): To migrate a Single-AZ deployment or Multi-AZ DB instance deployment to a Multi-AZ DB cluster deployment with reduced downtime, you can create a Multi-AZ DB cluster read replica.
- [Creating a DB instance read replica from a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-create-instance-read-replica.html): You can create a DB instance read replica from a Multi-AZ DB cluster in order to scale beyond the compute or I/O capacity of the cluster for read-heavy database workloads.
- [Setting up external replication from Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-external-replication.html): Set up external replication for RDS for MySQL and RDS for PostgreSQL Multi-AZ DB clusters.
- [Deleting a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteMultiAZDBCluster.Deleting.html): Delete a DB Multi-AZ DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.
- [Limitations of Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-clusters-concepts.Limitations.html): Learn about the limitations of Multi-AZ DB clusters.


## [RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support.html)

- [RDS Extended Support overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-overview.html): Learn about versions, charges, and responsibilities concerning Amazon RDS Extended Support.
- [RDS Extended Support charges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-charges.html): Learn about charges associated with Amazon RDS Extended Support.
- [Versions with RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-versions.html): Learn which engine versions support Amazon RDS Extended Support.
- [Responsibilities with RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-responsibilities.html): Learn about Amazon RDS and customer responsibilities with Amazon RDS Extended Support.
- [Creating a DB instance or a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-creating-db-instance.html): Learn about creating a DB instance or a Multi-AZ DB cluster with an Amazon RDS Extended Support version.
- [Viewing RDS Extended Support enrollment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-viewing.html): Learn about viewing the enrollment of your DB instances or Multi-AZ DB clusters in Amazon RDS Extended Support.
- [Viewing support dates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-viewing-support-dates.html): Learn about how to view the support dates for engine versions in DB instances or Multi-AZ DB clusters in Amazon RDS Extended Support.
- [Restoring a DB instance or a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/extended-support-restoring-db-instance.html): Learn about restoring a DB instance or a Multi-AZ DB cluster with an Amazon RDS Extended Support version.


## [Using Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)

### [Overview of Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-overview.html)

Learn about concepts related to Amazon RDS Blue/Green Deployments.

- [Authorizing access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-authorizing-access.html): Users must have the required permissions to perform operations related to blue/green deployments.
- [Limitations and considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-considerations.html): Blue/green deployments in Amazon RDS require careful consideration of factors such as replication slots, resource management, instance sizing, and potential impacts on database performance.

### [Best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-best-practices.html)

The following are best practices for blue/green deployments.

- [PostgreSQL replication methods](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-replication-type.html): Amazon RDS for PostgreSQL primarily uses physical replication for blue/green deployments.
- [Creating a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-creating.html): Learn about creating a blue/green deployment for reduce downtime when you make database updates.
- [Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-viewing.html): Learn about viewing details of a blue/green deployment.
- [Switching a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-switching.html): Learn about switching a blue/green deployment to make your staging environment your production environment.
- [Deleting a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments-deleting.html): Learn about deleting a blue/green deployment.


## [Backing up, restoring, and exporting data](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)

- [Introduction to backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html): Conceptual information about automated and manual backups.

### [Managing automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.html)

Conceptual information about automated backups.

- [Backup retention period](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.BackupRetention.html): You can set the backup retention period when you create or restore a DB instance or Multi-AZ DB cluster.
- [Enabling automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.Enabling.html): If your DB instance doesn't have automated backups enabled, you can enable them at any time.
- [Retaining automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.Retaining.html)
- [Deleting retained automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups-Deleting.html): You can delete retained automated backups when they are no longer needed.
- [Unsupported MySQL storage engines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.BackupDeviceRestrictions.html): For the MySQL DB engine, automated backups are only supported for the InnoDB storage engine.
- [Unsupported MariaDB storage engines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.BackupDeviceRestrictionsMariaDB.html): For the MariaDB DB engine, automated backups are only supported with the InnoDB storage engine.

### [Cross-Region automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html)

Replicate automated backups of your DB instances to another AWS Region.

- [Enabling cross-Region automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedBackups.Replicating.Enable.html): You can enable backup replication on new or existing DB instances using the Amazon RDS console.
- [Finding information about replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedBackups.Replicating.Describe.html): You can use the following CLI commands to find information about replicated backups:
- [Point-in-time recovery from a replicated backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedBackups.PiTR.html): You can restore a DB instance to a specific point in time from a replicated backup using the Amazon RDS console.
- [Stopping backup replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedBackups.StopReplicating.html): You can stop backup replication for DB instances using the Amazon RDS console.
- [Deleting replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedBackups.Delete.html): You can delete replicated backups for DB instances using the Amazon RDS console.
- [Troubleshooting stopped replicated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedXREGBackups.Troubleshooting.html): Amazon RDS automatically stops cross-Region automated backup replication under specific circumstances to protect your data and maintain compliance with AWS operational requirements.

### [Managing manual backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingManualBackups.html)

Learn how to create and delete DB snapshots and Multi-AZ cluster snapshots in Amazon Relational Database Service.

- [Creating a DB snapshot for a Single-AZ DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateSnapshot.html): Create a DB snapshot by identifying which DB instance you are going to back up and give that DB snapshot a name.
- [Creating a Multi-AZ DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateMultiAZDBClusterSnapshot.html): When you create a Multi-AZ DB cluster snapshot, make sure to identify which Multi-AZ DB cluster you are going to back up, and then give your DB cluster snapshot a name so you can restore from it later.
- [Deleting a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteSnapshot.html): Delete an Amazon RDS DB snapshot.

### [Restoring to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromSnapshot.html)

Restore to an Amazon RDS DB instance from a DB snapshot.

- [Point-in-time recovery](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.html): Restore an Amazon RDS DB instance to a specific point in time.
- [Restoring a Multi-AZ DB cluster to a specified time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIT.MultiAZDBCluster.html): Restore a Multi-AZ DB cluster to a specific point in time, creating a new Multi-AZ DB cluster.
- [Restoring from a snapshot to a Multi-AZ DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromMultiAZDBClusterSnapshot.Restoring.html): Restore a snapshot to a Multi-AZ DB cluster using the AWS Management Console, the AWS CLI, or the RDS API.
- [Restoring from a Multi-AZ DB cluster snapshot to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RestoreFromMultiAZDBClusterSnapshot.html): Restore a Multi-AZ DB cluster snapshot to a Single-AZ deployment or Multi-AZ DB instance deployment.
- [Tutorial: Restore a DB instance from a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.RestoringFromSnapshot.html): Learn how to restore an Amazon RDS DB instance from a DB snapshot.
- [Copying a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html): Copy an Amazon RDS DB snapshot.

### [Sharing a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html)

Share a manual DB snapshot so that other AWS accounts can copy or restore a DB instance from it.

- [Sharing public snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.Public.html): Share a public DB snapshot.
- [Sharing encrypted snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/share-encrypted-snapshot.html): Share an encrypted DB snapshot.
- [Stopping snapshot sharing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/share-snapshot-stop.html): Stop sharing a DB snapshot.

### [Exporting DB snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html)

Export data from Amazon RDS database snapshots to Amazon S3.

- [Monitoring snapshot exports](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.Monitoring.html): Monitor DB snapshot exports.
- [Canceling a snapshot export](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.Canceling.html): Cancel a DB snapshot export task.
- [Failure messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.failure-msg.html): Learn about the error messages that Amazon RDS returns when Amazon S3 export tasks fail.
- [Troubleshooting PostgreSQL permissions errors](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.postgres-permissions.html): Troubleshoot permissions errors when exporting from RDS for PostgreSQL databases to Amazon S3.
- [File naming conventions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.FileNames.html): Learn about file naming conventions for data exported from Amazon RDS to Amazon S3.
- [Data conversion](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.data-types.html): Amazon RDS converts, exports, and stores data in the Parquet format when exporting to an Amazon S3 bucket.
- [Using AWS Backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/AutomatedBackups.AWSBackup.html): AWS Backup is a fully managed backup service that makes it easy to centralize and automate the backup of data across AWS services in the cloud and on premises.


## [Monitoring metrics in a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html)

- [Monitoring tools](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MonitoringOverview.html): Overview of monitoring tools forAmazon RDS.
- [Viewing instance status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/accessing-monitoring.html): Using the Amazon RDS console, you can quickly access the status of your DB instance.

### [Recommendations from Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-recommendations.html)

Learn about recommendations for your Amazon RDS resources.

- [Viewing recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UserRecommendationsView.html): Learn how to view Amazon RDS recommendations.
- [Applying recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USERRecommendationsManage.ApplyRecommendation.html): Apply Amazon RDS recommendations using the Amazon RDS console or Amazon RDS API.
- [Dismissing recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USERRecommendationsManage.DismissRecommendation.html): Dismiss Amazon RDS recommendations using the Amazon RDS console, AWS CLI, or Amazon RDS API.
- [Modifying dismissed recommendations to active](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USERRecommendationsManage.DismissToActiveRecommendation.html): Modify dismissed Amazon RDS recommendations to active recommendations using the Amazon RDS console, AWS CLI, or Amazon RDS API.
- [Recommendations reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USERRecommendationsManage.RecommendationReference.html): A reference of recommendations from Amazon RDS.
- [Viewing metrics in the Amazon RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.html): View metrics in the Amazon RDS console.

### [Viewing the Performance Insights dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.html)

View CloudWatch and Performance Insights metrics in the Performance Insights dashboard.

- [Choosing the new monitoring view from the Monitoring tab](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.MonitoringTab.html): View Performance Insights and CloudWatch metrics for your database from the Monitoring tab.
- [Choosing the new monitoring view from the Performance Insights page](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.PInavigationPane.html): View Performance Insights and CloudWatch metrics for your database with Performance Insights.
- [Creating a custom dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.PIcustomizeMetricslist.html): Create a custom Performance Insights dashboard to view up to 50 Performance Insights and CloudWatch metrics.
- [Choosing the preconfigured dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.PI-preconfigured-dashboard.html): View the most commonly used metrics to diagnose performance issues using the Performance Insights dashboard.

### [Monitoring RDS with CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/monitoring-cloudwatch.html)

Monitor metrics for Amazon RDS resources using CloudWatch.

- [Viewing CloudWatch metrics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/metrics_dimensions.html): View metrics for your DB instance using the CloudWatch console and the AWS CLI.

### [Exporting Performance Insights metrics to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.html)

Export Performance Insights metrics to CloudWatch as a new dashboard or to an existing dashboard.

- [Exporting Performance Insights metrics as a new dashboard to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.new_dashboard.html): Export Performance Insights metrics to a new CloudWatch dashboard.
- [Adding Performance Insights metrics to an existing CloudWatch dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.existing_dashboard.html): Export Performance Insights metrics to an existing CloudWatch dashboard.
- [Viewing a Performance Insights metric widget in CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PI_metrics_export_CW.individual_widget.html): View Performance Insights metrics in the CloudWatch console.
- [Creating CloudWatch alarms](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/creating_alarms.html): Create CloudWatch alarms to monitor your Amazon RDS resources.
- [Tutorial: Creating a CloudWatch alarm for DB cluster replica lag](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/multi-az-db-cluster-cloudwatch-alarm.html): You can create an Amazon CloudWatch alarm that sends an Amazon SNS message when replica lag for a Multi-AZ DB cluster has exceeded a threshold.

### [Monitoring with Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html)

Monitor your Amazon RDS database load with Database Insights to analyze and troubleshoot the performance of your database fleet.

- [Engine, Region, and instance class support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Engines.html): Learn about the Amazon RDS engine versions that support Database Insights.
- [Turning on the Advanced mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.TurningOnAdvanced.html): Turn on the Advanced mode of Database Insights for Amazon RDS.
- [Turning on the Standard mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.TurningOnStandard.html): Turn on the Standard mode of Database Insights for Amazon RDS.
- [Monitor slow queries](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.SlowSQL.html): Configure your database to monitor slow SQL queries with Database Insights.
- [Considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.Considerations.html): Considerations for Database Insights for Amazon RDS.

### [Monitoring DB load with Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)

Monitor your Amazon RDS DB instance load with Performance Insights to analyze and troubleshoot your database performance.

### [Overview of Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.html)

Learn about using Amazon RDS Performance Insights with DB engines.

- [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html): Learn about the key metric in Amazon RDS Performance Insights, DBLoad, which is collected every second and measures the level of activity in your database.
- [Maximum CPU](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.MaxCPU.html): Use the Performance Insights dashboard to see whether active session activity is exceeding the maximum CPU.
- [Amazon RDS DB engine, Region, and instance class support for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.Engines.html): Learn about the Amazon RDS engine versions that support Performance Insights.
- [Pricing and data retention for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.cost.html): Learn about pricing and data retention for Performance Insights.
- [Turning Performance Insights on and off](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Enabling.html): Turn Performance Insights on or off in the AWS Management Console, AWS CLI, or API.

### [Performance Schema for MariaDB or MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.EnableMySQL.html)

Learn how to monitor runtime performance by turning on the Performance Schema.

- [Determining whether Performance Insights is managing the Performance Schema](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.EnableMySQL.determining-status.html): Determine whether Performance Insights is managing the Performance Schema.
- [Turn on the Performance Schema for Amazon RDS for MariaDB or MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.EnableMySQL.RDS.html): Allow Performance Insights to manage the Performance Schema.

### [Performance Insights policies](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.html)

Configure IAM access policies for Performance Insights.

- [Attaching the AmazonRDSPerformanceInsightsReadOnly policy to an IAM principal](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.managed-policy.html): AmazonRDSPerformanceInsightsReadOnly is an AWS managed policy that grants access to all read-only operations of the Amazon RDS Performance Insights API.
- [Attaching the AmazonRDSPerformanceInsightsFullAccess policy to an IAM principal](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.FullAccess-managed-policy.html): AmazonRDSPerformanceInsightsFullAccess is an AWS managed policy that grants access to all operations of the Amazon RDS Performance Insights API.
- [Creating a custom IAM policy for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.custom-policy.html): Create a custom IAM policy for Performance Insights and attach it to a user.
- [Changing an AWS KMS policy for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.cmk-policy.html): Change an AWS KMS policy to allow or restrict access to Performance Insights.
- [Granting fine-grained access for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.dimensionAccess-policy.html): Control access to Performance Insights data with fine-grained access control.
- [Using tag-based access control for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.access-control.tag-based-policy.html): Control access to Performance Insights using tags inherited from DB instance

### [Analyzing metrics with the Performance Insights dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.html)

Analyze and troubleshoot performance issues for your database with the Performance Insights dashboard.

- [Overview of the dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.Components.html): The dashboard is the easiest way to interact with Performance Insights.
- [Accessing the dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.Opening.html): View the Amazon RDS Performance Insights dashboard in the AWS Management Console.
- [Analyzing DB load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.html): Find performance issues by analyzing DB load by wait events with the Performance Insights dashboard.

### [Analyzing database performance for a period of time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.html)

Troubleshoot database performance issues for a selected period of time by viewing the Performance Insights dashboard.

- [Creating a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.CreatingPerfAnlysisReport.html): Create a performance analysis report for a specific period in Performance Insights.
- [Viewing a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.ViewPerfAnalysisReport.html): View a performance analysis report for a specific period in Performance Insights.
- [Adding tags to a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html): Add tags to a performance analysis report when you create or view a report in Performance Insights.
- [Deleting a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.DeletePerfAnalysisReport.html): Delete a performance analysis report in Performance Insights.

### [Analyzing queries](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.html)

Analyze queries using the Top SQL tab in the Performance Insights dashboard.

### [Accessing more SQL text](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.SQLTextSize.html)

Access more SQL text for the top SQL statements in the Performance Insights dashboard.

- [Setting the SQL text limit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.SQLTextLimit.html): Set the text size for Amazon RDS for PostgreSQL in Performance Insights.
- [Viewing and downloading SQL text](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/view-download-text.html): View and download SQL text in the Performance Insights dashboard.
- [Viewing SQL statistics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.AnalyzingSQLLevel.html): View SQL statistics for the top SQL statements in the Performance Insights dashboard.
- [Analyzing Oracle PDBs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.TopPDB.html): Use the Top PDB tab in the Top dimensions table to find information about running queries in pluggable databases (PDBs) that are part of an Oracle Container DB (CDB).

### [Analyzing execution plans](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzingPlans.html)

Analyze execution plans using the Performance Insights dashboard.

- [Analyzing Oracle execution plans](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AccessPlans.html): Analyze Oracle execution plans using the Performance Insights dashboard.
- [Analyzing SQL Server execution plans](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AccessPlansSqlServer.html): Analyze SQL Server execution plans using the Performance Insights dashboard.
- [Viewing Performance Insights proactive recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.InsightsRecommendationViewDetails.html): Learn about viewing Performance Insights proactive recommendations in Amazon RDS.

### [Retrieving metrics with the Performance Insights API](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.API.html)

Retrieve metrics with the Performance Insights API.

- [Retrieving time-series metrics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.API.TimeSeries.html): Use the GetResourceMetrics operation to retrieve time-series metrics.
- [AWS CLI examples for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.API.Examples.html): In the following sections, learn more about the AWS Command Line Interface (AWS CLI) for Performance Insights and use AWS CLI examples.
- [Logging Performance Insights calls using AWS CloudTrail](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.CloudTrail.html): View a record of Performance Insights actions using CloudTrail.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/pi-vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your virtual private cloud (VPC) and Performance Insights API.
- [Analyzing performance with DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/devops-guru-for-rds.html): Amazon DevOpsÂ Guru for Amazon RDS applies machine learning to Performance Insights metrics for Amazon RDS databases.

### [Monitoring the OS with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

Monitor the operating system of your DB instance in real time with Enhanced Monitoring.

- [Setting up and enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Enabling.html): Create an IAM role for Enhanced Monitoring.
- [Viewing OS metrics in the RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.Viewing.html): View OS metrics in the Amazon RDS console.
- [Viewing OS metrics using CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.CloudWatchLogs.html): View OS metrics with CloudWatch Logs.

### [RDS metrics reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/metrics-reference.html)

Metrics for Amazon CloudWatch, Performance Insights, and Enhanced Monitoring for Amazon RDS.

- [CloudWatch metrics for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html): Metrics for Amazon CloudWatch for Amazon RDS.
- [CloudWatch dimensions for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/dimensions.html): A listing of the Amazon CloudWatch dimensions for Amazon RDS.
- [CloudWatch metrics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Cloudwatch.html): Metrics for Amazon CloudWatch for Performance Insights.
- [Counter metrics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights_Counters.html): Native and non-native counter metrics for Performance Insights.

### [SQL statistics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sql-statistics.html)

A reference for SQL statistics for Performance Insights.

- [SQL statistics for MariaDB and MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.html): Obtain digest, per-second, and per-call statistics for MariaDB and MySQL.
- [SQL statistics for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.Oracle.html): Collect per-second and per-call statistics for Oracle SQL queries.
- [SQL statistics for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.SQLServer.html): Collect per-second and per-call statistics for SQL Server SQL queries.
- [SQL statistics for RDS PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.html): Collect per-second and per-call digest statistics for RDS PostgreSQL queries.
- [OS metrics in Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring-Available-OS-Metrics.html): A reference for OS metrics for Enhanced Monitoring.


## [Monitoring events, logs, and database activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitor_Logs_Events.html)

- [Viewing logs, events, and streams in the Amazon RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/logs-events-streams-console.html): View the events, logs, and activity streams for an Amazon RDS database in the Amazon RDS console.

### [Monitoring RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-events.html)

An event indicates a change in an environment.

- [Viewing Amazon RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ListEvents.html): Get the date and time, source name and type, and message of an event related to your DB instance, snapshot, and security or parameter groups using Amazon RDS.

### [Working with Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html)

Get a notification by email, text message, or a call to an HTTP endpoint when an Amazon RDS event occurs using Amazon SNS.

- [Overview of Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.overview.html): Subscribe to event notifications when an Amazon RDS event occurs using Amazon SNS and see examples of Amazon RDS events.
- [Granting permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.GrantingPermissions.html): Grant Amazon RDS permissions to publish notifications to an Amazon Simple Notification Service (Amazon SNS) topic by attaching an AWS Identity and Access Management (IAM) policy to the destination topic.
- [Subscribing to Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Subscribing.html): Create an event notification subscription for an Amazon RDS event using Amazon SNS.
- [Amazon RDS event notification tags and attributes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.TagsAttributesForFiltering.html): Event notification details sent to SNS or EventBridge for filtering.
- [Listing Amazon RDS event notification subscriptions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.ListSubscription.html): List event notification subscriptions for Amazon RDS events.
- [Modifying an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Modifying.html): Modify event notification subscriptions for Amazon RDS events.
- [Adding a source identifier to an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.AddingSource.html): Add a source identifier to existing event notification subscriptions for Amazon RDS events.
- [Removing a source identifier from an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.RemovingSource.html): Remove a source identifier from existing event notification subscriptions for Amazon RDS events.
- [Listing the Amazon RDS event notification categories](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.ListingCategories.html): List event notification categories for Amazon RDS events.
- [Deleting an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Deleting.html): Delete an Amazon RDS event notification subscription.
- [Creating a rule that triggers on an Amazon RDS event](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-cloud-watch-events.html): Learn how to write rules to send Amazon RDS events to targets such as Amazon EventBridge.
- [Amazon RDS event categories and event messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html): Amazon RDS generates a significant number of events in categories that you can subscribe to using the Amazon RDS Console, AWS CLI, or the API.

### [Monitoring RDS logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.html)

View, download, and watch database logs by using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API.

- [Viewing and listing database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.Viewing.html): View database log files using the AWS Management Console, AWS CLI, or Amazon RDS API.
- [Downloading a database log file](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.Downloading.html): Download a database log file using the AWS Management Console or the AWS Command Line Interface (AWS CLI).
- [Watching a database log file](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.Watching.html): Monitor the contents of a log file by using the AWS Management Console.
- [Publishing to CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html): Learn how to publish logs from Amazon RDS to Amazon CloudWatch Logs.
- [Reading log file contents using REST](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DownloadCompleteDBLogFile.html): How to access log file contents using REST
- [Db2 database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.Db2.html): Access RDS for Db2 diagnostic logs and notify logs by using the Amazon RDS console, AWS CLI, or RDS API.

### [MariaDB database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MariaDB.html)

Learn how to monitor the MariaDB error log, slow query log, and the general log directly through the Amazon RDS console, API, AWS CLI, or AWS SDKs.

- [Accessing MariaDB error logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.Errorlog.html): Learn how to access the error logs for an RDS for MariaDB database.
- [Accessing the MariaDB slow query and general logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.Generallog.html): Learn how to access the slow query and general logs for an RDS for MariaDB database.
- [Publishing MariaDB logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.PublishtoCloudWatchLogs.html): Learn how to configure your RDS for MariaDB DB instance to publish log data to Amazon CloudWatch Logs.
- [Log rotation and retention for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.LogFileSize.html): Learn how Amazon RDS rotates and retains logs for RDS for MariaDB databases to maintain storage thresholds.
- [Managing table-based MariaDB logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.CommonDBATasks.Logs.html): Learn how to manage table-based logging for RDS for MariaDB databases.
- [Configuring MariaDB binary logging](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.BinaryFormat.html): Learn how to configure binary logging for RDS for MariaDB databases.
- [Accessing MariaDB binary logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.Binarylog.html): Learn how to access binary logs for an RDS for MariaDB database.
- [Enabling MariaDB binary log annotation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MariaDB.BinarylogAnnotation.html): Learn how to enable binary log annotation for an RDS for MariaDB database.
- [Microsoft SQL Server database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.SQLServer.html): Access SQL Server error logs, agent logs, and trace files by using the Amazon RDS console, AWS CLI, or RDS API.

### [MySQL database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.MySQL.html)

Monitor the MySQL error log, slow query log, and the general log directly through the Amazon RDS console, API, AWS CLI, or AWS SDKs.

- [Overview of RDS for MySQL database logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.LogFileSize.html): Learn about database logs that you can monitor for RDS for MySQL databases.
- [Publishing MySQL logs to Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQLDB.PublishtoCloudWatchLogs.html): Learn how to publish MySQL log data to Amazon CloudWatch Logs.
- [Sending MySQL log output to tables](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.Logs.html): Enable logging to tables in your DB instance and rotate log tables.
- [Configuring RDS for MySQL binary logging for Single-AZ databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.BinaryFormat.html): Learn how to configure binary logging for RDS for MySQL databases.
- [Configuring MySQL binary logging for Multi-AZ DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Binlog.MultiAZ.html): Binary logging in Amazon RDS for MySQL Multi-AZ DB clusters records all database changes to support replication, point-in-time recovery, and auditing.
- [Accessing MySQL binary logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.Binarylog.html): You can use the mysqlbinlog utility to download or stream binary logs from RDS for MySQL DB instances.
- [Oracle database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.Oracle.html): Access Oracle alert logs, audit files, and trace files by using the Amazon RDS console or API.

### [PostgreSQL database log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.html)

Configure the settings for the PostgreSQL log files in your RDS for PostgreSQL DB instance.

- [Parameters for logging](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.overview.parameter-groups.html): Control logging for your Aurora PostgreSQL DB cluster.
- [Turning on query logging](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_LogAccess.Concepts.PostgreSQL.Query_Logging.html): Turn on query logging to collect more information about your queries.
- [Monitoring RDS API calls in CloudTrail](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/logging-using-cloudtrail.html): Learn about logging Amazon RDS with AWS CloudTrail.

### [Monitoring RDS with Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.html)

Monitor the activity for a database by using the Database Activity Streams feature in Amazon RDS.

- [Configuring Oracle unified auditing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.configuring-auditing.html): Configure unified auditing for Oracle Database with database activity streams for RDS for Oracle.
- [Configuring SQL Server auditing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.configuring-auditing-SQLServer.html): Configure server auditing for SQL Server with database activity streams for Amazon RDS for Microsoft SQL Server.
- [Starting a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Enabling.html): When you start an activity stream for the DB instance, each database activity event that you configured in the audit policy generates an activity stream event.
- [Modifying a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Modifying.html): Modify the audit policy state of your database activity stream.
- [Getting the activity stream status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Status.html): You can get the status of an activity stream for your Amazon RDS database instance using the console or AWS CLI.
- [Stopping a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Disabling.html): You can stop an activity stream using the console or AWS CLI.

### [Monitoring activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.Monitoring.html)

Monitor Amazon RDS database activity streams with Amazon Kinesis.

- [Accessing an activity stream from Kinesis](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.KinesisAccess.html): Access an activity stream to monitor your database activity in real time with Amazon Kinesis.
- [Audit logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.AuditLog.html): Examples for and the structure of audit logs for database activity streams.
- [databaseActivityEventList JSON array](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.AuditLog.databaseActivityEventList.html): Activity events stored in the audit log payload.
- [Processing an activity stream using the SDK](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.CodeExample.html): Process a database activity stream using the AWS SDK.
- [IAM policy examples for activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DBActivityStreams.ManagingAccess.html): Examples of IAM policies to create, start, stop, and modify database activity streams.
- [Monitoring threats with GuardDuty RDS Protection](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/guard-duty-rds-protection.html): Amazon GuardDuty analyzes and profiles login events for potential access threats to your Amazon RDS databases.


## [Amazon RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html)

- [RDS Custom architecture](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-concept.html): Learn about the components of the Amazon RDS Custom architecture.

### [RDS Custom security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-security.html)

Learn about security in RDS Custom.

- [Secure your Amazon S3 bucket against the confused deputy problem](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-security.confused-deputy.html): Prevent the confused deputy problem for RDS Custom.
- [Rotating credentials for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-security.cred-rotation.html): Automatically rotate database user credentials for RDS Custom for Oracle.

### [Working with RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html)

Following, you can find instructions for creating, managing, and maintaining your RDS Custom for Oracle DB instances.

- [RDS Custom for Oracle workflow](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-concept.workflow.html): The following diagram shows the typical workflow for RDS Custom for Oracle.
- [Database architecture for Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle.db-architecture.html): RDS Custom for Oracle supports both the Oracle multitenant and non-multitenant architecture.
- [Feature availability and support for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-feature-support.html): In this topic, you can find a summary of the RDS Custom for Oracle feature availability and support for quick reference.
- [RDS Custom for Oracle requirements and limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.html): Find a summary of the Amazon RDS Custom for Oracle feature availability and requirements for quick reference.
- [Setting up your RDS Custom for Oracle environment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-orcl.html): Set up your environment for Amazon RDS Custom for Oracle.

### [Working with CEVs for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html)

Learn how to create and use custom engine versions for Amazon RDS Custom for Oracle.

- [Preparing to create a CEV](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.preparing.html): To create a CEV, access the installation files and patches that are stored in your Amazon S3 bucket for any of the following releases:
- [Creating a CEV](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.create.html): You can create a CEV using the AWS Management Console or the AWS CLI.
- [Modifying CEV status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.modify.html): You can modify a CEV using the AWS Management Console or the AWS CLI.
- [Viewing CEV details](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.view.html): View details about your CEV manifest using the AWS Management Console or AWS CLI for Amazon RDS Custom for Oracle.
- [Deleting a CEV](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.delete.html): You can delete a CEV using the AWS Management Console or the AWS CLI.

### [Configuring an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.html)

Create an Amazon RDS Custom for Oracle DB instance and then connect to it using Secure Shell (SSH) or AWS Systems Manager.

- [Connecting using Session Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.ssm.html): Connect to a RDS Custom DB instance using AWS Systems Manager Session Manager.
- [Logging in as SYS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating.sysdba.html): Log in to a RDS Custom DB instance as user SYS.

### [Managing an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.html)

Manage an Amazon RDS Custom DB instance.

- [Working with container databases (CDBs) in RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.multitenant.html): You can either create your RDS Custom for Oracle DB instance with the Oracle multitenant architecture (custom-oracle-ee-cdb or custom-oracle-se2-cdb engine type) or with the traditional non-CDB architecture (custom-oracle-ee or custom-oracle-se2 engine type).
- [Working with high availability features for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.ha.html): RDS Custom for Oracle provides built-in high availability through Multi-AZ deployments.
- [Customizing your RDS Custom environment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.customizing-env.html): RDS Custom for Oracle includes built-in features that allow you to customize your DB instance environment without pausing automation.
- [Modifying your DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.modifying.html): Modifying an RDS Custom for Oracle DB instance is similar to modifying an Amazon RDS DB instance.
- [Changing the character set of an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.character-set.html): RDS Custom for Oracle defaults to the character set US7ASCII.
- [Setting the NLS_LANG value in RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.nlslang.html): A locale is a set of information addressing linguistic and cultural requirements that corresponds to a given language and country.
- [Tagging RDS Custom for Oracle resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.tagging.html): You can tag RDS Custom resources as with Amazon RDS resources, but with some important differences:
- [Deleting an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.deleting.html)

### [Managing a Multi-AZ deployment for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz.html)

Learn how to create, modify, and manage Multi-AZ deployments for RDS Custom for Oracle to achieve high availability and automatic failover capabilities.

- [Prerequisites](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz-prerequisites.html): A Multi-AZ deployment for RDS Custom for Oracle is different from Multi-AZ for RDS for Oracle.
- [Converting Single-AZ to Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz-modify-single-to-multi.html): You can convert an existing multi-AZ compatible RDS Custom for Oracle instance from a Single-AZ deployment to a Multi-AZ deployment.
- [Converting Multi-AZ to Single-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz-modify-multi-to-single.html): You can modify an existing RDS Custom for Oracle DB instance from a Multi-AZ to a Single-AZ deployment.
- [OS customization](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz-os-customization.html): With RDS Custom for Oracle Multi-AZ deployments, you can customize the operating system and install third-party software on both primary and standby EC2 instances.
- [Deploy with CloudFormation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-multiaz-deployment.html): Automate your RDS Custom for Oracle deployment using the provided AWS CloudFormation template.

### [Working with RDS Custom for Oracle replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.html)

Create Oracle replicas for RDS Custom for Oracle DB instances.

- [Guidelines and limitations for replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.reqs-limitations.html): When you create RDS Custom for Oracle replicas, not all RDS Oracle replica options are supported.
- [Promoting a replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.promoting.html): Just as with RDS for Oracle, you can promote an RDS Custom for Oracle replica to a standalone DB instance.
- [Configuring a VPN tunnel between a primary and replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/cfo-standby-vpn-tunnel.html): A VPN tunnel is an encrypted connection between two or more devices over a network.

### [Backing up and restoring an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.html)

Learn how to back up and restore an RDS Custom for Oracle DB instance.

- [Creating an RDS Custom for Oracle snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.creating.html): RDS Custom for Oracle creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases.
- [Restoring from an RDS Custom for Oracle DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.restoring.html): When you restore an RDS Custom for Oracle DB instance, you provide the name of the DB snapshot and a name for the new instance.
- [Point-in-time recovery](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.pitr.html): Restore an RDS Custom for Oracle DB instance to a specific point in time.
- [Deleting an RDS Custom for Oracle snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.deleting.html): You can delete DB snapshots managed by RDS Custom for Oracle when you no longer need them.
- [Deleting RDS Custom for Oracle automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.deleting-backups.html): You can delete retained automated backups for RDS Custom for Oracle when they are no longer needed.

### [Working with option groups in RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-option-groups.html)

RDS Custom uses option groups to enable and configure additional features.

- [Oracle time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.timezone.html): To change the system time zone used by your RDS Custom for Oracle DB instance, use the time zone option.
- [Migrating to RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-migrating-oracle.html): Learn how to migrate an on-premises Oracle database to RDS Custom for Oracle.

### [Upgrading an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading.html)

Learn how to upgrade a DB instance for Amazon RDS Custom for Oracle.

- [Considerations for RDS Custom for Oracle database upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-considerations.html): If you plan to upgrade your database, consider the following:
- [Considerations for RDS Custom for Oracle OS upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-considerations-os.html): When you plan an OS upgrade, consider the following:
- [Viewing valid RDS Custom for Oracle upgrade targets](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-target.html): You can see existing CEVs on the Custom engine versions page in the AWS Management Console.
- [Upgrading an RDS Custom for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-modify.html): To upgrade your RDS Custom for Oracle DB instance, modify it to use a new CEV.
- [Viewing pending database upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-pending.html): You can see pending database upgrades for your Amazon RDS Custom DB instances by using the describe-db-instances or describe-pending-maintenance-actions AWS CLI command.
- [Upgrade failure](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-failure.html): If an RDS Custom DB instance upgrade fails, an RDS event is generated and the DB instance status becomes upgrade-failed.
- [Troubleshooting RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-troubleshooting.html): Learn how to troubleshoot issues with Amazon RDS Custom DB instances.
- [Known issues for RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-known-issues.html): Learn about known issues for Amazon RDS Custom DB instances.

### [Working with RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-sqlserver.html)

Following, you can find instructions for creating, managing, and maintaining your RDS Custom for SQL Server DB instances.

- [RDS Custom for SQL Server workflow](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver.workflow.html): The following diagram shows the typical workflow for RDS Custom for SQL Server.

### [RDS Custom for SQL Server requirements and limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.html)

Find a summary of the Amazon RDS Custom for SQL Server requirements and limitations for quick reference.

- [DB instance class support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits.instancesMS.html): Check if the DB instance class is supported in your Region by using the describe-orderable-db-instance-options command.
- [Collation and character support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.collation.html)
- [Local time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-reqs-limits-MS.TimeZone.html): The time zone of an RDS Custom for SQL Server DB instance is set by default.
- [Using a Service Master Key](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-features.smk.html): RDS Custom for SQL Server supports using a Service Master Key (SMK).
- [CDC support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-features.cdc.html)
- [Setting up your RDS Custom for SQL Server environment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-setup-sqlserver.html): Set up your environment for Amazon RDS Custom for SQL Server.
- [Bring Your Own Media with RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver.byom.html): RDS Custom for SQL Server supports two licensing models: License Included (LI) and Bring Your Own Media (BYOM).

### [Working with CEVs for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev-sqlserver.html)

Learn how to create and use custom engine versions for RDS Custom for SQL Server.

- [Preparing to create a CEV for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev-sqlserver.preparing.html): Learn how to prepare and create a custom engine version for RDS Custom for SQL Server.
- [Creating a CEV for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev-sqlserver.create.html): You can create a custom engine version (CEV) using the AWS Management Console or the AWS CLI.

### [Modifying a CEV for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev-sqlserver-modifying.html)

Learn how to modify a CEV for RDS Custom for SQL Server.

- [Modifying an RDS Custom for SQL Server DB instance to use a new CEV](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev-sqlserver-modifying-dbinstance.html): Modify an existing RDS Custom for SQL Server DB instance to use a different CEV.
- [Viewing CEV details for Amazon RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-viewing-sqlserver.html): You can view details about your CEV by using the AWS Management Console or the AWS CLI.
- [Deleting a CEV for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev-sqlserver-deleting.html): Learn how to delete a CEV for RDS Custom for SQL Server.

### [Creating and connecting to an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating-sqlserver.html)

Create a DB instance for Amazon RDS Custom for SQL Server, and then connect to it using AWS Systems Manager or Remote Desktop Protocol (RDP).

- [RDS Custom service-linked role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating-sqlserver.slr.html): A service-linked role gives Amazon RDS Custom access to resources in your AWS account.
- [Connecting to your RDS Custom DB instance using AWS Systems Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating-sqlserver.ssm.html): After you create your RDS Custom DB instance, you can connect to it using AWS Systems Manager Session Manager.
- [Connecting to your RDS Custom DB instance using RDP](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-creating-sqlserver.rdp.html): After you create your RDS Custom DB instance, you can connect to this instance using an RDP client.

### [Managing an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing-sqlserver.html)

Manage an Amazon RDS Custom for SQL Server DB instance.

- [Pausing and resuming RDS Custom automation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing-sqlserver.pausing.html): RDS Custom automatically provides monitoring and instance recovery for an RDS Custom for SQL Server DB instance.
- [Modifying an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing.modify-sqlserver.html): Modifying an RDS Custom for SQL Server DB instance is similar to doing this for Amazon RDS, but the changes that you can make are limited to the following:
- [Modifying the storage for an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing-sqlserver.storage-modify.html): Modifying storage for an RDS Custom for SQL Server DB instance is similar to modifying storage for an Amazon RDS DB instance, but you can only do the following:
- [Tagging RDS Custom for SQL Server resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing-sqlserver.tagging.html): You can tag RDS Custom resources as with Amazon RDS resources, but with some important differences:
- [Starting and stopping an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-managing-sqlserver.startstop.html): You can start and stop your RDS Custom for SQL Server DB instance.

### [Working with Microsoft Active Directory with RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.html)

Working with Active Directory with RDS Custom for SQL Server

- [Configure Self-Managed or On-premise AD](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.config-Self-Managed.html): To join your on-premise or self-managed Microsoft AD to your RDS Custom for SQL Server DB instance, your Active Domain must be configured as follows:
- [Configure Microsoft Active Directory using Directory Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.config-ADS.html): AWS Managed Microsoft AD creates a fully managed Microsoft Active Directory in AWS that is powered by Windows Server 2019 and operates at the 2012 R2 Forest and Domain functional levels.
- [Network configuration port rules](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.NWConfigPorts.html): Make sure that you have met the following network configurations:
- [Network Validation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.NWValidation.html): Before joining your RDS Custom instance to either self-managed or AWS Managed Microsoft AD, check the following from a EC2 instance in the same VPC as where you plan to launch the RDS Custom for SQL Server instance.
- [Setting up Windows Authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.settingUp.html): We recommend creating a dedicated OU and service credentials scoped to that OU for any AWS account that owns an RDS Custom for SQL Server DB instance joined to your AD domain.
- [Managing a DB instance in a Domain](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.ManagingDBI.html): You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its relationship with your domain.
- [Understanding Domain membership](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.Understanding.html): After you create or modify your DB instance, the instance becomes a member of the domain.
- [Troubleshooting Active Directory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-WinAuth.Troubleshoot.html): The following are issues you might encounter when you set up or modify an AD.

### [Managing a Multi-AZ deployment for RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-multiaz.html)

Managing a Multi-AZ deployment for RDS Custom for SQL Server

- [Prerequisites](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-multiaz.prerequisites.html): If you have an existing RDS Custom for SQL Server Single-AZ deployment, the following additional prerequisites are required before modifying it to a Multi-AZ deployment.
- [Modify Single-AZ to Multi-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-multiaz.modify-saztomaz.html): You can modify an existing RDS Custom for SQL Server DB instance from a Single-AZ deployment to a Multi-AZ deployment.
- [Modify Multi-AZ to Single-AZ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-multiaz.modify-maztosaz.html): You can modify an existing RDS Custom for SQL Server DB instance from a Multi-AZ to a Single-AZ deployment.
- [Failover process](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-sqlserver-multiaz.failover.html): If a planned or unplanned outage of your DB instance results from an infrastructure defect, Amazon RDS automatically switches to a standby replica in another Availability Zone if you have turned on Multi-AZ.

### [Backing up and restoring an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup-sqlserver.html)

Learn how to back up and restore an RDS Custom for SQL Server DB instance.

- [Creating an RDS Custom for SQL Server snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup-sqlserver.creating.html): RDS Custom for SQL Server creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases.
- [Restoring from an RDS Custom for SQL Server DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup-sqlserver.restoring.html): When you restore an RDS Custom for SQL Server DB instance, you provide the name of the DB snapshot and a name for the new instance.
- [Point-in-time recovery](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup.pitr-sqs.html): Restore an RDS Custom for SQL Server DB instance to a specific point in time.
- [Deleting an RDS Custom for SQL Server snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup-sqlserver.deleting.html): You can delete DB snapshots managed by RDS Custom for SQL Server when you no longer need them.
- [Deleting RDS Custom for SQL Server automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-backup-sqlserver.deleting-backups.html): You can delete retained automated backups for RDS Custom for SQL Server when they are no longer needed.
- [Copying an RDS Custom for SQL Server DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-copying-snapshot-sqlserver.html): Copying RDS Custom for SQL Server DB snapshots
- [Migrating an on-premises database to RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-migrating.html): Learn how to migrate an on-premises Microsoft SQL Server database to RDS Custom for SQL Server using native backup and restore.
- [Upgrading an RDS Custom for SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-upgrading-sqlserver.html): Learn how to upgrade a DB instance for RDS Custom for SQL Server.
- [Troubleshooting Amazon RDS Custom for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-troubleshooting-sqlserver.html): Learn how to troubleshoot issues with Amazon RDS Custom for SQL Server DB instances.


## [Amazon RDS on AWS Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.html)

- [Support for Amazon RDS features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.features.html): Describes the Amazon RDS features supported by Amazon RDS on AWS Outposts.
- [Supported DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.db-instance-classes.html): Find a list of the supported DB instance classes types for Amazon RDS on AWS Outposts.
- [Customer-owned IP addresses](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.coip.html): Learn about customer-owned IP addresses for Amazon RDS on AWS Outposts.
- [Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.maz.html): Work with Multi-AZ deployments for Amazon RDS on AWS Outposts.
- [Creating DB instances for RDS on Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.creating.html): Describes creating Amazon RDS on AWS Outposts DB instances.
- [Creating read replicas for RDS on Outposts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.rr.html): Create a read replica from a source Amazon RDS on AWS Outposts DB instance to scale out read operations.
- [Considerations for restoring DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-on-outposts.restoring.html): Choose where to store backups for restored DB instances on Amazon RDS on AWS Outposts.


## [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)

- [Planning where to use RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-planning.html): Determine which DB instances, clusters, and applications can benefit from using RDS Proxy.
- [RDS Proxy concepts and terminology](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.howitworks.html): Learn about how RDS Proxy can simplify connection management for your Amazon RDS DB instances.

### [Getting started with RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-setup.html)

Learn how to create an RDS Proxy and use it to connect to a database.

- [Set up a proxy network](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-network-prereqs.html): Learn how to set up network requirements for your proxy
- [Setting up database credentials](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-secrets-arns.html): RDS Proxy in Amazon RDS uses AWS Secrets Manager to store and manage database credentials securely.
- [Configuring IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-iam-setup.html): To set up AWS Identity and Access Management (IAM) authentication for RDS Proxy in Amazon RDS, create and configure an IAM policy that grants the necessary permissions.
- [Creating a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-creating.html): You can associate a proxy with an RDS for MariaDB, RDS for Microsoft SQL Server, RDS for MySQL, or RDS for PostgreSQL DB instance.
- [Viewing a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-viewing.html): After you create one or more RDS proxies, you can view and manage them in the AWS Management Console, the AWS CLI, or the RDS API.
- [Connecting through RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-connecting.html): The way to connect to an RDS DB instance through a proxy or by connecting to the database is generally the same.

### [Managing an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html)

Learn how to modify RDS Proxy and tune it to suit your needs.

- [Modifying an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-modifying-proxy.html): You can change specific settings associated with a proxy after you create the proxy.
- [Adding a database user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-new-db-user.html): In some cases, you might add a new database user to an RDS DB instance or cluster that's associated with a proxy.
- [Moving to end-to-end IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-iam-migration.html): If you currently use standard IAM authentication for RDS Proxy, where clients authenticate to the proxy using IAM but the proxy connects to the database using secrets, you can migrate to end-to-end IAM authentication where both client-to-proxy and proxy-to-database connections use IAM authentication.
- [RDS Proxy connection considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-connections.html)
- [Avoid pinning RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-pinning.html): Multiplexing is more efficient when database requests don't rely on state information from previous requests.
- [Deleting an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-deleting.html): You can delete a proxy when you no longer need it.

### [Working with RDS Proxy endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.html)

RDS Proxy endpoints provide flexible and efficient ways to manage database connections, which improves scalability, availability, and security.

- [Creating a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.CreatingEndpoint.html): To create a proxy endpoint, follow these instructions:
- [Viewing proxy endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.DescribingEndpoint.html): To view existing proxy endpoints, follow these instructions:
- [Modifying a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.ModifyingEndpoint.html): To modify your proxy endpoints, follow these instructions:
- [Deleting a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-endpoints.DeletingEndpoint.html): To delete an endpoint for your proxy, follow these instructions:
- [Monitoring RDS Proxy with CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.monitoring.html): You can monitor RDS Proxy by using Amazon CloudWatch.
- [Working with RDS Proxy events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.events.html): Find a list of Amazon RDS Proxy events that you can subscribe to and an example of an RDS Proxy event.
- [Troubleshooting RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.troubleshooting.html): Learn how to troubleshoot issues with RDS Proxy.
- [Using RDS Proxy with AWS CloudFormation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-cfn.html): See a sample AWS CloudFormation template for creating an RDS Proxy.


## [Zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html)

- [Getting started with zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.setting-up.html): Learn how to configure your RDS database for a zero-ETL integration.
- [Creating zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.creating.html): Learn how to create zero-ETL integrations with Amazon Redshift.
- [Creating zero-ETL integrations with an Amazon SageMaker lakehouse](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.creating-smlh.html): Learn how to create zero-ETL integrations with an Amazon SageMaker lakehouse.
- [Data filtering for zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.filtering.html): Learn how to filter the data that a zero-ETL integration sends to the analytics destination.
- [Adding and querying data](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.querying.html): Learn how to add data to a source for a zero-ETL integration with Amazon Redshift.
- [Viewing and monitoring zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.describingmonitoring.html): Learn how to view and monitor the details of a zero-ETL integration.
- [Modifying zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.modifying.html): Learn how to modify a zero-ETL integration.
- [Deleting zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.deleting.html): Learn how to delete zero-ETL integrations.
- [Troubleshooting zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.troubleshooting.html): You can check the state of a zero-ETL integration by querying the SVV_INTEGRATION system table in the analytics destination.


## [Db2 on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Db2.html)

### [Db2 overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-overview.html)

Learn about different aspects of Amazon RDS for Db2.

- [Db2 features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Concepts.FeatureSupport.html): Learn how Amazon RDS for Db2 supports the features and capabilities of Db2.

### [Db2 versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Concepts.VersionMgmt.html)

Learn about Amazon RDS for Db2 versions.

- [Upgrade Db2 minor versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Concepts.VersionMgmt.Supported.html): To see the current list of supported Db2 minor versions on RDS, use one of the following commands:
- [Db2 licensing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-licensing.html): Learn about the licensing options for Amazon RDS for Db2.
- [Db2 instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Concepts.General.InstanceClasses.html): Learn about supported DB instance classes for Amazon RDS for Db2.
- [Db2 default roles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-default-roles.html): Learn about Amazon RDS for Db2 managed roles.
- [Db2 parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-supported-parameters.html): Learn about the parameters available for Amazon RDS for Db2 DB instances.
- [EBCDIC collation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-ebcdic.html): Learn about EBCDIC collation support for Db2 databases running on Amazon RDS.
- [Db2 local time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-time-zone.html): Learn about local time zones for Amazon RDS for Db2.
- [DB instance prerequisites](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-db-instance-prereqs.html): Review important information before creating an Amazon RDS for Db2 DB instance.
- [Multiple Db2 databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-multiple-databases.html): Review important information about running multiple databases on an Amazon RDS for Db2 DB instance.

### [Connecting to your Db2 DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToDb2DBInstance.html)

Connect to an Amazon RDS for Db2 DB instance running the Db2 database engine using various tools.

- [Finding the endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-finding-instance-endpoint.html): Learn how to find the endpoint and port for your Amazon RDS for Db2 DB instance.
- [IBM Db2 CLP](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-connecting-with-clp-client.html): Learn how to connect to your Amazon RDS for Db2 DB instance with IBM Db2 CLP.
- [IBM CLPPlus](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-connecting-with-ibm-clpplus-client.html): Learn how to connect to your Amazon RDS for Db2 DB instance with IBM CLPPlus.
- [DBeaver](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-connecting-with-dbeaver.html): Learn how to connect to your Amazon RDS for Db2 DB instance with DBeaver.
- [IBM Db2 Data Management Console](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-connecting-with-ibm-data-management-console.html): Learn how to connect to your Amazon RDS for Db2 DB instance with IBM Db2 Data Management Console.
- [Security group considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-security-groups-considerations.html): Learn about important considerations for security groups with Amazon RDS for Db2 DB instances.

### [Securing Db2 connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Concepts.RestrictedDBAPrivileges.html)

Amazon RDS for Db2 supports ways to improve security for your RDS for Db2 DB instance.

- [Encrypting with SSL/TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Concepts.SSL.html): Using SSL/TLS, you can encrypt a connection between your application client and your Amazon RDS for Db2 DB instance.

### [Using Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-kerberos.html)

Learn about using Kerberos authentication with Amazon RDS for Db2 DB instances.

- [Setting up Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-kerberos-setting-up.html): You use AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to set up Kerberos authentication for an RDS for Db2 DB instance.
- [Connecting with Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-kerberos-connecting.html): Use the following procedure to connect to your Amazon RDS for Db2 DB instance with Kerberos authentication.

### [Administering your RDS for Db2 DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-administering-db-instance.html)

Learn about the common management tasks that you perform with an Amazon RDS for Db2 DB instance.

### [System tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-performing-common-system-tasks-db-instances.html)

Learn about the common system tasks you can perform for Amazon RDS for Db2 DB instances.

- [Granting and revoking privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-granting-revoking-privileges.html): Grant and revoke user permissions for RDS for Db2.
- [Attaching to the remote DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-attaching-to-remote.html): Attach to the remote RDS for Db2 DB instance.

### [Database tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-performing-common-database-tasks-db-instances.html)

Learn about the common DBA tasks that you can perform on Amazon RDS for Db2 DB instances.

- [Buffer pools](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-managing-buffer-pools.html): Create, alter, or drop buffer pools for your RDS for Db2 database.
- [Databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-managing-databases.html): Create, drop, or restore databases for your RDS for Db2 DB instance.
- [Tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-managing-tablespaces.html): Create, alter, rename, or drop tablespaces for your RDS for Db2 database.
- [Integrating with S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-s3-integration.html): Learn how to integrate an Amazon RDS for Db2 DB instance with Amazon S3.

### [Migrating data to RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-migrating-data-to-rds.html)

Learn about the different approaches you can take to migrate self-managed Db2 databases to Amazon RDS for Db2.

### [Migrating data with AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-migration-approaches.html)

Learn how you can migrate Db2 databases to Amazon RDS for Db2 by using AWS.

- [Linux to Linux](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-one-time-migration-linux.html): Learn about migrating Db2 databases to Amazon RDS for Db2 with minimal to no application outage or downtime.
- [Linux to Linux (near-zero downtime)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-near-zero-downtime-migration.html): Learn about migrating Db2 databases to Amazon RDS for Db2 with minimal to no application outage or downtime.
- [Linux to Linux (synchronous)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-synchronous-migration-linux.html): Learn about synchronous migrations from Linux to Linux environments for migrating Db2 databases to Amazon RDS for Db2.
- [AIX or Windows to Linux](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-one-time-migration-aix-windows-linux.html): Learn about using native Db2 tools for migrating AIX-based or Windows-based Db2 databases to Amazon RDS for Db2.
- [Migrating with Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-migration-load-from-s3.html): Learn about migrating Db2 databases to Amazon RDS for Db2 by loading data from Amazon S3.
- [Migrating with AWS DMS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-migration-amazon-dms.html): Learn about using AWS DMS to migrate Db2 databases to Amazon RDS for Db2.

### [Migrating data with native Db2 tools](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools.html)

Learn how you can migrate Db2 databases to Amazon RDS for Db2 with native db2 tools.

- [Connecting a client machine to RDS for Db2](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-connecting-client-rds.html): Learn about client machines used to migrate data to Amazon RDS for Db2 DB instances with native Db2 tools.
- [Copying database metadata from Db2 with db2look](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools-db2look.html): Learn how you can migrate Db2 databases to Amazon RDS for Db2 with db2look.
- [Importing from a client machine with IMPORT](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools-import.html): Learn how you can migrate Db2 databases to Amazon RDS for Db2 with the IMPORT command.
- [Importing from a client machine with LOAD](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools-load.html): Learn how you can migrate Db2 databases to Amazon RDS for Db2 with the LOAD command.
- [Importing from Db2 with INSERT](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools-insert.html): Learn how you can migrate Db2 databases to Amazon RDS for Db2 with the INSERT command.
- [Importing from Db2 with INGEST](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-native-db2-tools-ingest.html): Learn how you can migrate Db2 databases to Amazon RDS for Db2 with the INGEST utility.
- [Federation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-federation.html): Learn how to set up homogeneous and heterogeneous federation for Amazon RDS for Db2.

### [Working with Db2 replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replication.html)

Learn how to create manage replica databases in standby or read-only mode using Amazon RDS for Db2.

- [Requirements and considerations for Db2 replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-read-replicas.limitations.html): Review requirements and considerations before creating Amazon RDS for Db2 replicas.
- [Preparing to create a Db2 replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-read-replicas.Configuration.html): Learn about the required preparation tasks before creating an Amazon RDS for Db2 replica.
- [Creating a standby Db2 replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-read-replicas.creating-in-standby-mode.html): Learn how to create an Amazon RDS for Db2 replica in standby mode.
- [Modifying the replica mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-replicas-changing-replica-mode.html): Learn how to modify the replica mode for Amazon RDS for Db2 replicas.
- [Working with Db2 replica backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-read-replicas.backups.html): Learn how to create and restore backups of Amazon RDS for Db2 replicas.
- [Troubleshooting Db2 replication issues](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-troubleshooting-replicas.html): Review common issues with Amazon RDS for Db2 replicas and how to solve them.

### [Options for RDS for Db2 DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Options.html)

Learn about options and additional features available for Amazon RDS DB instances running Db2.

- [Db2 audit logging](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Db2.Options.Audit.html): Learn about Db2 audit logging.
- [External stored procedures](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-external-stored-procedures.html): Learn how to implement external stored procedures with your Amazon RDS for Db2 databases.
- [Known issues and limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-known-issues-limitations.html): Learn about known issues and limitations for working with Amazon RDS for Db2.

### [RDS for Db2 stored procedures](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-stored-procedures.html)

Learn about system stored procedures that are available for Amazon RDS for Db2 DB instances running the Db2 engine.

- [Considerations for stored procedures](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-stored-procedures-considerations.html): Review important information before using system stored procedures for Amazon RDS for Db2 DB instances running the Db2 engine.
- [Granting and revoking privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-sp-granting-revoking-privileges.html): Learn about stored procedures for granting and revoking privileges that are available for Amazon RDS for Db2 DB instances running the Db2 engine.
- [Audit policies](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-sp-managing-audit-policies.html): Learn about stored procedures for managing audit policies for Amazon RDS for Db2 DB instances running the Db2 engine.
- [Buffer pools](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-sp-managing-buffer-pools.html): Learn about stored procedures for managing buffer pools that are available for Amazon RDS for Db2 DB instances running the Db2 engine.
- [Databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-sp-managing-databases.html): Learn about stored procedures for managing databases that are available for Amazon RDS for Db2 DB instances running the Db2 engine.
- [Storage access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-sp-managing-storage-access.html): Learn about stored procedures for managing storage access that are available for Amazon RDS DB instances running the RDS for Db2 DB engine.
- [Tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-sp-managing-tablespaces.html): Learn about stored procedures for managing tablespaces that are available for Amazon RDS for Db2 DB instances running the Db2 engine.
- [RDS for Db2 user-defined functions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-user-defined-functions.html): Learn about user-defined functions that are available for Amazon RDS DB instances running the Db2 database engine.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/db2-troubleshooting.html): Review troubleshooting for issues with Amazon RDS for Db2.


## [MariaDB on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.html)

### [MariaDB feature support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.FeatureSupport.html)

Learn how Amazon RDS for MariaDB supports the features and capabilities of MariaDB.

- [Supported storage engines](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.Storage.html): Learn about supported storage engines for RDS for MariaDB databases.
- [Cache warming](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.XtraDBCacheWarming.html): Learn about cache warming for RDS for MariaDB databases.
- [Features not supported](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.FeatureNonSupport.html): Learn about MariaDB features that aren't supported with RDS for MariaDB databases.
- [MariaDB versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.VersionMgmt.html): Learn about Amazon RDS for MariaDB versions.

### [Connecting to a DB instance running MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMariaDBInstance.html)

Connect to a DB instance running the MariaDB database engine.

- [Finding the connection information](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMariaDBInstance.EndpointAndPort.html): Find the connection information to connect to a MariaDB DB instance.
- [Connecting from the command-line client](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMariaDBInstance.CLI.html): Connect to a RDS for MariaDB DB instance with the MySQL command-line client.
- [Connecting with the AWS drivers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Connecting.Drivers.html): Connect to your RDS for MariaDB DB instance with the AWS JDBC Driver and the AWS Python Driver.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMariaDBInstance.Troubleshooting.html): Troubleshoot issues with RDS for MariaDB connections.

### [Securing MariaDB connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/securing-mariadb-connections.html)

Manage the security of your RDS for MariaDB DB instances.

- [MariaDB security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.UsersAndPrivileges.html): Overview of security for MariaDB DB instances.
- [Password validation plugins](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.PasswordValidationPlugins.html): Learn how to enable and disable the password validation plugins for MariaDB.

### [Encrypting with SSL/TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-ssl-connections.html)

Use a parameter to require SSL/TLS for MariaDB DB instance connections.

- [SSL/TLS support for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.SSLSupport.html): Use SSL/TLS encryption to securely connect applications to MariaDB DB instances on Amazon RDS.
- [Requiring SSL/TLS for users](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB-ssl-connections.require-ssl-users.html): Enforce secure connections to your MariaDB DB instance with the require_secure_transport parameter.
- [Requiring SSL/TLS for all connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-ssl-connections.require-ssl.html): Enforce secure connections to your MariaDB DB instance with the require_secure_transport parameter.
- [Connecting with SSL/TLS from CLI](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMariaDBInstanceSSL.CLI.html): Connect to your MySQL DB instance using SSL/TLS encryption from the MySQL command-line client.
- [Using new SSL/TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-mariadb.html): Update applications that connect to an RDS for MariaDB DB instance for SSL/TLS certificate rotation.
- [Improving query performance with RDS Optimized Reads](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-optimized-reads-mariadb.html): Learn how to achieve faster query processing for RDS for MariaDB with Amazon RDS Optimized Reads.
- [Improving write performance with RDS Optimized Writes for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-optimized-writes-mariadb.html): Learn how to improve the performance of write transactions with Amazon RDS Optimized Writes for MariaDB

### [Upgrades of the MariaDB DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.html)

Learn how to upgrade an Amazon RDS DB instance running MariaDB.

- [MariaDB version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.VersionID.html): Learn about MySQL version numbers in RDS for MariaDB databases.
- [RDS version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.rds.version.html): Learn about RDS version numbers in RDS for MariaDB databases.
- [Major version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.Major.html): Learn about major version upgrades for RDS for MariaDB databases.
- [Automatic minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.Minor.html): Learn about automatic minor version upgrades for RDS for MariaDB databases.
- [Upgrading with reduced downtime](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.ReducedDowntime.html): Learn how to reduce downtime when upgrading an RDS for MariaDB database by using a read replica.
- [Monitoring with events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MariaDB.Monitoring.html): Learn how to monitor RDS for MariaDB engine upgrades with events.

### [Upgrading a MariaDB DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-upgrade-snapshot.html)

How to upgrade a DB snapshot for RDS for MariaDB.

- [Upgrade options for unsupported engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-upgrade-snapshot.upgrade-options.html): Upgrade options for DB snapshot with unsupported engine versions for RDS for MariaDB.

### [Importing data into an RDS for MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Procedural.Importing.html)

Learn different methods for importing data into an Amazon RDS for MariaDB DB instance.

- [Importing data considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Procedural.Importing.Advanced.html): Read about important information to consider when important data into MariaDB.
- [Importing data from an external database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-importing-data-external-database.html): Import MariaDB database data to Amazon RDS DB instances using the mysqldump or mariadb-dump utility for efficient data transfer and backup operations.
- [Importing data with reduced downtime](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-importing-data-reduced-downtime.html): Import data from an external MariaDB database to Amazon RDS while minimizing application downtime and network costs.
- [Importing data from any source](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mariadb-importing-data-any-source.html): Migrate MariaDB databases to Amazon RDS by transferring data from on-premises, cloud, or existing Amazon RDS DB instances using backup files or replication.

### [MariaDB replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.html)

Learn how to replicate with read replicas and external sources when you use Amazon RDS for MariaDB.

### [MariaDB read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.html)

Learn about configuring and working with read replicas on Amazon RDS for MariaDB.

- [Configuring replication filters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.html): Use replication filters to specify which databases and tables to replicate with a read replica.
- [Configuring delayed replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.DelayReplication.html): Use delayed replication to delay replication from the source to the read replica.
- [Updating read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.Updates.html): Update read replicas for your RDS for MySQL database.
- [Multi-AZ read replica deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.MultiAZ.html): Create a read replica as a Multi-AZ DB instance.
- [Cascading read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.Cascading.html): Scale reads without adding overhead to your source DB instance with cascading read replicas.
- [Monitoring replication lag](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.Monitor.html): Monitor replication lag for RDS for MariaDB read replicas.
- [Starting and stopping replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MariaDB.Replication.ReadReplicas.StartStop.html): Start and stop replication with RDS for MariaDB read replicas.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Troubleshooting.MariaDB.html): Troubleshoot problems with RDS for MariaDB replication.
- [Configuring GTID-based replication with an external source instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Procedural.Replication.GTID.html): Set up replication based on global transaction identifiers (GTIDs) from an external MariaDB instance of version 10.0.24 or higher into an Amazon RDS for MariaDB DB instance.
- [Configuring binary log file position replication with an external source instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.External.ReplMariaDB.html): Replicate data from an external MariaDB or MySQL DB instance with an Amazon RDS for MariaDB or Amazon RDS for MySQL DB instance.
- [Options for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Options.html): Learn about options and additional features available for Amazon RDS instances running the MariaDB DB engine.
- [Parameters for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.Parameters.html): Learn about the parameters available for RDS for MariaDB DB instances.
- [Migrating data from a MySQL DB snapshot to a MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Migrate_MariaDB.html): Learn about migrating data from a MySQL DB snapshot to a MariaDB DB instance in Amazon RDS.

### [MariaDB on Amazon RDS SQL reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MariaDB.SQLRef.html)

Learn about system stored procedures that are available for Amazon RDS instances running the MariaDB DB engine.

- [mysql.rds_replica_status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_replica_status.html): Shows the replication status of a MariaDB read replica.
- [mysql.rds_set_external_master_gtid](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_set_external_master_gtid.html): Configures GTID-based replication from an instance of MariaDB running external to Amazon RDS to a MariaDB DB instance.
- [mysql.rds_kill_query_id](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_kill_query_id.html): Ends a query running against the MariaDB server.
- [mysql.rds_execute_operation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_execute_operation.html): Executes specific InnoDB operations to manage buffer pool states and temporary tablespace.
- [Local time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MariaDB.Concepts.LocalTimeZone.html): Learn about working with local time zones for RDS for MariaDB DB instances.
- [Known issues and limitations for MariaDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MariaDB.Limitations.html): Learn about the limitations for using the RDS for MariaDB database engine.


## [Microsoft SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html)

- [DB instance class support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.InstanceClasses.html): The computation and memory capacity of a DB instance is determined by its DB instance class.

### [Optimize CPU](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.OptimizeCPU.html)

With RDS for SQL Server, you can use Optimize CPU by specifying processor features to configure the vCPU count on your DB instance while maintaining the same memory and IOPS.

- [DB instance class support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.OptimizeCPU.Support.html): RDS for SQL Server supports Optimize CPU beginning with the 7th Generation instance class type.
- [Set CPU cores and threads](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.OptimizeCPU.Enabling.html): You can configure the number of CPU cores and threads per core for the DB instance class when you perform the following operations:

### [Security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.FeatureSupport.UnsupportedRoles.html)

The Microsoft SQL Server database engine uses role-based security.

- [Using SSL with a SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.SSL.Using.html): Use SSL to connect to your Amazon RDS DB Instance running Microsoft SQL Server.
- [Configuring SQL Server security protocols and ciphers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Ciphers.html): You can turn certain security protocols and ciphers on and off using DB parameters.
- [Updating applications for new SSL/TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-sqlserver.html): Update applications that connect to an Amazon RDS for Microsoft SQL Server DB instance for SSL/TLS certificate rotation.
- [Version support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.VersionSupport.html): You can specify any currently supported Microsoft SQL Server version when creating a new DB instance.

### [Feature support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.FeatureSupport.html)

The supported SQL Server versions on Amazon RDS include the following features.

- [CDC support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.CDC.html): Amazon RDS supports change data capture (CDC) for your DB instances running Microsoft SQL Server.
- [Unsupported and limited feature support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.FeatureNonSupport.html): The following Microsoft SQL Server features aren't supported on Amazon RDS:
- [Functions and stored procedures](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.StoredProcedures.html): Following, you can find a list of the Amazon RDS functions and stored procedures that help automate SQL Server tasks.
- [Local time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.TimeZone.html): The time zone of an Amazon RDS DB instance running Microsoft SQL Server is set by default.
- [Licensing SQL Server on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.Licensing.html): Learn about licensing for an Amazon RDS DB instance for Microsoft SQL Server.

### [Connecting to a DB instance running SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html)

Connect to a DB instance running the Microsoft SQL Server database engine using the Microsoft SQL Server command line tools.

- [Connecting to your DB instance with SSMS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.SSMS.html): In this procedure, you connect to your sample DB instance by using Microsoft SQL Server Management Studio (SSMS).
- [Connecting to your DB instance with SQL Workbench/J](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.JDBC.html): This example shows how to connect to a DB instance running the Microsoft SQL Server database engine by using the SQL Workbench/J database tool.
- [Security group considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.Security.html): To connect to your DB instance, your DB instance must be associated with a security group.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.Troubleshooting.html): The following table shows error messages that you might encounter when you attempt to connect to your SQL Server DB instance.

### [SQL Server Developer Edition](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.html)

Learn how to create and use SQL Server Developer Edition database instances on Amazon RDS.

- [Preparing a CEV](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.preparing.html)
- [Creating a custom engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.creating-cev.html): A custom engine version (CEV) for RDS for SQL Server consists of your SQL Server Developer Edition installation media imported into Amazon RDS.
- [Creating a Developer Edition DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.creating-instance.html): Launching Developer Edition instance on RDS for SQL Server follows a two-step process: first create a CEV with create-custom-db-engine-version, Once your custom engine version is in the available state, you can create Amazon RDS database instances using the CEV.
- [Applying database minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.minor-version-upgrades.html): Apply minor version upgrades to RDS for SQL Server Developer Edition databases.
- [Viewing and managing custom engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.managing.html): To view all your RDS for SQL Server Developer Edition CEVs, use the describe-db-engine-versions command with the --engine input as sqlserver-dev-ee.
- [Troubleshooting SQL Server Developer Edition for RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/sqlserver-dev-edition.troubleshooting.html): The following table lists some common errors and corresponding solutions when working with SQL Server Developer Edition for RDS for SQL Server

### [Working with Active Directory with RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User.SQLServer.ActiveDirectoryWindowsAuth.html)

Working with Active Directory with RDS for SQL Server

### [Working with self-managed Active Directory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServer_SelfManagedActiveDirectory.html)

Working with self-managed Active Directory with Microsoft SQL Server on Amazon RDS.

- [Requirements](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServer_SelfManagedActiveDirectory.Requirements.html): Make sure you've met the following requirements before joining an RDS for SQL Server DB instance to your self-managed AD domain.
- [Setting up self-managed Active Directory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServer_SelfManagedActiveDirectory.SettingUp.html): To set up a self-managed AD, take the following steps.
- [Joining self-managed Active Directory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServer_SelfManagedActiveDirectory.Joining.html): To join your RDS for SQL Server DB instance to your self-managed AD, follow these steps:
- [Managing a DB instance in a self-managed Active Directory Domain](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServer_SelfManagedActiveDirectory.Managing.html): You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its relationship with your self-managed AD domain.
- [Troubleshooting self-managed Active Directory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServer_SelfManagedActiveDirectory.TroubleshootingSelfManagedActiveDirectory.html): The following are issues you might encounter when you set up or modify self-managed AD.

### [Working with AWS Managed Active Directory with RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.html)

Working with AWS Managed Active Directory and Windows Authentication with RDS for SQL Server.

- [Creating the endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.KerberosEndpoint.html): Kerberos-based authentication requires that the endpoint be the customer-specified host name, a period, and then the fully qualified domain name (FQDN).
- [Setting up Windows authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.SettingUp.html): You use AWS Directory Service for Microsoft Active Directory, also called AWS Managed Microsoft AD, to set up Windows Authentication for a SQL Server DB instance.
- [Managing a DB instance in a Domain](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.Managing.html): You can use the console, AWS CLI, or the Amazon RDS API to manage your DB instance and its relationship with your domain.
- [Connecting with Windows authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerWinAuth.Connecting.html): To connect to SQL Server with Windows Authentication, you must be logged into a domain-joined computer as a domain user.

### [Upgrades of the SQL Server DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.SQLServer.html)

Learn about upgrading an Amazon RDS DB instance running Microsoft SQL Server.

- [Major version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.SQLServer.Major.html): Learn about major version upgrades for RDS for SQL Server databases.
- [Upgrade considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.SQLServer.Considerations.html): Review considerations before you upgrade the engine version of an RDS for SQL Server database.
- [Testing an upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.SQLServer.UpgradeTesting.html): Learn how to test a major engine version upgrade for an RDS for SQL Server database.
- [Working with SQL Server storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DatabaseStorage.html): With RDS for SQL Server, you can attach up to three additional volumes to your RDS for SQL Server instance, each mapped to a unique Windows drive letter.

### [Importing and exporting SQL Server databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html)

Import data into and export data from your DB instance running Amazon RDS for Microsoft SQL Server by using native backup and restore.

- [Setting up](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Native.Enabling.html): To set up for native backup and restore, you need three components:
- [Using native backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Native.Using.html): After you have enabled and configured native backup and restore, you can start using it.
- [Compressing backup files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Native.Compression.html): To save space in your Amazon S3 bucket, you can compress your backup files.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Native.Troubleshooting.html): The following are issues you might encounter when you use native backup and restore.
- [Importing and exporting SQL Server data using other methods](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.Snapshots.html): Import data into your Amazon RDS DB instance running Microsoft SQL Server by using snapshots.
- [Using BCP from Linux](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.BCP.Linux.html): Import and export data to and from your RDS for SQL Server DB instance using the BCP (Bulk Copy Program) utility from a Linux environment.

### [SQL Server read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.html)

Work with Microsoft SQL Server read replicas in Amazon RDS.

- [Synchronizing database users and objects](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.ObjectSynchronization.html): Synchronize a SQL login from a primary DB instance to the read replica.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ReadReplicas.Troubleshooting.html): Troubleshoot problems with SQL Server read replicas.

### [Multi-AZ for RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.html)

Work with Multi-AZ deployments of RDS for SQL Server with Database Mirroring (DBM) or Always On Availability Groups (AGs).

- [Limitations, notes, and recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.Recommendations.html): The following are some limitations when working with Multi-AZ deployments on RDS for SQL Server DB instances:
- [Determining the location of the secondary](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.Location.html): You can determine the location of the secondary replica by using the AWS Management Console.
- [Migrating to Always On AGs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerMultiAZ.Migration.html): In version 14.00.3049.1 of Microsoft SQL Server Enterprise Edition, Always On Availability Groups (AGs) are enabled by default.

### [Additional features for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User.SQLServer.AdditionalFeatures.html)

Use additional features available for Amazon RDS instances running the Microsoft SQL Server DB engine.

### [Using password policy with a SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.PasswordPolicy.Using.html)

Use a password policy for your RDS for SQL Server DB instance.

- [Master login considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.PasswordPolicy.MasterLogin.html): Password policy considerations for the master login for your RDS for SQL Server DB instance.

### [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User.SQLServer.Options.S3-integration.html)

Integrate an Amazon RDS for SQL Server DB instance with Amazon S3

- [Integration prerequisites](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.preparing.html): Before you begin, find or create the S3 bucket that you want to use.
- [Enabling S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.enabling.html): In the following section, you can find how to enable Amazon S3 integration with Amazon RDS for SQL Server.
- [Transferring files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.html): You can use Amazon RDS stored procedures to download and upload files between Amazon S3 and your RDS DB instance.
- [Listing files on the RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.listing-files.html): To list the files available on the DB instance, use both a stored procedure and a function.
- [Deleting files on the RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.deleting-files.html): To delete the files available on the DB instance, use the Amazon RDS stored procedure msdb.dbo.rds_delete_from_filesystem with the following parameters.
- [Monitoring file transfers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.using.monitortasks.html): To track the status of your S3 integration task, call the rds_fn_task_status function.
- [Canceling a task](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.canceltasks.html): To cancel S3 integration tasks, use the msdb.dbo.rds_cancel_task stored procedure with the task_id parameter.
- [Disabling S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.S3-integration.disabling.html): Following, you can find how to disable Amazon S3 integration with Amazon RDS for SQL Server.

### [Using Database Mail](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.html)

Use Database Mail on Microsoft SQL Server DB instances running on Amazon RDS.

- [Enabling Database Mail](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.Enable.html): Use the following process to enable Database Mail for your DB instance:
- [Configuring Database Mail](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.Configure.html): You perform the following tasks to configure Database Mail:
- [Sending messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.Send.html): You use the sp_send_dbmail stored procedure to send email messages using Database Mail.
- [Viewing messages, logs, and attachments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.View.html): You use RDS stored procedures to view messages, event logs, and attachments.
- [Deleting messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.Delete.html): You use the rds_sysmail_delete_mailitems_sp stored procedure to delete messages.
- [Starting and stopping mail queue](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.DBMail.StartStop.html): Use the following instructions to start and stop the DB mail queue:
- [Instance store support for tempdb](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.InstanceStore.html): Use an instance store for the tempdb database on certain Microsoft SQL Server DB instances running on Amazon RDS.
- [Using extended events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.ExtendedEvents.html): Use extended events in Microsoft SQL Server for tracing events and actions with Amazon RDS for SQL Server.

### [Access to transaction log backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.html)

List and copy database transaction log files from RDS for SQL Server to Amazon S3 with access to transaction log backups.

- [Setting up access to transaction log backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.Enabling.html): To set up access to transaction log backups, complete the list of requirements in the section, and then run the rds_tlog_copy_setup stored procedure.
- [Listing available transaction log backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.Listing.html): With RDS for SQL Server, databases configured to use the full recovery model and a DB instance backup retention set to one or more days have transaction log backups automatically enabled.
- [Copying transaction log backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.Copying.html): To copy a set of available transaction log backups for an individual database to your Amazon S3 bucket, call the rds_tlog_backup_copy_to_S3 stored procedure.
- [Amazon S3 bucket folder and file structure](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.S3namingConvention.html): Transaction log backups have the following standard structure and naming convention within an Amazon S3 bucket:
- [Tracking the status of tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.TrackTaskStatus.html): To track the status of your copy tasks, call the rds_task_status stored procedure.
- [Canceling a task](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.CancelTask.html): To cancel a running task, call the rds_cancel_task stored procedure.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.Troubleshooting.html): The following are issues you might encounter when you use the stored procedures for access to transaction log backups.

### [Options for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.html)

Use options and additional features available for Amazon RDS instances running the Microsoft SQL Server DB engine.

- [Linked Servers with Oracle OLEDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.LinkedServers_Oracle_OLEDB.html): Learn about Amazon RDS support for Linked Servers with Oracle OLEDB.

### [Linked Servers with Teradata ODBC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerTeradata.html)

Support for linked servers with the Teradata ODBC driver on RDS for SQL Server lets you access external data sources on a Teradata database.

- [Activating Teradata](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerTeradata.Activate.html): Activate linked servers with Teradata by adding the ODBC_TERADATA option to your RDS for SQL Server DB instance.
- [Creating linked servers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerTeradata.CreateLinkedServers.html): To create a linked server with Teradata, run the following commands:
- [Deactivating Teradata servers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_SQLServerTeradata.Deactivate.html): To deactivate linked servers to Teradata, remove the ODBC_TERADATA option from its option group.
- [Native backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.BackupRestore.html): By using native backup and restore for SQL Server databases, you can create a differential or full backup of your on-premises database and store the backup files on Amazon S3.

### [Transparent Data Encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.TDE.html)

Learn how Amazon RDS supports using Transparent Data Encryption (TDE) to encrypt stored data on your DB instances running Microsoft SQL Server.

- [Encrypting data](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TDE.Encrypting.html): When the TDE option is added to an option group, Amazon RDS generates a certificate that's used in the encryption process.
- [Backing up and restoring TDE certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TDE.BackupRestoreRDS.html): RDS for SQL Server provides stored procedures for backing up, restoring, and dropping TDE certificates.
- [Backing up and restoring TDE certificates for on-premises databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TDE.BackupRestoreOnPrem.html): You can back up TDE certificates for on-premises databases, then later restore them to RDS for SQL Server.
- [Turning off TDE](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/TDE.Disabling.html): To turn off TDE for an RDS for SQL Server DB instance, first make sure that there are no encrypted objects left on the DB instance.

### [SQL Server Audit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.html)

Learn about Amazon RDS support for SQL Server Audit.

- [Adding SQL Server Audit to the DB instance options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.Adding.html): Enabling SQL Server Audit requires two steps: enabling the option on the DB instance, and enabling the feature inside SQL Server.
- [Using SQL Server Audit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.CreateAuditsAndSpecifications.html): You can control server audits, server audit specifications, and database audit specifications the same way that you control them for on-premises database servers.
- [Viewing audit logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.AuditRecords.html): Your audit logs are stored in D:\rdsdbdata\SQLAudit.
- [Configuring an S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.S3bucket.html): The audit log files are automatically uploaded from the DB instance to your S3 bucket.
- [Manually creating an IAM role for SQL Server Audit](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.Audit.IAM.html): Typically, when you create a new option, the AWS Management Console creates the IAM role and the IAM trust policy for you.

### [SQL Server Analysis Services](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.SSAS.html)

Learn about Amazon RDS support for Microsoft SQL Server Analysis Services.

- [Turning on SSAS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Enabling.html): Use the following process to turn on SSAS for your DB instance:
- [Deploying SSAS projects](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Deploy.html): On RDS, you can't deploy SSAS projects directly by using SQL Server Management Studio (SSMS).
- [Monitoring deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Monitor.html): To track the status of your deployment (or download) task, call the rds_fn_task_status function.
- [Using SSAS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Use.html): After deploying the SSAS project, you can directly process the OLAP database on SSMS.
- [Backing up an SSAS database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Backup.html): You can create SSAS database backup files only in the D:\S3 folder on the DB instance.
- [Restoring an SSAS database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Restore.html): Use the following stored procedure to restore an SSAS database from a backup.
- [Changing the SSAS mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.ChangeMode.html): You can change the mode in which SSAS runs, either Tabular or Multidimensional.
- [Turning off SSAS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Disable.html): To turn off SSAS, remove the SSAS option from its option group.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Trouble.html): You might encounter the following issues when using SSAS.

### [SQL Server Integration Services](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.SSIS.html)

Learn about Amazon RDS support for SQL Server Integration Services.

- [Administrative permissions on SSISDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSIS.Permissions.html): When the instance is created or modified with the SSIS option, the result is an SSISDB database with the ssis_admin and ssis_logreader roles granted to the master user.
- [Deploying SSIS projects](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSIS.Deploy.html): On RDS, you can't deploy SSIS projects directly by using SQL Server Management Studio (SSMS) or SSIS procedures.
- [Monitoring deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSIS.Monitor.html): To track the status of your deployment task, call the rds_fn_task_status function.
- [Using SSIS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSIS.Use.html): After deploying the SSIS project into the SSIS catalog, you can run packages directly from SSMS or schedule them by using SQL Server Agent.
- [Disable and drop SSIS database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSIS.DisableDrop.html): Use the following steps to disable or drop SSIS databases:

### [SQL Server Reporting Services](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.SSRS.html)

Use Microsoft SQL Server Reporting Services (SSRS) with Amazon RDS for Microsoft SQL Server to collect data from various data sources and present it in a way that's easily understandable and ready for analysis.

- [Turning on SSRS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Enabling.html): Use the following process to turn on SSRS for your DB instance:
- [Accessing the SSRS web portal](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Access.html): Use the following process to access the SSRS web portal:
- [Deploy and configure reports](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.DeployConfig.html): Use the following procedures to deploy reports to SSRS and configure the reporting data sources:
- [SSRS Email](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Email.html): SSRS includes the SSRS Email extension, which you can use to send reports to users.
- [Revoking system-level permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Access.Revoke.html): The RDS_SSRS_ROLE system role doesn't have sufficient permissions to delete system-level role assignments.
- [Monitoring task status](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.Monitor.html): To track the status of your granting or revoking task, call the rds_fn_task_status function.
- [Disabling and deleting SSRS databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSRS.DisableDelete.html): Use the following procedures to disable SSRS and delete SSRS databases:

### [Microsoft Distributed Transaction Coordinator](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.MSDTC.html)

Learn about Amazon RDS support for Microsoft Distributed Transaction Coordinator (MSDTC).

- [Enabling MSDTC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.MSDTC.Enabling.html): Use the following process to enable MSDTC for your DB instance:
- [Disabling MSDTC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.MSDTC.Disable.html): To disable MSDTC, remove the MSDTC option from its option group.
- [Troubleshooting MSDTC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.MSDTC.Troubleshooting.html): In some cases, you might have trouble establishing a connection between MSDTC running on a client computer and the MSDTC service running on an RDS for SQL Server DB instance.

### [SQL Server resource governor](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.ResourceGovernor.html)

Learn about Amazon RDS support for SQL Server Resource governor.

- [Enable resource governor](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ResourceGovernor.Enabling.html): Enable resource governor by adding the RESOURCE_GOVERNOR option to your RDS for SQL Server DB instance.
- [Use resource governor](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ResourceGovernor.Using.html): After adding the resource governor option to your option group, resource governor is not yet active at the database engine level.
- [Monitor resource governor instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ResourceGovernor.Monitoring.html): Resource Governor statistics are cumulative since the last server restart.
- [Disabling resource governor](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ResourceGovernor.Disabling.html): When you disable resource governor on RDS for SQL Server, the service stops managing workload resources.
- [Best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ResourceGovernor.BestPractices.html): To control resource consumption, RDS for SQL Server supports Microsoft SQL Server resource governor.

### [Common DBA tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.html)

Describes common DBA tasks for Amazon RDS-specific implementations running the Microsoft SQL Server database engine.

### [Accessing the tempdb database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.TempDB.html)

Access the tempdb database for Microsoft SQL Server DB instances running on Amazon RDS.

- [Modifying tempdb database options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.TempDB.Modifying.html): You can modify the database options on the tempdb database on your Amazon RDS DB instances.
- [Shrinking the tempdb database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.TempDB.Shrinking.html): There are two ways to shrink the tempdb database on your Amazon RDS DB instance.
- [TempDB configuration for Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.TempDB.MAZ.html): If your RDS for SQL Server DB instance is in a Multi-AZ Deployment using Database Mirroring (DBM) or Always On Availability Groups (AGs), keep in mind the following considerations for using the tempdb database.

### [Analyzing database workload with Database Engine Tuning Advisor](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Workload.html)

Database Engine Tuning Advisor is a client application provided by Microsoft that analyzes database workload and recommends an optimal set of indexes for your Microsoft SQL Server databases based on the kinds of queries you run.

- [Running a client-side trace on a SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.TuningAdvisor.ClientSide.html): To run a client-side trace on a SQL Server DB instance
- [Running a server-side trace on a SQL Server DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.TuningAdvisor.ServerSide.html): Writing scripts to create a server-side trace can be complex and is beyond the scope of this document.
- [Running Tuning Advisor with a trace](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.TuningAdvisor.Running.html): Once you create a trace, either as a local file or as a database table, you can then run Tuning Advisor against your DB instance.
- [Changing the db_owner to the rdsa account for your database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.ChangeDBowner.html): When you create or restore a database in an RDS for SQL Server DB instance, Amazon RDS sets the owner of the database to rdsa.
- [Managing collations and character sets](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Collation.html): Set the collations for Microsoft SQL Server DB instances running on Amazon RDS.
- [Creating a database user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.CreateUser.html): Create database users for Microsoft SQL Server DB instances running on Amazon RDS.
- [Determining a recovery model](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DatabaseRecovery.html): In Amazon RDS, the recovery model, retention period, and database status are linked.
- [Determining the last failover time](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.LastFailover.html): Determine the last failover time for your RDS for SQL Server database.
- [Troubleshoot PITR failures due to LSN gaps](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.PITR-LSN-Gaps.html): When attempting point-in-time-recovery (PITR) in RDS for SQL Server, you might encounter failures due to gaps in log sequence numbers (LSNs).
- [Deny or allow viewing database names](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.ManageView.html): The master user cannot set DENY VIEW ANY DATABASE TO LOGIN â¨ to hide databases from a user. â¨ To change this permission, use the following stored procedure instead:
- [Disabling fast inserts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DisableFastInserts.html): Starting with SQL Server 2016, fast inserts are enabled by default.
- [Dropping a SQL Server database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DropMirrorDB.html): You can drop a database on an Amazon RDS DB instance running Microsoft SQL Server in a Single-AZ or Multi-AZ deployment.
- [Renaming a Multi-AZ database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.RenamingDB.html): To rename a Microsoft SQL Server database instance that uses Multi-AZ, use the following procedure:
- [Resetting the db_owner role membership for master user](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.ResetPassword.html): If you lock your master user out of the db_owner role membership on your RDS for SQL Server database and no other database user can grant the membership, you can restore lost membership by modifying the DB instance master user password.
- [Restoring license-terminated DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.RestoreLTI.html): Microsoft has requested that some Amazon RDS customers who did not report their Microsoft License Mobility information terminate their DB instance.
- [Transitioning a database from OFFLINE to ONLINE](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.TransitionOnline.html): You can transition your Microsoft SQL Server database on an Amazon RDS DB instance from OFFLINE to ONLINE.
- [Using CDC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.CDC.html): Amazon RDS supports change data capture (CDC) for your DB instances running Microsoft SQL Server.

### [Using SQL Server Agent](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Agent.html)

With Amazon RDS, you can use SQL Server Agent on a DB instance running Microsoft SQL Server Enterprise Edition, Standard Edition, or Web Edition.

- [Agent roles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServerAgent.AgentRoles.html): RDS for SQL Server supports the following SQL Server Agent roles with different levels of permissions for managing jobs:
- [Adding a user to the SQLAgentUser role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServerAgent.AddUser.html): To allow an additional login or user to use SQL Server Agent, log in as the master user and do the following:
- [Deleting a SQL Server Agent job](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServerAgent.DeleteJob.html): You use the sp_delete_job stored procedure to delete SQL Server Agent jobs on Amazon RDS for Microsoft SQL Server.
- [Working with SQL Server logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Logs.html): Use the Amazon RDS console to view, watch, and download SQL Server Agent logs, Microsoft SQL Server error logs, and SQL Server Reporting Services (SSRS) logs.
- [Working with trace and dump files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.TraceFiles.html): This section describes working with trace files and dump files for your Amazon RDS DB instances running Microsoft SQL Server.


## [MySQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_MySQL.html)

- [MySQL feature support](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.FeatureSupport.html): Learn about MySQL feature support on Amazon RDS.
- [MySQL versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.VersionMgmt.html): Learn about Amazon RDS for MySQL versions.

### [Connecting to a DB instance running MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html)

Connect to a DB instance running the MySQL database engine.

- [Finding the connection information](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.EndpointAndPort.html): Find the connection information to connect to a RDS for MySQL DB instance.
- [Installing the command-line client](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-install-cli.html): Install the MySQL command-line client.
- [Connecting from the command-line client](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.CLI.html): Connect to a RDS for MySQL DB instance with the MySQL command-line client.
- [Connecting from MySQL Workbench](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.MySQLWorkbench.html): Connect to your RDS for MySQL DB instance from MySQL Workbench.
- [Connecting with the AWS drivers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Connecting.Drivers.html): Connect to your RDS for MySQL DB instance with the AWS JDBC Driver, the AWS Python Driver, and the AWS ODBC Driver for MySQL.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.Troubleshooting.html): Troubleshoot connection issues for RDS for MySQL.

### [Securing MySQL connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/securing-mysql-connections.html)

Manage the security of your Amazon RDS for MySQL DB instances.

- [Password validation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.PasswordValidationPlugin.html): MySQL provides the validate_password plugin for improved security.

### [Encrypting with SSL/TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-ssl-connections.html)

Secure MySQL DB instances with SSL/TLS encrypted client connections.

- [SSL/TLS support with MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.SSLSupport.html): Use SSL/TLS encryption to securely connect applications to MySQL DB instances on Amazon RDS.
- [Requiring SSL/TLS for users](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-ssl-connections.require-ssl-users.html): Enforce secure connections to your MySQL DB instance with the require_secure_transport parameter.
- [Requiring SSL/TLS for all connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-ssl-connections.require-ssl.html): Enforce secure connections to your MySQL DB instance with the require_secure_transport parameter.
- [Connecting with SSL/TLS from CLI](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstanceSSL.CLI.html): Connect to your MySQL DB instance using SSL/TLS encryption from the MySQL command-line client.
- [Using new SSL/TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-mysql.html): Update applications that connect to an RDS for MySQL DB instance for SSL/TLS certificate rotation.
- [Using Kerberos authentication for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-kerberos.html): Use Kerberos authentication to authenticate users when they connect to your MySQL DB instance.
- [Improving query performance with RDS Optimized Reads](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-optimized-reads.html): Learn how to achieve faster query processing for RDS for MySQL with Amazon RDS Optimized Reads.
- [Improving write performance with RDS Optimized Writes for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-optimized-writes.html): Learn how to improve the performance of write transactions with RDS Optimized Writes for MySQL.

### [Upgrades of the MySQL DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.html)

Upgrade an Amazon RDS DB instance running MySQL.

- [MySQL version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.VersionID.html): Learn about MySQL version numbers in RDS for MySQL databases.
- [RDS version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.rds.version.html): Learn about RDS version numbers in RDS for MySQL databases.
- [Major version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.Major.html): Learn about major version upgrades for RDS for MySQL databases.
- [Testing an upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.UpgradeTesting.html): Learn how to test a major engine version upgrade for an RDS for MySQL database.
- [Automatic minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.Minor.html): Learn about automatic minor version upgrades for RDS for MySQL databases.
- [Upgrading with reduced downtime](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.ReducedDowntime.html): Learn how to reduce downtime when upgrading an RDS for MySQL database by using a read replica.
- [Monitoring with events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.MySQL.Monitoring.html): Learn how to monitor RDS for MySQL database engine upgrades with events.

### [Upgrading a MySQL DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-upgrade-snapshot.html)

How to upgrade a DB snapshot for RDS for MySQL.

- [Upgrade options for unsupported engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-upgrade-snapshot.upgrade-options.html): Upgrade options for DB snapshot with unsupported engine versions for RDS for MySQL.

### [Importing data into an RDS for MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.Other.html)

Learn about importing data into an Amazon RDS for MySQL DB instance.

- [Importing data considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.Advanced.html): Read about important information to consider when important data into MySQL.
- [Restoring a backup into a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.html): Follow these instructions for restoring a backup to an Amazon RDS DB instance.
- [Importing data from an external database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-importing-data-external-database.html): Import MySQL database data to Amazon RDS DB instances using the mysqldump utility for efficient data transfer and backup operations.
- [Importing data with reduced downtime](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-importing-data-reduced-downtime.html): Import data from an external MySQL database to Amazon RDS while minimizing application downtime and network costs.
- [Importing data from any source](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-importing-data-any-source.html): Migrate MySQL databases to Amazon RDS by transferring data from on-premises, cloud, or existing Amazon RDS DB instances using backup files or replication.

### [MySQL replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.html)

Replicate with read replicas and external sources when you use Amazon RDS for MySQL.

### [MySQL read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.html)

Find information about working with read replicas on Amazon RDS for MySQL.

- [Configuring replication filters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.ReplicationFilters.html): Use replication filters to specify which databases and tables to replicate with a read replica.
- [Configuring delayed replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.DelayReplication.html): Use delayed replication to delay replication from the source to the read replica.
- [Updating read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.Updates.html): Update read replicas for your RDS for MySQL database.
- [Multi-AZ read replica deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.MultiAZ.html): Create a read replica as a Multi-AZ DB instance.
- [Cascading read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.Cascading.html): Scale reads without adding overhead to your source DB instance with cascading read replicas.
- [Monitoring replication lag](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.Monitor.html): Monitor replication lag for RDS for MySQL read replicas.
- [Starting and stopping replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_MySQL.Replication.ReadReplicas.StartStop.html): Start and stop replication with RDS for MySQL read replicas.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.Troubleshooting.html): Troubleshoot problems with RDS for MySQL replication.

### [GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.html)

Replicate data based on global transaction IDs (GTIDs) for Amazon RDS for MySQL.

- [Enabling GTID-based replication for new read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.configuring-new-read-replicas.html): Enable GTID-based replication when creating new read replicas.
- [GTID-based replication for existing read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.configuring-existing-read-replicas.html): Enable GTID-based replication for existing read replicas.
- [Disabling GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-replication-gtid.disabling.html): Disable GTID-based replication for existing read replicas for a MySQL DB Instance.
- [Configuring binary log file position replication with an external source instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Importing.External.Repl.html): Replicate data from an external MariaDB or MySQL DB instance with an RDS for MariaDB or RDS for MySQL DB instance.
- [Configuring multi-source replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-multi-source-replication.html): Learn how to configure and manage multi-source replication on RDS for MySQL.

### [Configuring active-active clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters.html)

Learn how to configure and manage active-active clusters for RDS for MySQL.

- [Limitations and considerations for active-active clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-considerations-limitations.html): Active-active clusters in Amazon RDS offer enhanced availability and scalability by distributing workloads across multiple instances.
- [Preparing for a cross-VPC active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-cross-vpc-prerequisites.html): You can configure an active-active cluster with Amazon RDS for MySQL DB instances in more than one VPC.
- [Required parameter settings for active-active clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-parameters.html): Configuring parameters for active-active clusters in Amazon RDS for MySQL is essential for maintaining consistent performance and operational stability.
- [Converting a DB instance to an active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-converting.html): The DB engine version of the DB instance you want to migrate to an active-active cluster must be one of the following versions:
- [Setting up a new active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-setting-up.html): Complete the following steps to set up an active-active cluster using new Amazon RDS for MySQL DB instances.
- [Adding a DB instance to an active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-adding.html): You can add a DB instance to an Amazon RDS for MySQL active-active cluster by restoring a DB snapshot or by restoring a DB instance to a point in time.
- [Monitoring active-active clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-monitoring.html): Monitoring active-active clusters in Amazon RDS for MySQL is crucial for tracking performance, replication integrity, and node synchronization.
- [Stopping Group Replication in an active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-stopping.html): You can stop Group Replication on a DB instance in an active-active cluster.
- [Renaming a DB instance in an active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-renaming.html): You can change the name of a DB instance in an active-active cluster.
- [Removing a DB instance from an active-active cluster](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-active-active-clusters-remove.html): When you remove a DB instance from an active-active cluster, it reverts to a standalone DB instance.
- [Exporting data from a MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Procedural.Exporting.NonRDSRepl.html): Export data using replication from an instance of MySQL running in Amazon RDS to an instance of MySQL running outside of RDS.

### [Options for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.html)

Learn about options and additional features available for Amazon RDS DB instances running MySQL.

- [MariaDB Audit Plugin](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.AuditPlugin.html): Amazon RDS offers an audit plugin for MySQL database instances based on the open source MariaDB Audit Plugin.
- [memcached](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Options.memcached.html): Amazon RDS supports using the memcached interface to InnoDB tables that was introduced in MySQL 5.6.
- [Parameters for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.Parameters.html): Learn about the parameters available for Amazon RDS for MySQL DB instances.

### [Common DBA tasks for MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.html)

Work with common DBA tasks for Amazon RDS-specific implementations running the MySQL database engine.

- [Role-based privilege model](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.privilege-model.html): Use the role-based privilege model to manage account permissions.
- [Dynamic privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.dynamic-privileges.html): Determine which dynamic privileges you can grant for your MySQL version.
- [Ending a session or query](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.End.html): Ed user sessions or queries on your RDS for MySQL DB instance.
- [Skipping the current replication error](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.SkipError.html): Skip an error on your RDS for MySQL read replica.
- [Improve crash recovery times](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.Tables.html): Migrate multiple tablespaces to the shared tablespace to improve crash recovery for RDS for MySQL.
- [Managing the Global Status History](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.GoSH.html): Monitor status variables using the Global Status History (GoSH) for your RDS for MySQL DB instance.
- [Configuring buffer pool size and redo log capacity](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.CommonDBATasks.Config.Size.8.4.html): Configure buffer pool size and redo log capacity for RDS for MySQL 8.4.
- [Local time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.Concepts.LocalTimeZone.html): Work with the local time zone for Amazon RDS for MySQL DB instances.
- [Known issues and limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/MySQL.KnownIssuesAndLimitations.html): Learn about known issues and limitations for working with Amazon RDS for MySQL.

### [RDS for MySQL stored procedures](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.MySQL.SQLRef.html)

Learn about system stored procedures that are available for Amazon RDS instances running the MySQL DB engine.

- [Collecting and maintaining the Global Status History](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-gsh.html): Amazon RDS provides a set of procedures that take snapshots of the values of status variables over time and write them to a table, along with any changes since the last snapshot.
- [Configuring, starting, and stopping binary log (binlog) replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-replicating.html): Learn about configuring, starting, and stopping binary log (binlog) replication in MySQL databases.
- [Ending a session or query](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-ending.html): The following stored procedures end a session or query.
- [Managing active-active clusters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-active-active-clusters.html): The following stored procedures set up and manage RDS for MySQL active-active clusters.
- [Managing multi-source replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-multi-source-replication.html): Learn about stored procedures for managing multi-source replication in RDS for MySQL databases.
- [Replicating transactions using GTIDs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-gtid.html): The following stored procedures control how transactions are replicated using global transaction identifiers (GTIDs) with RDS for MySQL.
- [Rotating the query logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-logging.html): The following stored procedures rotate MySQL logs to backup tables.
- [Setting and showing binary log configuration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-configuring.html): The following stored procedures set and show configuration parameters, such as for binary log file retention.
- [Warming the InnoDB cache](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql-stored-proc-warming.html): The following stored procedures save, load, or cancel loading the InnoDB buffer pool on RDS for MySQL DB instances.


## [Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.html)

### [Oracle overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.overview.html)

You can read the following sections to get an overview of RDS for Oracle.

- [Oracle features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.FeatureSupport.html): Amazon RDS for Oracle supports most of the features and capabilities of Oracle Database.
- [Oracle versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.database-versions.html): RDS for Oracle supports Oracle Database 19c and Oracle Database 21c.
- [Oracle licensing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.Licensing.html): Amazon RDS for Oracle has two licensing options: License Included (LI) and Bring Your Own License (BYOL).
- [Oracle users and privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.Privileges.html): When you create an Amazon RDS for Oracle DB instance, the default master user has most of the maximum user permissions on the DB instance.
- [Oracle instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.InstanceClasses.html): The computation and memory capacity of an RDS for Oracle DB instance is determined by its instance class.
- [Oracle database architecture](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-multi-architecture.html): For Oracle Database 19c and 21c, Amazon RDS supports a subset of multitenant architecture called the single-tenant configuration.
- [Oracle parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.FeatureSupport.Parameters.html): In Amazon RDS, you manage parameters using a DB parameter group.
- [Oracle character sets](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleCharacterSets.html): See the character sets that are supported for RDS for Oracle DB instances.
- [Oracle limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.limitations.html): In the following sections, you can find important limitations of using RDS for Oracle.

### [Connecting to your Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.html)

Connect to a DB instance running the Oracle database engine using the Oracle command line tools.

- [Finding the endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Endpoint.html): Each Amazon RDS DB instance has an endpoint, and each endpoint has the DNS name and port number for the DB instance.
- [SQL developer](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.SQLDeveloper.html): In this procedure, you connect to your DB instance by using Oracle SQL Developer.
- [SQL*Plus](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.SQLPlus.html): You can use a utility like SQL*Plus to connect to an Amazon RDS DB instance running Oracle.
- [Security group considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.Security.html): For you to connect to your DB instance, it must be associated with a security group that contains the necessary IP addresses and network configuration.
- [Dedicated and shared server processes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.SharedServer.html): Server processes handle user connections to an Oracle DB instance.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToOracleInstance.Troubleshooting.html): The following are issues you might encounter when you try to connect to your Oracle DB instance.
- [Modifying Oracle sqlnet.ora parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ModifyInstance.Oracle.sqlnet.html): Change the settings of sqlnet.ora parameters for a DB instance running the Oracle database engine.

### [Securing Oracle connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.RestrictedDBAPrivileges.html)

Amazon RDS for Oracle supports SSL/TLS encrypted connections and also the Oracle Native Network Encryption (NNE) option to encrypt connections between your application and your Oracle DB instance.

- [Encrypting with SSL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.SSL.html): Using SSL, you can encrypt a connection between your application client and your Oracle DB instance.
- [Using new SSL/TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-oracle.html): Update applications that connect to an Amazon RDS for Oracle DB instance for SSL/TLS certificate rotation.
- [Encrypting with NNE](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.NNE.html): Using NNE, you can encrypt a connection between your application client and your Oracle DB instance.

### [Configuring Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos.html)

Using Kerberos authentication with Amazon RDS for Oracle DB instances.

- [Region and version availability](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos-setting-up.RegionVersionAvailability.html): Feature availability and support varies across specific versions of each database engine, and across AWS Regions.
- [Setting up](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos-setting-up.html): Use AWS Directory Service for Microsoft Active Directory, also called AWS Managed Microsoft AD, to set up Kerberos authentication for an Oracle DB instance.
- [Managing a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos-managing.html): You can use the console, the CLI, or the RDS API to manage your DB instance and its relationship with your Microsoft Active Directory.
- [Connecting with Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-kerberos-connecting.html): This section assumes that you have set up your Oracle client as described in .
- [Configuring UTL_HTTP access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.ONA.html): Configure UTL_HTTP access using certificates and an Oracle wallet.

### [Working with CDBs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-multitenant.html)

You can create an RDS for Oracle DB instance as either a CDB or non-CDB.

- [Overview of CDBs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.CDBs.html): You can create container databases (CDBs) with RDS for Oracle and convert non-CDBs to CDBs.
- [Configuring a CDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cdb.configuring.html): Configuring a CDB is similar to configuring a non-CDB.
- [Backing up and restoring a CDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.single-tenant.snapshots.html): You can back up and restore your CDB using either RDS DB snapshots or Recovery Manager (RMAN).
- [Converting a non-CDB to a CDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cdb-converting.html): You can change the architecture of an Oracle database from the non-CDB architecture to the Oracle multitenant architecture, also called the CDB architecture, with the modify-db-instance command.
- [Converting single-tenant to multi-tenant](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-single-tenant-converting.html): You can modify the architecture of an RDS for Oracle CDB from the single-tenant configuration to the multi-tenant configuration.
- [Adding an RDS for Oracle tenant database to your CDB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cdb-configuring.adding.pdb.html): In the RDS for Oracle multi-tenant configuration, a tenant database is a PDB.
- [Modifying an RDS for Oracle tenant database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cdb-configuring.modifying.pdb.html): You can modify only the PDB name and the master user password of a tenant database in your CDB.
- [Deleting an RDS for Oracle tenant database from your CDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cdb-configuring.deleting.pdb.html): You can delete a tenant database (PDB) using the AWS Management Console, the AWS CLI, or the RDS API.
- [Viewing tenant database details](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cdb-configuring.describing.pdb.html): You can view details about a tenant database in the same way that you can for a non-CDB or CDB.
- [Upgrading your CDB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.single-tenant.upgrades.html): You can upgrade a CDB to a different Oracle Database release.

### [Administering your Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.html)

Learn about the common management tasks that you perform with an RDS for Oracle DB instance.

### [System tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.System.html)

Find a description of the Amazon RDSâspecific implementations of common system-level DBA tasks for your DB instances that run the Oracle database engine.

- [Disconnecting a session](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.DisconnectingSession.html): To disconnect the current session by ending the dedicated server process, use the Amazon RDS procedure rdsadmin.rdsadmin_util.disconnect.
- [Terminating a session](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.KillingSession.html): To terminate a session, use the Amazon RDS procedure rdsadmin.rdsadmin_util.kill.
- [Canceling a SQL statement in a session](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CancellingSQL.html): To cancel a SQL statement in a session, use the Amazon RDS procedure rdsadmin.rdsadmin_util.cancel.
- [Enabling and disabling restricted sessions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RestrictedSession.html): To enable and disable restricted sessions, use the Amazon RDS procedure rdsadmin.rdsadmin_util.restricted_session.
- [Flushing the shared pool](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.FlushingSharedPool.html): To flush the shared pool, use the Amazon RDS procedure rdsadmin.rdsadmin_util.flush_shared_pool.
- [Granting SELECT or EXECUTE privileges to SYS objects](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.TransferPrivileges.html): Usually you transfer privileges by using roles, which can contain many objects.
- [Revoking SELECT or EXECUTE privileges on SYS objects](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RevokePrivileges.html): To revoke privileges on a single object, use the Amazon RDS procedure rdsadmin.rdsadmin_util.revoke_sys_object.
- [RDS_X$ view tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.X-dollar.html): Create and drop SYS.RDS_X$ views on SYS.X$ fixed tables
- [Granting privileges to non-master users](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.PermissionsNonMasters.html): You can grant select privileges for many objects in the SYS schema by using the SELECT_CATALOG_ROLE role.

### [Creating custom functions to verify passwords](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CustomPassword.html)

You can create a custom password verification function in the following ways:

- [create_verify_function](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CustomPassword.Standard.html): You can create a custom function to verify passwords by using the Amazon RDS procedure rdsadmin.rdsadmin_password_verify.create_verify_function.
- [create_passthrough_verify_fcn](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CustomPassword.Custom.html): The create_passthrough_verify_fcn procedure is supported for all versions of RDS for Oracle.
- [Setting and unsetting system-level events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.SystemEvents.html): To set and unset diagnostic events at the session level, you can use the Oracle SQL statement ALTER SESSION SET EVENTS.

### [Database tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Database.html)

Find a description of the Amazon RDSâspecific implementations of common database-level DBA tasks for your DB instances that run the Oracle database engine.

- [Changing the global name of a database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RenamingGlobalName.html): To change the global name of a database, use the Amazon RDS procedure rdsadmin.rdsadmin_util.rename_global_name.
- [Working with Oracle tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.TablespacesAndDatafiles.html): You can use tablespaces with RDS for Oracle, which is a logical storage unit that stores the database's data.

### [Working with Oracle tempfiles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.using-tempfiles.html)

- [Dropping tempfiles on a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.dropping-tempfiles-replica.html): You can't drop an existing temporary tablespace on a read replica.
- [Resizing Oracle tablespaces and files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.ResizeTempSpaceReadReplica.html): By default, Oracle tablespaces are created with auto-extend turned on and no maximum size.
- [Moving data between volumes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.MovingDataBetweenVolumes.html): You can move data files and database objects between your primary and additional storage volumes.
- [Working with Oracle external tables](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.External_Tables.html): Oracle external tables are tables with data that is not in the database.
- [Checkpointing a database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CheckpointingDatabase.html): To checkpoint the database, use the Amazon RDS procedure rdsadmin.rdsadmin_util.checkpoint.
- [Setting distributed recovery](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.SettingDistributedRecovery.html): To set distributed recovery, use the Amazon RDS procedures rdsadmin.rdsadmin_util.enable_distr_recovery and disable_distr_recovery.
- [Setting the database time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.TimeZoneSupport.html): You can set the time zone of your Amazon RDS Oracle database in the following ways:
- [Working with AWR](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.AWR.html): To gather performance data and generate reports, Oracle recommends Automatic Workload Repository (AWR).
- [Adjusting database links for use with DB instances in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.DBLinks.html): To use Oracle database links with Amazon RDS DB instances inside the same virtual private cloud (VPC) or peered VPCs, the two DB instances should have a valid route between them.
- [Setting the default edition](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.DefaultEdition.html): You can redefine database objects in a private environment called an edition.
- [Enabling auditing for the SYS.AUD$ table](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.EnablingAuditing.html): To enable auditing on the database audit trail table SYS.AUD$, use the Amazon RDS procedure rdsadmin.rdsadmin_master_util.audit_all_sys_aud_table.
- [Disabling auditing for the SYS.AUD$ table](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.DisablingAuditing.html): To disable auditing on the database audit trail table SYS.AUD$, use the Amazon RDS procedure rdsadmin.rdsadmin_master_util.noaudit_all_sys_aud_table.
- [Cleaning up interrupted online index builds](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CleanupIndex.html): To clean up failed online index builds, use the Amazon RDS procedure rdsadmin.rdsadmin_dbms_repair.online_index_clean.
- [Skipping corrupt blocks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.SkippingCorruptBlocks.html): To skip corrupt blocks during index and table scans, use the rdsadmin.rdsadmin_dbms_repair package.
- [Setting the default displayed values for full redaction](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.FullRedaction.html): To change the default displayed values for full redaction on your Amazon RDS Oracle instance, use the Amazon RDS procedure rdsadmin.rdsadmin_util.dbms_redact_upd_full_rdct_val.

### [Log tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Log.html)

Find a description of the Amazon RDSâspecific implementations of common log-related DBA tasks for your DB instances that run the Oracle database engine.

- [Resizing online redo logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.ResizingRedoLogs.html): An Amazon RDS DB instance running Oracle starts with four online redo logs, 128 MB each.
- [Retaining archived redo logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RetainRedoLogs.html): You can retain archived redo logs locally on your DB instance for use with products like Oracle LogMiner (DBMS_LOGMNR).
- [Accessing transaction logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Log.Download.html): You might want to access your online and archived redo log files for mining with external tools such as GoldenGate, Attunity, Informatica, and others.
- [Downloading archived logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.download-redo-logs.html): You can download archived redo logs on your DB instance using the rdsadmin.rdsadmin_archive_log_download package.

### [RMAN tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RMAN.html)

Find a description of the Amazon RDSâspecific implementations of common Oracle Recovery Manager (RMAN) DBA tasks for your DB instances that run the Oracle database engine.

- [Prerequisites for RMAN backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.RMAN-requirements.html): Before backing up your database using the rdsadmin.rdsadmin_rman_util package, make sure that you meet the following prerequisites:
- [Common parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.CommonParameters.html): You can use procedures in the Amazon RDS package rdsadmin.rdsadmin_rman_util to perform tasks with RMAN.
- [Validating DB instance files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.ValidateDBFiles.html): You can use the Amazon RDS package rdsadmin.rdsadmin_rman_util to validate Amazon RDS for Oracle database files, such as data files, tablespaces, control files, and server parameter files (SPFILEs).
- [Controlling block change tracking](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BlockChangeTracking.html): Block changing tracking records changed blocks in a tracking file.
- [Crosschecking archived redo logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Crosscheck.html): You can crosscheck archived redo logs using the Amazon RDS procedure rdsadmin.rdsadmin_rman_util.crosscheck_archivelog.
- [Backing up archived redo log files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BackupArchivedLogs.html): You can use the Amazon RDS package rdsadmin.rdsadmin_rman_util to back up archived redo logs for an Amazon RDS Oracle DB instance.
- [Performing a full backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BackupDatabaseFull.html): You can perform a backup of all blocks of data files included in the backup using Amazon RDS procedure rdsadmin.rdsadmin_rman_util.backup_database_full.
- [Performing a full tenant database backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BackupTenantDatabaseFull.html): You can perform a backup of all data blocks included a tenant database in a container database (CDB).
- [Performing an incremental backup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BackupDatabaseIncremental.html): You can perform an incremental backup of your DB instance using the Amazon RDS procedure rdsadmin.rdsadmin_rman_util.backup_database_incremental.
- [Performing an incremental backup of a tenant database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BackupTenantDatabaseIncremental.html): You can perform an incremental backup of the current tenant database in your CDB.
- [Backing up a tablespace](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.BackupTablespace.html): You can back up a tablespace using the Amazon RDS procedure rdsadmin.rdsadmin_rman_util.backup_tablespace.
- [Backing up a control file](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.backup-control-file.html): You can back up a control file using the Amazon RDS procedure rdsadmin.rdsadmin_rman_util.backup_current_controlfile.
- [Performing block media recovery](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.block-media-recovery.html): You can recovery individual data blocks, known as block media recovery, using the Amazon RDS procedures rdsadmin.rdsadmin_rman_util.recover_datafile_block.
- [Oracle Scheduler tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Scheduler.html): Find a description of the Amazon RDSâspecific implementations of common Oracle Scheduler DBA tasks for your DB instances that run the Oracle database engine.
- [Diagnosing problems](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Diagnostics.html): Learn about the Amazon RDSâspecific implementations of common diagnostic tasks for your RDS for Oracle DB instances.

### [Other tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Misc.html)

Find a description of the Amazon RDSâspecific implementations of miscellaneous common DBA tasks for your DB instances that run the Oracle database engine.

### [Transporting tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util.html)

Use the Amazon RDS package rdsadmin.rdsadmin_transport_util to copy a set of tablespaces from an on-premises Oracle database to an RDS for Oracle DB instance.

- [Importing transported tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util_import_xtts_tablespaces.html): Use the procedure rdsadmin.rdsadmin_transport_util.import_xtts_tablespaces to restore tablespaces that you have previously exported from a source DB instance.
- [Importing transportable tablespace metadata](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util_import_xtts_metadata.html): Use the procedure rdsadmin.rdsadmin_transport_util.import_xtts_metadata to import transportable tablespace metadata into your RDS for Oracle DB instance.
- [Listing orphaned files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util_list_xtts_orphan_files.html): Use the rdsadmin.rdsadmin_transport_util.list_xtts_orphan_files procedure to list data files that were orphaned after a tablespace import.
- [Deleting orphaned data files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rdsadmin_transport_util_cleanup_incomplete_xtts_import.html): ABSTRACT_DESC

### [Working with Oracle storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_Oracle_AdditionalStorage.html)

Every RDS for Oracle instance has a primary storage volume.

- [Modify storage volumes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_Oracle_AdditionalStorage.ModifyStorageVolumes.html): You can add, modify, and remove additional storage volumes using the AWS Management Console or AWS CLI.
- [Backup and restore storage volumes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_Oracle_AdditionalStorage.BackupRestore.html): You can use automated backups and create a DB snapshot with your DB instance with additional storage volumes.
- [Use cases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/User_Oracle_AdditionalStorage.UseCases.html): Additional storage volumes support various database management scenarios.

### [Configuring advanced RDS for Oracle features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.advanced-features.html)

RDS for Oracle supports various advanced features, including HugePages, an instance store, and extended data types.

### [Configuring the instance store](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.advanced-features.instance-store.html)

Use an instance store for the temporary tablespaces and the Database Smart Flash Cache (the flash cache) on certain Oracle DB instances running on Amazon RDS.

- [Configuring an RDS for Oracle instance store](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.advanced-features.instance-store.configuring.html): By default, 100% of instance store space is allocated to the temporary tablespace.
- [Working with an instance store on an Oracle read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.advanced-features.instance-store.replicas.html): Read replicas support the flash cache and temporary tablespaces on an instance store.
- [Configuring a temporary tablespace group on an instance store and Amazon EBS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Oracle.advanced-features.instance-store.temp-ebs.html): You can configure a temporary tablespace group to include temporary tablespaces on both an instance store and Amazon EBS.
- [Turning on HugePages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.HugePages.html): Amazon RDS for Oracle supports Linux kernel HugePages for increased database scalability.
- [Turning on extended data types](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.ExtendedDataTypes.html): Amazon RDS for Oracle supports extended data types.

### [Importing data into Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.html)

Import data into an Oracle DB instance an Amazon RDS after backing up your database.

- [Importing using Oracle SQL Developer](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.SQLDeveloper.html): Oracle SQL Developer is a graphical Java tool distributed without cost by Oracle.
- [Migrating using Oracle transportable tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-migrating-tts.html): You can use the Oracle transportable tablespaces feature to copy a set of tablespaces from an on-premises Oracle database to an RDS for Oracle DB instance.
- [Importing using Oracle Data Pump](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.DataPump.html): Oracle Data Pump is a utility that allows you to export Oracle data to a dump file and import it into another Oracle database.
- [Importing using Oracle Export/Import](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.ExportImport.html): You might consider Oracle Export/Import utilities for migrations in the following conditions:
- [Importing using Oracle SQL*Loader](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.SQLLoader.html): You might consider Oracle SQL*Loader for large databases that contain a limited number of objects.
- [Migrating with Oracle materialized views](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Procedural.Importing.Materialized.html): To migrate large datasets efficiently, you can use Oracle materialized view replication.

### [Working with Oracle replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.html)

You can create a replica database in either mounted or read-only mode using Amazon RDS for Oracle.

- [Overview of Oracle replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.overview.html): An Oracle replica database is a physical copy of your primary database.
- [Requirements and considerations for Oracle replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.limitations.html): Before creating an Oracle replica, familiarize yourself with the following requirements and considerations.
- [Preparing to create an Oracle replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.Configuration.html): Before you can begin using your replica, perform the following tasks.
- [Creating a mounted Oracle replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.creating-in-mounted-mode.html): By default, Oracle replicas are read-only.
- [Modifying the replica mode](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.changing-replica-mode.html): To change the replica mode of an existing replica, use the console, AWS CLI, or RDS API.
- [Working with Oracle replica backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.backups.html): You can create and restore backups of an RDS for Oracle replica.

### [Performing an Oracle Data Guard switchover](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-replication-switchover.html)

A switchover is a role reversal between a primary database and a standby database.

- [Requirements for the Oracle Data Guard switchover](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-switchover.preparing.html): Before initiating the Oracle Data Guard switchover, make sure that your replication environment meets the following requirements:
- [Initiating the Oracle Data Guard switchover](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-switchover.initiating.html): You can switch over an RDS for Oracle read replica to the primary role, and the former primary DB instance to a replica role.
- [Monitoring the Oracle Data Guard switchover](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-switchover.monitoring.html): To check the status of your instances, use the AWS CLI command describe-db-instances.
- [Troubleshooting Oracle replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.troubleshooting.html): This section describes possible replication problems and solutions.
- [Redo transport compression](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-read-replicas.redo-transport-compression.html): Use RDS for Oracle redo transport compression to improve the replication performance between your primary DB instance and standby replicas.

### [Options for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.html)

Describes options and additional features available for Amazon RDS instances running the Oracle DB engine.

- [Overview of Oracle DB options](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.overview.html): To enable options for your Oracle database, add them to an option group, and then associate the option group with your DB instance.

### [Amazon S3 integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.html)

Integrate an Oracle DB instance an Amazon RDS with Amazon S3.

- [Configuring IAM permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.preparing.html): For RDS for Oracle to integrate with Amazon S3, your DB instance must have access to an Amazon S3 bucket.
- [Adding the option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.preparing.option-group.html): To integrate Amazon RDS for Oracle with Amazon S3, your DB instance must be associated with an option group that includes the S3_INTEGRATION option.
- [Transferring files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.using.html): To transfer files between an RDS for Oracle DB instance and an Amazon S3 bucket, you can use the Amazon RDS package rdsadmin_s3_tasks.
- [Removing the option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-s3-integration.removing.html): You can remove Amazon S3 integration option from a DB instance.

### [Oracle Application Express (APEX)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.APEX.html)

Amazon RDS supports Oracle Application Express (APEX) through the use of the APEX and APEX-DEV options.

- [Requirements and limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.APEX.Requirements.html): The following topic lists the requirements and limitations for Oracle APEX and ORDS.
- [Set up Oracle APEX and ORDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.APEX.settingUp.html): The following topic lists the steps required to set up Oracle APEX and ORDS
- [Configuring Oracle Rest Data Services (ORDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.APEX.ORDSConf.html): The following topic lists the configuration options for ORDS 21 and 22:
- [Upgrading and removing](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.APEX.UpgradeandRemove.html): To upgrade or remove Oracle APEX, follow the instructions in this topic:

### [Amazon EFS integration](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.html)

Integrate an Amazon RDS for Oracle DB instance with Amazon EFS.

- [Configuring network permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.network.html): For RDS for Oracle to integrate with Amazon EFS, make sure that your DB instance has network access to an EFS file system.
- [Configuring IAM permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.iam.html): By default, Amazon EFS integration feature doesn't use an IAM role: the USE_IAM_ROLE option setting is FALSE.
- [Adding the EFS option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.adding.html): To integrate Amazon RDS for Oracle with Amazon EFS, your DB instance must be associated with an option group that includes the EFS_INTEGRATION option.
- [Configuring EFS file system permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.file-system.html): By default, only the root user (UID 0) has read, write, and execute permissions for a newly created EFS file system.
- [Transferring files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.transferring.html): To transfer files between an RDS for Oracle instance and an Amazon EFS file system, create at least one Oracle directory and configure EFS file system permissions to control DB instance access.
- [Removing the option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.removing.html): The steps for removing the EFS_INTEGRATION option depend on whether you're removing the option from multiple DB instances or a single instance.
- [Troubleshooting Amazon EFS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.troubleshooting.html): Your RDS for Oracle DB instance monitors the connectivity to an Amazon EFS file system.
- [Java virtual machine (JVM)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-options-java.html): Work with Java virtual machine (JVM) support for Amazon RDS for Oracle DB instances.

### [Enterprise Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.OEM.html)

Amazon RDS supports Oracle Enterprise Manager (OEM).

- [OEM Database Express](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.OEM_DBControl.html): Amazon RDS supports Oracle Enterprise Manager Database Express (EM Express) through the use of the OEM option.
- [OEM Management Agent](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.OEMAgent.html): OEM Agent support for Amazon RDS for Oracle DB instances.
- [Label security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.OLS.html): Work with Oracle Label Security support for Amazon RDS for Oracle DB instances.
- [Locator](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.Locator.html): Oracle Locator support for Amazon RDS for Oracle DB instances.

### [Native network encryption (NNE)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.NetworkEncryption.html)

Work with Oracle NNE support for Amazon RDS for Oracle DB instances.

- [NATIVE_NETWORK_ENCRYPTION settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.NNE.Options.html): You can specify encryption requirements on both the server and the client.
- [Adding the option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.NNE.Add.html): The general process for adding the NATIVE_NETWORK_ENCRYPTION option to a DB instance is the following:
- [Setting NNE values in the sqlnet.ora](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.NNE.Using.html): With Oracle native network encryption, you can set network encryption on the server side and client side.
- [Modifying NATIVE_NETWORK_ENCRYPTION option settings](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.NNE.ModifySettings.html): After you enable the NATIVE_NETWORK_ENCRYPTION option, you can modify its settings.
- [Removing the option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.NNE.Remove.html): You can remove NNE from a DB instance.
- [OLAP](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.OLAP.html): Work with Oracle OLAP support for Amazon RDS for Oracle DB instances.

### [Secure Sockets Layer (SSL)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.html)

To enable SSL encryption for an RDS for Oracle DB instance, add the Oracle SSL option to the option group associated with the DB instance.

- [Adding the SSL option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.OptionGroup.html): To use SSL, your RDS for Oracle DB instance must be associated with an option group that includes the SSL option.
- [Configuring SQL*Plus](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.ClientConfiguration.html): Before you can connect to an RDS for Oracle DB instance that uses the Oracle SSL option, you must configure SQL*Plus before connecting.
- [Connecting using SSL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.Connecting.html): After you configure SQL*Plus to use SSL as described previously, you can connect to the RDS for Oracle DB instance with the SSL option.
- [Setting up an SSL connection over JDBC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.JDBC.html): To use an SSL connection over JDBC, you must create a keystore, trust the Amazon RDS root CA certificate, and use the code snippet specified following.
- [Enforcing a DN match](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.DNMatch.html): You can use the Oracle parameter SSL_SERVER_DN_MATCH to enforce that the distinguished name (DN) for the database server matches its service name.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.SSL.troubleshooting.html): You might query your database and receive the ORA-28860 error.
- [Spatial](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.Spatial.html): Oracle Spatial support for Amazon RDS for Oracle DB instances.
- [SQLT](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.SQLT.html): Work with SQLT support for Amazon RDS for Oracle DB instances.
- [Statspack](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Statspack.html): The Oracle Statspack option installs and enables the Oracle Statspack performance statistics feature.
- [Time zone](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone.html): To change the system time zone used by your Oracle DB instance, use the time zone option.

### [Time zone file autoupgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.html)

With the TIMEZONE_FILE_AUTOUPGRADE option, you can upgrade the current time zone file to the latest version on your RDS for Oracle DB instance.

- [Overview](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.tz-overview.html): An Oracle Database time zone file stores the following information:
- [DST update strategies](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.strategies.html): Upgrading your DB engine and adding the TIMEZONE_FILE_AUTOUPGRADE option to an option group are separate operations.
- [Downtime during the update](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.considerations.html): When RDS updates your time zone file, existing data that uses TIMESTAMP WITH TIME ZONE might change.
- [Preparing to update](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.preparing.html): A time zone file upgrade has two separate phases: prepare and upgrade.
- [Adding the option](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.adding.html): When you add the option to an option group, the option group is in one of the following states:
- [Checking your data](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.Timezone-file-autoupgrade.checking.html): We recommend that you check your data after you update the time zone file.
- [Transparent Data Encryption (TDE)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.AdvSecurity.html): Amazon RDS supports Oracle Transparent Data Encryption (TDE), a feature of the Oracle Advanced Security option available in Oracle Enterprise Edition.
- [UTL_MAIL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Options.UTLMAIL.html): Work with the UTL_MAIL package for Amazon RDS for Oracle DB instances.
- [XML DB](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.Options.XMLDB.html): Oracle XML DB adds native XML support to your DB instance.

### [Upgrading the Oracle DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.html)

Upgrade a DB instance running Amazon RDS for Oracle DB instance.

- [Overview of Oracle upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.Overview.html): Before upgrading your RDS for Oracle DB instance, familiarize yourself with the following concepts.
- [Major version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.Major.html): To perform a major version upgrade, modify the DB instance manually.
- [Minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.Minor.html): In RDS for Oracle, a minor version upgrade is an update to a major DB engine version.
- [Upgrade considerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.OGPG.html): Before you upgrade your Oracle instance, review the following information.
- [Testing an upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.UpgradeTesting.html): Before you upgrade your DB instance to a major version, thoroughly test your database and all applications that access the database for compatibility with the new version.
- [Upgrading an RDS for Oracle DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.Oracle.Upgrading.html)
- [Upgrading an Oracle DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.Oracle.html): Upgrade a snapshot for an Amazon RDS for Oracle database.

### [Tools and third-party software for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Resources.html)

Discusses tools and third-party software available for RDS for Oracle DB instances.

### [Using Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.html)

Use Oracle GoldenGate with an RDS for Oracle DB instance.

- [Oracle GoldenGate architecture](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.Overview.html): The Oracle GoldenGate architecture for use with Amazon RDS consists of the following decoupled modules:
- [Setting up Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.setting-up.html): Overview of using Oracle GoldenGate with an Amazon RDS for Oracle DB instance
- [Working with the EXTRACT and REPLICAT utilities](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.ExtractReplicat.html): The Oracle GoldenGate utilities EXTRACT and REPLICAT work together to keep the source and target databases in sync via incremental transaction replication using trail files.
- [Monitoring Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.Monitoring.html): When you use Oracle GoldenGate for replication, make sure that the Oracle GoldenGate process is up and running and the source and target databases are synchronized.
- [Troubleshooting Oracle GoldenGate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.OracleGoldenGate.Troubleshooting.html): This section explains the most common issues when using Oracle GoldenGate with Amazon RDS for Oracle.
- [Using the Oracle Repository Creation Utility](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Resources.RCU.html): Working with the Oracle Repository Creation Utility on Oracle on Amazon RDS
- [Configuring CMAN](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-cman.html): Configure Connection Manager (CMAN) on an Amazon EC2 instance.
- [Installing a Siebel database on Oracle on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Resources.Siebel.html): Describes how to install a Siebel Database on Oracle on Amazon RDS
- [Oracle Database engine releases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Oracle_Releases.html): Provides information about the Amazon RDS releases for the Oracle Database engine.


## [PostgreSQL on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html)

- [Common management tasks](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.CommonTasks.html): The following are the common management tasks you perform with an Amazon RDS for PostgreSQL DB instance, with links to relevant documentation for each task.

### [Working with the Database Preview environment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-the-database-preview-environment.html)

The PostgreSQL community continuously releases new PostgreSQL version and extensions, including beta versions.

- [Creating a new DB instance in the Database Preview environment](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/create-db-instance-in-preview-environment.html): Use the following procedure to create a DB instance in the preview environment.
- [PostgreSQL versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.DBVersions.html): Use available PostgreSQL versions on Amazon RDS.
- [RDS for PostgreSQL release process](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.ReleaseProcess.html): RDS for PostgreSQL delivers security fixes, performance improvements, and new features through incremental releases while maintaining minor version compatibility.
- [PostgreSQL extension versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.Extensions.html): RDS for PostgreSQL supports many PostgreSQL extensions.

### [PostgreSQL features](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.html)

Use common PostgreSQL features that are supported in RDS for PostgreSQL.

- [Custom data types and enumerations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.AlterEnum.html): Use PostgreSQL CREATE TYPE and CREATE TYPE as ENUM syntax.
- [Event triggers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.EventTriggers.html): Use event triggers for PostgreSQL DB instances on Amazon RDS.
- [Huge pages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.HugePages.html): Huge pages are a memory management feature that reduces overhead when a DB instance is working with large contiguous chunks of memory, such as that used by shared buffers.
- [Performing logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication.html): Use logical replication for a PostgreSQL database on Amazon RDS.
- [Configuring IAM authentication for logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.IAMLogicalReplication.html): Configure IAM database authentication for logical replication connections with PostgreSQL databases on Amazon RDS.
- [RAM disk for the stats_temp_directory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.RamDisk.html): You can use the RDS for PostgreSQL parameter rds.pg_stat_ramdisk_size to specify the system memory allocated to a RAM disk for storing the PostgreSQL stats_temp_directory.
- [Tablespaces](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.FeatureSupport.Tablespaces.html): RDS for PostgreSQL supports tablespaces for compatibility.
- [Collations for EBCDIC and other mainframe migrations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Collations.mainframe.migration.html): Learn about available collations for EBCDIC conversions that support AWS Mainframe Modernization.
- [Managing logical slot synchronization](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.slot.synchronization.html): Starting in community PostgreSQL 17, a new feature to automatically synchronize logical replication slots from primary to standby servers has been introduced through the parameter sync_replication_slots or the related function pg_sync_replication_slots(), which manually synchronizes slots on execution.

### [Connecting to a PostgreSQL instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html)

Connect to a DB instance running the PostgreSQL database engine working with Amazon RDS.

- [Using pgAdmin to connect to a RDS for PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.pgAdmin.html): You can use the open-source tool pgAdmin to connect to your RDS for PostgreSQL DB instance.
- [Using psql to connect to your RDS for PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.psql.html): You can use a local instance of the psql command line utility to connect to a RDS for PostgreSQL DB instance.
- [Connecting to RDS for PostgreSQL with the AWS JDBC Driver](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Connecting.JDBCDriver.html): The Amazon Web Services (AWS) JDBC Driver is designed as an advanced JDBC wrapper.
- [Connecting to RDS for PostgreSQL with the AWS Python Driver](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Connecting.PythonDriver.html): The Amazon Web Services (AWS) Python Driver is designed as an advanced Python wrapper.
- [Troubleshooting connections to your RDS for PostgreSQL instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.Troubleshooting.html)

### [Securing connections with SSL/TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.Security.html)

RDS for PostgreSQL supports Secure Socket Layer (SSL)/Transport Layer Security (TLS) encryption for PostgreSQL DB instances.

- [Using SSL with a PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html): Use SSL with an RDS for PostgreSQL DB instance.
- [Updating applications to use new SSL/TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ssl-certificate-rotation-postgresql.html): Update applications to use new Secure Socket Layer or Transport Layer Security (SSL/TLS) certificates for Amazon RDS for PostgreSQL DB instances.

### [Using Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-kerberos.html)

Use Kerberos authentication with Amazon RDS for PostgreSQL DB instances.

- [Setting up](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-kerberos-setting-up.html): You use AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to set up Kerberos authentication for a PostgreSQL DB instance.
- [Managing an RDS for PostgreSQL DB instance in an Active Directory domain](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-kerberos-managing.html): You can use the console, the CLI, or the RDS API to manage your DB instance and its relationship with your Microsoft Active Directory.
- [Connecting with Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-kerberos-connecting.html): You can connect to PostgreSQL with Kerberos authentication with the pgAdmin interface or with a command-line interface such as psql.
- [Using a custom DNS server for outbound network access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.CustomDNS.html): Learn how and why you might want to set up a custom DNS server for outbound network access with Amazon RDS for PostgreSQL.

### [Upgrades of the PostgreSQL DB engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.html)

Learn about upgrading an Amazon RDS DB instance running PostgreSQL.

- [PostgreSQL version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.VersionID.html): Learn about MySQL version numbers in RDS for PostgreSQL databases.
- [RDS version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.rds.version.html): Learn about RDS version numbers in RDS for PostgreSQL databases.
- [Choosing a major version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.MajorVersion.html): Learn how to choose a major version to upgrade your RDS for PostgreSQL database to.
- [How to perform a major version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.MajorVersion.Process.html): Learn how to perform a major version upgrade on an Amazon RDS for PostgreSQL database.
- [Automatic minor version upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.Minor.html): Learn about automatic minor version upgrades for RDS for PostgreSQL databases.
- [Upgrading PostgreSQL extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.ExtensionUpgrades.html): Learn how to upgrade PostgreSQL extensions in RDS for PostgreSQL databases.
- [Monitoring with events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBInstance.PostgreSQL.Monitoring.html): Learn how to monitor RDS for PostgreSQL database upgrades with events.
- [Upgrading a PostgreSQL DB snapshot engine version](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_UpgradeDBSnapshot.PostgreSQL.html): How to upgrade a DB snapshot PostgreSQL engine version.

### [RDS for PostgreSQL read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.html)

Scale reads for your Amazon RDS for PostgreSQL DB instance by adding read replicas.

- [Read replica configuration with PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Configuration.html): RDS for PostgreSQL uses PostgreSQL native streaming replication to create a read-only copy of a source DB instance.
- [Logical decoding on a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.LogicalDecoding.html): RDS for PostgreSQL supports logical replication from standbys with PostgreSQL 16.1.
- [Using cascading read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Cascading.html): As of version 14.1, RDS for PostgreSQL supports cascading read replicas.
- [Creating cross-Region cascading read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Xregion.html): RDS for PostgreSQL supports cross-Region cascading read replicas.
- [How replication works for different RDS for PostgreSQL versions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Mechanisms-versions.html): As discussed in , RDS for PostgreSQL uses PostgreSQL's native streaming replication protocol to send WAL data from the source DB instance.
- [Monitoring and tuning the replication process](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Monitor.html): We strongly recommend that you routinely monitor your RDS for PostgreSQL DB instance and read replicas.
- [Configuring delayed replication with RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rpg-delayed-replication.html): Learn how to use delayed replication in RDS for PostgreSQL to protect against data corruption, accidental data loss, and erroneous transactions by introducing a configurable time lag in the replication process.
- [Troubleshooting for RDS for PostgreSQL read replica](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.ReadReplicas.Troubleshooting.html): Following, you can find troubleshooting ideas for some common RDS for PostgreSQL read replica issues.
- [Improving query performance with RDS Optimized Reads](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.optimizedreads.html): Learn how to achieve faster query processing for RDS for PostgreSQL with Amazon RDS Optimized Reads.

### [Importing data into PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.html)

Importing Data into RDS for PostgreSQL

- [Importing a PostgreSQL database from an Amazon EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.EC2.html): Importing a PostgreSQL Database from an Amazon EC2 Instance
- [Using the \copy command to import data to a table on a PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Procedural.Importing.Copy.html): Use the \copy command to import data to a table on a PostgreSQL DB instance.

### [Importing data from Amazon S3 into RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.html)

Import data from Amazon Simple Storage Service into an RDS for PostgreSQL DB instance.

- [Installing the extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.InstallExtension.html): Before you can use Amazon S3 with your RDS for PostgreSQL DB instance, you need to install the aws_s3 extension.
- [Overview of importing data from Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.Overview.html)
- [Setting up access to an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.AccessPermission.html): To import data from an Amazon S3 file, give the RDS for PostgreSQL DB instance permission to access the Amazon S3 bucket containing the file.
- [Importing data from Amazon S3 to your RDS for PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.FileFormats.html): You import data from your Amazon S3 bucket by using the table_import_from_s3 function of the aws_s3 extension.
- [Function reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PostgreSQL.S3Import.Reference.html): Functions

### [Transporting PostgreSQL databases between DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.html)

Transport PostgreSQL databases between DB instances using PostgreSQL transportable databases.

- [Setting up a DB instance for transport](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.Setup.html): Before you begin, make sure that your RDS for PostgreSQL DB instances meet the following requirements:
- [Transporting a PostgreSQL database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.Transporting.html): After you complete the process described in , you can start the transport.
- [Transportable databases function reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.transport.import_from_server.html): The transport.import_from_server function transports a PostgreSQL database by importing it from a source DB instance to a destination DB instance.
- [Transportable databases parameter reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.TransportableDB.Parameters.html)

### [Exporting PostgreSQL data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-s3-export.html)

Export data from an RDS for PostgreSQL DB instance into Amazon S3.

- [Setting up access to an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-s3-export-access-bucket.html): To export data to Amazon S3, give your PostgreSQL DB instance permission to access the Amazon S3 bucket that the files are to go in.
- [Exporting query data using the aws_s3.query_export_to_s3 function](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-s3-export-examples.html): Export your PostgreSQL data to Amazon S3 by calling the function.
- [Function reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-s3-export-functions.html): Functions
- [Troubleshooting access to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-s3-export-troubleshoot.html): If you encounter connection problems when attempting to export data to Amazon S3, first confirm that the outbound access rules for the VPC security group associated with your DB instance permit network connectivity.

### [Invoking a Lambda function from RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL-Lambda.html)

Invoke an AWS Lambda function from an RDS for PostgreSQL DB instance.

- [Examples: Invoking Lambda functions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL-Lambda-examples.html): Following, you can find several examples of calling the function.
- [Lambda function error messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL-Lambda-errors.html): In the following list you can find information about error messages, with possible causes and solutions.
- [Lambda function and parameter reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL-Lambda-functions.html): Following is the reference for the functions and parameters to use for invoking Lambda with RDS for PostgreSQL.

### [Common DBA tasks for RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.html)

Learn how to perform some common DBA tasks on DB instances running the Amazon RDS for PostgreSQL database engine.

- [Collations supported in RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL-Collations.html): Collations supported in RDS for PostgreSQL.

### [Understanding PostgreSQL roles and permissions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.html)

Learn how to use PostgreSQL roles and permissions in your RDS for PostgreSQL DB instance

### [Understanding the rds_superuser role](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.rds_superuser.html)

In PostgreSQL, a role can define a user, a group, or a set of specific permissions granted to a group or user for various objects in the database.

- [Viewing roles and privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.View.html): Learn how to view predefined roles and their privileges in your RDS for PostgreSQL DB instance.
- [Controlling user access to PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Access.html): Control user access to the PostgreSQL database.
- [Delegating and controlling user password management](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.RestrictPasswordMgmt.html): Delegating and controlling user password management by using the rds_password role.
- [Using SCRAM for PostgreSQL password encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_Password_Encryption_configuration.html): Using SCRAM on your RDS for PostgreSQL DB instance
- [Dead connection handling in PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.html): Learn how to manage dead connections in PostgreSQL and configure TCP keepalive parameters for optimal connection handling.

### [Working with PostgreSQL autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.html)

Learn how PostgreSQL autovacuum works with Amazon RDS for PostgreSQL and how to use it.

- [Determining if the tables in your database need vacuuming](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.NeedVacuuming.html): You can use the following query to show the number of unfrozen transactions in a database.
- [Determining which tables are currently eligible for autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.EligibleTables.html): Often, it is one or two tables in need of vacuuming.
- [Determining if autovacuum is currently running and for how long](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AutovacuumRunning.html): If you need to manually vacuum a table, make sure to determine if autovacuum is currently running.
- [Performing a manual vacuum freeze](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.VacuumFreeze.html): You might want to perform a manual vacuum on a table that has a vacuum process already running.
- [Reindexing a table when autovacuum is running](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.Reindexing.html): If an index has become corrupt, autovacuum continues to process the table and fails.
- [Managing autovacuum with large indexes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.html): As part of its operation, autovacuum performs several vacuum phases while running on a table.
- [Other parameters that affect autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.OtherParms.html): The following query shows the values of some of the parameters that directly affect autovacuum and its behavior.
- [Setting table-level autovacuum parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.TableParameters.html): You can set autovacuum-related storage parameters at a table level, which can be better than altering the behavior of the entire database.
- [Logging autovacuum and vacuum activities](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.Logging.html): Information about autovacuum activities is sent to the postgresql.log based on the level specified in the rds.force_autovacuum_logging_level parameter.
- [Understanding the behavior of autovacuum with invalid databases](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/appendix.postgresql.commondbatasks.autovacuumbehavior.html): Understand the behavior of autovacuum with invalid databases.

### [Identifying vacuum blockers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.html)

Identify and resolve aggressive vacuum blockers in RDS for PostgreSQL.

- [Installing autovacuum monitoring tools](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Installation.html): Installing autovacuum monitoring and diagnostic tools in RDS for PostgreSQL
- [Functions of postgres_get_av_diag()](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Functions.html): Functions of postgres_get_av_diag() in RDS for PostgreSQL
- [Resolving identifiable vacuum blockers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Resolving_Identifiableblockers.html): Resolving vacuum blockers in RDS for PostgreSQL
- [Resolving unidentifiable vacuum blockers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Unidentifiable_blockers.html): Resolving unidentifiable vacuum blockers in RDS for PostgreSQL
- [Resolving vacuum performance issues](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Resolving_Performance.html): Resolving vacuum performance issues on RDS for PostgreSQL
- [Explanation of the NOTICE messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.NOTICE.html): Explanation of the NOTICE messages in RDS for PostgreSQL
- [Managing TOAST OID contention](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.html): Identify and manage TOAST OID contention issues in your PostgreSQL databases.

### [Managing temporary files with PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.ManagingTempFiles.html)

Managing temporary files with PostgreSQL

- [Viewing temporary file usage with Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.ManagingTempFiles.Example.html): You can use Performance Insights to view temporary file usage by turning on the metrics temp_bytes and temp_files.
- [Managing custom casts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.CustomCasts.html): Learn how to create and manage custom type casts using the rds_casts extension.
- [Working with parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Parameters.html): Learn how to use custom DB paramater groups to change settings on your RDS for PostgreSQL DB instance.

### [Tuning with wait events for RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.html)

Tune with wait events for Amazon RDS for PostgreSQL.

### [Essential concepts for RDS for PostgreSQL tuning](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.concepts.html)

Learn some essential concepts for RDS for PostgreSQL tuning.

- [RDS for PostgreSQL wait events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.concepts.waits.html): A wait event is an indication that the session is waiting for a resource.
- [RDS for PostgreSQL memory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.concepts.memory.html): RDS for PostgreSQL memory is divided into shared and local.
- [RDS for PostgreSQL processes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.concepts.processes.html): RDS for PostgreSQL uses multiple processes.
- [RDS for PostgreSQL wait events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning.concepts.summary.html): Find a table that lists the wait events for RDS for PostgreSQL that most commonly indicate performance problems, with most common causes and corrective actions.
- [Client:ClientRead](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.clientread.html): The Client:ClientRead event occurs when RDS for PostgreSQL is waiting to receive data from the client.
- [Client:ClientWrite](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.clientwrite.html): The Client:ClientWrite event occurs when RDS for PostgreSQL is waiting to write data to the client.
- [CPU](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.cpu.html): The CPU wait event occurs when a thread is active in CPU or is waiting for CPU.
- [IO:BufFileRead and IO:BufFileWrite](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.iobuffile.html): The IO:BufFileRead and IO:BufFileWrite events occur when RDS for PostgreSQL creates temporary files.
- [IO:DataFileRead](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.iodatafileread.html): The IO:DataFileRead event occurs in RDS for PostgreSQL when a connection waits on a backend process to read a required page from storage because the page isn't available in shared memory.
- [IO:WALWrite](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.iowalwrite.html): Indicates that RDS for PostgreSQL is waiting for the write-ahead log (WAL) buffers to be written to a WAL file.
- [IPC:parallel wait events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rpg-ipc-parallel.html): The IPC:BgWorkerShutdown, IPC:BgWorkerStartup, IPC:ExecuteGather, and IPC:ParallelFinish wait events indicate that a session is waiting for inter-process communication related to parallel query execution operations.
- [IPC:ProcArrayGroupUpdate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/apg-rpg-ipcprocarraygroup.html): The IPC:ProcArrayGroupUpdate event occurs when a session is waiting for the group leader to update the transaction status at the end of that operation.
- [Lock:advisory](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lockadvisory.html): The Lock:advisory event occurs when a PostgreSQL application uses a lock to coordinate activity across multiple sessions.
- [Lock:extend](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lockextend.html): The Lock:extend event occurs when a backend process is waiting to lock a relation to extend it while another process has a lock on that relation for the same purpose.
- [Lock:Relation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lockrelation.html): The Lock:Relation event occurs when a query is waiting to acquire a lock on a table or view that's currently locked by another transaction.
- [Lock:transactionid](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.locktransactionid.html): The Lock:transactionid event occurs when a transaction is waiting for a row-level lock.
- [Lock:tuple](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.locktuple.html): The Lock:tuple event for RDS for PostgreSQL occurs when a backend process is waiting to acquire a lock on a tuple.
- [LWLock:BufferMapping (LWLock:buffer_mapping)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lwl-buffer-mapping.html): This event occurs when a session is waiting to associate a data block with a buffer in the shared buffer pool.
- [LWLock:BufferIO (IPC:BufferIO)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lwlockbufferio.html): The LWLock:BufferIO event occurs when RDS for PostgreSQL or Aurora PostgreSQL is waiting for other processes to finish their I/O operations.
- [LWLock:buffer_content (BufferContent)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lwlockbuffercontent.html): The LWLock:buffer_content event occurs when a session is waiting to read or write a data page in memory while another session has that page locked for writing.
- [LWLock:lock_manager (LWLock:lockmanager)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lw-lock-manager.html): The LWLock:lock_manager wait event occurs when the RDS for PostgreSQL engine maintains the shared lock's memory area to allocate, check, and deallocate a lock when a fast path lock is not possible.
- [LWLock:pg_stat_statements](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/apg-rpg-lwlockpgstat.html): The LWLock:pg_stat_statements wait event occurs when the pg_stat_statements extension takes an exclusive lock on the hash table that tracks SQL statements.
- [LWLock:SubtransSLRU (LWLock:SubtransControlLock)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.lwlocksubtransslru.html): The LWLock:SubtransSLRU and LWLock:SubtransBuffer wait events indicate that a session is waiting to access the simple least-recently used (SLRU) cache for subtransaction information.
- [Timeout:PgSleep](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.timeoutpgsleep.html): The Timeout:PgSleep event occurs in RDS for PostgreSQL when a server process has called the pg_sleep function and is waiting for the sleep timeout to expire.
- [Timeout:VacuumDelay](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/wait-event.timeoutvacuumdelay.html): The Timeout:VacuumDelay event indicates that the cost limit for vacuum I/O has been exceeded and that the vacuum process has been put to sleep.
- [Tuning RDS for PostgreSQL with Amazon DevOpsÂ Guru proactive insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Tuning_proactive_insights.html): Tune your RDS for PostgreSQL DB instance by following the recommendations in your DevOpsÂ Guru proactive insights.

### [Using PostgreSQL extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.html)

Learn how you can install and configure various PostgreSQL extensions to work with Amazon RDS for PostgreSQL.

- [Using functions from orafce](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.orafce.html): Use functions from the orafce extension with Amazon RDS for PostgreSQL to work with Oracle and other commercial databases more easily.
- [Using Amazon RDS delegated extension support for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/RDS_delegated_ext.html): Using Amazon RDS delegated extension support for PostgreSQL, you can delegate the extension management to a user who need not be an rds_superuser.
- [Managing partitions with the pg_partman extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_Partitions.html): Create and manage Amazon RDS for PostgreSQL database table partitions using the pg_partman extension.

### [Using pgAudit to log database activity](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.html)

Learn how to use the pgAudit extension to create audit logs for your RDS for PostgreSQL DB instance per session or per object, and how to exclude or include by user or by database.

- [Setting up the pgAudit extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.basic-setup.html): To set up the pgAudit extension on your RDS for PostgreSQL DB instance , you first add pgAudit to the shared libraries on the custom DB parameter group for your RDS for PostgreSQL DB instance.
- [Auditing database objects](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.auditing.html): With pgAudit set up on your RDS for PostgreSQL DB instance and configured for your requirements, more detailed information is captured in the PostgreSQL log.
- [Excluding users or databases from audit logging](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.exclude-user-db.html): As discussed in , PostgreSQL logs consume storage space.
- [Reference for pgAudit extension parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.html): You can specify the level of detail that you want for your audit log by changing one or more of the parameters listed in this section.
- [Scheduling maintenance with the pg_cron extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_pg_cron.html): You can use the PostgreSQL pg_cron extension to schedule maintenance commands within a PostgreSQL database.

### [Using pglogical to synchronize data](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.html)

Use the pglogical extension for logical replication with your RDS for PostgreSQL DB instance.

- [Setting up the pglogical extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup.html): To set up the pglogical extension on your RDS for PostgreSQL DB instance , you add pglogical to the shared libraries on the custom DB parameter group for your RDS for PostgreSQL DB instance.
- [Setting up logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.setup-replication.html): The following procedure shows you how to start logical replication between two RDS for PostgreSQL DB instances.
- [Reestablishing logical replication after upgrading](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.recover-replication-after-upgrade.html): Before you can perform a major version upgrade of an RDS for PostgreSQL DB instance that's set up as a publisher node for logical replication, you must drop all replication slots, even those that aren't active.
- [Managing logical replication slots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.handle-slots.html): Before you can perform a major version upgrade on an RDS for PostgreSQL DB instance that's serving as a publisher node in a logical replication scenario, you must drop the replication slots on the instance.
- [Parameter reference for pglogical extension parameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.reference.html): In the table you can find parameters associated with the pglogical extension.

### [Using pgactive to create active-active replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.html)

Use the pgactive extension for active-active replication with your RDS for PostgreSQL DB instance.

- [Initializing the pgactive extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.basic-setup.html): To initialize the pgactive extension capability on your RDS for PostgreSQL DB instance, set the value of the rds.enable_pgactive parameter to 1 and then create the extension in the database.
- [Setting up active-active replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.setup-replication.html): The following procedure shows you how to start active-active replication between two RDS for PostgreSQL DB instances where pgactive is available.
- [Measuring replication lag among pgactive members](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.replicationlag.html): You can use the following query to view the replication lag among the pgactive members.
- [Configuring parameter settings for the pgactive extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.parameters.html): You can use the following query to view all the parameters associated with pgactive extension.
- [Understanding active-active conflicts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.replication.html): When you use pgactive in active-active mode, writing to the same tables from multiple nodes can create data conflicts.
- [Understanding the pgactive schema](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.schema.html): The pgactive schema manages active-active replication in RDS for PostgreSQL.
- [pgactive functions reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/pgactive-functions-reference.html): pgactive functions with their parameters, return values, and practical usage notes to help you effectively use them:
- [Handling conflicts in active-active replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.handle-conflicts.html): The pgactive extension works per database and not per cluster.
- [Handling sequences in active-active replication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pgactive.handle-sequences.html): An RDS for PostgreSQL DB instance with the pgactive extension uses two different sequence mechanisms to generate unique values.
- [Reducing bloat with the pg_repack extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.pg_repack.html): Reduce bloat from tables and indexes by using the pg_repack extension with Amazon RDS for PostgreSQL.
- [Upgrading and using PLV8](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.UpgradingPLv8.html): Learn how to upgrade PLV8 on Amazon RDS for PostgreSQL.
- [Using PL/Rust to write functions in the Rust language](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.Using.PL_Rust.html): PL/Rust is a trusted Rust language extension for PostgreSQL.
- [Managing spatial data with PostGIS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.PostGIS.html): Manage spatial data by installing and using the PostGIS extension with Amazon RDS for PostgreSQL.

### [Supported foreign data wrappers in Amazon RDS for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.foreign-data-wrappers.html)

Work with the supported foreign data wrappers for Amazon RDS for PostgreSQL.

- [Using the log_fdw extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.Extensions.log_fdw.html): Access the Amazon RDS for PostgreSQL DB instance DB log using SQL.
- [Using postgres_fdw to access external data](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-commondbatasks-fdw.html): You can access data in a table on a remote database server with the postgres_fdw extension.
- [Working with a MySQL database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-mysql-fdw.html): To access a MySQL-compatible database from your RDS for PostgreSQL DB instance, you can install and use the mysql_fdw extension.
- [Working with an Oracle database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-oracle-fdw.html): To access an Oracle database from your RDS for PostgreSQL DB instance you can install and use the oracle_fdw extension.
- [Working with a SQL Server database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/postgresql-tds-fdw.html): You can use the PostgreSQL tds_fdw extension to access databases that support the tabular data stream (TDS) protocol, such as Sybase and Microsoft SQL Server databases.

### [Working with Trusted Language Extensions for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension.html)

Trusted Language Extensions for PostgreSQL is an open source development kit for building PostgreSQL extensions.

- [Terminology](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-terminology.html): To help you better understand Trusted Language Extensions, view the following glossary for terms used in this topic.
- [Requirements for using Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-requirements.html): The following are requirements for setting up and using the TLE development kit.
- [Setting up Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-setting-up.html): The following steps assume that your RDS for PostgreSQL DB instance is associated with a custom DB parameter group.
- [Overview of Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension.overview.html): Trusted Language Extensions for PostgreSQL is a PostgreSQL extension that you install in your RDS for PostgreSQL DB instance in the same way that you set up other PostgreSQL extensions.
- [Creating TLE extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-creating-TLE-extensions.html): You can install any extensions that you create with TLE in any RDS for PostgreSQL DB instance that has the pg_tle extension installed.
- [Dropping your TLE extensions from a database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-creating-TLE-extensions.dropping-TLEs.html): You can drop your TLE extensions by using the DROP EXTENSION command in the same way that you do for other PostgreSQL extensions.
- [Uninstalling Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-uninstalling-pg_tle-devkit.html): If you no longer want to create your own TLE extensions using TLE, you can drop the pg_tle extension and remove all artifacts.
- [Using PostgreSQL hooks with your TLE extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension.overview.tles-and-hooks.html): A hook is a callback mechanism available in PostgreSQL that allows developers to call custom functions or other routines during regular database operations.
- [Using Custom Data Types in Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-custom-data-type.html): PostgreSQL supports commands to register new base types (also known as scalar types) for efficiently handling complex data structures in your database.
- [Function reference for Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-functions-reference.html): Reference documentation for the management functions available in the Trusted Language Extensions development kit.
- [Hooks reference for Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL_trusted_language_extension-hooks-reference.html): Reference documentation for the hooks supported by Trusted Language Extensions for PostgreSQL.


## [Code examples](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon RDS with AWS SDKs.

- [Hello Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_Hello_section.html): Hello Amazon RDS
- [Learn the basics](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_Scenario_GetStartedInstances_section.html): Learn the basics of Amazon RDS with an AWS SDK

### [Actions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/service_code_examples_actions.html)

The following code examples show how to use Amazon RDS with AWS SDKs.

- [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_CreateDBInstance_section.html): Use CreateDBInstance with an AWS SDK or CLI
- [CreateDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_CreateDBParameterGroup_section.html): Use CreateDBParameterGroup with an AWS SDK or CLI
- [CreateDBSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_CreateDBSnapshot_section.html): Use CreateDBSnapshot with an AWS SDK or CLI
- [DeleteDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DeleteDBInstance_section.html): Use DeleteDBInstance with an AWS SDK or CLI
- [DeleteDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DeleteDBParameterGroup_section.html): Use DeleteDBParameterGroup with an AWS SDK or CLI
- [DescribeAccountAttributes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeAccountAttributes_section.html): Use DescribeAccountAttributes with an AWS SDK or CLI
- [DescribeDBEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeDBEngineVersions_section.html): Use DescribeDBEngineVersions with an AWS SDK or CLI
- [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeDBInstances_section.html): Use DescribeDBInstances with an AWS SDK or CLI
- [DescribeDBParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeDBParameterGroups_section.html): Use DescribeDBParameterGroups with an AWS SDK or CLI
- [DescribeDBParameters](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeDBParameters_section.html): Use DescribeDBParameters with an AWS SDK or CLI
- [DescribeDBSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeDBSnapshots_section.html): Use DescribeDBSnapshots with an AWS SDK or CLI
- [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_DescribeOrderableDBInstanceOptions_section.html): Use DescribeOrderableDBInstanceOptions with an AWS SDK or CLI
- [GenerateRDSAuthToken](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_GenerateRDSAuthToken_section.html): Use GenerateRDSAuthToken with an AWS SDK
- [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_ModifyDBInstance_section.html): Use ModifyDBInstance with an AWS SDK or CLI
- [ModifyDBParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_ModifyDBParameterGroup_section.html): Use ModifyDBParameterGroup with an AWS SDK or CLI
- [RebootDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_rds_RebootDBInstance_section.html): Use RebootDBInstance with an AWS SDK or CLI

### [Scenarios](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/service_code_examples_scenarios.html)

The following code examples show how to use Amazon RDS with AWS SDKs.

- [Create an Aurora Serverless work item tracker](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_cross_RDSDataTracker_section.html): Create an Aurora Serverless work item tracker

### [Serverless examples](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/service_code_examples_serverless_examples.html)

The following code examples show how to use Amazon RDS with AWS SDKs.

- [Connecting to an Amazon RDS database in a Lambda function](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/example_serverless_connect_RDS_Lambda_section.html): Connecting to an Amazon RDS database in a Lambda function


## [Security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.html)

- [Database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/database-authentication.html): Use different types of database authentication supported by Amazon RDS encryption.
- [Password management with RDS and Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html): Learn about managing Amazon RDS passwords with AWS Secrets Manager.

### [Data protection](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/DataDurability.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon RDS.

### [Data encryption](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Encryption.html)

Use data encryption to provide added security for your data stored in your Amazon RDS DB instances .

- [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html): Secure your RDS data by encrypting your DB instances.
- [AWS KMS key management](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.Keys.html): Amazon RDS automatically integrates with AWS Key Management Service (AWS KMS) for key management.
- [Using SSL/TLS to encrypt a connection](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html): Create encrypted connections to your Amazon RDS database using SSL/TLS.
- [Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL-certificate-rotation.html): Rotate your SSL/TLS certificate as a security best practice.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/inter-network-traffic-privacy.html): Describes how Amazon RDS secures connections from the service to other locations.

### [Identity and access management](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.html)

How to authenticate requests and manage access to your Amazon RDS resources.

- [How Amazon RDS works with IAM](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon RDS, you should understand what IAM features are available to use with Amazon RDS.

### [Identity-based policy examples](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_id-based-policy-examples.html)

Work with these identity-based policy examples for Amazon RDS.

- [Permission policies to create, modify and, delete resources in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_id-based-policy-examples-create-and-modify-examples.html): The following sections present examples of permission policies that grant and restrict access to resources:
- [Example policies: Using condition keys](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.Conditions.Examples.html): Following are examples of how you can use condition keys in Amazon RDS IAM permissions policies.
- [Using custom tags](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.SpecifyingCustomTags.html): Amazon RDS supports specifying conditions in an IAM policy using custom tags.
- [Tagging on creation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_id-based-policy-examples-grant-permissions-tags-on-create.html): Some RDS API operations allow you to specify tags when you create the resource.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon RDS and recent changes to those policies.
- [Policy updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-manpol-updates.html): View details about updates to AWS managed policies for Amazon RDS since RDS began tracking these changes.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/cross-service-confused-deputy-prevention.html): For AWS cross-service work, learn how to prevent the confused deputy problem, a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.

### [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html)

Authenticate to your DB instance or cluster using AWS Identity and Access Management (IAM) database authentication.

- [Enabling and disabling](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Enabling.html): By default, IAM database authentication is disabled on DB instances.
- [Creating and using an IAM policy for IAM database access](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.html): To allow a user or role to connect to your DB instance, you must create an IAM policy.
- [Creating a database account using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html): With IAM database authentication, you don't need to assign database passwords to the user accounts you create.

### [Connecting to your DB instance using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.html)

With IAM database authentication, you use an authentication token when you connect to your DB instance.

- [Connecting to your DB instance using IAM authentication with the AWS drivers](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/IAMDBAuth.Connecting.Drivers.html): The AWS suite of drivers has been designed to provide support for faster switchover and failover times, and authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM), and Federated Identity.
- [Connecting using IAM: AWS CLI and mysql client](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.AWSCLI.html): You can connect from the command line to an Amazon RDS DB instance with the AWS CLI and mysql command line tool as described following.
- [Connecting using IAM authentication from the command line: AWS CLI and psql client](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.AWSCLI.PostgreSQL.html): You can connect from the command line to an Amazon RDS for PostgreSQL DB instance with the AWS CLI and psql command line tool as described following.
- [Connecting using IAM authentication and the AWS SDK for .NET](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.NET.html): You can connect to an RDS for MariaDB, MySQL, or PostgreSQL DB instance with the AWS SDK for .NET as described following.
- [Connecting using IAM authentication and the AWS SDK for Go](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.Go.html): You can connect to an RDS for MariaDB, MySQL, or PostgreSQL DB instance with the AWS SDK for Go as described following.
- [Connecting using IAM authentication and the AWS SDK for Java](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.Java.html): You can connect to an RDS for MariaDB, MySQL, or PostgreSQL DB instance with the AWS SDK for Java as described following.
- [Connecting using IAM authentication and the AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.Python.html): You can connect to an RDS for MariaDB, MySQL, or PostgreSQL DB instance with the AWS SDK for Python (Boto3) as described following.
- [Troubleshooting IAM DB authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Troubleshooting.html): Following, you can find troubleshooting ideas for some common IAM DB authentication issues and information on CloudWatch logs and metrics for IAM DB authentication.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon RDS and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.LoggingAndMonitoring.html): Tools in Amazon RDS for monitoring resources and responding to incidents.
- [Compliance validation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/RDS-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and also specific Amazon RDS features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/infrastructure-security.html): Learn how Amazon RDS isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your virtual private cloud (VPC) and Amazon RDS API.
- [Security best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_BestPractices.Security.html): Use AWS Identity and Access Management (IAM) accounts to control access to Amazon RDS API operations, especially operations that create, modify, or delete Amazon RDS resources.
- [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html): Control the access the traffic in and out of a DB instance with security groups.
- [Master user account privileges](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.MasterAccounts.html): When you create a new DB instance , the default master user that you use gets certain privileges for that DB instance .
- [Service-linked roles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAM.ServiceLinkedRoles.html): How to use service-linked roles to give Amazon RDS access to resources in your AWS account.

### [Using Amazon RDS with Amazon VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html)

Learn about common tasks for working with a DB instance in a virtual private cloud (VPC) based on the Amazon VPC service.

- [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html): Learn about working with an Amazon RDS DB instance in a VPC.
- [Updating the VPC for a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.VPC2VPC.html): Learn about moving a DB instance to a different VPC.
- [Scenarios for accessing a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html): Learn about the various scenarios for accessing a DB instance in a VPC.
- [Tutorial: Create a VPC for use with a DB instance (IPv4 only)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html): Create a virtual private cloud (VPC) with public and private subnets to host a public web server and a private DB instance.
- [Tutorial: Create a VPC for use with a DB instance (dual-stack mode)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.CreateVPCDualStack.html): Create a virtual private cloud (VPC) based on the Amazon VPC service.
- [Moving a DB instance into a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Non-VPC2VPC.html): Discusses moving a DB instance not in a VPC into a VPC.


## [Amazon RDS API reference](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/ProgrammingGuide.html)

- [Using the Query API](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Using_the_Query_API.html): Use the Query API to handle authentication and selection of an action with your Amazon RDS instances.
- [Troubleshooting applications](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/APITroubleshooting.html): Provides specific and descriptive errors to help you troubleshoot problems while interacting with the Amazon RDS API.
