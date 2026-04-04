# Source: https://dbeaver.com/docs/dbeaver/Driver-Manager/

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
      * Driver manager  [ Driver manager  ](./) Table of contents 
        * Obtaining a JDBC driver 
        * Driver Manager 
          * Add a new driver 
          * Main parameters 
          * Generic driver 
          * URL template 
          * Libraries 
            * Maven artifacts 
          * Driver properties 
          * Advanced parameters 
            * Main parameters 
            * Queries 
            * DDL 
            * Formatting 
          * Saving the driver and adding a connection 
        * Edit driver 
          * Change connection driver 
          * Update driver manually 
          * Update driver automatically 
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

  * Obtaining a JDBC driver 
  * Driver Manager 
    * Add a new driver 
    * Main parameters 
    * Generic driver 
    * URL template 
    * Libraries 
      * Maven artifacts 
    * Driver properties 
    * Advanced parameters 
      * Main parameters 
      * Queries 
      * DDL 
      * Formatting 
    * Saving the driver and adding a connection 
  * Edit driver 
    * Change connection driver 
    * Update driver manually 
    * Update driver automatically 

  1. [DBeaver](/docs/dbeaver)
  2. [Configure connection](/docs/dbeaver/Create-Connection)
  3. Driver settings

# Driver manager

DBeaver supports many types of databases, including SQL, NoSQL, and others, by
using pre-configured drivers to establish connections. If a specific database
is not supported by default, you can manually add its JDBC driver through the
Driver Manager.

Tip

DBeaver also supports ODBC drivers for users who prefer this standard. For
more information on integrating ODBC drivers, see [ODBC driver](../ODBC-JDBC-
Driver/).

## Obtaining a JDBC driver¶

A JDBC driver is a Java library that lets you connect and work with a specific
database. It includes everything needed to use all the features of the
database. These drivers are usually provided by the companies that create the
databases.

JDBC drivers are made up of one or more `.jar` files. These files contain the
code and other important files needed to use the driver. To add a new driver
to DBeaver, you first need to get these `.jar` files. You can find them
included with your database server or download them from the database
providerâs website. If you are not sure where to find them, ask your
database administrator.

## Driver Manager¶

To begin adding a new JDBC driver, first open the Driver Manager. You can find
it by navigating to **Databases - > Driver Manager** from the main menu.

![](../images/ug/drivers/driver-manager-view.png)

Button | Description  
---|---  
**New** | Creates a new driver configuration.  
**Copy** | Copies the selected driver configuration.  
**Edit...** | Opens the selected driver configuration for editing.  
**Delete** | Removes the selected driver configuration from DBeaver.  
**Un-delete** | Restores recently deleted driver configurations.  
  
### Add a new driver¶

Click the **New** button to start adding a new driver. In the driver edit
dialog, you will need to fill all the necessary details to configure the
driver.

### Main parameters¶

![](../images/ug/drivers/driver-manager-settings.png)

Parameter | Description  
---|---  
**Driver Name** | The name you assign to the driver. This can be any descriptive name that helps you identify the driver among others.  
**Driver Type** | Specifies the type of the driver used for connecting to the database. Users typically select the appropriate driver type based on the database being connected to. For unsupported databases, the **Generic** type is often used. For more information see section below.  
**Class Name** | The fully qualified name of the Java class for the JDBC driver. This is the main class that Java uses to interact with the database. It can often be found in the driver's documentation or by inspecting the `.jar` file.  
**URL Template** | A template for the database connection URL. If left empty, you must specify the JDBC URL manually for each connection. It's recommended to provide a template to simplify connection setup. For more information see section below.  
**Default Port** | The port number typically used by the database. This is optional and can be left blank if the port is non-standard or varies between installations.  
**Embedded** | Check this option if the database runs embedded within an application. This setting adjusts network and connection management configurations accordingly.  
**No Authentication** | Indicates that the driver does not use authentication. If selected, user and password input fields will be hidden in connection dialogs.  
**Category** | Used to group drivers within DBeaver. This field is deprecated but may still appear in some versions of the software.  
**ID** | A system-generated unique identifier for the driver. This is usually auto-filled.  
**Description** | A brief description of the driver.  
  
### Generic driver¶

The **Generic** driver allows you to connect to databases that do not have a
predefined JDBC driver. It works with any database that supports JDBC, giving
you control to manually load the required JDBC library.

This driver is useful for connecting to custom or uncommon databases. It
ensures flexibility in setting connection parameters, but you must ensure that
the JDBC driver you provide is fully compatible with the database to avoid
issues with connections or queries.

### URL template¶

