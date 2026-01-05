# Source: https://dbeaver.com/docs/dbeaver/Data-migration/

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
      * Data migration  [ Data migration  ](./) Table of contents 
        * Data migration process 
          * Step 1 Define the data source 
          * Step 2 Define data transfer target type 
          * Step 3 Tables mapping 
            * Available options 
            * Target container and target table 
            * Specify target container 
            * Define a target table 
            * Mapping 
            * Transform column values 
            * Configure 
            * Column mapping 
            * Table properties 
            * Target DDL 
            * Mapping Rules 
          * Keyboard Shortcuts 
          * Step 4 Extraction settings 
          * Step 5 Data load settings 
          * Step 6 Confirm 
          * Step 7 Export completion notification 
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

  * Data migration process 
    * Step 1 Define the data source 
    * Step 2 Define data transfer target type 
    * Step 3 Tables mapping 
      * Available options 
      * Target container and target table 
      * Specify target container 
      * Define a target table 
      * Mapping 
      * Transform column values 
      * Configure 
      * Column mapping 
      * Table properties 
      * Target DDL 
      * Mapping Rules 
    * Keyboard Shortcuts 
    * Step 4 Extraction settings 
    * Step 5 Data load settings 
    * Step 6 Confirm 
    * Step 7 Export completion notification 

  1. [DBeaver](/docs/dbeaver)
  2. [Data transfer and schema compare](/docs/dbeaver/Data-transfer)
  3. Data transfer

# Data migration

Note

This feature is available in Community, [Enterprise](../Enterprise-Edition/),
[Ultimate](../Ultimate-Edition/) and [Team](https://dbeaver.com/docs/team-
edition/) editions only.

**Data Migration** in DBeaver provides the functionality to transfer data
between different databases or between tables within the same database.

## Data migration process¶

### Step 1 Define the data source¶

To initiate the data migration, you need to select your data source. Follow
the steps below:

  1. Navigate to the [Database Navigator](../Database-Navigator/).
  2. Select one or multiple tables that you want to export.
  3. Right-click to open the context menu.
  4. Choose **Export Data** from the options.

![](../images/dt/dt_migration/database-navigator-export_menu.png)

Alternatively, you can export data from a custom SQL query. Execute the query
and then choose **Export Data** from the results context menu.

Tip

You can start the migration through AI by sending a short request in AI chat.
See [Data transfer actions](../Data-Transfer-Actions/) for supported commands.

### Step 2 Define data transfer target type¶

After selecting the data source, the next step is to specify the type of
destination for the data transfer. Choose **Database** type as the data
transfer target and press **Next**.

![](../images/dt/dt_migration/data-transfer-export-target.png)

### Step 3 Tables mapping¶

Once you have chosen **Database** as the transfer target type, the next step
involves mapping data. This process includes specifying options, selecting the
target container, and setting other configurations. Configure your data
mapping settings and press **Next** to proceed to the next step.

![](../images/dt/dt_migration/data-transfer-tables-mapping.png)

#### Available options¶

Buttons:

Icon | Option | Description  
---|---|---  
![](../images/dt/dt_migration/configure-button.png) | **Customize** | Opens additional settings. For details, see the Configure section.  
![](../images/dt/dt_migration/preview-data-button.png) | **Preview data** | Shows a preview of the data to be transferred.  
![](../images/dt/dt_migration/up-button.png) | **Up** | Moves the selected mapping closer to the head of the queue.  
![](../images/dt/dt_migration/down-button.png) | **Down** | Moves the selected mapping closer to the tail of the queue.  
![](../images/dt/dt_migration/mapp-with-ai-button.png) | **Map with AI** | Automatically maps source tables and columns to target names and types using AI. It analyzes sample data and schema structure, then suggests how to name the new tables and columns in the target database. In the Mapping Rules, you can choose how AI matches columns.  
![](../images/dt/dt_migration/mapping-rules-button.png) | **Mapping Rules** | Choose how new tables and column names are transformed when transferring data. For details, see Mapping Rules section.  
  
Note

**Map with AI** button is available only when AI is enabled. For setup
instructions, see [AI Assistant setup](../AI-Assistance-settings/#ai-
assistant-setup).

Fields:

Option | Description  
---|---  
**Target container** | Defines the database or schema for the data transfer. For more details, see the Target Container section.  
**Source** | Displays the names of selected tables and their columns.  
**Target** | Shows the names of destination tables.  
**Mapping** | Lists the available actions for data transfer. For more details, see the Mapping section.  
**Transform** | Allows for the transformation of column values during the data transfer. For more details, see the Transform section.  
  
#### Target container and target table¶

#### Specify target container¶

In the mapping table, click the **Target** cell for the desired **Source**
row, then click the three dots button (![](../images/dt/dt_migration/target-
button.png)) to select the container where the data will be transferred.

#### Define a target table¶

![](../images/dt/dt_migration/data-transfer-tables-mapping-target.png)

