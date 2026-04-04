# Source: https://dbeaver.com/docs/dbeaver/Data-Viewing-and-Editing/

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
      * Data viewing and editing  [ Data viewing and editing  ](./) Table of contents 
        * Inline editing 
        * Cell Editor 
          * Data format handling 
          * Specialized handling of CLOB and BLOB data types 
          * Setting cell value to NULL 
          * Setting cell value to default 
        * Rows manipulation 
        * Copying and pasting cells 
          * Basic copy 
          * Advanced copy 
          * Basic paste 
          * Advanced paste 
        * Saving and previewing changes 
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

  * Inline editing 
  * Cell Editor 
    * Data format handling 
    * Specialized handling of CLOB and BLOB data types 
    * Setting cell value to NULL 
    * Setting cell value to default 
  * Rows manipulation 
  * Copying and pasting cells 
    * Basic copy 
    * Advanced copy 
    * Basic paste 
    * Advanced paste 
  * Saving and previewing changes 

  1. [DBeaver](/docs/dbeaver)
  2. [Data Editor](/docs/dbeaver/Data-Editor)
  3. Viewing and editing data

# Data viewing and editing

DBeaver provides tools for data editing and viewing within its [Data
Editor](../Data-Editor/). It supports inline editing in the grid view for
quick data changes and a cell editor for more intricate entries, including a
multi-line text. Users can manage rows by adding, copying, or deleting them
and can utilize copy-paste functions for data transfer. Detailed information
on these features and the steps for saving and reviewing changes are provided
in the following sections.

## Inline editing¶

Inline editing refers to the process of modifying content directly within a
cell in a table. To initiate inline editing, users have several options:

  * Double-click the desired cell.
  * Click the cell to focus on it, then press `Enter`.
  * Right-click the cell and select **Inline edit** from the context menu.

Once in inline editing mode, the cell becomes editable, allowing the user to
modify its value.

Tip

If your table doesn't have unique keys, DBeaver lets you create [virtual
keys](../Virtual-Keys/) to edit data.

## Cell Editor¶

The Cell Editor in DBeaver is a tool designed for detailed data editing within
individual cells. To access the Cell Editor, follow either of these methods:

  * Right-click on the desired cell and select **Edit - > Edit cell** from the context menu.
  * Click the cell to focus, then either press `Shift+Enter` or click the **Edit cell** button (![](../images/ug/Edit-cell-value-button.png)) located in the bottom toolbar.

Note

The toolbar is customizable. See [Toolbar Customization](../Toolbar-
Customization/) article.

### Data format handling¶

DBeaver manages a variety of data formats, and for most cells, activating the
Cell Editor displays a property window:

![](../images/ug/Edit-cell-window.png)

This window is divided into two main sections:

  * **Column Info** : Provides detailed properties of the column.
  * **Value** : Enables users to modify the cell's value. After making changes, click **Save** to apply them. For extended editing, use the **Open Editor** option for a separate editor tab.

### Specialized handling of CLOB and BLOB data types¶

In addition to general data formats, DBeaver offers specialized support for
`CLOB`/`BLOB` data types:

  * **Editing CLOB/BLOB data** : Editing cells containing `CLOB`/`BLOB` data in the Cell Editor opens the content in a new tab, allowing for comprehensive editing, particularly useful for large data objects.
  * **Saving/Loading BLOB values** : Users can save and load `BLOB` values to and from external files, aiding in the management of binary data like images and large text files.
  * **Image display in BLOB Columns** : DBeaver automatically renders images stored in `BLOB` columns (formats like `gif`, `png`, `jpeg`, `bmp`) within the interface, streamlining the process of viewing image data.
  * **Value View panel** : To efficiently browse images in `BLOB` columns, users can activate the value view panel by pressing `F7`.

### Setting cell value to NULL¶

To set a cell's value to `NULL`, right-click on the cell and choose **Edit - >
Edit cell -> Set to NULL**.

### Setting cell value to default¶

To set a cell's value to its default, right-click on the cell and select
**Edit - > Set to default** from the context menu. The default value for the
field, if predefined, will be displayed in parentheses next to this option.

## Rows manipulation¶

Refer to the table below for instructions on adding, copying, and deleting
rows in DBeaver's Data Editor.

Action | Description | Button/Image  
---|---|---  
**Adding rows** | To add a new, empty row, click the **Add row** button in the bottom toolbar. This inserts a row below the focused row. Populate the new row via inline editing or separate cell editor. | ![Add Row Button](../images/ug/Add-new-row-button.png)  
**Copying rows** | To duplicate rows, select the rows and click the **Duplicate row** button. The duplicates will appear below the original rows. | ![Duplicate Row Button](../images/ug/Duplicate-current-row-button.png)  
**Deleting rows** | For deleting rows, select them and click the **Delete current row** button. Rows marked for deletion turn red and are removed upon saving. | ![Delete Row Button](../images/ug/Delete-current-row-button.png)  
  
