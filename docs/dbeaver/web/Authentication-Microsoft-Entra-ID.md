# Source: https://dbeaver.com/docs/dbeaver/Authentication-Microsoft-Entra-ID/

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
      * Microsoft Entra ID  [ Microsoft Entra ID  ](./) Table of contents 
        * Prerequisites 
          * Microsoft Entra ID configuration 
        * Configure an authentication type 
          * Default credentials 
            * Environment variables 
              * macOS 
              * Linux 
              * Windows 
          * Enterprise application 
          * Client secret 
          * Client certificate 
        * Troubleshooting 
          * Authentication fails 
          * Group-based authentication fails 
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
      * [ Lite edition  ](../Lite-Edition/)
      * [ Ultimate edition  ](../Ultimate-Edition/)
    * [ Release cycles  ](../DBeaver-release-cycles/)
    * [ Statistics collection  ](../Statistics-Collection/)
    * [ Customer technical support  ](../Customer-technical-support-information/)
  * [ FAQ  ](../FAQ/)

Table of contents

  * Prerequisites 
    * Microsoft Entra ID configuration 
  * Configure an authentication type 
    * Default credentials 
      * Environment variables 
        * macOS 
        * Linux 
        * Windows 
    * Enterprise application 
    * Client secret 
    * Client certificate 
  * Troubleshooting 
    * Authentication fails 
    * Group-based authentication fails 

  1. [DBeaver](/docs/dbeaver)
  2. [Configure connection](/docs/dbeaver/Create-Connection)
  3. Database authentication models

# Microsoft Entra ID

Note

