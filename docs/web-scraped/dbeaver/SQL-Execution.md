# Source: https://dbeaver.com/docs/dbeaver/SQL-Execution/

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
      * SQL execution  [ SQL execution  ](./) Table of contents 
        * Result tabs 
          * Naming 
          * Pinning 
          * Detaching 
        * SQL Expression Evaluation 
        * Row Count 
        * Query Export 
        * Parameters and variables 
          * Parameters 
            * Common 
            * Scripts 
            * Delimiters 
          * Variables 
          * Dynamic parameters binding 
        * Miscellaneous 
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

  * Result tabs 
    * Naming 
    * Pinning 
    * Detaching 
  * SQL Expression Evaluation 
  * Row Count 
  * Query Export 
  * Parameters and variables 
    * Parameters 
      * Common 
      * Scripts 
      * Delimiters 
    * Variables 
    * Dynamic parameters binding 
  * Miscellaneous 

  1. [DBeaver](/docs/dbeaver)
  2. [SQL Editor](/docs/dbeaver/SQL-Editor)
  3. Query execution

# SQL execution

You can execute one query, a highlighted portion of a script, or a whole
script. You can execute them using the following:

  * shortcut key combinations (see details further in this article)
  * tools in the main toolbar:

![](../images/ug/Execute-buttons.png)

Note

