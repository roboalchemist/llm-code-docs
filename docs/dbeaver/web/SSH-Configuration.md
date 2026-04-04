# Source: https://dbeaver.com/docs/dbeaver/SSH-Configuration/

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
        * SSH configuration  [ SSH configuration  ](./) Table of contents 
          * Configure SSH tunnels 
            * Configuring Jump servers 
              * Practical use 
            * Advanced settings 
              * Port Forwarding 
              * SSH and URL based connections 
            * SSH shared tunnels 
              * SSH tunnel sharing criteria 
          * Configuring Cloud SSH Tunnels 
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
      * [ Lite edition  ](../Lite-Edition/)
      * [ Ultimate edition  ](../Ultimate-Edition/)
    * [ Release cycles  ](../DBeaver-release-cycles/)
    * [ Statistics collection  ](../Statistics-Collection/)
    * [ Customer technical support  ](../Customer-technical-support-information/)
  * [ FAQ  ](../FAQ/)

Table of contents

  * Configure SSH tunnels 
    * Configuring Jump servers 
      * Practical use 
    * Advanced settings 
      * Port Forwarding 
      * SSH and URL based connections 
    * SSH shared tunnels 
      * SSH tunnel sharing criteria 
  * Configuring Cloud SSH Tunnels 

  1. [DBeaver](/docs/dbeaver)
  2. [Configure connection](/docs/dbeaver/Create-Connection)
  3. [Network configuration](/docs/dbeaver/Network-configuration)
  4. Connection network options

# SSH configuration

Sometimes the database cannot be accessed directly, in such cases you can use
the SSH tunnel. The SSH or Secure Shell is a network communication protocol
that allows two computers to communicate and encrypts the shared data.

DBeaver supports the following SSH authentication methods:

  * Username/password
  * Public key authentication
  * Agent authentication

