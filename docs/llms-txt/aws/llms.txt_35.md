# Source: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/llms.txt

# Amazon Aurora User Guide for Aurora

> Amazon Web Services (AWS) documentation for Amazon Aurora (Aurora). Aurora is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. Aurora is part of the managed database service Amazon Relational Database Service (Amazon RDS). Amazon RDS is a web service that makes it easier to set up, operate, and scale a relational database in the cloud.

- [Setting up your environment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_SettingUp_Aurora.html)
- [Tutorials and sample code](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.html)
- [Best practices with Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html)
- [Performing an Aurora proof of concept](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-poc.html)
- [Quotas and constraints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Limits.html)
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Troubleshooting.html)
- [Document history](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/WhatsNew.html)
- [AWS Glossary](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/glossary.html)

## [What is Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)

- [Aurora DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html): Learn about Aurora DB clusters on Amazon RDS.

### [Aurora versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.html)

Learn about Amazon Aurora versions, which have their own version numbers, release cycle, and timeline for version deprecation.

- [Aurora versioning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.Versioning.html): Track Amazon Aurora database versions with quarterly minor releases, major versions compatible with community editions, and automatic patching for important fixes.
- [Aurora DB cluster upgrades](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.Upgrading.html): Upgrade Amazon Aurora DB clusters automatically to the latest minor version by enabling auto minor version upgrade, or manually control upgrades to new major versions.
- [Aurora version support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.Support.html): Understand the long-term support and extended support policies for managing selected Amazon Aurora minor versions over extended timeframes.
- [Regions and Availability Zones](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.RegionsAndAvailabilityZones.html): Learn how Amazon cloud computing resources are hosted in multiple locations world-wide, including AWS Regions and Availability Zones.

### [Supported Aurora features by Region and engine](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraFeaturesRegionsDBEngines.grids.html)

Learn which features are available in each AWS Region for Amazon Aurora MySQL-Compatible Edition and Amazon Aurora PostgreSQL-Compatible Edition.

- [Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.BlueGreenDeployments.html): View the AWS Region and Amazon RDS DB engine version support for Blue/Green Deployments.
- [Aurora cluster configurations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.storage-type.html): Learn which cluster storage configurations are available for Aurora DB engines.
- [Database activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.DBActivityStreams.html): View the AWS Region and Aurora DB engine version support for the database activity streams feature.
- [Exporting cluster data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportClusterToS3.html): View the AWS Region and Aurora DB engine version support for the exporting DB cluster data to Amazon S3 feature.
- [Exporting snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ExportSnapshotToS3.html): View the AWS Region and Aurora DB engine version support for the exporting DB cluster snapshot data to Amazon S3 feature.
- [Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.GlobalDatabase.html): View the AWS Region and Aurora DB engine version availability for the global databases feature.
- [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.IAMdbauth.html): View the AWS Region and Aurora DB engine version support for IAM.
- [Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.KerberosAuthentication.html): View the AWS Region and Aurora DB engine version support for Kerberos authentication.
- [Aurora machine learning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.Aurora_ML.html): View the AWS Region and Aurora DB engine version support for the machine learning feature.
- [Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.PerfInsights.html): View the AWS Region and Aurora DB engine version support for Performance Insights.
- [Zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.Zero-ETL.html): View the AWS Region and Aurora DB engine version support for Amazon Aurora zero-ETL integrations with Amazon Redshift.
- [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.RDS_Proxy.html): View the AWS Region and Aurora DB engine version support for Amazon RDS Proxy.
- [Secrets Manager integration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.SecretsManager.html): View the AWS Region and Amazon Aurora DB engine version support for AWS Secrets Manager integration.
- [Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.html): View the AWS Region and Aurora DB engine version support for Aurora Serverless v2.
- [Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.html): View the AWS Region and Aurora DB engine version support for Aurora Serverless v1.
- [RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.Data_API.html): View the AWS Region and Aurora DB engine version support for RDS Data API.
- [Zero-downtime patching (ZDP)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.ZDP.html): View the AWS Region and Aurora DB engine version support for zero-downtime patching (ZDP) for Amazon Aurora.
- [Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.AuroraLimitless.html): View the AWS Region support for Aurora PostgreSQL Limitless Database.
- [Engine-native features](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.Aurora_Fea_Regions_DB-eng.Feature.EngineNativeFeatures.html): Learn which engine-native features are available for Aurora DB engines.

### [Endpoint connections](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html)

Amazon Aurora typically involves a cluster of DB instances instead of a single instance.

- [Cluster endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Cluster.html): Connect to cluster endpoints.
- [Reader endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Reader.html): Connect to reader endpoints.
- [Instance endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Instance.html): Connect to instance endpoints.

### [Custom endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Custom.html)

Connect to custom endpoints.

- [Considerations for custom endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoints.Custom.Considerations.html): Considerations when creating and managing custom endpoints in Amazon Aurora.
- [Creating a custom endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-custom-endpoint-creating.html): Create a custom endpoint.
- [Viewing custom endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-endpoint-viewing.html): View a custom endpoint.
- [Editing a custom endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-endpoint-editing.html): Edit a custom endpoint.
- [Deleting a custom endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-endpoints-custom-deleting.html): Delete a custom endpoint.
- [AWS CLI examples for custom endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Endpoint.Tutorial.html): Use the AWS CLI to create, modify, and use custom endpoints for Amazon Aurora.

### [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.html)

Determine the computation and memory capacity of an Amazon Aurora DB instance by its DB instance class.

- [DB instance class types](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.Types.html): A reference of Aurora DB instance class types.
- [Supported DB engines](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.SupportAurora.html): A reference of supported DB engines for Aurora DB instance classes.
- [Determining DB instance class support in AWS Regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.RegionSupportAurora.html): Determine the DB instance classes Aurora supports for a DB engine in an AWS Region.
- [Hardware specifications](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.Summary.html): A reference of hardware specifications for DB instance class typesin Amazon Aurora.
- [Storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html): Learn about the Aurora storage subsystem.
- [Reliability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Reliability.html): Learn how Aurora supports reliability and high availability.
- [Aurora security](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Security.html): Learn how to manage security in Aurora.
- [High availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html): Ensure high availability for your Amazon Aurora databases with automatic failover, multi-Availability Zone configuration, and global databases that span AWS Regions.
- [Replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html): Leverage built-in replication options with Amazon Aurora for high availability, read scaling, and data distribution across AWS Regions.

### [DB instance billing for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/User_DBInstanceBilling.html)

Understand how Amazon Aurora DB instances are billed.

- [On-Demand DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_OnDemandDBInstances.html): Get on-demand DB instances by purchasing DB instance resources by the second.

### [Reserved DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithReservedDBInstances.html)

Get reserved DB instances by purchasing DB instances up front at a significantly lower cost.

- [Purchasing reserved DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithReservedDBInstances.WorkingWith.html): Purchase reserved DB instances with the Amazon RDS console, the AWS CLI, or the Amazon RDS API.
- [Viewing the billing for reserved DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/reserved-instances-billing.html): View the billing for your reserved DB instances in the AWS Management Console.


## [Getting started](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.html)

- [Creating and connecting to an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html): Create and connect to an Aurora MySQL DB cluster.
- [Creating and connecting to an Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.AuroraPostgreSQL.html): Create and connect to a DB Cluster on Aurora PostgreSQL

### [Tutorial: Create a web server and an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/TUT_WebAppWithRDS.html)

Follow this tutorial to create a web server and an Amazon Aurora DB cluster using Aurora and other AWS services.

- [Launch an EC2 instance to connect with your DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.LaunchEC2.html): Create an Amazon EC2 instance in the public subnet of your VPC.
- [Create a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateDBCluster.html): Create an Amazon Aurora DB cluster to use with a web server.
- [Install a web server](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateWebServer.html): Install a web server to serve public content and connect to the private Amazon Aurora DB Cluster.


## [Programmatic access to Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ProgrammaticAccess.html)

- [Console-to-Code](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Using_C2C.html): Learn about using Amazon Q Developer Console-to-Code to generate code for use in other Amazon RDS programming interfaces.


## [Setting up an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraSettingUp.html)

- [Creating a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html): Create a DB cluster using Aurora.
- [Creating resources with AWS CloudFormation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/creating-resources-with-cloudformation.html): Learn about how to create resources for Amazon Aurora using an AWS CloudFormation template.
- [Connecting to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Connecting.html): Connect to an Aurora DB cluster.

### [Parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.html)

Manage the DB engine configuration through the use of parameter groups.

- [Overview of parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/parameter-groups-overview.html): A conceptual overview of parameter groups and types of parameter groups.

### [DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithDBClusterParamGroups.html)

Manage the Amazon Aurora DB cluster configuration through the use of DB cluster parameter groups.

- [Creating a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html): Create a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Associating a DB cluster parameter group with a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.AssociatingCluster.html): Associate a DB cluster parameter group with an Aurora DB cluster using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Modifying parameters in a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html): Modifying parameters in a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Resetting parameters in a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ResettingCluster.html): Reset parameters in a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Copying a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CopyingCluster.html): Copy a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Listing DB cluster parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ListingCluster.html): List DB cluster parameter groups using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Viewing parameter values for a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ViewingCluster.html): View parameter values for a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Deleting a DB cluster parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.DeletingCluster.html): Delete a DB cluster parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.

### [DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithDBInstanceParamGroups.html)

Manage the DB instance configuration through the use of DB parameter groups.

- [Creating a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Creating.html): Create a new DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Associating a DB parameter group to a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Associating.html): Associate a DB parameter group to a DB instance using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Modifying parameters in a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Modifying.html): Modify a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Resetting parameters in a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Resetting.html): Reset parameters in a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Copying a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Copying.html): Copy a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Listing DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Listing.html): List DB parameter groups using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [View parameter values for a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Viewing.html): View parameter values for a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Deleting a DB parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Deleting.html): Delete a DB parameter group using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Comparing DB parameter groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.Comparing.html): Use the AWS Management Console to compare two DB parameter groups.
- [Specifying DB parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_ParamValuesRef.html): Specify the values for an Amazon RDS or Aurora DB parameter using formulas or functions in the values.
- [Migrating data to a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Migrate.html): Migrate (copy) data from an external database, an RDS instance, or an RDS DB snapshot to an Amazon Aurora DB cluster.
- [Creating an ElastiCache cache from Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/creating-elasticache-cluster-with-RDS-settings.html): Learn how to create an ElastiCache cache from Amazon RDS using settings from an Aurora DB clusterAmazon RDS DB instance.

### [Auto-migrating EC2 databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration.html)

You can use the Aurora console to migrate an EC2 database to Aurora.

### [Creating IAM resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration-IAM.html)

Aurora uses AWS DMS to migrate your data.

- [Secret access policy and role](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration-IAM.secret-iam-role-policy.html): Follow the procedures below to create your secret access policy and role which allow DMS to access the user credentials for your source and target databases.
- [Creating IAM role for DMS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration-IAM.dms-vpc-role.html): You must create an IAM role for AWS DMS to manage the VPC settings for your resources.
- [Set up data migration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration-SetUp.html): To begin migrating data from your EC2 source database, you must create an equivalent Aurora database.
- [Managing migrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration.Managing.html): After using the Migrate data from EC2 database action from the RDS console, Aurora starts the migration automatically.
- [Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DMS_migration.Monitoring.html): After the data migrations starts, you can monitor its status and progress.
- [Tutorial: Creating a MySQL DB cluster with a custom parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/tutorial-creating-custom-OPG.html): Create a MySQL DB cluster on Amazon Relational Database Service with a custom parameter and for password expiration policies and auditing capabilities.


## [Managing an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Aurora.html)

- [Stopping and starting a cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-cluster-stop-start.html): Stop and start all DB instances in an Amazon Aurora cluster at once.
- [Connecting an EC2 instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ec2-rds-connect.html): Connect an EC2 instance and an Aurora DB cluster.
- [Connecting a Lambda function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/lambda-rds-connect.html): Connect a Lambda function and an Aurora DB cluster.
- [Modifying an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html): Learn how to modify an Amazon Aurora DB cluster to accomplish tasks such as changing its backup retention period or its database port.

### [Adding Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.html)

Adding Aurora Replicas to a DB cluster

- [Auto Scaling with Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html): Apply Aurora Auto Scaling to automatically scale Aurora Replicas.
- [Adding an auto scaling policy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.Add.html): Add an auto scaling policy to your Amazon Aurora DB cluster.
- [Editing an auto scaling policy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.Edit.html): Edit an auto scaling policy for your Amazon Aurora DB cluster.
- [Deleting an auto scaling policy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.Delete.html): Delete an auto scaling policy from your Amazon Aurora DB cluster.
- [Managing performance and scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html): Improve performance and scaling by modifying storage, DB instance class, Aurora Replicas, maximum connections, and query plans.

### [Cloning a volume for an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.html)

Use Amazon Aurora cloning to quickly and cost-effectively create a new cluster that uses the same Aurora cluster volume and has the same data as the original.

- [Cross-VPC cloning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.Cross-VPC.html): By configuring resources such as virtual private clouds (VPCs), subnets, and DB subnet group, you can clone Aurora DB clusters where the original cluster and the clone are in separate VPCs.
- [Cross-account cloning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Clone.Cross-Account.html): By using AWS Resource Access Manager with Amazon Aurora, you can share Aurora DB clusters and clones that belong to your AWS account with another AWS account or organization.
- [Integrating with AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.html): Integrate your Amazon Aurora databases with other AWS services available in the AWS Cloud.

### [Maintaining an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html)

Learn about how Amazon RDS periodically performs maintenance on Amazon RDS resources such as a DB cluster.

- [AWS Organizations upgrade rollout](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Maintenance.AMVU.UpgradeRollout.html): Aurora supports AWS Organizations upgrade rollout policy to manage automatic minor version upgrades across multiple database resources and AWS accounts.

### [Rebooting an Aurora DB cluster or instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_RebootCluster.html)

Reboot an Amazon Aurora DB cluster to apply pending changes.

- [Rebooting a DB instance within an Aurora cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-reboot-db-instance.html): This procedure is the most important operation that you take when performing reboots with Aurora.
- [Rebooting an Aurora cluster with read availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-survivable-replicas.html)
- [Rebooting an Aurora cluster without read availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-reboot-cluster.html): Without the read availability feature, you reboot an entire Aurora DB cluster by rebooting the writer DB instance of that cluster.
- [Checking uptime for Aurora clusters and instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Reboot.Uptime.html): You can check and monitor the length of time since the last reboot for each DB instance in your Aurora cluster.
- [Examples of Aurora reboot operations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Reboot.Examples.html): The following Aurora MySQL examples show different combinations of reboot operations for reader and writer DB instances in an Aurora DB cluster.
- [Failing over an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-failover.html): Learn how to perform a manual failover of an Amazon Aurora DB cluster.
- [Deleting Aurora clusters and instances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DeleteCluster.html): Delete one or more Aurora DB instances within an Aurora DB cluster, or the entire DB cluster.

### [Tagging Aurora and RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html)

Use tags to manage access, control what actions can be applied to resources, and track costs by adding metadata to your Amazon Aurora and Amazon RDS resources.

- [Tutorial: Use tags to specify which Aurora DB clusters to stop](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Tagging.Aurora.Autostop.html): Add tags to DB clusters and then stop DB clusters with the assigned tag.

### [ARNs in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.html)

Get the format for the Amazon Resource Name, or ARN, for Amazon RDS resources.

- [Constructing an ARN](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.Constructing.html): Construct an ARN for your Amazon RDS resource.
- [Getting an existing ARN](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.ARN.Getting.html): Get an ARN for your Amazon RDS resource.
- [Aurora updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Updates.html): Amazon Aurora Updates


## [RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support.html)

- [RDS Extended Support overview](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-overview.html): Learn about versions, charges, and responsibilities concerning Amazon RDS Extended Support.
- [RDS Extended Support charges](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-charges.html): Learn about charges associated with Amazon RDS Extended Support.
- [Versions with RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-versions.html): Learn which engine versions support Amazon RDS Extended Support.
- [Responsibilities with RDS Extended Support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-responsibilities.html): Learn about Amazon Aurora and customer responsibilities with Amazon RDS Extended Support.
- [Creating an Aurora DB cluster or a global cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-creating-db-instance.html): Learn about creating an Aurora DB cluster or a global cluster with an Amazon RDS Extended Support version.
- [Viewing RDS Extended Support enrollment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-viewing.html): Learn about viewing the enrollment of your Aurora DB clusters or global clusters in Amazon RDS Extended Support.
- [Viewing support dates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-viewing-support-dates.html): Learn about how to view the support dates for engine versions in Aurora DB clusters or global clusters in Amazon RDS Extended Support.
- [Restoring an Aurora DB cluster or a global cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/extended-support-restoring-db-instance.html): Learn about restoring an Aurora DB cluster or a global cluster with an Amazon RDS Extended Support version.


