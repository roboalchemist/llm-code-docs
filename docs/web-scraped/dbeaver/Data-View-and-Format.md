# Source: https://dbeaver.com/docs/dbeaver/Data-View-and-Format/

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
      * Data view and format  [ Data view and format  ](./) Table of contents 
        * Data presentation 
          * Table and Record views 
          * Hints 
        * Formatting data 
          * Value display formats 
          * Data transform 
          * Complex data types 
          * Customizing numeric and date formats 
          * Customizing boolean values 
            * Text based mode 
            * Icon based mode 
        * Row coloring 
          * Coloring rows by value 
          * Coloring rows by data types 
          * Advanced coloring options 
            * Gradient coloring 
            * Regular expression 
          * Reset coloring 
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

  * Data presentation 
    * Table and Record views 
    * Hints 
  * Formatting data 
    * Value display formats 
    * Data transform 
    * Complex data types 
    * Customizing numeric and date formats 
    * Customizing boolean values 
      * Text based mode 
      * Icon based mode 
  * Row coloring 
    * Coloring rows by value 
    * Coloring rows by data types 
    * Advanced coloring options 
      * Gradient coloring 
      * Regular expression 
    * Reset coloring 

  1. [DBeaver](/docs/dbeaver)
  2. [Data Editor](/docs/dbeaver/Data-Editor)
  3. Viewing and editing data

# Data view and format

In DBeaver you can customize how your data is displayed to suit your needs.

## Data presentation¶

You can switch between data presentations based on your needs.

**Button** | **View** | **Description**  
---|---|---  
![Grid button](../images/ug/Grid-button.png) | **Grid** | Displays data in a grid, similar to Excel.  
![Text button](../images/ug/Text-button.png) | **Text** | Shows data in plain text format.  
![XML button](../images/ug/xml-button.png) | **XML** ![](../images/commercial.png) | Shows XML data (for XML tables only).  
  
Tip

Use `CTRL+~` to toggle between views.

### Table and Record views¶

By default, data appears in the **Table view** , where rows and columns are
organized like a spreadsheet.

![](../images/ug/Structurize.png)

To switch to **Record view** , which displays columns as rows and hides extra
rows in a single **Value** column:

  * Select a cell and click **Record** ![Record button](../images/ug/Record-button.png) on the bottom toolbar.
  * Select a cell and press `Tab`.
  * Or, right-click a cell and select **Layout - > Record**.

You can also transform all columns into rows. To do this, select all rows (for
example, with `Cmd`+` A`), right-click a cell and select **Layout - >
Record**.

![](../images/ug/Record-view.png)

Tip

You can navigate through rows using the navigation buttons ![Navigation
buttons](../images/ug/Navigation-buttons.png) at the bottom or the arrow keys
on your keyboard. For more details on navigating through rows, see
[Navigation](../Navigation/).

### Hints¶

You can use hints to get additional context for data and understand
relationships without opening additional panels. Hints are available for both
**cells** and **column headers** :

  * **Column header hints** display metadata about the entire column, like key constraints or read-only status.
  * **Cell hints** provide information about individual values, such as foreign key references or array sizes.

![](../images/ug/data-editor-hints.png)

To toggle hints:

  1. Right-click any cell.
  2. Go to **Hints**.
  3. Select the specific hints you want to display.

Tip

You can configure where hints apply - globally, for a specific datasource, or
for an individual entity. Use the **Configure for** menu to select the desired
level.

