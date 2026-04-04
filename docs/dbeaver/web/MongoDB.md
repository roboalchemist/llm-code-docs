# Source: https://dbeaver.com/docs/dbeaver/MongoDB/

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
        * MongoDB  [ MongoDB  ](./) Table of contents 
          * Setting Up 
            * MongoDB connection settings 
              * Connection details 
            * MongoDB driver properties 
            * Secure Connection Configurations 
            * Secure Storage with Secret Providers 
          * Powering MongoDB with DBeaver 
            * MongoDB database objects 
            * MongoDB features in DBeaver 
              * Browsing MongoDB collections 
            * Database operations 
              * Executing JavaScript 
              * Executing SQL 
                * SELECT queries 
                  * Conditions 
                  * Nested fields 
                  * Working with object IDs 
                  * Working with JOINs 
                  * Aggregate functions 
                * INSERT statement 
                * UPDATE statement 
                * DELETE statement 
                * CREATE TABLE statement 
                * DROP TABLE statement 
                * Working with dates 
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
      * [ Lite edition  ](../Lite-Edition/)
      * [ Ultimate edition  ](../Ultimate-Edition/)
    * [ Release cycles  ](../DBeaver-release-cycles/)
    * [ Statistics collection  ](../Statistics-Collection/)
    * [ Customer technical support  ](../Customer-technical-support-information/)
  * [ FAQ  ](../FAQ/)

Table of contents

  * Setting Up 
    * MongoDB connection settings 
      * Connection details 
    * MongoDB driver properties 
    * Secure Connection Configurations 
    * Secure Storage with Secret Providers 
  * Powering MongoDB with DBeaver 
    * MongoDB database objects 
    * MongoDB features in DBeaver 
      * Browsing MongoDB collections 
    * Database operations 
      * Executing JavaScript 
      * Executing SQL 
        * SELECT queries 
          * Conditions 
          * Nested fields 
          * Working with object IDs 
          * Working with JOINs 
          * Aggregate functions 
        * INSERT statement 
        * UPDATE statement 
        * DELETE statement 
        * CREATE TABLE statement 
        * DROP TABLE statement 
        * Working with dates 

  1. [DBeaver](/docs/dbeaver)
  2. [Databases support](/docs/dbeaver/Database-drivers)
  3. [Classic](/docs/dbeaver/Apache-Hive)
  4. MongoDB

# MongoDB

Note

