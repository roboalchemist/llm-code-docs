# Source: https://dbeaver.com/docs/dbeaver/Kerberos-Authentication/

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
      * Kerberos  [ Kerberos  ](./) Table of contents 
        * Supported databases 
        * Settings 
        * Extra configuration 
          * Using the kinit 
          * Using the keytab file 
            * Windows specifics 
          * Local Kerberos configuration file 
        * Additional settings 
        * Troubleshooting 
          * Oracle JDBC driver and Kerberos authentication 
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
      * [ Lite edition  ](../Lite-Edition/)
      * [ Ultimate edition  ](../Ultimate-Edition/)
    * [ Release cycles  ](../DBeaver-release-cycles/)
    * [ Statistics collection  ](../Statistics-Collection/)
    * [ Customer technical support  ](../Customer-technical-support-information/)
  * [ FAQ  ](../FAQ/)

Table of contents

  * Supported databases 
  * Settings 
  * Extra configuration 
    * Using the kinit 
    * Using the keytab file 
      * Windows specifics 
    * Local Kerberos configuration file 
  * Additional settings 
  * Troubleshooting 
    * Oracle JDBC driver and Kerberos authentication 

  1. [DBeaver](/docs/dbeaver)
  2. [Configure connection](/docs/dbeaver/Create-Connection)
  3. Database authentication models

# Kerberos

Note

