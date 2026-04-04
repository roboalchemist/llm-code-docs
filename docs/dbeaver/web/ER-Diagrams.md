# Source: https://dbeaver.com/docs/dbeaver/ER-Diagrams/

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
    * ER Diagrams  [ ER Diagrams  ](./) Table of contents 
      * Selection of Elements in Diagrams 
      * Generate SQL 
      * Structure Adjustment 
      * View Adjustment 
      * Refresh 
      * Diagram Notations and Routing types 
        * Notations 
        * Routing types 
        * Setting Notation and Routing type 
      * Notes 
      * Search in Diagram Entities 
      * Bindings 
        * Navigation and selection 
        * Table Manipulation 
        * Focus 
        * Other Functions 
      * Diagram Export 
      * Diagram Printing 
      * Settings 
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

  * Selection of Elements in Diagrams 
  * Generate SQL 
  * Structure Adjustment 
  * View Adjustment 
  * Refresh 
  * Diagram Notations and Routing types 
    * Notations 
    * Routing types 
    * Setting Notation and Routing type 
  * Notes 
  * Search in Diagram Entities 
  * Bindings 
    * Navigation and selection 
    * Table Manipulation 
    * Focus 
    * Other Functions 
  * Diagram Export 
  * Diagram Printing 
  * Settings 

  1. [DBeaver](/docs/dbeaver)
  2. Entity relation diagrams

# ER Diagrams

When you open the **Diagrams** tab of the [Database Object
Editor](../Database-Object-Editor/), you can visually explore, analyze, and
customize your database structure. The interface includes:

  * **Diagrams editor** : View and rearrange entities and their relationships.
  * **Palette panel** : Access tools for adding connections, notes, and more.
  * **Toolbar** : Manage diagrams with options for saving, exporting, zooming, and configuration.

DBeaver supports diagrams for existing tables, schemas, and custom
visualizations. You can select, modify, and customize elements or export
diagrams for further use. Advanced notations, routing types, and certain
features may depend on your product edition. For more, see [Database Structure
Diagrams](../Database-Structure-Diagrams/).

Tip

Create custom diagrams to tailor visualizations. See [Custom
Diagrams](../Custom-Diagrams/).

## Selection of Elements in Diagrams¶

You can use one of the two tools to select elements in diagrams:

  * Select â supports both, single and multi-select modes. To select a single element (table, connection, entity inside a table) in a diagram, just click that element. To select multiple elements, similar to using the Marquee tool, click outside the first element and draw until all elements you need are in focus:

![](../images/ug/ERD-Select-tool.png)

## Generate SQL¶

