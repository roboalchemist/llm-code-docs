# Source: https://dbeaver.com/docs/dbeaver/Database-driver-IBM-Db2/

Expand all

  * [ Getting started  ](..)

Getting started

    * [ First steps  ](../Getting-started/)
    * [ Installation  ](../Installation/)
    * [ Application window overview  ](../Application-Window-Overview/)
    * [ Basic operations  ](../Basic-operations/)
  * DBeaver configuration  DBeaver configuration 
    * [ User interface  ](../User-Interface-Themes/)
    * [ Interface language  ](../UI-Language/)
    * [ Accessibility  ](../Accessibility-Guide/)
    * [ Toolbar customization  ](../Toolbar-Customization/)
    * [ Database object editor  ](../Database-Object-Editor/)
    * [ Reset UI settings  ](../Reset-UI-settings/)
    * [ Shortcuts  ](../Shortcuts/)
  * Security  Security 
    * [ Security in DBeaver PRO  ](../Security-in-DBeaver-PRO/)
    * Password secure storage  Password secure storage 
      * [ Secure storage  ](../Security/)
      * [ Master password  ](../Managing-Master-Password/)
      * [ Automation (console) security  ](../Automation-Security/)
      * [ Integrated security  ](../Integrated-Security/)
    * [ Secret Management  ](../Secret-Providers/)
  * Configure connection  Configure connection 
    * Connection settings  Connection settings 
      * [ Create connection  ](../Create-Connection/)
      * [ Edit connection  ](../Edit-Connection/)
      * [ Invalidate and reconnect  ](../Invalidate-and-Reconnect-to-Database/)
      * [ Disconnect from database  ](../Disconnect-from-Database/)
      * [ Change current user password  ](../Change-current-user-password/)
      * [ Shell commands  ](../Working-with-Shell-Commands-in-DBeaver/)
      * [ Initialization settings  ](../Configure-Connection-Initialization-Settings/)
      * [ Security restrictions for database connection  ](../Managing-security-restrictions-for-database-connection/)
      * [ Connection types  ](../Connection-Types/)
      * [ Local client configuration  ](../Local-Client-Configuration/)
      * [ Multiple datasource connections  ](../Separate-Connections/)
    * Network configuration  Network configuration 
      * [ Network configuration  ](../Network-configuration/)
      * Connection network options  Connection network options 
        * [ SSH configuration  ](../SSH-Configuration/)
        * SSL  SSL 
          * [ SSL configuration  ](../SSL-Configuration/)
          * Truststore management  Truststore management 
            * [ Manage certificates  ](../Managing-Truststore-Settings/)
            * [ Import custom certificates  ](../Import-SSL-Certificates/)
          * [ Oracle SSL configuration  ](../SSL-Configuration-Oracle/)
        * Proxy  Proxy 
          * [ Proxy configuration  ](../Proxy-configuration/)
          * [ Proxy configuration with system files  ](../Proxy-configuration-with-system-files/)
        * [ Kubernetes configuration  ](../Kubernetes-configuration/)
        * [ AWS SSM configuration  ](../AWS-SSM-Configuration/)
      * [ Network profiles  ](../Network-profiles/)
    * Transaction mode  Transaction mode 
      * [ Transaction log  ](../Transaction-Log/)
      * [ Pending transactions  ](../Pending-Transactions/)
      * [ Auto and manual commit modes  ](../Auto-and-Manual-Commit-Modes/)
    * Database authentication models  Database authentication models 
      * [ Database native  ](../Authentication-Database-Native/)
      * [ DBeaver profile  ](../Authentication-DBeaver-profile/)
      * [ Microsoft Entra ID  ](../Authentication-Microsoft-Entra-ID/)
      * [ Kerberos  ](../Kerberos-Authentication/)
    * Driver settings  Driver settings 
      * [ Driver manager  ](../Driver-Manager/)
      * [ ODBC & JDBC driver  ](../ODBC-JDBC-Driver/)
      * [ File-based driver properties  ](../File-based-driver-properties/)
      * [ How to add additional artifacts to the driver  ](../How-to-add-additional-artifacts-to-the-driver/)
      * [ JDBC time zones  ](../JDBC-Time-Zones/)
      * [ JDBC tracing  ](../JDBC-Tracing/)
      * [ Deprecated legacy ODBC driver  ](../Deprecated-legacy-ODBC-driver/)
  * Databases support  Databases support 
    * [ Database drivers  ](../Database-drivers/)
    * Classic  Classic 
      * [ Apache Hive  ](../Apache-Hive/)
      * [ Cassandra  ](../Cassandra/)
      * [ ClickHouse  ](../Clickhouse/)
      * [ Couchbase  ](../Couchbase/)
      * IBM Db2  [ IBM Db2  ](./) Table of contents 
        * Setting Up 
          * Db2 connection settings 
            * Connection details 
            * Trace Settings 
        * Db2 driver properties 
        * ODBC and JDBC Driver Configuration 
        * Secure Connection Configurations 
          * Secure Storage with Secret Providers 
        * Powering Db2 with DBeaver 
          * Db2 database objects 
          * Db2 features in DBeaver 
      * [ Greenplum  ](../Database-driver-Greenplum/)
      * [ InfluxDB  ](../InfluxDB/)
      * [ Microsoft SQL Server  ](../Database-driver-Microsoft-SQL-Server/)
      * [ MariaDB  ](../Database-driver-MariaDB/)
      * MongoDB  MongoDB 
        * [ MongoDB  ](../MongoDB/)
        * [ MongoDB authentication  ](../Authentication-MongoDB/)
      * MySQL  MySQL 
        * [ MySQL  ](../Database-driver-MySQL/)
        * [ Two-factor authentication  ](../Authentication-MySQL-Two-factor/)
      * [ Netezza  ](../Database-driver-Netezza/)
      * Oracle  Oracle 
        * [ Oracle  ](../Oracle/)
        * [ Oracle authentication  ](../Connecting-to-Oracle-databases/)
        * [ JDBC OCI driver  ](../Connecting-to-Oracle-Database-using-JDBC-OCI-driver/)
      * PostgreSQL  PostgreSQL 
        * [ PostgreSQL  ](../Database-driver-PostgreSQL/)
        * [ PgPass authentication  ](../Authentication-PostgreSQL-Pgpass/)
        * [ SSPI (Windows SSO)  ](../Authentication-PostgreSQL-SSPI/)
      * [ Redis  ](../Redis/)
      * Salesforce  Salesforce 
        * [ Salesforce  ](../Database-driver-Salesforce/)
        * [ Salesforce authentication  ](../Authentication-Salesforce/)
      * Teradata  Teradata 
        * [ Teradata  ](../Database-driver-Teradata/)
        * [ LDAP authentication in Teradata  ](../Authentication-LDAP-Mechanism/)
      * [ Trino  ](../Database-driver-Trino/)
      * [ Yellowbrick  ](../Database-driver-Yellowbrick/)
    * Cloud  Cloud 
      * AWS  AWS 
        * [ Athena  ](../Database-driver-Amazon-Athena/)
        * [ Aurora DSQL  ](../Database-driver-Aurora-DSQL/)
        * [ DocumentDB  ](../AWS-DocumentDB/)
        * [ DynamoDB  ](../AWS-DynamoDB/)
        * [ Keyspaces  ](../AWS-Keyspaces/)
        * [ Neptune  ](../Database-driver-Neptune/)
        * [ Redshift  ](../Database-driver-Amazon-Redshift/)
        * [ Timestream  ](../Database-driver-Amazon-Timestream/)
      * Azure  Azure 
        * [ Cosmos DB  ](../Database-driver-CosmosDB/)
        * [ Cosmos DB for NoSQL  ](../Database-driver-Azure-CosmosDB-for-NoSQL/)
      * Google  Google 
        * [ AlloyDB for PostgreSQL  ](../Database-driver-AlloyDB-for-PostgreSQL/)
        * [ BigQuery  ](../Database-driver-BigQuery/)
        * [ Bigtable  ](../Google-Bigtable/)
        * [ Cloud SQL for MySQL  ](../Database-driver-MySQL-on-Google-Cloud/)
        * [ Cloud SQL for PostgreSQL  ](../Database-driver-PostgreSQL-on-Google-Cloud/)
        * [ Cloud SQL for SQL Server  ](../Database-driver-Microsoft-SQL-Server-on-Google-Cloud/)
        * [ Firestore  ](../Database-driver-Firestore/)
        * [ Spanner  ](../Database-driver-Google-Cloud-Spanner/)
      * Databricks  Databricks 
        * [ Databricks  ](../Database-driver-Databricks/)
        * [ Databricks authentication  ](../Authentication-Databricks/)
      * Snowflake  Snowflake 
        * [ Snowflake  ](../Snowflake/)
        * [ Snowflake authentication  ](../Authentication-Snowflake/)
    * Embedded  Embedded 
      * [ SQLite  ](../Database-driver-SQLite/)
    * File drivers  File drivers 
      * [ Multi source  ](../Database-driver-Files-MultiSource/)
      * [ CSV  ](../Database-driver-CSV/)
      * [ JSON  ](../Database-driver-JSON/)
      * [ Parquet  ](../Database-driver-Parquet/)
      * [ XLSX  ](../Database-driver-XLSX/)
      * [ XML  ](../Database-driver-XML/)
    * Graph  Graph 
      * [ Neo4j  ](../Database-driver-Neo4j/)
  * Navigation  Navigation 
    * Database Navigator  Database Navigator 
      * [ Database Navigator  ](../Database-Navigator/)
      * [ Simple and advanced view  ](../Simple-and-Advanced-View/)
      * [ Configuring filters  ](../Configure-Filters/)
      * [ Filter database objects  ](../Filter-Database-Objects/)
      * [ Bookmarks  ](../Bookmarks/)
    * Projects  Projects 
      * [ Projects  ](../Projects/)
      * [ Projects view  ](../Projects-View/)
      * [ Project security  ](../Project-security/)
      * [ Project explorer  ](../Project-Explorer/)
    * Search  Search 
      * [ Search  ](../Search-Tool/)
      * [ Data search  ](../Data-Search/)
      * [ Full-text search database  ](../DB-Full-Text-Search/)
      * [ Metadata search  ](../DB-Metadata-Search/)
      * [ File search  ](../File-Search/)
  * [ Properties Editor  ](../Properties-Editor/)
  * Data Editor  Data Editor 
    * [ Data Editor  ](../Data-Editor/)
    * Viewing and editing data  Viewing and editing data 
      * [ Data view and format  ](../Data-View-and-Format/)
      * [ Data filters  ](../Data-Filters/)
      * [ Data viewing and editing  ](../Data-Viewing-and-Editing/)
      * [ Data refresh  ](../Data-Refresh/)
      * [ Result set navigation  ](../Navigation/)
      * Panels  Panels 
        * [ Panels  ](../Panels/)
        * [ Value Panel  ](../Value-Panel/)
        * [ References Panel  ](../References-Panel/)
        * [ Metadata Panel  ](../Metadata-Panel/)
        * [ Grouping Panel  ](../Grouping-Panel/)
        * [ Calc Panel  ](../Calc-Panel/)
        * [ Result details Panel  ](../Result-Details-Panel/)
        * [ Query trace Panel  ](../Query-Trace-Panel/)
      * [ Managing charts  ](../Managing-Charts/)
      * [ Mock data generation  ](../Mock-Data-Generation-in-DBeaver/)
      * [ Dashboards  ](../Dashboards/)
    * [ XML and JSON data  ](../Working-with-XML-and-JSON/)
    * [ Dictionary data  ](../Working-with-Dictionary-Data/)
    * [ Spatial GIS data  ](../Working-with-Spatial-GIS-data/)
    * Virtual entities  Virtual entities 
      * [ Virtual columns  ](../Virtual-column-expressions/)
      * [ Virtual keys  ](../Virtual-Keys/)
    * [ Data Editor preferences  ](../Data-Editor-preferences/)
    * [ Data format preferences  ](../Managing-Data-Formats/)
  * SQL Editor  SQL Editor 
    * [ SQL Editor  ](../SQL-Editor/)
    * [ Visual query builder  ](../Visual-Query-Builder/)
    * Query execution  Query execution 
      * [ SQL execution  ](../SQL-Execution/)
      * [ Query execution plan  ](../Query-Execution-Plan/)
      * [ Script management  ](../Script-Management/)
    * Query development and assistance  Query development and assistance 
      * [ SQL Assist and Auto Complete  ](../SQL-Assist-and-Auto-Complete/)
      * [ SQL templates  ](../SQL-Templates/)
      * [ SQL query formatter  ](../SQL-Formatting/)
      * [ Variables panel  ](../Variables-panel/)
      * [ Spelling  ](../Spelling/)
    * [ SQL generation  ](../SQL-Generation/)
    * [ SQL terminal  ](../SQL-Terminal/)
    * Client side commands  Client side commands 
      * [ Client side scripting  ](../Client-Side-Scripting/)
      * [ Export command  ](../Export-Command/)
    * [ Query manager  ](../Query-Manager/)
    * [ SQL code Editor  ](../SQL-Code-Editor/)
    * [ SQL Plus script execution  ](../SQL-Plus-Script-Execution/)
    * [ PostgreSQL Arrays  ](../PostgreSQL-Arrays/)
    * [ PostgreSQL Extensions  ](../PostgreSQL-Extensions/)
  * Entity relation diagrams  Entity relation diagrams 
    * [ ER Diagrams  ](../ER-Diagrams/)
    * [ Database structure diagrams  ](../Database-Structure-Diagrams/)
    * [ Custom diagrams  ](../Custom-Diagrams/)
    * [ Edit mode for diagrams  ](../Edit-mode/)
  * Cloud services  Cloud services 
    * Cloud explorer  Cloud explorer 
      * [ Cloud explorer  ](../Cloud-Explorer/)
      * [ AWS cloud explorer  ](../AWS-Cloud-Explorer/)
      * [ Azure cloud explorer  ](../Azure-Cloud-Explorer/)
      * [ Google cloud explorer  ](../Google-Cloud-Explorer/)
    * [ Cloud storage  ](../Cloud-Storage/)
    * Cloud connection settings  Cloud connection settings 
      * AWS  AWS 
        * [ AWS permissions  ](../AWS-Permissions/)
        * [ AWS SSO  ](../AWS-SSO/)
        * [ AWS credentials  ](../AWS-Credentials/)
      * Azure  Azure 
        * [ Azure permissions  ](../Azure-Permissions/)
      * Google Cloud  Google Cloud 
        * [ Google Cloud SSO  ](../GCP-SSO/)
        * [ Google Cloud credentials  ](../GCP-Credentials/)
  * AI  AI 
    * [ AI Assistant  ](../AI-Smart-Assistance/)
    * [ Data privacy  ](../AI-Assistance-and-Data-Privacy/)
    * Features  Features 
      * AI chat  AI chat 
        * [ AI chat  ](../AI-chat/)
        * [ Speech recognition  ](../AI-speech-recognition/)
      * AI functions  AI functions 
        * [ AI functions  ](../AI-Functions/)
        * [ Data transfer actions  ](../Data-Transfer-Actions/)
        * [ Advanced metadata actions  ](../Advanced-Metadata-Read-Actions/)
        * [ View and editor actions  ](../View-and-Editor-Actions/)
      * Work with SQL  Work with SQL 
        * [ Query suggestion  ](../AI-query-suggestion/)
        * [ Explain query  ](../AI-query-explanation/)
        * [ Fix SQL errors  ](../AI-error-explanation/)
        * [ AI command  ](../AI-command/)
      * Work with objects  Work with objects 
        * [ Describe object with AI  ](../AI-smart-metadata-description/)
    * Tutorials  Tutorials 
      * [ Quick start with AI  ](../Quick-start-with-AI-Assistance/)
    * Settings  Settings 
      * [ AI Assistant settings  ](../AI-Assistance-settings/)
      * Providers  Providers 
        * [ OpenAI  ](../AI-integration-with-OpenAI/)
        * [ GitHub Copilot  ](../AI-integration-with-GitHub-Copilot/)
        * [ Azure OpenAI  ](../AI-integration-with-Azure-OpenAI/)
        * [ Google Gemini  ](../AI-integration-with-Google-Gemini/)
        * [ Ollama  ](../AI-integration-with-Ollama/)
        * [ Anthropic Claude  ](../AI-integration-with-Anthropic-Claude/)
        * [ Amazon Bedrock  ](../AI-integration-with-Amazon-Bedrock/)
      * [ Disable AI Assistant  ](../Disable-AI-assistance/)
  * Data transfer and schema compare  Data transfer and schema compare 
    * Data transfer  Data transfer 
      * [ Data transfer  ](../Data-transfer/)
      * [ Data import  ](../Data-import/)
      * [ Data import and replace  ](../Data-Import-and-Replace/)
      * [ Data export  ](../Data-export/)
      * [ Data transfer external storage  ](../Data-transfer-external-storage/)
      * [ Data migration  ](../Data-migration/)
      * [ Data transfer via email  ](../Data-transfer-email/)
    * [ Data compare  ](../Data-compare/)
    * [ Backup and restore  ](../Backup-Restore/)
    * Schema compare  Schema compare 
      * [ Schema compare  ](../Schema-compare/)
      * [ Liquibase support  ](../Using-Liquibase-in-DBeaver/)
  * Tasks  Tasks 
    * [ Task management  ](../Task-Management/)
    * [ Task scheduler  ](../Task-Scheduler/)
    * [ Composite tasks  ](../Composite-Tasks/)
  * Integrated tools  Integrated tools 
    * [ GIT integration  ](../Project-team-work/)
    * [ Tableau integration  ](../Tableau-integration-in-DBeaver/)
    * [ Database debugger (PostgreSQL)  ](../PGDebugger/)
    * [ Session Manager  ](../Session-Manager-Guide/)
    * [ Lock Manager  ](../Lock-Manager/)
    * [ Eclipse extensions  ](../Eclipse-extensions/)
  * Tutorials  Tutorials 
    * Table Creation  Table Creation 
      * [ New table creation  ](../New-Table-Creation/)
      * [ Incorporating triggers  ](../Incorporating-Triggers/)
      * [ Creating columns  ](../Creating-columns/)
      * [ Creating indexes  ](../Creating-Indexes/)
      * [ Implementing constraints  ](../Implementing-Constraints/)
      * [ Utilizing foreign keys  ](../Utilizing-Foreign-Keys/)
    * [ Sample database  ](../Sample-Database/)
    * [ Database partitions  ](../How-to-work-with-database-Partitions/)
    * [ Import connections from external tools  ](../How-to-import-Connections-from-External-Tools/)
  * Administration  Administration 
    * Admin preferences  Admin preferences 
      * [ Admin manage preferences  ](../Admin-Manage-Preferences/)
      * [ Admin manage drivers  ](../Admin-Manage-Drivers/)
      * [ Admin preference restrictions  ](../Admin-Preference-Restrictions/)
      * [ Admin variables  ](../Admin-Variables/)
    * General configuration  General configuration 
      * [ Configuration files  ](../Configuration-files-in-DBeaver/)
      * [ Pre-configured database connections  ](../Admin-Manage-Connections/)
      * [ Pre-configured variables  ](../Pre-configured-Variables/)
      * [ How to set a variable if dbeaver.ini is read only  ](../How-to-set-a-variable-if-dbeaver-ini-is-read-only/)
      * [ Command line  ](../Command-Line/)
      * [ Error log  ](../Log-files/)
      * [ Background tasks  ](../Background-Tasks/)
      * [ Workspace location  ](../Workspace-Location/)
      * [ Resetting your workspace  ](../Reset-workspace/)
      * [ Importing CA certificates from your local Java into DBeaver  ](../Importing-CA-certificates-from-your-local-Java-into-DBeaver/)
    * Troubleshooting  Troubleshooting 
      * [ Troubleshooting system issues  ](../Troubleshooting-system-issues/)
      * [ Troubleshooting task scheduler issues  ](../Troubleshooting-task-scheduler-issues/)
      * [ Making a thread dump  ](../Making-a-thread-dump/)
      * [ Posting issues  ](../Posting-issues/)
    * [ Windows silent install  ](../Windows-Silent-Install/)
    * [ Snap installation  ](../Snap-installation/)
  * Licenses  Licenses 
    * [ Import license  ](../How-to-Import-License/)
    * [ Update license  ](../How-to-Update-License/)
    * [ Reassign license  ](../How-to-Reassign-License/)
    * [ License administration  ](../License-Administration/)
    * License types  License types 
      * [ License types  ](../Differences-between-license-types/)
      * [ Early Access Program (EAP) license  ](../Early-Access-Program-license/)
  * About DBeaver  About DBeaver 
    * Editions  Editions 
      * [ Enterprise edition  ](../Enterprise-Edition/)
      * [ Lite edition  ](../Lite-Edition/)
      * [ Ultimate edition  ](../Ultimate-Edition/)
    * [ Release cycles  ](../DBeaver-release-cycles/)
    * [ Statistics collection  ](../Statistics-Collection/)
    * [ Customer technical support  ](../Customer-technical-support-information/)
  * [ FAQ  ](../FAQ/)

