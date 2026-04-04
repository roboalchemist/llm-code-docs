# Source: https://dbeaver.com/docs/dbeaver/Visual-Query-Builder/

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
    * Visual query builder  [ Visual query builder  ](./) Table of contents 
      * Getting started 
      * Visual Query Builder interface 
      * Executing queries 
      * Query configuration 
        * Tables 
        * Columns 
          * Selecting columns in the workspace 
          * Using the Columns tab in the Query settings 
            * Adding and removing columns 
            * Adjusting column order 
            * Aliases 
            * Grouping and aggregation 
        * Where condition 
          * Adding and removing conditions 
        * Joins 
          * Modifying joins 
            * Context menu 
            * Joins tab 
        * Sorting 
          * Adding and removing sorting conditions 
        * Miscellaneous 
        * Disable Visual Query Builder 
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
  * Visual Query Builder interface 
  * Executing queries 
  * Query configuration 
    * Tables 
    * Columns 
      * Selecting columns in the workspace 
      * Using the Columns tab in the Query settings 
        * Adding and removing columns 
        * Adjusting column order 
        * Aliases 
        * Grouping and aggregation 
    * Where condition 
      * Adding and removing conditions 
    * Joins 
      * Modifying joins 
        * Context menu 
        * Joins tab 
    * Sorting 
      * Adding and removing sorting conditions 
    * Miscellaneous 
    * Disable Visual Query Builder 

  1. [DBeaver](/docs/dbeaver)
  2. SQL Editor

# Visual query builder

Note

