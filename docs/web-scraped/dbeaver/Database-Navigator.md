# Source: https://dbeaver.com/docs/dbeaver/Database-Navigator/

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
      * Database Navigator  [ Database Navigator  ](./) Table of contents 
        * Navigation 
          * Browse database objects 
          * Filter database objects 
          * Group database objects in folders 
          * Simple and advanced view 
          * Highlight object from editor 
          * Show all databases 
        * Toolbar 
        * View menu 
        * Context menu 
        * Navigator preferences 
        * Additional capabilities 
          * Drag and drop from Database Navigator 
          * Shortcuts 
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

  * Navigation 
    * Browse database objects 
    * Filter database objects 
    * Group database objects in folders 
    * Simple and advanced view 
    * Highlight object from editor 
    * Show all databases 
  * Toolbar 
  * View menu 
  * Context menu 
  * Navigator preferences 
  * Additional capabilities 
    * Drag and drop from Database Navigator 
    * Shortcuts 

  1. [DBeaver](/docs/dbeaver)
  2. [Navigation](/docs/dbeaver/Database-Navigator)
  3. Database Navigator

# Database Navigator

**Database Navigator** is the main tool in DBeaver for working with database
structure and data. It shows a tree of objects - like connections, schemas,
tables, and views - based on your database type.

![](../images/ug/Database-Navigator.png)

Tip

If you donât see Database Navigator, go to **Window - > Database Navigator**
to open it.

## Navigation¶

### Browse database objects¶

Use the tree in **Database Navigator** to view and explore databases. Each
connection shows its own set of objects - schemas, tables, views, procedures,
and more. Expand a connection to access its contents. Click any object to open
it in the appropriate editor or viewer.

### Filter database objects¶

Use the filter bar above the navigator tree to search and filter database
objects.

Start typing to highlight matching items. The filter supports partial matches
and updates results instantly.

You can also filter using the view options or context menu.

![](../images/ug/filter-database-object.png)

Tip

The filter applies only to expanded nodes. For details, see [Filter database
objects](../Filter-Database-Objects/).

### Group database objects in folders¶

Use folders to organize connections:

  * Right-click in the tree and select **Create - > New Folder** to add a new folder.
  * Drag and drop connections or objects into folders to group them.

![](../images/ug/group-database-objects-in-folders.png)

Tip

You can also create subfolders within existing folders to further organize
your database objects.

### Simple and advanced view¶

Switch between **Simple** , **Advanced** , or **Custom** view to control how
much detail is shown in **Database Navigator**.

Use this option to simplify the tree or show all available objects, depending
on your needs.

![](../images/ug/simple-and-advanced-view.png)

Info

For details, see [Simple and advanced view](../Simple-and-Advanced-View/).

### Highlight object from editor¶

Use **Link with editor** button ![](../images/ug/Link-with-Editor-icon.png) to
highlight the object currently opened in the [SQL Editor](../SQL-Editor/) or
[Data Editor](../Data-Editor/) in **Database Navigator**.

When enabled, **Database Navigator** selects and scrolls to the schema that
contains the active object.

Toggle this option from the top toolbar of the **Database Navigator**.

![](../images/ug/link-with-editor.png)

### Show all databases¶

Enable **Show all databases** in the connection settings to display all
databases in **Database Navigator**.

Some databases (such as [PostgreSQL](../Database-driver-PostgreSQL/)) may show
only the active database or a limited set of schemas by default.

![](../images/ug/show-all-databases.png)

## Toolbar¶

The toolbar contains buttons for the most basic and frequently used commands:

Icon | Menu item | Description  
---|---|---  
![](../images/ug/Collapse-All-icon.png) | **Collapse All** | Collapses all tree items to the root level.  
![](../images/ug/Link-with-Editor-icon.png) | **Link with editor** | Syncs the selected item in active editor with schema in the Database Navigator.  
![](../images/ug/show-all-connections-button.png) | **Show all connections/Show connected only** | Filters the tree to show either all connections or only connected ones.  
![](../images/ug/filter-mode-button.png) | **Filter mode** | Cycles through object filter levels: connections, catalogs and schemas, or individual objects. [Read more](../Filter-Database-Objects/)  
![](../images/ug/View-menu-icon.png) | **View menu** | Opens additional options. Read more  
  
## View menu¶

Click the **View Menu** button (![](../images/ug/View-menu-icon.png)) in the
upper-right corner of the **Database Navigator** panel to open additional
options.

Icon | Menu item | Description  
---|---|---  
![](../images/ug/new-connection-wizard-button.png) | **New Database Connection** | Opens the connection wizard.  
![](../images/ug/driver-manager-button.png) | **Driver Manager** | Opens the driver manager for configuring drivers.  
| **Active Project** | Switches between projects.  
![](../images/ug/Create-new-folder-button.png) | **New Folder** | Creates a new folder in the current project.  
![](../images/ug/Collapse-All-icon.png) | **Collapse All** | Collapses all nodes in the tree.  
![](../images/ug/Link-with-Editor-icon.png) | **Link with editor** | Syncs the selected object with the active editor tab.  
![](../images/ug/Configure-columns-visibility-icon.png) | **Preferences** | Opens DBeaver settings.  
![](../images/ug/Refresh-button.png) | **Refresh Projects** | Reloads all projects and folders.  
  
Tip

