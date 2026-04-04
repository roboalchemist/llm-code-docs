# Source: https://dbeaver.com/docs/dbeaver/Data-export/

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
      * Data export  [ Data export  ](./) Table of contents 
        * Steps to export data 
        * Export parameters 
          * CSV 
          * DBUnit 
          * JSON 
          * Markdown 
          * Source code 
          * SQL 
          * TXT 
          * XML 
          * XLSX 
          * HTML 
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

  * Steps to export data 
  * Export parameters 
    * CSV 
    * DBUnit 
    * JSON 
    * Markdown 
    * Source code 
    * SQL 
    * TXT 
    * XML 
    * XLSX 
    * HTML 

  1. [DBeaver](/docs/dbeaver)
  2. [Data transfer and schema compare](/docs/dbeaver/Data-transfer)
  3. Data transfer

# Data export

DBeaver allows you to export query results or tables. This guide explains the
export process using `CSV` as an example. For details on supported formats,
see [Data Transfer](../Data-transfer/#supported-formats).

Note

Each format may have specific configuration settings that can be adjusted to
meet your needs.

## Steps to export data¶

  1. Select the table or tables you want to export. In the context menu, choose **Export Data**.

![](../images/dt/dt-export_menu.png)

Alternatively, you can also export data from custom SQL query results. To do
that, choose **Export data** in the results context menu.

Tip

You can start the export through AI by sending a short request in AI chat. See
[Data transfer actions](../Data-Transfer-Actions/) for supported commands.

  2. In the window that appears, choose `CSV` and click **Next**.

![](../images/dt/dt-export-format.png)

  3. Set your data extraction options (how the data will be read from the tables). This may affect the extraction's performance. And set the export format option. They are specific to the data format you chose in step 2:

![](../images/dt/dt-options-extract.png)

Setting name | Description  
---|---  
**Maximum threads** | Number of threads used for data extraction.  
**Extract type** | Defines the method of data extraction (`Single query` or `Multiple queries`).  
**Segment size** | The size of data segments to be extracted at a time (active while Multiple queries are selected as an **Extract type**).  
**Open new connection(s)** | Opens a new physical connection for data reading, recommended if you plan to continue working with the database during the export process.  
**Select row count** | Queries row count before performing export to track progress, but may cause performance issues in some cases.  
**Fetch size** | Number of rows the driver retrieves in one batch from the database.  
**Log SELECT queries** | Records all `SELECT` queries in the [Query Manager](../Query-Manager/) (disabled by default). This may slow data transfer and increase the size of the Query Manager database.  
  
Tip

The **Maximum threads** option is active when exporting data from multiple
tables. It is recommended to set the number of threads to match the number of
cores in your computer for optimal performance.

  4. Configure the format settings.

At this stage, you configure the format settings for the output file. These
settings determine how the data will be presented and encoded in the exported
file. For more details on exporter settings, see Export parameters.

![](../images/dt/dt-format-settings.png)

Setting name | Description  
---|---  
**Formatting** | Selects the formatting settings for the exported data. Reed more in the related [article](../Managing-Data-Formats/)  
**Binaries** | Specifies how binary data is represented in the export.  
**Encoding** | Sets the character encoding for the exported file.  
**Value display format** | Chooses the format for displaying values in the export.  
**Configure columns** | Allows you to set which columns to export. Configure the columns to export by clicking **Configure**. In the **Action** column, use the down arrow on a row to toggle between **skip** or **export** for that column/table.   
![](../images/dt/export-skip-columns.png)  
  
Note

The options within the Exporter settings section will vary and provide
specific controls tailored to the format selected for export.

  5. Set options for output files or clipboards.

![](../images/dt/dt-options-output.png)

Tip

You can export files to a remote file system via [Cloud Storage](../Cloud-
Storage/) using the **Browser remote file system** button
![](../images/dt/Browser-remote-file-system-button.png). This feature is
exclusively available to users of the Ultimate Edition, Team Edition, and
CloudBeaver PRO versions.

  6. Review what you want to format and which format you will export. You can also save all your settings as a task in this step or change the task variables:

![](../images/dt/dt-export-final.png)

  7. Press finish. See extraction progress. You can keep working with your database during the export process as the extraction will be performed in the background.

![](../images/dt/dt_message-success.png)

## Export parameters¶

In this section, you will find specific configuration settings for each
supported export format. These settings allow you to customize the export
process according to the requirements of the data format you choose.

### CSV¶

Setting name | Description | Available options  
---|---|---  
Characters escape | Bad characters escaping model (surrounded with quotes or escaped with '\' character). | `quotes`/`escape`  
Delimiter | Column delimiter. | You can use special characters like `\t`, `\n`, and `\r`.  
File extension | The default file extension for the exported file. | `csv`  
Format numbers | Format numeric values using locale settings. | `true`/`false`  
Header | CSV header settings. | `none`/`top`/`bottom`  
Header case | You can choose lower or upper case for column names or descriptions in the header. | `as is`/`upper`/`lower`  
Header format | Defines the formatting of the header. | `label`/`description`/`both`  
NULL string | String which will be used instead of NULL values. |   
Quote always | Quote all cell values. Cannot be used with "Quote Never". | `disabled`/`all`/`strings`/`all but numbers`/`all including nulls`  
Quote character | Character which will be used to quote strings (space means no quote). |   
Quote never | Do not quote cell values. Cannot be used with "Quote Always". | `true`/`false`  
Row delimiter | Row delimiter. Default is system-specific line feed delimiter. | `default`/`\n`/`\r`/`\r\n`/`\n\r`  
  
### DBUnit¶

Setting name | Description | Available options  
---|---|---  
File extension | The default file extension for the exported file. | `xml`  
Force upper case column names | Convert all column names to upper case. | `true`/`false`  
Force upper case table name | Convert the table name to upper case. | `true`/`false`  
Include NULL values in export | Include NULL values in the exported data. | `true`/`false`  
Replace NULL values with | Specify a string to replace NULL values in the export. |   
  
### JSON¶

Setting name | Description | Available options  
---|---|---  
File extension | The default file extension for the exported file. | `json`  
Format dates in ISO 8601 | Convert all date values to ISO 8601 format. | `true`/`false`  
Print table name | Include the table name in the exported file. | `true`/`false`  
Export JSON values as | Export values as text or as JSON objects. | `string`/`JSON`  
  
### Markdown¶

Setting name | Description | Available Options  
---|---|---  
Confluence format | Enable Confluence-specific Markdown formatting. | `true`/`false`  
File extension | The default file extension for the exported file. | `md`  
Format numbers | Format numeric values using locale settings. | `true`/`false`  
NULL string | String to represent NULL values in the export. |   
Show header separator | Include a separator line below the header. | `true`/`false`  
  
### Source code¶

Setting name | Description | Available options  
---|---|---  
File extension | The default file extension for the exported file. | `php`  
Format dates in ISO 8601 | Convert all date values to ISO 8601 format. | `true`/`false`  
Language | Specifies the PHP version compatibility for the generated code. | `PHP < 5.4`, `PHP 5.4+`  
Quote character | Character which will be used to quote strings. | `"`, `'`  
Row delimiter | Row delimiter. Default is system-specific line feed delimiter. | `default`, `\n`, `\r`, `\r\n`, `\n\r`  
  
### SQL¶

Setting name | Description | Available options  
---|---|---  
Data rows per statement | Specifies the number of data rows in a single insert statement. | `integer`  
File extension | The default file extension for the exported file. | `sql`  
Identifier case | Allows selection of lower or upper keyword case for table and column names. | `as is`/`upper`/`lower`  
Include generated columns | Specifies whether to include auto-generated columns (e.g., auto-increment) in SQL INSERT statements. | `true`/`false`  
Insert line before rows | Specifies inserting a line feed before values in multi-row inserts. | `true`/`false`  
Keyword case | Allows selection of lower or upper keyword case. | `upper`/`lower`  
Native date/time format | Specifies using native date/time format in INSERT statements. | `true`/`false`  
Omit schema name | Specifies omitting schema/catalog name in INSERT statements. | `true`/`false`  
On conflict expression | Provides an expression for the end of the statement. This setting is specific to the database. |   
Target table name | Allows specification of the target table name to generate an INSERT statement. |   
Upsert keyword | Allows selection of different upsert keywords. | `INSERT`/`INSERT ALL`/`UPDATE OR`/`UPSERT INTO`/`REPLACE INTO`/`ON DUPLICATE KEY UPDATE`/`ON CONFLICT`  
  
### TXT¶

Setting name | Description | Available options  
---|---|---  
Batch size | Specifies the number of records per batch. | `integer`  
File extension | Specifies the file type for output. | `txt`  
In-between delimiter | Adds a custom character between data values. |   
Max column length | Specifies the maximum length of data in a column; longer values will be cropped. | `integer`  
Min column length | Specifies the minimum length of data in a column; shorter values will be padded with spaces. | `integer`  
Print header | Specifies whether to print column names at the top of the file. | `true`/`false`  
Show header delimiter | Adds hyphen characters either in the first row without a header or between the header and data. | `true`/`false`  
Show leading delimiter | Adds a pipe character at the start of the row. | `true`/`false`  
Show NULLs | Controls the display of NULL values in the output. | `true`/`false`  
Show trailing delimiter | Adds a pipe character at the end of the row. | `true`/`false`  
  
### XML¶

Setting name | Description | Available options  
---|---|---  
File extension | Specifies the file type for output. | `xml`  
Include DOCTYPE declaration | Specifies whether to include the DOCTYPE declaration in the XML file export. | `true`/`false`  
  
### XLSX¶

Setting name | Description | Available options  
---|---|---  
Append strategy | Strategy used when appending data to an existing file. | `create new sheets`/`use existing sheets`  
Boolean string FALSE | String that replaces FALSE boolean values in the exported file. | `true`/`false`  
Boolean string TRUE | String that replaces TRUE boolean values in the exported file. | `true`/`false`  
Border style | Style of cell borders in the exported file. | `NONE`/`THIN`/`THICK`  
Excel date format | Date and time format used in the Excel file (modifiable in Excel application). | `m/d/yy` / `d-mmm-yy` / `d-mmm` / `mmm-yy` / `h:mm AM/PM` / `h:mm:ss AM/PM` / `h:mm` / `h:mm:ss` / `m/d/yy h:mm`  
Column group | Column number used for grouping rows on a sheet by column value. | `integer`  
Export SQL | Specifies whether to export SQL to a second sheet in the Excel file. | `true`/`false`  
File extension | File extension for the exported document. | `xlsx`  
Header format | Format of the header in the exported file. | `label`/`description`/`both`/`none`  
Header row font | Font styling for the first row in the exported file. | `NONE`/`BOLD`/`ITALIC`/`STRIKEOUT`/`UNDERLINE`  
Max row on sheet | Maximum number of rows allowed on a single sheet, after which data will split into another sheet. | `integer`  
NULL string | String used instead of displaying NULL values in the exported file. |   
Row number(s) | Includes the row index as the first column in the exported file. | `true`/`false`  
Split SQL Text | Splits exported SQL into rows by CR (Carriage Return) in the exported file. | `true`/`false`  
Trim strings | Removes extra leading and trailing spaces from all string values in the exported file. | `true`/`false`  
  
### HTML¶

Setting name | Description | Available options  
---|---|---  
File extension | File extension for the exported document. | `html`  
Images | Extracts images to graphic files. | `true`/`false`  
Output column headers | Outputs column names as an additional row in the generated table. | `true`/`false`  
Output table header | Outputs the query or table name as the first row in the generated table. | `true`/`false`  
  
Back to top

