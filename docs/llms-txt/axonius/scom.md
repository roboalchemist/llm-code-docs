# Source: https://docs.axonius.com/docs/scom.md

# Microsoft SCOM

Microsoft SCOM (System Center Operations Manager) is a cross-platform data center monitoring system for operating systems and hypervisors, reporting state, health and performance information of computer systems.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Server Host or IP Address** *(required)* - The hostname / domain of the Microsoft SCOM SQL server.
   For MSSQL:
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}`\\`{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional)* - The port of the SQL server.
   For MSSQL the required ports are:
   * Microsoft SQL Server discovery port - 1433.
3. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

4. **Password** *(required)* - The user's password. The password must not include ";".
5. **Database** *(required)* - The database to connect to.
6. **Use SSL** - Select whether to use SSL.
7. **Table Name to Fetch Computer Devices From** - Enter the table name from which devices will be fetched. The default is `MTV_Computer`.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MicrosoftScom](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-F2ME922H.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections  for this adapter.
2. **Devices type to fetch** *(required, default: Computer)*  - an array field that can select multiple types to fetch. You can choose either computer or agents.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Creating a Local Read-Only User for Microsoft SQL Server

To connect to the Microsoft SQL Server to create a Local Read-Only User, you can use Microsoft SQL Server Management Studio. If you don't have it on your local machine, you can probably find it on the machine the Microsoft SQL Server is installed on.

After connecting to the server, you should do the following:

1. If you don't have the name of your database, expand the **Databases** folder which shows all the databases in this server. Your database should appear here, starting with **"CM\_"**.

2. Navigate to the **Security** folder and expand it. Right-click the **Logins** folder and click **New Login**.

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(45\).png)

3. Create a user using the **"SQL Server Authentication"** option. Fill in the details and select your database from the **Default Database List**.

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(46\).png)

4. Navigate to the **User Mapping** page, and check the check box for the database that your login can access. In the **Database role membership list**, leave the default option **public** selected, and select the **db\_datareader** check box.

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(47\).png)

5. Click **OK** and create the user.

6. Reconnect with the new user to validate that it was indeed created (**File** -> **Connect Object Explorer**).

   ![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(48\).png)

## Suported from Version

Supported from Axonius version 4.5

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.