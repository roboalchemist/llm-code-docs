# Source: https://dbeaver.com/docs/dbeaver/Database-driver-SQLite/

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
      * [ IBM Db2  ](../Database-driver-IBM-Db2/)
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
      * SQLite  [ SQLite  ](./) Table of contents 
        * Setting Up 
          * SQLite connection configuration 
            * General SQLite connection settings 
            * SQLite Crypt connection settings 
            * SQLite extensions 
              * Extensions in Community Edition 
            * Remote database connection 
              * Synchronization 
          * Connection details 
          * SQLite driver properties 
          * ODBC and JDBC Driver Configuration 
          * Secure Connection Configurations 
          * Secure Storage with Secret Providers 
        * Powering SQLite with DBeaver 
          * SQLite database objects 
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
    * SQLite connection configuration 
      * General SQLite connection settings 
      * SQLite Crypt connection settings 
      * SQLite extensions 
        * Extensions in Community Edition 
      * Remote database connection 
        * Synchronization 
    * Connection details 
    * SQLite driver properties 
    * ODBC and JDBC Driver Configuration 
    * Secure Connection Configurations 
    * Secure Storage with Secret Providers 
  * Powering SQLite with DBeaver 
    * SQLite database objects 

  1. [DBeaver](/docs/dbeaver)
  2. [Databases support](/docs/dbeaver/Database-drivers)
  3. Embedded

# SQLite

This guide provides instructions on how to set up and use SQLite with DBeaver.

Before you start, you must create a connection in DBeaver and select SQLite.
If you have not done this, please refer to our [Database
Connection](../Create-Connection/) article.

DBeaver interacts with the SQLite server using a specific driver, supporting
all versions of SQLite. DBeaver also supports SQLite extensions such as SQLite
Crypt (Cipher). You can also create a sample database in DBeaver. See our
[Creating a Sample Database article](../Sample-Database/) for more
information. ![](../images/database/sqlite/sqlite-drivers.png)

## Setting Up¶

This section provides an overview of DBeaver's settings for establishing a
direct connection and the configuration of secure connections using SSH,
proxies, Kubernetes, and the setup of ODBC/JDBC drivers for SQLite.

### SQLite connection configuration¶

#### General SQLite connection settings¶

In this subsection, we will outline the settings for establishing a direct
connection to a SQLite database using DBeaver. Correctly configuring your
connection ensures seamless interaction between DBeaver and your SQLite
database.

The page of the connection settings requires you to fill in specific fields to
establish the initial connection.

![](../images/database/sqlite/sqlite-connection-main.png)

Field | Description  
---|---  
**Connect by (Host/URL)** | Choose whether you want to connect using a host or a URL.  
**Driver Type** | Select the appropriate driver for your SQLite database.  
**URL** | If you are connecting via URL, enter the URL of your SQLite database here. This field is disabled if you're connecting via the host.  
**Path** | Enter the path to the database file.  
**Database is remote** | If the SQLite database resides on a remote server, check this box. Reed more.  
**Connection Details** | Provide additional connection details if necessary.  
**Driver Name** | This field will be auto-filled based on your selected driver type.  
**Driver Settings** | If there are any specific driver settings, configure them here.  
  
#### SQLite Crypt connection settings¶

This subsection outlines the settings to establish a connection to encrypted
SQLite databases.

![](../images/database/sqlite/sqlite-crypt-connection-main.png)

