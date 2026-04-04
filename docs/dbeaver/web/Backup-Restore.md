# Source: https://dbeaver.com/docs/dbeaver/Backup-Restore/

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
    * Backup and restore  [ Backup and restore  ](./) Table of contents 
      * Database specific settings 
        * MySQL 
          * Backup MySQL database 
          * Restore MySQL database 
        * PostgreSQL 
          * Backup PostgreSQL database 
          * Global PostgreSQL database backup 
          * Restore PostgreSQL database 
      * Additional features 
        * Execute Script Command 
        * Extra command arguments 
        * Dump and restore operations as tasks 
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

  * Database specific settings 
    * MySQL 
      * Backup MySQL database 
      * Restore MySQL database 
    * PostgreSQL 
      * Backup PostgreSQL database 
      * Global PostgreSQL database backup 
      * Restore PostgreSQL database 
  * Additional features 
    * Execute Script Command 
    * Extra command arguments 
    * Dump and restore operations as tasks 

  1. [DBeaver](/docs/dbeaver)
  2. Data transfer and schema compare

# Backup and restore

Note

This feature is available in Community, [Enterprise](../Enterprise-Edition/),
[Ultimate](../Ultimate-Edition/) and [Team](https://dbeaver.com/docs/team-
edition/) editions only.

This article provides an in-depth guide to the Backup and Restore features
available in DBeaver. DBeaver supports a wide range of databases for backup
and restore operations:

**Classic databases** | **Cloud databases**  
---|---  
CrateDB | [AlloyDB](../Database-driver-AlloyDB-for-PostgreSQL/)  
[Greenplum](../Database-driver-Greenplum/) | [Google Cloud SQL for MySQL](../Database-driver-MySQL-on-Google-Cloud/)  
[MariaDB](../Database-driver-MariaDB/) | [Google Cloud SQL for PostgreSQL](../Database-driver-PostgreSQL-on-Google-Cloud/)  
Materialize |   
[MySQL](../Database-driver-MySQL/) |   
[PostgreSQL](../Database-driver-PostgreSQL/) |   
SingleStore |   
TiDB |   
TimescaleDB |   
[Yellowbrick](../Database-driver-Yellowbrick/) |   
YugabyteDB |   
EnterpriseDB |   
  
The native backup and restore differs from the standard DBeaver [Data
Transfer](../Data-transfer/) feature by focusing on creating and applying
database backups using specialized utilities. These tools are tailored for
high-performance interactions with databases, potentially accelerating the
backup and restore processes compared to general data transfer methods.

These functions can be accessed from the Context Menu's **Tools** or the Main
Menu's **Database** -> **Tools**.

## Database specific settings¶

Different database systems possess distinct settings for backup and restore
processes. This section presents the settings specific to MySQL and
PostgreSQL.

### MySQL¶

#### Backup MySQL database¶

To initiate a backup:

  1. Select the desired database.

  2. Right-click on the database and choose **Tools** -> **Dump database**.

  3. The **Dump** window will appear. Select the necessary objects and click **Next**.

  4. The **Export configuration** tab will be displayed. Here you can find the following checkboxes and fields:

![](../images/ug/tools/backup-restore/mysql-dump-window.png)