Available agent authentication implementations:

  * [pageant](https://www.digitalocean.com/community/tutorials/how-to-use-pageant-to-streamline-ssh-key-authentication-with-putty) _(Windows only)_
  * [ssh-agent](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

Note

You have to run the agent first before connecting to the database in DBeaver.

## Configure SSH tunnels¶

To set up **SSH** , you need to configure the following settings:

  1. Start [creating a new connection](../Create-Connection/).
  2. Click on the plus (![](../images/plus-button.png)) button and select **SSH**.

![](../images/ug/network/ssh/ssh-configuration-select-ssh.png)

  3. After selecting, an **SSH** tab will appear in the menu at the top.

![](../images/ug/network/ssh/ssh-configuration.png)

  4. In the **SSH** tab, enter the necessary configuration details:

Field | Description  
---|---  
**Host/IP** | Remote server address. Use IP or hostname (e.g. `192.168.0.10`, `myhost`).  
**Port** | SSH port (default is `22`).  
**User name** | Your SSH username.  
**Authentication method** | Choose how to authenticate: `Password`, `Public Key`, or `Agent`.  
**Password** (optional) | Enter your SSH password.  
**Save credentials** (optional) | Enable this to store credentials securely.  
  5. After configuring settings, click on **Test tunnel configuration** button to test whether all parameters are valid.

  6. Set the host in **Main** tab to `localhost`. This tells the database connection to use the remote server accessed via SSH, but tunnel I/O through your local machine.

Tip

Use [network profiles](../Network-profiles/) to save and reuse your settings
across multiple connections.

### Configuring Jump servers¶

DBeaver allows the use of Jump servers, also known as Gateway hosts. This
feature is essential when the direct access to a target machine is not
possible from your local machine, and a gateway server is required for
connection.

![](../images/ug/network/ssh/jump-server-configuration.png)

To add a jump server:

  1. Ensure **Use SSH Tunnel** is checked.
  2. Expand the **Jump servers** group.
  3. Specify your target in the **Settings** section.
  4. Click on the **Create new jump host** button ![](../images/ug/network/ssh/Create-new-jump-host-button.png) to add your first jump server configuration.

Repeat step 3 for each additional jump host you need to add, configuring each
one within the **Settings** section.

#### Practical use¶

Imagine you have the following situation: your database is located on remote
machine with IP address `100.100.100.100` and which is accessible through SSH.
You cannot access this IP directly from your machine because of your network
settings or firewall, but you can access other machines with the IP address
`200.200.200.200` through SSH and which **is able** to access the desired
remote machine. You will need to specify `100.100.100.100` as a host in
regular SSH configuration and `200.200.200.200` as a host in a gateway
configuration to achieve such a "connection order": `localhost` →
`200.200.200.200` → `100.100.100.100`.

### Advanced settings¶

![](../images/ug/network/ssh/advanced-options.png)

Setting | Description  
---|---  
Implementation | Specifies the SSH library used for the connection.  
Bypass host verification | If checked, disables verification of the server's identity by not checking the remote host's fingerprint, which may lead to security risks such as Man-In-The-Middle attacks.  
Share this tunnel with other connections | If checked, allows multiple connections to share the same SSH tunnel. This can improve connection speed and reduce server load. Sessions remain open until all connections using the tunnel are closed, even if the initiating connection is terminated.  
Keep-Alive interval (ms) | Sets the interval in milliseconds for sending a keep-alive packet to keep the connection active. A value of 0 disables keep-alive packets.  
Tunnel connect timeout (ms) | Sets the maximum time in milliseconds to establish a tunnel connection before timing out.  
  
#### Port Forwarding¶

Port forwarding is used to expose a socket sitting on a remote port to your
local port, allowing you to communicate with it. After the SSH connection to
the remote machine is established, you need to connect to the database on that
machine. You must pass the port on which the database is listening from that
remote machine to your local machine. This is when port forwarding becomes
handy.

By default, it randomly chooses the local port and forwards it to the
destination port set in **Connection settings - > Main**

It is not usually required to change this configuration, but it can be useful,
for example, when you want to use a particular local port.

#### SSH and URL based connections¶

By default DBeaver opens random local port and forwards it to a target
database port. It then implicitly replaces port configured in the connection
with this random port. So technically DBeaver will connect to something like
`localhost:45678` (random port on localhost) instead of
`database.server.domain:5432` (default PostgreSQL server port). But if you use
URL instead of manual connection configuration then you connect to
`jdbc:postgresql://database.server.domain/postgresql`. DBeaver cannot replace
port number automatically because you can use any type of sophisticated URLs.
DBeaver just don't know how to change this URL.

If you use URL connection then you must configure port forwarding manually. In
the Advanced Settings set both Local Port and Remote Port to 5432 (database
server port, 5432 is the default value for PostgreSQL). It will work in most
cases. But it will fail if you have PostgreSQL server on your local machine
because port 5432 is already occupied. In this case you can use any random
port number for Loca Port (e.g. 15432). Use the same 5432 for Remote Port
because it is real port number for remote PostgreSQL server.

### SSH shared tunnels¶

By default, DBeaver shares SSH tunnels across connections when the same SSH
settings are used. This is particularly useful when connecting to several
databases on the same remote server, as it avoids the need to establish a
separate SSH tunnel for each connection.

To view the active SSH tunnels and the databases utilizing a shared tunnel,
use the **SSH tunnel explorer**. This feature provides a comprehensive
overview of your SSH tunnel usage, including detailed information on each
tunnel and the databases it serves. Here is how to access **SSH tunnel
explorer** :

  1. Navigate to **Window - > Show View -> Other...**
  2. In the window that appears, expand the **Database** category.
  3. Select **SSH tunnel explorer** and click **Open**.

In the **SSH tunnel explorer** view, you will find information about each
active tunnel. This includes:

Field | Description  
---|---  
**Destination** | The remote server to which the tunnel connects.  
**Used by** | A list of databases that are currently using the tunnel.  
**Port Forwards** | The local and remote ports involved in the tunneling process.  
  
#### SSH tunnel sharing criteria¶

DBeaver shares SSH tunnels across connections if SSH settings are identical.
The application compares the following parameters to determine if the SSH
settings match:

  * **Hostname** : The address of the SSH server.
  * **Host port** : The port number used for the SSH connection.
  * **Username** : The username required for SSH authentication.

Depending on the authentication method selected, DBeaver also compares:

  * For password authentication:
    * **Password** : The SSH account password.
  * For public key authentication:
    * **Private Key** : The file path to the SSH private key.
    * **Passphrase** : The passphrase for decrypting the private key, if set.
  * For agent authentication:
  * **Agents** : DBeaver treats all agent authentication configurations as identical, ignoring specific agent settings and focusing only on the method's selection.

## Configuring Cloud SSH Tunnels¶

  * To configure Cloud SSH Tunnels, start by navigating to the **Cloud Explorer** button ![](../images/ug/cloud-explorer/cloud-explorer-button.png) in the Toolbar.
  * Select **Edit** button ![](../images/ug/cloud-explorer/edit-configuration-button.png) for an existing connection or **New** button ![](../images/plus-button.png) to create a new connection.
  * In the opened window, go to the **Tunnels** tab.

![](../images/ug/cloud-explorer/ssh-cloud-tunnel-configuration.png)

  * This tab allows you to set up SSH tunnels specifically for cloud connections.

  * The configuration here is similar to the standard SSH setup, but it's integrated within your cloud service provider's settings.

Back to top

