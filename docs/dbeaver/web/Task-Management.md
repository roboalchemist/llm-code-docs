# Source: https://dbeaver.com/docs/dbeaver/Task-Management/

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
    * Task management  [ Task management  ](./) Table of contents 
      * Database Tasks view 
        * Toolbar actions 
        * Context menu actions 
      * Create tasks 
        * Task setup 
      * Manage tasks 
        * Add, edit, or delete tasks 
        * Run a task 
          * Run tasks from the command line 
        * Adjusting task configurations 
        * Scheduling tasks 
        * Set task timeout 
      * Customize the Database Tasks view 
        * Group tasks 
        * Configure columns 
        * Folders 
          * Move tasks between folders 
          * Delete a folder 
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

  * Database Tasks view 
    * Toolbar actions 
    * Context menu actions 
  * Create tasks 
    * Task setup 
  * Manage tasks 
    * Add, edit, or delete tasks 
    * Run a task 
      * Run tasks from the command line 
    * Adjusting task configurations 
    * Scheduling tasks 
    * Set task timeout 
  * Customize the Database Tasks view 
    * Group tasks 
    * Configure columns 
    * Folders 
      * Move tasks between folders 
      * Delete a folder 

  1. [DBeaver](/docs/dbeaver)
  2. Tasks

# Task management

Note

This feature is available in Community, [Enterprise](../Enterprise-Edition/),
[Ultimate](../Ultimate-Edition/) and [Team](https://dbeaver.com/docs/team-
edition/) editions only.

Use tasks to save and reuse configurations for database tools like data
transfer or import/export. Tasks help you automate routine actions and run
them with one click. You can create tasks from tool wizards or from the main
menu, group them in folders, and manage them in a dedicated view.

## Database Tasks view¶

All your tasks are stored in the **Database Tasks** view. Use it to review,
organize, and run tasks when you need them.

From this view, you can:

  * Add, edit, or delete tasks.
  * See task information.
  * Run tasks manually.
  * Schedule tasks.

![](../images/ug/tools/task_manager/task-view.png)

To open it:

  * Go to **Database - > Tasks -> Database Tasks**,
  * Or click **Open Tasks view** (![](../images/ug/tools/task_manager/open-database-tasks-button.png)) from the task creation wizard.

### Toolbar actions¶

The toolbar includes quick-access buttons:

Icon | Name | Description  
---|---|---  
![](../images/ug/tools/task_manager/schedule-task-button.png) | **Open scheduler** | Configure time-based task runs.  
![](../images/ug/Refresh-button.png) | **Refresh** | Reload the task list.  
![](../images/ug/tools/task_manager/group-tasks-by-category.png) | **Group by category** | Toggle grouping by category (Common/Database-specific).  
![](../images/ug/tools/task_manager/group-tasks-by-type.png) | **Group by type** | Toggle grouping by type (Export, Import, etc.).  
![](../images/ug/tools/task_manager/run-task-button.png) | **Run task** | Start the selected task manually.  
![](../images/ug/tools/task_manager/view-menu-button.png) | **View menu** | Open options to create a new task, add a folder, or delete items.  
  
Tip

You can also right-click a task in the list to access these actions.

### Context menu actions¶

Right-click any task in the **Database Tasks** view to access task actions:

Action | Description  
---|---  
**Run task** | Execute the selected task immediately.  
**Edit task** | Open the task editor.  
**Create new task...** | Open the task creation wizard.  
**Copy** | Copy task name to clipboard.  
**Delete** | Remove the selected task.  
**Create new task folder** | Create a folder to organize tasks.  
**Rename folder** | Rename a selected folder.  
**Scheduler** | Access task scheduling settings.  
**Group tasks by category** | Enable grouping by user-defined categories.  
**Group tasks by type** | Enable grouping by task type.  
**Copy** | Copy task info to clipboard.  
**Configure columns** | Choose which columns to display in the view.  
**Auto-size columns** | Adjust column widths to fit content.  
  
## Create tasks¶