## Copying and pasting cells¶

This section outlines the procedures for copying and pasting cell data within
DBeaver.

### Basic copy¶

To copy the contents of one or more cells to the clipboard in a TAB-delimited
format, you can use the shortcut ` Ctrl+C`. Alternatively, right-click on the
cell or selection of cells and select **Copy** from the context menu. This
copied content can then be pasted into spreadsheet editors like Excel.

### Advanced copy¶

For more control over the copy process, DBeaver offers an advanced copy
option. This feature allows users to include column names and row numbers,
configure delimiters, and choose value formats during the copy operation.
Activate this feature by pressing `Ctrl+Shift+C` or by selecting **Advanced
Copy - > Advanced Copy** from the context menu after right-clicking on the
selected cells. The Advanced Copy settings window provides various options:

Field | Description  
---|---  
**Copy header** | Includes the column names as headers in the copied data.  
**Copy row numbers** | Adds the row number for each row in the copied data.  
**Quote cell values** | Encloses each cell value in quotes.  
**Always quote values** | Forces quoting of all cell values, regardless of the need.  
**Copy as HTML** | Formats the copied data as HTML, suitable for web publishing.  
**Value display format** | Determines how the copied data will be displayed.  
**Column Delimiter** | Character or sequence used to separate columns in the copied data.  
**Row Delimiter** | Character or sequence used to separate rows in the copied data.  
**Quote Character** | Character used to quote cell values if quoting is enabled.  
  
In addition to these options, users can perform a **Save as** operation in
various formats by selecting **Advanced Copy** from the context menu after
right-clicking on the selected cells, which can be further configured for each
format. Here are the additional options available:

Option | Description  
---|---  
**Copy as CSV** | Copies the data in Comma-Separated Values format.  
**Copy as DbUnit** | Copies the data in the DbUnit dataset format.  
**Copy as HTML** | Copies the data in Hypertext Markup Language format for web use.  
**Copy as JSON** | Copies the data in JavaScript Object Notation format.  
**Copy as Markdown** | Copies the data in Markdown format suitable for documentation.  
**Copy as SQL** | Copies the data as SQL INSERT or UPDATE commands.  
**Copy as Source code** | Copies the data in a format ready to use in source code.  
**Copy as TXT** | Copies the data as plain text.  
**Copy as XML** | Copies the data in eXtensible Markup Language format.  
  
To further refine how each format is copied, select **Configure 'Copy as'
commands...** from the context menu. This opens a configuration window where
you can set the specific copying behavior for each format, such as delimiter
choice, quoting options, and more, ensuring the copied data meets the
requirements of different use cases and target applications.

Tip

Admin can disable the ability to copy data using the registry or configuration
file. For details, see [Admin preference restrictions](../Admin-Preference-
Restrictions/#registry-and-configuration-file-parameters).

### Basic paste¶

To paste copied content, press `Ctrl+V` when focusing on a cell. DBeaver
intelligently handles the pasting process, applying necessary data type
conversions to fit the destination cell's format.

### Advanced paste¶

DBeaver's **Advanced Paste** feature caters to scenarios requiring the
insertion of multiple cells or complex data structures. It can be accessed
through the context menu or by using the shortcut `Ctrl+Shift+V`. When
activated, the following options are presented in a dialog:

Feature | Description  
---|---  
**Insert multiple rows** | Allows for the pasting of data into multiple rows at once.  
**Ignore quotes** | Disregards quotation marks when parsing pasted values.  
**Insert NULLs** | Allows for pasting the `NULL` values.  
**NULL value mark** | Defines the symbol or text that represents a `NULL` value.  
  
These settings provide additional control over how data is pasted, ensuring
that data is inserted correctly and efficiently, especially in bulk operations
or when special data considerations are necessary.

## Saving and previewing changes¶

In DBeaver, data modifications are committed to the database when saved. To
confirm changes:

  * Click the **Save** button ![](../images/ug/Save-button-Data-Editor.png) in the bottom toolbar.
  * To revert modifications, click the **Cancel** button ![](../images/ug/Cancel-button-Data-Editor.png).

Tip

The **Save** and **Cancel** buttons are enabled only after making edits and
moving to another cell.

To validate changes before saving, preview the SQL script:

  * Click the dropdown arrow next to the **Save** button ![](../images/ug/Save-button-Data-Editor.png).
  * Choose **Generate Script**. The Preview Changes window will display the SQL script for review and copying if required.

![](../images/ug/Preview-changes-window.png)

Back to top

