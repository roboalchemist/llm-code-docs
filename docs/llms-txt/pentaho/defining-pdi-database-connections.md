# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/defining-pdi-database-connections.md

# Defining PDI database connections

You can use Pentaho Data Integration (PDI) to access data from various databases. You
\
must connect to the database before accessing its records. You define database connections
\
in PDI through the Database Connection dialog box.

Before you can create a connection, the appropriate driver must be installed for your
\
particular data connection. Your IT administrator should be able to install the appropriate
\
driver for you.

## Open the Database Connection dialog box from PDI

Perform the following steps to open a new database connection in PDI:

1. Start the PDI client (Spoon) and create a new transformation or job.
2. In the **View** tab of the **Explorer** pane, double-click on the **Database connections** folder.

   The Database Connection dialog box appears, as shown below:![Database Connection dialog box](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2F3cSDr8qiSyS93js07h2v%2FssPDIDataConnectionFromViewTabInExplorerPane.png?alt=media\&token=3697598d-8571-4433-8e36-8e8bdcee108c)
3. Enter your data connection information and test.

   See [Enter database connection information](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/broken-reference) for further details.

In PDI, you can define connections to multiple databases provided by multiple database vendors such as MySQL and Oracle. PDI ships with the most suitable JDBC drivers for PostgreSQL, our default database.

Pentaho recommends avoiding ODBC connections. The ODBC to JDBC bridge driver does not always provide an exact match and adds another level of complexity, which affects performance. The only time you may have to use ODBC is if no JDBC driver is available. For details, see the [Pentaho Community article on why you should avoid ODBC](http://wiki.pentaho.com/pages/viewpage.action?pageId=14850644).

When you define a database connection in PDI, the connection information (such as the user name, password, and port number) is stored in the Pentaho Repository and is available to other users when they connect to the repository. If you are not using the Pentaho Repository, the database connection information is stored in the XML file associated with your transformation or job. See the **Pentaho Data Integration** document for details on the Pentaho Repository.

You must have information about your database (such as your database type, port number, user name and password) before you define a JDBC connection. In PDI, you can also set connection properties as variables. Through such variables, your transformations and jobs can access data from multiple database types.

Make sure to use clean ANSI SQL that works on all the database types used.

## Enter database connection information

The type of database connection information entered depends on your access protocol. The following sections show examples for Native (JDBC) and OCI protocols:

### Native (JDBC) protocol information

Perform the following steps to create a Native (JDBC) connection in the Database Connection dialog box:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Database Type** list, select the database you want to use (for example, MySQL or Oracle).
3. In the **Access** list, select **Native (JDBC)**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information:

   | Field         | Description                                                                                                                               |
   | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
   | Host Name     | The name of the server that hosts the database to which you are connecting. Alternatively, you can specify the host by IP address.        |
   | Database Name | The name of the database to which you are connecting. If you are using a ODBC connection, enter the Data Source Name (DSN) in this field. |
   | Port Number   | The TCP/IP port number (if it is different from the default)                                                                              |
   | User Name     | Optional user name used to connect to the database                                                                                        |
   | Password      | Optional password used to connect to the database                                                                                         |
5. Click **Test**.

   A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **OK** to close the Database Connection dialog box.
   * In PUC, your connection name appears in the list of available data sources in the Manage Data Sources dialog box.
   * In PDI, your connection name appears under the **Database connections** folder in the **View** tab.

### OCI protocol information (PDI only)

Perform the following steps to create an OCI connection in the PDI Database Connection dialog box:

1. In the **Connection Name** field, enter a name that uniquely describes this connection.

   The name can have spaces, but it cannot have special characters (such as #, $, and %).
2. In the **Database Type** list, select **Oracle**.
3. In the **Access** list, select **OCI**. The access protocol which appears depends on the database type you select.
4. In the **Settings** section, enter the following information as directed by the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm).

   | Field                  | Description                                                              |
   | ---------------------- | ------------------------------------------------------------------------ |
   | SID                    | The Oracle system ID that uniquely identifies the database on the system |
   | Tablespace for Data    | The name of the tablespace where the data is stored                      |
   | Tablespace for Indices | The name of the tablespace where the indices is stored                   |
   | User Name              | The user name used to connect to the database                            |
   | Password               | The password used to connect to the database                             |
5. Click **Test**.

   A success message appears if the connection is established.
6. Click **OK** to close the connection test dialog box.
7. To save the connection, click **OK** to close the Database Connection dialog box.

If you want to use **Advanced**, **Options**, or **Pooling** for your OCI connection, refer to the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm) to understand how to specify these settings.