JDBC drivers use URLs to connect to databases, similar to web URLs. These URLs
typically follow the format `jdbc:vendor:host:port/database`. For example, a
PostgreSQL database might use `jdbc:postgresql:localhost:5432/postgres`.
Directly editing these long and complex strings can be prone to errors and
inconvenient.

DBeaver simplifies this process by constructing the URL from connection
parameters like host, port, and database name, which you provide on the
connection configuration page. For the example mentioned, the URL template
would be: `jdbc:postgresql://{host}:{port}/{database}`

Info

For more information on the available variables, see [Pre-configured
variables](../Pre-configured-Variables/).

### Libraries¶

The Libraries tab displays a list of `.jar` files, binary libraries (such as
`.dll` or `.so` files), and other files necessary for the driver. Typically,
you only need to add `.jar` files here.

![](../images/ug/drivers/driver-manager-libraries.png)

Button | Description  
---|---  
**Add File** | Adds a single `.jar` file. Useful for including individual JDBC driver files or additional libraries needed.  
**Add Folder** | Adds an entire directory that contains Java classes or resources, facilitating bulk additions.  
**Add Artifact** | Allows for the inclusion of a Maven artifact directly, streamlining dependency management for users who utilize Maven. For more information see the section below.  
**Edit...** | Allows you to modify the selected file or folder properties.  
**Delete** | Enables you to remove a selected file or folder from the list.  
**Download/Update** | Allows for the downloading or updating of the selected library file or artifact.  
**Information** | Provides detailed information about the selected file or artifact, such as version, source, and dependencies.  
**Find Class** | Searches the added `.jar` files for JDBC driver classes and displays all found classes, enabling you to select the correct one for your configuration.  
**Classpath** | Displays the full classpath constructed from the added files and folders, useful for debugging or verification purposes.  
  
Once you have added the necessary `.jar` files, you can locate the JDBC driver
classes contained within these files. Click the **Find Class** button, and
DBeaver will list all available driver classes found in the added `.jars`.
Usually, there is only one driver class per driver, but if multiple classes
are listed, you should consult the driver's documentation to identify the
correct one.

#### Maven artifacts¶

DBeaver can download driver `.jars` from the Maven repository, a global
collection of Java libraries. If your database driver is listed in this public
repository, you can use this feature. Maven artifacts are useful because they
let you see all driver versions and change the driver version during runtime
without reconfiguring driver properties.

Info

For additional information, see [How to add additional artifacts to the
driver](../How-to-add-additional-artifacts-to-the-driver/).

### Driver properties¶

The Driver Properties tab displays default connection properties related to
the JDBC driver once a driver file is loaded. This tab allows for the
configuration and customization of various driver-specific settings necessary
for establishing and managing database connections.

![](../images/ug/drivers/driver-manager-properties.png)

### Advanced parameters¶

For most JDBC drivers, the default advanced properties suffice. However, you
may find it beneficial to adjust these settings for performance optimization
or to correct structural issues.

![](../images/ug/drivers/driver-manager-advanced-parameters.png)

#### Main parameters¶

Parameter | Description  
---|---  
**Driver supports indexes** | Indicates if the driver can utilize table indexes.  
**Driver supports stored code** | Supports stored database objects like procedures, functions, and packages.  
**Driver supports references** | Allows the driver to handle table references such as foreign keys.  
**Driver supports SELECT count(*) clause** | Supports the use of the SELECT count(*) SQL clause.  
**Driver supports views** | Enables the driver to manage table views.  
**Split procedures and functions** | Displays procedures and functions in separate folders in the UI.  
**Script delimiter** | Character or string used to separate SQL statements in scripts.  
**Script delimiter redefiner** | SQL clause that changes the script delimiter during execution.  
**Use script delimiter after query** | Retains the delimiter after each SQL query within scripts.  
**Use script delimiter after SQL block** | Maintains the delimiter after SQL blocks like `BEGIN/END`.  
**String escape character** | Character used to escape special characters in SQL strings.  
**Meta model type** | Defines the metadata model type, either standard or indexed.  
**All Objects Pattern** | SQL pattern to match all metadata objects.  
**Omit catalog(s)** | Skips catalog (database) information in metadata operations.  
**Omit single catalog** | Hides catalog in the UI if only one exists on the server.  
**Omit schema(s)** | Omits reading schema information from metadata.  
**Omit single schema** | Hides schema in the UI if only one exists.  
**Use schema filters** | Applies JDBC schema filters for databases not supporting catalogs, or filters schemas client-side.  
**Omit type cache** | Avoids using the driver's internal cache for data types.  
**Shutdown parameter** | Parameter for shutting down the database through URL.  
**Create database parameter** | URL parameter used to create a new database.  
**Driver supports multiple results** | Supports multiple result sets per query.  
**Driver supports result set limit** | Allows setting limits on the number of rows in a result set.  
**Driver supports structure cache** | Uses cache for database structure such as columns and keys.  
**Driver supports TRUNCATE operation** | Enables use of the `TRUNCATE` command, faster than using `DELETE`.  
  