This feature is available in [Lite](../Lite-Edition/),
[Enterprise](../Enterprise-Edition/), [Ultimate](../Ultimate-Edition/) and
[Team](https://dbeaver.com/docs/team-edition/) editions only.

DBeaver comes with Microsoft Entra ID (formerly Azure AD) authentication
support, allowing secure access to your databases.

Info

The official [Entra documentation](https://learn.microsoft.com/en-us/entra/).

## Prerequisites¶

Make sure you have:

  * an active Azure account with the appropriate permissions
  * a Microsoft Entra ID application is registered and configured by your administrator.

Info

For more details on permissions, see [Azure permissions](../Azure-
Permissions/).

### Microsoft Entra ID configuration¶

To enable authorization with the Microsoft platform, you need a registered
application in Azure. If one doesn't exist, create and configure it as
follows:

  1. **Register an application** Create a new enterprise application in Microsoft Entra by following the steps in the [official Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app?tabs=certificate#register-an-application).

  2. **Configure application secrets** DBeaver uses the OpenID Connect protocol for authorization with Microsoft Entra ID. To enable this, configure application secrets. Detailed instructions are available in the [official Microsoft documentation](https://learn.microsoft.com/en-us/entra/identity-platform/security-best-practices-for-app-registration).

Important

Record the value of the client secret immediately after creating it. It can
only be viewed once. If you miss this step, youâll need to create a new
secret.

## Configure an authentication type¶

### Default credentials¶

Use this when you do not want to store secrets in DBeaver.

![](../images/auth_methods/Entra_ID/entra-id-authentication-default-
credentials.png)

  1. Open **Edit connection**.
  2. On **Connection settings** , set **Credentials** to **Default credentials**.
  3. (Optional) If database access is granted through an Entra ID group, enter the **AD Group name**.
  4. (Optional) Review **Use legacy token permissions**.

     * keep it unchecked in almost all cases
     * enable it only if your DBA or admin specifically instructs you

Info

This option forces the connection to use older token scopes and claim formats
for backward compatibility with databases or drivers that donât fully
support modern Microsoft Entra ID permissions.

  5. Click **Test connection** , then **Save**.

Tip

To see how DefaultAzureCredential picks a provider, see
[DefaultAzureCredential overview](https://learn.microsoft.com/en-
us/azure/developer/java/sdk/authentication/credential-
chains#defaultazurecredential-overview).

#### Environment variables¶

Set these **before** starting DBeaver if you want to guide how the SDK gets a
token.

  * **If you use the environment-variable credential**

    * `AZURE_CLIENT_ID` â your appâs client ID
    * `AZURE_TENANT_ID` â your Microsoft Entra directory (tenant) ID
    * then either:
      * `AZURE_CLIENT_SECRET`, or
      * `AZURE_CLIENT_CERTIFICATE_PATH` and `AZURE_CLIENT_CERTIFICATE_PASSWORD` (optional, for `.pfx`)
  * **If you use managed identity**

    * for a **user-assigned** identity: `AZURE_CLIENT_ID`
    * for a **system-assigned** identity: no variables are required
    * _(available only in Azure environments like VM, App Service, or Function App)_

##### macOS¶

    
    
    launchctl setenv AZURE_CLIENT_ID <value>
    launchctl setenv AZURE_TENANT_ID <value>
    # optional
    launchctl setenv AZURE_CLIENT_SECRET <value>
    launchctl setenv AZURE_CLIENT_CERTIFICATE_PATH /path/to/cert.pfx
    launchctl setenv AZURE_CLIENT_CERTIFICATE_PASSWORD <value>
    

Tip

Restart DBeaver (or log out and back in) after running these commands.
Variables set with `launchctl` are visible only to new GUI apps.

##### Linux¶

    
    
    export AZURE_CLIENT_ID=<value>
    export AZURE_TENANT_ID=<value>
    # optional
    export AZURE_CLIENT_SECRET=<value>
    export AZURE_CLIENT_CERTIFICATE_PATH=/path/to/cert.pfx
    export AZURE_CLIENT_CERTIFICATE_PASSWORD=<value>
    

Tip

These variables work only in the current terminal session. Add them to
`~/.bashrc` or `~/.profile` to make them persistent when is launched from the
desktop.

##### Windows¶

Set variables as **User variables** in **System Properties - Environment
Variables** , then restart DBeaver.

Or set them from PowerShell:

    
    
    setx AZURE_CLIENT_ID "<value>"
    setx AZURE_TENANT_ID "<value>"
    # optional
    setx AZURE_CLIENT_SECRET "<value>"
    setx AZURE_CLIENT_CERTIFICATE_PATH "C:\path\to\cert.pfx"
    setx AZURE_CLIENT_CERTIFICATE_PASSWORD "<value>"
    

### Enterprise application¶

Use this for user sign-in without storing a secret in DBeaver.

![](../images/auth_methods/Entra_ID/entra-id-authentication-enterprise-
application.png)

  1. Open **Edit connection**.
  2. Set **Credentials** to **Enterprise application**.
  3. Enter the values below:

Field in DBeaver | What to enter | Where to find in the Azure portal | Reference  
---|---|---|---  
**Client ID** | Your applicationâs **Application (client) ID** | Microsoft Entra ID - App registrations - **Your app** \- **Overview** | [Copy the application ID (client ID)](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#copy-the-application-id-client-id)  
**Tenant ID** | Your **Directory (tenant) ID** | Microsoft Entra ID - **Overview** \- **Tenant ID** | [Find your tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)  
**AD Group name** (Optional) | The exact Entra **group name** that was granted database access | Microsoft Entra ID - **Groups** \- **Your group** \- **Overview** | [Create a group and add members](https://learn.microsoft.com/en-us/entra/fundamentals/quickstart-create-group-add-members)  
  4. (Optional) Review **Use legacy token permissions**.

     * keep it unchecked in almost all cases
     * enable it only if your DBA or admin specifically instructs you

Info

This option forces the connection to use older token scopes and claim formats
for backward compatibility with databases or drivers that donât fully
support modern Microsoft Entra ID permissions.

  5. Click **Test connection** , then **Save**.

Info

For information on creating the application in Azure, see [Register an
app](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-
register-app).

### Client secret¶

Use this for service connections where an app authenticates with a secret.

![](../images/auth_methods/Entra_ID/entra-id-authentication-client-secret.png)

  1. Open **Edit connection**.
  2. Set **Credentials** to **Client secret**.
  3. Enter the values below:

Field in DBeaver | What to enter | Where to find in the Azure portal | Reference  
---|---|---|---  
**Client ID** | Your appâs **Application (client) ID** | Microsoft Entra ID - **App registrations** \- **Your app** \- **Overview** | [Copy the client ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#copy-the-application-id-client-id)  
**Tenant ID** | Your **Directory (tenant) ID** | Microsoft Entra ID - **Overview** \- **Tenant ID** | [Find your tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)  
**Client secret** | The secret **Value** (not the Secret ID) | **Your app** \- **Certificates & secrets** \- **Client secrets** | [Add a client secret](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret)  
**AD Group name** (Optional) | The exact Entra **group name** that was granted database access | Microsoft Entra ID - **Groups** \- **Your group** \- **Overview** | [Create a group and add members](https://learn.microsoft.com/en-us/entra/fundamentals/quickstart-create-group-add-members)  
  4. (Optional) Review **Use legacy token permissions**.

     * keep it unchecked in almost all cases
     * enable it only if your DBA or admin specifically instructs you

Info

This option forces the connection to use older token scopes and claim formats
for backward compatibility with databases or drivers that donât fully
support modern Microsoft Entra ID permissions.

  5. Click **Test connection** , then **Save**.

Info

For information on creating the secret in Azure, see [Add a client
secret](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-
credentials?tabs=client-secret).

### Client certificate¶

Use this when your org prefers certificates to secrets.

![](../images/auth_methods/Entra_ID/entra-id-authentication-client-
certificate.png)

  1. Open **Edit connection**.
  2. Set **Credentials** to **Client certificate**.
  3. Enter the values below:

Field in DBeaver | What to enter | Where to find in the Azure portal | Reference  
---|---|---|---  
**Client ID** | Your appâs **Application (client) ID** | Microsoft Entra ID - **App registrations** \- **Your app** \- **Overview** | [Copy the client ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app#copy-the-application-id-client-id)  
**Tenant ID** | Your **Directory (tenant) ID** | Microsoft Entra ID - **Overview** \- **Tenant ID** | [Find your tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)  
**Client certificate path** | Local path to the private-key file | You generate the cert locally and upload the **public** cert to **Your app** \- **Certificates & secrets** \- **Certificates** | [Certificate credentials](https://learn.microsoft.com/en-us/entra/identity-platform/certificate-credentials)  
**Client certificate password** (Optional) | Password for the `.pfx`, if set when exporting | Set during export of the `.pfx` on your machine | [Certificate credentials](https://learn.microsoft.com/en-us/entra/identity-platform/certificate-credentials)  
**AD Group name** (Optional) | Exact **group name** that has database access | Microsoft Entra ID - **Groups** \- **Your group** \- **Overview** | [Create a group and add members](https://learn.microsoft.com/en-us/entra/fundamentals/quickstart-create-group-add-members)  
  4. (Optional) Review **Use legacy token permissions**.

     * keep it unchecked in almost all cases
     * enable it only if your DBA or admin specifically instructs you

Info

This option forces the connection to use older token scopes and claim formats
for backward compatibility with databases or drivers that donât fully
support modern Microsoft Entra ID permissions.

  5. Click **Test connection** , then **Save**.

Info

For information on certificate credentials in Azure, see [Certificate
credentials](https://learn.microsoft.com/en-us/entra/identity-
platform/certificate-credentials).

## Troubleshooting¶

### Authentication fails¶

  * Check that the **Client ID** and **Tenant ID** match the [registered application in Azure](https://learn.microsoft.com/en-us/azure/active-directory/develop/howto-add-app-roles-in-azure-ad-apps#find-the-application-id-and-directory-tenant-id).
  * Make sure the user is assigned in the [Azure portal](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/assign-user-or-group-access-portal).
  * Confirm the app has the required [API permissions or roles](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent).
  * Make sure required [tenant-wide admin consent](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/grant-admin-consent) was granted by the user or an admin.

### Group-based authentication fails¶

If you're using an Entra ID security group to connect to Azure Database for
PostgreSQL and see an error like:

    
    
    password authentication failed for user "<group-name>"
    

Check the following:

  * The Entra ID user is a [member of the group](https://learn.microsoft.com/en-us/entra/fundamentals/quickstart-create-group-add-members).
  * The group has [database access granted in PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-configure-sign-in-azure-ad-authentication#grant-database-access).
  * Youâre using an authentication method that supports Entra ID tokens (like **Default credentials** or **Enterprise application**).
  * The access token includes group claims, and the [required API permissions were granted by an admin](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-permissions-and-consent).
  * Enter the group name in the **AD Group name** field of the connection settings in DBeaver.

Back to top