This feature is available in [Lite](../Lite-Edition/),
[Enterprise](../Enterprise-Edition/), [Ultimate](../Ultimate-Edition/) and
[Team](https://dbeaver.com/docs/team-edition/) editions only.

The **Visual Query Builder** in DBeaver is a visual tool that helps you build
and understand SQL queries in complex databases. It lets you work with your
database in a visual way, making it easy to see how tables connect and how
data flows between them. This tool is useful when you want to create queries
without writing SQL code yourself. The Visual Query Builder in DBeaver
automatically converts your visual selections into SQL scripts, making it
easier to explore and work with your data.

## Getting started¶

To start using **Visual Query Builder** , click the **Builder** button in the
SQL Editor for the desired database.

![](../images/visual_query_builder/vqb-getting-started.png)

Tip

You can switch between the **SQL Editor** and the **Visual Query Builder**
easily. If you write a valid SQL query in the [SQL Editor](../SQL-Editor/), it
will show up in the Visual Query Builder. The same way, any query you build
visually will appear in the SQL Editor.

## Visual Query Builder interface¶

The **Visual Query Builder** interface consists of the following sections:

  * **Workspace** : This area displays all the tables, columns, and their relationships that you have added to your query.

  * **Palette** : The **Palette** shows tools to interact with tables, and the section below displays the tables you have already selected and moved into the **Visual Query Builder** workspace.

  * **Query settings** window: This section displays the **Query** settings, where you can configure columns, conditions, joins, sorting, and other settings related to your query.

![](../images/visual_query_builder/visual-query-builder-interface.png)

## Executing queries¶

The **Visual Query Builder** works in a similar way to the **SQL Editor** when
you run queries.

  * Click the **Execute SQL statement** button ![](../images/visual_query_builder/query_builder_run_icon.png) to run your query. You will see the results in the same tab.
  * You can also use the **Execute SQL statement in new tab** button ![](../images/visual_query_builder/query_builder_run1_icon.png) to run the query and open the results in a new tab.

You will find both buttons on the vertical toolbar of the **Visual Query
Builder** , giving you easy ways to run your queries and view the results.

Note

The toolbar is customizable. For more information, see [Toolbar
Customization](../Toolbar-Customization/).

## Query configuration¶

The **Visual Query Builder** allows you to easily add tables, set query
conditions, and customize how your query results are displayed using the
**Query settings** available at the bottom of the workspace. These settings
provide options for filtering, sorting, selecting columns, and setting join
conditions, giving you full control over your query results.

To open/close the **Query settings** window, click the **QUERY** button
![](../images/visual_query_builder/query-button.png).

Tip

You can toggle the visibility of the generated SQL query text by using the
**Show/hide generated SQL query text** button
![](../images/visual_query_builder/query_builder_run_icon.png) on the right
side of the window or by pressing `Ctrl+B` (`âB` for macOS).

Below are the sections explaining how to work with the **Visual Query
Builder** capabilities in more detail:

### Tables¶

You can add tables to the **Visual Query Builder** workspace using one of the
following methods:

  1. **Drag-and-Drop** : Drag the tables from the [Database Navigator](../Database-Navigator/) into the **Visual Query Builder** workspace.

  2. **Using the Palette** :

     * In the **Pallete** menu, select **Add Table** from the **Tools** section.
     * Click on the **Visual Query Builder** workspace and choose the necessary table.

### Columns¶

By default, all columns (`*`) from the tables you add are selected. To
customize use the following methods:

#### Selecting columns in the workspace¶

  * Click the checkboxes next to the column names in the table within the **Visual Query Builder** workspace to include or exclude columns from your query.
  * The SQL script will update automatically in the SQL script area, reflecting your selections.

![](../images/visual_query_builder/selecting-columns-in-the-workspace.png)

Tip

Click **Hide unused columns** button (![](../images/visual_query_builder/hide-
unused-columns.png)) in the toolbar to collapse columns youâre not using.
Keys stay visible even when this option is on.

#### Using the Columns tab in the Query settings¶

  * Select the **Columns** tab in the **Query settings**. In this tab, you can specify details related to the columns:

Option | Description  
---|---  
**Column** | Select the desired column for your `SELECT` statement from the dropdown list.  
**Alias** | Provide a custom name for the column.  
**Grouping** | Define grouping for aggregated data.  
**Aggregation** | Select an aggregation function (e.g., `COUNT`, `AVG`, `MAX`, `MIN`, `SUM`) to process the selected data.  

##### Adding and removing columns¶

  * **Adding a Column** : Press the **Add** button ![](../images/visual_query_builder/query_builder_add_icon.png). A new column will be added to the query. Click on the first cell in the **Column or Expression** column and select a column from the dropdown list that appears.

![](../images/visual_query_builder/using-the-columns-tab-in-the-query-
settings.png)

  * **Removing a Column** : To remove a column, click on the row containing its name and press the **Remove** button ![](../images/visual_query_builder/query_builder_remove_icon.png).

##### Adjusting column order¶

Use the **Move Up/Down** buttons
![](../images/visual_query_builder/query_builder_move_icon.png) to change the
display order of columns in the result table. This will adjust the sequence in
which the columns appear in your query.

##### Aliases¶

You can set a user-friendly name for your columns by clicking on a cell in the
**Alias** column and entering the desired name. This alias will be reflected
in the SQL script area and the final query result.

##### Grouping and aggregation¶

  * If you want to apply a grouping condition, click the checkbox in the **Grouping** column row. This action will update your expression automatically. Other columns will become aggregated, and if there are no other columns, a `COUNT(*)` expression will be added.

  * You can select different aggregation functions from the dropdown list or manually enter your preferred function in the cell.

Tip

When you remove columns, they are also removed from the grouping expression.
Any newly added columns will be automatically included in the grouping
expression.

### Where condition¶

You can add conditional expressions using the **Where** tab, which allows you
to manage query conditions by filtering your query results.

Select the **Where** tab in the **Query settings**. In this tab, you can
specify details related to the columns:

Setting | Description  
---|---  
**Left Operand** | Defines the left operand of the conditional expression. This can be a column or a numeric value.  
**Operation** | Specifies the comparison rule (e.g., `=`, `>`, `LIKE`) to apply between the left and right operands.  
**Right Operand** | Defines the right operand of the expression, which can be a column, numeric value, or string.  
  
![](../images/visual_query_builder/vqb-conditions.png)

#### Adding and removing conditions¶

  * **Adding a conditional expression** : Click the **Add** button ![](../images/visual_query_builder/query_builder_add_icon.png) on the right side of the tab. This action will create a new condition row, and a default `WHERE` clause will be automatically added to the SQL script area.

  * **Removing a conditional expression** : To remove an existing condition, select the row containing the condition you wish to delete and click the **Remove** button ![](../images/visual_query_builder/query_builder_remove_icon.png) on the right side of the tab.

### Joins¶

When you add a table to the **Visual Query Builder** workspace, the joins are
created automatically based on existing relationships:

  * **Automatic Joins** : If the table you add has an existing relationship with one or more tables already in the workspace, the join will be displayed automatically.

  * **Inner join** behavior: If the table does not have any existing relationship with the tables already in the workspace, the system will create a `SIMPLE JOIN` with the first table you added to the workspace.

Tip

You can disable automatic joins based on foreign keys in the Miscellaneous tab
by unchecking the **Auto-create joins according to foreign keys** option. For
more information, see Miscellaneous section.

#### Modifying joins¶

To modify joins in the **Visual Query Builder** , use either the **context
menu** or the **Joins tab**.

##### Context menu¶

Right-click on the connection line between tables in the workspace to open a
context menu. Youâll see join options labeled with their types (`Left Join`,
`Right Join`, `Inner Join`, or `Full outer Join`). For more join options, use
the Joins tab.

![](../images/visual_query_builder/vqb-joins-in-context-menu.png)

##### Joins tab¶

Open the **Joins** tab in the **Query settings** to manage and adjust join
settings for all tables in the workspace. In this tab, you can work with the
following options:

Options | Icon | Description  
---|---|---  
**Table/Conditions** |  | Displays the tables involved in the join along with the join conditions.  
**Type** |  | Allows you to modify the join type (e.g., `Simple`, `Inner`, `Left`, `Right`, `Full`, `Cross`, `Natural`).  
**Alias** |  | Lets you define a custom name for the join.  
**Add Column/Expression** | ![](../images/visual_query_builder/query_builder_add_icon.png) | Adds a new join condition. Select a row in **Table/Conditions** to enable this button in the right-side menu. Also available in the context menu.  
**Remove** | ![](../images/visual_query_builder/query_builder_remove_icon.png) | Removes the selected join condition. Select a row in **Table/Conditions** to enable this button in the right-side menu. Also available in the context menu.  
  
To change a join condition:

  * select the cell under **Table/Conditions** and edit the expression directly.
  * select the cell and click the three dots button to open the **Edit value** dialog.

![](../images/visual_query_builder/vqb-joins.png)

### Sorting¶

You can set the order of rows in the result table.

Select the **Sorting** tab in the **Query settings**. In this tab, you can
specify details related to the columns:

Setting | Description  
---|---  
**Conditions or Expressions** | Click on the first cell in this column to display a drop-down list of all available columns. Select the column you want to sort by clicking on its name.  
**Order** | Defines whether the selected column should be sorted in ascending or descending order.  
  
![](../images/visual_query_builder/vqb-sorting.png)

#### Adding and removing sorting conditions¶

  * **Adding a sorting condition** : Click the **Add** button ![](../images/visual_query_builder/query_builder_add_icon.png) on the right side of the tab. This action will create a new sorting row, and a default `ORDER BY` expression will be automatically added to the SQL script area.

  * **Removing a sorting condition** : To remove an existing sorting condition, select the row containing the condition you wish to delete and click the **Remove** button ![](../images/visual_query_builder/query_builder_remove_icon.png) on the right side of the tab.

### Miscellaneous¶

You can configure additional settings in the **Miscellaneous** tab.

Setting | Description  
---|---  
**Add table aliases** | Enable or disable the automatic generation of aliases for tables by selecting this check-box.  
**Use fully qualified table names** | Use full table names (including schema) by selecting this check-box, which disables auto-completion for table names.  
**Auto-create joins according to foreign keys** | Enable or disable the automatic creation of joins based on foreign key relationships.  
**Autosave on SQL-editor switch** | Enable autosave when switching between SQL editors by selecting this check-box.  
  
![](../images/visual_query_builder/vqb-miscellaneous.png)

### Disable Visual Query Builder¶

You can disable the **Visual Query Builder**. When disabled, the **Builder**
tab in the SQL Editor is hidden.

  1. Go to **Window - > Preferences -> SQL Editor**
  2. In the **SQL Presentations** section, check the box **Disable Visual Query Builder**
  3. Click **Apply and Close**

Tip

You can also disable the Visual Query Builder in [admin preferences](../Admin-
Manage-Preferences/#sql-editor-settings).

Back to top

