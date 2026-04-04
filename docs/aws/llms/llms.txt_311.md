# Source: https://docs.aws.amazon.com/dms/latest/userguide/llms.txt

# AWS Database Migration Service User Guide

> Migrate databases to AWS easily and securely using AWS Database Migration Service (AWS DMS) with this User Guide.

- [What is AWS Database Migration Service?](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
- [AWS zero-ETL integration for self-managed database sources](https://docs.aws.amazon.com/dms/latest/userguide/zero-etl.html)
- [Best practices](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.html)
- [Working with EventBridge events](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_EventBridge.html)
- [Working with Amazon SNS events](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html)
- [Tagging resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html)
- [Limits](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Limits.html)
- [Release notes](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReleaseNotes.html)
- [Document history](https://docs.aws.amazon.com/dms/latest/userguide/WhatsNew.html)
- [AWS Glossary](https://docs.aws.amazon.com/dms/latest/userguide/glossary.html)

## [Terminology and concepts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.html)

- [High-level view of AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.HighLevelView.html): Get a high-level view of AWS DMS.
- [Components](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Components.html): This section describes the internal components of AWS DMS and how they function together to accomplish your data migration.
- [Sources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Sources.html): Use the listed data stores as sources for different AWS DMS features.
- [Targets](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.Targets.html): Use the listed data stores as target endpoints for data migration using AWS DMS.
- [Amazon Resource Names](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.ARN.html): Create Amazon Resource Names (ARNs) for use with AWS DMS.
- [With other AWS services](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.AWS.html): Use AWS DMS with other AWS services.


## [Getting started](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)

- [Set up](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.SettingUp.html): Set up for AWS Database Migration Service.
- [Prerequisites](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Prerequisites.html): Perform prerequisite tasks for AWS Database Migration Service such as setting up your source and target databases.
- [Migrate schema](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.SCT.html): In this section, you use the AWS Schema Conversion Tool to migrate your source schema to your target database.
- [Replication](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.Replication.html): In this topic, you set up replication between the source and target databases.


## [AWS DMS Fleet Advisor end of support](https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html)

- [Discovering databases for migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_FleetAdvisor.html)
- [Understand DMS Fleet Advisor](https://docs.aws.amazon.com/dms/latest/userguide/fa-getting-started.html): Learn how you can get started with DMS Fleet Advisor.
- [Creating required resources](https://docs.aws.amazon.com/dms/latest/userguide/fa-resources.html): Create required AWS resources for DMS Fleet Advisor.
- [Creating database users](https://docs.aws.amazon.com/dms/latest/userguide/fa-database-users.html): Create database users with minimum privileges for AWS DMS Fleet Advisor.

### [Data collectors](https://docs.aws.amazon.com/dms/latest/userguide/fa-data-collectors.html)

Learn how to use AWS DMS Fleet Advisor to discover databases for migration using AWS DMS data collectors.

- [Creating a data collector](https://docs.aws.amazon.com/dms/latest/userguide/fa-data-collectors-create.html): How to create a data collector for DMS Fleet Advisor.
- [Installing a data collector](https://docs.aws.amazon.com/dms/latest/userguide/fa-data-collectors-install.html): How to install a data collector for DMS Fleet Advisor.
- [Discovering OS and database servers](https://docs.aws.amazon.com/dms/latest/userguide/fa-discovery.html): Use your on-premises DMS data collector to find and list all available servers in your network that you can monitor.
- [Managing monitored objects](https://docs.aws.amazon.com/dms/latest/userguide/fa-managing-objects.html): Manually manage monitored objects such as operating system (OS) servers and database servers.
- [Using SSL](https://docs.aws.amazon.com/dms/latest/userguide/fa-using-ssl.html): How to use SSL with AWS DMS Fleet Advisor.
- [Collecting data](https://docs.aws.amazon.com/dms/latest/userguide/fa-collecting.html): Start collecting data for AWS DMS Fleet Advisor.

### [Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/fa-collectors-troubleshooting.html)

Find actions that you can take when you encounter issues while collecting data with the DMS data collector.

- [Network and server connection related issues](https://docs.aws.amazon.com/dms/latest/userguide/fa-collectors-troubleshooting-net.html): Find actions that you can take when you encounter issues related to network and server connections with the DMS data collector.
- [WMI related issues](https://docs.aws.amazon.com/dms/latest/userguide/fa-collectors-troubleshooting-wmi.html): Find actions that you can take when you encounter issues related to Windows Management Instrumentation with the DMS data collector.
- [WPC related issues](https://docs.aws.amazon.com/dms/latest/userguide/fa-collectors-troubleshooting-wpc.html): Find actions that you can take when you encounter issues related to Windows webpage composer with the DMS data collector.
- [SSL related issues](https://docs.aws.amazon.com/dms/latest/userguide/fa-collectors-troubleshooting-ssl.html): Find actions that you can take when you encounter issues related to SSL with the DMS data collector.

### [Inventory](https://docs.aws.amazon.com/dms/latest/userguide/fa-inventory.html)

Work with inventories of discovered databases and schemas to check the feasibility of potential database migrations.

- [Using the database inventory](https://docs.aws.amazon.com/dms/latest/userguide/fa-inventory-database.html): Learn how to view the inventory of your databases in AWS DMS Fleet Advisor.
- [Using the schema inventory](https://docs.aws.amazon.com/dms/latest/userguide/fa-inventory-schema.html): Learn how to view the inventory of your database schemas in AWS DMS Fleet Advisor.

### [Target recommendations](https://docs.aws.amazon.com/dms/latest/userguide/fa-recommendations.html)

Generate, view, and save a local copy of the target recommendations for your source databases.

- [Generating target recommendations](https://docs.aws.amazon.com/dms/latest/userguide/fa-recommendations-generate.html): Learn how to generate target recommendations with AWS DMS Fleet Advisor.
- [Recommendation details](https://docs.aws.amazon.com/dms/latest/userguide/fa-recommendations-view.html): Learn how to explore details of your target recommendations with AWS DMS Fleet Advisor.
- [Exporting target recommendations](https://docs.aws.amazon.com/dms/latest/userguide/fa-recommendations-export.html): Learn how to save a copy of your target recommendations with AWS DMS Fleet Advisor.
- [Migration limitations](https://docs.aws.amazon.com/dms/latest/userguide/fa-data-collectors-database-features.html): Learn more about database features that DMS Fleet Advisor collects.
- [Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/fa-recommendations-troubleshooting.html): Learn more about actions to take when you encounter issues with the AWS DMS Fleet Advisor Target Recommendations feature.
- [Limitations](https://docs.aws.amazon.com/dms/latest/userguide/fa-welcome-limitations.html): Learn about the limitations of the DMS Fleet Advisor.


## [Converting database schemas](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html)

### [Getting started](https://docs.aws.amazon.com/dms/latest/userguide/getting-started.html)

Use this tutorial to get started with DMS Schema Conversion in AWS Database Migration Service.

- [Prerequisites](https://docs.aws.amazon.com/dms/latest/userguide/set-up.html): Set up DMS Schema Conversion in AWS Database Migration Service to convert your database schemas to a format compatible with Amazon RDS.
- [Create an instance profile](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-instance.html): Learn how to create an instance profile for DMS Schema Conversion in AWS Database Migration Service.
- [Configure data providers](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-data-providers.html): Learn how to configure your data providers in DMS Schema Conversion in AWS Database Migration Service.
- [Create a migration project](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-project.html): Learn how to create a migration project in DMS Schema Conversion in AWS Database Migration Service.
- [Create an assessment report](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-assessment.html): Learn how to create an assessment report in DMS Schema Conversion in AWS Database Migration Service.
- [Convert your source code](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-convert.html): Learn how to convert your source database storage and code objects in DMS Schema Conversion in AWS Database Migration Service.
- [Apply the converted code](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-apply.html): Learn how to apply your converted code to the target data provider for DMS Schema Conversion in AWS Database Migration Service.
- [Clean up and troubleshoot](https://docs.aws.amazon.com/dms/latest/userguide/getting-started-clean-up.html): Learn how to stop your migration project and find log information for DMS Schema Conversion in AWS Database Migration Service.
- [Setting up a network](https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles-network.html): Learn how to set up a network for DMS Schema Conversion in AWS Database Migration Service.

### [Creating source data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-source.html)

Learn how to create source data providers for DMS Schema Conversion in AWS Database Migration Service.

- [Using SQL Server as a source](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-sql-server.html): Learn how use a SQL Server database as a source for DMS Schema Conversion in AWS Database Migration Service.
- [Using Oracle as a source](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-oracle.html): Learn how to use an Oracle database as a source for DMS Schema Conversion in AWS Database Migration Service.
- [Using Oracle Data Warehouse as a source](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-oracle-dw.html): Learn how to use an Oracle Data Warehouse database as a source for DMS Schema Conversion in AWS Database Migration Service.
- [Using PostgreSQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/sc-data-providers-postgresql.html): Learn how use a PostgreSQL database as a source for DMS Schema Conversion in AWS Database Migration Service.
- [Using MySQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/sc-data-providers-mysql.html): Learn how use a MySQL database as a source for DMS Schema Conversion in AWS Database Migration Service.
- [Using Db2 for z/OS as a source](https://docs.aws.amazon.com/dms/latest/userguide/sc-data-providers-db2zos.html): Learn how use a DB2 for z/OS database as a source for DMS Schema Conversion in AWS Database Migration Service.
- [Using a SAP ASE (Sybase ASE) database](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-sybase-ASE.html): Learn how to use a SAP ASE (Sybase ASE) database as a source in in AWS DMS Schema Conversion

### [Creating and setting target data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-target.html)

Learn how to create and set target data providers for DMS Schema Conversion in AWS Database Migration Service.

- [Using MySQL as a target](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-mysql.html): Learn how use a MySQL database as a target in for DMS Schema Conversion in AWS Database Migration Service.
- [Using PostgreSQL as a target](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-postgresql.html): Learn how to use a PostgreSQL database as a target for DMS Schema Conversion in AWS Database Migration Service.
- [Using Amazon Redshift as a target](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-redshift.html): Learn how to use an Amazon Redshift cluster as a target for DMS Schema Conversion in AWS Database Migration Service.
- [Using Amazon RDS for Db2 database as a target](https://docs.aws.amazon.com/dms/latest/userguide/sc-data-providers-rds.html): You can use Amazon RDS for Db2 databases as a migration target in DMS Schema Conversion.
- [Virtual data provider](https://docs.aws.amazon.com/dms/latest/userguide/virtual-data-provider.html): Learn how to use Virtual Mode for data providers in AWS DMS Schema Conversion to perform schema conversion without connecting to a target database, reducing infrastructure costs and providing flexibility for migration planning.
- [Managing migration projects](https://docs.aws.amazon.com/dms/latest/userguide/sc-migration-projects.html): Learn how to create and manage a migration project for DMS Schema Conversion in AWS Database Migration Service.

### [Database migration assessment reports](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports.html)

Creating database migration assessment reports by using DMS Schema Conversion in AWS Database Migration Service.

- [Creating an assessment report](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports.create.html): Create a database migration assessment report for DMS Schema Conversion in AWS Database Migration Service.
- [Viewing your assessment report](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports-view.html): View your database migration assessment report for DMS Schema Conversion in AWS Database Migration Service.
- [Saving assessment reports](https://docs.aws.amazon.com/dms/latest/userguide/assessment-reports-save.html): Save your database migration assessment report for DMS Schema Conversion in AWS Database Migration Service.

### [Schema conversion](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion.html)

Convert database schemas by using DMS Schema Conversion in AWS Database Migration Service.

- [Setting up transformation rules](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-transformation-rules.html): Set up transformation rules to change the names of your database objects during DMS Schema Conversion in AWS Database Migration Service.
- [Converting your database schema: step-by-step guide](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-convert.html): Convert your source schema to an equivalent schema for your target DB instance for DMS Schema Conversion in AWS Database Migration Service.
- [Converting database objects with generative AI](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-convert.databaseobjects.html): The DMS Schema Conversion with generative AI feature streamlines the database migration process by offering recommendations to help you convert previously unconverted code objects that typically require complex manual conversion.

### [Specifying schema conversion settings](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html)

Learn how you can edit schema conversion settings for your DMS Schema Conversion project in AWS Database Migration Service.

- [Oracle to MySQL](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-oracle-mysql.html): Set up Oracle to MySQL conversion settings for DMS Schema Conversion in AWS Database Migration Service.
- [Oracle to PostgreSQL](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-oracle-postgresql.html): Set up Oracle to PostgreSQL conversion settings for DMS Schema Conversion in AWS Database Migration Service.
- [SQL Server to MySQL](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-sql-server-mysql.html): Set up Microsoft SQL Server to MySQL conversion settings for DMS Schema Conversion in AWS Database Migration Service.
- [SQL Server to PostgreSQL](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-sql-server-postgresql.html): Set up Microsoft SQL Server to PostgreSQL conversion settings for DMS Schema Conversion in AWS Database Migration Service.
- [PostgreSQL to MySQL](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-postgresql-mysql.html): Set up PostgreSQL to MySQL conversion settings for DMS Schema Conversion in AWS Database Migration Service.
- [Db2 for z/OS to RDS for Db2](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-db2-zos-db2.html): Set up for z/OS to DB2 LUW conversion settings for DMS Schema Conversion in AWS Database Migration Service.
- [SAP ASE (Sybase ASE) to PostgreSQL](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion--sybase-ASE.html): Understanding SAP ASE (Sybase ASE) to PostgreSQL conversion settings for AWS DMS
- [Refreshing your database schemas](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-refresh.html): Learn how you can refresh your source and target database schemas for your DMS Schema Conversion project in AWS Database Migration Service.
- [Saving and applying your schema](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-save-apply.html): Save your converted code as SQL scripts and apply it to your target database for DMS Schema Conversion in AWS Database Migration Service.
- [Converting embedded SQL in Java applications](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-embedded-sql.html): When you use AWS DMS and DMS Schema Conversion to migrate a database, you might need to convert the embedded SQL in your application to be compatible with your target database.
- [Using extension packs](https://docs.aws.amazon.com/dms/latest/userguide/extension-pack.html): Use extension packs with DMS Schema Conversion in AWS Database Migration Service to emulate source database functions in your target database.
- [IAM to API Mapping](https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-iam.mapping.html): When setting up access control and writing IAM permissions policies for DMS Schema Conversion and Common Studio Framework, it is important to understand how API actions map to IAM permissions.


## [Homogeneous data migrations](https://docs.aws.amazon.com/dms/latest/userguide/data-migrations.html)

- [Overview](https://docs.aws.amazon.com/dms/latest/userguide/dm-getting-started.html): Learn how you can get started with homogeneous data migrations in AWS DMS.

### [Setting up](https://docs.aws.amazon.com/dms/latest/userguide/dm-prerequisites.html)

Learn how to configure required resources for homogeneous data migrations in AWS DMS and set up a network for your data migration.

- [Creating IAM resources](https://docs.aws.amazon.com/dms/latest/userguide/dm-iam-resources.html): Create required IAM resources for homogeneous data migrations.
- [Setting up a network](https://docs.aws.amazon.com/dms/latest/userguide/dm-network.html): Learn how to set up a network for homogeneous data migrations.
- [VPC peering network configurations](https://docs.aws.amazon.com/dms/latest/userguide/vpc-peering.html): With AWS DMS, you can create a serverless environment for homogeneous data migrations in a virtual private cloud (VPC) based on the Amazon VPC service.

### [Creating source data providers](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source.html)

Learn how to create source data providers for homogeneous data migrations in AWS Database Migration Service.

- [Using MySQL or MariaDB as a source](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-mysql.html): Learn how use a MySQL-compatible database as a source in for homogeneous data migrations in AWS Database Migration Service.
- [Using PostgreSQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-postgresql.html): Learn how to configure your source PostgreSQL database to use it for homogeneous data migrations in AWS DMS.
- [Using MongoDB or Amazon DocumentDB as a source](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-source-mongodb.html): Learn how to configure your source MongoDB database to use it for homogeneous data migrations in AWS DMS.

### [Create and set a target database](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-target.html)

Learn how to create and set a target database to work with AWS DMS schema conversion

- [Using MySQL or MariaDB as a target](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-target-mysql.html): Learn how use a MySQL database as a target for homogeneous data migrations in AWS Database Migration Service.
- [Using PostgreSQL as a target](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-target-postgresql.html): Learn how to configure your target PostgreSQL database to use it for homogeneous data migrations in AWS DMS.
- [Using Amazon DocumentDB as a target](https://docs.aws.amazon.com/dms/latest/userguide/dm-data-providers-target-docdb.html): Learn how to configure your target Amazon DocumentDB database to use it for homogeneous data migrations in AWS DMS.

### [Migrating data](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data.html)

Learn how you can run homogeneous data migrations in AWS DMS.

- [Creating a data migration](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-create.html): Learn how you can create a data migration in AWS DMS.
- [Selection rules](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-selectionrules.html): Learn how you can selectively migrate data in a data migration in AWS DMS.
- [Managing data migrations](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-manage.html): Learn how you can start, modify, or delete a data migration in AWS DMS.
- [Monitoring data migrations](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-monitoring.html): Learn how you can configure and use different monitoring options for data migration in AWS DMS.
- [Migration statuses](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-statuses.html): Understand the statuses of homogeneous data migrations.
- [Migrating data from MySQL](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-mysql.html): Learn how to migrate data from MySQL databases with homogeneous data migrations in AWS DMS.
- [Migrating data from PostgreSQL](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-postgresql.html): Learn how to migrate data from PostgreSQL databases with homogeneous data migrations in AWS DMS.
- [Migrating data from MongoDB](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-mongodb.html): Learn how to migrate data from MongoDB databases with homogeneous data migrations in AWS DMS.
- [Target table preparation mode](https://docs.aws.amazon.com/dms/latest/userguide/dm-migrating-data-table-prep.html): Learn about the Target table preparation mode in homogeneous data migrations in AWS DMS.
- [Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/dm-troubleshooting.html): Learn about actions to take when you encounter issues with homogeneous data migrations in AWS DMS.


## [Working with migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects.html)

- [Creating a subnet group](https://docs.aws.amazon.com/dms/latest/userguide/subnet-group.html): Learn how to create subnet groups for AWS DMS migration projects.
- [Creating instance profiles](https://docs.aws.amazon.com/dms/latest/userguide/instance-profiles.html): Create an instance profile for your migration project to use with DMS Schema Conversion or homogeneous data migrations in AWS Database Migration Service.
- [Creating data providers](https://docs.aws.amazon.com/dms/latest/userguide/data-providers-create.html): Learn how to create data providers for AWS Database Migration Service.
- [Creating migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects-create.html): Learn how to create migration projects in AWS Database Migration Service.
- [Managing migration projects](https://docs.aws.amazon.com/dms/latest/userguide/migration-projects-manage.html): Learn how to modify and delete migration projects in AWS Database Migration Service.


## [Working with AWS DMS Serverless](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.html)

- [DMS Serverless components](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.Components.html): Understand the components of AWS DMS Serverless.
- [Serverless limitations](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.Limitations.html): Learn about the limitations of Serverless
- [Serverless premigrations](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Serverless.Premigrations.html): AWS DMS Serverless includes pre-migration assessment capabilities that help identify potential issues before starting your database migration.


## [Working with replication instances](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)

- [Choosing replication instance types](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html): Choose the right AWS DMS replication instance type for your migration.
- [Sizing a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html): Learn the sizing recommendations for replication instances for AWS DMS.
- [Replication engine versions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.EngineVersions.html): Learn about AWS DMS engine versions, and how to choose the engine version for your replication instance.
- [Public and private replication instances](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.PublicPrivate.html): You can specify if a replication instance has a public or private IP address that the instance uses to connect to the source and target databases.
- [IP addressing and network types](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.IPAddressing.html): AWS DMS always creates your replication instance in an Amazon Virtual Private Cloud (VPC).
- [Setting up a network for a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.VPC.html): Use AWS Database Migration Service with various Amazon VPC configurations.
- [Setting an encryption key](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.EncryptionKey.html): Discusses setting the encryption key used for AWS Database Migration Service.
- [Creating a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html): Get started with AWS Database Migration Service, step 2: Create a replication instance.
- [Modifying a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Modifying.html): Modify a replication instance.
- [Rebooting a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Rebooting.html): rebooting a replication instance.
- [Deleting a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Deleting.html): Deleting a replication instance.
- [DMS maintenance window](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.MaintenanceWindow.html): Every AWS DMS replication instance has a weekly maintenance window during which any available system changes are applied.


## [Endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html)

### [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html)

Get started with AWS Database Migration Service, step 3: Specify database endpoints.

- [Using IAM authentication for Amazon RDS endpoint in AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.IAMRDS.html): AWS Identity and Access Management (IAM) database authentication provides enhanced security for your Amazon RDS databases by managing database access through AWS IAM credentials.

### [Sources for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.html)

Use different databases as sources for AWS Database Migration Service.

- [Using Oracle as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html): Use an Oracle database as a source for AWS DMS.

### [Using SQL Server as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html)

Use a Microsoft SQL Server database as a source for AWS DMS.

- [CDC for SQL Server as a Source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.CDC.html): This topic describes how to set up CDC replication on a SQL Server source.
- [Using Azure SQL database as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.AzureSQL.html): Use Microsoft Azure SQL Database as a source for AWS DMS.
- [Using Azure SQL Managed Instance as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.AzureMgd.html): Use Azure SQL Managed Instance as a source for AWS DMS.
- [Using Azure Database for PostgreSQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.AzureDBPostgreSQL.html): Use Microsoft Azure Database for PostgreSQL as a source for AWS DMS.
- [Using Azure Database for MySQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.AzureDBMySQL.html): Use Microsoft Azure Database for MySQL as a source for AWS DMS.
- [Using OCI MySQL Heatwave as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.heatwave.html): Use OCI MySQL Heatwave as a source for AWS DMS.
- [Using Google Cloud for MySQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.GC.html): Use Google Cloud for MySQL as a source for AWS DMS.
- [Using Google Cloud for PostgreSQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.GCPostgres.html): Use Google Cloud for PostgreSQL as a source for AWS DMS.
- [Using PostgreSQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html): Use a PostgreSQL database as a source for AWS DMS.
- [Using MySQL as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html): Use a MySQL database as a source for AWS DMS.
- [Using SAP ASE as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html): Use a SAP ASE database as a source for AWS DMS.
- [Using MongoDB as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html): Use MongoDB as a source for AWS DMS
- [Using Amazon DocumentDB as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html): Use Amazon DocumentDB (with MongoDB compatibility) as a source for AWS DMS.
- [Using Amazon S3 as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html): Use Amazon S3 as a Source for AWS DMS.
- [Using IBM Db2 LUW as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html): Use an IBM Db2 LUW database as a source for AWS DMS.
- [Using IBM Db2 for z/OS as a source](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2zOS.html): Use an IBM Db2 for z/OS database as a source for AWS DMS.

### [Targets for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.html)

Learn about the databases that can be used as a target for data migration using AWS Database Migration Service.

- [Using Oracle as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html): Use an Oracle database as a target for data migration using AWS Database Migration Service.
- [Using SQL Server as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html): Use a Microsoft SQL Server database as a target for data migration using AWS Database Migration Service.
- [Using PostgreSQL as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html): Use a PostgreSQL database as a target for data migration using AWS Database Migration Service.
- [Using MySQL as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html): Use a MySQL-compatible database as a target for data migration using AWS Database Migration Service.
- [Using Amazon Redshift as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html): Use an Amazon Redshift database as a target for data migration using AWS Database Migration Service.
- [Using SAP ASE as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html): Use a SAP ASE database as a target for data migration using AWS Database Migration Service.
- [Using Amazon S3 as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html): Use Amazon S3 as a target for data migration using AWS Database Migration Service.
- [Using Amazon DynamoDB as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html): Use an Amazon DynamoDB database as a target for data migration using AWS Database Migration Service.
- [Using Amazon Kinesis Data Streams as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html): Use Amazon Kinesis Data Streams as a target for data migration using AWS Database Migration Service.
- [Using Apache Kafka as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html): Use Apache Kafka as a target for data migration using AWS Database Migration Service.
- [Using OpenSearch as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html): Use an OpenSearch cluster as a target for data migration using AWS Database Migration Service.
- [Using Amazon DocumentDB as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html): Use Amazon DocumentDB as a target for data migration using AWS Database Migration Service.
- [Using Amazon Neptune as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html): Use Amazon Neptune as a target for data migration with AWS Database Migration Service.
- [Using Redis OSS as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html): Use Redis OSS as a target for data migration with AWS Database Migration Service.
- [Using Babelfish as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Babelfish.html): Use Babelfish as a target for data migration with AWS Database Migration Service.
- [Using Amazon Timestream as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Timestream.html): Use Amazon Timestream as a target for data migration using AWS Database Migration Service.
- [Using Db2 as a target](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DB2.html): Use an IBM Db2 LUW database as a target for AWS DMS.
- [VPC endpoints for data migration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_VPC_Endpoints.html): Learn about VPC source and target endpoints.
- [Supported DDL statements](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Introduction.SupportedDDL.html): Discusses the DDL statements supported by AWS Database Migration Service.

### [Advanced endpoint configuration](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Advanced.Endpoints.html)

Learn about advanced endpoints for AWS Database Migration Service.

- [VPC peering configuration for AWS DMS.](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Advanced.Endpoints.vpc.peering.html): VPC peering enables private network connectivity between two VPCs, allowing AWS DMS replication instances and database endpoints to communicate across different VPCs as if they were in the same network.
- [Security group configuration for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Advanced.Endpoints.securitygroup.html): Security group in AWS DMS must allow inbound and outbound connections for your replication instances on the appropriate database port.
- [Network Access Control List (NACL) configuration for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Advanced.Ednpoints.NACL.html): When using Amazon RDS as a replication source, you should update the Network Access Control Lists (NACLs) for your DMS and RDS instance.
- [Configuring AWS DMS secrets manager VPC Endpoint](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Advanced.Endpoints.secretsmanager.html): You must create a VPC endpoint to access the AWS Secrets Manager from a replication instance in a private subnet.


## [Tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)

### [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html)

How to create a migration task using AWS DMS.

### [Task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html)

Work with settings for AWS Database Migration Service tasks.

- [Target metadata task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TargetMetadata.html): Work with target metadata settings for AWS Database Migration Service tasks.
- [Full-load task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.FullLoad.html): Work with full-load settings for AWS DMS tasks.

### [Time Travel task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.html)

Work with Time Travel settings for AWS DMS tasks.

- [Turning on Time Travel logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.TaskEnabling.html): Turn on Time Travel logs for a task.
- [Time Travel logs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.LogSchema.html): Use the Time Travel logs
- [How often AWS DMS uploads Time Travel logs to S3](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.TimeTravel.UploadsToS3.html): Learn how often AWS DMS uploads Time Travel logs to S3.
- [Logging task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.Logging.html): Work with logging settings for AWS DMS tasks.
- [Control table task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ControlTable.html): Work with the control table settings for AWS DMS tasks.
- [Stream buffer task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.StreamBuffer.html): Work with the stream buffer settings for AWS DMS tasks.
- [Change processing tuning settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html): Work with the change processing tuning settings for AWS DMS tasks.
- [Data validation task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.DataValidation.html): Work with the data validation settings for AWS DMS tasks.
- [Data resync settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.DataResyncSettings.html): The Data resync feature allows you to resync target database with your source database based on data validation report.
- [Task settings for change processing DDL handling](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.DDLHandling.html): Work with the task settings for change processing handling in AWS DMS.
- [Character substitution task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.CharacterSubstitution.html): You can specify that your replication task perform character substitutions on the target database for all source database columns with the AWS DMS STRING or WSTRING data type.
- [Before image task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.BeforeImage.html): When writing CDC updates to a data-streaming target like Kinesis or Apache Kafka, you can view a source database row's original values before change by an update.
- [Error handling task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ErrorHandling.html): You can set the error handling behavior of your replication task using the following settings.
- [Saving task settings](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.Saving.html): You can save task settings as a JSON file in case you want to reuse the settings for another task.
- [Setting LOB support](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.LOBSupport.html): Set the large binary object (LOB) handling in AWS DMS.
- [Creating multiple tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.ReplicationTasks.MultipleTasks.html): Work with multiple replication tasks for AWS DMS.
- [Continuous replication tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html): Perform continuous replication using AWS DMS.
- [Modifying a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Modifying.html): How to modify a migration task using AWS DMS.
- [Moving a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Moving.html): How to move a migration task using AWS DMS.
- [Reloading tables during a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.ReloadTables.html): How to reload tables during a migration task using AWS DMS.

### [Table mapping](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html)

Create table mappings for AWS DMS tasks.

- [Specifying table selection and transformations rules from the console](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.Console.html): You can use the AWS Management Console to perform table mapping, including specifying table selection and transformations.
- [Specifying table selection and transformations rules using JSON](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html): To specify the table mappings that you want to apply during migration, you can create a JSON file.
- [Selection rules and actions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Selections.html): Using table mapping, you can specify what tables, views, and schemas you want to work with by using selection rules and actions.
- [Wildcards in table mapping](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Wildcards.html): This section describes wildcards you can use when specifying the schema and table names for table mapping.
- [Transformation rules and actions](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.html): You use the transformation actions to specify any transformations you want to apply to the selected schema, table, or view.
- [Using transformation rule expressions to define column content](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Expressions.html): Use transformation rule expressions to define column content in AWS Database Migration Service.
- [Table and collection settings rules and operations](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Tablesettings.html): Working with table and collection settings rules and operations in AWS Database Migration Service
- [Using data masking to hide sensitive information](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Masking.html): To conceal sensitive data stored in one or more columns of the tables being migrated, you can leverage Data Masking transformation rule actions.
- [Using source filters](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.Filters.html): Use filters with tasks in AWS DMS.

### [Enabling and working with premigration assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html)

Work with premigration assessment runs to assess tasks using multiple individual assessments.

- [Prerequisites](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Prerequisites.html): This section describes the Amazon S3 and IAM resources you need to create a premigration assessment.
- [Specifying, starting, and viewing assessment runs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.PremigrationAssessmentRuns.html): Specify premigration assessment runs before running a new or existing task.

### [Individual assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Assessments.html)

This section describes individual premigration assessments.

- [Assessments for all endpoint types](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Assessments.All.html): This section describes individual premigration assessments for all endpoint types.
- [Oracle assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Oracle.html): For more information about permissions when using Oracle as a source, see or User account privileges required on an AWS-managed Oracle source for AWS DMS.
- [Sql Server assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.SqlServer.html): This section describes individual premigration assessments for migration tasks that use a Microsoft SQL Server source endpoint.
- [MySQL assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.MySQL.html): This section describes individual premigration assessments for migration tasks that use a MySQL, Aurora MySQL-Compatible Edition or Aurora MySQL-Compatible Edition Serverless source endpoint.
- [MariaDB assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.MariaDB.html): This section describes individual premigration assessments for migration tasks that use a MariaDB source endpoint.
- [PostgreSQL assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.PG.html): This section describes individual premigration assessments for migration tasks that use a PostgreSQL source endpoint.
- [Db2 LUW Assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Db2.html): This section describes individual premigration assessments for migration tasks that use a Db2 LUW source endpoint.
- [Starting and viewing data type assessments](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.DataTypeAssessments.html): Start and view a report that shows unsupported data types for a migration task.
- [Troubleshooting assessment runs](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.Troubleshooting.html): Following, you can find topics about troubleshooting issues with running assessment reports with AWS Database Migration Service.
- [Specifying supplemental data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html): Specify supplemental data for task settings for some AWS DMS endpoints.


## [Monitoring tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.html)

- [Enhanced monitoring dashboard](https://docs.aws.amazon.com/dms/latest/userguide/enhanced-monitoring-dashboard.html): Learn how to use the AWS DMS enhanced monitoring dashboard to track metrics, optimize your data migration tasks, and analyze their performance.
- [Viewing AWS DMS events](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Monitoring.View.dms.events.html): You can retrieve the following event information for your AWS DMS resources:


## [Data validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.html)

- [S3 Validation](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating_S3.html): Validate data in Amazon S3.
- [AWS DMS data resync](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Validating.DataResync.html): AWS Database Migration Service (AWS DMS) Data resync automatically fixes data inconsistencies identified through data validation between your source and target databases.


## [Security](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html)

### [Data protection](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.DataProtection.html)

- [Opting out of storing data](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.dataserviceimprovement.html): You can choose to opt out of having your data used to develop and improve AWS DMS by using the AWS Organizations opt-out policy.
- [Cross-region inference](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.DataProtection.CrossRegionInference.html): Learn how AWS Database Migration Service uses cross-region AI inference for your database migrations.

### [Identity and access management](https://docs.aws.amazon.com/dms/latest/userguide/security-iam.html)

How to authenticate requests and manage access your AWS DMS resources.

- [How AWS Database Migration Service works with IAM](https://docs.aws.amazon.com/dms/latest/userguide/security_iam_service-with-iam.html): Before you use IAM to manage access to AWS DMS, you should understand what IAM features are available to use with AWS DMS.
- [Identity-based policy examples](https://docs.aws.amazon.com/dms/latest/userguide/security_iam_id-based-policy-examples.html): By default, IAM users and roles don't have permission to create or modify AWS DMS resources.
- [Resource-based policy examples](https://docs.aws.amazon.com/dms/latest/userguide/security_iam_resource-based-policy-examples.html): AWS DMS allows you to create custom AWS KMS encryption keys to encrypt supported target endpoint data.
- [Using secrets to access resources](https://docs.aws.amazon.com/dms/latest/userguide/security_iam_secretsmanager.html): Access AWS DMS resources using secrets.

### [Using service-linked roles](https://docs.aws.amazon.com/dms/latest/userguide/using-service-linked-roles.html)

How to use service-linked roles to give AWS DMS access to resources in your AWS account.

- [Fleet Advisor](https://docs.aws.amazon.com/dms/latest/userguide/slr-services-fa.html): AWS DMS Fleet Advisor uses the service-linked role named AWSServiceRoleForDMSFleetAdvisor â DMS Fleet Advisor uses this service-linked role to manage Amazon CloudWatch metrics.
- [Serverless](https://docs.aws.amazon.com/dms/latest/userguide/slr-services-sl.html): AWS DMS uses the service-linked role named AWSServiceRoleForDMSServerless.
- [Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with AWS DMS and IAM.
- [Cross-service confused deputy prevention](https://docs.aws.amazon.com/dms/latest/userguide/cross-service-confused-deputy-prevention.html): The confused deputy problem is a security issue where an entity that doesn't have permission to perform an action can coerce a more-privileged entity to perform the action.
- [AWS managed policies](https://docs.aws.amazon.com/dms/latest/userguide/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS DMS and recent changes to those policies.
- [Compliance validation](https://docs.aws.amazon.com/dms/latest/userguide/dms-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/dms/latest/userguide/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Database Migration Service features for data resiliency.
- [Infrastructure security](https://docs.aws.amazon.com/dms/latest/userguide/infrastructure-security.html): Learn how AWS Database Migration Service isolates service traffic.
- [Fine-grained access control](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.FineGrainedAccess.html): You can use resource names and resource tags based on Amazon Resource Names (ARNs) to manage access to AWS DMS resources.
- [Using SSL](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.SSL.html): Use SSL with AWS DMS
- [Using Kerberos Authentication](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.Kerberos.html): Starting with DMS v3.5.3, you can configure your Oracle or SQL Server source endpoint to connect to your database instance using Kerberos authentication.


## [Troubleshooting and diagnostic support](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting.html)

### [Troubleshooting latency](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency.html)

Troubleshoot latency issues when migrating data using AWS Database Migration Service (AWS DMS).

### [Troubleshooting latency issues](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Troubleshooting.html)

This section contains troubleshooting steps for replication latency.

### [Troubleshooting source latency issues](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Source.html)

The following topics describe replication scenarios specific to source endpoint types.

- [Oracle Endpoint Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Source_Oracle.html): This section contains replication scenarios specific to Oracle.
- [MySQL Endpoint Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Source_MySQL.html): This section contains replication scenarios specific to MySQL.
- [PostgreSQL Endpoint Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Source_PostgreSQL.html): This section contains replication scenarios specific to PostgreSQL.
- [SQL Server Endpoint Troubleshooting](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Source_SQLServer.html): This section contains replication scenarios specific to SQL Server.
- [Troubleshooting target latency issues](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Troubleshooting_Latency_Target.html): This section contains scenarios that can contribute to target latency.

### [Working with diagnostic support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.html)

Work with AWS DMS support scripts to return diagnostics for AWS DMS databases.

- [Oracle support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.Oracle.html): Work with Oracle diagnostic support scripts for AWS DMS.
- [SQL Server support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.SQLServer.html): Work with SQL Server diagnostic support scripts with AWS DMS.
- [MySQL-compatible support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.MySQL.html): Work with MySQL-compatible diagnostic support scripts with AWS DMS.
- [PostgreSQL support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.PostgreSQL.html): Work with PostgreSQL diagnostic support scripts with AWS DMS.
- [Working with the diagnostic support AMI](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportAmi.html): Work with the AWS DMS support AMI to return diagnostics for AWS DMS networks.


## [Reference](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Reference.html)

- [AWS DMS data types](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Reference.DataTypes.html): Discusses the data types used for AWS Database Migration Service.