You can specify the target table where the data will be transferred in
multiple ways:

  * **Manual Entry** : Click on a cell in the **Target** column and manually enter the name of the table where you wish to transfer the data.

  * **Drop-down list** : Use the drop-down list next to the **Target** column to choose among the following options:

    * Pre-existing table names.
    * **Skip** : Skips the data transfer for this table.
    * **Browse** : Opens the **Choose Target Table** window
  * **Browse** button: Click the **Target** cell for the desired **Source** row, then click the three dots button (![](../images/dt/dt_migration/target-button.png)).

![](../images/dt/dt_migration/choose-target-table.png)

#### Mapping¶

To change the mapping type, click a cell in the **Mapping** column of **Table
mapping dialog box** and select the required mapping type.

![](../images/dt/dt_migration/data-transfer-tables-mapping-mapping-column.png)

Action | Description  
---|---  
**Create** | Transfers source data into a newly created table or column in the target container.  
**Skip** | Does not transfer the source data.  
**Existing** | Transfers source data to an existing table in the target container.  
**Recreate** | Recreate the table, which means that the available data, keys, indexes, and other possible entities of the existing table will be lost.  
  
Tip

If the cells are marked with ![](../images/dt/dbt_step3_Target_red.png), it
means that in the target table, there are no columns with matching names,
otherwise the names will be filled in automatically.

#### Transform column values¶

You may also want to transform the values of some columns during the transfer.
To do that, define column transformers by clicking on corresponding cells in
the **Transform** column. You can choose one of three options:

![](../images/dt/dt_migration/data-transfer-tables-mapping-transform.png)

Option | Description  
---|---  
**Set to NULL** | All values in the corresponding column are set to `null`.  
**Constant** | Sets column value to a constant value.  
**Expression** | Uses `JEXL` expressions to calculate the column's value.  
  
#### Configure¶

Click the **Configure** button to open the **Configure metadata structure**
window. This window allows you to delve into additional settings are
distributed across the following tabs:

#### Column mapping¶

By navigating to the **Column mapping** , you can explore detailed mapping
between the source and target columns.

![](../images/dt/dt_migration/configure-metadata-structure.png)

Element | Description  
---|---  
**Source Column** | Contains names of columns existing in the selected source table.  
**Source Type** | Lists the data types assigned to the columns in the selected source table.  
**Target Column** | Contains names of columns in the target table where the data from the source column will be transferred.  
**Target Type** | Lists the data types that will be assigned to the columns in the target table.  
**Mapping** | Contains the list of actions to be applied to the data on data transfer.  
**Transform** | Displays transformations for the data in a column during the transfer.  
  
Important

Data types that are supported in the source database may not be supported in
the target, and vice versa. To set a data type for a target column, click the
cell in the **Target Type** column and choose from the dropdown list.

#### Table properties¶

By selecting the **Table properties** tab, you can modify properties of the
target table, such as:

Property | Description  
---|---  
**Tablespace** | Specifies the tablespace for the target table.  
**Partition By** | Sets the partitioning for the target table.  
**Comment** | Allows you to add comments to the target table.  
  
Note

The availability of these settings may vary depending on the database you are
using.

#### Target DDL¶

By selecting the **Target DDL** tab, you can view the SQL script that will be
executed during the data transfer.

If you're exporting data to a new table or recreating an existing one, the tab
will display the necessary SQL statements. If not, the DDL tab will remain
empty.

#### Mapping Rules¶

Clicking the **Mapping Rules** button opens a window that provides options for
customizing how new tables and column names are transformed during the data
transfer.

![](../images/dt/dt_migration/data-transfer-tables-mapping-mapping-rules.png)

In the window, the following settings are available:

Option | Description  
---|---  
**Name case** | Sets the letter casing for table and column names. Choices include **Default** , **Upper case** , and **Lower case**.  
**Replace spaces** | Determines how spaces in table and column names are handled. Options are: **Do not replace** , **Replace with underscore** , and **Remove, convert to CamelCase**.  
**Max data type length** | Sets the maximum length for data types.  
**Save current changes to global settings** | If checked, saves the current mapping rules to global settings. Otherwise, they will be saved at the data source settings level.  
**Global settings** | Opens the global settings window for **Names Mapping Rules**. Alternatively, to open global settings, go to **Window** -> **Preferences** -> **Connections** -> **Data Transfer**  
**Choose mapping strategy** ![](../images/commercial.png) | Defines how AI Custom Mapping matches columns between source and target tables. You can choose to match by **Data types** , **Column names** , or **Data types and column names**. This option is used when clicking the Map with AI button.  
  
In addition to using the Global settings button, you can also access these
settings by navigating to **Window** -> **Preferences** -> **Connections** ->
**Data Transfer**.

Important

After modifying the **Mapping Rules** settings, you will be prompted to
confirm your changes. Modifying the **Mapping Rules** may result in the loss
of names that were already changed.

### Keyboard Shortcuts¶

The following keyboard shortcuts for easy navigation within the mapping table
area of the **Tables mapping** tab are supported:

Shortcut | Action  
---|---  
`Up` | Move one row up.  
`Down` | Move one row down.  
`Right` | Expand list of source table columns.  
`Left` | Collapse list of source table columns.  
`Space` | Auto-assigns the target.  
`Del` | Sets mapping type to skip.  
  
### Step 4 Extraction settings¶

After setting up your table mappings, the next step is to define how the data
will be extracted from the source. The **Extraction settings** tab offers
various options to optimize this process. Configure these settings to suit
your specific data transfer requirements and press **Next**.

![](../images/dt/dt_migration/data-transfer-extraction-settings.png)

Option | Description  
---|---  
**Maximum threads** | Defines the number of threads to be used for data transfer.  
**Extract type** | Use **Multiple queries** if database doesn't support resultset scrolling. You can also set the **Segment Size** value when this option is selected.  
**Open new connection(s)** | If checked, a new connection is established, ensuring data transfer does not affect other database operations.  
**Select row count** | Enables a progress bar to display data migration status.  
**Fetch size** | Indicates the number of rows fetched per server round trip, affecting extraction performance.  
  
### Step 5 Data load settings¶

![](../images/dt/dt_migration/data-transfer-data-load-settings.png)

After configuring the extraction settings, you'll need to specify how the data
will be loaded into the target database. The **Data load settings** tab
provides a range of options to control this part of the process. Adjust the
settings according to your needs and then press **Next**.

**Data load settings** tab defines how the extracted data will be pushed to
the target. The following options are available.

Option | Description  
---|---  
**Transfer auto-generated columns** | Fill in or skip columns marked with the "autogenerated" status. Some databases accept values in such columns, while others will throw a syntax error.  
**Truncate target table(s) before load** | Select this checkbox only if you want all the data to be cleared from the target table. Be very careful with this option!  
**Disable referential integrity checks during the transfer** | Disabling constraints in the target table. This setting prevents database errors by temporarily disabling the constraints. However, please note that not all databases support this functionality.  
**Replace method** | Read our guide on [Data Import and Replace](../Data-Import-and-Replace/) to learn more about the replacing method option.  
**Log INSERT queries** | Records all `INSERT` queries in the [Query Manager](../Query-Manager/) (disabled by default). This may slow data transfer and increase the size of the Query Manager database.  
**Open new connection(s)** | Use this option to speed up data transfer. If selected, a new connection will be opened and the data transfer will not interfere with other calls to the database where data is being transferred to.  
**Use transactions** | This option allows you to speed up the data transfer and to define the number of rows for each transaction by setting the **Commit after insert of** parameter.  
**Do Commit after row insert** | Performing a commit after a certain number of inserted rows. This setting specifies that a commit operation should be executed after a specified number of rows have been inserted into the table.  
**Use multi-row value insert** | Use multi-row insert with extended values number for higher performance. Database-specific setting.  
**Skip bind values during insert** | This option can drastically increase performance for some drivers like Redshift by skipping a process of binding values and setting them directly, but it opens up a vulnerability to SQL injections. Not recommended if you are not sure of imported file contents.  
**Disable batches** | Select this checkbox if you want to disable the use of batch imports. The import will be made row by row. Enabling this function will show all import errors, but make the import process slower.  
**Ignore duplicate rows errors** | In the import process, if a database encounters a duplicate key from the import row in the target table, such errors are ignored, and the import operation continues without failure.  
**Use bulk load** | Bypasses transaction settings and loads the entire dataset using the native tool provided by the database.  
**Open table editor on finish** | If selected, the table editor is to be opened when data transfer is finished.  
**Show finish message** | If selected, a notification message will be shown when the transfer is finished.  
**Send results by E-Mail** | Sends data transfer results by E-Mail on finish. Read our guide to [using email to transfer data](../Data-transfer-email/) to learn more.  
  
### Step 6 Confirm¶

![](../images/dt/dt_migration/data-transfer-confirm.png)

The final step before initiating the data transfer is the **Confirm** tab.
This tab provides a summary of all configurations set up in the previous
steps. It serves as a last review to ensure all settings are correct.

Here is a table summarizing the configurations:

Option | Description  
---|---  
**Source Container** | Displays the source container from which data will be pulled.  
**Source** | Shows the specific source within the container.  
**Target Container** | Displays the target container to which data will be pushed.  
**Target** | Shows the specific target within the container.  
**Source Settings** | Summarizes settings related to data extraction from the source.  
**Target Settings** | Summarizes settings related to data loading into the target.  
  
These settings are final and cannot be changed at this stage. If all
configurations are correct, click **Finish** to start the data transfer.

Tip

You can save these configurations for future use and create a task related to
the data transfer operation by selecting **Save[task](../Task-Management/)**.
This option consolidates your settings into a reusable task.

Upon clicking **Proceed** , the data transfer process will initiate.

### Step 7 Export completion notification¶

If there are no errors, you will see a notification window indicating the
successful completion of the export task. You can continue working with your
database during the export process, as it will be performed in the background.

Back to top

