# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs/define-a-new-database-connection.md

# Define a new database connection

While working on a transformation or job, you can define a new database connection to use.

Before you can create a connection, the appropriate driver must be installed for your particular data connection. Your IT administrator should be able to install the appropriate driver for you. For details, see [Specify data connections for the Pentaho Server](https://app.gitbook.com/s/qfaQ2p0JAZrP8b3cpM9a/legacy-redirects/tasks-to-be-performed-by-an-it-administrator-legacy-redirects/configure-the-pentaho-server-legacy-pages/specify-data-connections-for-the-pentaho-server) in the Install Pentaho Data Integration and Analytics guide.

To define a new database connection, complete the following steps:

1. With a transformation or job open, on the left side of the Pipeline Designer interface, click the **View** icon. The **View** pane opens with the Transformations folder expanded, containing the **Database Connections** list.
2. Find **Database Connections**, click the **More Actions** icon, and then select **New**. The Database Connection window opens.&#x20;
3. Enter database connection information for your new Database Connection. The type of database connection information entered depends on your access protocol. Refer to the examples in the following sections of this topic for Native (JDBC) and OCI protocols:
   * [Native (JDBC) protocol information](#native-jdbc-protocol-information)
   * [OCI protocol information](#oci-protocol-information)
   * [Connect to Snowflake using strong authentication](#connect-to-snowflake-using-strong-authentication)
   * [Connect to an Azure SQL database](#connect-to-an-azure-sql-database)

### Native (JDBC) protocol information

Create a Native (JDBC) connection in the Database Connection dialog box by completing the following steps:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Connection Type** list, select the database you want to use (for example, MySQL or Oracle).
3. In the **Access** **Type** list, select **Native (JDBC)**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information:

   <table><thead><tr><th width="159">Field</th><th>Description</th></tr></thead><tbody><tr><td>Host Name</td><td>The name of the server that hosts the database to which you are connecting. Alternatively, you can specify the host by IP address.</td></tr><tr><td>Database Name</td><td>The name of the database to which you are connecting. If you are using an ODBC connection, enter the Data Source Name (DSN) in this field.</td></tr><tr><td>Port Number</td><td>The TCP/IP port number (if it is different from the default)</td></tr><tr><td>Username</td><td>Optional user name used to connect to the database</td></tr><tr><td>Password</td><td>Optional password used to connect to the database</td></tr></tbody></table>
5. Click **Test Connection**. A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **Save**. The database connection is saved and appears in the **Database Connections** list.

### OCI protocol information

Perform the following steps to create an OCI connection in the PDI Database Connection dialog box:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Connection Type** list, select **Oracle**.
3. In the **Access** list, select **OCI**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information as directed by the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm).

   | Field                  | Description                                                              |
   | ---------------------- | ------------------------------------------------------------------------ |
   | SID                    | The Oracle system ID that uniquely identifies the database on the system |
   | Tablespace for Data    | The name of the tablespace where the data is stored                      |
   | Tablespace for Indices | The name of the tablespace where the indices is stored                   |
   | User Name              | The user name used to connect to the database                            |
   | Password               | The password used to connect to the database                             |
5. Click **Test Connection**.

   A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **OK** to close the Database Connection dialog box.

If you want to use **Advanced**, **Options**, or **Pooling** for your OCI connection, refer to the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm) to understand how to specify these settings.

### Connect to Snowflake using strong authentication

If you are defining a data connection to Pentaho Data Integration and Analytics from a Snowflake data warehouse in the cloud, you can improve connection security by applying strong authentication.

You can apply strong authentication to your defined Pentaho data connection from Snowflake through a key pair.&#x20;

Configure key pair strong authentication for your Snowflake data connection by completing the following steps:

1. After entering the information for your Snowflake data connection in the **General** tab of the Database Connection dialog box, select the **Options** tab.
2. Set the key pair parameters as indicated in the following table:

   <table><thead><tr><th width="198.00006103515625">Parameter</th><th>Value</th></tr></thead><tbody><tr><td><code>authenticator</code></td><td><code>snowflake_jwt</code></td></tr><tr><td><code>private_key_file</code></td><td>Specify the name of the private key file you use in your environment. For example, <code>/rsa_key.p8</code></td></tr><tr><td><code>private_key_file_pwd</code></td><td>Specify the password for accessing the private key file you use in your environment. For example, <code>PentahoSnowFlake123</code></td></tr></tbody></table>

   See <https://docs.snowflake.com/en/developer-guide/jdbc/jdbc-configure#private-key-file-name-and-password-as-connection-properties> for details on the private key file and its password.
3. Click **Test Connection** to verify your connection. A success message appears if the connection is established.
4. Click **OK** to close the connection test dialog box.
5. To save the connection, click **OK** to close the Database Connection dialog box.

You have applied key pair authentication to your defined data connection between Pentaho and Snowflake.

### Connect to an Azure SQL database

You can use an Azure SQL database as a data source with the Pipeline Designer. This connection is required if you want to bulk load into Azure SQL DB job entry to load data into your Azure SQL database from Azure Data Lake Storage. Pentaho supports the [Always Encrypted](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) option, [dynamic masking](https://docs.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview), and multiple authentication methods for connecting to an Azure SQL database.

Because one physical server may host databases for multiple customers, keep in mind that SQL for Azure is different from MSSQL. For more information regarding the differences between Azure SQL and MSSQL, see <https://docs.microsoft.com/en-us/azure/azure-sql/database/features-comparison>

#### Before you begin

You must have an Azure account with an active subscription and an instance of an Azure SQL database. You also need to install the Azure SQL database drivers. For help installing your drivers, see your Microsoft documentation for details.

Additionally, you need to obtain the following information from your system administrator:

* Host name
* Database name
* Port number
* Authentication method
* Username
* Password

If you use the **Always Encryption Enabled** option, you also need to obtain the **Client id** and **Client Secret Key**.

#### Authentication method

Pentaho supports four authentication methods for connecting to the Azure SQL DB instance:

* **SQL Authentication**

  Connect using the Azure SQL Server username and password.
* **Azure Active Directory**

  Connect using Multi Factor Authentication (MFA). The MFA password must be entered on the displayed webpage.
* **Azure Active Directory with password**

  Connect using an Azure AD username and password.
* **Azure Active Directory with integrated authentication**

  Connect using the federated on-premises Active Directory Federation Services (ADFS) with Azure Active Directory in the cloud.

#### Connect to an Azure database

1. In the **Connection Name** field, enter a name that uniquely describes this connection. The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Connection Type** list, select **Azure SQL DB**.
3. In the **Access** list, select **Native (JDBC)**.&#x20;
4. Enter your database connection information.

   <table><thead><tr><th width="234">Field</th><th>Description</th></tr></thead><tbody><tr><td><strong>Host Name</strong></td><td>The name of the Azure SQL server instance.</td></tr><tr><td><strong>Database Name</strong></td><td>The name of the Azure SQL database to which you are connecting.</td></tr><tr><td><strong>Port Number</strong></td><td>The TCP/IP port number. The Azure SQL Database service is only available through TCP port 1433. You must set your firewall to allow outgoing TCP communication on port 1433.</td></tr><tr><td><strong>Authentication method</strong></td><td>The authentication method used to connect to the Azure SQL DB instance. The default is SQL Authentication.</td></tr><tr><td><strong>Username</strong></td><td>The username used to connect to the database.</td></tr><tr><td><strong>Password</strong></td><td>The password used to connect to the database.</td></tr><tr><td><strong>Always Encryption Enabled</strong></td><td>Select to use encryption. See <a href="#use-the-always-encryption-enabled-option">Use the Always Encryption Enabled option</a> for instructions on using this option.</td></tr><tr><td><strong>Client id</strong></td><td>The unique client identifier, used to identify and set up a durable connection path to the server.</td></tr><tr><td><strong>Client Secret Key</strong></td><td>The unique name of the key value in the Azure Key Vault.</td></tr></tbody></table>
5. Click **Test Connection** to verify your connection.

#### Use the Always Encryption Enabled option

Before you can use the **Always Encryption Enabled** option, you must perform the following steps. Consult the [Microsoft Azure SQL documentation](https://docs.microsoft.com/en-us/azure/azure-sql/) for assistance with your Azure SQL tools.

1. Generate a column master key in the Azure Key Vault.
2. Encrypt the column using the column master key.
3. Register the app under Azure Active Directory and obtain both the **Client id** and **Client Secret Key**.
4. Grant permissions to the **Client id** for accessing the Azure Key Vault.
5. Select **Always Encryption Enabled** and provide the **Client id** and **Client Secret Key**.

The Azure Always Encrypted feature is now active.
