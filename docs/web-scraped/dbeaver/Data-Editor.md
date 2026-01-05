# Source: https://dbeaver.com/docs/dbeaver/Data-Editor/

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
    * Data Editor  [ Data Editor  ](./) Table of contents 
      * Top toolbar 
      * Left sidebar 
      * Right sidebar 
      * Bottom toolbar 
      * Table status indicators 
      * Column context menu 
      * Cell context menu 
      * Additional features 
        * Disable metadata queries 
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

  * Top toolbar 
  * Left sidebar 
  * Right sidebar 
  * Bottom toolbar 
  * Table status indicators 
  * Column context menu 
  * Cell context menu 
  * Additional features 
    * Disable metadata queries 

  1. [DBeaver](/docs/dbeaver)
  2. Data Editor

# Data Editor

The Data editor appears:

  * as the **Data** tab of the [Database Object Editor](../Database-Object-Editor/), which is only available for tables and views;
  * as the **Results** tab when you run a custom SQL query in [SQL Editor](../SQL-Editor/).

The Data editor allows to view and edit data of a database table or view. The
central part of the Data editor is the data grid. The editor also provides top
toolbar, bottom toolbar, left sidebar, right sidebar and a filter field:

Info

To configure how data is displayed and edited, see [Data Editor
preferences](../Data-Editor-preferences/).

![](../images/ug/Data-Editor-with-markup.png)

Tip

To learn about ways to navigate data in the table data, see
[Navigation](../Navigation/) article.

## Top toolbar¶

The top toolbar contains the following buttons:

Button | Name | Description  
---|---|---  
![](../images/filters/data_filters/Remove-all-filters-orderings.png) | **Remove all filters/orderings** | Removes all filters and orderings applied to the data in the filter field.  
![](../images/ug/Filter-button.png) | **Custom Filters** | Opens the Result Set Order/Filter Settings window. See [Data Filters](../Data-Filters/) article for more information.  
![](../images/filters/data_filters/Save-filter-settings-for-current-object.png) | **Save filter settings** | See [Save filter settings](../Data-Filters/#save-filter-settings) for more details.  
![](../images/ug/History-navigation.png) | Forward and backward - history navigation buttons | Navigate forward and backward in the Data Editor history, see the [history section](../Navigation/#history) of our article for more information.  
  
## Left sidebar¶

The left sidebar contains the following tabs:

Button | Name | Description  
---|---|---  
![](../images/ug/Grid-button.png) | **Grid** | Switches to the grid view of data.  
![](../images/ug/Text-button.png) | **Text** | Switches to the plain text view of data.  
![](../images/ug/spatial-button.png) | **Spatial** | Switches to the spatial view. For more details, see the [GIS data](../Working-with-Spatial-GIS-data/) article.  
![](../images/ug/Chart_button.png) | **Chart** | Switches to the chart view. For more details, see [Charts](../Managing-Charts/).  
![](../images/ug/Record-button.png) | **Record** | \- Same as pressing `Tab`  
\- Switches the positions of rows and columns so that the columns appear as
rows, and the rows hide in one **Value** column. See details in the [Table vs.
Record Views section](../Data-View-and-Format/#table-and-record-views) of our
article.  
  
## Right sidebar¶

The right sidebar contains the following tabs (see the [Panels](../Panels/)
for more information):

Button | Name | Description  
---|---|---  
![](../images/ug/panels-button.png) | **Panels** | Opens panels on the right side of the Data Editor.  
![](../images/ug/Calc-button.png) | **Calc** | Opens the result cells calculation panel (`SUM`, `MAX`, `AVG`, etc.).  
![](../images/ug/Grouping-button.png) | **Grouping** | Opens grouping panel window tools.  
![](../images/ug/Metadata-button.png) | **Metadata** | Opens Metadata panel.  
![](../images/ug/References-button.png) | **References** | Opens References panel.  
![](../images/ug/Value-button.png) | **Value** | Opens Value Viewer.  
![](../images/ug/Result-details-button.png) | **Result Details** /**Query Trace** | Opens the Result Details or Query Trace panel depending on the database.  
  
Note

The **Result Details** panel is compatible with specific databases such as
[BigQuery](../Database-driver-BigQuery/), while the **Query Trace** panel is
available for [Cassandra](../Cassandra/) and Yugabyte CQL. For guidance on
enabling **Query Trace** , see [Query Trace Panel article](../Query-Trace-
Panel/).

## Bottom toolbar¶

The bottom toolbar provides the following buttons:

Button | Name | Description  
---|---|---  
![](../images/ug/Refresh-button.png) | **Refresh** | Refreshes the whole results set, including all items that are not visible on the screen, while its dropdown option allows to customize the refresh frequency over a specific period.  
![](../images/ug/Save-button-Data-Editor.png) | **Save** | Saves all unsaved changes to the data such as adding, duplicating, deleting rows, inline editing of values. See [the Data Viewing and Editing](../Data-Viewing-and-Editing/) article for information.  
![](../images/ug/Cancel-button-Data-Editor.png) | **Cancel** | Discards all unsaved changes to the data.  
![](../images/ug/Edit-cell-value-button.png) | **Edit cell value in separate dialog/editor** | Opens the cell in focus for editing in a separate editor or dialog box. See details in the [Cell Editor section](../Data-Viewing-and-Editing/#cell-editor) of our article.  
![](../images/ug/Add-new-row-button.png) | **Add new row** | Adds a new empty row below the current row, see details in the [Adding, Copying and Deleting Rows section](../Data-Viewing-and-Editing/#rows-manipulation) of our article.  
![](../images/ug/Duplicate-current-row-button.png) | **Duplicate current row** | Copies the current rows and pastes the copy below the current row, see details in [Adding, Copying and Deleting Rows section](../Data-Viewing-and-Editing/#rows-manipulation) of our article.  
![](../images/ug/Delete-current-row-button.png) | **Delete current row** | Colors the rows in focus in red to mark them for deletion, see details in the [Adding, Copying and Deleting Rows section](../Data-Viewing-and-Editing/#rows-manipulation) of our article.  
![](../images/ug/Move-to-first-row-button.png) | **Move to first row** | Moves the focus (highlighting) from the current to the first row of the table.  
![](../images/ug/Move-to-previous-row-button.png) | **Move to previous row** | Moves the focus (highlighting) from the current to the previous row of the table.  
![](../images/ug/Move-to-next-row-button.png) | **Move to next row** | Moves the focus (highlighting) from the current to the next row of the table.  
![](../images/ug/Move-to-last-row-button.png) | **Move to last row** | Moves the focus (highlighting) from the current to the last row of the table.  
![](../images/ug/Fetch-all-rows-button.png) | **Fetch all data** | Fetches the whole result set making it ready for display. See the [Scrolling Results Page section](../Navigation/#scrolling-results-page) of our article.  
![](../images/ug/Configure-columns-visibility-icon.png) | **Configure** | Opens a menu with settings.  
![](../images/ug/fetch-size-window.png) | **Result-set fetch size** | Displays the initial fetch number of rows in the result set on loading or refreshing.  
![](../images/ug/Calculate-total-rows-button.png) | **Calculate total row count** | Calculates the total number of rows in the table.  
  
To learn how many rows the table data contains, click the **Calculate total
row count** button. The number of rows appears in a status field next to the
button: ![](../images/ug/Calculate-rows-button.png)

Note

Some of these buttons may be disabled and may not work if you are using a
read-only connection, connecting to a read-only database or if you see the
result of a complex query, such as joining two or more tables.

## Table status indicators¶

When working in the Data Editor grid, you might notice icons in the top left
corner of each table. These icons are tools to help you quickly understand why
you may encounter limitations while attempting to edit data in specific
tables. Here is a guide to understanding what each icon means and how it can
help you:

Icon | Indicator | Description  
---|---|---  
![](../images/ug/no-unique-key-found.png) | No unique key was found. Data modification is not possible. | The table lacks a unique key, restricting editing.  
![](../images/ug/unique-key-found.png) | PRIMARY KEY `column_name` | A unique key enables editing of the table.  
![](../images/ug/virtual-unique-key-found.png) | VIRTUAL PRIMARY KEY `column_name`. | A virtual key enables editing of the table. For more information about virtual keys, see [Virtual keys](../Virtual-Keys/).  
![](../images/ug/table-metadata-not-found.png) | Table metadata not found. Data edit is not possible. | Unavailable metadata prevents editing of the table.  
![](../images/ug/read-only-connection.png) | Read-only connection. | A read-only connection prevents any edits.  
  
Tip

In addition to table status indicators, you can highlight column headers. See
[Hints](../Data-View-and-Format/#hints) for details.

## Column context menu¶

Each column has a context menu, accessed by clicking the downward arrow button
![](../images/ug/downward-arrow.png), providing different filter options.

![](../images/ug/column-submenu.png)

## Cell context menu¶

Every cell in the table data also has a context menu â right-click the cell
to open the menu. The context menu provides the following items:

Menu Item | Description  
---|---  
**Copy** | Copies the content of the current cell or column to the clipboard.  
**Advanced Copy** | Opens advanced copy submenu that allows copying data with preset formatting parameters.  
**Paste** | Pastes the copied content to the cells in focus.  
**Advanced Paste** | Pastes several values delimited with a tabulation or line break starting from the selected cell.  
**Delete** | Deletes the row that has the cell in focus.  
**NOTE** : In fact, when users click **Delete** , the system only highlights
the red row while the actual deletion happens when users click **Save**.  
**Edit** | Opens a submenu enabling inline editing. See the [Data Viewing and Editing](../Data-Viewing-and-Editing/) article.  
**Order** | Displays a submenu that allows to specify ordering criteria for the data. The submenu contains the most common ordering options that can be applied to the column in focus. See details in [Data Filters](../Data-Filters/) article. By default, DBeaver orders data by sending a request to the server (the Server-side results ordering checkbox selected). To order data on the client side using DBeaver's internal algorithm, clear the checkbox.  
**Filter** | Displays a submenu that allows to specify filter criteria for the data. The submenu contains the most common filters that can be applied to the cell in focus. See details in [Data Filters](../Data-Filters/) article. By default, DBeaver filters data by sending a request to the server (the Server-side results ordering checkbox selected). To filter data on the client side using DBeaver's internal algorithm, clear the checkbox.  
**View/Format** | Opens a submenu that provides options for formatting and modifying the view of data. See the [Data View and Format](../Data-View-and-Format/) article.  
**Navigate** | Opens a submenu that helps users to navigate through the table data. See the [Navigation](../Navigation/) article.  
**Layout** | Changes the layout of data, see the [Data View and Format](../Data-View-and-Format/#table-and-record-views) article.  
**Export data** | Opens the Data Transfer wizard that guides you through the steps to export data to a selected format. See the [Data Transfer](../Data-transfer/) article.  
**Note** : The system exports the whole result set including records that are
not visible on the screen and preserves all applied data filters and ordering.  
**Generate SQL** | Opens a submenu where you can select the type of SQL query to generate. See the [SQL Generation](../SQL-Generation/) article.  
**Generate Mock Data** | Opens Mock Data Generator. See the [Mock Data Generation in DBeaver](../Mock-Data-Generation-in-DBeaver/) article.  
**Logical structure** | Opens a submenu allowing you to write virtual column expressions, including use of functions, namespaces, and special variables like `row` and `table`. See the article about [Virtual column expressions](../Virtual-column-expressions/).  
**Open with** | Opens the data in external applications like Excel or a web browser.  
**Toggle result panel** | Opens Value panel on the right side of the Data Editor.  
**Refresh** | Refreshes the whole results set including all items that are not visible on the screen.  
  
## Additional features¶

### Disable metadata queries¶

If you want to improve performance and save money in databases where you pay
for each query, you can stop reading the metadata queries in the Data Editor.
This means the editor would not automatically ask for information about tables
and columns.

To enable, navigate to **Window - > Preferences -> Connections -> Metadata**
and check the option **Do not read tables information in SQL and data
editors**.

  * **Benefits** :

    * Makes the Editor work faster because it runs fewer queries.
    * Saves money in databases where each query costs you, by only running queries that you start yourself.
  * **Disadvantages** :

    * You won't have auto-completion or other tools that need metadata.
    * Results from queries are read-only. To check if modifications are possible, look for an indicator in the top left corner of the table grid. For more information on indicators, see Table status indicators.

Tip

This setting is particularly valuable for managing databases, such as:

  * [Amazon Athena](../Database-driver-Amazon-Athena/)
  * [Amazon Redshift Serverless](../Database-driver-Amazon-Redshift/)
  * [Amazon Timestream](../Database-driver-Amazon-Timestream/)
  * [AWS DynamoDB](../AWS-DynamoDB/)
  * [AWS Keyspaces](../AWS-Keyspaces/)
  * [Databricks](../Database-driver-Databricks/)
  * [Google BigQuery](../Database-driver-BigQuery/)
  * [Google Cloud Spanner](../Database-driver-Google-Cloud-Spanner/)
  * [Snowflake](../Snowflake/)

In general, any cloud database may charge for metadata queries, even when
you're just browsing schema or table lists.

Back to top

