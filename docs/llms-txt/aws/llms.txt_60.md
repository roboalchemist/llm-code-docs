# Source: https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/llms.txt

# AWS Schema Conversion Tool User Guide

> Use the AWS Schema Conversion Tool (AWS SCT) to help convert a database schema to a schema you can use with AWS resources. For example, you can use AWS SCT to convert a database schema to migrate a data store to Amazon Relational Database Service (RDS), an Amazon Redshift cluster, an Amazon Aurora DB cluster, or as data stored on Amazon S3.

- [What is AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)
- [Getting started](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_GettingStarted.html)
- [Integrating with AWS DMS](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_DMSIntegration.html)
- [Migrating from a data warehouse](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/agents.html)
- [Extension packs](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_ExtensionPack.html)
- [Best practices](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_BestPractices.html)
- [Troubleshooting](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Troubleshooting.html)
- [CLI Reference](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Reference.html)
- [Release notes](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_ReleaseNotes.html)
- [Document history](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/WhatsNew.html)

## [Installing and Configuring AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.html)

- [Installing AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.Procedure.html): This section of the AWS Schema Conversion Tool user guide shows how to install AWS SCT on your local system, including the prerequisites, setup instructions, and any necessary configurations for different operating systems.
- [Validating installation](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.InstallValidation.html): This section of the AWS Schema Conversion Tool user guide shows how to validate and verify the successful installation of the tool by running a test command and checking the output for any errors or issues, as well as how to troubleshoot and diagnose potential problems during the installation process.
- [Installing JDBC drivers](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.JDBCDrivers.html): This section of the AWS Schema Conversion Tool user guide shows you how to install and configure the necessary JDBC drivers for connecting to different database sources, including vendor-specific instructions, prerequisites, and troubleshooting steps to ensure successful database connectivity for the schema conversion process.
- [Updating AWS SCT](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.Updating.html): This section of the AWS Schema Conversion Tool user guide shows how to update the tool to the latest version, including checking for new releases, downloading and installing updates or patches, reviewing release notes for changes and improvements, ensuring compatibility with your existing setup, and troubleshooting any issues that may arise during the update process.
- [AWS Schema Conversion Tool CLI](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Installing.CLI.html): This section of the AWS SCT user guide shows how to update the tool to the latest version, including checking for new releases, downloading and installing updates or patches, reviewing release notes for changes and improvements, ensuring compatibility with your existing setup, and troubleshooting any issues that may arise during the update process.


## [AWS SCT user interface](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.html)