Table of contents

  * Setting Up 
    * Db2 connection settings 
      * Connection details 
      * Trace Settings 
  * Db2 driver properties 
  * ODBC and JDBC Driver Configuration 
  * Secure Connection Configurations 
    * Secure Storage with Secret Providers 
  * Powering Db2 with DBeaver 
    * Db2 database objects 
    * Db2 features in DBeaver 

  1. [DBeaver](/docs/dbeaver)
  2. [Databases support](/docs/dbeaver/Database-drivers)
  3. Classic

# IBM Db2

This guide provides instructions on how to set up and use IBM DB2 with
DBeaver.

Before you start, you must create a connection in DBeaver and select IBM DB2.
If you have not done this, please refer to our [Database
Connection](../Create-Connection/) article.

DBeaver interacts with the IBM DB2 server using a specific driver, it supports
all versions of IBM DB2, but the correct driver must be selected: use **Db2
for LUW (Old 8.x)** for versions below 8.x and **Db2 for LUW** for newer
versions. DBeaver also supports various IBM DB2 databases such as **Db2 for
IBM i** , and **Db2 for z/OS**. You must select the appropriate driver in the
**Connect to a database** window for these databases.

![](../images/database/db2/db2-drivers.png)

## Setting Up¶

This section provides an overview of DBeaver's settings for establishing a
direct connection and the configuration of secure connections using SSH,
proxies, SSL, and the setup of ODBC/JDBC drivers for Db2.