Option/Field | Description  
---|---  
**Execution Method** | Method for execution. The default is **Normal (no locks)**.  
**Execution Method** options: | **Normal (no locks)** : This is the default method. It performs the dump without acquiring any locks on the tables. Suitable for databases where minimal disruption is required during the dump process.  
| **Online backup in single transaction** : This method ensures the
consistency of the database by performing the dump within a single
transaction. It's ideal for databases that support transactional storage
engines like InnoDB. The backup occurs without interrupting other database
operations but requires a higher isolation level.  
| **Lock all tables** : As the name suggests, this method locks all tables in
the database during the dump process. It ensures complete consistency of the
dump but may interrupt other database operations. Suitable for databases or
situations where you want a consistent snapshot and are okay with potential
disruptions.  
**No CREATE statements** | Do not include `CREATE` statements in the dump.  
**Compressed** | Include the `--compress` flag to enable network compression during dump.  
**Add DROP statements** | Include `DROP` statements before CREATE statements.  
**Disable keys** | Disable keys during the dump process.  
**Extended inserts** | Use extended `INSERT` statements in the dump.  
**Dump events** | Include events in the dump.  
**Additional comments** | Include comments in the dump.  
**Remove DEFINER** | Remove `DEFINER` clause from the dump.  
**Dump binaries in hex** | Display binary data as `HEX` in the dump.  
**Structure only** | Only dump table structures, not data.  
**Output folder** | Specify the directory where the dump file will be saved. For Ultimate Edition, Team Edition, and CloudBeaver versions, users have the option to save to a remote file system using the **Browser remote file system** button ![](../images/dt/Browser-remote-file-system-button.png).  
**Extra command args** | Provide additional command-line arguments. See details in the Extra command arguments section.  
**Authenticate** | Click to open the **Authentication** window where you can fill in the Username/Password for override.  
**Reset to default** | Reset credentials to their default values.  
**Override host credentials** | Use different host credentials, if necessary.  
**Local Client** | Open a window to specify the path to the Local client. [More about setting it up](../Local-Client-Configuration/).  
  
Note

The particular set of configuration options depends on the database type.

  5. After configuring the settings, click **Start**.

  6. Upon successful completion, a notification will appear with information about the process.

  7. The backup file can be found in the folder specified during the **Export configuration** step.

#### Restore MySQL database¶

To initiate a restore:

  1. Select the desired database.

  2. Right-click on the database and choose **Tools** -> **Restore database**.

  3. The **Restore** window will appear. In this window you have to provide the path to the SQL file you wish to restore from in the designated field. Example path: `/path/to/file.sql`

![](../images/ug/tools/backup-restore/mysql-restore-window.png)

Below are the settings for the restore process:

Setting Name | Description  
---|---  
**Log Level** | Choose the level of logging for the restore process.  
**Log Level** options: | **Normal** : Provides standard logging information. It captures the essential details of the restore process, ensuring that the logs remain concise and focused on primary events.  
| **Verbose** : Gives more detailed logging information than the Normal level.
It includes additional context and information, making it suitable for
situations where you want to understand the process more in-depth without
getting into debugging details.  
| **Debug** : Offers the most detailed logging information. It captures all
events, including low-level operations and potential issues. This level is
ideal for troubleshooting problems or understanding the inner workings of the
restore process.  
**Extra command args** | Provide additional command-line arguments. See details in the Extra command arguments section.  
**Disable foreign key checks** | Disable foreign key checks during the restore process.  
**Authenticate** | Click to open the **Authentication** window where you can fill in the Username/Password for override.  
**Reset to default** | Reset credentials to their default values.  
**Override host credentials** | Use different host credentials, if necessary.  
**Local Client** | Specify the path to the Local client.  
  
Tip

In the input field for specifying the path to the SQL file, you can choose a
file from a local directory or use the **Browser remote file system** button
![](../images/dt/Browser-remote-file-system-button.png) to select a file from
a remote file system. This functionality is accessible to users of the
Ultimate Edition, Team Edition, and CloudBeaver.

  4. After configuring the settings, click **Start**.

  5. Upon successful completion, a notification will appear with information about the process.

### PostgreSQL¶

#### Backup PostgreSQL database¶

To initiate a backup:

  1. Select the desired database.

  2. Right-click on the database and choose **Tools** -> **Backup**.

  3. The **Dump** window will appear. Select the necessary objects and click **Next**.

![](../images/ug/tools/backup-restore/postgresql-dump-choose-objects-
window.png)

Note

By default, when all schemas are selected, DBeaver enables the **Complete
backup** checkbox and skips `-n` flags in the `pg_dump` command to include all
database objects. Clear the checkbox to add `-n` for each selected schema and
back up only those. For details, see the [`pg_dump` \--schema
documentation](https://www.postgresql.org/docs/current/app-pgdump.html#APP-
PGDUMP-OPTIONS).

  4. The **Backup settings** tab will be displayed. Here you can find the following checkboxes and fields:

![](../images/ug/tools/backup-restore/postgresql-dump-window.png)

Setting | Description  
---|---  
**Format** | Choose the format for the dump. Options include Directory, Tar, Custom, and Plain.  
**Format** options: | **Directory** : Splits the output into one file per table. Suitable for larger databases as it facilitates parallel restoration.  
| **Tar** : Produces archive in tar format. Useful for backups since it can be
read by standard tools.  
| **Custom** : A flexible format that allows selective restore and other
operations.  
| **Plain** : Produces plain-text SQL script file. It can be used with psql
for restoring.  
**Compression** | Set the compression level for the dump, ranging from 0 (no compression) to 9 (maximum compression).  
**Encoding** | Select the character encoding for the dump. The available encodings depend on database configuration and locale.  
**Use SQL INSERT instead of COPY for rows** | Use the `INSERT` command instead of the `COPY` command for row data.  
**Do not backup privileges (GRANT/REVOKE)** | Exclude privilege commands (`GRANT`/`REVOKE`) from the dump.  
**Discard objects owner** | Exclude the ownership information from the dump.  
**Add drop database statement** | Include a statement in the dump to drop the database before restoring.  
**Add create database statement** | Include a statement in the dump to create the database when restoring.  
**Output folder** | Specify the directory where the dump file will be saved. For Ultimate Edition, Team Edition, and CloudBeaver versions, users have the option to save to a remote file system using the **Browser remote file system** ![](../images/dt/Browser-remote-file-system-button.png) button.  
**File name pattern** | Define the naming pattern for the dump file, with variables like `${database}` and `${timestamp}` to customize the filename.  
**Extra command args** | Provide additional command-line arguments. See details in the Extra command arguments section.  
**Authentication** | Click to open the **Authentication** window where you can fill in the Username/Password for override.  
**Reset to default** | Reset credentials to their default values.  
**Override host credentials** | Use different host credentials, if necessary.  
**Local Client** | Specify the path to the Local client.  
  
Note

The particular set of configuration options depends on the database type.

  5. After configuring the settings, click **Start**.

  6. Upon successful completion, a notification will appear with information about the process.

  7. The backup file can be found in the folder specified during the **Backup settings** step.

#### Global PostgreSQL database backup¶

When performing a Global PostgreSQL database Backup, the entire database is
dumped, including roles and tablespaces. This differs from standard backup
procedures where only specific schemas and their contents can be selected.
Additionally, multiple databases can be chosen for backup at once in the
global method.

To initiate a global backup:

  1. Select the desired database.

  2. Right-click on the database and choose **Tools** -> **Global Backup**.

  3. The **Global Dump** window will appear. Select the necessary objects and click **Next**.

  4. The **Backup settings** tab will be displayed. Here you can find the following checkboxes and fields:

![](../images/ug/tools/backup-restore/postgresql-global-dump-window.png)

**Setting** | **Description**  
---|---  
**Encoding** | Set the character encoding for the backup.  
**Dump only the object definitions, not data** | Includes only the structure of the database objects, excluding the data.  
**Dump only global objects, no databases** | Includes only global objects and excludes individual databases.  
**Dump only roles** | Includes only user roles.  
**Dump only tablespaces** | Captures only tablespaces without the databases.  
**Do not backup privileges (GRANT/REVOKE)** | Excludes privilege statements like `GRANT` and `REVOKE`.  
**Discard objects owner** | Excludes the ownership information of the database objects.  
**Dump passwords for roles** | Includes passwords associated with the user roles.  
**Output folder** | Specify the directory where the dump file will be saved. For Ultimate Edition, Team Edition, and CloudBeaver versions, users have the option to save to a remote file system using the **Browser remote file system** button ![](../images/dt/Browser-remote-file-system-button.png).  
**File name pattern** | Define the naming pattern for the dump file, with variables like `${database}` and `${timestamp}` to customize the filename.  
**Extra command args** | Provide additional command-line arguments. See details in the Extra command arguments section.  
**Authenticate** | Click to open the **Authentication** window where you can fill in the Username/Password for override.  
**Reset to default** | Reset credentials to their default values.  
**Override host credentials** | Use different host credentials, if necessary.  
**Local Client** | Specify the path to the Local client.  
  5. After configuring the settings, click **Start**.

  6. Upon successful completion, a notification will appear with information about the process.

  7. The backup file can be found in the folder specified during the **Global backup settings** step.

