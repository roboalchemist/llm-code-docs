# Source: https://docs.axonius.com/docs/snow-software-exceptions.md

# Snow Software Exceptions

Snow Software Exceptions adapter provides a way to track and manage software exceptions.

<Callout icon="📘" theme="info">
  Note

  Axonius considers the results imported from the SQL server as if these were received from a CSV file. This means  the imported data must include at least one column of required data as specified in the [CSV adapter - Which fields will be imported with a devices file?](/docs/csv#which-fields-can-be-populated-for-each-file-import-type)
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Server Host or IP Address** *(required)* - The hostname / domain of the SQL server.<br />
   For MSSQL:
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(required)* - The port of the SQL server.
   For MSSQL the required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **Database** *(required)* - The database to connect to.
4. **Table** *(required)* - The name of the table to fetch information from. Axonius runs a *'SELECT \* FROM \[\[specified value]]'* statement.
5. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you're using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

6. **Password** *(required)* - The user's password. The password must not include ";".
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="Snow_Software_Exceptions" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Snow_Software_Exceptions.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections  for this adapter.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Creating a Local Read-Only User for Microsoft SQL Server

To connect to the Microsoft SQL Server to create a Local Read-Only User, you can use Microsoft SQL Server Management Studio. If you don't have it on your local machine, you can probably find it on the machine the Microsoft SQL Server is installed on.

After connecting to the server, do the following:

1. If you don't have the name of your database, expand the **Databases** folder which shows all the databases in this server. Your database should appear here, starting with **"CM\_"**.

2. Navigate to the **Security** folder and expand it. Right-click the **Logins** folder and click **New Login**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(45).png" />

3. Create a user using the **"SQL Server Authentication"** option. Fill in the details and select your database from the **Default Database List**.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(46).png" />

4. Navigate to the **User Mapping** page, and check the check box for the database that your login can access. In the **Database role membership list**, leave the default option **public** selected, and select the **db\_datareader** check box.

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(47).png" />

5. Click **OK** and create the user.

6. Reconnect with the new user to validate that it was indeed created (**File** -> **Connect Object Explorer**).

   <Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(48).png" />

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.