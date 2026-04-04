# Source: https://dbeaver.com/docs/dbeaver/Command-Line/

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
      * Command line  [ Command line  ](./) Table of contents 
        * Windows 
        * MacOS 
        * Linux 
        * Using dbeaver.ini 
        * Command line parameters 
          * DBeaver control 
          * System parameters 
            * VM parameters 
            * Connection parameters 
          * Install Eclipse extensions 
        * Exit codes 
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

  * Windows 
  * MacOS 
  * Linux 
  * Using dbeaver.ini 
  * Command line parameters 
    * DBeaver control 
    * System parameters 
      * VM parameters 
      * Connection parameters 
    * Install Eclipse extensions 
  * Exit codes 

  1. [DBeaver](/docs/dbeaver)
  2. [Administration](/docs/dbeaver/Admin-Manage-Preferences)
  3. General configuration

# Command line

Command line parameters can be passed directly to the DBeaver executable. The
way to do this depends on your operating system.

## Windows¶

You can use the `dbeaverc.exe [parameters]` executable. This version doesnât
spawn a new window, so you can see output messages in the same terminal.

## MacOS¶

Parameters can be passed in two ways:

  * Use the `open` command with the `-a` flag and the app name, followed by `--args` and your parameters.

Depending on the edition, use `DBeaver.app`, `DBeaverLite.app`,
`DBeaverEE.app`, or `DBeaverUltimate.app`.

Example

`open -a "DBeaver.app" --args [parameters]`

This method does **not** redirect logs, `stdout`, or `stderr` to the terminal.

  * Run the actual executable directly from inside the `.app` package.

Example

`/Applications/DBeaver.app/Contents/MacOS/dbeaver [parameters]`

This method **does** redirect logs, `stdout`, and `stderr` to the terminal.

## Linux¶

Pass parameters directly to the DBeaver executable in the terminal.

Example

`/usr/bin/dbeaver-ce [parameters]`.

This method redirects logging messages, `stdout`, and `stderr` to the
terminal.

## Using dbeaver.ini¶

Parameters can also be added in the `dbeaver.ini` configuration file. These
should be written at the beginning of the file, with each parameter on its own
line.

Tip