Diagrams in DBeaver support generating SQL for various commands, including
`SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `JOIN`, and some database-
specific commands such as `INSERT ON CONFLICT`, `UPDATE FROM`, and `DELETE
USING`.

Tip

`INSERT ON CONFLICT`, `UPDATE FROM`, and `DELETE USING` are specific to
PostgreSQL.

  * Right-click the selected tables and choose **Generate SQL** to create the query automatically.
  * To generate a **JOIN** statement, select multiple tables in the diagram.

## Structure Adjustment¶

Note

All changes to existing database schemas cannot be saved and are intended for
exploration purposes only. You can do the following structural changes in the
diagrams.

  * Add new tables to a diagram by drag-n-dropping them onto the diagram field from the [Database Navigator](../Database-Navigator/).
  * Rearrange tables in the diagram by dragging them all over the space. You can select several tables and drag them to a new location.
  * Auto-arrange tables into a compact view after manual rearrangements: click the **Arrange Diagram** (![](../images/ug/Arrange-diagrams.png)) in the toolbar or on the context menu (right-click anywhere on the diagram tab).
  * (Available for [Custom Diagrams](../Custom-Diagrams/) only) - connect tables with a connector: click the **Show Palette** button (![](../images/ug/Show-pallette-icon.png)) in the upper-left corner of the diagram tab and then, in the Palette panel, click **Connection** :

![](../images/ug/ERD-Connections.png)

Now click the tables that you want to connect with each other in turn, one by
one. To stop the connection line, double-click the last table * (Available for
[Custom Diagrams](../Custom-Diagrams/) only) - removes tables and connections:
right-click the table or connection and click **Delete** on the context menu
or just click the table or connection and press `Delete`.

Tip

In cases where tables lack actual foreign keys, dragging one column onto
another allows you to set up a [virtual foreign key](../Virtual-
Keys/#creating-a-virtual-foreign-key). This can be useful for managing data
relationships in environments where physical constraints are not defined.

## View Adjustment¶

You can adjust the view of any diagram in the following ways:

  * Enable/disable the diagram grid: Click **Toggle Grid** (![](../images/ug/Toggle-grid.png)) in the toolbar.
  * Modify attributes visibility: Right-click the diagram and, on the context menu, click **Show Attributes** and then select one of the options:
  * **All** \- all attributes
  * **Any keys** \- primary and foreign keys
  * **Primary key** \- only primary keys
  * **None** \- no attributes
  * Modify attributes presentation: Right-click the diagram and, on the context menu, click **View Styles** and then select one of the options:
  * **Show Icons**
  * **Show Data Types**
  * **Show Nullability**
  * **Show Comments**
  * **Show Fully qualified names**
  * Change the color of the entities/notes: Right-click the header of the entity or comment and then click **Set color** on the context menu. Then you can select the color and click **OK**.
  * For elements located in front of/behind others, bring an element to the front or send it to the back: Right-click the element and then click **Bring to front** / **Send to back** on the context menu.
  * Zoom the diagram in/out: Click the **Zoom In** /**Zoom Out** buttons or choose the scaling value in the dropdown list in the toolbar: ![](../images/ug/ERD-zoom.png)

## Refresh¶

To see changes made by others to the database schema, you might need to
refresh the diagram: click **Refresh Diagram** (![](../images/ug/Refresh-
projects-icon.png)) in the toolbar.

## Diagram Notations and Routing types¶

DBeaver offers a variety of notations and routing types for Diagrams, allowing
you to customize database structure representations to suit your needs.

### Notations¶

  * **IDEF1X** (default): Highly recommended for designing relational databases. It places a strong emphasis on detailing entity relationships and constraints. For more information, see [IDEF1X Notation](https://www.softwaregems.com.au/Documents/Documentary%20Examples/IDEF1X%20Notation.pdf).

![](../images/ug/1DEF1X-notation-sample.png)

  * **Bachman** : A notation that is particularly useful for data processing diagrams and reflects the data structure of the designed system from the data management perspective. For a more detailed understanding, refer to [Bachman Notation](https://www.conceptdraw.com/examples/bachman-notation).

![](../images/ug/Bachman-notation-sample.png)

Note

Bachman notation is available in [Enterprise](../Enterprise-Edition/),
[Ultimate](../Ultimate-Edition/) and [Team](https://dbeaver.com/dbeaver-team-
edition) editions only.

  * **Crow's Foot** : This notation is widely used and is particularly intuitive for representing cardinality and relationships between entities. More information is available on [Crow's Foot Notation](https://miro.com/diagramming/crows-foot-notation-in-er-diagrams/).

![](../images/ug/Crows-foot-notation-sample.png)

### Routing types¶

  * **Shortest paths** (default): Calculate and display the shortest possible lines connecting entities, ensuring a compact and efficient diagram representation.

![](../images/ug/Shortest-paths-router-sample.png)

Tip

Click on a connection to view detailed relationships.

  * **Orthogonal paths** : Uses right-angled lines for clear, structured layouts; Showing direct relationships between tables and columns.

![](../images/ug/Orthogonal-paths-router-sample.png)

Note

Orthogonal paths are available in [Enterprise](../Enterprise-Edition/),
[Ultimate](../Ultimate-Edition/) and [Team](https://dbeaver.com/dbeaver-team-
edition) editions only.

### Setting Notation and Routing type¶

To set notation or routing type in an Diagram:

  1. Right-click on an empty space within the Diagram area.
  2. From the context menu, hover over **Notation** or **Routing** for the respective settings.
  3. Select your preferred option from the submenu.

Alternatively, adjust these settings through the Diagram toolbar:

  1. Click the **Settings** button ![](../images/ug/Configure-columns-visibility-icon.png).
  2. In the **Advanced** section, find the **Notation type** or **Routing type** dropdown menu.
  3. Choose your preferred setting.

## Notes¶

You can create notes only in [Custom Diagrams](../Custom-Diagrams/). To create
a note, click the **Show Palette** button (![](../images/ug/Show-pallette-
icon.png)) in the upper-left corner of the diagram tab. Then, in the Palette
panel, click **Note** and click anywhere in the diagram tab. Now you can
double-click the **Note** box to enter the note text:

![](../images/ug/ERD-Notes.png)

## Search in Diagram Entities¶

To search among entities of a diagram, click the **Search items** button
(![](../images/ug/Search-icon.png)) in the toolbar, then type in the search
combination. The entities that contain the search combination are highlighted
in the diagram. To remove the filter, click the cross icon next to the search
field.

## Bindings¶

### Navigation and selection¶

  * Use `ARROWS` to navigate between tables.
  * Press `SHIFT`|`â§` \+ `ARROWS` to select multiple tables.
  * Press `CTRL`|`â` \+ `ARROWS` to select additional tables using `SPACEBAR`.
  * Press `SPACEBAR` to select the current table.

### Table Manipulation¶

  * Press `.` (period) to change the mode to move/resize tables, then use `ARROWS` and `ENTER`|`â©` to move/resize tables.

Note

To use this feature on macOS, you may need to enable accessibility permissions
for DBeaver. This can be done in `System Preferences -> Security & Privacy ->
Accessibility`.

### Focus¶

  * Press `ENTER`|`â©` to focus on attributes in the table.
  * Press `BACKSPACE`|`â«` to leave the focus.
  * Use `|`, `?`, `\` to focus on associations.
  * Press `ALT/FN + 1`|`â¥/FN + 1` to focus on the diagram.
  * Press `ALT/FN + 2`|`â¥/FN + 2` to focus on the palette.
  * Press `ALT/FN + 3`|`â¥/FN + 3` to focus/open the outline.
  * Press `ALT/FN + 4`|`â¥/FN + 4` to focus on the parameter view.

### Other Functions¶

  * Press `CTRL + SHIFT + ENTER` |`â + SHIFT + â©` to open the selected table diagram.

## Diagram Export¶

You can export (save) a diagram as an image (PNG, GIF, BMP formats) or as a
file in GraphML format. To export a diagram, click **Save diagram in external
format** (![](../images/ug/ERD-Export.png)) in the toolbar.

## Diagram Printing¶

To print a diagram, press `CTRL+P` or click **Print Diagram**
(![](../images/ug/Print-icon.png)) on the toolbar.

## Settings¶

To modify the diagram settings, click **Configuration**
(![](../images/ug/Configure-columns-visibility-icon.png)) on the toolbar.

Back to top