You can create a new task from:

  * Database Tasks view: Go to **Database - > Tasks -> Database Tasks**
  * [Menu bar](../Application-Window-Overview/#menu-bar): Go to **Database - > Tasks -> Create New Task**
  * [Toolbar](../Application-Window-Overview/#toolbar): click arrow next to **Open Tasks view** (![](../images/ug/tools/task_manager/open-database-tasks-button.png)) and choose **Create new task**.

Note

The toolbar is customizable. For further information, refer to [Toolbar
Customization](../Toolbar-Customization/) article.

  * [Database Navigator](../Database-Navigator/): Right-click a database object, then select **Tools - > Create new task**

  * [Properties editor](../Properties-Editor/): Right-click a database object, then choose **Tools - > Create new task**

Alternatively, you can save tasks directly from tools like [Data
Transfer](../Data-transfer/), [Data Compare](../Data-compare/), [Back up and
Restore](../Backup-Restore/), [Mock Data generator](../Mock-Data-Generation-
in-DBeaver/). Just configure the tool, click **Save task** , fill in the task
details, and save.

### Task setup¶

  1. Open the task creation wizard.

![](../images/ug/tools/task_manager/task-creation-wizard.png)

  2. Fill in the task properties and choose the tool you want to automate:

Field | Description  
---|---  
**Name** | Enter a unique name for the task.  
**Description** | (Optional) Add a short description to help identify the task later.  
**Task folder** | (Optional) Select a folder to organize tasks.  
**Task type** | Choose the tool you want to automate. Select from the list of task types:  
  
| **Common** : Available for any database type.  
| **Database-specific** : Available only for supported database types.  
**Max execution time (in seconds)** | (Optional) Set a time limit for task execution. Default is `300`.  
  
Note

The list of available task types depends on the databases listed in **Database
Navigator**. Database-specific tasks only appear if their corresponding
database (like PostgreSQL, MySQL, etc.) is present.

  3. Click **Next**.

  4. Complete the task-specific configuration wizard.
  5. Save the task when you're done.

## Manage tasks¶

To manage tasks open the Database Tasks view.

![](../images/ug/tools/task_manager/task-view.png)

### Add, edit, or delete tasks¶

You can manage tasks using the toolbar or by right-clicking a task in the
**Database Tasks** view.

Available actions:

Action | How to use it  
---|---  
**Add** | Click the **View Menu** button (![](../images/ug/tools/task_manager/view-menu-button.png)) in the view's toolbar and select **Create new task...** , or right-click to open the context menu and choose **Create new task...**  
**Edit** | Select a task, then right-click and choose **Edit task**  
**Delete** | Select a task, then right-click and choose **Delete**  
  
Warning

Deleted tasks canât be restored.

### Run a task¶

  1. Select a task in the **Database Tasks** view.
  2. Right-click it to open the context menu.
  3. Click **Run task**.
     * Alternatively, use **Run task** button (![](../images/ug/tools/task_manager/run-task-button.png)) on the viewâs toolbar.

#### Run tasks from the command line¶

You can run saved tasks using the DBeaver [command line](../Command-Line/)
interface. Use the `-runTask` parameter like this:

    
    
    -runTask "@projectName:taskName"
    

Tasks run in the background without keeping the client open.

If your workspace has only one project, you can omit the `@projectName:` part.

On Windows, use the `dbeaverc` executable (or the legacy name `dbeaver-cli`)
to run tasks.

Tip

Add the `-nosplash` [parameter](../Command-Line/#system-parameters) to skip
the splash screen.

### Adjusting task configurations¶

The process of editing a task is similar to the process of creating a task.

By double-clicking on a task or right-click and choose **Edit task** , the
task edit wizard will be opened. In this wizard, you can:

  * Change the task properties.
  * Change the file format, either output for an export task or input for an import task.
  * Alter the set of objects for data transfer.
  * Adjust any export/import configuration.

After modifying the task settings, click the **Save task** button. This button
is located on the left side of the task configuration wizard.

### Scheduling tasks¶

Note

This feature is available in [Lite](../Lite-Edition/),
[Enterprise](../Enterprise-Edition/), [Ultimate](../Ultimate-Edition/) and
[Team](https://dbeaver.com/docs/team-edition/) editions only.

You can schedule tasks for later/regular execution. See the [Task
Scheduler](../Task-Scheduler/) article.

### Set task timeout¶

You can set how long a task can run before it stops automatically. This helps
avoid cases where one long or stuck task prevents the next ones from running.

To configure it:

  1. In the Database Tasks view, select or create a task.
  2. Click the **Timeout** button (![](../images/ug/tools/task_manager/timeout-button.png)).

Note

The **Timeout** button is enabled after you finish setting up the task.

  3. Choose a preset duration (1 min, 5 min, 30 min, 1 hour) or set a custom time.

## Customize the Database Tasks view¶

You can personalize how tasks are displayed in the **Database Tasks** view.
Group them by type or category, and choose which columns are visible.

### Group tasks¶

To organize your task list:

  1. Right-click anywhere in the task list
  2. Select **Group tasks by category** or **Group tasks by type** from the context menu

Tip

You can enable both grouping options at the same time.

### Configure columns¶

To show or hide columns:

  1. Right-click anywhere in the task list
  2. Click **Configure columns**
  3. Select the columns to show or hide

![](../images/ug/tools/task_manager/task-view-configure-dialog.png)

### Folders¶

You can organize tasks into folders. To create one:

  1. Right-click in the **Database Tasks** view and select **Create new task folder**.
  2. Enter a unique name and choose a project.

#### Move tasks between folders¶

You can:

  * Open a task for editing, click **Back** , and change the folder.
  * Drag and drop tasks between folders directly in the view.

#### Delete a folder¶

To remove a folder, right-click it and select **Delete**.

Warning

All tasks inside will also be deleted. Deleted tasks canât be restored.

Back to top