This driver is available in [Lite](../Lite-Edition/),
[Enterprise](../Enterprise-Edition/), [Ultimate](../Ultimate-Edition/) and
[Team](https://dbeaver.com/docs/team-edition/) editions only.

This guide provides instructions on how to set up and use MongoDB with
DBeaver.

One of the standout features of DBeaver's MongoDB support is its flexibility
in presentation. You can view MongoDB collections as standard relational
tables, JSON documents, or even in chart presentations.

DBeaver interacts with MongoDB servers using a specific driver, supporting
versions from 2.x to the current version. DBeaver also supports MongoDB
extension such as Cosmos DB, you can find more information about this driver
in our [article](../Database-driver-CosmosDB/).

Before you start, you must create a connection in DBeaver and select MongoDB.
If you have not done this, please refer to our [Database
Connection](../Create-Connection/) article.

![](../images/database/mongodb/mongodb-drivers.png)

## Setting Up¶

This section provides an overview of DBeaver's settings for establishing a
direct connection and the configuration of secure connections using SSH,
proxies and SSL.

### MongoDB connection settings¶

In this subsection, we will outline the settings for establishing a direct
connection to a MongoDB database using DBeaver. Correctly configuring your
connection ensures seamless interaction between DBeaver and your MongoDB
database.

The page of the connection settings requires you to fill in specific fields to
establish the initial connection.

![](../images/database/mongodb/mongodb-connection-init.png)

Field | Description  
---|---  
**Connect by (Host/URL)** | Choose whether you want to connect using a host or a URL.  
**URL** | If you are connecting via URL, enter the URL of your MongoDB database here. This field is disabled if you're connecting via the host.  
**Host** | If you are connecting via host, enter the host address of your MongoDB database here.  
**Database** | Enter the name of the MongoDB database you want to connect to.  
**Replica Set** | Specify the name of the replica set if your MongoDB instance is a part of a replica set configuration.  
**Port** | Enter the port number for your MongoDB database. The default MongoDB port is `27017`.  
**Authentication** | Choose the type of authentication you want to use for the connection. For detailed guides on authentication types, please refer to the following articles:  
  
\- MongoDB Authentication  
\- [DBeaver Profile Authentication](../Authentication-DBeaver-profile/)  
  
You can also read about [security in DBeaver PRO](../Security-in-DBeaver-
PRO/).  
**Connection Details** | Provide additional connection details if necessary.  
**Driver Name** | This field will be auto-filled based on your selected driver type.  
**Driver Settings** | If there are any specific driver settings, configure them here.  
  
#### Connection details¶

The **Connection Details** section in DBeaver allows you to customize your
experience while working with MongoDB database. This includes options for
adjusting the **Navigator View** , setting up **Security measures** , applying
**Filters** , configuring **Connection Initialization** settings, and setting
up **Shell Commands**. Each of these settings can significantly impact your
database operations and workflow. For detailed guides on these settings,
please refer to the following articles:

  * [Connection Details Configuration](../Create-Connection/#connection-details)
  * [Database Navigator](../Database-Navigator/)
  * [Security Settings Guide](../Managing-security-restrictions-for-database-connection/)
  * [Filters Settings Guide](../Configure-Filters/)
  * [Connection Initialization Settings Guide](../Configure-Connection-Initialization-Settings/)
  * [Shell Commands Guide](../Working-with-Shell-Commands-in-DBeaver/)

### MongoDB driver properties¶

You can customize the MongoDB driver in DBeaver via the **Edit Driver** page,
accessible by clicking on the **Driver Settings** button on the first page of
the driver settings. This page offers a range of settings that can influence
your MongoDB database connections. For a comprehensive guide on these
settings, please refer to our [Driver manager](../Driver-Manager/) article.

### Secure Connection Configurations¶

DBeaver supports secure connections to your MongoDB database. Guidance on
configuring such connections, specifically **SSH** , **Proxy** ,
**Kubernetes** , **AWS SSM** and **SSL** connections, can be found in various
referenced articles. For a comprehensive understanding, please refer to these
articles:

  * [**SSH Configuration**](../SSH-Configuration/)

  * [**Proxy Configuration**](../Proxy-configuration/)

  * [**SSL Configuration**](../SSL-Configuration/)

  * [**Kubernetes Configuration**](../Kubernetes-configuration/)

  * [**AWS SSM**](../AWS-SSM-Configuration/)

### Secure Storage with Secret Providers¶

DBeaver supports various cloud-based secret providers to retrieve database
credentials. For detailed setup instructions, see [Secret
Providers](../Secret-Providers/).

## Powering MongoDB with DBeaver¶

DBeaver provides a host of features designed for MongoDB databases. This
includes the ability to view and manage collections, along with numerous
unique capabilities aimed at optimizing database operations.

### MongoDB database objects¶

DBeaver lets you view and manipulate a wide range of MongoDB database objects.
DBeaver has extensive support for various MongoDB metadata types, allowing you
to interact with a wide variety of database objects, such as:

  * Databases
  * Collections
  * Java Script
  * Users
  * Administration
  * Active Operations

### MongoDB features in DBeaver¶

DBeaver is not confined to handling typical SQL tasks. It also embraces the
NoSQL database spectrum, offering numerous unique features specifically
designed for MongoDB. Beyond standard SQL operations, DBeaver facilitates a
plethora of MongoDB-specific capabilities, such as:

Category | Feature  
---|---  
Data Types | BSON Data Types (e.g., Object ID, ISODate)  
Security | User-Based Access Control  
Database Management | MongoDB Stored Procedures (JavaScript Functions)  
  
Additional features compatible with MongoDB, but not exclusive to it:

Category | Feature  
---|---  
Data Transfer | [Data Import](../Data-import/)  
| [Data Export](../Data-export/)  
Session Management | [Session Manager](../Session-Manager-Guide/)  
  
#### Browsing MongoDB collections¶

You can view or edit MongoDB collection content as standard relational tables
(in grid/plain text presentations/chart) or as [JSON documents](../Working-
with-XML-and-JSON/). You can switch between these presentations using the
[toolbar](../Data-Editor/#left-sidebar) of the Data Editor.

![](../images/database/mongodb/mongodb-data-json.png)

### Database operations¶

#### Executing JavaScript¶

Execute JavaScript statements in the [SQL editor](../SQL-Editor/) as usual.
DBeaver supports all JavaScript queries for MongoDB versions 2 and 3, as well
as a subset of the `mongo` shell queries.

Here is an example that creates a user in the current database:

    
    
    db.createUser({
        user: 'testuser',
        pwd: 'test',
        roles: []
    })
    

This example returns all documents in the collection 'test_col':

    
    
    db.test_col.find()
    

Note

Scripts will be executed in the current database. You can not set an explicit
database name in your query. The current database can be changed on the SQL
Editor toolbar or on the [Database Navigator](../Database-Navigator/).

#### Executing SQL¶

You can use standard SQL statements (`SELECT`, `INSERT`, `UPDATE`, `DELETE`)
to manipulate data in MongoDB.

##### SELECT queries¶

SELECT queries can include `WHERE`, `ORDER BY`, `GROUP BY`, `JOIN` and
`HAVING` clauses.

    
    
    SELECT * FROM test_col
    WHERE propName.subProp='value'
    
    UPDATE FROM test_col
    SET propsName.val1=123
    WHERE propName.subProp='value'
    

Note

The MongoDB dialect does not support SQL sub-queries.

###### Conditions¶

SELECT queries with `WHERE` clauses support `AND`, `OR`, `<`, `<=`, `>`, `>=`,
`=` and `!=` operators:

    
    
    SELECT * FROM Employees
    WHERE (Country = 'CA' OR Country = 'RU') AND Age > 20;
    

Tip

Be aware that `AND` has a higher precedence than `OR` and will be evaluated
first; enclose it with parentheses to maintain the correct order.

###### Nested fields¶

You can differentiate nested JSON fields using a dot. Enclose fields
containing special characters (like spaces or dashes) with double quotes, as
demonstrated below:

    
    
    SELECT title FROM movies WHERE info."imdb-details".rating > 6
    

###### Working with object IDs¶

To find a document by ID, use the `ObjectId` function:

    
    
    SELECT * FROM documents
    WHERE _id = ObjectId('5f9c458018e3c69d0adc0fbd')
    ORDER BY value DESC
    

###### Working with JOINs¶

The SQL dialect for MongoDB supports `LEFT JOIN` and `INNER JOIN` currently:

    
    
    SELECT
        ar.Name as Artist,
        al.Title as Album,
        SUM(tr.Milliseconds) as Duration
    FROM Track tr
    INNER JOIN Album al ON tr.AlbumId = al.AlbumId
    INNER JOIN Artist ar ON al.ArtistId = ar.ArtistId
    GROUP BY Artist, Album
    ORDER BY Duration DESC
    

Remember to specify aliases for both the source and target tables in a defined
order, as shown:

    
    
    SELECT *
    FROM <source> <source-alias>
    INNER JOIN <target> <target-alias> ON <source-alias>.column = <target-alias>.column
    

Executing the script below does not yield a merged document but produces
separate documents for `Track` and `Album`:

    
    
    SELECT *
    FROM Track tr
    INNER JOIN Album al ON tr.AlbumId = al.AlbumId
    

###### Aggregate functions¶

In version 22.x only `COUNT` function is supported.

##### INSERT statement¶

You cannot use conditions in `INSERT` statements, only the basic form is
supported:

    
    
    INSERT INTO <collection-name> (field1, field2) VALUES (val1, val2);
    

##### UPDATE statement¶

While you can use various expressions in the `WHERE` clause, sub-selects or
joins are not permissible.

    
    
    UPDATE <collection-name> SET field2=val3 WHERE field1=val1;
    

##### DELETE statement¶

You may use any expression in the `WHERE` clause, but sub-selects or joins are
not allowed.

    
    
    DELETE FROM <collection-name> WHERE field1=val1;
    

##### CREATE TABLE statement¶

In the `CREATE TABLE` statement, only the collection name can be specified,
column lists are not allowed.

    
    
    CREATE TABLE  <collection-name>;
    

##### DROP TABLE statement¶

    
    
    DROP TABLE  <collection-name>;
    

##### Working with dates¶

When working with dates, ensure to specify them in ISO format. This is
applicable in both JavaScript and SQL dialects:

    
    
    db.dates.insert([
        { value: new Date('2016-05-18T16:00:00Z') },
        { value: new Date('2017-05-18T16:00:00Z') },
        { value: new Date('2018-05-18T16:00:00Z') },
        { value: new Date('2019-05-18T16:00:00Z') },
        { value: new Date('2020-05-18T16:00:00Z') }
    ])
    

To query data in JavaScript, follow this example:

    
    
    db.dates.find({
        value: { $gte: new Date('2018-05-18T16:00:00Z') }
    })
    

When querying data in the SQL dialect, you can use either the ISO format or
UNIX timestamp (in milliseconds):

    
    
    SELECT value FROM dates
    WHERE value > ISODate('2018-05-18T16:00:00.000Z')
    ORDER BY value DESC
    
    SELECT value FROM dates
    WHERE value > ISODate(1526659200000)
    ORDER BY value DESC
    

Back to top