This feature is available in [Lite](../Lite-Edition/),
[Enterprise](../Enterprise-Edition/), [Ultimate](../Ultimate-Edition/) and
[Team](https://dbeaver.com/docs/team-edition/) editions only.

DBeaver includes support for Kerberos authentication, enabling secure
connections to your databases.

![](../images/auth_methods/Kerberos/kerberos-authentication.png)

Kerberos authentication is a secure method for verifying user identities over
non-secure networks. It is widely used in various environments, especially in
database management systems, to ensure that communication between the client
and server remains encrypted and authenticated.

This guide is designed to help you configure Kerberos authentication on the
client machine, where DBeaver is installed. It assumes that the Kerberos Key
Distribution Center (KDC) and the necessary server configurations have already
been completed.

## Supported databases¶

  * [AlloyDB](../Database-driver-AlloyDB-for-PostgreSQL/)
  * Cockroach
  * [Db2 for LUW](../Database-driver-IBM-Db2/)

Note

Kerberos authentication is only supported with [version 11.x of the Db2
driver](https://www.ibm.com/docs/en/db2/11.1.0).

  * EnterpriseDB (EDB)

  * Fujitsu
  * [Greenplum](../Database-driver-Greenplum/)
  * HANA
  * [MariaDB](../Database-driver-MariaDB/)
  * [MySQL](../Database-driver-MySQL/)
  * [Oracle](../Oracle/)
  * [PostgreSQL](../Database-driver-PostgreSQL/)
  * PrestoDB
  * PrestoSQL
  * [Redshift](../Database-driver-Amazon-Redshift/)
  * [Teradata](../Database-driver-Teradata/)
  * TimescaleDB
  * [Trino](../Database-driver-Trino/)
  * [Yellowbrick](../Database-driver-Yellowbrick/)
  * YugabyteDB

## Settings¶

The table below lists the basic settings required for Kerberos authentication
in DBeaver. These settings are essential for establishing a secure connection
to your database using Kerberos, providing user identification,
authentication, and access control.

Setting | Description  
---|---  
**Username** | Specifies the name of the user or role within the database. This is the identity under which you will connect to your database.  
**Kerberos user** | A unique identity in the Kerberos system to which Kerberos can assign tickets, enabling access to services that are Kerberos-aware.  
**Realm** | The domain over which a Kerberos authentication server can authenticate users, hosts, or services. It's often the uppercase version of the DNS domain name it oversees.  
**KDC Server** | The hostname of your Kerberos Key Distribution Center (KDC), which is a service that provides session tickets and keys within an Active Directory domain.  
**Password** | The password associated with your Kerberos user. This method involves directly entering your password. It's a simple, manual process suitable for environments where automated authentication methods are not preferred or available.  
  
Below are additional Kerberos authentication settings for advanced
configuration:

Extra configuration | Description  
---|---  
**Use kinit** | When selected, it indicates the use of the `kinit` tool on your machine, which obtains and caches an initial ticket-granting ticket. Generally, you only need to provide your Kerberos username when this option is selected. Selecting this option makes the **Password** field inactive because authentication is managed through the ticket obtained by `kinit`.  
**Use keytab** | A checkbox option for those who prefer to use a keytab file instead of manually entering a password. Selecting this option also makes the **Password** field inactive because the keytab file contains encrypted keys that the Kerberos system uses for authentication.  
**Custom krb5.conf** | Allows you to specify the path to your local Kerberos configuration file. This file contains settings that define the Kerberos realms, KDCs, and other parameters for your environment.  
**Debug Kerberos Connection** | A checkbox that, when selected, enables the logging of detailed Kerberos connection information in your [log files](../Log-files/).  
  
Note

Some settings may be stored in a session cache. If you have updated the
settings and still encounter connection issues, restarting DBeaver might be
necessary to apply the changes effectively.

## Extra configuration¶

The **Extra configuration** section within DBeaver's connection settings
offers advanced options for customizing the Kerberos. This section allows
users to specify detailed settings, such as the use of a keytab file, `kinit`
commands, or a custom `krb5.conf`/`krb5.ini` file.

### Using the kinit¶

The `kinit` command is a utility Kerberos provides to obtain and cache an
initial ticket-granting ticket (TGT).

In the context of using DBeaver, the `kinit` command streamlines the
authentication process by obtaining and caching an initial ticket-granting
ticket (TGT). This mechanism enables users to authenticate against Kerberos-
enabled services, reducing the need for continuous password inputs during the
session.

To configure Kerberos authentication using `kinit` command, follow these
steps:

  1. Make sure you have a valid Kerberos ticket-granting ticket (TGT), which can be obtained using the `kinit` command. For a detailed guide, refer to the [official documentation](https://www.ibm.com/docs/en/aix/7.3?topic=k-kinit-command) on `kinit` command.
  2. Specify the path to your `kinit` tool in the **Extra Configuration** section in the **Use kinit** field.
  3. Try connecting to your database. With these settings, DBeaver will use the `kinit` command for authentication.

![](../images/auth_methods/Kerberos/kerberos-kinit-settings.png)

### Using the keytab file¶

A keytab is a file containing pairs of Kerberos principals and encrypted keys
derived from the Kerberos password. It enables authentication to various
remote systems using Kerberos without entering a password.

In the context of using DBeaver, the keytab file simplifies the authentication
process by requiring the user to provide all necessary credentials except the
password.

To configure Kerberos authentication using a keytab file, follow these steps:

  1. Utilize the `ktutil` command-line utility to generate a keytab file. This involves adding entries for your principals along with their encrypted keys. For comprehensive instructions on creating a keytab file, consult the [official documentation](https://www.ibm.com/docs/en/pasc/1.1.1?topic=file-creating-kerberos-principal-keytab) on creating a Kerberos keytab file.
  2. Specify the path to your keytab file in the **Extra Configuration** section in the **Use keytab** field.
  3. Attempt to connect to your database. DBeaver will utilize the specified keytab file for authentication.

![](../images/auth_methods/Kerberos/kerberos-keytab-settings.png)

#### Windows specifics¶

On Linux and macOS, `kinit` and keytab files are supported natively. However,
Windows does not support these functionalities natively. To enable these
features, Windows users need to install additional software.

A key tool for Windows users is [MIT Kerberos](https://ist.mit.edu/mit-
apps/kerberos-win) for Windows. It allows the use of `kinit` and provides
utilities for managing keytab files, bridging the gap between Windows and
Kerberos authentication standards.

### Local Kerberos configuration file¶

If you have a custom Kerberos configuration file (`krb5.conf`/`krb5.ini`),
input the complete file path in the **Custom krb5.conf** field.

The configuration file includes necessary configuration details such as KDCs
and admin server locations for Kerberos realms, default values for the current
Realm, and hostname to Kerberos realm mappings. If a custom configuration file
path is provided, it is not necessary to fill in the standard authentication
fields, as the configuration file contains all the required information.

## Additional settings¶

When configuring PrestoSQL and Trino connections, especially in environments
that utilize Kerberos authentication and SSL, certain additional settings
might be necessary for connection:

Setting | Description  
---|---  
**Service name** | Add the Kerberos service name of the remote coordinator.  
**Use SSL from JKS** | Check this setting and manually add the file path to your `.jks` file if you need an SSL certificate from a JKS file. This is useful when the server's SSL certificate is not automatically trusted. If your JKS file is password-protected, add the password to the **SSL JKS Password** field to allow database to access the keystone.  
**SSL JKS Password** | For additional security, the JKS file is password-protected. Add the password to the "SSL JKS" field to allow database to access the keystone.  
  
## Troubleshooting¶

### Oracle JDBC driver and Kerberos authentication¶

When configuring Kerberos authentication for Oracle databases, it is important
to be aware of compatibility issues with certain JDBC driver versions.
Specifically, Oracle JDBC driver version 21 has been known to cause issues
with Kerberos authentication, often not working with older configurations.

To ensure Kerberos authentication functions properly with Oracle databases, it
is recommended to use an older version of the Oracle JDBC driver. Versions
12.x or 19.x are known to be compatible and should be used for Kerberos
authentication. By selecting one of these older driver versions, you can avoid
the authentication problems introduced in version 21.

Back to top