## [Using Blue/Green Deployments for database updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments.html)

### [Overview of Blue/Green Deployments](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-overview.html)

Learn about concepts related to Amazon RDS Blue/Green Deployments.

- [Authorizing access](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-authorizing-access.html): Users must have the required permissions to perform operations related to blue/green deployments.
- [Limitations and considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-considerations.html): Blue/green deployments in Amazon RDS require careful consideration of factors such as replication slots, resource management, instance sizing, and potential impacts on database performance.
- [Best practices](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-best-practices.html): The following are best practices for blue/green deployments.
- [Creating a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-creating.html): Learn about creating a blue/green deployment for reduce downtime when you make database updates.
- [Viewing a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-viewing.html): Learn about viewing details of a blue/green deployment.
- [Switching a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-switching.html): Learn about switching a blue/green deployment to make your staging environment your production environment.
- [Deleting a blue/green deployment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/blue-green-deployments-deleting.html): Learn about deleting a blue/green deployment.


## [Backing up and restoring an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/BackupRestoreAurora.html)

- [Overview of backing up and restoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.html): Learn about Aurora backups and how to restore your Aurora DB cluster.

### [Retaining automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.Retaining.html)

When you delete a provisioned or Aurora Serverless v2 DB cluster, you can retain automated backups.

- [Viewing retained automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.Retaining.Viewing.html): To view your retained automated backups in the RDS console, choose Automated backups in the navigation pane, then choose Retained.
- [Deleting retained automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Backups.Retaining.Deleting.html): You can delete retained automated backups when they are no longer needed.
- [Backup storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-storage-backup.html): Learn about storage for automated backups and snaphots.
- [Creating a DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CreateSnapshotCluster.html): Create a DB cluster snapshot by identifying which DB cluster you are going to back up, and give that DB cluster snapshot a name.
- [Restoring from a DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-restore-snapshot.html): Restore an Amazon Aurora DB cluster from a DB cluster snapshot.

### [DB cluster snapshot copying](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-copy-snapshot.html)

Copy an Amazon Aurora DB cluster snapshot.

- [Copying a DB cluster snapshot with the AWS Management Console](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopyDBClusterSnapshot.CrossRegion.html): Use the procedures in this topic to copy a DB cluster snapshot.
- [Copying an unencrypted DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopyDBClusterSnapshot.Unencrypted.CrossRegion.html): Copy an unencrypted DB cluster snapshot using the AWS CLI or Amazon RDS API.
- [Copying an encrypted DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopyDBClusterSnapshot.Encrypted.CrossRegion.html): Copy an encrypted DB cluster snapshot using the AWS CLI or Amazon RDS API.
- [Copying a DB cluster snapshot across accounts](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_CopyDBClusterSnapshot.CrossAccount.html): Copy a DB cluster snapshot across accounts with the Amazon RDS API.

### [Sharing a DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-share-snapshot.html)

Share a manual DB cluster snapshot so that other AWS accounts can copy or restore a DB instance from it.

- [Sharing public snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-share-snapshot.public.html): Share public DB cluster snapshots.
- [Sharing encrypted snapshots](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/share-encrypted-snapshot.html): Share encrypted DB cluster snapshots.
- [Stopping snapshot sharing](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/share-snapshot-stop.html): Stop sharing a DB cluster snapshot by removing permissions from the target AWS account.

### [Exporting DB cluster data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.html)

Export data from an Amazon Aurora DB cluster.

- [Considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.Considerations.html): Limitations and other considerations when exporting data from DB clusters to Amazon S3.
- [Setting up access to an S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.Setup.html): Give your DB cluster access to an Amazon S3 bucket.
- [Creating DB cluster export tasks](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.Exporting.html): Create export tasks to export data from your Aurora DB cluster to an Amazon S3 bucket.
- [Monitoring DB cluster exports](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.Monitoring.html): Display information about DB cluster export tasks.
- [Canceling a DB cluster export](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.Canceling.html): Cancel a DB cluster export task using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/export-cluster-data.Troubleshooting.html): Troubleshoot failure messages and PostgreSQL permission errors for DB cluster export tasks.

### [Exporting DB cluster snapshot data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.html)

Export an Amazon Aurora database cluster snapshot.

- [Considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.Considerations.html): Limitations and other considerations when exporting snapshot data from DB clusters to Amazon S3.
- [Setting up access to an S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.Setup.html): Give your snapshot access to an Amazon S3 bucket.
- [Creating snapshot export tasks](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.Exporting.html): Create snapshot export tasks to export data from your snapshot to an Amazon S3 bucket.
- [Monitoring snapshot exports](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.Monitoring.html): Display information about snapshot export tasks.
- [Canceling a snapshot export](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.Canceling.html): Cancel a snapshot export task using the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- [Export performance in Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.parallel.html): Learn how Aurora MySQL reduces export time.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-export-snapshot.Troubleshooting.html): Troubleshoot failure messages and PostgreSQL permission errors for snapshot export tasks.

### [Point-in-time recovery](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-pitr.html)

Restore an Amazon Aurora DB cluster to a specific point in time.

- [Point-in-time recovery from a retained automated backup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-pitr-retained.html): Restore a DB cluster to a specified time after deleting the source DB cluster.
- [Point-in-time recovery using AWS Backup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-pitr-bkp.html): Restore a DB cluster to a specified time using AWS Backup.
- [Deleting a DB cluster snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-delete-snapshot.html): Delete an Amazon Aurora DB cluster snapshot.

### [Tutorial: Restore a DB cluster from a snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/tut-restore-cluster.html)

Learn how to restore an Amazon Aurora DB cluster from a DB cluster snapshot.

- [Restoring a DB cluster using the console](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/tut-restore-cluster.console.html): Restore a DB cluster from a DB cluster snapshot using the Amazon RDS console.
- [Restoring a DB cluster using the AWS CLI](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/tut-restore-cluster.CLI.html): Restore a DB cluster from a DB cluster snapshot using the AWS CLI.


## [Monitoring metrics in an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/MonitoringAurora.html)

- [Monitoring tools](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/MonitoringOverview.html): Overview of monitoring tools forAmazon Aurora.
- [Viewing cluster status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/accessing-monitoring.html): Using the Amazon RDS console, you can quickly access the status of your DB cluster.

### [Recommendations from Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html)

Learn about recommendations for your Amazon Aurora resources.

- [Viewing recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UserRecommendationsView.html): Learn how to view Aurora recommendations.
- [Applying recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USERRecommendationsManage.ApplyRecommendation.html): Apply Amazon Aurora recommendations using the Amazon RDS console or Amazon RDS API.
- [Dismissing recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USERRecommendationsManage.DismissRecommendation.html): Dismiss Amazon Aurora recommendations using the Amazon RDS console, AWS CLI, or Amazon RDS API.
- [Modifying dismissed recommendations to active](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USERRecommendationsManage.DismissToActiveRecommendation.html): Modify dismissed Amazon Aurora recommendations to active recommendations using the Amazon RDS console, AWS CLI, or Amazon RDS API.
- [Recommendations reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USERRecommendationsManage.RecommendationReference.html): A reference of recommendations from Amazon Aurora.
- [Viewing metrics in the Amazon RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.html): View metrics in the Amazon RDS console.

### [Viewing the Performance Insights dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Viewing_Unifiedmetrics.html)

View CloudWatch and Performance Insights metrics in the Performance Insights dashboard.

- [Choosing the new monitoring view from the Monitoring tab](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Viewing_Unifiedmetrics.MonitoringTab.html): View Performance Insights and CloudWatch metrics for your database from the Monitoring tab.
- [Choosing the new monitoring view from the Performance Insights page](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Viewing_Unifiedmetrics.PInavigationPane.html): View Performance Insights and CloudWatch metrics for your database with Performance Insights.
- [Creating a custom dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Viewing_Unifiedmetrics.PIcustomizeMetricslist.html): Create a custom Performance Insights dashboard to view up to 50 Performance Insights and CloudWatch metrics.
- [Choosing the preconfigured dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Viewing_Unifiedmetrics.PI-preconfigured-dashboard.html): View the most commonly used metrics to diagnose performance issues using the Performance Insights dashboard.

### [Monitoring Aurora with CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-cloudwatch.html)

Monitor metrics for Amazon RDS resources using CloudWatch.

- [Viewing CloudWatch metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/metrics_dimensions.html): View metrics for your DB instance using the CloudWatch console and the AWS CLI.

### [Exporting Performance Insights metrics to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PI_metrics_export_CW.html)

Export Performance Insights metrics to CloudWatch as a new dashboard or to an existing dashboard.

- [Exporting Performance Insights metrics as a new dashboard to CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PI_metrics_export_CW.new_dashboard.html): Export Performance Insights metrics to a new CloudWatch dashboard.
- [Adding Performance Insights metrics to an existing CloudWatch dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PI_metrics_export_CW.existing_dashboard.html): Export Performance Insights metrics to an existing CloudWatch dashboard.
- [Viewing a Performance Insights metric widget in CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PI_metrics_export_CW.individual_widget.html): View Performance Insights metrics in the CloudWatch console.
- [Creating CloudWatch alarms](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/creating_alarms.html): Create CloudWatch alarms to monitor your Amazon RDS resources.

### [Monitoring with Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.html)

Monitor your Amazon Aurora database load with Database Insights to analyze and troubleshoot the performance of your database fleet.

- [Engine, Region, and instance class support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.Engines.html): Learn about the Amazon Aurora engine versions that support Database Insights.
- [Turning on the Advanced mode](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.TurningOnAdvanced.html): Turn on the Advanced mode of Database Insights for Amazon Aurora.
- [Turning on the Standard mode](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.TurningOnStandard.html): Turn on the Standard mode of Database Insights for Amazon Aurora.
- [Monitor slow queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.SlowSQL.html): Configure your database to monitor slow SQL queries with Database Insights.
- [Considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.Considerations.html): Considerations for Database Insights for Amazon Aurora.

### [Monitoring DB load with Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html)

Monitor your Amazon Aurora cluster load with Performance Insights to analyze and troubleshoot your database performance.

### [Overview of Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.html)

Learn about using Amazon RDS Performance Insights with DB engines.

- [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html): Learn about the key metric in Amazon RDS Performance Insights, DBLoad, which is collected every second and measures the level of activity in your database.
- [Maximum CPU](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.MaxCPU.html): Use the Performance Insights dashboard to see whether active session activity is exceeding the maximum CPU.
- [Amazon Aurora DB engine, Region, and instance class support for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.Engines.html): Learn about the Amazon Aurora engine versions that support Performance Insights.
- [Pricing and data retention for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.cost.html): Learn about pricing and data retention for Performance Insights.
- [Turning Performance Insights on and off](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Enabling.html): Turn Performance Insights on or off in the AWS Management Console, AWS CLI, or API.

### [Performance Schema for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.EnableMySQL.html)

Learn how to monitor runtime performance by turning on the Performance Schema.

- [Determining whether Performance Insights is managing the Performance Schema](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.EnableMySQL.determining-status.html): Determine whether Performance Insights is managing the Performance Schema.
- [Turn on the Performance Schema for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.EnableMySQL.RDS.html): Allow Performance Insights to manage the Performance Schema.

### [Performance Insights policies](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.html)

Configure IAM access policies for Performance Insights.

- [Attaching the AmazonRDSPerformanceInsightsReadOnly policy to an IAM principal](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.managed-policy.html): AmazonRDSPerformanceInsightsReadOnly is an AWS managed policy that grants access to all read-only operations of the Amazon RDS Performance Insights API.
- [Attaching the AmazonRDSPerformanceInsightsFullAccess policy to an IAM principal](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.FullAccess-managed-policy.html): AmazonRDSPerformanceInsightsFullAccess is an AWS managed policy that grants access to all operations of the Amazon RDS Performance Insights API.
- [Creating a custom IAM policy for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.custom-policy.html): Create a custom IAM policy for Performance Insights and attach it to a user.
- [Changing an AWS KMS policy for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.cmk-policy.html): Change an AWS KMS policy to allow or restrict access to Performance Insights.
- [Granting fine-grained access for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.dimensionAccess-policy.html): Control access to Performance Insights data with fine-grained access control.
- [Using tag-based access control for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.access-control.tag-based-policy.html): Control access to Performance Insights using tags inherited from DB instance

### [Analyzing metrics with the Performance Insights dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.html)

Analyze and troubleshoot performance issues for your database with the Performance Insights dashboard.

- [Overview of the dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.Components.html): The dashboard is the easiest way to interact with Performance Insights.
- [Accessing the dashboard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.Opening.html): View the Amazon RDS Performance Insights dashboard in the AWS Management Console.
- [Analyzing DB load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.html): Find performance issues by analyzing DB load by wait events with the Performance Insights dashboard.

### [Analyzing database performance for a period of time](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzePerformanceTimePeriod.html)

Troubleshoot database performance issues for a selected period of time by viewing the Performance Insights dashboard.

- [Creating a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.CreatingPerfAnlysisReport.html): Create a performance analysis report for a specific period in Performance Insights.
- [Viewing a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.ViewPerfAnalysisReport.html): View a performance analysis report for a specific period in Performance Insights.
- [Adding tags to a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.ManagePerfAnalysisReportTags.html): Add tags to a performance analysis report when you create or view a report in Performance Insights.
- [Deleting a performance analysis report](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.DeletePerfAnalysisReport.html): Delete a performance analysis report in Performance Insights.

### [Analyzing queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.html)

Analyze queries using the Top SQL tab in the Performance Insights dashboard.

### [Accessing more SQL text](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.SQLTextSize.html)

Access more SQL text for the top SQL statements in the Performance Insights dashboard.

- [Setting the SQL text limit](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.SQLTextLimit.html): Set the text size for Aurora PostgreSQL in Performance Insights.
- [Viewing and downloading SQL text](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/view-download-text.html): View and download SQL text in the Performance Insights dashboard.
- [Viewing SQL statistics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.AnalyzingSQLLevel.html): View SQL statistics for the top SQL statements in the Performance Insights dashboard.
- [Viewing Performance Insights proactive recommendations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.InsightsRecommendationViewDetails.html): Learn about viewing Performance Insights proactive recommendations in Amazon RDS.

### [Retrieving metrics with the Performance Insights API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.API.html)

Retrieve metrics with the Performance Insights API.

- [Retrieving time-series metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.API.TimeSeries.html): Use the GetResourceMetrics operation to retrieve time-series metrics.
- [AWS CLI examples for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.API.Examples.html): In the following sections, learn more about the AWS Command Line Interface (AWS CLI) for Performance Insights and use AWS CLI examples.
- [Logging Performance Insights calls using AWS CloudTrail](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.CloudTrail.html): View a record of Performance Insights actions using CloudTrail.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/pi-vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your virtual private cloud (VPC) and Performance Insights API.
- [Analyzing performance with DevOpsÂ Guru for RDS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/devops-guru-for-rds.html): Amazon DevOpsÂ Guru for Amazon RDS applies machine learning to Performance Insights metrics for Amazon RDS databases.

### [Monitoring the OS with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.html)

Monitor the operating system of your DB instance in real time with Enhanced Monitoring.

- [Setting up and enabling Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.Enabling.html): Create an IAM role for Enhanced Monitoring.
- [Viewing OS metrics in the RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.Viewing.html): View OS metrics in the Amazon RDS console.
- [Viewing OS metrics using CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring.OS.CloudWatchLogs.html): View OS metrics with CloudWatch Logs.

### [Aurora metrics reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/metrics-reference.html)

Metrics for Amazon CloudWatch, Performance Insights, and Enhanced Monitoring for Aurora.

