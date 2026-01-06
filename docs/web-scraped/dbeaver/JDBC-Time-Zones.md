# Source: https://dbeaver.com/docs/dbeaver/JDBC-Time-Zones/

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
      * [ JDBC time zones  ](./)
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

  1. [DBeaver](/docs/dbeaver)
  2. [Configure connection](/docs/dbeaver/Create-Connection)
  3. Driver settings

# JDBC time zones

ID | Display Name | GMT shift  
---|---|---  
Africa/Abidjan | Greenwich Mean Time | 0.0  
Africa/Accra | Ghana Mean Time | 0.0  
Africa/Addis_Ababa | Eastern African Time | 3.0  
Africa/Algiers | Central European Time | 1.0  
Africa/Asmara | Eastern African Time | 3.0  
Africa/Asmera | Eastern African Time | 3.0  
Africa/Bamako | Greenwich Mean Time | 0.0  
Africa/Bangui | Western African Time | 1.0  
Africa/Banjul | Greenwich Mean Time | 0.0  
Africa/Bissau | Greenwich Mean Time | 0.0  
Africa/Blantyre | Central African Time | 2.0  
Africa/Brazzaville | Western African Time | 1.0  
Africa/Bujumbura | Central African Time | 2.0  
Africa/Cairo | Eastern European Time | 2.0  
Africa/Casablanca | Western European Time | 0.0  
Africa/Ceuta | Central European Time | 1.0  
Africa/Conakry | Greenwich Mean Time | 0.0  
Africa/Dakar | Greenwich Mean Time | 0.0  
Africa/Dar_es_Salaam | Eastern African Time | 3.0  
Africa/Djibouti | Eastern African Time | 3.0  
Africa/Douala | Western African Time | 1.0  
Africa/El_Aaiun | Western European Time | 0.0  
Africa/Freetown | Greenwich Mean Time | 0.0  
Africa/Gaborone | Central African Time | 2.0  
Africa/Harare | Central African Time | 2.0  
Africa/Johannesburg | South Africa Standard Time | 2.0  
Africa/Juba | Eastern African Time | 3.0  
Africa/Kampala | Eastern African Time | 3.0  
Africa/Khartoum | Eastern African Time | 3.0  
Africa/Kigali | Central African Time | 2.0  
Africa/Kinshasa | Western African Time | 1.0  
Africa/Lagos | Western African Time | 1.0  
Africa/Libreville | Western African Time | 1.0  
Africa/Lome | Greenwich Mean Time | 0.0  
Africa/Luanda | Western African Time | 1.0  
Africa/Lubumbashi | Central African Time | 2.0  
Africa/Lusaka | Central African Time | 2.0  
Africa/Malabo | Western African Time | 1.0  
Africa/Maputo | Central African Time | 2.0  
Africa/Maseru | South Africa Standard Time | 2.0  
Africa/Mbabane | South Africa Standard Time | 2.0  
Africa/Mogadishu | Eastern African Time | 3.0  
Africa/Monrovia | Greenwich Mean Time | 0.0  
Africa/Nairobi | Eastern African Time | 3.0  
Africa/Ndjamena | Western African Time | 1.0  
Africa/Niamey | Western African Time | 1.0  
Africa/Nouakchott | Greenwich Mean Time | 0.0  
Africa/Ouagadougou | Greenwich Mean Time | 0.0  
Africa/Porto-Novo | Western African Time | 1.0  
Africa/Sao_Tome | Greenwich Mean Time | 0.0  
Africa/Timbuktu | Greenwich Mean Time | 0.0  
Africa/Tripoli | Eastern European Time | 2.0  
Africa/Tunis | Central European Time | 1.0  
Africa/Windhoek | Western African Time | 1.0  
America/Adak | Hawaii Standard Time | -10.0  
America/Anchorage | Alaska Standard Time | -9.0  
America/Anguilla | Atlantic Standard Time | -4.0  
America/Antigua | Atlantic Standard Time | -4.0  
America/Araguaina | Brasilia Time | -3.0  
America/Argentina/Buenos_Aires | Argentine Time | -3.0  
America/Argentina/Catamarca | Argentine Time | -3.0  
America/Argentina/ComodRivadavia | Argentine Time | -3.0  
America/Argentina/Cordoba | Argentine Time | -3.0  
America/Argentina/Jujuy | Argentine Time | -3.0  
America/Argentina/La_Rioja | Argentine Time | -3.0  
America/Argentina/Mendoza | Argentine Time | -3.0  
America/Argentina/Rio_Gallegos | Argentine Time | -3.0  
America/Argentina/Salta | Argentine Time | -3.0  
America/Argentina/San_Juan | Argentine Time | -3.0  
America/Argentina/San_Luis | Argentine Time | -3.0  
America/Argentina/Tucuman | Argentine Time | -3.0  
America/Argentina/Ushuaia | Argentine Time | -3.0  
America/Aruba | Atlantic Standard Time | -4.0  
America/Asuncion | Paraguay Time | -4.0  
America/Atikokan | Eastern Standard Time | -5.0  
America/Atka | Hawaii Standard Time | -10.0  
America/Bahia | Brasilia Time | -3.0  
America/Bahia_Banderas | Central Standard Time | -6.0  
America/Barbados | Atlantic Standard Time | -4.0  
America/Belem | Brasilia Time | -3.0  
America/Belize | Central Standard Time | -6.0  
America/Blanc-Sablon | Atlantic Standard Time | -4.0  
America/Boa_Vista | Amazon Time | -4.0  
America/Bogota | Colombia Time | -5.0  
America/Boise | Mountain Standard Time | -7.0  
America/Buenos_Aires | Argentine Time | -3.0  
America/Cambridge_Bay | Mountain Standard Time | -7.0  
America/Campo_Grande | Amazon Time | -4.0  
America/Cancun | Eastern Standard Time | -5.0  
America/Caracas | Venezuela Time | -4.0  
America/Catamarca | Argentine Time | -3.0  
America/Cayenne | French Guiana Time | -3.0  
America/Cayman | Eastern Standard Time | -5.0  
America/Chicago | Central Standard Time | -6.0  
America/Chihuahua | Mountain Standard Time | -7.0  
America/Coral_Harbour | Eastern Standard Time | -5.0  
America/Cordoba | Argentine Time | -3.0  
America/Costa_Rica | Central Standard Time | -6.0  
America/Creston | Mountain Standard Time | -7.0  
America/Cuiaba | Amazon Time | -4.0  
America/Curacao | Atlantic Standard Time | -4.0  
America/Danmarkshavn | Greenwich Mean Time | 0.0  
America/Dawson | Pacific Standard Time | -8.0  
America/Dawson_Creek | Mountain Standard Time | -7.0  
America/Denver | Mountain Standard Time | -7.0  
America/Detroit | Eastern Standard Time | -5.0  
America/Dominica | Atlantic Standard Time | -4.0  
America/Edmonton | Mountain Standard Time | -7.0  
America/Eirunepe | Acre Time | -5.0  
America/El_Salvador | Central Standard Time | -6.0  
America/Ensenada | Pacific Standard Time | -8.0  
America/Fort_Nelson | Mountain Standard Time | -7.0  
America/Fort_Wayne | Eastern Standard Time | -5.0  
America/Fortaleza | Brasilia Time | -3.0  
America/Glace_Bay | Atlantic Standard Time | -4.0  
America/Godthab | Western Greenland Time | -3.0  
America/Goose_Bay | Atlantic Standard Time | -4.0  
America/Grand_Turk | Atlantic Standard Time | -4.0  
America/Grenada | Atlantic Standard Time | -4.0  
America/Guadeloupe | Atlantic Standard Time | -4.0  
America/Guatemala | Central Standard Time | -6.0  
America/Guayaquil | Ecuador Time | -5.0  
America/Guyana | Guyana Time | -4.0  
America/Halifax | Atlantic Standard Time | -4.0  
America/Havana | Cuba Standard Time | -5.0  
America/Hermosillo | Mountain Standard Time | -7.0  
America/Indiana/Indianapolis | Eastern Standard Time | -5.0  
America/Indiana/Knox | Central Standard Time | -6.0  
America/Indiana/Marengo | Eastern Standard Time | -5.0  
America/Indiana/Petersburg | Eastern Standard Time | -5.0  
America/Indiana/Tell_City | Central Standard Time | -6.0  
America/Indiana/Vevay | Eastern Standard Time | -5.0  
America/Indiana/Vincennes | Eastern Standard Time | -5.0  
America/Indiana/Winamac | Eastern Standard Time | -5.0  
America/Indianapolis | Eastern Standard Time | -5.0  
America/Inuvik | Mountain Standard Time | -7.0  
America/Iqaluit | Eastern Standard Time | -5.0  
America/Jamaica | Eastern Standard Time | -5.0  
America/Jujuy | Argentine Time | -3.0  
America/Juneau | Alaska Standard Time | -9.0  
America/Kentucky/Louisville | Eastern Standard Time | -5.0  
America/Kentucky/Monticello | Eastern Standard Time | -5.0  
America/Knox_IN | Central Standard Time | -6.0  
America/Kralendijk | Atlantic Standard Time | -4.0  
America/La_Paz | Bolivia Time | -4.0  
America/Lima | Peru Time | -5.0  
America/Los_Angeles | Pacific Standard Time | -8.0  
America/Louisville | Eastern Standard Time | -5.0  
America/Lower_Princes | Atlantic Standard Time | -4.0  
America/Maceio | Brasilia Time | -3.0  
America/Managua | Central Standard Time | -6.0  
America/Manaus | Amazon Time | -4.0  
America/Marigot | Atlantic Standard Time | -4.0  
America/Martinique | Atlantic Standard Time | -4.0  
America/Matamoros | Central Standard Time | -6.0  
America/Mazatlan | Mountain Standard Time | -7.0  
America/Mendoza | Argentine Time | -3.0  
America/Menominee | Central Standard Time | -6.0  
America/Merida | Central Standard Time | -6.0  
America/Metlakatla | Alaska Standard Time | -9.0  
America/Mexico_City | Central Standard Time | -6.0  
America/Miquelon | Pierre & Miquelon Standard Time | -3.0  
America/Moncton | Atlantic Standard Time | -4.0  
America/Monterrey | Central Standard Time | -6.0  
America/Montevideo | Uruguay Time | -3.0  
America/Montreal | Eastern Standard Time | -5.0  
America/Montserrat | Atlantic Standard Time | -4.0  
America/Nassau | Eastern Standard Time | -5.0  
America/New_York | Eastern Standard Time | -5.0  
America/Nipigon | Eastern Standard Time | -5.0  
America/Nome | Alaska Standard Time | -9.0  
America/Noronha | Fernando de Noronha Time | -2.0  
America/North_Dakota/Beulah | Central Standard Time | -6.0  
America/North_Dakota/Center | Central Standard Time | -6.0  
America/North_Dakota/New_Salem | Central Standard Time | -6.0  
America/Ojinaga | Mountain Standard Time | -7.0  
America/Panama | Eastern Standard Time | -5.0  
America/Pangnirtung | Eastern Standard Time | -5.0  
America/Paramaribo | Suriname Time | -3.0  
America/Phoenix | Mountain Standard Time | -7.0  
America/Port-au-Prince | Eastern Standard Time | -5.0  
America/Port_of_Spain | Atlantic Standard Time | -4.0  
America/Porto_Acre | Acre Time | -5.0  
America/Porto_Velho | Amazon Time | -4.0  
America/Puerto_Rico | Atlantic Standard Time | -4.0  
America/Punta_Arenas | GMT-03:00 | -3.0  
America/Rainy_River | Central Standard Time | -6.0  
America/Rankin_Inlet | Central Standard Time | -6.0  
America/Recife | Brasilia Time | -3.0  
America/Regina | Central Standard Time | -6.0  
America/Resolute | Central Standard Time | -6.0  
America/Rio_Branco | Acre Time | -5.0  
America/Rosario | Argentine Time | -3.0  
America/Santa_Isabel | Pacific Standard Time | -8.0  
America/Santarem | Brasilia Time | -3.0  
America/Santiago | Chile Time | -4.0  
America/Santo_Domingo | Atlantic Standard Time | -4.0  
America/Sao_Paulo | Brasilia Time | -3.0  
America/Scoresbysund | Eastern Greenland Time | -1.0  
America/Shiprock | Mountain Standard Time | -7.0  
America/Sitka | Alaska Standard Time | -9.0  
America/St_Barthelemy | Atlantic Standard Time | -4.0  
America/St_Johns | Newfoundland Standard Time | -3.5  
America/St_Kitts | Atlantic Standard Time | -4.0  
America/St_Lucia | Atlantic Standard Time | -4.0  
America/St_Thomas | Atlantic Standard Time | -4.0  
America/St_Vincent | Atlantic Standard Time | -4.0  
America/Swift_Current | Central Standard Time | -6.0  
America/Tegucigalpa | Central Standard Time | -6.0  
America/Thule | Atlantic Standard Time | -4.0  
America/Thunder_Bay | Eastern Standard Time | -5.0  
America/Tijuana | Pacific Standard Time | -8.0  
America/Toronto | Eastern Standard Time | -5.0  
America/Tortola | Atlantic Standard Time | -4.0  
America/Vancouver | Pacific Standard Time | -8.0  
America/Virgin | Atlantic Standard Time | -4.0  
America/Whitehorse | Pacific Standard Time | -8.0  
America/Winnipeg | Central Standard Time | -6.0  
America/Yakutat | Alaska Standard Time | -9.0  
America/Yellowknife | Mountain Standard Time | -7.0  
Antarctica/Casey | Australian Western Standard Time | 11.0  
Antarctica/Davis | Davis Time | 7.0  
Antarctica/DumontDUrville | Dumont-d'Urville Time | 10.0  
Antarctica/Macquarie | Macquarie Island Standard Time | 11.0  
Antarctica/Mawson | Mawson Time | 5.0  
Antarctica/McMurdo | New Zealand Standard Time | 12.0  
Antarctica/Palmer | Chile Time | -3.0  
Antarctica/Rothera | Rothera Time | -3.0  
Antarctica/South_Pole | New Zealand Standard Time | 12.0  
Antarctica/Syowa | Syowa Time | 3.0  
Antarctica/Troll | Coordinated Universal Time | 0.0  
Antarctica/Vostok | Vostok Time | 6.0  
Arctic/Longyearbyen | Central European Time | 1.0  
Asia/Aden | Arabia Standard Time | 3.0  
Asia/Almaty | Alma-Ata Time | 6.0  
Asia/Amman | Eastern European Time | 2.0  
Asia/Anadyr | Anadyr Time | 12.0  
Asia/Aqtau | Aqtau Time | 5.0  
Asia/Aqtobe | Aqtobe Time | 5.0  
Asia/Ashgabat | Turkmenistan Time | 5.0  
Asia/Ashkhabad | Turkmenistan Time | 5.0  
Asia/Atyrau | GMT+05:00 | 5.0  
Asia/Baghdad | Arabia Standard Time | 3.0  
Asia/Bahrain | Arabia Standard Time | 3.0  
Asia/Baku | Azerbaijan Time | 4.0  
Asia/Bangkok | Indochina Time | 7.0  
Asia/Barnaul | GMT+07:00 | 7.0  
Asia/Beirut | Eastern European Time | 2.0  
Asia/Bishkek | Kirgizstan Time | 6.0  
Asia/Brunei | Brunei Time | 8.0  
Asia/Calcutta | India Standard Time | 5.5  
Asia/Chita | Yakutsk Time | 9.0  
Asia/Choibalsan | Choibalsan Time | 8.0  
Asia/Chongqing | China Standard Time | 8.0  
Asia/Chungking | China Standard Time | 8.0  
Asia/Colombo | India Standard Time | 5.5  
Asia/Dacca | Bangladesh Time | 6.0  
Asia/Damascus | Eastern European Time | 2.0  
Asia/Dhaka | Bangladesh Time | 6.0  
Asia/Dili | Timor-Leste Time | 9.0  
Asia/Dubai | Gulf Standard Time | 4.0  
Asia/Dushanbe | Tajikistan Time | 5.0  
Asia/Famagusta | GMT+03:00 | 3.0  
Asia/Gaza | Eastern European Time | 2.0  
Asia/Harbin | China Standard Time | 8.0  
Asia/Hebron | Eastern European Time | 2.0  
Asia/Ho_Chi_Minh | Indochina Time | 7.0  
Asia/Hong_Kong | Hong Kong Time | 8.0  
Asia/Hovd | Hovd Time | 7.0  
Asia/Irkutsk | Irkutsk Time | 8.0  
Asia/Istanbul | Eastern European Time | 3.0  
Asia/Jakarta | West Indonesia Time | 7.0  
Asia/Jayapura | East Indonesia Time | 9.0  
Asia/Jerusalem | Israel Standard Time | 2.0  
Asia/Kabul | Afghanistan Time | 4.5  
Asia/Kamchatka | Petropavlovsk-Kamchatski Time | 12.0  
Asia/Karachi | Pakistan Time | 5.0  
Asia/Kashgar | Xinjiang Standard Time | 6.0  
Asia/Kathmandu | Nepal Time | 5.75  
Asia/Katmandu | Nepal Time | 5.75  
Asia/Khandyga | Yakutsk Time | 9.0  
Asia/Kolkata | India Standard Time | 5.5  
Asia/Krasnoyarsk | Krasnoyarsk Time | 7.0  
Asia/Kuala_Lumpur | Malaysia Time | 8.0  
Asia/Kuching | Malaysia Time | 8.0  
Asia/Kuwait | Arabia Standard Time | 3.0  
Asia/Macao | China Standard Time | 8.0  
Asia/Macau | China Standard Time | 8.0  
Asia/Magadan | Magadan Time | 11.0  
Asia/Makassar | Central Indonesia Time | 8.0  
Asia/Manila | Philippines Time | 8.0  
Asia/Muscat | Gulf Standard Time | 4.0  
Asia/Nicosia | Eastern European Time | 2.0  
Asia/Novokuznetsk | Krasnoyarsk Time | 7.0  
Asia/Novosibirsk | Novosibirsk Time | 7.0  
Asia/Omsk | Omsk Time | 6.0  
Asia/Oral | Oral Time | 5.0  
Asia/Phnom_Penh | Indochina Time | 7.0  
Asia/Pontianak | West Indonesia Time | 7.0  
Asia/Pyongyang | Korea Standard Time | 8.5  
Asia/Qatar | Arabia Standard Time | 3.0  
Asia/Qyzylorda | Qyzylorda Time | 6.0  
Asia/Rangoon | Myanmar Time | 6.5  
Asia/Riyadh | Arabia Standard Time | 3.0  
Asia/Saigon | Indochina Time | 7.0  
Asia/Sakhalin | Sakhalin Time | 11.0  
Asia/Samarkand | Uzbekistan Time | 5.0  
Asia/Seoul | Korea Standard Time | 9.0  
Asia/Shanghai | China Standard Time | 8.0  
Asia/Singapore | Singapore Time | 8.0  
Asia/Srednekolymsk | Srednekolymsk Time | 11.0  
Asia/Taipei | China Standard Time | 8.0  
Asia/Tashkent | Uzbekistan Time | 5.0  
Asia/Tbilisi | Georgia Time | 4.0  
Asia/Tehran | Iran Standard Time | 3.5  
Asia/Tel_Aviv | Israel Standard Time | 2.0  
Asia/Thimbu | Bhutan Time | 6.0  
Asia/Thimphu | Bhutan Time | 6.0  
Asia/Tokyo | Japan Standard Time | 9.0  
Asia/Tomsk | GMT+07:00 | 7.0  
Asia/Ujung_Pandang | Central Indonesia Time | 8.0  
Asia/Ulaanbaatar | Ulaanbaatar Time | 8.0  
Asia/Ulan_Bator | Ulaanbaatar Time | 8.0  
Asia/Urumqi | Xinjiang Standard Time | 6.0  
Asia/Ust-Nera | Ust-Nera Time | 10.0  
Asia/Vientiane | Indochina Time | 7.0  
Asia/Vladivostok | Vladivostok Time | 10.0  
Asia/Yakutsk | Yakutsk Time | 9.0  
Asia/Yangon | Myanmar Time | 6.5  
Asia/Yekaterinburg | Yekaterinburg Time | 5.0  
Asia/Yerevan | Armenia Time | 4.0  
Atlantic/Azores | Azores Time | -1.0  
Atlantic/Bermuda | Atlantic Standard Time | -4.0  
Atlantic/Canary | Western European Time | 0.0  
Atlantic/Cape_Verde | Cape Verde Time | -1.0  
Atlantic/Faeroe | Western European Time | 0.0  
Atlantic/Faroe | Western European Time | 0.0  
Atlantic/Jan_Mayen | Central European Time | 1.0  
Atlantic/Madeira | Western European Time | 0.0  
Atlantic/Reykjavik | Greenwich Mean Time | 0.0  
Atlantic/South_Georgia | South Georgia Standard Time | -2.0  
Atlantic/St_Helena | Greenwich Mean Time | 0.0  
Atlantic/Stanley | Falkland Is. Time | -3.0  
Australia/ACT | Australian Eastern Standard Time (New South Wales) | 10.0  
Australia/Adelaide | Australian Central Standard Time (South Australia) | 9.5  
Australia/Brisbane | Australian Eastern Standard Time (Queensland) | 10.0  
Australia/Broken_Hill | Australian Central Standard Time (South Australia/New South Wales) | 9.5  
Australia/Canberra | Australian Eastern Standard Time (New South Wales) | 10.0  
Australia/Currie | Australian Eastern Standard Time (New South Wales) | 10.0  
Australia/Darwin | Australian Central Standard Time (Northern Territory) | 9.5  
Australia/Eucla | Australian Central Western Standard Time | 8.75  
Australia/Hobart | Australian Eastern Standard Time (Tasmania) | 10.0  
Australia/LHI | Lord Howe Standard Time | 10.5  
Australia/Lindeman | Australian Eastern Standard Time (Queensland) | 10.0  
Australia/Lord_Howe | Lord Howe Standard Time | 10.5  
Australia/Melbourne | Australian Eastern Standard Time (Victoria) | 10.0  
Australia/NSW | Australian Eastern Standard Time (New South Wales) | 10.0  
Australia/North | Australian Central Standard Time (Northern Territory) | 9.5  
Australia/Perth | Australian Western Standard Time | 8.0  
Australia/Queensland | Australian Eastern Standard Time (Queensland) | 10.0  
Australia/South | Australian Central Standard Time (South Australia) | 9.5  
Australia/Sydney | Australian Eastern Standard Time (New South Wales) | 10.0  
Australia/Tasmania | Australian Eastern Standard Time (Tasmania) | 10.0  
Australia/Victoria | Australian Eastern Standard Time (Victoria) | 10.0  
Australia/West | Australian Western Standard Time | 8.0  
Australia/Yancowinna | Australian Central Standard Time (South Australia/New South Wales) | 9.5  
Brazil/Acre | Acre Time | -5.0  
Brazil/DeNoronha | Fernando de Noronha Time | -2.0  
Brazil/East | Brasilia Time | -3.0  
Brazil/West | Amazon Time | -4.0  
CET | Central European Time | 1.0  
CST6CDT | Central Standard Time | -6.0  
Canada/Atlantic | Atlantic Standard Time | -4.0  
Canada/Central | Central Standard Time | -6.0  
Canada/East-Saskatchewan | Central Standard Time | -6.0  
Canada/Eastern | Eastern Standard Time | -5.0  
Canada/Mountain | Mountain Standard Time | -7.0  
Canada/Newfoundland | Newfoundland Standard Time | -3.5  
Canada/Pacific | Pacific Standard Time | -8.0  
Canada/Saskatchewan | Central Standard Time | -6.0  
Canada/Yukon | Pacific Standard Time | -8.0  
Chile/Continental | Chile Time | -4.0  
Chile/EasterIsland | Easter Is. Time | -6.0  
Cuba | Cuba Standard Time | -5.0  
EET | Eastern European Time | 2.0  
EST5EDT | Eastern Standard Time | -5.0  
Egypt | Eastern European Time | 2.0  
Eire | Greenwich Mean Time | 0.0  
Etc/GMT | Greenwich Mean Time | 0.0  
Etc/GMT+0 | Greenwich Mean Time | 0.0  
Etc/GMT+1 | GMT-01:00 | -1.0  
Etc/GMT+10 | GMT-10:00 | -10.0  
Etc/GMT+11 | GMT-11:00 | -11.0  
Etc/GMT+12 | GMT-12:00 | -12.0  
Etc/GMT+2 | GMT-02:00 | -2.0  
Etc/GMT+3 | GMT-03:00 | -3.0  
Etc/GMT+4 | GMT-04:00 | -4.0  
Etc/GMT+5 | GMT-05:00 | -5.0  
Etc/GMT+6 | GMT-06:00 | -6.0  
Etc/GMT+7 | GMT-07:00 | -7.0  
Etc/GMT+8 | GMT-08:00 | -8.0  
Etc/GMT+9 | GMT-09:00 | -9.0  
Etc/GMT-0 | Greenwich Mean Time | 0.0  
Etc/GMT-1 | GMT+01:00 | 1.0  
Etc/GMT-10 | GMT+10:00 | 10.0  
Etc/GMT-11 | GMT+11:00 | 11.0  
Etc/GMT-12 | GMT+12:00 | 12.0  
Etc/GMT-13 | GMT+13:00 | 13.0  
Etc/GMT-14 | GMT+14:00 | 14.0  
Etc/GMT-2 | GMT+02:00 | 2.0  
Etc/GMT-3 | GMT+03:00 | 3.0  
Etc/GMT-4 | GMT+04:00 | 4.0  
Etc/GMT-5 | GMT+05:00 | 5.0  
Etc/GMT-6 | GMT+06:00 | 6.0  
Etc/GMT-7 | GMT+07:00 | 7.0  
Etc/GMT-8 | GMT+08:00 | 8.0  
Etc/GMT-9 | GMT+09:00 | 9.0  
Etc/GMT0 | Greenwich Mean Time | 0.0  
Etc/Greenwich | Greenwich Mean Time | 0.0  
Etc/UCT | Coordinated Universal Time | 0.0  
Etc/UTC | Coordinated Universal Time | 0.0  
Etc/Universal | Coordinated Universal Time | 0.0  
Etc/Zulu | Coordinated Universal Time | 0.0  
Europe/Amsterdam | Central European Time | 1.0  
Europe/Andorra | Central European Time | 1.0  
Europe/Astrakhan | GMT+04:00 | 4.0  
Europe/Athens | Eastern European Time | 2.0  
Europe/Belfast | Greenwich Mean Time | 0.0  
Europe/Belgrade | Central European Time | 1.0  
Europe/Berlin | Central European Time | 1.0  
Europe/Bratislava | Central European Time | 1.0  
Europe/Brussels | Central European Time | 1.0  
Europe/Bucharest | Eastern European Time | 2.0  
Europe/Budapest | Central European Time | 1.0  
Europe/Busingen | Central European Time | 1.0  
Europe/Chisinau | Eastern European Time | 2.0  
Europe/Copenhagen | Central European Time | 1.0  
Europe/Dublin | Greenwich Mean Time | 0.0  
Europe/Gibraltar | Central European Time | 1.0  
Europe/Guernsey | Greenwich Mean Time | 0.0  
Europe/Helsinki | Eastern European Time | 2.0  
Europe/Isle_of_Man | Greenwich Mean Time | 0.0  
Europe/Istanbul | Eastern European Time | 3.0  
Europe/Jersey | Greenwich Mean Time | 0.0  
Europe/Kaliningrad | Eastern European Time | 2.0  
Europe/Kiev | Eastern European Time | 2.0  
Europe/Kirov | GMT+03:00 | 3.0  
Europe/Lisbon | Western European Time | 0.0  
Europe/Ljubljana | Central European Time | 1.0  
Europe/London | Greenwich Mean Time | 0.0  
Europe/Luxembourg | Central European Time | 1.0  
Europe/Madrid | Central European Time | 1.0  
Europe/Malta | Central European Time | 1.0  
Europe/Mariehamn | Eastern European Time | 2.0  
Europe/Minsk | Moscow Standard Time | 3.0  
Europe/Monaco | Central European Time | 1.0  
Europe/Moscow | Moscow Standard Time | 3.0  
Europe/Nicosia | Eastern European Time | 2.0  
Europe/Oslo | Central European Time | 1.0  
Europe/Paris | Central European Time | 1.0  
Europe/Podgorica | Central European Time | 1.0  
Europe/Prague | Central European Time | 1.0  
Europe/Riga | Eastern European Time | 2.0  
Europe/Rome | Central European Time | 1.0  
Europe/Samara | Samara Time | 4.0  
Europe/San_Marino | Central European Time | 1.0  
Europe/Sarajevo | Central European Time | 1.0  
Europe/Saratov | GMT+04:00 | 4.0  
Europe/Simferopol | Moscow Standard Time | 3.0  
Europe/Skopje | Central European Time | 1.0  
Europe/Sofia | Eastern European Time | 2.0  
Europe/Stockholm | Central European Time | 1.0  
Europe/Tallinn | Eastern European Time | 2.0  
Europe/Tirane | Central European Time | 1.0  
Europe/Tiraspol | Eastern European Time | 2.0  
Europe/Ulyanovsk | GMT+04:00 | 4.0  
Europe/Uzhgorod | Eastern European Time | 2.0  
Europe/Vaduz | Central European Time | 1.0  
Europe/Vatican | Central European Time | 1.0  
Europe/Vienna | Central European Time | 1.0  
Europe/Vilnius | Eastern European Time | 2.0  
Europe/Volgograd | Moscow Standard Time | 3.0  
Europe/Warsaw | Central European Time | 1.0  
Europe/Zagreb | Central European Time | 1.0  
Europe/Zaporozhye | Eastern European Time | 2.0  
Europe/Zurich | Central European Time | 1.0  
GB | Greenwich Mean Time | 0.0  
GB-Eire | Greenwich Mean Time | 0.0  
GMT | Greenwich Mean Time | 0.0  
GMT0 | Greenwich Mean Time | 0.0  
Greenwich | Greenwich Mean Time | 0.0  
Hongkong | Hong Kong Time | 8.0  
Iceland | Greenwich Mean Time | 0.0  
Indian/Antananarivo | Eastern African Time | 3.0  
Indian/Chagos | Indian Ocean Territory Time | 6.0  
Indian/Christmas | Christmas Island Time | 7.0  
Indian/Cocos | Cocos Islands Time | 6.5  
Indian/Comoro | Eastern African Time | 3.0  
Indian/Kerguelen | French Southern & Antarctic Lands Time | 5.0  
Indian/Mahe | Seychelles Time | 4.0  
Indian/Maldives | Maldives Time | 5.0  
Indian/Mauritius | Mauritius Time | 4.0  
Indian/Mayotte | Eastern African Time | 3.0  
Indian/Reunion | Reunion Time | 4.0  
Iran | Iran Standard Time | 3.5  
Israel | Israel Standard Time | 2.0  
Jamaica | Eastern Standard Time | -5.0  
Japan | Japan Standard Time | 9.0  
Kwajalein | Marshall Islands Time | 12.0  
Libya | Eastern European Time | 2.0  
MET | Middle Europe Time | 1.0  
MST7MDT | Mountain Standard Time | -7.0  
Mexico/BajaNorte | Pacific Standard Time | -8.0  
Mexico/BajaSur | Mountain Standard Time | -7.0  
Mexico/General | Central Standard Time | -6.0  
NZ | New Zealand Standard Time | 12.0  
NZ-CHAT | Chatham Standard Time | 12.75  
Navajo | Mountain Standard Time | -7.0  
PRC | China Standard Time | 8.0  
PST8PDT | Pacific Standard Time | -8.0  
Pacific/Apia | West Samoa Standard Time | 13.0  
Pacific/Auckland | New Zealand Standard Time | 12.0  
Pacific/Bougainville | Bougainville Standard Time | 11.0  
Pacific/Chatham | Chatham Standard Time | 12.75  
Pacific/Chuuk | Chuuk Time | 10.0  
Pacific/Easter | Easter Is. Time | -6.0  
Pacific/Efate | Vanuatu Time | 11.0  
Pacific/Enderbury | Phoenix Is. Time | 13.0  
Pacific/Fakaofo | Tokelau Time | 13.0  
Pacific/Fiji | Fiji Time | 12.0  
Pacific/Funafuti | Tuvalu Time | 12.0  
Pacific/Galapagos | Galapagos Time | -6.0  
Pacific/Gambier | Gambier Time | -9.0  
Pacific/Guadalcanal | Solomon Is. Time | 11.0  
Pacific/Guam | Chamorro Standard Time | 10.0  
Pacific/Honolulu | Hawaii Standard Time | -10.0  
Pacific/Johnston | Hawaii Standard Time | -10.0  
Pacific/Kiritimati | Line Is. Time | 14.0  
Pacific/Kosrae | Kosrae Time | 11.0  
Pacific/Kwajalein | Marshall Islands Time | 12.0  
Pacific/Majuro | Marshall Islands Time | 12.0  
Pacific/Marquesas | Marquesas Time | -9.5  
Pacific/Midway | Samoa Standard Time | -11.0  
Pacific/Nauru | Nauru Time | 12.0  
Pacific/Niue | Niue Time | -11.0  
Pacific/Norfolk | Norfolk Time | 11.0  
Pacific/Noumea | New Caledonia Time | 11.0  
Pacific/Pago_Pago | Samoa Standard Time | -11.0  
Pacific/Palau | Palau Time | 9.0  
Pacific/Pitcairn | Pitcairn Standard Time | -8.0  
Pacific/Pohnpei | Pohnpei Time | 11.0  
Pacific/Ponape | Pohnpei Time | 11.0  
Pacific/Port_Moresby | Papua New Guinea Time | 10.0  
Pacific/Rarotonga | Cook Is. Time | -10.0  
Pacific/Saipan | Chamorro Standard Time | 10.0  
Pacific/Samoa | Samoa Standard Time | -11.0  
Pacific/Tahiti | Tahiti Time | -10.0  
Pacific/Tarawa | Gilbert Is. Time | 12.0  
Pacific/Tongatapu | Tonga Time | 13.0  
Pacific/Truk | Chuuk Time | 10.0  
Pacific/Wake | Wake Time | 12.0  
Pacific/Wallis | Wallis & Futuna Time | 12.0  
Pacific/Yap | Chuuk Time | 10.0  
Poland | Central European Time | 1.0  
Portugal | Western European Time | 0.0  
ROK | Korea Standard Time | 9.0  
Singapore | Singapore Time | 8.0  
SystemV/AST4 | Atlantic Standard Time | -4.0  
SystemV/AST4ADT | Atlantic Standard Time | -4.0  
SystemV/CST6 | Central Standard Time | -6.0  
SystemV/CST6CDT | Central Standard Time | -6.0  
SystemV/EST5 | Eastern Standard Time | -5.0  
SystemV/EST5EDT | Eastern Standard Time | -5.0  
SystemV/HST10 | Hawaii Standard Time | -10.0  
SystemV/MST7 | Mountain Standard Time | -7.0  
SystemV/MST7MDT | Mountain Standard Time | -7.0  
SystemV/PST8 | Pacific Standard Time | -8.0  
SystemV/PST8PDT | Pacific Standard Time | -8.0  
SystemV/YST9 | Alaska Standard Time | -9.0  
SystemV/YST9YDT | Alaska Standard Time | -9.0  
Turkey | Eastern European Time | 3.0  
UCT | Coordinated Universal Time | 0.0  
US/Alaska | Alaska Standard Time | -9.0  
US/Aleutian | Hawaii Standard Time | -10.0  
US/Arizona | Mountain Standard Time | -7.0  
US/Central | Central Standard Time | -6.0  
US/East-Indiana | Eastern Standard Time | -5.0  
US/Eastern | Eastern Standard Time | -5.0  
US/Hawaii | Hawaii Standard Time | -10.0  
US/Indiana-Starke | Central Standard Time | -6.0  
US/Michigan | Eastern Standard Time | -5.0  
US/Mountain | Mountain Standard Time | -7.0  
US/Pacific | Pacific Standard Time | -8.0  
US/Pacific-New | Pacific Standard Time | -8.0  
US/Samoa | Samoa Standard Time | -11.0  
UTC | Coordinated Universal Time | 0.0  
Universal | Coordinated Universal Time | 0.0  
W-SU | Moscow Standard Time | 3.0  
WET | Western European Time | 0.0  
Zulu | Coordinated Universal Time | 0.0  
  
Back to top