Warning

This database may charge for metadata queries, such as listing tables or
reading schema information. These queries can trigger compute usage or per-
request billing. You can turn off metadata queries to avoid extra costs. For
details, see [Disable metadata queries](../Data-Editor/#disable-metadata-
queries).

### Db2 connection settings¶

In this subsection, we will outline the settings for establishing a direct
connection to a Db2 database using DBeaver. Correctly configuring your
connection ensures seamless interaction between DBeaver and your Db2 database.

The page of the connection settings requires you to fill in specific fields to
establish the initial connection.

![](../images/database/db2/db2-connection-main.png)

Field | Description  
---|---  
**Connect by (Host/URL)** | Choose whether you want to connect using a host or a URL.  
**Driver Type** | Select the appropriate driver for your Db2 database.  
**URL** | If you are connecting via URL, enter the URL of your Db2 database here. This field is hidden if you are connecting via the host.  
**Host** | If you are connecting via host, enter the host address of your Db2 database here.  
**Database** | Enter the name of the Db2 database you want to connect to.  
**Port** | Enter the port number for your Db2 database.  
**Authentication** | Choose the type of authentication you want to use for the connection. For detailed guides on authentication types, please refer to the following articles:  
  
\- [Native Database Authentication](../Authentication-Database-Native/)  
\- [DBeaver Profile Authentication](../Authentication-DBeaver-profile/)
![](../images/commercial.png)  
\- [Kerberos Authentication](../Kerberos-Authentication/) (only supported with
**Db2 for LUW** driver version 11) ![](../images/commercial.png)  
**Connection Details** | Provide additional connection details if necessary.  
**Driver Name** | This field will be auto-filled based on your selected driver type.  
**Driver Settings** | If there are any specific driver settings, configure them here.  
  