- [CloudWatch metrics for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html): Metrics for Amazon CloudWatch for Aurora.
- [CloudWatch dimensions for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/dimensions.html): A listing of the Amazon CloudWatch dimensions for Aurora.
- [Availability of Aurora metrics in the Amazon RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Monitoring.Metrics.RDSAvailability.html): Aurora available in the Amazon RDS console.
- [CloudWatch metrics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Cloudwatch.html): Metrics for Amazon CloudWatch for Performance Insights.
- [Counter metrics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights_Counters.html): Native and non-native counter metrics for Performance Insights.

### [SQL statistics for Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/sql-statistics.html)

A reference for SQL statistics for Performance Insights.

- [SQL statistics for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.MySQL.html): Obtain digest, per-second, and per-call statistics for Aurora MySQL.
- [SQL statistics for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.UsingDashboard.AnalyzeDBLoad.AdditionalMetrics.PostgreSQL.html): Collect per-second and per-call digest statistics for Aurora PostgreSQL queries.
- [OS metrics in Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Monitoring-Available-OS-Metrics.html): A reference for OS metrics for Enhanced Monitoring.


## [Monitoring events, logs, and database activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Monitor_Logs_Events.html)

- [Viewing logs, events, and streams in the Amazon RDS console](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/logs-events-streams-console.html): View the events, logs, and activity streams for an Amazon Aurora database in the Amazon RDS console.

### [Monitoring Aurora events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/working-with-events.html)

An event indicates a change in an environment.

- [Viewing Amazon RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_ListEvents.html): Get the date and time, source name and type, and message of an event related to your DB cluster, , snapshot, and security or parameter groups using Amazon RDS.

### [Working with Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.html)

Get a notification by email, text message, or a call to an HTTP endpoint when an Amazon RDS event occurs using Amazon SNS.

- [Overview of Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.overview.html): Subscribe to event notifications when an Amazon RDS event occurs using Amazon SNS and see examples of Amazon RDS events.
- [Granting permissions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.GrantingPermissions.html): Grant Amazon RDS permissions to publish notifications to an Amazon Simple Notification Service (Amazon SNS) topic by attaching an AWS Identity and Access Management (IAM) policy to the destination topic.
- [Subscribing to Amazon RDS event notification](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Subscribing.html): Create an event notification subscription for an Amazon RDS event using Amazon SNS.
- [Amazon RDS event notification tags and attributes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.TagsAttributesForFiltering.html): Event notification details sent to SNS or EventBridge for filtering.
- [Listing Amazon RDS event notification subscriptions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.ListSubscription.html): List event notification subscriptions for Amazon RDS events.
- [Modifying an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Modifying.html): Modify event notification subscriptions for Amazon RDS events.
- [Adding a source identifier to an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.AddingSource.html): Add a source identifier to existing event notification subscriptions for Amazon RDS events.
- [Removing a source identifier from an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.RemovingSource.html): Remove a source identifier from existing event notification subscriptions for Amazon RDS events.
- [Listing the Amazon RDS event notification categories](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.ListingCategories.html): List event notification categories for Amazon RDS events.
- [Deleting an Amazon RDS event notification subscription](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Deleting.html): Delete an Amazon RDS event notification subscription.
- [Creating a rule that triggers on an Amazon Aurora event](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-cloud-watch-events.html): Learn how to write rules to send Amazon Aurora events to targets such as Amazon EventBridge.
- [Amazon RDS event categories and event messagesfor Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html): Amazon RDS generates a significant number of events in categories that you can subscribe to using the Amazon RDS Console, AWS CLI, or the API.

### [Monitoring Aurora logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.html)

View, download, and watch database logs by using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon RDS API.

- [Viewing and listing database log files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Procedural.Viewing.html): View database log files using the AWS Management Console, AWS CLI, or Amazon RDS API.
- [Downloading a database log file](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Procedural.Downloading.html): Download a database log file using the AWS Management Console or the AWS Command Line Interface (AWS CLI).
- [Watching a database log file](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Procedural.Watching.html): Monitor the contents of a log file by using the AWS Management Console.
- [Publishing to CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Procedural.UploadtoCloudWatch.html): Learn how to publish logs from Aurora to Amazon CloudWatch Logs.
- [Reading log file contents using REST](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DownloadCompleteDBLogFile.html): How to access log file contents using REST

### [MySQL database log files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Concepts.MySQL.html)

Monitor the Aurora MySQL error log, slow query log, and the general log directly through the Amazon RDS console, API, AWS CLI, or AWS SDKs.

- [Overview of Aurora MySQL database logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.MySQL.LogFileSize.html): Learn about database logs that you can monitor for Aurora MySQL databases.
- [Sending AuroraMySQL log output to tables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.MySQL.CommonDBATasks.Logs.html): Enable logging to tables in your DB instance and rotate log tables.
- [Configuring Aurora MySQL binary logging for Single-AZ databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.MySQL.BinaryFormat.html): Learn how to configure binary logging for Aurora MySQL databases.
- [Accessing MySQL binary logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.MySQL.Binarylog.html): You can use the mysqlbinlog utility to download or stream binary logs from RDS for MySQL DB instances.

### [PostgreSQL database log files](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Concepts.PostgreSQL.html)

Configure the settings for the PostgreSQL log files in your Aurora PostgreSQL DB cluster.

- [Parameters for logging](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Concepts.PostgreSQL.overview.parameter-groups.html): Control logging for your Aurora PostgreSQL DB cluster.
- [Turning on query logging](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_LogAccess.Concepts.PostgreSQL.Query_Logging.html): Turn on query logging to collect more information about your queries.
- [Monitoring Aurora API calls in CloudTrail](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail.html): Learn about logging Amazon RDS with AWS CloudTrail.

### [Monitoring Aurora with Database Activity Streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.html)

Monitor the activity for a database by using the Database Activity Streams feature in Amazon Aurora.

- [Aurora MySQL network prerequisites](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.Prereqs.html): In the following section, you can find how to configure your virtual private cloud (VPC) for use with database activity streams.
- [Starting a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.Enabling.html): To monitor database activity for all instances in your Aurora DB cluster, start an activity stream at the cluster level.
- [Getting the activity stream status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.Status.html): You can get the status of an activity stream using the console or AWS CLI.
- [Stopping a database activity stream](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.Disabling.html): You can stop an activity stream using the console or AWS CLI.

### [Monitoring activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.Monitoring.html)

Monitor Aurora database activity streams with Amazon Kinesis.

- [Accessing an activity stream from Kinesis](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.KinesisAccess.html): Access an activity stream to monitor your database activity in real time with Amazon Kinesis.
- [Audit logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.AuditLog.html): Examples for and the structure of audit logs for database activity streams.
- [databaseActivityEventList JSON array](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.AuditLog.databaseActivityEventList.html): Activity events stored in the audit log payload.
- [Processing an activity stream using the SDK](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.CodeExample.html): Process a database activity stream using the AWS SDK.
- [IAM policy examples for activity streams](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DBActivityStreams.ManagingAccess.html): Examples of IAM policies to create, start, stop, and modify database activity streams.
- [Monitoring threats with GuardDuty RDS Protection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/guard-duty-rds-protection.html): Amazon GuardDuty analyzes and profiles login events for potential access threats to your Amazon Aurora databases.


## [Working with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)

### [Overview of Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.html)

The following sections provide an overview of Amazon Aurora MySQL.

### [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html)

Describes Aurora version 3 support for MySQL 8.0 features.

- [New temporary table behavior in Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams3-temptable-behavior.html): Learn about temporary table behavior in Aurora MySQL version 3.
- [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html): Learn about changes to be aware of when you upgrade your Aurora MySQL version 2 cluster to version 3.
- [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html): Learn about the changes to be aware of when you convert from a different MySQL 8.0âcompatible system to Aurora MySQL version 3.
- [Upgrading to Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-upgrade-procedure.html): Learn about upgrading your database from Aurora MySQL version 2 to version 3.
- [Aurora MySQL version 2 compatible with MySQL 5.7](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.CompareMySQL57.html): Learn about MySQL 5.7âcompatible Aurora MySQL version 2.
- [Security with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Security.html): Manage security with Amazon Aurora MySQL.
- [Updating applications for new TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ssl-certificate-rotation-aurora-mysql.html): Update applications to connect to an Aurora MySQL DB cluster for TLS certificate rotation.

### [Using Kerberos authentication for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-kerberos.html)

Learn how to use Kerberos authentication for Aurora MySQL.

- [Setting up Kerberos authentication for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-kerberos-setting-up.html): Learn how to use AWS Managed Microsoft AD to set up Kerberos authentication for an Aurora MySQL DB cluster.
- [Connecting to Aurora MySQL with Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-kerberos-connecting.html): Learn how to connect to Aurora MySQL using Kerberos authentication.
- [Managing a DB cluster in a domain](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-kerberos-managing.html): Learn how to manage your DB cluster and its relationship with your managed Active Directory.

### [Migrating data to Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.html)

Migrate (copy) data from a MySQL database or MySQL for Amazon RDS DB snapshot to an Amazon Aurora MySQL DB cluster.

### [Migrating from an external MySQL database to Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html)

Migrate data from an external MySQL database to an Amazon Aurora MySQL DB cluster.

### [Physical migration using Percona XtraBackup and Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.S3.html)

Learn about migrating data physically from MySQL by using Percona XtraBackup and Amazon S3.

- [Reducing the physical migration time](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.Prechecks.html): Learn about the modifications that you can do to speed up physical migration from MySQL to Amazon Aurora MySQL.
- [Logical migration using mysqldump](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.mysqldump.html): Learn about logical migration by using the mysqldump utility to copy data from your MySQL or MariaDB database to an existing Aurora MySQL DB cluster.

### [Migrating from a MySQL DB instance to Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.html)

Migrate data from an RDS for MySQL DB instance to an Amazon Aurora MySQL DB cluster.

- [Migrating an RDS for MySQL snapshot to Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.Snapshot.html): You can migrate a DB snapshot of an RDS for MySQL DB instance to create an Aurora MySQL DB cluster.
- [Migrating from RDS for MySQL to Aurora MySQL using a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.Replica.html): Migrate from an RDS for MySQL DB instance to an Amazon Aurora MySQL DB cluster by using an Aurora read replica.

### [Managing Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.html)

Manage an Amazon Aurora MySQL DB cluster.

- [Managing performance and scaling for Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.html)

### [Backtracking a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.html)

With Amazon Aurora MySQL-Compatible Edition, you can backtrack a DB cluster to a specific time, without restoring data from a backup.

- [Configuring backtracking a Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.Configuring.html): To use the Backtrack feature, you must enable backtracking and specify a target backtrack window.
- [Performing a backtrack for an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.Performing0.html): You can backtrack a DB cluster to a specified backtrack time stamp.
- [Monitoring backtracking](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.Monitoring.html): You can view backtracking information and monitor backtracking metrics for a DB cluster.
- [Disabling backtracking for an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Backtrack.Disabling.html): You can disable the Backtrack feature for a DB cluster.
- [Testing Amazon Aurora MySQL using fault injection queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.FaultInjectionQueries.html): You can test the fault tolerance of your Aurora MySQL DB cluster by using fault injection queries.
- [Altering tables in Amazon Aurora using Fast DDL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.FastDDL.html): Alter tables in Amazon Aurora using fast data definition language (DDL) operations.
- [Displaying volume status for an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.VolumeStatus.html): In Amazon Aurora, a DB cluster volume consists of a collection of logical blocks.

### [Tuning Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Tuning.html)

Tune Amazon Aurora MySQL-Compatible Edition with wait events, thread states, and DevOpsÂ Guru proactive insights.

- [Essential concepts for Aurora MySQL tuning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Tuning.concepts.html): Learn some essential concepts for Amazon Aurora MySQL-Compatible Edition tuning.

### [Tuning Aurora MySQL with wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Tuning.wait-events.html)

Tune Aurora MySQL with wait events, using this table that summarizes the wait events that most commonly indicate performance problems.

- [cpu](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.cpu.html): The cpu wait event occurs when an Aurora MySQL thread is active in CPU or is waiting for CPU.
- [io/aurora_redo_log_flush](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.io-auredologflush.html): The io/aurora_redo_log_flush event occurs when a session is writing persistent data to Amazon Aurora storage.
- [io/aurora_respond_to_client](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.respond-to-client.html): The io/aurora_respond_to_client event occurs when a thread is waiting to return a result set to a client.
- [io/redo_log_flush](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.io-redologflush.html): The io/redo_log_flush event occurs when a session is writing persistent data to Amazon Aurora storage.
- [io/socket/sql/client_connection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.client-connection.html): The io/socket/sql/client_connection event occurs when an Aurora MySQL thread is in the process of handling a new connection.
- [io/table/sql/handler](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.waitio.html): The io/table/sql/handler event in Aurora MySQL occurs when work has been delegated to a storage engine.
- [synch/cond/innodb/row_lock_wait](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.row-lock-wait.html): The synch/cond/innodb/row_lock_wait event occurs for Aurora MySQL when one session has locked a row for an update, and another session tries to update the same row.
- [synch/cond/innodb/row_lock_wait_cond](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.row-lock-wait-cond.html): The synch/cond/innodb/row_lock_wait_cond event occurs for Aurora MySQL when one session has locked a row for an update, and another session tries to update the same row.
- [synch/cond/sql/MDL_context::COND_wait_status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.cond-wait-status.html): The synch/cond/sql/MDL_context::COND_wait_status event occurs when there are threads waiting on a table metadata lock.
- [synch/mutex/innodb/aurora_lock_thread_slot_futex](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.waitsynch.html): The synch/mutex/innodb/aurora_lock_thread_slot_futex event occurs for Aurora MySQL when one session has locked a row for an update, and another session tries to update the same row.
- [synch/mutex/innodb/buf_pool_mutex](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.bufpoolmutex.html): The synch/mutex/innodb/buf_pool_mutex event occurs when a thread has acquired a lock on the InnoDB buffer pool to access a page in memory.
- [synch/mutex/innodb/fil_system_mutex](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.innodb-fil-system-mutex.html): The synch/mutex/innodb/fil_system_mutex event occurs when a session is waiting to access the tablespace memory cache.
- [synch/mutex/innodb/trx_sys_mutex](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.trxsysmutex.html): The synch/mutex/innodb/trx_sys_mutex event occurs when there is high database activity with a large number of transactions.
- [synch/sxlock/innodb/hash_table_locks](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.sx-lock-hash-table-locks.html): The synch/sxlock/innodb/hash_table_locks event occurs when pages not found in the buffer pool must be read from storage.
- [synch/mutex/innodb/temp_pool_manager_mutex](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.io-temppoolmanager.html): The synch/mutex/innodb/temp_pool_manager_mutex wait event occurs when a session is waiting to acquire a mutex for managing the pool of session temporary tablespaces.

### [Tuning Aurora MySQL with thread states](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Tuning.thread-states.html)

Tune Aurora MySQL with thread states using this table that summarizes the most common general thread states for Aurora MySQL.

- [creating sort index](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-states.sort-index.html): The creating sort index thread state for Amazon Aurora indicates that a thread is processing a SELECT statement that requires the use of an internal temporary table to sort the data.
- [sending data](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-states.sending-data.html): The sending data thread state for Amazon Aurora indicates that a thread is reading and filtering rows for a query to determine the correct result set.

### [Tuning Aurora MySQL with Amazon DevOpsÂ Guru proactive insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/MySQL.Tuning.proactive-insights.html)

Tune your Aurora MySQL DB cluster by following the recommendations in your DevOpsÂ Guru proactive insights.

- [The InnoDB history list length increased significantly](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/proactive-insights.history-list.html): Starting on date, your history list for row changes increased significantly, up to length on db-instance.
- [Database is creating temporary tables on disk](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/proactive-insights.temp-tables.html): Your recent on-disk temporary table usage increased significantly, up to percentage.

### [Parallel query for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.html)

Use the parallel query optimization feature of Amazon Aurora MySQL.

- [Creating a parallel query cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query-creating-cluster.html): Create an Aurora MySQL DB cluster that works with parallel query.
- [Turning parallel query on and off](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query-enabling.html): Turn parallel query on and off for your Aurora MySQL DB cluster.
- [Optimizing parallel query](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query-optimizing.html): Optimize your Aurora MySQL DB cluster for parallel query.
- [Verifying parallel query usage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query-verifying.html): Check if a query is using parallel query.
- [Monitoring parallel query](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query-monitoring.html): Monitor Aurora MySQL DB clusters that use parallel query.
- [SQL constructs for parallel query](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query-sql.html): Determine which SQL statements do or don't use parallel query.
- [Advanced Auditing with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Auditing.html): Audit the activity in your Amazon Aurora MySQL DB cluster.