#### Queries¶

Parameter | Description  
---|---  
**Get active database** | Retrieves the name of the currently active database.  
**Set active database** | Sets the active database during the session.  
**Shutdown database** | Command to shut down the active database connection.  
**PING query** | SQL query to check the connection state.  
**Dual table name** | Specifies the name of a dummy table used for evaluating expressions.  
**Active object type** | Defines the type of database object that can be selected (e.g., schema, catalog).  
**Driver supports results scrolling** | Enables scrolling through results in the result set.  
**Quote reserved words** | Automatically quotes SQL reserved words when they conflict with identifier names.  
**Escape LIKE masks in search queries** | Escapes special characters in `LIKE` clauses during metadata searches.  
  
#### DDL¶

Parameter | Description  
---|---  
**Drop column short syntax** | Uses a shorter syntax for dropping columns.  
**Drop column - use brackets** | Encloses column names in brackets when dropping.  
**Use legacy SQL dialect for DDL** | Uses a traditional SQL dialect for DDL operations.  
**Add COLUMN keyword in alter table query** | Adds the `COLUMN` keyword in `ALTER TABLE` queries for clarity.  
  
#### Formatting¶

Parameter | Description  
---|---  
**Timestamp format** | The format pattern for timestamp columns.  
**Date format** | The format pattern for date columns.  
**Time format** | The format pattern for time columns.  
  
Info

For more information on a date/time format pattern, see [DateTimeFormatter
documentation](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html#patterns).

### Saving the driver and adding a connection¶

Once you have completed configuring your driver, click the **Ok** button to
save the settings. You are now ready to [Create a connection](../Create-
Connection/).

## Edit driver¶

Editing an existing driver can be done through several access points:

  * **Driver Manager** : Navigate through **Databases - > Driver Manager** in the main menu to edit any listed driver.
  * **Database Navigator** : Right-click on a database connection to open the context menu, then select **Edit Connection** to open the [**Connection Properties** dialog](../Create-Connection/#configuring-connection-settings). This method allows you to modify the driver settings linked specifically to that connection.

### Change connection driver¶

You can change the driver version for an existing connection:

  1. Select a connection in the [Database Navigator](../Database-Navigator/).
  2. Go to **Database** in the [Menu bar](../Application-Window-Overview/#menu-bar).
  3. Click **Change connection(s) driver** , then select a different driver.

![](../images/ug/drivers/change-connection-driver.png)

Note

DBeaver uses two types of drivers: built-in and downloadable (Maven-based).
You can only change the version for downloadable drivers. To update a built-in
driver, update it manually.

### Update driver manually¶

To update a driver version manually:

  1. In [Database Navigator](../Database-Navigator/), right-click your connection.
  2. Click **Edit Connection**.
  3. In the window that opens, click **Driver Settings**.
  4. Go to the **Libraries** tab.
  5. Double-click the driver file - this opens its folder.

Info

If thereâs no driver listed (for example, you deleted it), click **Add
File** or **Add Folder** , then select the driver file manually.

  6. Replace the file with the new version. You need to download the `.jar` file manually. Sources vary depending on the driver:

     * **Official vendor site** \- some drivers are only available on the database vendorâs site.
     * **GitHub releases** \- many open-source drivers publish binaries in the **Releases** section.
     * **Maven Central** \- some drivers are available at [search.maven.org](https://search.maven.org).
     * **Other public repositories** \- some projects host drivers on project-specific sites or custom registries.

Tip

You donât need to delete the whole folder - just replace or remove old
`.jar` files to avoid conflicts.

  7. Click **OK** , then **Test Connection** to verify it works.

### Update driver automatically¶

You can configure your drivers to update automatically on startup.

  1. Go to **Window - > Preferences -> Connections -> Drivers**.

![](../images/ug/drivers/update-driver-automatically.png)

  2. Configure driver-related settings:

Setting | Description  
---|---  
**Check for new driver versions** | Automatically checks for driver updates when DBeaver starts.  
**Proxy Host** | Hostname of the proxy server used for driver downloads.  
**Proxy Port** | Port number for the proxy.  
**User** | Username for proxy authentication (if needed).  
**Password** | Password for proxy authentication.  
**Local folder** | Local folder where downloaded drivers are stored. You can specify a custom directory.  
**File repositories** | URLs of remote repositories used for downloading drivers.  
  3. Click **Apply and Close**.

Back to top