- [Project window](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.Overview.ProjectWindow.html): This section of the AWS Schema Conversion Tool user guide shows you how to view and navigate the Project Window, which is the main interface for managing your schema conversion projects.
- [Starting and Managing projects](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.Project.html): This section of the AAWS Schema Conversion Tool user guide shows how to manage your schema conversion projects, including starting the tool, creating new projects, opening existing projects, and working with project files.
- [Using the Wizard](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.Wizard.html): This section of the A AWS Schema Conversion Tool user guide shows you how to use the Wizard, which provides a step-by-step process for converting your database schema determine the migration target with a new project wizard.
- [Saving projects](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.SaveProject.html): This section of the AWS Schema Conversion Tool user guide shows you how to save your schema conversion projects, including creating new project files and overwriting existing project files.
- [Adding database servers](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.AddServers.html): This section of the AWS Schema Conversion Tool user guide shows how to add source and target database servers for your schema conversion and data migration projects.
- [Offline mode](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.OfflineMode.html): This section of the AWS Schema Conversion Tool user guide shows you how to use the Offline Mode feature, which allows you to work on schema conversion projects without an active internet connection.
- [Tree filters](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.TreeFilters.html): This section of the AWS Schema Conversion Tool user guide shows you how to use the Tree Filters feature, which allows you to filter and organize the schema elements displayed in the project tree view.
- [Hiding schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.HidingSchemas.html): This section of the AWS Schema Conversion Tool user guide shows you how to hide or show database schemas in the project tree view, allowing you to better manage and organize your schema conversion projects.
- [Assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.AssessmentReport.html): This section of the AWS Schema Conversion Tool user guide shows you how to view and interpret the Assessment Report, which provides detailed information about the compatibility of your source database schema with the target AWS database service.
- [Converting schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.Converting.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert your source database schema to the target AWS database service, including selecting the appropriate conversion settings and applying any necessary transformations.
- [Applying converted schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.ApplyingConversion.html): This section of the AWS Schema Conversion Tool user guide shows you how to apply a conversion to transform your source data schema into the desired target data schema using the AWS Schema Conversion Tool.
- [Managing profiles](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.Profiles.html): This section of the AWS Schema Conversion Tool user guide shows you how to manage user profiles in the AWS Schema Conversion Tool, allowing you to customize settings and preferences for your data conversion tasks.
- [Configuring Secrets Manager](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.SecretsManager.html): This section of the AWS Schema Conversion Tool user guide shows you how to configure AWS Secrets Manager in AWS SCT for secure management of your database credentials and sensitive data during the conversion process.
- [Storing database passwords](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.StoringPasswords.html): This section of the AWS Schema Conversion Tool user guide shows you how to securely store and manage passwords and sensitive data within the AWS Schema Conversion Tool, ensuring proper data protection and following security best practices.
- [UNION ALL view](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.UnionAllView.html): This section of the AWS Schema Conversion Tool user guide shows you how to create a UNION ALL view, which allows you to consolidate and merge data from multiple tables or queries into a single virtual table for efficient data processing and transformation.
- [Keyboard shortcuts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_UserInterface.KeyboardShortcuts.html): This section of the AWS Schema Conversion Tool user guide shows you how to use keyboard shortcuts to streamline your workflow and increase productivity while working with AAWS SCT, enhancing your overall user experience.


## [Connecting to source databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.html)

- [Connecting to encrypted Amazon RDS and and Aurora](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Encrypt.RDS.html): This section explains how to connect the AWS Schema Conversion Tool to encrypted Amazon Relational Database Service and Amazon Aurora including configuring SSL/TLS connections and managing encryption keys for secure data transfer during the migration process..
- [Connecting to Apache Cassandra](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Cassandra.html): This section provides instructions to connect AWS Schema Conversion Tool to Apache Cassandra databases, including configuring the connection settings, testing the connection, and creating a new conversion project in the AWS SCT user interface.
- [Connecting to Apache Hadoop](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Hadoop.html): This section provides instructions to connect AWS Schema Conversion Tool to Apache Hadoop databases, including configuring the connection settings and testing the connection before creating a new conversion project.
- [Connecting to Apache Oozie](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oozie.html): This section covers the process of connecting the AWS SCT Apache Oozie, a workflow scheduler for Apache Hadoop, to manage and monitor the data conversion process during database migration projects.
- [Connecting to Azure SQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.AzureSQL.html): >This section of the AWS Schema Conversion Tool guide provides instructions to conntct to Microsoft Azure SQL databases, including configuring the connection settings, testing the connection, and creating a new conversion project in the AWS SCT user interface.
- [Connecting to IBM DB2 for z/OS](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2zOS.html): instruction on connecting AWS SCT to IBM Db2 for z/OS databases, allowing users to convert schemas from their mainframe database environments to AWS database services.

### [IBM Db2 LUW databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2LUW.html)

This section of the AWS Schema Conversion Tool guide provides instruction to connect AWS SCT IBM DB2 for Linux, UNIX, and Windows (DB2 LUW) databases, including configuring the connection settings, testing the connection, and creating a new conversion project in the AWS SCT user interface

- [Db2 LUW to PostgreSQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2LUW.ToPostgreSQL.html): This section of the AWS Schema Conversion Tool guide provides instructions to migrate data from IBM DB2 for Linux, UNIX, and Windows to Amazon Relational Database Service for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition using the AWS SCT.
- [Db2 LUW to MySQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.DB2LUW.ToMySQL.html): This section of the AWS Schema Conversion Tool guide provides instructions to migrate data from IBM DB2 for Linux, UNIX, and Windows to Amazon RDS for MySQL or Amazon Aurora MySQL using the AWS Schema Conversion Tool.
- [Using MySQL as a source](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.MySQL.html): Instructions on how to connect AWS SCT to MySQL databases, enabling schema conversion from MySQL to AWS database services

### [Oracle databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.html)

This section of the AWS Schema Conversion Tool guide provides instructions on how to connect AWS SCT to Oracle databases, including configuring the connection settings, testing the connection, and creating a new conversion project in the AWS SCT user interface.

- [Oracle to PostgreSQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.ToPostgreSQL.html): This section of the AWS Schema Conversion Tool guide provides intructions to migrate data from Oracle Database to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL using the AWS SCT.
- [Oracle to MySQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.ToMySQL.html): This section of the AWS Schema Conversion Tool guide provides instructions to migrate schemas from Oracle databases to Amazon RDS for MySQL or Amazon Aurora MySQL using the AAWS SCT, including data type mappings, compatibility considerations, and best practices.
- [Oracle to Amazon RDS for Oracle](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Oracle.ToRDSOracle.html): This section of the AWS Schema Conversion Tool guide provides instructions to migrate data from Oracle Database to Amazon RDS for Oracle using the AWS SCT.
- [PostgreSQL databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.PostgreSQL.html): This section of the AWS Schema Conversion Tool provides instructions to connect the AWS Schema Conversion Tool (SCT) to PostgreSQL databases, including configuring the connection settings, testing the connection, and creating a new conversion project in the SCT user interface.
- [SAP databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SAP.html): This section of the AWS Schema Conversion Tool guide provides instructions to connect to SAP databases, including configuring the connection settings, testing the connection, and creating a new conversion project in the AWS SCT user interface.

### [SQL Server databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.html)

This section of the AWS Schema Conversion Tool guide provides information on using the AWS Schema Conversion Tool to migrate SQL Server databases to the AWS Cloud.

- [SQL Server to MySQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.ToMySQL.html): This section of the AWS Schema Conversion Tool guide Provides instructions to migrate data from Microsoft SQL Server to MySQL using the AWS SCT.

### [SQL Server to PostgreSQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.ToPostgreSQL.html)

This section of the AWS Schema Conversion Tool guide provides instructions to migrate data from Microsoft SQL Server to PostgreSQL using the AWS SCT.

- [Emulating SQL Server Agent in PostgreSQL with an extension pack](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.ToPostgreSQL.ExtensionPack.Agent.html): Use an AWS Schema Conversion Tool extension pack to emulate SQL Server Agent in PostgreSQL.
- [Emulating SQL Server Database Mail in PostgreSQL with an extension pack](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.ToPostgreSQL.ExtensionPack.Mail.html): Use an AWS Schema Conversion Tool extension pack to emulate SQL Server Database Mail in PostgreSQL.
- [SQL Server to Amazon RDS SQL Server](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServer.ToRDSSQLServer.html): This section of the AWS Schema Conversion Tool guide provides instructions to migrate data from Microsoft SQL Server to Amazon RDS for SQL Server using AWS SCT.

### [Data warehouses](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source-Data-Warehouses.html)

This section of the AWS Schema Conversion Tool guide provides information on using the AWS Schema Conversion Tool to migrate data from various source data warehouses to AWS.

- [Amazon Redshift](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Redshift.html): This section of the AWS Schema Conversion Tool guide provides instrictions to migrate data from Amazon Redshift data warehouses to other AWS database services using AWS SCT.
- [Azure Synapse Analytics as a source](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.AzureSynapse.html): This section of the guide AWS Schema Conversion Tool provides instructions to migrate data from Azure Synapse Analytics data warehouses to other AWS database services using AWS SCT.
- [BigQuery as a source](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.BigQuery.html): This section of the AWS Schema Conversion Tool guide provides instructions to migrate data from Google BigQuery data warehouses to other AWS database services using AWS SCT.
- [Greenplum databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Greenplum.html): This section of the AWS Schema Conversion Tool guide provides instructions on how to convert Greenplum database schema and migrate data to AWS database serviceswith AWS SCT.
- [Netezza databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Netezza.html): This section of the AWS Schema Conversion Tool guide provides instruction to convert the schema and migrate Netezza databases to Amazon Redshift using AWS SCT.
- [Oracle data warehouse](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.OracleDW.html): This section of AWS Schema Conversion Tool the provides instructions to connect Oracle data warehouse databases to to Amazon Redshift or Amazon Redshift and AWS Glue using AWS SCT.
- [Snowflake](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Snowflake.html): This section of the AWS SCT guide provides instructions to connect AWS SCT to a Snowflake data warehouse, enabling you to migrate your database schema and data.
- [SQL Server Data Warehouses](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.SQLServerDW.html): This section of the AWS SCT guide provides instructions to connect the AWS Schema Conversion Tool to a SQL Server data warehouse, enabling you to migrate your database schema and data.
- [Teradata databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Teradata.html): This section of the AWS SCT guide shows you how to connect the AWS Schema Conversion Tool to Teradata databases, an enterprise-class massively parallel processing (MPP) data warehouse platform, enabling schema conversion and data migration to AWS database services.
- [Vertica databases](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Source.Vertica.html): This section of the AWS SCT guide shows you how to connect the AWS Schema Conversion Tool to Vertica databases, an analytics data warehouse platform using a massively parallel processing (MPP) architecture, enabling schema conversion and data migration to AWS database services.


## [Data type mapping](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Mapping.html)

- [New data type mapping](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Mapping.New.html): This section of the AWS SCT user guide shows you how to map new or custom data types during the schema conversion process, allowing you to extend the tool's capabilities and ensure compatibility with user-defined or proprietary data types when migrating databases.
- [Editing data type mappings](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Mapping.Edit.html): This section of the AWS SCT user guide shows you how to edit and modify the data type mappings used during the schema conversion process, allowing you to customize the mappings based on your specific database migration requirements and ensure accurate data type translations.
- [Virtual target mapping](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Mapping.VirtualTargets.html): This section of the AWS SCT user guide shows you how to map data types to virtual targets, which are intermediate or generic representations of data types used during the schema conversion process, providing greater flexibility and compatibility when migrating databases across different platforms.
- [Data type mapping limitations](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Mapping.Limitations.html): This section of the AWS SCT user guide shows you the limitations and potential issues related to data type mapping during the schema conversion process, including unsupported data types, compatibility problems, and scenarios that may lead to data loss or inaccurate conversions.


## [Reports](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-Reports.html)

### [Assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.html)

This section of the AWS Schema Conversion Tool user guide shows you how to use the assessment report feature to analyze the compatibility of your source database schema with the target AWS database service, identifying potential issues, data type mappings, and providing insights to help plan and evaluate the readiness for database migration.

- [Create assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Create.html): This section of the AWS Schema Conversion Tool user guide shows you how to create an assessment report for your data migration project.

### [Viewing assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.View.html)

This section of the AWS Schema Conversion Tool user guide shows you how to view an assessment report for your data migration project.

- [Report summary](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Summary.html): The Summary tab displays the summary information from the database migration assessment report.
- [Action items](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.ActionItems.html): The assessment report view also includes an Action Items tab.
- [Warning message](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.WarningMessage.html): To assess the complexity of converting to another database engine, AWS SCT requires access to objects in your source database.
- [Saving the assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Save.html): This section of the AWS Schema Conversion Tool user guide shows you how to save an assessment report for your data migration project.
- [Configuring an assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Configure.html): This section of the AWS Schema Conversion Tool user guide shows you how to configure an assessment report for your data migration project.
- [Multiserver assessment report](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_AssessmentReport.Multiserver.html): This section of the AWS Schema Conversion Tool user guide shows you how to create a multi-server assessment report for your data migration project.


## [Converting schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.html)

- [Applying migration rules](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.MigrationRules.html): This section of the AWS Schema Conversion Tool user guide shows you how to apply migration rules to customize and configure the schema conversion process, including mapping data types, transforming data structures, ensuring compatibility between source and target schemas, and making other necessary adjustments to the conversion process.
- [Converting schemas manually](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.Convert.html): This section of the AWS Schema Conversion Tool user guide shows you how to initiate and perform the schema conversion process, including selecting the source and target databases, configuring the conversion settings, applying necessary data transformations and mappings, validating the output, and generating the final converted schema for the target database.
- [Manually converting schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.Manual.html): This section of the AWS Schema Conversion Tool user guide shows you how to shows you how to manually convert schemas using the built-in schema editor, including mapping data types, applying custom transformations, modifying the source and target schemas, validating the converted output, and making any necessary adjustments or customizations to the conversion process.
- [Updating and refreshing schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.UpdateRefresh.html): This section of the AWS Schema Conversion Tooluser guide shows you how to update and refresh the source and target schemas to reflect any changes or modifications made to the underlying databases, ensuring that the conversion process stays synchronized and up-to-date with the latest data structures and schema definitions.
- [Saving and applying converted schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.SaveAndApply.html): This section of the AWS Schema Conversion Tool user guide shows you how to save and apply your converted schemas to the target database, including options for saving the converted schema as SQL scripts for further modifications, applying the converted schema directly to an Amazon RDS instance, and understanding the extension pack schema that is automatically added during the schema migration process.
- [Comparing schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.SchemaCompare.html): This section of the AWS Schema Conversion Tool user guide shows you how to compare source and target schemas for your data migration project.
- [Viewing related transformed objects](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.RelatedObjects.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert related objects during the schema conversion process for your data migration project.


## [Converting data warehouse schemas](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.DW.html)

- [Converting Amazon Redshift data](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.DW.RedshiftOpt.html): This section of the AWS Schema Conversion Tool User Guide shows you how to convert data from Amazon Redshift data warehouse.


## [Converting Data Using ETL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-etl.html)

- [ETL processes](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-aws-glue-ui-process.html): This section of the AWS Schema Conversion Tool user guide shows how to convert data from one format AWS Glue in the AWS Schema Conversion Tool.
- [ETL processes using Python](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-aws-glue-api-process.html): This section of the AWS Schema Conversion Tool user shows how to convert data to AWS Glue using Python API for AWS Glue.
- [Informatica ETL scripts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-informatica.html): This section of the AWS Schema Conversion Tool guide shows how to convert Informatica ETL scripts in AWS SCT.
- [SSIS packages](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-aws-glue-ssis.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert SQL Server Integration Services (SSIS) packages to AWS Glue in AWS SCT.
- [SSIS to AWS Glue Studio](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-ssis-glue-studio.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert data from SQL Server Integration Services (SSIS) to AWS Glue Studio with AWS SCT.
- [Teradata BTEQ scripts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-bteq-rsql.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert Bteq scripts from Teradata databases to Amazon Redshift RSQL with AWS Schema Conversion Tool.
- [Shell scripts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-shell-rsql.html): This section of the AWS Schema Conversion Tooll user guide shows you how to convert shell scripts with embedded Teradata BTEQ commands to Amazon Redshift RSQL with AWS SCT.
- [FastExport scripts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-fastexport-rsql.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert Fast/Export scripts to Amazon Redshift RSQL with AWS SCT.
- [FastLoad scripts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-fastload-rsql.html): This section of the AWS Schema Conversion Tool user guides shows how to convert Teradata FastLoad job scripts to Amazon Redshift RSQL withj AWS SCT.
- [MultiLoad scripts](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-converting-multiload-rsql.html): This section of the AWS Schema Conversion Tool user guide shows how to convert MultiLoad job scripts to Amazon Redshift RSQL with AWS SCT.


## [Migrating big data frameworks](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP-migrating-big-data.html)

- [Migrating Hadoop workloads](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/big-data-hadoop.html): This section of the AWS Schema Conversion Tool user guide shows you how to migrate on-premises Hadoop workloads and the Hadoop ecosystem to Amazon EMR with AWS SCT .
- [Converting Oozie workflows;](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/big-data-oozie.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert Apache Oozie workflows from on-premises Hadoop environments to AWS Step Functions with AWS SCT.


## [Converting application SQL](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.html)

- [SQL code](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.Generic.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert SQL code in your applications with the AWS SCT.
- [SQL code in C# applications](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.Csharp.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert SQL code in C# applications with the AWS SCT.
- [SQL code in C++](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.Cplusplus.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert SQL code in C++ applications with AWS SCT.
- [SQL code in Java](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.Java.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert QL code in Java applications to work with AWS database services with AWS SCT.
- [SQL code in Pro*C](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Converting.App.ProC.html): This section of the AWS Schema Conversion Tool user guide shows you how to convert SQL code in Pro*C applications to work with AWS database services using AWS SCT.