### [Replication with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.html)

Read-scale your data using Aurora Replicas in an Amazon Aurora MySQL DB cluster.

- [Replication filters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.Filters.html): Use replication filters to specify which databases and tables are replicated.

### [Cross-Region replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.html)

You can create an Amazon Aurora MySQL DB cluster as a read replica in a different AWS Region than the source DB cluster.

- [Creating a cross-Region read replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.Creating.html): Create an Aurora MySQL DB cluster that is a cross-Region read replica using the AWS Management Console, AWS CLI, or Amazon RDS API.
- [Promoting a read replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.Promote.html): Promoting a read replica to a DB cluster for Aurora MySQL.
- [Troubleshooting cross-Region replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.CrossRegion.Troubleshooting.html): Troubleshoot error messages when creating cross-Region read replicas for Aurora MySQL.

### [Binary log (binlog) replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.html)

Use binary log (binlog) replication to replicate between a MySQL database and an Amazon Aurora MySQL DB cluster.

- [Setting up binlog replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.SettingUp.html): Set up binlog replication with MySQL or another Aurora DB cluster.
- [Stopping binlog replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.Stopping.html): Stop binary log replication between Aurora and MySQL or between Aurora and another Aurora DB cluster.
- [Scaling MySQL reads](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.ReadScaling.html): Scale reads for your MySQL DB instance using binlog replication in Amazon Aurora.
- [Optimizing binlog replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/binlog-optimization.html): Optimize binlog replication and troubleshoot issues in Aurora MySQL.
- [Setting up enhanced binlog](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Enhanced.binlog.html): Set up enhanced binlog for Aurora MySQL DB clusters.

### [GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-replication-gtid.html)

Replicate data based on global transaction IDs (GTIDs) for Amazon Aurora MySQL.

- [Enabling GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-replication-gtid.configuring-aurora.html): Enabling GTID-based replication for an Aurora MySQL cluster.
- [Disabling GTID-based replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-replication-gtid.disabling.html): Disable GTID-based replication for an Aurora cluster.

### [Local write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-write-forwarding.html)

Learn how to use local write forwarding with Aurora MySQL.

- [Enabling local write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-write-forwarding-enabling.html): Enable local write forwarding for your Aurora MySQL DB cluster.
- [Read consistency](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-write-forwarding-consistency.html): Adjust read consistency for write forwarding.
- [Metrics for write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-write-forwarding-cloudwatch.html): A reference of metrics for write forwarding for Aurora MySQL.

### [Integrating Aurora MySQL with AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.html)

Amazon Aurora MySQL integrates with other AWS services so that you can extend your Aurora MySQL DB cluster to use additional capabilities in the AWS Cloud.

### [Authorizing Aurora MySQL to access AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.html)

Authorize Aurora MySQL to access other AWS services on your behalf.

### [Setting up IAM roles to access AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.html)

To permit your Aurora DB cluster to access another AWS service, do the following:

- [Creating an IAM policy to access Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.S3CreatePolicy.html): Aurora can access Amazon S3 resources to either load data to or save data from an Aurora DB cluster.
- [Creating an IAM policy to access Lambda](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.LambdaCreatePolicy.html): You can create an IAM policy that provides the minimum required permissions for Aurora to invoke an AWS Lambda function on your behalf.
- [Creating an IAM policy to access CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.CWCreatePolicy.html): Aurora can access CloudWatch Logs to export audit log data from an Aurora DB cluster.
- [Creating an IAM policy to access AWS KMS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.KMSCreatePolicy.html): Aurora can access the AWS KMS keys used for encrypting their database backups.
- [Creating an IAM role to access AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.CreateRole.html): After creating an IAM policy to allow Aurora to access AWS resources, you must create an IAM role and attach the IAM policy to the new IAM role.
- [Associating an IAM role with a DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.AddRoleToDBCluster.html): Learn how to permit database users in an Amazon Aurora DB cluster to access other AWS services by associating an IAM role with the DB cluster.
- [Enabling network communication to AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.Network.html): To use certain other AWS services with Amazon Aurora, the network configuration of your Aurora DB cluster must allow outbound connections to endpoints for those services.
- [Loading data from text files in Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LoadFromS3.html): Load data from text files stored in an Amazon S3 bucket into an Aurora MySQL DB cluster.
- [Saving data into text files in Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.SaveIntoS3.html): Save data from an Aurora MySQL DB cluster into text files stored in an Amazon S3 bucket.

### [Invoking a Lambda function from Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html)

Invoke a Lambda function from an Aurora MySQL DB cluster.

- [Giving Aurora access to Lambda](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.LambdaAccess.html): Before you can invoke Lambda functions from an Aurora MySQL DB cluster, make sure to first give your cluster permission to access Lambda.
- [Invoking a Lambda function with a native function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.NativeLambda.html): Invoke a Lambda function from an Aurora MySQL DB cluster with a native function.
- [Invoking a Lambda function with a stored procedure (deprecated)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.ProcLambda.html): Invoke a Lambda function from an Aurora MySQL DB cluster with a stored procedure.
- [Publishing Aurora MySQL logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.CloudWatch.html): Publish general, slow, audit, and error logs from Aurora MySQL to CloudWatch Logs.
- [Aurora MySQL lab mode](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.LabMode.html)

### [Best practices with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.html)

Follow these best practices when using Amazon Aurora MySQL.

- [Best practices for performance and scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.Performance.html): Apply best practices for performance and scalability for Aurora MySQL.
- [Best practices for high availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.HA.html): Apply best practices for high availability for Aurora MySQL.
- [Recommendations for MySQL features](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.FeatureRecommendations.html): Apply recommendations for MySQL features for your Aurora MySQL DB clusters.
- [Evaluating DB instance usage for Aurora MySQL with Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.BestPractices.CW.html): You can use Amazon CloudWatch metrics to monitor your DB instance throughput and determine whether your DB instance class provides sufficient resources for your applications.

### [Troubleshooting Aurora MySQL performance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting.html)

Learn how to troubleshoot the performance of your Aurora MySQL DB cluster.

### [Troubleshooting workload issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-workload.html)

Learn about Aurora MySQL database workload issues and troubleshooting them.

- [Troubleshooting Aurora MySQL memory usage issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-workload-memory.html): Learn how to troubleshoot memory usage issues for Aurora MySQL databases.
- [Troubleshooting Aurora MySQL out-of-memory issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQLOOM.html): Learn how to troubleshoot out-of-memory issues for Aurora MySQL databases.
- [Logging for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-logging.html): Learn about Aurora MySQL database logs.
- [Troubleshooting database connection issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-troubleshooting-dbconn.html): Learn about troubleshooting Aurora MySQL database connection issues.
- [Troubleshooting query performance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-mysql-troubleshooting-query.html): Learn about troubleshooting Aurora MySQL database query performance.

### [Aurora MySQL reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.html)

Find reference information for Aurora MySQL.

- [Configuration parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html): Manage your Aurora MySQL DB cluster using DB cluster parameter groups and DB parameter groups.
- [Global status variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.GlobalStatusVars.html): Aurora MySQL includes status variables from community MySQL and variables that are unique to Aurora.
- [Wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.Waitevents.html): Learn about common wait events for Aurora MySQL.
- [Thread states](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.thread-states.html): Learn about common thread states for Aurora MySQL.
- [Isolation levels](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.IsolationLevels.html): Learn how DB instances in an Aurora MySQL cluster implement the database property of isolation.
- [Hints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.Hints.html): Learn how to use SQL hints with Aurora MySQL queries to fine-tune performance.

### [Stored procedure reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.StoredProcs.html)

Manage your Aurora MySQL DB cluster by calling built-in stored procedures.

- [Collecting and maintaining the Global Status History](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-gsh.html): Amazon RDS provides a set of procedures that take snapshots of the values of status variables over time and write them to a table, along with any changes since the last snapshot.
- [Configuring, starting, and stopping binary log (binlog) replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html): Learn about configuring, starting, and stopping binary log (binlog) replication in MySQL databases.
- [Ending a session or query](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-ending.html): The following stored procedures end a session or query.
- [Replicating transactions using GTIDs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-gtid.html): The following stored procedures control how transactions are replicated using global transaction identifiers (GTIDs) with Aurora MySQL.
- [Rotating the query logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-logging.html): The following stored procedures rotate MySQL logs to backup tables.
- [Setting and showing binary log configuration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-configuring.html): The following stored procedures set and show configuration parameters, such as for binary log file retention.
- [information_schema tables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ISTables.html): Learn about specific information schema tables that you can use to get status information for your Aurora MySQL databases.

### [Aurora MySQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.html)

Learn how and when Amazon Aurora applies updates.

- [Checking version numbers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Versions.html): Find out about Aurora MySQL features and bug fixes that are specific to particular Aurora MySQL versions.
- [Long-term support and beta releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Update.SpecialVersions.html): Special versions for Aurora MySQL, including long-term support and beta release versions.
- [Preparing for Aurora MySQL version 2 end of life](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.MySQL57.EOL.html): Prepare to upgrade from Amazon Aurora MySQL-Compatible Edition version 2 to Aurora MySQL version 3 before version 2 reaches the end of its support period.
- [Preparing for Aurora MySQL version 1 end of life](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.MySQL56.EOL.html): Prepare to upgrade from Amazon Aurora MySQL-Compatible Edition version 1 to Aurora MySQL version 2 or Aurora MySQL version 3 before version 1 reaches the end of its support period.

### [Upgrading Amazon Aurora MySQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Upgrading.html)

Upgrade your Aurora MySQL DB cluster to get bug fixes, new features, or change engine versions.

### [Upgrading the minor version or patch level of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.html)

Upgrade the minor version or patch your DB cluster.

- [Modifying the engine version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.Patching.ModifyEngineVersion.html): Upgrading the minor version of an Aurora MySQL DB cluster applies additional fixes and new features to an existing cluster.
- [Enabling automatic upgrades between minor versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.AMVU.html)
- [Using zero-downtime patching](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.ZDP.html)

### [Upgrading the major version of an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.MajorVersionUpgrade.html)

Upgrade between Amazon Aurora MySQL major versions for a DB cluster.

### [Major version upgrade prechecks for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.upgrade-prechecks.html)

Learn about major version upgrade prechecks for Aurora MySQL.

- [Precheck descriptions reference for Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.upgrade-prechecks.descriptions.html): Learn about the prechecks for upgrading Amazon Aurora MySQL.
- [How to perform an in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Upgrading.Procedure.html): Learn how to perform an in-place upgrade of Aurora MySQL.
- [Aurora MySQL in-place upgrade tutorial](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Upgrading.Tutorial.html): Learn how to perform the in-place upgrade procedure for Aurora MySQL using the AWS CLI.
- [Finding the reasons for major version upgrade failures](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Upgrading.failure-events.html): Learn how to find the reasons for Aurora MySQL major version upgrade failures.
- [Troubleshooting for Aurora MySQL in-place upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Upgrading.Troubleshooting.html): Use the following tips to help troubleshoot problems with Aurora MySQL in-place upgrades.
- [Post-upgrade cleanup for Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.mysql80-post-upgrade.html): Learn about cleanup actions that you can perform after upgrading from Aurora MySQL version 2 to Aurora MySQL version 3.
- [Database engine updates and fixes for Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Updates.RN.html): See the Release notes for Amazon Aurora MySQL-Compatible Edition for information about database engine updates and fixes for Amazon Aurora MySQL.


## [Working with Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.html)

- [The database preview environment](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/working-with-the-apg-database-preview-environment.html): Learn how to work with the Aurora PostgreSQL database preview environment

### [Security with Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.html)

Security with Amazon Aurora PostgreSQL.

### [Understanding PostgreSQL roles and permissions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.html)

Learn how to use PostgreSQL roles and permissions in yourAurora PostgreSQL DB cluster

### [Understanding the rds_superuser role](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.rds_superuser.html)

In PostgreSQL, a role can define a user, a group, or a set of specific permissions granted to a group or user for various objects in the database.

- [Viewing roles and privileges](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Roles.View.html): Learn how to view predefined roles and their privileges in your RDS for PostgreSQL DB instance.
- [Controlling user access to PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Access.html): Control user access to the PostgreSQL database.
- [Delegating and controlling user password management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.RestrictPasswordMgmt.html): Delegating and controlling user password management by using the rds_password role.
- [Using SCRAM for PostgreSQL password encryption](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_Password_Encryption_configuration.html): Using SCRAM on your Aurora PostgreSQL DB cluster

### [Aurora PostgreSQL dynamic masking](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.html)

Dynamic data masking is a security feature that protects sensitive data in Aurora PostgreSQL databases by controlling how data appears to users at query time.

- [Getting started](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.GetStarted.html): To dynamically mask data, you install the pg_columnmask extension in your database and create masking policies for your tables.
- [Data masking policies](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.Procedures.html): You can manage masking policies using procedures provided by the pg_columnmask extension.
- [Escape identifiers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.EscapeIdentifiers.html): When creating data masking policies with quoted identifiers, proper escaping is required to ensure correct object references and policy application.
- [Data masking functions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.PredefinedMaskingFunctions.html): pg_columnmask extension provides built-in utility functions written in C language (for faster execution) which can be used as masking expression for pg_columnmask policies.
- [End-to-end workflow](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.WorkflowExample.html): This section demonstrates a complete implementation of pg_columnmask using a sample employee table with sensitive data.
- [Masking in DML](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.DMLMasking.html): pg_columnmask applies consistently across all DML operations, including INSERT, UPDATE, DELETE, and MERGE statements.
- [Masking in trigger functions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.TriggerFunctionMasking.html): When pg_columnmask policies are applied to tables, it's important to understand how masking interacts with trigger functions.
- [Masking policy management role](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.PolicyManagementRole.html): The PostgreSQL column masking extension, pg_columnmask, allows you to delegate the management of masking policies to a specific role, rather than requiring rds_superuser or table owner privileges.
- [Best practices](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.BestPractices.html): The following section provides security best practices for implementing pg_columnmask in your Aurora PostgreSQL environment.
- [Data movement scenarios](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Security.DynamicMasking.DataMovement.html): pg_columnmask behavior varies across different data movement operations depending on whether the operation occurs at the storage, logical, or application layer.
- [Updating applications for new SSL/TLS certificates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ssl-certificate-rotation-aurora-postgresql.html): Update applications that connect to Aurora PostgreSQL DB clusters for SSL/TLS certificate rotation.

### [Using Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-kerberos.html)

Use Kerberos authentication with Aurora PostgreSQL DB clusters.

- [Setting up](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-kerberos-setting-up.html): You use AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD) to set up Kerberos authentication for a PostgreSQL DB cluster.
- [Managing an Aurora PostgreSQL DB cluster in an Active Directory domain](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-kerberos-managing.html): You can use the console, the CLI, or the RDS API to manage your DB cluster and its relationship with your Microsoft Active Directory.
- [Connecting with Kerberos authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-kerberos-connecting.html): You can connect to PostgreSQL with Kerberos authentication with the pgAdmin interface or with a command-line interface such as psql.
- [Using AD security groups for Aurora PostgreSQL access control](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AD.Security.Groups.html): Using AD security groups for Aurora PostgreSQL access control.

### [Migrating data to Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Migrating.html)

Migrate (copy) data from an RDS for PostgreSQL DB snapshot to an Amazon Aurora PostgreSQL-Compatible Edition DB cluster.

- [Migrating an RDS for PostgreSQL DB instance using a snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Migrating.RDSPostgreSQL.Import.Console.html): Migrate (copy) an RDS for PostgreSQL DB snapshot to an Aurora PostgreSQL DB cluster.
- [Migrating an RDS for PostgreSQL DB instance using an Aurora read replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Migrating.RDSPostgreSQL.Replica.html): Migrate (copy) an RDS for PostgreSQL DB instance to an Aurora PostgreSQL DB cluster by using an Aurora read replica.

### [Optimizing query performance in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimizing.queries.html)

Learn how to optimize query performance in Aurora PostgreSQL using different methods.

