# Source: https://dbeaver.com/docs/dbeaver/Dashboards/

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
      * Dashboards  [ Dashboards  ](./) Table of contents 
        * Dashboard Types 
          * Connection Dashboards 
          * Project Dashboards 
        * Managing Dashboard panel 
          * Opening Dashboard panel 
          * Adding charts 
          * Removing charts 
          * Resetting charts 
          * Changing chart representation 
          * Adjusting chart configuration 
          * Setting connection preferences 
          * Detaching charts 
          * Changing chart view 
          * Copying chart to clipboard 
          * Saving charts 
          * Printing charts 
          * Zooming 
        * Managing charts 
          * Creating charts 
            * To create a chart from scratch 
            * To create a chart from a template 
          * Editing charts 
            * To edit a chart's configuration 
          * Deleting Dashboards 
            * To delete a dashboard 
        * Managing web-based dashboards 
          * Web charts 
          * Tableau charts 
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

  * Dashboard Types 
    * Connection Dashboards 
    * Project Dashboards 
  * Managing Dashboard panel 
    * Opening Dashboard panel 
    * Adding charts 
    * Removing charts 
    * Resetting charts 
    * Changing chart representation 
    * Adjusting chart configuration 
    * Setting connection preferences 
    * Detaching charts 
    * Changing chart view 
    * Copying chart to clipboard 
    * Saving charts 
    * Printing charts 
    * Zooming 
  * Managing charts 
    * Creating charts 
      * To create a chart from scratch 
      * To create a chart from a template 
    * Editing charts 
      * To edit a chart's configuration 
    * Deleting Dashboards 
      * To delete a dashboard 
  * Managing web-based dashboards 
    * Web charts 
    * Tableau charts 

  1. [DBeaver](/docs/dbeaver)
  2. [Data Editor](/docs/dbeaver/Data-Editor)
  3. Viewing and editing data

# Dashboards

Note

This feature is available in Community, [Enterprise](../Enterprise-Edition/),
[Ultimate](../Ultimate-Edition/) and [Team](https://dbeaver.com/docs/team-
edition/) editions only.

**Dashboards** tool allows DBAs and programmers to quickly identify
performance, disk space issues, the number of connections, and other important
KPIs associated with a single [database connections](../Create-Connection/).

By default, DBeaver comes equipped with predefined charts sets for several
popular databases. These include:

Database | Predefined charts  
---|---  
**Exasol** | Connections, User activity.  
[MySQL](../Database-driver-MySQL/) | InnoDB data, InnoDB memory, Key Efficiency, Queries, Server sessions, Traffic.  
[Oracle](../Oracle/) | CPU usage, Global Query Stats, IO Stats, Memory usage, Memory usage by components.  
[PostgreSQL](../Database-driver-PostgreSQL/) | Block IO, Server sessions, Transactions per second.  
[BigQuery](../Database-driver-BigQuery/) | Bytes Processed for Project.  
  
In addition to these predefined charts, DBeaver also supports the creation of
custom charts. For more information on customizing a dashboard panel, refer to
the Managing Dashboards section.

## Dashboard Types¶

You can create and open two types of dashboards: Connection dashboards and
Project dashboards.

### Connection Dashboards¶

Connection dashboards are specific to individual database connections. These
dashboards allow you to monitor performance, disk space, the number of
connections, and other critical metrics related to the connected database. Any
changes or customizations made to a connection dashboard are temporary and
specific to the session of the database connection.

For instructions on managing dashboards, see the Managing Dashboard panel
section.

### Project Dashboards¶

Project dashboards can include web-based dashboards and are saved within the
active [Project](../Projects/).

For instructions on adding and configuring these dashboards, refer to the
Managing web-based dashboards section.

## Managing Dashboard panel¶

The Dashboards panel aggregates a collection of real-time displays that update
continuously. Each display consists of ongoing SQL `SELECT` queries and
dynamically generated charts, ensuring that data visualizations are always
current.

### Opening Dashboard panel¶

To open the Dashboards panel:

  * Press the **Open Dashboard** button ![](../images/ug/dashboards/Open_Dashboard_icon.png) on the top toolbar. The default configuration of the dashboards panel for the current database connection will appear.

Note

The toolbar is customizable. For further information, refer to [Toolbar
Customization](../Toolbar-Customization/) article.

  * You can also right-click a connection in **Database Navigator** , then navigate to **Tools - > Open Dashboard**, or use the keyboard shortcut `Ctrl+Alt+Shift+B` to open the Dashboards panel.

![](../images/ug/dashboards/Open_Dashboard_Menu_Option.png)

Once you open the Dashboards panel, the following controls are available on
the toolbar:

Name | Icon | Description  
---|---|---  
**Settings** | ![](../images/ug/dashboards/Dashboard_Settings_icon.png) | Opens the dashboard's configuration.  
**Add chart** | ![](../images/ug/dashboards/Dashboard_Add_icon.png) | Opens a window where you can select which chart to add to the dashboard.  
**Show charts catalog** | ![](../images/ug/dashboards/show-charts-catalog-button.png) | Opens the side menu displaying available charts.  
**Delete dashboards** | ![](../images/ug/dashboards/Dashboard_Delete_icon.png) | Deletes the Dashboard panel. Default dashboards cannot be permanently deleted and will be restored automatically if removed; however, custom dashboards, once deleted, must be manually recreated.  
  