#### Restore PostgreSQL database¶

To initiate a restore:

  1. Select the desired database.

  2. Right-click on the database and choose **Tools** -> **Restore**.

![](../images/ug/tools/backup-restore/postgresql-restore-window.png)

Setting | Description  
---|---  
**Format** | Choose the format for the restore operation. Options include **Directory** , **Tar** , **Custom** , and **Plain**.  
**Format** options: | **Directory** : Assumes the input consists of one file per table. Suitable for larger databases as it supports parallel restore.  
| **Tar** : Assumes the input is an archive in tar format. This is useful when
restoring backups made in tar format.  
| **Custom** : A flexible input format that allows selective restore and other
operations.  
| **Plain** : Assumes the input is a plain-text SQL script file. Suitable for
scripts that can be executed with psql.  
**Clean (drop) database objects before recreating them** | Drop database objects before recreating them from the backup.  
**Create database** | Create a new database from the backup.  
**Discard objects owner** | Exclude ownership information during the restore.  
**Backup file** | Specify the path to the backup file that you wish to restore. For Ultimate Edition, Team Edition, and CloudBeaver versions, use the **Browser remote file system** button ![](../images/dt/Browser-remote-file-system-button.png) to select a backup file from a remote file system via [Cloud Storage](../Cloud-Storage/).  
**Extra command args** | Provide additional command-line arguments. See details in the Extra command arguments section.  
**Authentication** | Click to open the **Authentication** window where you can fill in the Username/Password for override.  
**Reset to default** | Reset credentials to their default values.  
**Local Client** | Specify the path to the Local client.  
  3. After configuring the settings, click **Start**.

  4. Upon successful completion, a notification will appear with information about the process.

## Additional features¶

### Execute Script Command¶

In DBeaver, besides the standard backup and restore operations, there's an
additional capability to run scripts directly through the **Execute script**
command. This functionality uses native database clients.

![](../images/ug/tools/backup-restore/postgresql-execute-script-command-
window.png)

Steps to use the **Execute script** command:

  1. Right-click on the desired database in the navigator tree.
  2. Navigate to **Tools** -> **Execute script**.
  3. A window will appear prompting you to provide the path to your script.

Tip

In the input field for specifying the path to the SQL file, you can choose a
file from a local directory or use the **Browser remote file system** button
![](../images/dt/Browser-remote-file-system-button.png) to select a file from
a remote file system.

The **Execute script** command provides an alternative way to perform database
operations that may not be covered by the traditional restore functionality.
This includes running complex scripts or batch operations that require direct
execution in the database's native environment.

### Extra command arguments¶

The **Extra command args** field allows you to input additional command-line
arguments to further customize the dump process. This offers more specific
control over the operation.

For example, when configuring backup/restore for PostgreSQL, you may want to
exclude specific tables. To exclude a table named `employee_data`, use the
`--exclude-table` option. Enter `--exclude-table=employee_data` in the **Extra
command args** field during the setup process.

By doing this, the resulting process won't contain any data or structure from
the `employee_data` table.

Note

Always consult the database's official documentation for a comprehensive list
and explanation of available command-line arguments.

### Dump and restore operations as tasks¶

You can set up both restore and dump operations as tasks. To save an operation
as a task, click the **Save task** button ![](../images/ug/tools/backup-
restore/save-task-button.png) during the dump/restore process. For detailed
instructions and features related to task management in DBeaver, refer to
[Task management article](../Task-Management/).

Back to top