- [Improving query performance with Aurora Optimized Reads](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.html): Learn how to achieve faster query processing for Aurora PostgreSQL with Aurora Optimized Reads.
- [Optimizing correlated subqueries in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-correlated-subquery.html): A correlated subquery references table columns from the outer query.
- [Improving query performance using adaptive join](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/user-apg-adaptive-join.html): Learn how to use adaptive join to improve query performance in Aurora PostgreSQL 17.4 by dynamically switching join strategies at runtime.
- [Using shared plan cache](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-shared-plan-cache.html)
- [Working with unlogged tables in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-unlogged-tables.html): Learn how to use unlogged tables in Aurora PostgreSQL.

### [Working with PostgreSQL autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.html)

Learn how PostgreSQL autovacuum works with Amazon RDS for PostgreSQL and how to use it.

- [Determining if the tables in your database need vacuuming](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.NeedVacuuming.html): You can use the following query to show the number of unfrozen transactions in a database.
- [Determining which tables are currently eligible for autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.EligibleTables.html): Often, it is one or two tables in need of vacuuming.
- [Determining if autovacuum is currently running and for how long](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AutovacuumRunning.html): If you need to manually vacuum a table, make sure to determine if autovacuum is currently running.
- [Performing a manual vacuum freeze](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.VacuumFreeze.html): You might want to perform a manual vacuum on a table that has a vacuum process already running.
- [Reindexing a table when autovacuum is running](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.Reindexing.html): If an index has become corrupt, autovacuum continues to process the table and fails.
- [Managing autovacuum with large indexes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.html): As part of its operation, autovacuum performs several vacuum phases while running on a table.
- [Other parameters that affect autovacuum](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.OtherParms.html): The following query shows the values of some of the parameters that directly affect autovacuum and its behavior.
- [Setting table-level autovacuum parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.TableParameters.html): You can set autovacuum-related storage parameters at a table level, which can be better than altering the behavior of the entire database.
- [Logging autovacuum and vacuum activities](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.Logging.html): Information about autovacuum activities is sent to the postgresql.log based on the level specified in the rds.force_autovacuum_logging_level parameter.
- [Understanding the behavior of autovacuum with invalid databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/appendix.postgresql.commondbatasks.autovacuumbehavior.html): Understand the behavior of autovacuum with invalid databases.

### [Identifying vacuum blockers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.html)

Identify and resolve aggressive vacuum blockers in Aurora PostgreSQL.

- [Installing autovacuum monitoring tools](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Installation.html): Installing autovacuum monitoring and diagnostic tools in Aurora PostgreSQL
- [Functions of postgres_get_av_diag()](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Functions.html): Functions of postgres_get_av_diag() in Aurora PostgreSQL
- [Resolving identifiable vacuum blockers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Resolving_Identifiableblockers.html): Resolving vacuum blockers in Aurora PostgreSQL
- [Resolving unidentifiable vacuum blockers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Unidentifiable_blockers.html): Resolving unidentifiable vacuum blockers in Aurora PostgreSQL
- [Resolving vacuum performance issues](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Resolving_Performance.html): Resolving vacuum performance issues on Aurora PostgreSQL
- [Explanation of the NOTICE messages](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.NOTICE.html): Explanation of the NOTICE messages in Aurora PostgreSQL
- [Managing TOAST OID contention](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.html): Identify and manage TOAST OID contention issues in your PostgreSQL databases.

### [Using Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html)

Set up Babelfish for Aurora PostgreSQL and migrate your SQL Server databases to Aurora PostgreSQL-Compatible Edition.

- [Babelfish limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-limitations.html): The following limitations currently apply to Babelfish for Aurora PostgreSQL:

### [Understanding Babelfish architecture and configuration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-understanding-overview-howitworks.html)

You manage the Aurora PostgreSQL-Compatible Edition DB cluster running Babelfish much as you would any Aurora DB cluster.

- [Babelfish architecture](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-architecture.html): When you create an Aurora PostgreSQL cluster with Babelfish turned on, Aurora provisions the cluster with a PostgreSQL database named babelfish_db.
- [DB cluster parameter group settings for Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-configuration.html): Configure a database for Babelfish using DB cluster parameter group settings.

### [Understanding Collations in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-collations.html)

Learn how Babelfish handles SQL Server collations and locales, and some of the differences.

- [Managing collations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/collation.managing.html): Manage collations in Babelfish for Aurora PostgreSQL.
- [Collation limitations and differences](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/collation.limitations.html): Learn about collation, locale, and language-representation limitations in Babelfish.
- [Managing Babelfish error handling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-strict.html): Manage how Babelfish handles errors by using escape hatches.
- [Creating a Babelfish for Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-create.html): Create a Babelfish Aurora DB cluster
- [Migrating a SQL Server database to Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-migration.html): Use Babelfish for Aurora PostgreSQL to ease migration from a SQL Server database to an Amazon Aurora PostgreSQL DB cluster.

### [Database authentication with Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-db-authentication.html)

Different database authentication methods with Babelfish for Aurora PostgreSQL.

- [Kerberos authentication with Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-active-directory.html): Kerberos authentication with Babelfish.

### [Setting up Kerberos authentication using Active Directory security groups for Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad.html)

Show how to set up Kerberos authentications using AD security groups.

- [Mapping T-SQL group logins with AD security group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad-maptsql.html): You need to explicitly provision T-SQL Windows Group Login for each AD security group that requires access to the database server.
- [Connecting to Babelfish via TDS endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad-connect.html): In the following example, user1 is member of accounts-group and sales-group, user2 is member of accounts-group and dev-group.
- [Utilizing privileges of AD security group membership](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad-privileges.html)
- [Handling DDL Statement behavior based on default or explicit schema](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad-ddl.html): When using an AD authenticated session, the default schema for the current session is determined by the following conditions:
- [Limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad-limitations.html)
- [Connecting to Babelfish via PostgreSQL endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-kerberos-securityad-connect-pgendpoint.html): You can utilize group logins created from the TDS port to connect through PostgreSQL port as well.

### [Connecting to a Babelfish DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-connect.html)

Connect to a Babelfish for Aurora PostgreSQL DB cluster.