### Connect to Snowflake using strong authentication

If you are defining a data connection to Pentaho Data Integration and Analytics from a Snowflake data warehouse in the cloud, you can improve connection security by applying strong authentication.

You can apply strong authentication to your defined Pentaho data connection from Snowflake through a key pair. Perform the following steps to configure key pair strong authentication for your Snowflake data connection:

1. After [entering the information for your Snowflake data connection](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/broken-reference) in the **General** tab of the Database Connection dialog box, select the **Options** tab.
2. Set the key pair parameters as indicated in the following table:

   | Parameter              | Value                                                                                                                   |
   | ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
   | `authenticator`        | `snowflake_jwt`                                                                                                         |
   | `private_key_file`     | Specify the name of the private key file you use in your environment. For example, `/rsa_key.p8`                        |
   | `private_key_file_pwd` | Specify the password for accessing the private key file you use in your environment. For example, `PentahoSnowFlake123` |

   See <https://docs.snowflake.com/en/developer-guide/jdbc/jdbc-configure#private-key-file-name-and-password-as-connection-properties> for details on the private key file and its password.
3. Click **Test** to verify your connection. A success message appears if the connection is established.
4. Click **OK** to close the connection test dialog box.
5. To save the connection, click **OK** to close the Database Connection dialog box.

You have applied key pair authentication to your defined data connection between Pentaho and Snowflake.

### Connect to an Azure SQL database

You can use an Azure SQL database as a data source with the PDI client. This connection is required if you want to use the PDI Bulk load into Azure SQL DB job entry to load data into your Azure SQL database from Azure Data Lake Storage. Pentaho supports the [Always Encrypted](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine?view=sql-server-ver15) option, [dynamic masking](https://docs.microsoft.com/en-us/azure/azure-sql/database/dynamic-data-masking-overview), and multiple authentication methods for connecting to an Azure SQL database.

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

Perform the following steps to connect to your database:

1. Start the PDI client and create a new transformation or job.

   See the **Pentaho Data Integration** document for instructions on creating a PDI transformation.

   **Note:** You can also use the Pentaho User Console to make this connection. See the **Pentaho Business Analytics** document for instructions.
2. In the **View** tab of the **Explorer** pane, double-click on the **Database connections** folder. The **Database Connection** dialog box appears, as shown below:

   ![Database connection dialog for Azure SQL](https://773338310-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYwnJ6Fexn4LZwKRHghPK%2Fuploads%2FkAmeVj9dIeW4oNNb8yCZ%2FDatabase%20connection%20dialog%20for%20Azure%20SQL.png?alt=media\&token=f1034bcd-2018-4477-a6eb-70b970ad292b)
3. Enter your database connection information.

   | Field                         | Description                                                                                                                                                                                               |
   | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Host Name**                 | The name of the Azure SQL server instance.                                                                                                                                                                |
   | **Database Name**             | The name of the Azure SQL database to which you are connecting.                                                                                                                                           |
   | **Port Number**               | The TCP/IP port number. The Azure SQL Database service is only available through TCP port 1433. You must set your firewall to allow outgoing TCP communication on port 1433.                              |
   | **Authentication method**     | The authentication method used to connect to the Azure SQL DB instance. The default is SQL Authentication.                                                                                                |
   | **Username**                  | The username used to connect to the database.                                                                                                                                                             |
   | **Password**                  | The password used to connect to the database.                                                                                                                                                             |
   | **Always Encryption Enabled** | Select to use encryption. See [Use the Always Encryption Enabled option](https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/broken-reference) for instructions on using this option. |
   | **Client id**                 | The unique client identifier, used to identify and set up a durable connection path to the server.                                                                                                        |
   | **Client Secret Key**         | The unique name of the key value in the Azure Key Vault.                                                                                                                                                  |
4. Click **Test**to verify your connection.

#### Use the Always Encryption Enabled option

Before you can use the **Always Encryption Enabled** option, you must perform the following steps. Consult the [Microsoft Azure SQL documentation](https://docs.microsoft.com/en-us/azure/azure-sql/) for assistance with your Azure SQL tools.

1. Generate a column master key in the Azure Key Vault.
2. Encrypt the column using the column master key.
3. Register the app under Azure Active Directory and obtain both the **Client id** and **Client Secret Key**.
4. Grant permissions to the **Client id** for accessing the Azure Key Vault.
5. Select **Always Encryption Enabled** and provide the **Client id** and **Client Secret Key**.

The Azure Always Encrypted feature is now active.

<br>

<br>

\ <br>