Use the **View Menu** for project-level actions and layout options - itâs
different from the context menu, which changes based on the selected object.

## Context menu¶

Right-click an object in the **Database Navigator** tree to open its context
menu. The menu shows different items depending on the database type and
selected object.

Menu item | Description  
---|---  
**Create** | Creates objects like connection, folder, and other.  
**Open folder** | Opens the selected folder in a new view.  
**Copy** | Copies the selected object.  
**Paste** | Pastes the copied object into the selected folder or node.  
**Delete** | Deletes the object.  
**Warning** : This action removes the object from the database or file system.
It can't be undone.  
**Rename** | Opens a dialog to rename the object.  
**Refresh** | Refreshes the selected node and its children.  
**Connect** | Connects to the database.  
**Invalidate/Reconnect** | Reconnects if the connection is broken.  
**Disconnect** | Disconnects from the database.  
**SQL Editor** | Opens new script, last edited script for this connection.  
**Edit connection** | Opens the connection settings.  
**Connection view** | Lets you switch between **Simple** , **Advanced** , or **Custom** views. [Read more](../Simple-and-Advanced-View/)  
**View`[object]`** | Opens the object in a viewer.  
**Edit`[object]`** | Opens the object in an editor.  
**Create new`[object]`** | Starts creating a new object.  
**Filter** | Opens filtering options for the selected object:  
\- Hide `[object]`  
\- Show only `[object]`  
\- Configure `[object]` filter  
\- Toggle filter  
\- Clear filter  
[Read more](../Configure-Filters/)  
**Copy Advanced Info** | Copies the objectâs full name.  
**Read data in SQL console** | Opens a console to preview data from the object.  
**Compare/Migrate** | Opens the [export](../Data-compare/) wizard.  
**Generate SQL** | Opens options to generate SQL statements:  
\- `SELECT`  
\- `INSERT`  
\- `UPDATE`  
\- `DELETE`  
\- `MERGE`  
\- `DDL`  
**Export Data** | Opens the [export](../Data-export/) wizard.  
**Import Data** | Opens the [import](../Data-import/) wizard.  
**Tools** | Opens tools like [Dashboards](../Dashboards/), [Tasks](../Task-Management/), [Backup and restore](../Backup-Restore/).  
  
Tip

The available menu items change depending on the selected object and database.

## Navigator preferences¶

You can control how the **Database Navigator** behaves and displays objects.
These settings are available in **Window - > Preferences -> User Interface ->
Navigator**.

Setting name | Description  
---|---  
**Show connection host name** | Show target database host name or tunnel host name next to the connection name  
**Show objects description** | Shows object (table, column, etc.) description next to it  
**Show statistics info** | Show statistics (e.g. table size) on the right side of navigator  
**Show action icons** | Show action icons for database elements  
**Show placeholders for special folders** | Show special folders (e.g. Scripts) even if they were not created yet  
**Folders first** | Show folders before regular elements  
**Show child count in navigator** | Display the number of children for expanded folders in the navigator tree  
**Order elements alphabetically** | Order navigator nodes (not folders) alphabetically  
**Case-insensitive alphabetical sorting** | Order navigator nodes without case sensitivity, for example, `A,a,B,b`  
**Set connection color for all elements** | Color all elements according to connection type, otherwise set color only for connection node itself  
**Show object modifiers in tree** | Show object modifiers (e.g. column data type) in the tree right after the name  
**Show tooltips** | Show tooltips in navigator views  
**Show file contents in tooltips** | Show file (e.g. SQL script) contents in tooltips  
**Show grid lines in lists** | Displays grid lines between rows and columns in navigator and editor lists for better readability  
**Double-click on node** | \- **Open Properties** \- opens the object properties tab   
\- **Expand / Collapse** \- expands or collapses the selected node in the tree  
**Double-click on connection** | \- **Open Properties** \- opens the connection properties   
\- **Connect / Disconnect** \- connects or disconnects from the database  
\- **Open SQL Editor** \- opens the SQL Editor  
\- **Open new SQL Editor** \- opens a new SQL Editor tab  
\- **Expand / Collapse** \- expands or collapses the connection node  
**Default editor page** | \- **Last opened** \- opens the editor on the page that was active last time   
\- **Properties** \- opens the Properties page  
\- **Data** \- opens the Data tab  
\- **Diagram** \- opens the Diagram tab  
**Expand navigator tree on connect** | Expand the Navigator tree for active elements on connect  
**Save database navigator filter** | Saves object filter specified in the database navigator view between application restarts  
**Elements fetch size** | Children elements fetch size for long lists. Rest of elements can be read by double clicking on the last element  
**Restore navigator state up to depth** | Restore navigator state on startup up to depth  
  
Tip

You can also configure these settings through preference files without opening
the app. For details, see [Manage application preferences](../Admin-Manage-
Preferences/).

## Additional capabilities¶

### Drag and drop from Database Navigator¶

You can drag objects from **Database Navigator** into the **SQL Editor** to
quickly add their names to a query.

Note

After you drop an object, it stays selected in the editor. If you run the
query right away, only the selected part runs - which often causes an error
because it's not a complete query. Click in the editor to deselect the object
before running the query.

### Shortcuts¶

You can navigate, filter, and edit objects faster with keyboard shortcuts.

Info

For a full list, see [Shortcuts](../Shortcuts/#database-navigator).

Back to top

