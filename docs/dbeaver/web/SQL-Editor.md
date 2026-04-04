# Source: https://dbeaver.com/docs/dbeaver/SQL-Editor/

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
    * SQL Editor  [ SQL Editor  ](./) Table of contents 
      * Getting started 
      * SQL Editor overview 
        * Script panel 
          * Spelling 
          * Hyperlinks 
          * Highlighting 
        * Toolbar 
        * Results Panel 
          * Multiple results in one tab 
      * Additional features 
        * Active Database 
        * Layout Adjustment 
        * Outline 
        * Error indication 
          * Explain errors with AI 
      * Features summary 
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

  * Getting started 
  * SQL Editor overview 
    * Script panel 
      * Spelling 
      * Hyperlinks 
      * Highlighting 
    * Toolbar 
    * Results Panel 
      * Multiple results in one tab 
  * Additional features 
    * Active Database 
    * Layout Adjustment 
    * Outline 
    * Error indication 
      * Explain errors with AI 
  * Features summary 

  1. [DBeaver](/docs/dbeaver)
  2. SQL Editor

# SQL Editor

With the SQL Editor in DBeaver, you can write and execute multiple SQL scripts
within a single database connection, save them as files, and reuse them later.

## Getting started¶

To start working with the SQL Editor, you have several options:

  1. **Via Database Navigator** :

     * Navigate to your desired database connection in the [Database Navigator](../Database-Navigator/) view.
     * Press `F4` or go to **SQL Editor** -> **Open SQL script** from the main menu, or right-click on the connection and choose **Open SQL script** from the context menu.
     * A **Choose SQL Script** window appears. Click any script to open it in a new tab.
  2. **Open Recent SQL script** :

     * Right-click on your database connection and select **SQL Editor** -> **Recent SQL script** from the context menu or go to **SQL Editor** -> **Recent SQL script** from the main menu. Alternatively use the `Ctrl+Enter` shortcut in the **Database Navigator** view.
     * A **Choose SQL Script** window appears. Click any script to open it in a new tab.
  3. **Create a New SQL Script** :

     * Navigate to **SQL Editor - > New SQL Editor** on the main menu.
     * Press `F3` and click **New Script** in the **Choose SQL Script** window.

Note

SQL Editor for a connection is different from SQL console for a table or view.
Unlike the console, it can save scripts and changes made to them.

You can see all your saved SQL scripts in the [Project Explorer](../Project-
Explorer/) view in the **Scripts** folder.

## SQL Editor overview¶

The SQL Editor contains the Script panel, the Toolbar, and the Result panel.

![](../images/ug/SQL-Editor.png)

Tip

You can open the SQL editor preferences by pressing `Alt+Enter` or right-click
and navigate to **Preferences**.

### Script panel¶

The Script Panel is the primary area where you can write, edit, and manage
your SQL scripts. It provides basic text editing features with the added
benefits of specialized functionalities tailored for SQL development:

#### Spelling¶

The panel includes a spelling checker to identify and highlight misspelled
words, assisting you in maintaining the quality of your scripts. For more
information check out our [article](../Spelling/).

#### Hyperlinks¶

You can press and hold `Ctrl` and at the same time move the mouse over the SQL
text. If DBeaver recognizes some identifier as a table/view name, it presents
it as a hyperlink. You can click the hyperlink to open this object`s editor:

![](../images/ug/SQL-Editor-hyperlink.png)

#### Highlighting¶

DBeaver uses SQL syntax highlighting which depends on the database associated
with the script. Different databases have different sets of reserved keywords
and system functions. For more information, see the relevant section on
highlighting settings in our article on [SQL Code Editor](../SQL-Code-
Editor/).

### Toolbar¶

The toolbar is customizable and contains buttons for commonly used commands.
For more information on customization, see [our article on toolbar
customization](../Toolbar-Customization/#sql-editor-toolbar-customization).

### Results Panel¶

The results panel displays tabs with results in various formats. The tabs
resulting from script execution represent instances of the [Data
Editor](../Data-Editor/). You can create, edit and execute SQL scripts in the
script panel and then see the results in the result tabs.

Tip

You can also visualize query results as charts to explore data patterns. For
details, see [Charts](../Managing-Charts/).

#### Multiple results in one tab¶

You can view and manage multiple query results within a single tab.

![](../images/ug/sql-editor-multiple-tabs.png)

To use the Multiple results feature in the SQL Editor, follow these steps:

  1. **Add Toolbar Item** : Add the **Show multiple results in a single tab** ![](../images/ug/toggle-execution-result-orientation-button.png) to the SQL Editor toolbar. [Read more](../Toolbar-Customization/) on Toolbar customization.

**Alternatively** :

     * Right-click in the SQL Editor window and navigate to **Execute - > Layout -> Show multiple results in a single tab**.
     * Navigate to **SQL Editor** -> **Show multiple results in a single tab**.
  2. **Toggle** : Click the toolbar item to activate multiple query results view.

  3. **View results** :

     * To view multiple results in a single tab, execute queries using the **Execute SQL Script** button ![](../images/ug/execute-button.png).
     * You can collapse some result sets according to your preference by clicking the arrow button ![](../images/ug/toggle-button.png).

Important

When using two or more queries in parallel, exercise caution as this may lead
to client UI freeze, high database server load, or transaction deadlock.

## Additional features¶

### Active Database¶

You can change the connection associated with the current SQL editor or change
the active database/schema, at the same time retaining the SQL text. To change
the connection, press `Ctrl+9` or click the **Active datasource** box on
DBeaver`s main toolbar:

![](../images/ug/Active-Connection-change.png)

