# Source: https://dbeaver.com/docs/dbeaver/Lite-Edition/

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
      * Lite edition  [ Lite edition  ](./) Table of contents 
        * Lite Edition features 
          * Subscription model 
          * Integrated database drivers 
          * Supported databases 
            * Relational databases 
            * Non-Relational databases 
      * [ Ultimate edition  ](../Ultimate-Edition/)
    * [ Release cycles  ](../DBeaver-release-cycles/)
    * [ Statistics collection  ](../Statistics-Collection/)
    * [ Customer technical support  ](../Customer-technical-support-information/)
  * [ FAQ  ](../FAQ/)

Table of contents

  * Lite Edition features 
    * Subscription model 
    * Integrated database drivers 
    * Supported databases 
      * Relational databases 
      * Non-Relational databases 

  1. [DBeaver](/docs/dbeaver)
  2. [About DBeaver](/docs/dbeaver/Enterprise-Edition)
  3. Editions

# Lite edition

[DBeaver Lite Edition](https://dbeaver.com/dbeaver-lite/) is tailored for
users who need basic tools to work with databases. This version offers a
streamlined interface that focuses on simple database tasks like viewing data
and running queries. It is especially useful for business users who need an
easy-to-use tool.

Note

The DBeaver Lite Edition is designed for individual use only.

## Lite Edition features¶

Key features included in the Lite Edition are designed to support everyday
database tasks with minimal hassle:

  * **Data Visualization**

    * **Color coding and highlighting** : Simplifies data analysis by color-coding and highlighting table rows and fields based on conditions. [Learn more](../SQL-Code-Editor/).
    * **Data filtering and sorting** : Provides tools to filter and sort data directly within the database interface. [Learn more](../Data-Filters/).
    * **Analytical charts** : Offers tool for creating analytical charts to represent data visually. [Learn more](../Managing-Charts/).
    * **Entity relationship diagrams** : Visualize database schemas through entity-relationship diagrams. [Learn more](../ER-Diagrams/).
  * **Data import/export**

    * **Office formats support (XLS)** : Enables users to import and export data in Office formats, specifically Excel (`XLS`). [Learn more](../Data-transfer/).
  * **Query development**

    * **AI Assistant in SQL Editor** : Integrates an AI Assistant and AI Chat to offer guidance and automation within the SQL Editor. [Learn more](../AI-Smart-Assistance/).
    * **Search in query history** : Enables searching through previous queries for easier management and reuse.
    * **Spelling** : Provides spelling verification to improve the quality and accuracy of SQL scripts. [Learn more](../Spelling/).
    * **Visual query builder** : Provides a graphical interface to construct SQL queries without writing code. [Learn more](../Visual-Query-Builder/).
  * **Comprehensive security support** : Ensures secure access to databases within your environment, even if they are protected by Single Sign-On (SSO), Kerberos, SSL, and other security measures.

### Subscription model¶

The DBeaver Lite Edition is offered as an annual subscription, which should be
renewed to continue receiving updates and support.

[Discover more about the DBeaver Lite Edition and
subscribe](https://dbeaver.com/dbeaver-lite/).

### Integrated database drivers¶

The Lite Edition has a comprehensive set of JDBC drivers, offering
connectivity to various databases without needing separate downloads and
configurations. Additionally, a versatile ODBC driver is supported for broader
database compatibility.

Info

For additional details on utilizing the ODBC driver, please consult the [ODBC-
JDBC driver](../ODBC-JDBC-Driver/) article.

### Supported databases¶

The Lite Edition provides support for a wide range of databases. Below are
tables listing the databases available and specifying whether the Lite Edition
offers enhanced features compared to the Community Edition.

*

Enhanced features may include additional metadata capabilities, such as the
ability to manage and interact with specific database objects unique to
certain systems. For instance, managing **Roles** in Redshift. These features
also cover various advanced authentication methods, and numerous other
functionalities designed to improve security and data management.

#### Relational databases¶

Database name | Enhanced features* compared to the Community Edition  
---|---  
**Altibase** | -  
**Apache Arrow** | Not available in Community Edition  
**Apache Calcite Avatica** | â  
**Apache Kylin** | -  
**Aurora DSQL** | Not available in Community Edition  
**Azure SQL Server** | â  
**Babelfish via TDS (beta)** | â  
**CUBRID** | â  
**Cache** | -  
[**ClickHouse**](../Clickhouse/) | -  
**CloudberryDB** | -  
[**ClickHouse (Legacy)**](../Clickhouse/) | â  
[**CloudSQL - MySQL**](../Database-driver-MySQL-on-Google-Cloud/) | Not available in Community Edition  
[**CloudSQL - PostgreSQL**](../Database-driver-PostgreSQL-on-Google-Cloud/) | Not available in Community Edition  
[**CloudSQL - SQL Server**](../Database-driver-Microsoft-SQL-Server-on-Google-Cloud/) | Not available in Community Edition  
**CockroachDB** | -  
**CrateDB** | -  
**CrateDB (Legacy)** | -  
[**Databricks**](../Database-driver-Databricks/) | â  
**Dameng** | -  
[**Db2 for IBM i**](../Database-driver-IBM-Db2/) | â  
[**Db2 for LUW**](../Database-driver-IBM-Db2/) | -  
[**Db2 for z/OS**](../Database-driver-IBM-Db2/) | â  
**Denodo 8** | -  
**Derby Embedded** | -  
**Derby Server** | -  
**Dremio** | -  
**DuckDB** | -  
**EDB** | â  
**Exasol** | â  
**FerretDB** | Not available in Community Edition  
**Firebird** | â  
[**Firestore**](../Database-driver-Firestore/) | Not available in Community Edition  
**Fujitsu Enterprise Postgres** | Not available in Community Edition  
**GaussDB** | -  
[**Google AlloyDB**](../Database-driver-AlloyDB-for-PostgreSQL/) | Not available in Community Edition  
**Google Cloud Spanner** | â  
[**Greenplum**](../Database-driver-Greenplum/) | â  
**Greengage** | Not available in Community Edition  
**H2 Embedded** | â  
**H2 Embedded V.2** | -  
**H2 Server** | â  
**H2GIS Embedded** | -  
**H2GIS Server** | -  
**HANA** | â  
**HSQL Embedded** | -  
**HSQL Server** | -  
**Informix** | â  
**Ingres** | -  
**InterSystems IRIS** | -  
**JDBCX** | -  
**Jennifer** | -  
**MS Access (UCanAccess)** | -  
[**MariaDB**](../Database-driver-MariaDB/) | â  
**Materialize** | -  
**MaxDB** | -  
**Mimer SQL** | -  
**MonetDB** | -  
[**MySQL**](../Database-driver-MySQL/) | â  
[**MySQL 5 (Legacy)**](../Database-driver-MySQL/) | â  
**NDB Cluster** | -  
**NetSuite** | Not available in Community Edition  
[**Netezza**](../Database-driver-Netezza/) | â  
**NuoDB** | -  
**ODBC** | Not available in Community Edition  
**OceanBase** | -  
**Ocient** | -  
**OmniSci (formerly MapD)** | -  
**OpenEdge** | -  
**OpenSearch** | â  
[**Oracle**](../Oracle/) | â  
**Pervasive SQL** | -  
[**PostgreSQL**](../Database-driver-PostgreSQL/) | â  
**PrestoDB** | -  
**PrestoSQL** | -  
**Raima** | Not available in Community Edition  
[**Redshift**](../Database-driver-Amazon-Redshift/) | â  
[**Redshift Serverless**](../Database-driver-Amazon-Redshift/) | â  
**RisingWave** | -  
**SAP ASE jConnect** | -  
[**SQL Server**](../Database-driver-Microsoft-SQL-Server/) | â  
[**SQL Server (Old driver, jTDS)**](../Database-driver-Microsoft-SQL-Server/) | â  
[**SQLite**](../Database-driver-SQLite/) | â  
[**SQLite Crypt**](../Database-driver-SQLite/) | Not available in Community Edition  
**SQream DB** | -  
[**Salesforce**](../Database-driver-Salesforce/) | Not available in Community Edition  
**Salesforce Data Cloud** | â  
**SingleStore** | â  
[**Snowflake**](../Snowflake/) | â  
**StarRocks** | -  
**Sybase jConnect** | â  
**Sybase jTDS** | â  
[**Teradata**](../Database-driver-Teradata/) | â  
**TiDB** | -  
[**Trino**](../Database-driver-Trino/) | -  
**Vertica** | â  
**Virtuoso** | -  
[**Yellowbrick**](../Database-driver-Yellowbrick/) | -  
**YugabyteDB** | -  
  
#### Non-Relational databases¶

Database name | Enhanced features* compared to the Community Edition  
---|---  
**Apache Drill** | â  
[**Apache Hive**](../Apache-Hive/) | â  
**Apache Ignite** | -  
**Apache Kyuubi** | -  
**Apache Phoenix** | -  
**Apache Spark** | -  
[**Athena**](../Database-driver-Amazon-Athena/) | â  
**Azure Cosmos DB for Cassandra** | Not available in Community Edition  
[**Azure Cosmos DB for MongoDB**](../Database-driver-CosmosDB/) | Not available in Community Edition  
[**Azure Cosmos DB for NoSQL**](../Database-driver-Azure-CosmosDB-for-NoSQL/) | Not available in Community Edition  
[**Cassandra**](../Cassandra/) | Not available in Community Edition  
**Cloudera Impala** | -  
**CouchDB** | Not available in Community Edition  
[**Couchbase**](../Couchbase/) | Not available in Community Edition  
[**Couchbase 5+**](../Couchbase/) | Not available in Community Edition  
[**CSV**](../Database-driver-CSV/) | +  
**DBF** | -  
[**DocumentDB**](../AWS-DocumentDB/) | Not available in Community Edition  
[**DynamoDB**](../AWS-DynamoDB/) | Not available in Community Edition  
**Elasticsearch** | â  
**Gemfire XD** | -  
[**Google BigQuery**](../Database-driver-BigQuery/) | â  
[**Google Cloud Bigtable**](../Google-Bigtable/) | Not available in Community Edition  
[**InfluxDB**](../InfluxDB/) | Not available in Community Edition  
[**InfluxDB 2**](../InfluxDB/) | Not available in Community Edition  
[**InfluxDB 3**](../InfluxDB/) | Not available in Community Edition  
[**Keyspaces**](../AWS-Keyspaces/) | Not available in Community Edition  
**Machbase** | -  
[**MongoDB**](../MongoDB/) | Not available in Community Edition  
[**Neo4j**](../Database-driver-Neo4j/) | Not available in Community Edition  
[**Neptune**](../Database-driver-Neptune/) | Not available in Community Edition  
**Open Distro Elasticsearch** | â  
**OrientDB** | -  
[**Parquet**](../Database-driver-Parquet/) | Not available in Community Edition  
[**Redis**](../Redis/) | Not available in Community Edition  
**ScyllaDB** | Not available in Community Edition  
**SnappyData** | -  
**Solr** | -  
**TDengine** | â  
**TDengine Cloud** | â  
**TimescaleDB** | -  
[**Timestream**](../Database-driver-Amazon-Timestream/) | Not available in Community Edition  
[**XLSX**](../Database-driver-XLSX/) | Not available in Community Edition  
**Yugabyte CQL** | Not available in Community Edition  
  
Back to top