#### Connection details¶

The **Connection Details** section in DBeaver allows for further customization
of your Db2 connection. This includes options for adjusting the **Navigator
View** , setting up **Security measures** , applying **Filters** , configuring
**Connection Initialization** settings, and setting up **Shell Commands**.
Each of these settings can significantly impact your database operations and
workflow. For detailed guides on these settings, please refer to the following
articles:

  * [Connection Details Configuration](../Create-Connection/#connection-details)
  * [Database Navigator](../Database-Navigator/)
  * [Security Settings Guide](../Managing-security-restrictions-for-database-connection/)
  * [Filters Settings Guide](../Configure-Filters/)
  * [Connection Initialization Settings Guide](../Configure-Connection-Initialization-Settings/)
  * [Shell Commands Guide](../Working-with-Shell-Commands-in-DBeaver/)

#### Trace Settings¶

In DBeaver, the trace settings feature allows you to monitor and record
database operations in a detailed manner. To enable this feature, check the
**Enable trace** box. You will need to specify a file where the traced
information will be stored and formatted into a readable format.

The trace settings page allows you to configure various levels and settings to
tailor the tracing process according to your preferences.

![](../images/database/db2/db2-trace-settings.png)

Setting | Description  
---|---  
**Folder** /**File name** | Specify the directory and file name where the trace data will be stored. This file will contain detailed information about the operations performed in the database.  
**Append** | This option allows you to add information to an existing trace file, instead of creating a new file each time the trace is enabled.  
**Connection Calls** | Records calls related to database connections.  
**Result Set Calls** | Records calls pertaining to the result sets.  
**Connects** | Records information about database connects.  
**Result Set Metadata** | Records metadata information from the result sets.  
**Diagnostics** | Records diagnostic information about database operations.  
**XA Calls** | Records information on XA distributed transactions.  
**Statement Calls** | Records calls related to SQL statements.  
**Driver Configuration** | Records configuration details of the database driver.  
**DRDA Flows** | Records information on DRDA data flows.  
**Parameter Metadata** | Records metadata about SQL parameters.  
**SQL J** | Records information on SQL J operations.  
  
For more detailed information on these settings, please refer to the [IBM
documentation](https://www.ibm.com/docs/en/db2/11.5?topic=tools-traces).

## Db2 driver properties¶

The settings for Db2 **Driver properties** enable you to adjust the
performance of the Db2 JDBC and ODBC driver. These adjustments can influence
the efficiency, compatibility, and features of your Db2 database.

For a complete walkthrough on setting up Db2 JDBC and ODBC drivers properties,
you can refer to the official [Db2 JDBC
documentation](https://www.ibm.com/docs/en/db2/11.5?topic=SSEPGG_11.5.0/com.ibm.db2.luw.apdv.java.doc/src/tpc/imjcc_r0052607.htm)
and [Db2 ODBC documentation](https://www.ibm.com/docs/en/db2/11.5?topic=odbc-
cliodbc-configuration-keywords). These guides detail each driver's properties
and how they can be used to optimize Db2 database connections.

You can customize the Db2 driver in DBeaver via the **Edit Driver** page,
accessible by clicking on the **Driver Settings** button on the first page of
the driver settings. This page offers a range of settings that can influence
your Db2 database connections. For a comprehensive guide on these settings,
please refer to our [Driver manager](../Driver-Manager/) article.

## ODBC and JDBC Driver Configuration¶

DBeaver provides extensive capabilities for managing Db2 database connections
via ODBC/JDBC drivers. This functionality enables you to connect to your Db2
database using native ODBC drivers, offering an alternative when specific
DBeaver drivers are not available.

You can find a comprehensive, step-by-step guide on how to install the driver
manager, set up drivers, configure data sources, and establish connections in
DBeaver in our [ODBC Driver Configuration](../ODBC-JDBC-Driver/) article.

## Secure Connection Configurations¶

DBeaver supports secure connections to your Db2 database. Guidance on
configuring such connections, specifically **SSH** , **Proxy** , **SSL** ,
**Kubernetes** and **AWS SSM** connections, can be found in various referenced
articles. For a comprehensive understanding, please refer to these articles:

  * [**SSH Configuration**](../SSH-Configuration/)

  * [**Proxy Configuration**](../Proxy-configuration/)

  * [**Kubernetes Configuration**](../Kubernetes-configuration/)

  * [**AWS SSM**](../AWS-SSM-Configuration/)

### Secure Storage with Secret Providers¶

DBeaver supports various cloud-based secret providers to retrieve database
credentials. For detailed setup instructions, see [Secret
Providers](../Secret-Providers/).

## Powering Db2 with DBeaver¶

DBeaver provides a host of features designed for Db2 databases. This includes
the ability to view schemas, along with numerous unique capabilities aimed at
optimizing database operations.

### Db2 database objects¶

DBeaver lets you view and manipulate a wide range of Db2 database objects.
DBeaver has extensive support for various Db2 metadata types, allowing you to
interact with a wide variety of database objects, such as:

  * Schemas
    * Tables
      * Columns
      * Unique Constraints
      * Foreign Keys
      * Indexes
      * References
      * Check Constraints
      * Partitions
      * Periods
      * Triggers
      * Columns Masks
    * Views
    * MQTs
    * Indexes
    * Sequences
    * Aliases
    * Nicknames
    * Triggers
    * XML Schemas
    * Application Objects
      * Functions
      * Modules
      * Packages
      * Procedures
      * User Defined Types
  * Federation
    * Wrappers
    * Remote Servers
    * User Mappings
  * Global metadata
    * Types
    * Variables
    * XML Strings
  * Storage
    * Bufferpools
    * Tablespaces
    * Storage Groups
  * Administer
    * Session Manager
  * Security
    * Roles
    * Groups
    * Users

### Db2 features in DBeaver¶

DBeaver is not limited to typical SQL tasks. It also includes numerous unique
features specifically for DB2. Beyond regular SQL operations, DBeaver provides
a range of Db2-specific capabilities, such as:

Category | Feature  
---|---  
Schemas | Unique Constraints  
| Periods  
| Column Masks  
Views | MQTs  
Federation | Wrappers  
| Remote Servers  
Global Metadata | XML Strings  
Storage | Bufferpools  
| Tablespaces  
Security | Roles  
| Groups  
  
Additional features compatible with Db2, but not exclusive to it:

Category | Feature  
---|---  
Data Transfer | [Data Import](../Data-import/)  
| [Data Export](../Data-export/)  
Session Management | [Session Manager](../Session-Manager-Guide/)  
Lock Management | [Lock Manager](../Lock-Manager/)  
Schema Management | [Schema Compare](../Schema-compare/)  
Data Visualization | [GIS Guide](../Working-with-Spatial-GIS-data/)  
| [ERD Guide](../ER-Diagrams/)  
Query insights | [Disable metadata queries](../Data-Editor/#disable-metadata-queries)  
  
Back to top