**Cell hint** | **Displayed information**  
---|---  
**Foreign keys** ![](../images/commercial.png) | Shows linked table information.  
**Table references** | Adds a button in the cell to navigate to related table.  
**Arrays** | Displays the number of elements in the array.  
**Binary data** | Shows the size of the binary block in bytes.  
**Timezone** | Indicates the timezone for date or time values.  
**SRID** | Displays the Spatial Reference System Identifier for geometric or geographic data.  
**Column hint** | **Displayed information**  
---|---  
**Keys information** | Displays information about imported and exported keys in column headers.  
**Column status** | Highlights read-only columns in column headers. For more details on table status indicators, see [Data Editor](../Data-Editor/#table-status-indicators).  
  
For foreign key hints, you can customize what is displayed. Right-click a cell
with primary key, go to **Hints - > Dictionary title for {column name}
referenced row ...**, where you can:

  * Select specific columns to show in the hint.
  * Set a custom expression for descriptions.
  * Define a delimiter to separate values.

Note

Hints perform additional queries to display detailed information. For
databases where minimizing resource usage is important, you can disable
metadata reading. For more details, see [Disabling metadata queries](../Data-
Editor/#disable-metadata-queries).

## Formatting data¶

You can transform how data is presented in DBeaver.

### Value display formats¶

**Format** | **Description**  
---|---  
**Display (default)** | Shows data with standard formatting applied for clarity.  
**Editable** | Displays data in a plain, editable text format, useful for quick changes.  
**Database native** | Presents data as it appears in the database without additional formatting, reflecting the raw values.  
  
To switch between these formats:

  1. Right-click a cell.
  2. Go to **View/Formats - > Value display format**.
  3. Select format.

### Data transform¶

  1. Right-click a cell and choose **View/Format - > Set {column name} transform**.
  2. Select a format (e.g., URL, Binary, Numeric, Geometry) and click **OK**.
  3. The settings window opens where you can adjust additional options based on the data type:

**Format** | **Description** | **Settings**  
---|---|---  
**URL** | Displays the value as a clickable URL. | \- **URL pattern** : Set a URL template using `${value}` as a placeholder.  
**Numeric** | Converts a string value into a numeric type. | \- **Type** : Choose a numeric type.  
|  | \- **Lenient** : Ignore conversion errors and display the original value instead of showing an error.  
**Binary** | Displays the value as binary data. | \- **Binary format** : Choose a format.  
|  | \- **Character encoding** : Set encoding.  
**Geometry** | Shows data as spatial geometry. | \- **SRID** : Set the spatial reference system ID.  
|  | \- **Invert coordinates** : Switch the order of coordinates.  
|  | \- **MySQL-compatible format** : Enable compatibility with MySQL geometry.  
  4. To reset the format to default, right-click any cell and select **View/Format - > Set {column name} transform -> Default**.

Tip

To format multiple columns at once, open the **Transforms** window: 1\. Right-
click any cell and select **View/Format - > Columns transforms...**. 2\. In
the window that opens, adjust the formatting settings for multiple columns at
the same time.

### Complex data types¶

For structured data (like objects, structures or arrays), you can expand them
into columns.

  * Right-click a cell and choose **View/Format - > Show complex columns structure**.

![](../images/ug/Structurize.png)

### Customizing numeric and date formats¶

You can specify how numeric and time-based data is formatted globally or for a
specific database:

  1. Right-click a cell, then select **View/Format - > Data formats**.
  2. In the Properties window, adjust settings:
     * To apply changes to the current database, check **Datasource "[Connection name]" settings**.
     * To apply globally, choose **Global settings**.

Info

For more details, see [Managing data formats](../Managing-Data-Formats/).

### Customizing boolean values¶

You can choose between text-based or icon-based presentations for boolean
values.

Go to **Window - > Preferences -> User Interface -> Miscellaneous**.

To toggle between **text-based** and **icon-based** modes, select the desired
**Display mode**.

#### Text based mode¶

You can customize the following options:

  1. Update labels under the **Label** column or use presets.
  2. Align text to the left, center, or right.
  3. Change colors using the **Color** column or reset to the themeâs default.
  4. Adjust the font style (normal, **bold** , or _italic_).

![](../images/ug/Data-boolean-presentation-preferences.png)

#### Icon based mode¶

In this mode, you can only adjust alignment.

## Row coloring¶

### Coloring rows by value¶

You can highlight rows with the same value in a specific column:

  1. Right-click a cell, then select **View/Format - > Set row color for {column name = value}**.
  2. Choose a color in the palette window and exit the window.

![](../images/ug/Colored_rows.png)

### Coloring rows by data types¶

You can color values based on their data type.

  1. To enable or disable data tyoe colorizing, right-click any cell, select **View/Format** , and check or uncheck **Colorize Data Types**.
  2. To customize colors for each data type, go to **Window - > Preferences -> User Interface -> Appearance -> Colors and Fonts**.

Note

Primary key and foreign key columns arenât colorized.

### Advanced coloring options¶

For advanced options, choose **View/Format - > Row colors...**. In this window
you can set multiple conditions, define ranges, or even use regular
expressions.

![](../images/ug/Row-coloring-customization.png)

Section | Description  
---|---  
**Fields list (left panel)** | A large list that shows all the available fields (e.g., `id`, `city`, `name`, etc.) that you can customize.  
**Configuration panel (right panel)** | The area where you configure settings for the selected field. It contains:  
**Settings (top-right field)** | Displays current rules or conditions applied to the selected column. Use the buttons on the right to:  
| \- **Add** a new condition ![Add Row Button](../images/ug/Add-new-row-
button.png).  
| \- **Delete** an existing condition ![Delete Row
Button](../images/ug/Delete-connection-type-button.png).  
**Range/gradient** | Enables gradient coloring for a value range.  
**Apply colors to this column only** | Restricts the color rule to the selected column.  
**Operator** | Defines the comparison operator for conditions. Options include: `=`, `<>`, `>`, `>=`, `<`, `<=`, `ILIKE`, `LIKE`, `NOT LIKE`, and `REGEX`.  
**Value(s)** | Sets the value or range for the condition. To define a range, enable the **Range/Gradient** checkbox and specify the minimum and maximum values (e.g., `1` to `10`).  
**Background** | Allows you to choose colors for the cell/s background.  
**Foreground** | Sets the text color inside the cells.  
  
#### Gradient coloring¶

You can use gradients to highlight data within a range. For example, you can
highlight `Id` values from `1` to `10` with a gradient transitioning.

  1. Right-click on the cell and go to **View/Format - > Row colors...**.
  2. Select the column containing `Id`.
  3. In the **Values** section, set the range (e.g., from `1` to `10`).
  4. Choose a **Background** color for the start and end of the range.
  5. Use **Foreground** to set the text color inside the cells, if needed.
  6. Press **OK** to save your settings.

#### Regular expression¶

You can use regular expressions to highlight specific rows.

  1. Right-click on the cell and go to **View/Format - > Row colors...**.
  2. Set the **Operator** to **REGEX**.
  3. In the **Value** field, enter the desired regular expression.
  4. Choose a **Background** color.
  5. Use **Foreground** to set the text color inside the cells, if needed.
  6. Press **OK** to save your settings.

### Reset coloring¶

If you want to remove a specific highlight:

  * Right-click the cell again and select **View/Format - > Clear color for {column name = value}**.
  * Or right-click the cell again and select **View/Format - > Reset all row coloring**.

Back to top