Field | Description  
---|---  
**Path** | Enter the path to the database file.  
**Cipher** | Choose the encryption algorithm for your database. Available options include `AES 128`, `AES 256`, `ChaCha20`, `SQLCipher`, `SQLCipher v1`, `SQLCipher v2`, `SQLCipher v3`, `SQLCipher v4`, `RC4`, and `Custom` option. For more details, refer to the [SQLite Ciphers documentations](https://utelle.github.io/SQLite3MultipleCiphers/).  
**Password** | This field will be auto-filled based on your selected driver type.  
**Cipher parameters** | These parameters are read-only and change according to the chosen Cipher. You can customize them only if you select **Custom** in the Cipher field.  
  
#### SQLite extensions¶

DBeaver supports the addition of SQLite extensions to enhance database
functionality. Extensions can introduce new custom functions, collating
sequences, or virtual tables, which are useful for advanced data manipulation
or utilizing encryption algorithms not natively supported.

![](../images/database/sqlite/sqlite-extensions.png)

To import an SQLite extension, do the following:

  1. Locate the **Extensions** tab in your SQLite connection settings.

  2. Click on the **Add** button.

  3. Enter the path to the extension file you wish to import.

Note

Make sure the extension you are importing matches your operating system and
CPU architecture to ensure compatibility.

##### Extensions in Community Edition¶

To enable and load SQLite extensions in the Community Edition, follow these
steps:

  1. Set the `enable_load_extension` property to `true` in Driver properties tab.
  2. Execute `SELECT load_extension('extension-name.so')` either as a bootstrap query in the [Connection Initialization Settings](../Configure-Connection-Initialization-Settings/) or in the [SQL editor](../SQL-Editor/).

Note

You need to have a 64-bit version of the extension library.

#### Remote database connection¶

When connecting to a remote SQLite database in DBeaver:

  1. Specify a local path in the connection settings. This path should mirror the path on the remote server.

  2. Set up an [SSH](../SSH-Configuration/) tunnel.

##### Synchronization¶

To maintain consistency between your local SQLite database and the remote
server, follow these steps:

  1. Make local changes to your database.

  2. Save changes.

  3. Click the **Synchronize** button ![](../images/database/sqlite/Synchronize-button.png) in the main [toolbar](../Application-Window-Overview/#toolbar).

  4. A dialog will prompt you with two options:

![](../images/database/sqlite/SQLite-synchronization-window.png)

  * **Save local changes to server** : This will push your local changes to the server.
  * **Load remote changes from server** : This will pull the server's data to your local environment. After selecting this, refresh the result set to view updated data.

### Connection details¶

The **Connection Details** section in DBeaver allows you to customize your
experience while working with SQLite database. This includes options for
adjusting the **Navigator View** , setting up **Security measures** , applying
**Filters** , configuring **Connection Initialization** settings, and setting
up **Shell Commands**. Each of these settings can significantly impact your
database operations and workflow. For detailed guides on these settings,
please refer to the following articles:

  * [Connection Details Configuration](../Create-Connection/#connection-details)
  * [Database Navigator](../Database-Navigator/)
  * [Security Settings Guide](../Managing-security-restrictions-for-database-connection/)
  * [Filters Settings Guide](../Configure-Filters/)
  * [Connection Initialization Settings Guide](../Configure-Connection-Initialization-Settings/)
  * [Shell Commands Guide](../Working-with-Shell-Commands-in-DBeaver/)

### SQLite driver properties¶

The settings for SQLite **Driver properties** enable you to adjust the
performance of the SQLite JDBC and ODBC driver. These adjustments can
influence the efficiency, compatibility, and features of your SQLite database.

For a complete walkthrough on setting up SQLite JDBC and ODBC drivers
properties, you can refer to the official [SQLite JDBC
documentation](https://github.com/xerial/sqlite-jdbc) and [SQLite ODBC
documentation](http://www.ch-werner.de/sqliteodbc/html/index.html). These
guides detail each driver's properties and how they can be used to optimize
SQLite database connections.

You can customize the SQLite driver in DBeaver via the **Edit Driver** page,
accessible by clicking on the **Driver Settings** button on the first page of
the driver settings. This page offers a range of settings that can influence
your SQLite database connections. For a comprehensive guide on these settings,
please refer to our [Driver manager](../Driver-Manager/) article.

### ODBC and JDBC Driver Configuration¶

DBeaver provides extensive capabilities for managing SQLite database
connections via ODBC/JDBC drivers. This functionality enables you to connect
to your SQLite database using native ODBC drivers, offering an alternative
when specific DBeaver drivers are not available.

This process is similar across most databases that support ODBC/JDBC drivers.
For a comprehensive, step-by-step guide on how to install the driver manager,
set up drivers, configure data sources, and establish connections in DBeaver,
you can refer to our [ODBC Driver Configuration](../ODBC-JDBC-Driver/)
article.

### Secure Connection Configurations¶

DBeaver supports secure connections to your SQLite database. Guidance on
configuring such connections, specifically **SSH** , **Proxy** ,
**Kubernetes** and **AWS SSM** connections, can be found in various referenced
articles. For a comprehensive understanding, please refer to these articles:

  * [**SSH Configuration**](../SSH-Configuration/) ![](../images/commercial.png)

  * [**Proxy Configuration**](../Proxy-configuration/) ![](../images/commercial.png)

  * [**Kubernetes Configuration**](../Kubernetes-configuration/) ![](../images/commercial.png)

  * [**AWS SSM**](../AWS-SSM-Configuration/) ![](../images/commercial.png)

### Secure Storage with Secret Providers¶

DBeaver supports various cloud-based secret providers to retrieve database
credentials. For detailed setup instructions, see [Secret
Providers](../Secret-Providers/).

## Powering SQLite with DBeaver¶

DBeaver provides a host of features designed for SQLite databases. This
includes the ability to view and manage tables, along with numerous unique
capabilities aimed at optimizing database operations.

### SQLite database objects¶

DBeaver lets you view and manipulate a few SQLite database objects. DBeaver
has extensive support for various SQLite metadata types, allowing you to
interact with:

  * Tables
  * Views

Back to top

