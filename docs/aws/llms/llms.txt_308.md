# Source: https://docs.aws.amazon.com/dms/latest/sbs/llms.txt

# Database Migration Guide Step-by-Step Walkthroughs

> Migrate databases to AWS easily and securely using AWS Database Migration Service (AWS DMS) with this Step-by-Step Migration Guide.

- [Database Migration Step-by-Step Walkthroughs](https://docs.aws.amazon.com/dms/latest/sbs/dms-sbs-welcome.html)

## [Migrating Databases to Amazon Web Services Managed Databases](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.html)

### [Migrating a MySQL Database to RDS for MySQL or Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.mysql2rds.html)

Migrate (copy) data from a MySQL database to an Amazon RDS for MySQL or Amazon Aurora MySQL database instance.

- [Full load MySQL database migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.mysql2rds.fullload.html): Discusses tools to move data from your MySQL database to Amazon RDS for MySQL or Amazon Aurora MySQL.
- [Full load MySQL database migration options performance comparison](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.mysql2rds.performance.html): Compares the results of running three tools to move data from your MySQL database to Amazon RDS for MySQL or Amazon Aurora MySQL.
- [Migrate MySQL database with AWS DMS ongoing replication](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.mysql2rds.replication.html): Discusses the ongoing replication in AWS Database Migration Service.

### [Migrating PostgreSQL Databases to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql.html)

This walkthrough gets you started with homogeneous database migration from PostgreSQL to Amazon Relational Database Service (Amazon RDS) for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition.

### [Full load PostgreSQL database migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load.html)

The full load migration phase populates the target database with a copy of the source data.

- [Preparing for Ongoing Replication](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-preparing.html): Before you start full load, make sure that you record the current log sequence number (LSN) as the starting position for ongoing replication.
- [PostgreSQL pg_dump and pg_restore utility](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-pd_dump.html): pg_dump and pg_restore is a native PostgreSQL client utility.
- [PostgreSQL publisher and subscriber model](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-publisher.html): In PostgreSQL, logical replication uses a publisher and subscriber model.
- [PostgreSQL pglogical extension](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-full-load-pglogical.html): The pglogical extension for PostgreSQL implements logical streaming replication, using a similar publish and subscribe built-in approach.
- [Full load PostgreSQL database migration options performance comparison](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-performance-comparison.html): We analyzed the performance of pg_dump and pg_restore, publisher and subscriber, and pglogical in a full load migration.
- [Migrate PostgreSQL database with AWS DMS ongoing replication](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.postgresql-rds-postgresql-ongoing-replication.html): After you complete the full load, make sure that you perform ongoing replication using AWS DMS to keep the source and target databases in sync.

### [Migrating PostgreSQL databases to Amazon RDS for PostgreSQL with DMS homogeneous data migrations](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql.html)

Migrate your PostgreSQL databases to Amazon RDS for PostgreSQL with homogeneous data migrations in AWS DMS.

- [Prerequisties for migrating PostgreSQL databases](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-prerequisites.html): The following prerequisites are also required to complete this walkthrough:
- [PostgreSQL to Amazon RDS migration overview](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-migration-overview.html): This section provides high-level guidance for customers looking to migrate their PostgreSQL database to Amazon RDS for PostgreSQL using homogeneous data migrations in AWS DMS.

### [Step-by-step PostgreSQL database to Amazon RDS migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-by-step-migration.html)

In the following sections, you can find step-by-step instructions for migrating your PostgreSQL database to Amazon RDS for PostgreSQL using homogeneous data migrations in AWS DMS.

- [Step 1: Create AWS Resources](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-1.html): In this step, you create and configure the required AWS resources for homogeneous data migrations in AWS DMS.
- [Step 2: Configure Your Source Database](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-2.html): In this step, you create a new database user on your source PostgreSQL database and configure the data replication.
- [Step 3: Create Your Target Amazon RDS for PostgreSQL Database](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-3.html): In this step, you create a new Amazon RDS for PostgreSQL database to use as a migration target.
- [Step 4: Store Database Credentials in AWS Secrets Manager](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-4.html): To connect to your source and target databases in an AWS DMS migration project, store your database credentials in AWS Secrets Manager.
- [Step 5: Create an Instance Profile](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-5.html): Before you create an instance profile, configure a subnet group for your instance profile.
- [Step 6: Configure Data Providers](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-6.html): In this step, you create data providers that describe your source and target databases.
- [Step 7: Create a Migration Project](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-7.html): Now you can create a migration project.
- [Step 8: Configure a Data Migration](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-8.html): After you create the migration project with two PostgreSQL data providers, you can use this project for homogeneous data migrations.
- [Step 9: Running and Monitoring a Data Migration](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-step-9.html): After you create a data migration, you can run it and monitor its status.
- [PostgreSQL database to Amazon RDS post-migration clean-up](https://docs.aws.amazon.com/dms/latest/sbs/dm-postgresql-next-steps.html): After you migrate your PostgreSQL database to Amazon RDS for PostgreSQL using homogeneous data migrations in AWS DMS, you can explore several other resources:

### [Migrating an Oracle Database to Amazon RDS for Oracle](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.oracle2rds.html)

Read this step-by-step guide to learn more about migrating an Oracle database to Amazon RDS for Oracle.

- [Full load Oracle database migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.oracle2rds.load.html): The full load phase populates the target database with a copy of the source.
- [Full load Oracle database migration options performance comparison](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.oracle2rds.performance.html): We analyzed the Oracle Export/Import, Oracle Data Pump, database link, and SQL*Loader tools for their performance in a full load migration.
- [Migrate Oracle database with AWS DMS ongoing replication](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.oracle2rds.replication.html): After you complete the full load, make sure that you perform ongoing replication using AWS DMS to keep the source and target databases in sync.

### [Migrating a SQL Server Always On Database to Amazon Web Services](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson.html)

Using AWS Database Migration Service to migrate a Microsoft SQL Server Always On database to AWS.

- [Prerequisties for migrating SQL Server AlwaysOn databases to AWS](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson.prerequisites.html): The following prerequisites are required to complete this walkthrough:
- [SQL Server Always On Availability Groups](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson.ag.html): Always On availability groups provide high availability, disaster recovery, and read-scale balancing.

### [Migrating an Amazon RDS for MySQL Database to an Amazon DynamoDB target](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.mysql2dynamodb.html)

Using AWS Database Migration Service to migrate a MySQL or MariaDB database to Amazon DynamoDB.

- [Step-by-step Amazon RDS for MySQL database to Amazon DynamoDB migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.mysql2dynamodb.stepbystepmigration.html): The following steps provide instructions for migrating an Amazon RDS for MySQL database to DynamoDB.

### [Migrating an RDS for MySQL database to an S3 data lake](https://docs.aws.amazon.com/dms/latest/sbs/mysql-s3datalake.html)

Migrate a MySQL database to an Amazon S3 data lake by using AWS Schema Conversion Tool.

- [Choosing an instance class and storage size](https://docs.aws.amazon.com/dms/latest/sbs/mysql-s3datalake.choosinginstanceandstorage.html): Before you start migrating your database, you need to consider your source, target, and replication instance resources such as CPU, memory, disk space, and network bandwidth/latency.
- [Step-By-Step Migration](https://docs.aws.amazon.com/dms/latest/sbs/mysql-s3datalake.stepbystep.html): The following steps provide instructions for migrating Amazon RDS for MySQL databases to an Amazon S3 data lake.

### [Migrating an RDS PostgreSQL database to an S3 data lake](https://docs.aws.amazon.com/dms/latest/sbs/postgresql-s3datalake.html)

Migrate an Amazon RDS PostgreSQL database to an Amazon S3 data lake by using AWS Schema Conversion Tool.

- [Step-by-step an Amazon RDS PostgreSQL database to an Amazon S3 data lake migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/postgresql-s3datalake.stepbystep.html)

### [Migrating SQL Server Databases to Amazon RDS for SQL Server](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server.html)

This walkthrough gets you started with homogeneous database migration from Microsoft SQL Server to Amazon Relational Database Service (Amazon RDS) for SQL Server.

### [Full load SQL Server database migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-full-load.html)

The full load migration phase populates the target database with a copy of the source data.

- [SQL Server database backup and restore using Amazon S3](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-full-load-backup-restore.html): SQL Server database backup and restore using Amazon S3
- [SQL Server import and export wizard](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-full-load-import-export.html): SQL Server import and export wizard
- [Generate and Publish Scripts wizard and Bulk Copy Program Utility](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-full-load-bcp.html): Generate and Publish Scripts wizard and Bulk Copy Program Utility
- [Full load SQL Server database migration options performance comparison](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-performance.html): To compare the full load migration performance for all three methods, we used a test environment.
- [Migrate SQL Server database with AWS DMS ongoing replication](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sql-server-rds-sql-server-replication.html): After you complete the full load, set up ongoing replication using AWS DMS to keep the source and target databases synchronized.

### [Migrating from Amazon RDS for Oracle to Amazon RDS for PostgreSQL and Aurora PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.html)

Migrate from Amazon RDS for Oracle to Amazon RDS for PostgreSQL and Aurora PostgreSQL.

- [Can My Oracle Database Migrate?](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.can-my-db-migrate.html): To quickly see if your workload qualifies as a migration candidate, please use the DMA Connect Application and Database Questionnaire to sort out migration obstacles specific to your application.
- [Oracle application future state architecture design](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.future-state.html): When you migrate an Oracle application to use a different database like PostgreSQL you must capture the architecture of the existing application to ensure that all considerations are covered, we call that the current state architecture.
- [Oracle database schema conversion](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.database-schema-conversion.html): Relational databases contain a tabular structure for data using basic data types and procedural code in the form of triggers, functions and stored procedures.
- [Oracle application conversion or remediation](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.application-conversion.html): The Oracle application may be written in a variety of languages like C++, C# and Java, each with their own patterns for calling Oracle.
- [Database migration script/ETL/report conversion](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.script-conversion.html): ETL is an acronym that stands for Extract, Transform and Load.
- [Oracle application migration and integration with third-party applications](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.integration.html): Few applications are islands and your Oracle application is likely to integrate with other applications that are not themselves going to be migrated.
- [Amazon RDS for Oracle data migration mechanism](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.data-migration.html): For testing purposes and for production cutover, data needs to be migrated from the old Amazon RDS for Oracle instance to the new Amazon RDS or Aurora PostgreSQL instance.
- [Oracle database migration testing and bug fixing](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.testing.html): Testing can be manual or automated.
- [Oracle database migration performance tuning](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.performance-tuning.html): Any migration is likely to slightly change the performance of individual queries in the application and in stored procedures and functions.
- [Oracle dabatase migration to PostgreSQL setup, DevOps, integration, deployment, and security](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.deployment.html): Deployment to production is the culmination of the migration activity and is a high stakes effort which requires good planning and benefits from well tested automation.
- [Oracle dabatase migration to PostgreSQL documentation and knowledge transfer](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.knowledge-transfer.html): As a result of the migration, the operation of the database and the future development of the application and database will have been affected due to infrastructure and technology changes.
- [Oracle dabatase migration to PostgreSQL project management and version control](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.project-management.html): Experience tells us that the steps take different amounts of efforts across a typical project.
- [Oracle dabatase migration to PostgreSQL post-production support](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.migration-process.post-production.html): After production cutover, there are a few possibilities for what can happen.
- [Oracle and PostgreSQL platform differences](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle-postgresql.platform-differences.html): This section discusses some of the differences between Oracle and PostgreSQL to illustrate opportunities and challenges with migrating an Oracle application.

### [Migrating from SAP ASE to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sap-ase-aurora-mysql.html)

Migrate an on-premises SAP ASE database to Amazon Aurora MySQL.

- [Prerequisties for migrating from SAP AWS to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sap-ase-aurora-mysql.prerequisites.html): The following prerequisites are required to complete this walkthrough:
- [Preparation and assessment for migrating from SAP ASE to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sap-ase-aurora-mysql.assessment.html): Preparation and assessment of your source database is the initial phase.
- [SAP ASE to Amazon Aurora MySQL database code conversion and data loading](https://docs.aws.amazon.com/dms/latest/sbs/chap-sap-ase-aurora-mysql.migration.html): This section covers two major database migration tasks: code conversion and data load.
- [Best practices for migrating from SAP ASE to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sap-ase-aurora-mysql.bestpractices.html)


## [Migrating Databases to the Amazon Web Services Cloud Using the Database Migration Service](https://docs.aws.amazon.com/dms/latest/sbs/chap-dms.html)

### [Migrating an On-Premises Oracle Database to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.html)

Migrating an Oracle Database to Amazon Aurora MySQL Using AWS Database Migration Service

- [Migration from Oracle to Aurora MySQL using AWS DMS high-level outline](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.quickstart.html): Learn the high-level concepts involved in migrating from Oracle to Amazon Aurora MySQL.

### [Step-by-step Oracle to Aurora MySQL using AWS DMS migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.html)

View the step-by-step guide to migrating from Oracle to Amazon Aurora MySQL

- [Step 1: Configure Your Oracle Source Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.configureoracle.html): Step 1: Configure Your Oracle Source Database
- [Step 2: Configure Your Aurora Target Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.configureaurora.html): Step 2: Configure Your Aurora MySQL Target Database
- [Step 3: Create a Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createreplicationinstance.html): An AWS DMS replication instance performs the actual data migration between source and target.
- [Step 4: Create Your Oracle Source Endpoint](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createoracle.html): While your replication instance is being created, you can specify the Oracle source endpoint using the AWS Management Console.
- [Step 5: Create Your Aurora MySQL Target Endpoint](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createaurora.html): Next, you can provide information for the target Amazon Aurora MySQL database by specifying the target endpoint settings.
- [Step 6: Create a Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.createtask.html): When you create a migration task you tell AWS DMS exactly how you want your data migrated.
- [Step 7: Monitor Your Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.monitor.html): Three sections in the console provide visibility into what your migration task is doing:
- [Troubleshooting](https://docs.aws.amazon.com/dms/latest/sbs/chap-on-premoracle2aurora.steps.troubleshooting.html): The two most common areas people have issues with when working with Oracle as a source and Aurora MySQL as a target are: supplemental logging and case sensitivity.

### [Migrating an Amazon RDS for Oracle Database to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.html)

Migrate an Amazon RDS for Oracle database to Amazon Aurora MySQL by using AWS Database Migration Service.

- [Prerequisites for migrating from Amazon RDS for Oracle to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.prerequisites.html): Find prerequisites for migrating an Amazon RDS for Oracle database to Amazon Aurora MySQL by using AWS Database Migration Service.
- [Migration architecture for migrating from Amazon RDS for Oracle database to Amazon Aurora MySQL-Compatible Edition](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.architecture.html): Get an overview of the architecture used to migrate an Amazon RDS for Oracle database to Amazon Aurora MySQL-Compatible Edition by using AWS Database Migration Service.

### [Step-by-step Amazon Relational Database Service to Amazon Aurora MySQL-Compatible Edition migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.html)

Migrate an Amazon RDS for Oracle database to Amazon Aurora MySQL.

- [Step 1: Launch the RDS Instances in a VPC by Using the AWS CloudFormation Template](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.launchrdswcloudformation.html): Step 1: Launch your Amazon RDS instances in a VPC by using the AWS CloudFormation template provided.
- [Step 2: Install the SQL Tools and AWS Schema Conversion Tool on Your Local Computer](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.installsct.html): Step 2: Install the SQL tools and the AWS Schema Conversion Tool on your local computer for the AWS DMS migration walkthrough.
- [Step 3: Test Connectivity to the Oracle DB Instance and Create the Sample Schema](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.connectoracle.html): Step 3: Test connectivity to your Oracle DB instance.
- [Step 4: Test the Connectivity to the Aurora MySQL DB Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.connectaurora.html): Step 4: Test connectivity to your Amazon Aurora MySQL DB instance.
- [Step 5: Use the AWS Schema Conversion Tool to Convert the Oracle Schema to Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.convertschema.html): Step 5: Use the AWS Schema Conversion Tool to convert your Oracle schema to an Amazon Aurora MySQL-Compatible Edition schema.
- [Step 6: Validate the Schema Conversion](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.validateschemaconversion.html): Step 6: Validate the Schema Conversion
- [Step 7: Create an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.createreplicationinstance.html): Step 7: Create an AWS DMS Replication Instance
- [Step 8: Create AWS DMS Source and Target Endpoints](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.createsourcetargetendpoints.html): Step 8: Create AWS DMS Source and Target Endpoints
- [Step 9: Create and Run Your AWS DMS Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.createmigrationtask.html): Create an AWS DMS migration task by specifying what schema to migrate and the type of migration.
- [Step 10: Verify That Your Data Migration Completed Successfully](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.verifydatamigration.html): Verify that your AWS DMS data migration completed successfully.
- [Step 11: Delete Walkthrough Resources](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.steps.deleteresources.html): After you have completed this walkthrough, perform the following steps to avoid being charged further for AWS resources used in the walkthrough.
- [AWS DMS migration from Amazon RDS for Oracle next steps](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2aurora.nextsteps.html): You can explore several other features of AWS DMS that were not included in this walkthrough, including the following:

### [Migrating a SQL Server Database to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.html)

Migrate a Microsoft SQL Server database to Amazon Aurora MySQL Using AWS Database Migration Service.

- [Prerequisites for Migrating from a SQL Server database to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.prerequisites.html): Find prerequisites for migrating a Microsoft SQL Server database to Aurora MySQL by using AWS Database Migration Service.

### [Step-by-step SQL Server database to Amazon Aurora MySQL migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.html)

Follow step-by-step guidance for migrating a Microsoft SQL Server database to Aurora MySQL.

- [Step 1: Install the SQL Drivers and AWS Schema Conversion Tool on Your Local Computer](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.installsct.html): Step 1: Install the SQL drivers and AWS SCT on your local computer for the AWS DMS migration walkthrough.
- [Step 2: Configure Your Microsoft SQL Server Source Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.configuresqlserver.html): Step 2: Choose the appropriate options for configuring your SQL Server source database.
- [Step 3: Configure Your Aurora MySQL Target Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.configureaurora.html): Step 3: Configure your Aurora MySQL target database and create the AWS DMS user to connect to the database
- [Step 4: Use AWS SCT to Convert the SQL Server Schema to Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.convertschema.html): Step 4: Use the AWS Schema Conversion Tool to convert your SQL Server schema to an Aurora MySQL schema.
- [Step 5: Create an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.createreplicationinstance.html): Step 5: Overview of the data migration process
- [Step 6: Create AWS DMS Source and Target Endpoints](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.createsourcetargetendpoints.html): Step 6: Specify the source and target database endpoints for your data migration.
- [Step 7: Create and Run Your AWS DMS Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.createmigrationtask.html): Step 7: Create an AWS DMS migration task by specifying what schema to migrate and the type of migration.
- [Step 8: Cut Over to Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.cutover.html): Step 8: Move connections from your SQL Server source database to your target Aurora MySQL database.
- [SQL Server database migration to Amazon Aurora MySQL troubleshooting](https://docs.aws.amazon.com/dms/latest/sbs/chap-sqlserver2aurora.steps.troubleshooting.html): Troubleshoot issues when migrating data between SQL Server and Aurora MySQL.

### [Migrating a SQL Server AlwaysOn Database on Primary Replica to Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson2aurorapostgresql.html)

Using AWS Database Migration Service to migrate a Microsoft SQL Server Always On database to Amazon Aurora PostgreSQL.

- [Prerequisties for migrating SQL Server AlwaysOn databases on primary replica to Amazon Aurora PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson2aurorapostgresql.prerequisites.html): The following prerequisites are required to complete this migration:
- [Step-by-step SQL Server AlwaysOn databases on primary replica to Amazon Aurora PostgreSQL migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-manageddatabases.sqlserveralwayson2aurorapostgresql.sbs.html): The following standard steps assume you have prepared your source and target endpoint as described in the above prerequisites.

### [Migrating an Amazon RDS for Oracle Database to an Amazon S3 Data Lake](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake.html)

Using AWS Database Migration Service to migrate an Amazon RDS for Oracle database to an Amazon S3 data lake.

- [Prerequisites for migrating an RDS for Oracle database to an Amazon S3 data lake](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-prerequisites.html): Find prerequisites for migrating an Oracle database to an Amazon S3 data lake by using AWS Database Migration Service.

### [Step-by-step Amazon RDS for Oracle database to Amazon S3 data lake migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-by-step.html)

Find the steps to take to migrate an Oracle database to an Amazon S3 data lake by using AWS Database Migration Service.

- [Step 1: Create an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-1.html): Learn how to create an AWS DMS replication instance.
- [Step 2: Configure a Source Amazon RDS for Oracle Database](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-2.html): Learn how to configure your source Amazon RDS for Oracle database for the migration to an Amazon S3 data lake.
- [Step 3: Create an AWS DMS Source Endpoint](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-3.html): Learn how to create your source AWS DMS endpoint.
- [Step 4: Create a Target Amazon S3 Bucket](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-4.html): Learn how to create your target Amazon S3 bucket.
- [Step 5: Configure an AWS DMS Target Endpoint](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-5.html): Learn how to configure your target AWS DMS endpoint.
- [Step 6: Create an AWS DMS Task](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-6.html): Learn how to create an AWS DMS task to migrate from Oracle to an Amazon S3 data lake.
- [Step 7: Run the AWS DMS Task](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-step-7.html): Learn how to run the AWS DMS task to migrate from Oracle to an Amazon S3 data lake.
- [Step-by-step Amazon RDS for Oracle database to Amazon S3 data lake migration conclusion](https://docs.aws.amazon.com/dms/latest/sbs/oracle-s3-data-lake-conclusion.html): See the results o the migration from Oracle to an Amazon S3 data lake.

### [Migrating an Amazon RDS for SQL Server Database to an Amazon S3 Data Lake](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.html)

Using AWS Database Migration Service to migrate an Amazon RDS for SQL Server database to an Amazon S3 data lake.

- [Prerequisties for migrating from an Amazon RDS for SQL Server database to an Amazon S3 data lake](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.prerequisites.html): Find prerequisites for migrating a Microsoft SQL Server database to an Amazon S3 data lake by using AWS Database Migration Service.

### [Step-by-step Amazon RDS for SQL Server database to an Amazon S3 data lake migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.html)

Follow step-by-step guidance for migrating a Microsoft SQL Server database to Amazon S3 data lake.

- [Step 1: Create an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.createreplicationinstance.html): Step 1: Follow this guidance to create an AWS DMS replication instance.
- [Step 2: Configure a Source Amazon RDS for SQL Server Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.configuresource.html): Step 2: Follow this guidance to configure your Amazon RDS for SQL Server database.
- [Step 3: Create an AWS DMS Source Endpoint](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.sourceendpoint.html): Step 3: Follow this guidance to create a source endpoint.
- [Step 4: Configure a Target Amazon S3 Bucket](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.targets3bucket.html): Step 4: Follow this guidance to configure a target Amazon S3 bucket.
- [Step 5: Configure an AWS DMS Target Endpoint](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.targetendpoint.html): Step 5: Follow this guidance to create an AWS DMS target endpoint.
- [Step 6: Create an AWS DMS Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.createtask.html): Step 6: Follow this guidance to create an AWS DMS task.
- [Step 7: Run the AWS DMS Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdssqlserver2s3datalake.steps.runtask.html): Step 7: Follow this guidance to run the AWS DMS task.

### [Migrating an Oracle Database to PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.html)

Migrate an Oracle database to PostgreSQL by using AWS Database Migration Service.

- [Prerequisites for migrating from an Oracle database to PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.prerequisites.html): Find prerequisites for migrating an Oracle database to PostgreSQL by using AWS Database Migration Service.

### [Step-by-step Oracle database to PostgreSQL migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.html)

Migrate an Oracle database to PostgreSQL.

- [Step 1: Install the SQL Drivers and AWS Schema Conversion Tool on Your Local Computer](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.installsct.html): Step 1: Install the SQL drivers and the AWS Schema Conversion Tool on your local computer for the AWS DMS migration walkthrough.
- [Step 2: Configure Your Oracle Source Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle2postgresql.steps.configureoracle.html): Step 2: Configure Your Oracle Source Database
- [Step 3: Configure Your PostgreSQL Target Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle2postgresql.steps.configurepostgresql.html): Step 3: Configure Your PostgreSQL Target Database
- [Step 4: Use AWS SCT to Convert the Oracle Schema to PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.convertschema.html): Step 4: Use the AWS Schema Conversion Tool to convert your Oracle schema to a PostgreSQL schema.
- [Step 5: Create an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.createreplicationinstance.html): Step 5: Create an AWS DMS Replication Instance
- [Step 6: Create AWS DMS Source and Target Endpoints](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.createsourcetargetendpoints.html): Step 6: Create AWS DMS Source and Target Endpoints
- [Step 7: Create and Run Your AWS DMS Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.createmigrationtask.html): Create an AWS DMS migration task by specifying what schema to migrate and the type of migration.
- [Step 8: Cut Over to PostgreSQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2postgresql.steps.cutover.html): To move connections from your Oracle database to your PostgreSQL database, do the following:
- [Rolling Back the Migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle2postgresql.rollback.html): If there are major issues with the migration that cannot be resolved in a timely manner, you can roll back the migration.
- [Oracle database migration to PostgreSQL troubleshooting](https://docs.aws.amazon.com/dms/latest/sbs/chap-oracle2postgresql.troubleshooting.html): The two most common problem areas when working with Oracle as a source and PostgreSQL as a target are: supplemental logging and case sensitivity.

### [Migrating Oracle databases to Amazon Aurora MySQL with DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql.html)

Migrate your Oracle databases to Aurora MySQL by using DMS Schema Conversion.

- [Prerequisites for Migrating Oracle databases to Amazon RDS for MySQL with DMS schema conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-prerequisites.html): The following prerequisites are also required to complete this walkthrough:

### [Step-by-step Oracle database to Amazon RDS for MySQL with DMS schema conversion migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-by-step-migration.html)

In the following sections, you can find step-by-step instructions for migrating your Oracle database to Aurora MySQL using DMS Schema Conversion.

- [Step 1: Create AWS Resources](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-1.html): In this step, you create and configure the required AWS resources for DMS Schema Conversion.
- [Step 2: Configure Your Source Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-2.html): In this step, you configure a new database user on your source Oracle database.
- [Step 3: Create Your Target Aurora MySQL Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-3.html): In this step, you create a new Aurora MySQL database to use as a migration target for DMS Schema Conversion.
- [Step 4: Store Database Credentials in AWS Secrets Manager](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-4.html): To connect to your source and target databases with DMS Schema Conversion, store your database credentials in AWS Secrets Manager.
- [Step 5: Create an Instance Profile](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-5.html): Before you create an instance profile, configure a subnet group for your instance profile.
- [Step 6: Configure Data Providers](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-6.html): In this step, you create data providers that describe your source and target databases.
- [Step 7: Create a Migration Project](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-7.html): Now you can create a migration project which is the foundation of your work with DMS Schema Conversion.
- [Step 8: Convert Database Objects](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-8.html): After you create the migration project, you can convert your Oracle database schemas to MySQL.
- [Step 9: Edit and Apply Your Converted Code](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-step-9.html): After you convert your source Oracle database objects, you can review the conversion statistics.
- [Migration from Oracle database to Amazon RDS for MySQL with DMS schema conversion next steps](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-aurora-mysql-next-steps.html): After you migrate your Oracle database to Aurora MySQL using DMS Schema Conversion, you can explore several other resources:

### [Migrating Oracle databases to Amazon RDS for PostgreSQL with DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql.html)

Migrate your Oracle databases to Amazon RDS for PostgreSQL by using DMS Schema Conversion.

- [Prerequisites for migrating Oracle databases to Amazon Aurora PostgreSQL with DMS schema conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-prerequisites.html): The following prerequisites are also required to complete this walkthrough:

### [Step-by-step Oracle databases to Amazon Aurora PostgreSQL with DMS schema conversion migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-by-step-migration.html)

In the following sections, you can find step-by-step instructions for migrating your Oracle database to Amazon RDS for PostgreSQL using DMS Schema Conversion.

- [Step 1: Create AWS Resources](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-1.html): In this step, you create and configure the required AWS resources for DMS Schema Conversion.
- [Step 2: Configure Your Source Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-2.html): In this step, you configure a new database user on your source Oracle database.
- [Step 3: Create Your Target Amazon RDS for PostgreSQL Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-3.html): In this step, you create a new Amazon RDS for PostgreSQL database to use as a migration target for DMS Schema Conversion.
- [Step 4: Store Database Credentials in AWS Secrets Manager](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-4.html): To connect to your source and target databases with DMS Schema Conversion, store your database credentials in AWS Secrets Manager.
- [Step 5: Create an Instance Profile](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-5.html): Before you create an instance profile, configure a subnet group for your instance profile.
- [Step 6: Configure Data Providers](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-6.html): In this step, you create data providers that describe your source and target databases.
- [Step 7: Create a Migration Project](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-7.html): Now you can create a migration project which is the foundation of your work with DMS Schema Conversion.
- [Step 8: Convert Database Objects](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-8.html): After you create the migration project, you can convert your Oracle database schemas to PostgreSQL.
- [Step 9: Edit and Apply Your Converted Code](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-step-9.html): After you convert your source Oracle database objects, you can review the conversion statistics.
- [Migration from Oracle databases to Amazon Aurora PostgreSQL with DMS schema conversion next steps](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-oracle-postgresql-next-steps.html): After you migrate your Oracle database to Amazon RDS for PostgreSQL using DMS Schema Conversion, you can explore several other resources:

### [Migrating SQL Server databases to Amazon Aurora PostgreSQL with DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql.html)

Migrate your SQL Server databases to Aurora PostgreSQL by using DMS Schema Conversion.

- [Prerequisites for migrating SQL Server databases to Aurora PostgreSQL with DMS schema conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-prerequisites.html): The following prerequisites are also required to complete this walkthrough:

### [Step-by-step SQL Server database to Aurora PostgreSQL with DMS schema conversion migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-by-step-migration.html)

In the following sections, you can find step-by-step instructions for migrating your SQL Server database to Aurora PostgreSQL using DMS Schema Conversion.

- [Step 1: Create AWS Resources](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-1.html): In this step, you create and configure the required AWS resources for DMS Schema Conversion.
- [Step 2: Configure Your Source Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-2.html): In this step, you configure a new database user on your source SQL Server database.
- [Step 3: Create Your Target Aurora PostgreSQL Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-3.html): In this step, you create a new Aurora PostgreSQL database to use as a migration target for DMS Schema Conversion.
- [Step 4: Store Database Credentials in AWS Secrets Manager](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-4.html): To connect to your source and target databases with DMS Schema Conversion, store your database credentials in AWS Secrets Manager.
- [Step 5: Create an Instance Profile](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-5.html): Before you create an instance profile, configure a subnet group for your instance profile.
- [Step 6: Configure Data Providers](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-6.html): In this step, you create data providers that describe your source and target databases.
- [Step 7: Create a Migration Project](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-7.html): Now you can create a migration project which is the foundation of your work with DMS Schema Conversion.
- [Step 8: Convert Database Objects](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-8.html): After you create the migration project, you can convert your SQL Server database schemas to PostgreSQL.
- [Step 9: Edit and Apply Your Converted Code](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-step-9.html): After you convert your source SQL Server database objects, you can review the conversion statistics.
- [Migration from SQL Server databases to Aurora PostgreSQL with DMS schema conversion next steps](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-aurora-postgresql-next-steps.html): After you migrate your SQL Server database to Aurora PostgreSQL using DMS Schema Conversion, you can explore several other resources:

### [Migrating SQL Server databases to Amazon RDS for MySQL with DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql.html)

Migrate your SQL Server databases to Amazon RDS for MySQL by using DMS Schema Conversion.

- [Prerequisites for migrating SQL Server databases to Amazon RDS for MySQL with DMS schema conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-prerequisites.html): The following prerequisites are also required to complete this walkthrough:

### [Step-by-step SQL Server databases to Amazon RDS for MySQL with DMS schema conversion](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-by-step-migration.html)

In the following sections, you can find step-by-step instructions for migrating your SQL Server database to Amazon RDS for MySQL using DMS Schema Conversion.

- [Step 1: Create AWS Resources](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-1.html): In this step, you create and configure the required AWS resources for DMS Schema Conversion.
- [Step 2: Configure Your Source Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-2.html): In this step, you configure a new database user on your source SQL Server database.
- [Step 3: Create Your Target Amazon RDS for MySQL Database](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-3.html): In this step, you create a new Amazon RDS for MySQL database to use as a migration target for DMS Schema Conversion.
- [Step 4: Store Database Credentials in AWS Secrets Manager](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-4.html): To connect to your source and target databases with DMS Schema Conversion, store your database credentials in AWS Secrets Manager.
- [Step 5: Create an Instance Profile](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-5.html): Before you create an instance profile, configure a subnet group for your instance profile.
- [Step 6: Configure Data Providers](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-6.html): In this step, you create data providers that describe your source and target databases.
- [Step 7: Create a Migration Project](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-7.html): Now you can create a migration project which is the foundation of your work with DMS Schema Conversion.
- [Step 8: Convert Database Objects](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-8.html): After you create the migration project, you can convert your SQL Server database schemas to MySQL.
- [Step 9: Edit and Apply Your Converted Code](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-step-9.html): After you convert your source SQL Server database objects, you can review the conversion statistics.
- [Migration from SQL Server databases to Amazon RDS for MySQL with DMS schema conversion next steps](https://docs.aws.amazon.com/dms/latest/sbs/schema-conversion-sql-server-mysql-next-steps.html): After you migrate your SQL Server database to Amazon RDS for MySQL using DMS Schema Conversion, you can explore several other resources:

### [Migrating an Amazon RDS for Oracle Database to Amazon Redshift](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.html)

Migrate an Amazon RDS for Oracle database to Amazon Redshift by using AWS Database Migration Service.

- [Prerequisites for migrating from Amazon RDS for Oracle to Amazon Redshift](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.prerequisites.html): Find prerequisites for migrating an Amazon RDS for Oracle database to Amazon Redshift by using AWS Database Migration Service.
- [Migration architecture for migrating from Amazon RDS for Oracle to Amazon Redshift](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.architecture.html): Get an overview of the architecture used to migrate an Amazon RDS for Oracle database to Amazon Redshift by using AWS Database Migration Service.

### [Step-by-step Amazon RDS for Oracle to Amazon Redshift migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.html)

Migrate an Amazon RDS for Oracle database to Amazon Redshift.

- [Step 1: Launch the RDS Instances in a VPC by Using the AWS CloudFormation Template](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.launchrdswcloudformation.html): Step 1: Launch your Amazon RDS instances in a VPC by using the AWS CloudFormation template provided.
- [Step 2: Install the SQL Tools and AWS Schema Conversion Tool on Your Local Computer](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.installsct.html): Step 2: Install the SQL tools and the AWS Schema Conversion Tool on your local computer for the AWS DMS migration walkthrough.
- [Step 3: Test Connectivity to the Oracle DB Instance and Create the Sample Schema](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.connectoracle.html): Step 3: Test connectivity to your Oracle DB instance.
- [Step 4: Test the Connectivity to the Amazon Redshift Database](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.connectredshift.html): Step 4: Test connectivity to your Amazon Redshift DB instance.
- [Step 5: Use AWS SCT to Convert the Oracle Schema to Amazon Redshift](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.convertschema.html): Step 5: Use the AWS Schema Conversion Tool to convert your Oracle schema to an Amazon Redshift schema.
- [Step 6: Validate the Schema Conversion](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.validateschemaconversion.html): Step 6: Validate the Schema Conversion
- [Step 7: Create an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.createreplicationinstance.html): Step 7: Create an AWS DMS Replication Instance
- [Step 8: Create AWS DMS Source and Target Endpoints](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.createsourcetargetendpoints.html): Step 8: Create AWS DMS Source and Target Endpoints
- [Step 9: Create and Run Your AWS DMS Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.createmigrationtask.html): Create an AWS DMS migration task by specifying what schema to migrate and the type of migration.
- [Step 10: Verify That Your Data Migration Completed Successfully](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.verifydatamigration.html): Verify that your AWS DMS data migration completed successfully.
- [Step 11: Delete Walkthrough Resources](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.steps.deleteresources.html): After you have completed this walkthrough, perform the following steps to avoid being charged further for AWS resources used in the walkthrough.
- [Migration from Amazon RDS for Oracle to Amazon Redshift next steps](https://docs.aws.amazon.com/dms/latest/sbs/chap-rdsoracle2redshift.nextsteps.html): You can explore several other features of AWS DMS that were not included in this walkthrough, including the following:

### [Migrating a BigQuery Project to Amazon Redshift](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift.html)

Migrate a BigQuery Project to Amazon Redshift by using AWS Schema Conversion Tool.

- [Prerequisites for migrating a BigQuery project to Amazon Redshift](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-prerequisites.html): The following prerequisites are also required to complete this walkthrough:

### [Step-by-Step BigQuery project to Amazon Redshift migration walkthrough](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-step-by-step-migration.html)

In the following sections, you can find step-by-step instructions for migrating your BigQuery project to Amazon Redshift.

- [Step 1: Create a BigQuery Service Account Key File](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-1.html): You can connect to BigQuery with a user account or a service account.
- [Step 2: Create an Amazon Redshift Cluster](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-2.html): To store your data in the AWS cloud, you can use your existing Amazon Redshift cluster or create a new one.
- [Step 3: Create Buckets to Store Your Temporary Data](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-3.html): Data migration from BigQuery to Amazon Redshift includes the following steps:
- [Step 4: Install AWS SCT on Your Local Computer](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-4.html): In this step, you install and configure the AWS Schema Conversion Tool.
- [Step 5: Create an AWS SCT Project](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-5.html): After you configure AWS SCT, create a new migration project.
- [Step 6: Convert Database Schemas](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-6.html): After you create a new AWS SCT project, convert your source database schemas and apply converted code to your target database.
- [Step 7: Install and Configure Data Extraction Agents](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-7.html): AWS SCT uses a data extraction agent to migrate data from BigQuery to Amazon Redshift.
- [Step 8: Run Your Migration Task](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-8.html): After you install and configure the data extraction agent, register it in AWS SCT.
- [Step 9: Delete Walkthrough Resources](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-migration-step-9.html): After you complete this step-by-step guide, make sure that you delete your Amazon Redshift cluster to avoid additional charges.
- [Migration from a BigQuery project to Amazon Redshift next steps](https://docs.aws.amazon.com/dms/latest/sbs/bigquery-redshift-next-steps.html): After you migrate your BigQuery project to Amazon Redshift, you can explore several other resources:

### [Migrating a MySQL-Compatible Database to Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-mysql2aurora.html)

Migrate (copy) data from a MySQL database or RDS MySQL DB snapshot to an Amazon Aurora MySQL DB cluster.

- [Migrating Data from an Amazon RDS MySQL DB Instance to an Amazon Aurora MySQL DB Cluster](https://docs.aws.amazon.com/dms/latest/sbs/chap-mysql2aurora.rdsmysql.html): You can migrate (copy) data to an Amazon Aurora MySQL DB cluster from an Amazon RDS snapshot, as described following.

### [Migrating a MariaDB Database to Amazon RDS for MySQL or Amazon Aurora MySQL](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.html)

Learn how to migrate a MariaDB database to Amazon Aurora MySQL-Compatible Edition by using AWS DMS.

- [Set up MariaDB as a source database](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.provisioningmariadb.html): Learn how to provision a MariaDB database to migrate to Amazon Aurora MySQL-Compatible Edition by using AWS DMS.
- [Set up Aurora MySQL as a target database](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.provisioningauroramysql.html): Learn how to provision an Amazon Aurora MySQL-Compatible Edition database so you can migrate a MariaDB database to it by using AWS DMS.
- [Set up an AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.provisioningdms.html): Learn how to provision an AWS DMS replication instance to migrate a MariaDB database to migrate to Amazon RDS for MySQL or Amazon Aurora MySQL-Compatible Edition by using AWS DMS.
- [Test the endpoints for MariaDB database migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.testendpoints.html)
- [Create a migration task for a MariaDB database](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.createtask.html): Weâve now verified that the replication instance can connect to both the source and target endpoints.
- [Validate the MariaDB database migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.validate.html): AWS DMS performs data validation to confirm that your data successfully migrated the source database to the target.
- [Cut over for the migration from a MariaDB database](https://docs.aws.amazon.com/dms/latest/sbs/chap-mariadb2auroramysql.cutover.html): After the data validation is complete and any problems resolved, you can load the database triggers, functions, and procedures.

### [Migrating from MongoDB to Amazon DocumentDB](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.html)

Use the following tutorial to guide you through the process of migrating from MongoDB to Amazon DocumentDB (with MongoDB compatibility).

- [Launch an Amazon EC2 instance for MongoDB migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.01.html): For this tutorial, you launch an Amazon EC2 instance into your default VPC.
- [Install and configure MongoDB community edition](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.02.html): Perform these steps on the Amazon EC2 instance that you launched in Launch an Amazon EC2 instance.
- [Create an AWS DMS replication instance for MongoDB migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.03.html): To perform replication in AWS DMS, you need a replication instance.
- [Create source and target endpoints for MongoDB migration](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.04.html): The source endpoint is the endpoint for your MongoDB installation running on your Amazon EC2 instance.
- [Create and run a MongoDB migration task](https://docs.aws.amazon.com/dms/latest/sbs/chap-mongodb2documentdb.05.html): You are now ready to launch an AWS DMS migration task, to migrate the zips data from MongoDB to Amazon DocumentDB.