The Select Data Source dialog box opens. In the tree of connections, click the
required connection and then click **Select**. To disassociate the SQL Editor
with any connection, click **None** :

![](../images/ug/Connection-change-dialog.png)

To change the active schema, press `Ctrl+0` or click the **Active
Catalog/Schema** box in DBeaver`s main toolbar:

![](../images/ug/Active-Schema-Change.png)

The Choose catalog/schema dialog box opens. In the list of schemas, double-
click the required schema:

![](../images/ug/Schema-change-dialog.png)

If there are many schemas, and they do not fit in the dialog box use the
search field ![](../images/ug/Search-field.png) to find the schema.

To configure the set of columns to be visible for each schema in the dialog
box, click the **Configure columns** button ![](../images/ug/Configure-
columns-visibility-icon.png).

Tip

You can easily associate the SQL Editor with the connection that is currently
in focus in the Database Navigator (the focus can be on any object of the
connection - a table, a folder, etc.) - click the **Link with editor**
![](../images/ug/Link-with-Editor-icon.png) or use the shortcut
`Ctrl+Shift+,`.

### Layout Adjustment¶

You can modify the layout of the SQL Editor by showing/hiding the results
panel and changing the horizontal/vertical position of the panes.

  * To toggle (hide/show) the results panel, press `CTRL+6` or right-click anywhere in the script pane and, on the context menu, click **Layout** -> **Toggle results panel**.
  * To maximize the results panel, press `CTRL+Shift+T`, or double-click the results tab name, or right-click anywhere in the script panel and, on the context menu, click **Layout** -> **Maximize results panel**.
  * To switch between the script panel and the results pane, press `Ctrl+Alt+T` or right-click anywhere in the script panel and, on the context menu, click **Layout** -> **Switch active panel**.

To position both panels horizontally, right-click anywhere in the script panel
and, on the context menu, click **Layout** -> **Horizontal**. To position both
panels vertically, right-click anywhere in the script panel and, on the
context menu, click **Layout** -> **Vertical**.

### Outline¶

You can use the Outline feature in the SQL Editor to get a structured view of
your SQL query.

![](../images/ug/outline-feature-overview.png)

Here's how you can access the Outline:

  * Use the shortcut: `Alt+Shift+Q, O` (on macOS use `â¥âQ O`).
  * Click on the **Toggle Outline** button ![](../images/ug/toggle-outline-button.png) in the SQL Editor bottom toolbar.
  * Select **Panels - > Toggle outline** from the [Script panel](./#script-panel).
  * Select **SQL Editor - > Panels -> Toggle outline** from [Menu bar](../Application-Window-Overview/#menu-bar).

When you open the Outline, it shows a tree structure of your SQL query. This
representation reflects the components of your SQL query and is beneficial for
analyzing and moving through large queries. The relationship between the
Outline and SQL Editor is interactive:

  * The tree selection in the Outline automatically follows the cursor movement in the SQL Editor. This synchronization helps you identify the specific section of the query you are editing within its overall structure.
  * Alternatively, clicking an item in the Outline tree will highlight the corresponding fragment in the SQL Editor, facilitating swift navigation to different parts of your SQL query.

### Error indication¶

The SQL Editor indicates errors during the execution of an incorrect query by
displaying an error icon ![](../images/ug/sql-editor-error-icon.png) to the
left of the query text. Hovering over this icon reveals a tooltip.

  * **Tooltip** : A tooltip will show a detailed list of errors.
  * **Error list** : Moving the mouse over an error in the list will highlight it directly in the query.
  * **Error types** : The SQL Editor detects and displays server issues, semantic errors, and spelling mistakes.

Note

Semantic errors are displayed only when the **Enable semantic analysis**
setting is activated and the database in use is relational. For more
information, see [Query analysis settings](../SQL-Code-Editor/#query-analysis-
settings).

![](../images/ug/sql-editor-error-highlighting.png)

#### Explain errors with AI¶

Note

This feature is available in [Lite](../Lite-Edition/),
[Enterprise](../Enterprise-Edition/), [Ultimate](../Ultimate-Edition/) and
[Team](https://dbeaver.com/docs/team-edition/) editions only.

You can use AI to explain and fix errors after query execution.

Info

For details, see [AI error explanation](../AI-error-explanation/).

## Features summary¶

The SQL Editor offers a variety of advanced features to enhance your scripting
experience.

  * **[SQL templates](../SQL-Templates/)** : Insert pre-defined SQL code snippets for quick access.

  * **[SQL assist and auto-complete](../SQL-Assist-and-Auto-Complete/)** : Complete SQL queries with suggested options as you type.

  * **[AI SQL assistance](../AI-Smart-Assistance/)** : Get AI-powered suggestions for optimizations and best practices.

  * **[SQL formatting](../SQL-Formatting/)** : Automatically format SQL queries to enhance readability.

  * **[SQL execution](../SQL-Execution/)** : Choose from various options to execute SQL queries.

  * **[SQL terminal](../SQL-Terminal/)** : Use a terminal interface for executing SQL commands directly.

  * **[Variables](../Variables-panel/)** : Manage variables within SQL queries. _For information on this feature, see also[Pre-configured Variables](../Pre-configured-Variables/)._

  * **[Query execution plan](../Query-Execution-Plan/)** : Visualize the execution plan of SQL queries for better insight.

  * **[Visual query builder](../Visual-Query-Builder/)** : Use a graphical interface to build SQL queries.

  * **[Script management](../Script-Management/)** : Manage multiple SQL scripts within a single editor interface.

  * **[Client-side commands](../Client-Side-Scripting/)** : Execute client-side commands directly within the editor.

Back to top