Toolbar is customizable. See [Toolbar Customization](../Toolbar-
Customization/#sql-editor-toolbar-customization)

  * context menu (right-click the query):

![](../images/ug/execute-context-menu.png)

  * DBeaver main menu:

![](../images/ug/Execute-main-menu.png)

To execute a query under the cursor or selected text, press `Ctrl+Enter` or
right-click the query and click **Execute** -> **Execute SQL Statement** on
the context menu. You can do the same using the main toolbar or main menu:
**SQL Editor** -> **Execute SQL Statement**. This executes the SQL query under
the cursor or selected text and fills the results pane with the query results.

To execute a query under the cursor in a separate tab, press `CTRL+\ ` or
right-click the query and click **Execute** -> **Execute SQL in new tab** on
the context menu. The same can be done using the main toolbar or the main
menu: **SQL Editor** -> **Execute SQL in new tab**. This executes the SQL
query under the cursor or selected text and creates a new results tab.

To execute the whole script, press `Alt+X` or click **Execute** -> **Execute
SQL Script** on the context menu or **SQL Editor** -> **Execute SQL Script**
on the main menu or in the main toolbar. This executes all queries in the
current editor (or selected queries) as a script. DBeaver parses queries one
by one using a statement delimiter (â;â by default) and executes them
consecutively. For these settings, see the Delimiter preferences section.

To execute the script natively, press `Alt+N` or click **Execute** ->
**Execute SQL Script natively** on the context menu or **SQL Editor** ->
**Execute SQL Script natively** on the main menu or in the main toolbar. Upon
activation, a setup wizard is launched, which allows you to configure the
parameters for script execution before the script is launched in the native
client like PLSQL, MySQL, or SQLPlus. The results are displayed in a text
field in the format of console output. It is handy when functions are not
supported by DBeaver drivers and require more specialized clients or when the
function is weighty, and a faster client is needed.

Note

This function is available for MySQL/Maria, Oracle, and PostgreSQL and may
require additional software installation for each database.

To execute a script opening, each query results in a separate tab, press
`Ctrl+Alt+Shift+X` or click **Execute** -> **Execute Statements In Separate
Tabs** on the context menu or **SQL Editor** -> **Execute Statements In
Separate Tabs** on the main menu or in the main toolbar. It executes all
queries in the script but opens multiple result tabs. Each script query is
executed in a separate thread (that is, all queries are executed
simultaneously).

Important

Executing a massive script with numerous queries can result in unforeseen
problems.

## Result tabs¶

A single query may generate several result sets represented by tabs. These
tabs are linked to the query they are executed from.

  * to close an individual tab, press `CTRL+Shift+\` or middle-click on a tab header
  * to close all tabs expect current, click **Close all result tabs except this** on the context menu of this tab
  * to close all tabs of the desired query, click **Close all result tabs of same query** on the context menu of this tab

### Naming¶

A tab is often named after the primary table of your query. For example, after
executing the following query you will see a single tab called `Album`
(assuming that your database has a table called `Album`):

    
    
    SELECT * FROM Album;
    

If a query has joins or, in other words, has multiple source tables, a `(+)`
is shown right to the table name. The following query will result in a tab
called `Album(+)`:

    
    
    SELECT * FROM Album al, Artist ar WHERE al.AlbumId = ar.ArtistId;
    

Additionally, you can change the name of a given tab via its context menu or
by using a special comment:

    
    
    -- title: DBeaver is cool
    SELECT * FROM Album;
    

In other cases, tabs are named in the form of `Results <**A** > (<**B** >)`,
where:

  * **A** is _an index of query_
  * **B** is _an index of the result set of this query_

### Pinning¶

Tabs can be moved around by dragging them with a mouse and pinned using the
**Pin tab** on the context menu of the desired tab. Pinned tabs are stacked on
the left. They can be moved among other pinned tabs but can't be mixed with
unpinned tabs. Pinned tabs cannot be closed without being unpinned first and
cannot be overwritten by executing a query (by making this tab active).

### Detaching¶

Tabs can be detached from the SQL editor into a separate view using the
**Detach Tab** action found in the context menu of the desired tab. After the
tab is detached, you can rearrange and move it anywhere you want (for example,
you can put two tabs side-by-side for comparison).

Additionally, you can detach it from the application window using **Detach**
found in the context menu of an already detached tab.

After the tab is detached, it's still synchronized with the SQL editor,
meaning you can edit and refresh data as long as the SQL editor that produced
that tab is open. Once you close it, tabs become read-only.

## SQL Expression Evaluation¶

To evaluate an SQL expression, right-click the expression and click **Execute
- > Evaluate SQL expression** on the context menu. This command performs a
query of **SELECT [expression] FROM DUAL** type:

![](../images/ug/Evaluate-SQL-expression.png)

## Row Count¶

If you want to know how many rows an SQL query will produce, you need to apply
the Row Count feature â highlight and right-click the SQL text and then
click **Execute** -> **Select row count** on the context menu:

![](../images/ug/Row-Count.png)

## Query Export¶

It might be useful to export a query if you have a long-running query, and you
do not need to see its results in the results panel. You can directly export
the current query results to a file/table by right-clicking the query and then
clicking **Execute** -> **Export From Query** on the context menu:

![](../images/ug/Export-from-Query.png)

The Data transfer wizard opens. Go through its steps to complete the export of
the query.

![](../images/ug/Data-transfer-window.png)

## Parameters and variables¶

In DBeaver, parameters are used within SQL queries as placeholders, prompting
for user input at query execution.

Info

Variables, defined with the `@set` command or through the [Variables
panel](../Variables-panel/), substitute placeholders with predefined values,
enabling scripts to run without manual input each time.

To customize parameter and variable behavior in DBeaver, access the settings
through **Window - > Preferences -> Editors -> SQL Editor -> SQL Processing**.

### Parameters¶

Setting | Description  
---|---  
**Enable SQL parameters** | Allows the use of named parameters within SQL queries.  
**Anonymous SQL parameters** | Permits the usage of unnamed parameters, enabling the SQL editor to recognize placeholders denoted by the character specified in the **Anonymous parameter mark** field.  
**Anonymous parameter mark** | Sets the symbol for anonymous parameters (default `?`).  
**Named parameter prefix** | Defines the prefix for named parameters (default `:`).  
**Control command prefix** | Specifies the prefix for control commands like `@set` (default `@`).  
**Enable parameters in DDL and`$$..$$` blocks** | Permits the use of parameters within DDL statements and `$$..$$` code blocks.  
**Enable variables** | Activates variable substitution within SQL scripts.  
  
#### Common¶

Setting | Description  
---|---  
**Invalidate connection before execute** | Reconnect the session before each execution to clear a stale or dropped connection.  
**Beep after query finish** | Play a short system sound when the current execution finishes.  
**Refresh active schema after SQL execution** | Read active schema contents after each execution. If a query or procedure changes the active schema, the schema objects are updated in the UI. This option doesnât work if additional metadata read is disabled.  
**Clear output log before execution** | Clear output log before each query/script execution. Suggested if queries produce a very large output log.  
**SQL statement timeout (sec)** | Maximum execution time for a single query in seconds. `0` means no limit. DBeaver passes this value to the JDBC driver as a query timeout.  
  
#### Scripts¶

Setting | Description  
---|---  
**Commit type** | Chooses when to commit during script execution:   
\- **At script end** \- run everything in one transaction, commit at the end.  
\- **After each query (autocommit)** \- commit after every statement.  
\- **After each N-th query** \- commit every N statements; when this option is
selected, an input field appears to set **N**.  
\- **No commit** \- leave the transaction open, so you decide when to commit
or roll back.  
**Error handling** | What to do on the first error:   
\- **Stop + rollback** \- stop and roll back the current transaction.  
\- **Stop + commit** \- stop and keep successful work.  
\- **Ignore** \- continue running the rest of the script.  
**Fetch query results** | For `SELECT` queries fetch and show results in a separate tab.  
**Maximize editor on script execute** | Maximize the editor when you run the script.  
**Show statistics** | Defines whether to show a special tab with statistics about query execution:   
\- **Only when no data**  
\- **For multiple queries with results** \- statistics will be shown even if
`SELECT` statements returned data. If no data is returned, statistics are
displayed anyway.  
\- **Always**  
**Set selection to Statistics tab** | Set selection to the tab containing statistics about query execution.  
**Close included script tab after execution** | Close the editor after a script included with `@include` command has executed.  
  
#### Delimiters¶

Setting | Description  
---|---  
**Statements delimiter** | Character that separates SQL statements.   
Default: `;`.  
**Ignore native delimiter** | Ignore native delimiter and use the default delimiter value from **Statements delimiter** above.  
**Blank line is statement delimiter** | Use blank line as delimiter when parsing statements. Options:   
\- **Always** \- any blank line is treated as a delimiter.  
\- **Never** \- blank lines are not treated as delimiters.  
\- **Smart** \- the editor checks the following lines to decide whether a
blank line should act as a delimiter.  
**Remove trailing query delimiter** | Remove trailing query delimiter when sending statements to the server.  
  
### Variables¶

Define the custom variables with the predefined command or add in the
[Variables panel](../Variables-panel/).

You can create a variable by using the `@set` command followed by the variable
name and its value. For instance:

    
    
    @set actor_name = Mark
    

Once defined, you can include variables in your SQL queries. Use the
`${varname}` or `:varname` syntax to insert the value of a variable into the
script. For example:

    
    
    SELECT * FROM public.actor WHERE first_name = '${actor_name}';
    

Info

For advanced SQL execution, DBeaver extends functionality with context
variables that come from:

  * **CLI** : Command-line interface variables, which offer a hands-off approach for setting up environments. See the [Command-line guide](../Command-Line/#dbeaver-control) for usage details.
  * **Auth properties** : Authentication-related variables that enhance security for credential handling, detailed in the [Authentication properties documentation](../Admin-Variables/).

### Dynamic parameters binding¶

You can define parameters using the `:parameter` syntax, turning parts of the
query into placeholders for values input at execution. For instance:

    
    
    SELECT :first_parameter FROM public.actor WHERE first_name = :second_parameter;
    

Upon every execution of the parameterized query, DBeaver brings up the **Bind
parameter(s)** window.

![](../images/ug/Bind-parameters-dialog.png)

Field | Description  
---|---  
**Value** | Fill in values for each parameter to ensure correct query execution.  
**Hide parameters set in script** | If checked, parameters that you have already given values with the `@set` command will not show up.  
  
Tip

To simplify the process, consider using variables for predefined values before
running the script.

## Miscellaneous¶

To open the definition of the database object currently in focus (under
cursor) in a viewer/editor, press `F4`.

Back to top