- [Creating C# or JDBC client connections to Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-connect-configure.html): Creating client connections to Babelfish using C# or JDBC classes.
- [Using a SQL Server client to connect to your DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-connect-sqlserver.html): Use a SQL Server client to connect to your DB cluster for Babelfish for Aurora PostgreSQL.
- [Using a PostgreSQL client to connect to your DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-connect-PostgreSQL.html): Use a PostgreSQL client to connect to your DB cluster for Babelfish for Aurora PostgreSQL.

### [Working with Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/working-with-babelfish-usage-notes-features.html)

Following, you can find usage information for Babelfish, including some of the differences between working with Babelfish and SQL Server, and between Babelfish and PostgreSQL databases.

- [Getting information from the Babelfish system catalog](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-query-database.html): Query your database for Babelfish object information.

### [Managing permissions and access control in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-permissions.html)

In Babelfish for Aurora PostgreSQL, you can manage permissions and access control for databases, schemas, and objects.

- [Object ownership differences](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-ownership-differences.html): Babelfish versions 4.6 and later, and 5.2 and later include a change to object ownership handling through the TDS endpoint.

### [Differences between Babelfish for Aurora PostgreSQL and SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.html)

Learn about the differences between SQL Server and Babelfish as implemented in Aurora PostgreSQL.

- [T-SQL differences in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.tsql.limitations.html): Functionality or behavior differences when using T-SQL with Babelfish

### [Transaction isolation levels in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-transaction.html)

Learn how Babelfish handles SQL Server collations and locales, and some of the differences.

- [Comparing Babelfish and SQL Server isolation levels](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-transaction.examples.html): Below are a few examples on the nuances in how SQL Server and Babelfish implement the ANSI isolation levels.
- [Using Babelfish features with limited implementation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.tsql.limited-implementation.html): Each new version of Babelfish adds support for features that better align with T-SQL functionality and behavior.

### [Improving Babelfish query performance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-query-performance.html)

Show methods to improve Babelfish query performance.

- [Using explain plan to improve query performance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/working-with-babelfish-usage-notes-features.using.explain.html): Use the Babelfish implementation of EXPLAIN to analyze query execution plans to improve your SQL queries.
- [Using T-SQL query hints to improve Babelfish query performance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-tsql-hints.html): Use T-SQL query hints to improve Babelfish query performance.
- [Using Aurora PostgreSQL extensions with Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-aws-extensions.html): Use Amazon Aurora PostgreSQL extensions with Babelfish.
- [Babelfish supports linked servers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-linkedservers.html): Use Amazon Aurora PostgreSQL extensions with Babelfish.
- [Using Full Text Search in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-postgres-fulltextsearch.html): Use Full Text Searching in Babelfish.
- [Babelfish supports Geospatial data types](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-geospatial.html): Babelfish supports Geospatial data types.
- [Understanding partitioning in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-partition.html): Starting with version 4.3.0, Babelfish introduces table and index partitioning with limited support.
- [Troubleshooting Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-troubleshooting.html): Troubleshoot issues with Babelfish for Aurora PostgreSQL.
- [Turning off Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-remove.html): If you no longer need Babelfish, turn off its functionality.

### [Managing Babelfish version updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information.html)

Learn about the Babelfish versions supported by Aurora PostgreSQL.

- [Identifying your version of Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-identify-version.html): Get Amazon Aurora and Babelfish version information from your Babelfish DB cluster.

### [Upgrading Babelfish to a new version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-upgrading.html)

New versions of Babelfish become available with some new releases of the Aurora PostgreSQL database engine after version 13.4.

- [Babelfish minor version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-upgrading-minor.html): A minor version update aims to maintain backward compatibility.
- [Babelfish major version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-information-upgrading-major.html): For a major version upgrade, you need to first upgrade your Babelfish for Aurora PostgreSQL DB cluster to a version that supports the major version upgrade.
- [Using Babelfish product version parameter](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-guc-version.html): A new Grand Unified Configuration (GUC) parameter called babelfishpg_tds.product_version is introduced from Babelfish 2.4.0 and 3.1.0 versions.

### [Babelfish reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_AuroraPostgreSQL_Babelfish_Reference.html)

- [Supported functionalities in Babelfish by version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.supported-functionality-table.html): Find supported functionality for different Babelfish versions.
- [Unsupported functionalities in Babelfish](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-compatibility.tsql.limitations-unsupported.html): Find unsupported functionality for Babelfish.

### [Working with Babelfish procedures](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.Babelfish.Functions.html)

Find a description of procedures that are available for Amazon RDS instances running the Babelfish for Aurora PostgreSQL DB engine.

- [sp_babelfish_volatility](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/sp_babelfish_volatility.html): Decides how this function is used in query execution when used in parts of certain clauses.
- [sp_execute_postgresql](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/sp_execute_postgresql.html): Executes postgresql statements from T-SQL endpoint.
- [Babelfish supports XML datatype methods](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-xml-datatype-methods.html): Babelfish supports XML datatype methods.

### [Performance and scaling for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.html)

Managing Amazon Aurora PostgreSQL.

- [Testing Amazon Aurora PostgreSQL by using fault injection queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.FaultInjectionQueries.html): You can test the fault tolerance of your Aurora PostgreSQL DB cluster by using fault injection queries.
- [Displaying volume status for an Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.VolumeStatus.html): In Amazon Aurora, a DB cluster volume consists of a collection of logical blocks.
- [Specifying the RAM disk for the stats_temp_directory](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Managing.RamDisk.html): You can use the Aurora PostgreSQL parameter, rds.pg_stat_ramdisk_size, to specify the system memory allocated to a RAM disk for storing the PostgreSQL stats_temp_directory.

### [Managing temporary files with PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ManagingTempFiles.html)

Managing temporary files with PostgreSQL

- [Viewing temporary file usage with Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.ManagingTempFiles.Example.html): You can use Performance Insights to view temporary file usage by turning on the metrics temp_bytes and temp_files.

### [Tuning with wait events for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.html)

Tune with wait events for Amazon Aurora PostgreSQL-Compatible Edition.

- [Essential concepts for Aurora PostgreSQL tuning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.concepts.html): Learn some essential concepts for Amazon Aurora PostgreSQL-Compatible Edition tuning.
- [Aurora PostgreSQL wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Tuning.concepts.summary.html): Find a table that lists the wait events for Aurora PostgreSQL that most commonly indicate performance problems, with most common causes and corrective actions.
- [Client:ClientRead](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.clientread.html): The Client:ClientRead event occurs when Aurora PostgreSQL is waiting to receive data from the client.
- [Client:ClientWrite](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.clientwrite.html): The Client:ClientWrite event occurs when Aurora PostgreSQL is waiting to write data to the client.
- [CPU](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.cpu.html): The CPU wait event occurs when a thread is active in CPU or is waiting for CPU.
- [IO:BufFileRead and IO:BufFileWrite](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.iobuffile.html): The IO:BufFileRead and IO:BufFileWrite events occur when Aurora PostgreSQL creates temporary files.
- [IO:DataFileRead](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.iodatafileread.html): The IO:DataFileRead event occurs in Aurora PostgreSQL when a connection waits on a backend process to read a required page from storage because the page isn't available in shared memory.
- [IO:XactSync](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.xactsync.html): The IO:XactSync event occurs when the database is waiting for the Aurora storage subsystem to acknowledge the commit of a regular transaction, or the commit or rollback of a prepared transaction.
- [IPC:DamRecordTxAck](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.ipcdamrecordtxac.html): The IPC:DamRecordTxAck event occurs when Aurora PostgreSQL generates an activity stream event and waits for the event to become durable.
- [IPC:parallel wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-ipc-parallel.html): The IPC:BgWorkerShutdown, IPC:BgWorkerStartup, IPC:ExecuteGather, and IPC:ParallelFinish wait events indicate that a session is waiting for inter-process communication related to parallel query execution operations.
- [IPC:ProcArrayGroupUpdate](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-rpg-ipcprocarraygroup.html): The IPC:ProcArrayGroupUpdate event occurs when a session is waiting for the group leader to update the transaction status at the end of that operation.
- [Lock:advisory](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lockadvisory.html): The Lock:advisory event occurs when a PostgreSQL application uses a lock to coordinate activity across multiple sessions.
- [Lock:extend](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lockextend.html): The Lock:extend event occurs when a backend process is waiting to lock a relation to extend it while another process has a lock on that relation for the same purpose.
- [Lock:Relation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lockrelation.html): The Lock:Relation event occurs when a query is waiting to acquire a lock on a table or view that's currently locked by another transaction.
- [Lock:transactionid](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.locktransactionid.html): The Lock:transactionid event occurs when a transaction is waiting for a row-level lock.
- [Lock:tuple](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.locktuple.html): The Lock:tuple event for Aurora PostgreSQL occurs when a backend process is waiting to acquire a lock on a tuple.
- [LWLock:buffer_content (BufferContent)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lockbuffercontent.html): The LWLock:buffer_content event occurs when a session is waiting to read or write a data page in memory while another session has that page locked for writing.
- [LWLock:buffer_mapping](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lwl-buffer-mapping.html): This event occurs when a session is waiting to associate a data block with a buffer in the shared buffer pool.
- [LWLock:BufferIO (IPC:BufferIO)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lwlockbufferio.html): The LWLock:BufferIO event occurs when Aurora PostgreSQL or RDS for PostgreSQL is waiting for other processes to finish their I/O operations.
- [LWLock:lock_manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lw-lock-manager.html): The LWLock:lock_manager wait event occurs when the Aurora PostgreSQL engine maintains the shared lock's memory area to allocate, check, and deallocate a lock when a fast path lock is not possible.
- [LWLock:MultiXact](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.lwlockmultixact.html): The LWLock:MultiXact
- [LWLock:pg_stat_statements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-rpg-lwlockpgstat.html): The LWLock:pg_stat_statements wait event occurs when the pg_stat_statements extension takes an exclusive lock on the hash table that tracks SQL statements.
- [Timeout:PgSleep](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/apg-waits.timeoutpgsleep.html): The Timeout:PgSleep event occurs in Aurora PostgreSQL when a server process has called the pg_sleep function and is waiting for the sleep timeout to expire.
- [Tuning Aurora PostgreSQL with Amazon DevOpsÂ Guru proactive insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL.Tuning_proactive_insights.html): Tune your Aurora PostgreSQL DB cluster by following the recommendations in your DevOpsÂ Guru proactive insights.

### [Best practices with Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.html)

Follow these best practices when using Amazon Aurora PostgreSQL.

- [Diagnosing table and index bloat](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.diag-table-ind-bloat.html): Diagnosing table and index bloat in Amazon Aurora PostgreSQL-Compatible Edition.
- [Improved memory management in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.management.html): Aurora PostgreSQL now includes advanced memory management capabilities to optimize database performance and resilience under varying workloads.
- [Fast failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.FastFailover.html): Learn how to make sure that failover occurs in Amazon Aurora PostgreSQL as fast as possible.
- [Fast recovery after failover](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.cluster-cache-mgmt.html): Recover quickly after failover with cluster cache management for Amazon Aurora PostgreSQL-Compatible Edition.
- [Managing connection churn](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.connection_pooling.html): Identify connection churn on your Aurora PostgreSQL-Compatible Edition DB cluster and see how connection pooling can help.
- [Dead connection handling in PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.html): Learn how to manage dead connections in PostgreSQL and configure TCP keepalive parameters for optimal connection handling.
- [Tuning memory parameters for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.Tuning-memory-parameters.html): Learn how to use various parameters on your Aurora PostgreSQL-Compatible Edition DB cluster to avoid "out of memory" errors and other memory-related issues.
- [Analyze resource usage with CloudWatch metrics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL_AnayzeResourceUsage.html): Steps to analyze resource usage for Aurora PostgreSQL using CloudWatch metrics.
- [Using logical replication for a major version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.MajorVersionUpgrade.html): Follow these steps to perform a low downtime major version upgrade for Aurora PostgreSQL using logical replication.
- [Troubleshooting storage issues in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.BestPractices.TroubleshootingStorage.html): If the amount of working memory needed for sort or index-creation operations exceeds the amount allocated by the work_mem parameter, Aurora PostgreSQL writes the excess data to temporary disk files.

### [Replication with Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.html)

Replicate data with Amazon Aurora PostgreSQL.

- [Overview of logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.html): Use logical replication to replicate and synchronize individual tables.
- [Setting up logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.Configure.html): Set up logical replication for your Aurora PostgreSQL DB cluster.
- [Turning off logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.Stop.html): Turn off logical replication for your Aurora PostgreSQL DB cluster.
- [Monitoring the write-through cache and logical slots](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical-monitoring.html): Monitor the logical replication write-through cache and manage logical slots to improve performance for your Aurora PostgreSQL DB cluster.
- [Example: Using logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.PostgreSQL-Example.html): Start logical replication between two Aurora PostgreSQL DB cluster.
- [Example: Logical replication using Aurora PostgreSQL and AWS DMS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.DMS-Example.html): Replicate a database using Aurora PostgreSQL and AWS Database Migration Service.
- [Configuring IAM authentication for logical replication connections](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Replication.Logical.IAM-auth.html): Understand how IAM authentication works for logical replication and its security model.

### [Local write forwarding in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding.html)

Learn how to use local write forwarding with Aurora PostgreSQL.

- [Limitations and considerations of local write forwarding in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding-limitations.html): The following limitations currently apply to local write forwarding in Aurora PostgreSQL:
- [Configuring Aurora PostgreSQL for Local write forwarding](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding-configuring.html): Using the following sections, you can enable local write forwarding for your Amazon Aurora PostgreSQL DB cluster, configuring consistency levels, and managing transactions with write forwarding.
- [Working with local write forwarding for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding-understanding.html): Using the following sections, you can check if a database cluster has local write forwarding enabled, view compatibility considerations, and see configurable parameters and authentication setup.
- [Monitoring local write forwarding in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-postgresql-write-forwarding-monitoring.html): Using the following sections you can monitor local write forwarding in Aurora PostgreSQL clusters, including relevant CloudWatch metrics and wait events to track performance and identify potential issues.

### [Using Aurora PostgreSQL as a Knowledge Base for Amazon Bedrock](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.VectorDB.html)

Learn how to use Aurora PostgreSQL as a Knowledge Base

- [Quick create an Aurora PostgreSQL Knowledge Base for Amazon Bedrock](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.quickcreatekb.html): Learn how to quick create Aurora PostgreSQL as a Knowledge Base

### [Integrating Aurora PostgreSQL with AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Integrating.html)

Amazon Aurora integrates with other AWS services so that you can extend your Aurora PostgreSQL DB cluster to use additional capabilities in the AWS Cloud.

### [Importing data from Amazon S3 into Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.html)

Import data from Amazon Simple Storage Service into an Aurora PostgreSQL DB cluster .

- [Installing the extension](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.InstallExtension.html): Before you can use Amazon S3 with your Aurora PostgreSQL DB cluster, you need to install the aws_s3 extension.
- [Overview of importing data from Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.Overview.html)
- [Setting up access to an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.AccessPermission.html): To import data from an Amazon S3 file, give the Aurora PostgreSQL DB cluster permission to access the Amazon S3 bucket containing the file.
- [Importing data from Amazon S3 to your Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.FileFormats.html): You import data from your Amazon S3 bucket by using the table_import_from_s3 function of the aws_s3 extension.
- [Function reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PostgreSQL.S3Import.Reference.html): Functions

### [Exporting PostgreSQL data to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export.html)

Export data from an Aurora PostgreSQL DB cluster into Amazon S3.

- [Setting up access to an Amazon S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export-access-bucket.html): To export data to Amazon S3, give your PostgreSQL DB cluster permission to access the Amazon S3 bucket that the files are to go in.
- [Exporting query data using the aws_s3.query_export_to_s3 function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export-examples.html): Export your PostgreSQL data to Amazon S3 by calling the function.
- [Function reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export-functions.html): Functions
- [Troubleshooting access to Amazon S3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-s3-export-troubleshoot.html): If you encounter connection problems when attempting to export data to Amazon S3, first confirm that the outbound access rules for the VPC security group associated with your DB instance permit network connectivity.

### [Invoking a Lambda function from Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda.html)

Invoke an AWS Lambda function from an Aurora PostgreSQL DB cluster .

- [Examples: Invoking Lambda functions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda-examples.html): Following, you can find several examples of calling the function.
- [Lambda function error messages](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda-errors.html): In the following list you can find information about error messages, with possible causes and solutions.
- [Lambda function and parameter reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda-functions.html): Following is the reference for the functions and parameters to use for invoking Lambda with Aurora PostgreSQL .

### [Publishing Aurora PostgreSQL logs to CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.CloudWatch.html)

Publish PostgreSQL logs from Aurora to CloudWatch Logs.

- [Turning on the option to publish logs to Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.CloudWatch.Publishing.html): Choose the Log export option for your Aurora PostgreSQL DB cluster to export to CloudWatch Logs.
- [Monitoring log events in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.CloudWatch.Monitor.html): View and monitor events using CloudWatch Logs with Aurora PostgreSQL log events exported to CloudWatch Logs.
- [Analyzing PostgreSQL logs using CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.CloudWatch.Analyzing.html): Analyze logs from your Aurora PostgreSQL published as CloudWatch Logs.
- [Monitoring query execution plans and peak memory for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.Plans.html): Monitoring query execution plans with aurora_compute_plan_id for Aurora PostgreSQL-Compatible Edition.

### [Managing query execution plans for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.html)

Manage PostgreSQL query execution plans with query plan management for Aurora PostgreSQL-Compatible Edition.

- [Overview of Aurora PostgreSQL query plan management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.overview.html): Aurora PostgreSQL query plan management is designed to ensure plan stability regardless of changes to the database that might cause query plan regression.
- [Best practices for Aurora PostgreSQL query plan management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.BestPractice.html): Techniques for optimal query plan management.
- [Query plan management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Start.html): Understand how Aurora PostgreSQL query plan management works with the optimizer.
- [Capturing Aurora PostgreSQL execution plans](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.CapturePlans.html): Capture execution plans.
- [Using Aurora PostgreSQL managed plans](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.UsePlans.html): Use managed plans.
- [Examining Aurora PostgreSQL query plans in the dba_plans view](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.ViewPlans.html): Examine plans in the dba_plans view.
- [Improving plans](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Maintenance.html): Improving execution plans.
- [Deleting plans](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Deleting.html): Delete execution plans that aren't valid.
- [Exporting and importing managed plans](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Maintenance.ExportingImporting.html): Export and import plans.
- [Parameter reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Parameters.html): Find descriptions of the parameters that control query plan management behavior.
- [Function reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.Functions.html): Find information about query plan management functions.
- [Reference for the apg_plan_mgmt.dba_plans view](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Optimize.dba_plans_view_Reference.html): Get reference information about the available columns in the dba_plans view.

### [Advanced features in Query Plan Management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.QPM.Advanced.html)

Following you can find information about the advanced Aurora PostgreSQL Query Plan Management (QPM) features:

- [Capturing Aurora PostgreSQL execution plans in Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.QPM.Plancapturereplicas.html): QPM (Query Plan Management) allows you to capture the query plans generated by Aurora Replicas and stores them on the primary DB instance of the Aurora DB cluster.
- [Supporting table partition by Query Plan Management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.QPM.Partitiontable.html): Aurora PostgreSQL Query Plan Management (QPM) supports declarative table partitioning in the following versions:

### [Working with extensions and foreign data wrappers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.html)

Add functionality to Amazon Aurora PostgreSQL with extensions and foreign data wrappers.

- [Using Amazon Aurora delegated extension support for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora_delegated_ext.html): Using Amazon Aurora delegated extension support for PostgreSQL, you can delegate the extension management to a user who need not be an rds_superuser.
- [Managing large objects more efficiently with the lo module](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_large_objects_lo_extension.html): If you work with PostgreSQL databases through JDBC or ODBC drivers when using Amazon Aurora PostgreSQL-Compatible Edition, you can avoid orphaned objects by using the lo extension.
- [Managing spatial data with PostGIS](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.PostGIS.html): Manage spatial data by installing and using the PostGIS extension with Amazon RDS for PostgreSQL.
- [Managing partitions with the pg_partman extension](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_Partitions.html): Create and manage Amazon RDS for PostgreSQL database table partitions using the pg_partman extension.
- [Scheduling maintenance with the pg_cron extension](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_pg_cron.html): You can use the PostgreSQL pg_cron extension to schedule maintenance commands within a PostgreSQL database.

### [Using pgAudit to log database activity](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.html)

Learn how to use the pgAudit extension to create audit logs for your Aurora PostgreSQL DB cluster per session or per object, and how to exclude or include by user or by database.

- [Setting up the pgAudit extension](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.basic-setup.html): To set up the pgAudit extension on your Aurora PostgreSQL DB cluster, you first add pgAudit to the shared libraries on the custom DB cluster parameter group for your Aurora PostgreSQL DB cluster.
- [Auditing database objects](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.auditing.html): With pgAudit set up on your Aurora PostgreSQL DB cluster and configured for your requirements, more detailed information is captured in the PostgreSQL log.
- [Excluding users or databases from audit logging](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.exclude-user-db.html): As discussed in , PostgreSQL logs consume storage space.
- [Reference for pgAudit extension parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pgaudit.reference.html): You can specify the level of detail that you want for your audit log by changing one or more of the parameters listed in this section.

### [Using pglogical to synchronize data](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.html)

Use the pglogical extension for logical replication with your Aurora PostgreSQL DB cluster.

- [Setting up the pglogical extension](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.basic-setup.html): To set up the pglogical extension on your Aurora PostgreSQL DB cluster, you add pglogical to the shared libraries on the custom DB cluster parameter group for your Aurora PostgreSQL DB cluster.
- [Setting up logical replication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.setup-replication.html): The following procedure shows you how to start logical replication between two Aurora PostgreSQL DB clusters.
- [Reestablishing logical replication after upgrading](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.recover-replication-after-upgrade.html): Before you can perform a major version upgrade of an Aurora PostgreSQL DB cluster that's set up as a publisher node for logical replication, you must drop all replication slots, even those that aren't active.
- [Managing logical replication slots](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.handle-slots.html): Before you can perform a major version upgrade on an Aurora PostgreSQL DB cluster's writer instance that's serving as a publisher node in a logical replication scenario, you must drop the replication slots on the instance.
- [Parameter reference for pglogical extension parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.reference.html): In the table you can find parameters associated with the pglogical extension.

### [Supported foreign data wrappers in Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.foreign-data-wrappers.html)

Work with the supported foreign data wrappers for Amazon RDS for PostgreSQL.

- [Using the log_fdw extension](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_PostgreSQL.Extensions.log_fdw.html): Access the Amazon Aurora PostgreSQL DB cluster DB log using SQL.
- [Using postgres_fdw to access external data](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-commondbatasks-fdw.html): You can access data in a table on a remote database server with the postgres_fdw extension.
- [Working with a MySQL database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-mysql-fdw.html): To access a MySQL-compatible database from your Aurora PostgreSQL DB cluster, you can install and use the mysql_fdw extension.
- [Working with an Oracle database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-oracle-fdw.html): To access an Oracle database from your Aurora PostgreSQL DB cluster you can install and use the oracle_fdw extension.
- [Working with a SQL Server database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-tds-fdw.html): You can use the PostgreSQL tds_fdw extension to access databases that support the tabular data stream (TDS) protocol, such as Sybase and Microsoft SQL Server databases.

### [Working with Trusted Language Extensions for PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.html)

Trusted Language Extensions for PostgreSQL is an open source development kit for building PostgreSQL extensions.

- [Terminology](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-terminology.html): To help you better understand Trusted Language Extensions, view the following glossary for terms used in this topic.
- [Requirements for using Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-requirements.html): The following are requirements for setting up and using the TLE development kit.
- [Setting up Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-setting-up.html): The following steps assume that your Aurora PostgreSQL DB cluster is associated with a custom DB cluster parameter group.
- [Overview of Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.overview.html): Trusted Language Extensions for PostgreSQL is a PostgreSQL extension that you install in your Aurora PostgreSQL DB cluster in the same way that you set up other PostgreSQL extensions.
- [Creating TLE extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-creating-TLE-extensions.html): You can install any extensions that you create with TLE in any Aurora PostgreSQL DB cluster that has the pg_tle extension installed.
- [Dropping your TLE extensions from a database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-creating-TLE-extensions.dropping-TLEs.html): You can drop your TLE extensions by using the DROP EXTENSION command in the same way that you do for other PostgreSQL extensions.
- [Uninstalling Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-uninstalling-pg_tle-devkit.html): If you no longer want to create your own TLE extensions using TLE, you can drop the pg_tle extension and remove all artifacts.
- [Using PostgreSQL hooks with your TLE extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension.overview.tles-and-hooks.html): A hook is a callback mechanism available in PostgreSQL that allows developers to call custom functions or other routines during regular database operations.
- [Function reference for Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-functions-reference.html): Reference documentation for the management functions available in the Trusted Language Extensions development kit.
- [Hooks reference for Trusted Language Extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL_trusted_language_extension-hooks-reference.html): Reference documentation for the hooks supported by Trusted Language Extensions for PostgreSQL.

### [Aurora PostgreSQL reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Reference.html)

Reference information for Aurora PostgreSQL.

- [Collations supported in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Collations.html): Collations supported in Aurora PostgreSQL .

### [Aurora PostgreSQL functions reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Appendix.AuroraPostgreSQL.Functions.html)

Find a description of functions that are available for Amazon RDS instances running the Aurora PostgreSQL DB engine.

- [aurora_db_instance_identifier](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_db_instance_identifier.html): Reports the name of the DB instance name to which you're connected.
- [aurora_ccm_status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_ccm_status.html): Displays the status of cluster cache manager.
- [aurora_global_db_instance_status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_global_db_instance_status.html): Displays the status of all Aurora instances, including replicas in an Aurora global DB cluster.
- [aurora_global_db_status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_global_db_status.html): Displays Aurora global database durability and recovery point objective (RPO) lag.
- [aurora_list_builtins](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_list_builtins.html): Lists all available Aurora PostgreSQL built-in functions, along with brief descriptions and function details.
- [aurora_replica_status](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_replica_status.html): Displays the status of all Aurora PostgreSQL reader nodes.
- [aurora_stat_activity](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_activity.html): Reports wait event information for the Aurora PostgreSQL DB instance.
- [aurora_stat_backend_waits](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_backend_waits.html): Displays statistics for wait activity for a specific backend process.
- [aurora_stat_bgwriter](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_bgwriter.html): It carries all columns of pg_stat_bgwriter and append new columns in the end.
- [aurora_stat_database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_database.html): It carries all columns of pg_stat_database and append new columns in the end.
- [aurora_stat_dml_activity](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_dml_activity.html): Reports cumulative activity for each type of data manipulation language (DML) operation on a database in an Aurora PostgreSQL cluster.
- [aurora_stat_get_db_commit_latency](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_get_db_commit_latency.html): Gets the cumulative commit latency in microseconds for Aurora PostgreSQL databases.
- [aurora_stat_logical_wal_cache](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_logical_wal_cache.html): Shows logical write-ahead log (WAL) cache usage per slot.
- [aurora_stat_memctx_usage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_memctx_usage.html): Reports the memory context usage for each PostgreSQL process.
- [aurora_stat_optimized_reads_cache](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_optimized_reads_cache.html): This function shows tiered cache stats.
- [aurora_stat_plans](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_plans.html): Returns a row for every tracked execution plan.
- [aurora_stat_reset_wal_cache](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_reset_wal_cache.html): Resets the counter for logical wal cache.
- [aurora_stat_resource_usage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_resource_usage.html): Reports the real-time resource utilization which consists of backend resource metrics and cpu usage for all Aurora PostgreSQL backend processes.
- [aurora_stat_statements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_statements.html): It carries all pg_stat_statements columns and append new columns in the end.
- [aurora_stat_system_waits](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_system_waits.html): Reports wait event information for the Aurora PostgreSQL DB instance.
- [aurora_stat_wait_event](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_wait_event.html): Lists all supported wait events for Aurora PostgreSQL.
- [aurora_stat_wait_type](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_stat_wait_type.html): Lists all supported wait types for Aurora PostgreSQL.
- [aurora_version](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_version.html): Returns the string value of the Amazon Aurora PostgreSQL-Compatible Edition version number.
- [aurora_volume_logical_start_lsn](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_volume_logical_start_lsn.html): Returns the log sequence number (LSN) used for identifying the beginning of a record in the logical write-ahead log (WAL) stream of the Aurora cluster volume.
- [aurora_wait_report](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_wait_report.html): This function shows wait event activity over a period of time.
- [Aurora PostgreSQL parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Reference.ParameterGroups.html): Understanding your Aurora PostgreSQL DB cluster's DB cluster parameter group and DB parameter group.
- [Aurora PostgreSQL wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Reference.Waitevents.html): The following are common wait events for Aurora PostgreSQL.

### [Aurora PostgreSQL updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.html)

Discover Amazon Aurora PostgreSQL engine releases, updates, and instructions for upgrading your Aurora PostgreSQL DB clusters.

- [Aurora PostgreSQL releases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.html): Find out about releases for the Aurora PostgreSQL-Compatible Edition database engine.
- [Extension versions for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Extensions.html): Find out about extensions for Aurora PostgreSQL-Compatible Edition.

### [Upgrading Amazon Aurora PostgreSQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html)

Upgrade your DB cluster engine based on Amazon Aurora PostgreSQL-Compatible Edition to a new version of PostgreSQL.

- [Getting a list of available upgrade targets](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.UpgradeVersion.html): You can get a list of all engine versions available as upgrade targets for your Aurora PostgreSQL DB cluster by querying your AWS Region using the describe-db-engine-versions AWS CLI command, as follows.
- [Performing a major version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.MajorVersion.html): Major version upgrades might contain database changes that are not backward-compatible with previous versions of the database.
- [Performing minor version upgrade](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.MinorUpgrade.html): You can use the following methods to upgrade the minor version of a DB cluster or to patch a DB cluster:
- [Upgrading PostgreSQL extensions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades.html): Upgrading your Aurora PostgreSQL DB cluster to a new major or minor version doesn't upgrade the PostgreSQL extensions at the same time.
- [Using a long-term support (LTS) release](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.LTS.html): Learn about long-term support for your DB cluster engine for Aurora PostgreSQL.


## [Using Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html)

- [Limitless Database architecture](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-architecture.html): Learn about the Aurora PostgreSQL Limitless Database architecture.
- [Getting started with Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-getting-started.html): Learn about the process of using Aurora PostgreSQL Limitless Database.
- [Aurora PostgreSQL Limitless Database requirements and considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.html): Learn about the requirements and considerations for Aurora PostgreSQL Limitless Database.
- [Prerequisites for using Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-prereqs.html): Perform tasks to prepare for using Aurora PostgreSQL Limitless Database.

### [Creating a DB cluster that uses Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-cluster.html)

Create your Aurora PostgreSQL primary DB cluster that uses Aurora PostgreSQL Limitless Database.

- [Creating your DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-create-cluster.html): Learn how to create a DB cluster that uses Aurora PostgreSQL Limitless Database.

### [Working with DB shard groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-shard.html)

Learn how to work with DB shard groups.

- [Changing the capacity of a DB shard group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-capacity.html): Learn how to change the capacity of a DB shard group.
- [Splitting a shard](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-shard-split.html): Learn how to split shards in a DB shard group in Aurora PostgreSQL Limitless Database.
- [Adding a router](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-add-router.html): Learn how to add a router to a DB shard group in Aurora PostgreSQL Limitless Database.
- [Deleting a DB shard group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-shard-delete.html): Learn how to delete a DB shard group in Aurora PostgreSQL Limitless Database.
- [Adding a DB shard group to an existing Limitless Database DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-shard-add.html): Learn how to add a DB shard group to an existing Aurora PostgreSQL Limitless Database DB cluster.

### [Creating Limitless Database tables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-creating.html)

Learn how to create Aurora PostgreSQL Limitless Database tables.

- [Creating limitless tables by using variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-creating-config.html): You can use variables to create sharded and reference tables in Aurora PostgreSQL Limitless Database by setting the table creation mode in a session.
- [Converting standard tables to limitless tables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-converting-standard.html): You can convert standard tables into sharded or reference tables in Aurora PostgreSQL Limitless Database.
- [Sample schemas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-sample-schemas.html): We provide sample schemas for Aurora PostgreSQL Limitless Database.

### [Loading data into Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.html)

Learn about loading data into Aurora PostgreSQL Limitless Database.

- [Using the COPY command with Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.copy.html): Learn how to use the COPY command to load data into and from Aurora PostgreSQL Limitless Database.

### [Using the Limitless Database data loading utility](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.utility.html)

Learn about the data loading utility for Aurora PostgreSQL Limitless Database.

- [Setting up access using a script](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.script.html): Learn how to set up database authentication and resource access for the data loading utility by using a script.
- [Setting up access manually](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.manual.html): Learn how to set up database authentication and resource access manually for the data loading utility.
- [Loading data into Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.data.html): Learn how to load data into Aurora PostgreSQL Limitless Database using the data loading utility.
- [Monitoring data loading](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.monitor.html): Aurora PostgreSQL Limitless Database provides several ways to monitor data loading jobs.
- [Canceling data loading](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-load.cancel.html): Learn how to cancel a data loading job.

### [Querying Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-query.html)

Learn about querying Aurora PostgreSQL Limitless Database.

- [Single-shard queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-query.single-shard.html): Learn about single-shard queries in Aurora PostgreSQL Limitless Database.
- [Distributed queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-query.distributed.html): Distributed queries in Aurora PostgreSQL Limitless Database run on a router and more than one shard.
- [Distributed query tracing](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-query.tracing.html): Distributed query tracing is a tool to trace and correlate queries in PostgreSQL logs across Aurora PostgreSQL Limitless Database.
- [Distributed deadlocks](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-query.deadlocks.html): In a DB shard group in Aurora PostgreSQL Limitless Database, deadlocks can occur between transactions that are distributed among different routers and shards.

### [Managing Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-managing.html)

Learn how to manage Aurora PostgreSQL Limitless Database.

- [Reclaiming storage space by vacuuming](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-vacuum.html): Learn how to use VACUUM and AUTOVACUUM to recover table space.

### [Monitoring Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.html)

Learn how to monitor Aurora PostgreSQL Limitless Database.

- [Monitoring Limitless Database with CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cw.html): Learn how to monitor Aurora PostgreSQL Limitless Database using Amazon CloudWatch.

### [Monitoring Limitless Database with Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.html)

Learn how to monitor Aurora PostgreSQL Limitless Database using CloudWatch Database Insights.

- [Turning on the Advanced mode of Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.advanced.html): Create or modify a Aurora PostgreSQL Limitless Database cluster to use the Advanced mode of Database Insights.
- [Turning on the Standard mode of Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.standard.html): Create or modify a Aurora PostgreSQL Limitless Database cluster to use the Standard mode of Database Insights.
- [Monitoring Limitless Database with CloudWatch Logs](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwl.html): Learn how to monitor Aurora PostgreSQL Limitless Database using Amazon CloudWatch Logs.
- [Monitoring Limitless Database with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.em.html): Learn how to monitor Aurora PostgreSQL Limitless Database using Enhanced Monitoring.

### [Monitoring Limitless Database with Performance Insights](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.pi.html)

Learn how to monitor Aurora PostgreSQL Limitless Database using Performance Insights.

### [Analyzing DB load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.AnalyzeLimitlessTables.html)

Analyze DB load for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard.

- [Analyzing DB load by waits](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.AnalyzeLimitlessTables.Waits.html): Analyze DB load for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard.
- [Analyzing load distribution](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.AnalyzeLimitlessTables.LoadDistribution.html): Analyze DB load for Aurora PostgreSQL Limitless Database using the Performance Insights dashboard.
- [Monitoring Limitless Database with GuardDuty RDS Protection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.gd.html): Learn how to monitor Aurora PostgreSQL Limitless Database using Amazon GuardDuty RDS Protection.

### [Functions and views for Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring-fns-views.html)

Learn about the functions and views for Aurora PostgreSQL Limitless Database.

- [Functions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring-functions.html): Learn how to use the functions for Aurora PostgreSQL Limitless Database.
- [Views](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring-views.html): Learn how to use the views for Aurora PostgreSQL Limitless Database.

### [Wait events for Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-monitoring-waits.html)

Learn about wait events for Aurora PostgreSQL Limitless Database.

- [Wait events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-waits-reference.html): Learn the most important wait events for Aurora PostgreSQL Limitless Database.
- [Building for efficiency with functions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-performance-functions.html): Learn how to optimize functions for single-shard execution in Aurora PostgreSQL Limitless Database.
- [Instance monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-instance-monitoring.html): Monitor instance-level performance to understand connection skew, workload skew, and data skew.
- [Backing up and restoring Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-bak.html): Learn about backing up and restoring DB clusters that use Aurora PostgreSQL Limitless Database.
- [Upgrading Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-upg.html): The following apply to upgrading Aurora PostgreSQL Limitless Database:

### [Limitless Database reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.html)

Learn about the reference topics provided for Aurora PostgreSQL Limitless Database.

- [DDL commands](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DDL-support.html): Learn about the Data Definition Language (DDL) commands that are supported and not supported by Aurora PostgreSQL Limitless Database.
- [DDL limitations and information](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DDL-limitations.html): Learn about the limitations for DDL SQL commands in Aurora PostgreSQL Limitless Database.
- [DML commands](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DML-support.html): Learn about the Data Manipulation Language (DML) commands that are supported and not supported by Aurora PostgreSQL Limitless Database.
- [DML limitations and information](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DML-limitations.html): Learn about the limitations for DML and query processing SQL commands in Aurora PostgreSQL Limitless Database.
- [Variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.variables.html): Learn about the variables that you can use to configure Aurora PostgreSQL Limitless Database.
- [DB cluster parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DBCparams.html): Learn about the DB cluster parameters that you can use to configure Aurora PostgreSQL Limitless Database.


## [Using Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)

### [Getting started with Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html)

Learn how to create and configure resources for the Amazon Aurora Global Database feature.

- [Configuration requirements](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.configuration.requirements.html): Before you start working with your global database, plan the cluster and instance names, AWS Regions, number of instances and instance classes that you intend to use.
- [Creating a global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-creating.html): To create an Aurora global database and its associated resources by using the AWS Management Console, the AWS CLI, or the RDS API, use the following steps.
- [Adding a secondary cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-attaching.html): You can use the following procedure to add an additional secondary cluster to an existing global database.
- [Creating a headless secondary cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-attach.console.headless.html): Although an Aurora global database requires at least one secondary Aurora DB cluster in a different AWS Region than the primary, you can use a headless configuration for the secondary cluster.
- [Creating a global database from a snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.use-snapshot.html): You can restore a snapshot of an Aurora DB cluster or from an Amazon RDS DB instance to use as the starting point for your Aurora global database.

### [Managing an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-managing.html)

Learn how to modify the properties and cluster configurations of Amazon Aurora global databases.

- [Modifying an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-modifying.html): The Databases page in the AWS Management Console lists all your Aurora global databases, showing the primary cluster and secondary clusters for each one.
- [Modifying global database parameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-modifying.parameters.html): You can configure the Aurora DB cluster parameter groups independently for each Aurora cluster within the Aurora global database.
- [Removing a cluster from an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-detaching.html): You can remove Aurora DB clusters from your Aurora global database for several different reasons.
- [Deleting an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-deleting.html): Because an Aurora global database typically holds business-critical data, you can't delete the global database and its associated clusters in a single step.
- [Tagging for Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-tagging.html): Learn how to use AWS tagging with the Amazon Aurora Global Database feature.
- [Connecting to Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-connecting.html): Learn about the endpoints you use to connect to Amazon Aurora Global Database.

### [Using write forwarding in an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding.html)

Learn how to use write forwarding in an Amazon Aurora global database.

- [Using write forwarding in Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding-ams.html): Learn how to work with write forwarding in an Aurora MySQL global database.
- [Using write forwarding in Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-write-forwarding-apg.html): Learn how to work with write forwarding in an Aurora PostgreSQL global database.

### [Switchover or failover for Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html)

Learn how to switch primary and secondary Regions in a healthy environment or to fail over an Amazon Aurora global database for disaster recovery.

- [Cross-Region resiliency for secondary clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-secondary-availability.html): Understand availability characteristics of Global Database secondary clusters.
- [Monitoring an Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-monitoring.html): Learn how to monitor an Amazon Aurora global database.
- [Using Blue/Green Deployments for Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-bluegreen.html): Learn how to perform a Blue/Green Deployment for Amazon Aurora Global Database.
- [Using Aurora global databases with other AWS services](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-interop.html): Learn about using Aurora global databases with other AWS services.
- [Upgrading an Amazon Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.html): Upgrade an Amazon Aurora global database by following similar procedures as when you upgrade Aurora DB clusters, with some important differences.


## [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.html)

- [Planning where to use RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-planning.html): Determine which DB instances, clusters, and applications can benefit from using RDS Proxy.
- [RDS Proxy concepts and terminology](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.howitworks.html): Learn about how RDS Proxy can simplify connection management for your Amazon Aurora DB clusters.

### [Getting started with RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-setup.html)

Learn how to create an RDS Proxy and use it to connect to a database.

- [Set up a proxy network](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-network-prereqs.html): Learn how to set up network requirements for your proxy
- [Setting up database credentials](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-secrets-arns.html): RDS Proxy in Amazon RDS uses AWS Secrets Manager to store and manage database credentials securely.
- [Configuring IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-iam-setup.html): To set up AWS Identity and Access Management (IAM) authentication for RDS Proxy in Amazon RDS, create and configure an IAM policy that grants the necessary permissions.
- [Creating a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-creating.html): You can use Amazon RDS Proxy to improve the scalability, availability, and security of your database applications by pooling connections and managing database failovers more efficiently.
- [Viewing a proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-viewing.html): After you create one or more RDS proxies, you can view and manage them in the AWS Management Console, the AWS CLI, or the RDS API.
- [Connecting through RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-connecting.html): You connect to an Aurora DB cluster or cluster that uses Aurora Serverless v2 through a proxy in generally the same way as you connect directly to the database.

### [Managing an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html)

Learn how to modify RDS Proxy and tune it to suit your needs.

- [Modifying an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-modifying-proxy.html): You can change specific settings associated with a proxy after you create the proxy.
- [Adding a database user](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-new-db-user.html): In some cases, you might add a new database user to an Aurora cluster that's associated with a proxy.
- [Moving to end-to-end IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-iam-migration.html): If you currently use standard IAM authentication for RDS Proxy, where clients authenticate to the proxy using IAM but the proxy connects to the database using secrets, you can migrate to end-to-end IAM authentication where both client-to-proxy and proxy-to-database connections use IAM authentication.
- [RDS Proxy connection considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-connections.html)
- [Avoid pinning RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-pinning.html): Multiplexing is more efficient when database requests don't rely on state information from previous requests.
- [Deleting an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-deleting.html): You can delete a proxy when you no longer need it.

### [Working with RDS Proxy endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.html)

RDS Proxy endpoints provide flexible and efficient ways to manage database connections, which improves scalability, availability, and security.

- [Creating a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.CreatingEndpoint.html): To create a proxy endpoint, follow these instructions:
- [Viewing proxy endpoints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.DescribingEndpoint.html): To view existing proxy endpoints, follow these instructions:
- [Modifying a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.ModifyingEndpoint.html): To modify your proxy endpoints, follow these instructions:
- [Deleting a proxy endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-endpoints.DeletingEndpoint.html): To delete an endpoint for your proxy, follow these instructions:
- [Monitoring RDS Proxy with CloudWatch](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.monitoring.html): You can monitor RDS Proxy by using Amazon CloudWatch.
- [Working with RDS Proxy events](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.events.html): Find a list of Amazon RDS Proxy events that you can subscribe to and an example of an RDS Proxy event.
- [RDS Proxy examples](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.examples.html): See command-line examples for working with RDS Proxy.
- [Troubleshooting RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy.troubleshooting.html): Learn how to troubleshoot issues with RDS Proxy.
- [Using RDS Proxy with AWS CloudFormation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-cfn.html): See a sample AWS CloudFormation template for creating an RDS Proxy.
- [Using RDS Proxy with Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-gdb.html): Learn about using RDS Proxy with Aurora global databases.


## [Zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html)

- [Getting started with zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.setting-up.html): Learn how to configure your Aurora DB cluster for a zero-ETL integration.
- [Creating zero-ETL integrations with Amazon Redshift](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.creating.html): Learn how to create zero-ETL integrations with Amazon Redshift.
- [Creating zero-ETL integrations with an Amazon SageMaker lakehouse](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.creating-smlh.html): Learn how to create zero-ETL integrations with an Amazon SageMaker lakehouse.
- [Data filtering for zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.filtering.html): Learn how to filter the data that a zero-ETL integration sends to the analytics destination.
- [Adding and querying data](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.querying.html): Learn how to add data to a source for a zero-ETL integration with Amazon Redshift.
- [Viewing and monitoring zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.describingmonitoring.html): Learn how to view and monitor the details of a zero-ETL integration.
- [Modifying zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.modifying.html): Learn how to modify a zero-ETL integration.
- [Deleting zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.deleting.html): Learn how to delete zero-ETL integrations.
- [Troubleshooting zero-ETL integrations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.troubleshooting.html): You can check the state of a zero-ETL integration by querying the SVV_INTEGRATION system table in the analytics destination.


## [Using Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html)

- [How Aurora Serverless v2 works](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.how-it-works.html): Get a description of how Aurora Serverless v2 works.
- [Requirements and limitations for Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.html): Learn about the requirements and limitations for Aurora Serverless v2.
- [Creating an Aurora Serverless v2 DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.create.html): Learn how to create a cluster that uses Aurora Serverless v2.
- [Managing Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-administration.html): Learn about managing clusters that contain Aurora Serverless v2 DB instances.
- [Performance and scaling for Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.setting-capacity.html): Learn about performance and scaling for Aurora Serverless v2.
- [Scaling to 0 ACUs with auto-pause and resume](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-auto-pause.html)
- [Migrating to Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.upgrade.html): Migrate to Amazon Aurora Serverless V2.


## [Using Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html)

- [How Aurora Serverless v1 works](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v1.how-it-works.html): Learn how Amazon Aurora Serverless v1 works.
- [Creating an Aurora Serverless v1 DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.create.html)
- [Restoring an Aurora Serverless v1 DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.restorefromsnapshot.html)
- [Modifying an Aurora Serverless v1 DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.modifying.html): Learn how to modify Aurora Serverless v1 DB clusters.
- [Scaling Aurora Serverless v1 DB cluster capacity manually](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.setting-capacity.html)
- [Viewing Aurora Serverless v1 DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.viewing.html)
- [Deleting an Aurora Serverless v1 DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.delete.html)
- [Aurora Serverless v1 and Aurora database engine versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.relnotes.html): Learn about Aurora Serverless v1 database engine versions.


## [Using the Amazon RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)

- [Region and version availability for the Amazon RDS Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.regions.html): Information about the Regions and engine versions available for Data API.
- [IPv6 support](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.ipv6.html): Learn how to use IPv6 endpoints with Amazon RDS Data API to execute SQL queries over IPv6 networks.
- [Limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.limitations.html): Information about the limitations for the Amazon RDS Data API.
- [Data API with Aurora Serverless v2 compared with Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.differences.html): A list of comparisons between Data API operations for Aurora Serverless v2 and provisioned clusters, and Aurora Serverless v1 clusters.
- [Authentication and authorization](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.access.html): Learn more about authorizing access to the Amazon RDS Data API.
- [Enabling Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.enabling.html): Use this section to enable the Amazon RDS Data API.
- [Creating a Amazon VPC endpoint (PrivateLink)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.vpc-endpoint.html): Create a Amazon VPC endpoint for the Amazon RDS Data API.

### [Calling Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.calling.html)

Learn how to call the Amazon RDS Data API.

- [Operations reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api-operations.html): The Amazon RDS Data API provides the following operations to perform SQL statements.
- [Calling from AWS CLI](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.calling.cli.html): You can call RDS Data API (Data API) using the AWS CLI.
- [Calling from Python apps](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.calling.python.html): Learn more about calling the Amazon RDS Data API from a Python application.
- [Calling from Java apps](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.calling.java.html): You can call the Amazon RDS Data API (Data API) from a Java application.
- [Controlling timeout behavior](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api-timeouts.html): All calls to the Data API are synchronous.
- [Java client library](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.java-client-library.html): You can download and use a Java client library for RDS Data API (Data API).
- [Processing query results in JSON](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api-json.html): When you call the ExecuteStatement operation, you can choose to have the query results returned as a string in JSON format.
- [Troubleshooting Data API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.troubleshooting.html): Learn how to troubleshoot Amazon RDS Data API issues.
- [Logging Data API calls](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/logging-using-cloudtrail-data-api.html): Learn about logging RDS Data API with AWS CloudTrail.
- [Monitoring Data API queries](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-using-performance-insights-data-api.html): Learn about monitoring RDS Data API with Performance Insights.


## [Using the query editor](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/query-editor.html)

- [DBQMS API reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/dbqms-api.html): DBQMS API reference.


## [Using Aurora machine learning](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-ml.html)

- [Using Aurora machine learning with Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-ml.html): Use your Amazon Bedrock, Amazon SageMaker AI, and Amazon Comprehend machine learning models from an Aurora MySQL DB cluster by through Aurora MySQL stored functions.
- [Using Aurora machine learning with Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/postgresql-ml.html): Use your Amazon Bedrock, Amazon SageMaker AI, and Amazon Comprehend machine learning models from an Aurora PostgreSQL DB cluster by embedding function calls in your SQL queries.


## [Code examples](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/service_code_examples_basics.html)

The following code examples show how to use the basics of Aurora with AWS SDKs.

- [Hello Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_Hello_section.html): Hello Aurora
- [Learn the basics](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_Scenario_GetStartedClusters_section.html): Learn the basics of Aurora with an AWS SDK

### [Actions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/service_code_examples_actions.html)

The following code examples show how to use Aurora with AWS SDKs.

- [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_CreateDBCluster_section.html): Use CreateDBCluster with an AWS SDK
- [CreateDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_CreateDBClusterParameterGroup_section.html): Use CreateDBClusterParameterGroup with an AWS SDK
- [CreateDBClusterSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_CreateDBClusterSnapshot_section.html): Use CreateDBClusterSnapshot with an AWS SDK
- [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_CreateDBInstance_section.html): Use CreateDBInstance with an AWS SDK
- [DeleteDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DeleteDBCluster_section.html): Use DeleteDBCluster with an AWS SDK
- [DeleteDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DeleteDBClusterParameterGroup_section.html): Use DeleteDBClusterParameterGroup with an AWS SDK
- [DeleteDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DeleteDBInstance_section.html): Use DeleteDBInstance with an AWS SDK
- [DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeDBClusterParameterGroups_section.html): Use DescribeDBClusterParameterGroups with an AWS SDK
- [DescribeDBClusterParameters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeDBClusterParameters_section.html): Use DescribeDBClusterParameters with an AWS SDK
- [DescribeDBClusterSnapshots](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeDBClusterSnapshots_section.html): Use DescribeDBClusterSnapshots with an AWS SDK
- [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeDBClusters_section.html): Use DescribeDBClusters with an AWS SDK
- [DescribeDBEngineVersions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeDBEngineVersions_section.html): Use DescribeDBEngineVersions with an AWS SDK
- [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeDBInstances_section.html): Use DescribeDBInstances with an AWS SDK
- [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_DescribeOrderableDBInstanceOptions_section.html): Use DescribeOrderableDBInstanceOptions with an AWS SDK or CLI
- [ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_aurora_ModifyDBClusterParameterGroup_section.html): Use ModifyDBClusterParameterGroup with an AWS SDK

### [Scenarios](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/service_code_examples_scenarios.html)

The following code examples show how to use Aurora with AWS SDKs.

- [Create a lending library REST API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_cross_AuroraRestLendingLibrary_section.html): Create a lending library REST API
- [Create an Aurora Serverless work item tracker](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/example_cross_RDSDataTracker_section.html): Create an Aurora Serverless work item tracker


## [Security](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.html)

- [Database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/database-authentication.html): Use different types of database authentication supported by Amazon Aurora encryption.
- [Password management with Aurora and Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html): Learn about managing Amazon Aurora passwords with AWS Secrets Manager.

### [Data protection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/DataDurability.html)

Learn how the AWS shared responsibility model applies to data protection in Amazon RDS.

### [Data encryption](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Encryption.html)

Use data encryption to provide added security for your data stored in your Amazon Aurora DB clusters.

- [Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html): Secure your RDS data by encrypting your DB clusters.
- [AWS KMS key management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.Keys.html): Amazon Aurora automatically integrates with AWS Key Management Service (AWS KMS) for key management.
- [Using SSL/TLS to encrypt a connection](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL.html): Create encrypted connections to your Amazon Aurora cluster using SSL/TLS.
- [Rotating your SSL/TLS certificate](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.SSL-certificate-rotation.html): Rotate your SSL/TLS certificate as a security best practice.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/inter-network-traffic-privacy.html): Describes how Amazon Aurora secures connections from the service to other locations.