### Adding charts¶

To add a chart to the Dashboards panel:

  * Press the **Add chart** button ![](../images/ug/dashboards/Dashboard_Add_icon.png) on the Dashboards panel's toolbar, choose one of the charts from the list of available charts, and press **Add** button or double-click on it, or press `Enter`.

  * You can also right-click in any place of the Dashboards panel and then select the **Add chart** option.

  * Alternatively, press the **Show charts catalog** button ![](../images/ug/dashboards/show-charts-catalog-button.png) on the Dashboards panel's toolbar to open the side menu displaying available charts. From this menu, you can add a chart to the dashboard by dragging it to the Dashboard panel, double-clicking on it, or press `Enter`.

### Removing charts¶

To remove a chart from the Dashboards panel:

  * Press the **Remove chart** button ![](../images/ug/dashboards/Dashboard_Remove_icon.png) located on the chart panel's toolbar.
  * Select the **Remove chart** option from the chart's context menu.

### Resetting charts¶

If you want to restart a chart's calculations, you can reset it.

To reset a chart:

  * Right-click on the chart and select the **Reset dashboards** option ![](../images/ug/dashboards/Dashboard_Reset_icon.png).
  * Left-click on the chart and press the **Reset dashboards** button on the chart panel's toolbar.

### Changing chart representation¶

To adjust chart representation settings:

  * Right-click on a chart and select the **Settings** menu option ![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the Dashboards toolbar.
  * Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) located on the chart panel's toolbar.

Then, in the opened dialog, change the parameters you want.

![](../images/ug/dashboards/RepresentationSettings_DialogBox.png)

Parameter | Description  
---|---  
**Name** | Defines the name of a chart.  
**Description** | Defines the chart's description. Use this field to make it easy to understand what kind of information the chart represents.  
**Update periods(ms)** | Defines how often chart's rendering should be updated. The default value is 1000 ms.  
**Maximum items** | Defines the maximum number of fetched items. The default value is 300.  
**View** | Defines the visual representation of the chart. The following options are available: Bar, Pie, Time series.  
**Show legend** | If this check-box is selected, the legend will be displayed on the chart.  
**Show grid** | If this check-box is selected, the grid will be displayed on the chart.  
**Show domain axis** | If this check-box is selected, the domain axis will be displayed on the chart.  
**Show range axis** | If this check-box is selected, the range axis will be displayed on the chart.  
  
### Adjusting chart configuration¶

To adjust a chart's configuration settings:

  * Right-click on a chart and select the **Settings** menu option ![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the Dashboards toolbar.
  * Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) located on the chart panel's toolbar.

in the opened dialog box, press the **Configuration** menu option.

![](../images/ug/dashboards/ConfigurationSettings_DialogBox.png)

The following chart parameters can be configured:

Parameter | Description | Available values  
---|---|---  
**ID** | Unique identifier for the chart. This is typically a structured string. |   
**Name** | The name of the chart, which describes its function or the data it displays. |   
**Display Name** | A user-friendly name for the chart that can be displayed in the user interface. |   
**Description** | A brief explanation of what the chart displays, including the type of data and its use case. |   
**Database** | Specifies the type of database connected to the chart. |   
**Data type** | The nature of data used in the chart, which indicates continuous data points over time. | `timeseries`, `statistics`, `provided`  
**Calc type** | The calculation type for data processing, which indicates direct value use without derivatives. | `value`, `delta`  
**Value type** | The data unit measure, useful in contexts like memory usage. | `decimal`, `integer`, `percent`, `bytes`  
**Interval** | The time interval for data refresh or update, indicating rapid data refresh cycles. | `millisecond`, `second`, `minute`, `hour`, `day`, `week`, `month`, `year`  
**Fetch type** | Method of data retrieval, indicating row-wise fetching of data. | `columns`, `rows`, `stats`  
**Queries** | SQL query used to fetch data for the chart, should correctly reflect conditions and targets specific data. |   
**Default view** | Default visual representation style of the chart, which provides a pie chart of the data. | `Bar`, `Pie`, `Time series`, `Browser`  
**Update period (ms)** | Frequency of chart updates in milliseconds, indicating how often the chart data gets refreshed. |   
**Maximum items** | The maximum number of data points or items to display at any given time on the chart. |   
  
Note

Predefined charts are read-only and cannot be re-configured, but you can copy
them and use them as templates to create new charts with any query and other
settings. To learn about creating new charts, see the Managing charts section.

### Setting connection preferences¶

By default, if there is no active connection to the database and you open its
Dashboards panel, all the charts on the panel will be empty.

