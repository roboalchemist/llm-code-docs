# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database/connect-to-azure-azure-sql-database.md

# Source: https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database/connect-to-azure-azure-sql-database.md

# Connect to an Azure database

Perform the following steps to connect to your database:

1. Start the PDI client and create a new transformation or job.

   See the **Pentaho Data Integration** document for instructions on creating a PDI transformation.

   **Note:** You can also use the Pentaho User Console to make this connection. See [Define data connections](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections)
2. In the **View** tab of the **Explorer** pane, double-click on the **Database connections** folder. The **Database Connection** dialog box appears, as shown below:

   ![Database connection dialog for Azure SQL](https://3897443520-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F7HOrU4JuCmIFVNup2Gxd%2Fuploads%2Fgit-blob-f60eccc56d0067c7af5f89ba749a243be3bcdd0c%2FDatabase%20connection%20dialog%20for%20Azure%20SQL.png?alt=media)
3. Enter your database connection information.

   | Field                         | Description                                                                                                                                                                                                                                                                                                                                                           |
   | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **Host Name**                 | The name of the Azure SQL server instance.                                                                                                                                                                                                                                                                                                                            |
   | **Database Name**             | The name of the Azure SQL database to which you are connecting.                                                                                                                                                                                                                                                                                                       |
   | **Port Number**               | The TCP/IP port number. The Azure SQL Database service is only available through TCP port 1433. You must set your firewall to allow outgoing TCP communication on port 1433.                                                                                                                                                                                          |
   | **Authentication method**     | The authentication method used to connect to the Azure SQL DB instance. The default is SQL Authentication.                                                                                                                                                                                                                                                            |
   | **Username**                  | The username used to connect to the database.                                                                                                                                                                                                                                                                                                                         |
   | **Password**                  | The password used to connect to the database.                                                                                                                                                                                                                                                                                                                         |
   | **Always Encryption Enabled** | Select to use encryption. See [Use the Always Encryption Enabled option](https://docs.pentaho.com/install/10.2-install/pentaho-configuration/tasks-to-be-performed-by-a-pentaho-administrator/define-data-connections/enter-database-connection-information/connect-to-an-azure-sql-database/use-the-always-encryption-option) for instructions on using this option. |
   | **Client id**                 | The unique client identifier, used to identify and set up a durable connection path to the server.                                                                                                                                                                                                                                                                    |
   | **Client Secret Key**         | The unique name of the key value in the Azure Key Vault.                                                                                                                                                                                                                                                                                                              |
4. Click **Test**to verify your connection.
