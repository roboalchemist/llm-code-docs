# Source: https://docs.pentaho.com/pba/pipeline-designer/managing-transformations-and-jobs/manage-connections-for-transformations-and-jobs.md

# Source: https://docs.pentaho.com/pdia-data-integration/pipeline-designer/manage-connections-for-transformations-and-jobs.md

# Manage connections for transformations and jobs

When you create or edit a transformation or job in Pipeline Designer, you can connect to multiple databases. Pipeline Designer supports many database vendors, including MySQL and Oracle.

Pipeline Designer includes JDBC drivers for PostgreSQL, the default database.

Pentaho recommends avoiding ODBC connections. The ODBC-to-JDBC bridge is not exact. It also adds overhead. Use ODBC only when a JDBC driver is unavailable. For details, see [Why you should avoid ODBC](http://wiki.pentaho.com/pages/viewpage.action?pageId=14850644).

When you define a database connection, Pipeline Designer stores connection details in the Pentaho Repository. These details include username, password, and port. Other users can reuse the connection through the repository.

If you do not use the Pentaho Repository, Pipeline Designer stores connection details in the transformation or job XML.

Collect your connection details before you start. You typically need database type, host, port, username, and password. You can also set connection properties as variables.

Use ANSI SQL when possible. It improves portability across databases.

You must have a transformation or job open to manage connections. For help, see [Create a transformation](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference), [Create a job](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference), or [Edit a transformation or job](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference).

### In this topic

* [Define a new database connection](#define-a-new-database-connection)
* [Clear cached database metadata](#clear-cached-database-metadata)
* [Edit a database connection](#edit-a-database-connection)
* [Delete a database connection](#delete-a-database-connection)
* [Explore configured database connections](#explore-configured-database-connections)
* [Show dependencies](#show-dependencies)

### Define a new database connection

1. In **Connection Name**, enter a descriptive name.

   The name can include spaces. Do not use special characters like `#`, `$`, or `%`.
2. In **Connection Type**, select the database type.
3. In **Access Type**, select **Native (JDBC)**.
4. In **Settings**, enter the connection values:
   * **Host Name**: Server host name or IP address.
   * **Database Name**: Database name. For ODBC, enter the DSN.
   * **Port Number**: TCP/IP port, if not the default.
   * **Username**: Optional username.
   * **Password**: Optional password.
5. Select **Test Connection**.
6. Select **OK** to close the test dialog.
7. Select **Save** to save the connection.

#### OCI protocol information

Use these steps to create an Oracle OCI connection:

1. In **Connection Name**, enter a descriptive name.
2. In **Connection Type**, select **Oracle**.
3. In **Access**, select **OCI**.
4. In **Settings**, enter values as described in the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm):
   * **SID**: Oracle system ID.
   * **Tablespace for Data**: Tablespace for data.
   * **Tablespace for Indices**: Tablespace for indexes.
   * **User Name**: Database username.
   * **Password**: Database password.
5. Select **Test Connection**.
6. Select **OK** to close the test dialog.
7. Select **OK** to close the Database Connection dialog.

If you want to use **Advanced**, **Options**, or **Pooling**, see the [Oracle OCI documentation](http://docs.oracle.com/cd/B28359_01/java.111/b31224/instclnt.htm).

#### Connect to Snowflake using strong authentication

Snowflake key pair authentication uses a private key file instead of a password.

1. After you enter the connection values on the **General** tab, select **Options**.
2. Add these parameters:

   * `authenticator`: `snowflake_jwt`
   * `private_key_file`: Path to your private key file. Example: `/rsa_key.p8`
   * `private_key_file_pwd`: Password for the private key file. Example: `PentahoSnowFlake123`

   See the Snowflake JDBC docs: <https://docs.snowflake.com/en/developer-guide/jdbc/jdbc-configure#private-key-file-name-and-password-as-connection-properties>.
3. Select **Test Connection**.
4. Select **OK** to close the test dialog.
5. Select **OK** to close the Database Connection dialog.

#### Connect to an Azure SQL database

You can use an Azure SQL database as a data source in Pipeline Designer.

This connection is required for the **Bulk load into Azure SQL DB** job entry.

Pipeline Designer supports:

* Always Encrypted
* Dynamic masking
* Multiple authentication methods

Azure SQL differs from on-premises SQL Server. See Microsoft documentation: <https://docs.microsoft.com/en-us/azure/azure-sql/database/features-comparison>.

**Before you begin**

* Ensure you have an Azure subscription and an Azure SQL database instance.
* Install the Azure SQL database drivers.
* Get these values from your administrator:
  * Host name
  * Database name
  * Port number
  * Authentication method
  * Username
  * Password
* If you use **Always Encryption Enabled**, also get:
  * Client ID
  * Client Secret Key

**Authentication method**

Pipeline Designer supports four Azure SQL authentication methods:

* **SQL Authentication**
* **Azure Active Directory**
* **Azure Active Directory with password**
* **Azure Active Directory with integrated authentication**

**Connect to an Azure SQL database**

1. In **Connection Name**, enter a descriptive name.
2. In **Connection Type**, select **Azure SQL DB**.
3. In **Access**, select **Native (JDBC)**.
4. Enter your Azure SQL connection values:
   * **Host Name**: Azure SQL server instance name.
   * **Database Name**: Azure SQL database name.
   * **Port Number**: TCP port. Azure SQL uses `1433`.
   * **Authentication method**: Default is SQL Authentication.
   * **Username**
   * **Password**
   * **Always Encryption Enabled** (optional)
   * **Client id** (if Always Encryption Enabled)
   * **Client Secret Key** (if Always Encryption Enabled)
5. Select **Test Connection**.

**Use the Always Encryption Enabled option**

Before you enable **Always Encryption Enabled**, complete these steps using Azure tools:

1. Generate a column master key in Azure Key Vault.
2. Encrypt the column using the column master key.
3. Register the app in Azure Active Directory. Collect **Client id** and **Client Secret Key**.
4. Grant the app permissions to access Azure Key Vault.
5. Enable **Always Encryption Enabled**. Enter **Client id** and **Client Secret Key**.

### Clear cached database metadata

When you work with complex transformations or jobs, Pipeline Designer can cache outdated metadata. Use **Clear Complete DB Cache** to refresh it.

Cached metadata can include:

* Table structures
* Column types
* Indexes
* Primary and foreign keys
* Other schema metadata

{% hint style="info" %}
Clearing cached database metadata does not delete database data. It also does not change transformation or job files.
{% endhint %}

1. Open a transformation or job.
2. On the left, select **View** to open the **View** pane.
3. Under **Database Connections**, select **More Actions**, then select **Clear Complete DB Cache**.

### Edit a database connection

Open the connection editor, then review these tabs and options.

#### Advanced options

| Option                                            | Description                                                  |
| ------------------------------------------------- | ------------------------------------------------------------ |
| Supports the Boolean data type                    | Uses the database native Boolean data type.                  |
| Supports the timestamp data type                  | Uses the database native timestamp data type.                |
| Quote all in database                             | Uses quoted identifiers. This can make names case-sensitive. |
| Force all to lower-case                           | Converts identifiers to lowercase.                           |
| Force all to upper-case                           | Converts identifiers to uppercase.                           |
| Preserve case of reserved words                   | Uses the database reserved word list.                        |
| The Preferred Schema name where no schema is used | Sets a default schema name, such as `MYSCHEMA`.              |
| SQL Code Editor                                   | SQL statements to run immediately after connecting.          |

#### Options tab

Use the **Options** tab to add or delete driver parameters.

* To add a parameter, select **Add Row**.
* To delete a parameter row, select the **Delete** icon.

#### Pooling tab

Use **Pooling** to configure a connection pool. Pooling can reduce connection overhead. It can also help when database licensing limits concurrent connections.

* To add a pool parameter, select **Add Row**, then enter **Parameter** and **Value**.
* To delete a pool parameter, select the **Delete** icon.
* To control pagination, select a new **Items per page** value.

Common pooling parameters include `validationQuery`.

* For Oracle and PostgreSQL, use `Select 1 from dual`.
* For Microsoft SQL Server and MySQL, use `Select 1`.

Typical pooling options include:

* **Enable Connection Pooling**
* **Pool Size (Initial, Maximum)**
* **Parameters**
* **Description**

#### Clustering tab

Use **Clustering** to cluster a database connection and create connections to data partitions.

To create a partition connection, enter:

* Partition ID
* Host Name
* Port
* Database Name
* User Name
* Password

If you use the Data Source Wizard (DSW) in a clustered Pentaho Server setup, disable DSW data source caching. This helps ensure new data sources appear on all nodes.

To disable DSW caching, set `enableDomainIdCache=false` in `server/pentaho-server/pentaho-solutions/system/system.properties`.

### Delete a database connection

Delete a database connection that you no longer need.

{% hint style="danger" %}
Deleting a connection can affect reports, charts, dashboards, and other content that uses the connection.
{% endhint %}

1. Open a transformation or job.
2. On the left, select **View** to open the **View** pane.
3. Expand **Database Connections**.
4. Find the connection, select **More Actions**, then select **Delete**.
5. In **Confirm deletion**, select **Yes**.

### Explore configured database connections

Use the Database Explorer to inspect configured connections. You can browse tables, views, synonyms, catalogs, and schemas.

1. Open a transformation or job.
2. On the left, select **View** to open the **View** pane.
3. Expand **Database Connections**.
4. Find the connection, select **More Actions**, then select **Explore**.
5. (Optional) Select **Refresh** to reload the list.
6. Browse to the object you want, then select **Actions**:
   * **Preview first 100**: Shows the first 100 rows.
   * **Preview x Rows**: Prompts for the number of rows.
   * **Row Count**: Shows the total row count.
   * **Show Layout**: Shows columns and data types.
   * **DDL**: Generates DDL for the selected object.
   * **View SQL**: Opens the Simple SQL Editor for the selected table.
   * **Truncate Table**: Generates a `TRUNCATE TABLE` statement. The statement is commented out by default.
   * **Data Profile**: Shows basic profiling information.
7. Select **OK** to close the Database Explorer.

### Show dependencies

Show all platform dependencies for a connection, including transformations and jobs.

1. Open a transformation or job.
2. On the left, select **View** to open the **View** pane.
3. Expand **Database Connections**.
4. Find the connection, select **More Actions**, then select **Show dependencies**.

### Related tasks

* [Use the SQL Editor](https://docs.pentaho.com/pdia-data-integration/pipeline-designer/broken-reference)