You can force a database connection on the Dashboard panel's activation by
pressing the **Settings** button
![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the dashboards
panel's toolbar and then selecting the **Connect to database on activation**
checkbox.

### Detaching charts¶

If you have several monitors and would like to place a chart on a separate
screen, you can either detach the whole Dashboards panel or a single chart,
and drag-and-drop them to any place you want.

  * To detach the whole Dashboard panel, right-click on the dashboard's tab name and select the **Detach** menu option.

  * To detach a single chart:

  * Double left-click over it.
  * Select the **View in popup** button ![](../images/ug/dashboards/view-in-popup-button.png).

### Changing chart view¶

You can change the representation of a dashboard and view it as a **Pie** ,
**Bar** , or **Time series**. To change the dashboard view:

  * Right-click on it and select the **View as** menu option.
  * Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) located on the chart panel's toolbar and select the **View** menu option.

### Copying chart to clipboard¶

To copy a chart onto the clipboard, right-click on the chart and use the
**Copy to Clipboard** menu option. The screenshot of the dashboard will be
placed onto the clipboard.

### Saving charts¶

If you want to save a screenshot of a chart locally in `PNG` format, right-
click on it and select the **Save as...** option in the context menu
displayed.

### Printing charts¶

If you want to print out a screenshot of a dashboard, right-click the
dashboard to be printed and select the **Print...** option.

### Zooming¶

For **Time series** and **Bar** chart representations, the following zooming
options are available on the dashboard's context menu:

  * Zoom In
  * Zoom Out
  * Zoom Reset

## Managing charts¶

You can extend the list of predefined default dashboards by creating your own
custom dashboards. This section describes dashboards' list management.

### Creating charts¶

You can create a new custom dashboard either from scratch or from any existing
dashboards.

#### To create a chart from scratch¶

  1. Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the Dashboards panel toolbar.
  2. In the opened dialog box, click the **Manage charts...** button.
  3. In the **Manage dashboard charts** window, click the **New Database chart** button.
  4. Set up all configuration parameters as required and press **OK**.

Tip

To learn more about the chart's configuration parameters, see [Adjusting chart
Configuration](./#adjusting-chart-configuration).

![](../images/ug/dashboards/New_dashboard_from_scratch.png)

#### To create a chart from a template¶

  1. Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the Dashboards panel toolbar.
  2. In the opened dialog box, click the **Manage charts...** button.
  3. In the **Manage dashboard charts** window, select any of the existing charts from the list and click **Copy**.
  4. Adjust all configuration parameters as required and press **OK**.

### Editing charts¶

If you need to change the chart's name, ID, or any other configuration
setting, you can edit a chart.

Note

Only custom charts can be edited.

#### To edit a chart's configuration¶

  1. Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the Dashboards panel toolbar.
  2. In the opened dialog box, click the **Manage charts...** button.
  3. In the **Manage dashboard charts** window, select any of the custom charts from the list and click **Edit...**.
  4. Adjust all configuration parameters as required and press **OK**.

### Deleting Dashboards¶

Note

Predefined charts cannot be deleted, but any custom dashboards can be deleted.

If you want to delete a dashboard, follow the steps described below.

#### To delete a dashboard¶

  1. Press the **Settings** button ![](../images/ug/dashboards/Dashboard_Settings_icon.png) on the Dashboards panel toolbar.
  2. In the opened dialog box, click the **Manage charts...** button.
  3. In the **Manage dashboard charts** window, select any of the custom charts from the list and click **Delete**.

## Managing web-based dashboards¶

### Web charts¶

DBeaver allows the integration of custom web-based charts into your
dashboards, enabling a flexible way to display data from any accessible URL.

To add a web chart to a dashboard, follow these steps:

  1. Click on the arrow next to the **Open Dashboard** button ![](../images/ug/dashboards/Open_Dashboard_icon.png) on the top toolbar, and select **new project dashboard**.

Note

The toolbar is customizable. For further information, refer to [Toolbar
Customization](../Toolbar-Customization/) article.

  1. In the new dashboard, navigate to **Add chart - > Manage charts**.
  2. Choose **Web** and click on the **New Web chart** button.
  3. You will be prompted to enter `ID`, `Name`, `Description` and the `URL` of the Web chart.

![](../images/ug/dashboards/web-based-charts.png)

Tip

The URL can point to any web-hosted visualization tool, such as Grafana pages
with specific metrics. You can also use DBeaver's pre-configured variables in
the URL. For more information on existing variables, see the [Pre-configured
variables](../Pre-configured-Variables/) article.

### Tableau charts¶

DBeaver supports integrating Tableau charts for enhanced data visualization.

Note

You must be logged into your Tableau account through DBeaver. For more details
on setting this up, see our [article](../Tableau-integration-in-DBeaver/).

To access and use Tableau charts, follow these steps:

  1. Click on the arrow next to the **Open Dashboard** button ![](../images/ug/dashboards/Open_Dashboard_icon.png) on the top toolbar, and select **new project dashboard**.
  2. Enter a **Name** and **ID** for your dashboard; this will open the Dashboard panel.
  3. On the right side of the Dashboard panel, Tableau charts will be available in a dropdown menu.
  4. Select the desired chart and either drag it to the left side of the Dashboard panel or double-click on the chart to add it.

![](../images/ug/dashboards/tableau-charts.png)

Back to top