### [Identity and access management](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.html)

How to authenticate requests and manage access to your Amazon Aurora resources.

- [How Amazon Aurora works with IAM](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/security_iam_service-with-iam.html): Before you use IAM to manage access to Amazon Aurora, you should understand what IAM features are available to use with Aurora.

### [Identity-based policy examples](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/security_iam_id-based-policy-examples.html)

Work with these identity-based policy examples for Amazon Aurora.

- [Permission policies to create, modify and, delete resources in Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/security_iam_id-based-policy-examples-create-and-modify-examples.html): The following sections present examples of permission policies that grant and restrict access to resources:
- [Example policies: Using condition keys](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.Conditions.Examples.html): Following are examples of how you can use condition keys in Amazon Aurora IAM permissions policies.
- [Using custom tags](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.SpecifyingCustomTags.html): Amazon Aurora supports specifying conditions in an IAM policy using custom tags.
- [Tagging on creation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/security_iam_id-based-policy-examples-grant-permissions-tags-on-create.html): Some RDS API operations allow you to specify tags when you create the resource.
- [AWS managed policies](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon RDS and recent changes to those policies.
- [Policy updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-manpol-updates.html): View details about updates to AWS managed policies for Amazon RDS since RDS began tracking these changes.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/cross-service-confused-deputy-prevention.html): For AWS cross-service work, learn how to prevent the confused deputy problem, a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.