Detailed instructions on finding `dbeaver.ini` are available in [our
article](../Configuration-files-in-DBeaver/#how-to-locate-the-dbeaver-ini).

## Command line parameters¶

### DBeaver control¶

Name | Value | Example  
---|---|---  
`-help` | Prints help message. |   
`-stop` | Quits DBeaver. |   
`-dump` | Prints DBeaver thread dump. [Learn more about Thread Dump](../Making-a-thread-dump/) |   
`-f` | Opens the file in DBeaver UI, if the command has `-con` argument, connects it to datasource. | `-f c:\some-path\some-file.sql`  
`-connect` | Opens database connection in DBeaver UI. Learn more | See connection parameters table  
`-closeTabs` | Closes all open editor tabs. |   
`-disconnectAll` | Closes all open connections. |   
`-reuseWorkspace` | Forces reuse of single workspace by multiple DBeaver instances. |   
`-newInstance` | Forces new DBeaver instance creation (do not try to reuse already running one). |   
`-bringToFront` | Brings the DBeaver window on top of other applications. |   
`-runTask` ![](../images/commercial.png) | Executes specified [task](../Task-Management/#run-tasks-from-the-command-line). The command returns an exit code that indicates success or failure. | `-runTask @projectName:taskName`.  
`-var` ![](../images/commercial.png) | Customs variables for runTask. You can add several parameters at once to the command line, each starting with `-var`. Used right after `-runTask`. Example: `-var variableName=variableValue`. | `-runTask exportFromSakila`  
`-var film=sakila.film`  
`-var actor=sakila.actor`  
`-vars` | Path to a property file with variables. | `-vars c:\path\to\file.properties`  
For more information, see [Declare external variables in a file](../Admin-
Variables/#declare-external-variables-in-a-file)  
`-license` | Path to the license file. | `-license "/etc/licenses/dbeaver.txt"`.  
  
Important

Place task variables (`-var`) after the `-runTask` command. Example:

    
    
    -runTask @General:export -var test=123
    

### System parameters¶

Name | Value | Example  
---|---|---  
`-nl` | UI language and locale (affects UI translation, number/date formats). For supported values, see [Supported languages](../UI-Language/#supported-languages). | `-nl "en_US"`  
`-data` | Workspace path. | `-data "c:\ProgramData\MyWorkspace"`  
`-nosplash` | Omits splash screen. |   
`-clean` | Clears all Eclipse caches. Use it if DBeaver fails to start after it upgrades. |   
`-vmargs` | Passes VM parameters. | See VM arguments table  
  
Important

The `-data` parameter only affects the **workspace** location. Other folders
are created in the [default location](../Workspace-Location/#default-location-
of-the-workspace).

#### VM parameters¶

You can pass any advanced Java parameters supported by your local JVM.
Parameters supported by HotSpot JVM (21):
`https://docs.oracle.com/en/java/javase/21/docs/specs/man/java.html`

Parameters supported by all JVMs:

Name | Value | Example  
---|---|---  
`-Xms` | Sets initial memory available for DBeaver. | `-Xmx1000m`  
`-Xmx` | Sets maximum memory available for DBeaver. | `-Xmx4000m`  
  
#### Connection parameters¶

Use the `-con` argument to open a database connection in the DBeaver UI.

Pass all parameters as a **single string** , using:

  * `|` to separate parameters
  * `=` to separate names and values

Example

`-con "driver=sqlite|database=C:\db\SQLite\Chinook.db|name=SQLite"`

See the table below for supported arguments.

Name | Description | Example  
---|---|---  
`name` | Connection name. | `Test connection`  
`driver` | Driver name or ID. | `driver=sqlite`, `driver=mysql`, etc  
`url` | Connection URL. Optional (JDBC URL may be constructed by a driver from other parameters). | `url=jdbc:sqlite:C:\db\SQLite\Chinook.db`  
`host` | Database host name (optional). | `host=localhost`  
`port` | Database port number (optional). | `port=1534`  
`server` | Database server name (optional). | `server=myserver`  
`database` | Database name or path (optional). | `database=db-name`  
`user` | User name (optional). | `user=root`  
`password` | User password (optional). | `password=mysecret`  
`auth` | Authentication model ID. See [Auth models](../Database-authentication-models/). | `auth=postgres_pgpass`  
`authProp.propName` | Custom authentication parameters (depends on the driver and [auth model](../Database-authentication-models/)). | `authProp.oracle.net.wallet_location=C:/temp/ora-wallet`  
`savePassword` | Does not ask user for a password on connection. | `savePassword=true`  
`showSystemObjects` | Shows/Hides system schemas, tables, etc. | `showSystemObjects=true`  
`showUtilityObjects` | Shows/Hides utility schemas, tables, etc. | `showUtilityObjects=true`  
`folder` | Puts a new connection in a folder. | `folder=FolderName`  
`autoCommit` | Sets connection auto commit flag (default value depends on driver). | `autoCommit=true`  
`prop.propName` | Advanced connection parameters (depend on driver). | `prop.connectTimeout=30`  
`id` | Connection id. | `oracle_thin-16a88e815bd-70598e648cedd28c` (useful in conjunction with `create=false`)  
`connect` | Connects to this database. | `connect=false`  
`openConsole` | Opens the SQL console for this database (sets `connect` to true). | `openConsole=true`  
`create` | Creates new connection. | `create=false` (true by default). If it is set as false, then an existing connection configuration will be used. The name or id parameter must be specified.  
`save` | Saves new connection. | When `create=true`, then `save=false` (default) makes new connection temporary, `save=true` means that new connection will be saved and accessible between DBeaver launches.  
  
Tip

See how to [declare external variables in a file](../Admin-Variables/#declare-
external-variables-in-a-file)

### Install Eclipse extensions¶

You can install additional Eclipse-compatible extensions directly from the
command line using the built-in P2 Director. This method doesnât require the
graphical interface.

Name | Value | Example  
---|---|---  
`-application` | Defines which Eclipse application to run. Use `org.eclipse.equinox.p2.director` to install extensions via the built-in Eclipse P2 Director. | `-application org.eclipse.equinox.p2.director -repository https://wakatime.com/eclipse/update-site/ -repository https://download.eclipse.org/releases/2025-06/ -installIU com.wakatime.eclipse.feature.feature.group -followReferences`  
  
Info

For details on Eclipse P2 Director syntax and available arguments, see the
[official Eclipse
documentation](https://help.eclipse.org/latest/topic/org.eclipse.platform.doc.isv/guide/p2_director.html?cp=2_0_20_2)

## Exit codes¶

When DBeaver finishes executing a command, it returns an **exit code** to
indicate the result.

Code | Name | Description  
---|---|---  
`-1` | `EXIT_CODE_CONTINUE` | Indicates that the process continues running. You wonât normally see this code when running commands.  
`0` | `EXIT_CODE_OK` | Command executed successfully.  
`1` | `EXIT_CODE_ERROR` | A general error occurred during execution.  
`2` | `EXIT_CODE_ILLEGAL_ARGUMENTS` | Invalid command line arguments were provided.  
  
Back to top