### [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.html)

Authenticate to your DB instance or cluster using AWS Identity and Access Management (IAM) database authentication.

- [Enabling and disabling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Enabling.html): By default, IAM database authentication is disabled on DB clusters.
- [Creating and using an IAM policy for IAM database access](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.IAMPolicy.html): To allow a user or role to connect to your DB cluster, you must create an IAM policy.
- [Creating a database account using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.DBAccounts.html): With IAM database authentication, you don't need to assign database passwords to the user accounts you create.

### [Connecting to your DB cluster using IAM authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.html)

With IAM database authentication, you use an authentication token when you connect to your DB cluster.

- [Connecting to your DB cluster using IAM authentication with the AWS drivers](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/IAMDBAuth.Connecting.Drivers.html): The AWS suite of drivers has been designed to provide support for faster switchover and failover times, and authentication with AWS Secrets Manager, AWS Identity and Access Management (IAM), and Federated Identity.
- [Connecting using IAM: AWS CLI and mysql client](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.AWSCLI.html): You can connect from the command line to an Aurora DB cluster with the AWS CLI and mysql command line tool as described following.
- [Connecting using IAM authentication from the command line: AWS CLI and psql client](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.AWSCLI.PostgreSQL.html): You can connect from the command line to an Aurora PostgreSQL DB cluster with the AWS CLI and psql command line tool as described following.
- [Connecting using IAM authentication and the AWS SDK for .NET](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.NET.html): You can connect to an Aurora MySQL or Aurora PostgreSQL DB cluster with the AWS SDK for .NET as described following.
- [Connecting using IAM authentication and the AWS SDK for Go](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.Go.html): You can connect to an Aurora MySQL or Aurora PostgreSQL DB cluster with the AWS SDK for Go as described following.
- [Connecting using IAM authentication and the AWS SDK for Java](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.Java.html): You can connect to an Aurora MySQL or Aurora PostgreSQL DB cluster with the AWS SDK for Java as described following.
- [Connecting using IAM authentication and the AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Connecting.Python.html): You can connect to an Aurora MySQL or Aurora PostgreSQL DB cluster with the AWS SDK for Python (Boto3) as described following.
- [Troubleshooting IAM DB authentication](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAMDBAuth.Troubleshooting.html): Following, you can find troubleshooting ideas for some common IAM DB authentication issues and information on CloudWatch logs and metrics for IAM DB authentication.
- [Troubleshooting](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Aurora and IAM.
- [Logging and monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.LoggingAndMonitoring.html): Tools in Amazon Aurora for monitoring resources and responding to incidents.
- [Compliance validation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/RDS-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy and also specific Amazon Aurora features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/infrastructure-security.html): Learn how Amazon RDS isolates service traffic.
- [VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your virtual private cloud (VPC) and Amazon RDS API.
- [Security best practices](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_BestPractices.Security.html): Use AWS Identity and Access Management (IAM) accounts to control access to Amazon RDS API operations, especially operations that create, modify, or delete Amazon Aurora resources.
- [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.RDSSecurityGroups.html): Control the access the traffic in and out of a DB cluster with security groups.
- [Master user account privileges](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.MasterAccounts.html): When you create a new DB cluster, the default master user that you use gets certain privileges for that DB cluster.
- [Service-linked roles](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/UsingWithRDS.IAM.ServiceLinkedRoles.html): How to use service-linked roles to give Amazon Aurora access to resources in your AWS account.

### [Using Amazon Aurora with Amazon VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.html)

Learn about common tasks for working with a DB instance in a virtual private cloud (VPC) based on the Amazon VPC service.

- [Working with a DB cluster in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html): Learn about working with an Amazon Aurora DB instance in a VPC.
- [Scenarios for accessing a DB cluster in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.Scenarios.html): Learn about the various scenarios for accessing a DB cluster in a VPC.
- [Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html): Create a virtual private cloud (VPC) with public and private subnets to host a public web server and a private DB cluster.
- [Tutorial: Create a VPC for use with a DB cluster (dual-stack mode)](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.CreateVPCDualStack.html): Create a virtual private cloud (VPC) based on the Amazon VPC service.


## [Amazon RDS API reference](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ProgrammingGuide.html)

- [Using the Query API](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Using_the_Query_API.html): Use the Query API to handle authentication and selection of an action with your Amazon RDS instances.
- [Troubleshooting applications](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/APITroubleshooting.html): Provides specific and descriptive errors to help you troubleshoot problems while interacting with the Amazon RDS API.
