# Source: https://docs.axonius.com/docs/sql-server.md

# SQL Server

The SQL Server adapter imports device information from arbitrary SQL servers: Microsoft SQL Server, MySQL, Oracle and PostgreSQL.

<Callout icon="📘" theme="info">
  Note

  Axonius considers the results imported from the SQL server as if these were received from a CSV file. This means  the imported data must include at least one column of required data as specified in the [CSV adapter - Which fields will be imported with a devices file?](/docs/csv#which-fields-can-be-populated-for-each-file-import-type)
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Databases
* Networks
* Accounts/Tenants

## Parameters

1. **SQL Server Host** *(optional)* - The hostname / domain of the SQL server.<br />
   For MSSQL:
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **SQL Server Port** *(optional)* - The port of the SQL server.
   For MSSQL the required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.

  * If you are using Athena for your database type, enter your access key and secret key in the User Name and Password fields.
</Callout>

4. **Password** *(required)* - The user's password. The password must not include ";".
5. **SQL Server Database Name** *(required)* - The database to connect to.
6. **SQL Server Table Name** *(required)* - The name of the table to fetch information from. Axonius runs a *'SELECT \* FROM \[\[specified value]]'* statement.
7. **SQL Query** *(optional)* - Enter a query to run in SQL Server.

<Callout icon="📘" theme="info">
  Note

  * Only read-only queries are allowed.
  * Do not put ";" at the end of the query.
  * Chained queries are not allowed.
</Callout>

8. **Database Type** *(required)* - Select between MSSQL, PostgreSQL, MySQL, Oracle, HyperSQL, or Athena. MySQL also supports the MariaDB.
   * If **Athena** is selected, the following parameters appear:
     * **Region** *(required)* - The AWS region in which the Athena DB is located.
     * **Output Bucket** *(required)* - The S3 bucket used to output the query execution results.
   * If either **PostgreSQL** or **MySQL** are selected, the following parameters appear:
     * **SSL Connection** - Turn this on to enable SSL connection. When enabled, upload the following certificates: Root Certificate File, Client Certificate File, and Client Private Key File.
9. **Table asset type** - Select the asset type associated with the SQL Server table. Axonius will consider the data fetched from the specified table as the data of the selected asset type.
   * When selecting **Devices**, you can also fetch Software Vulnerabilities data in addition to device data. table with Software Vulnerabilities data must contain a CVE ID field. See [CSV](/docs/csv#which-fields-can-be-populated-for-each-file-import-type) for more information.
   * When selecting **Databases**, only databases listed under the SQL instance are fetched. This option is only valid when a valid **SQL Query** is provided. If no query is provided, a default query, "Select \* from `{Table Name}`" will be used.
10. **Fetch system users in addition to table** *(default: true)* - Select this option to not only fetch the SQL Server Table Name provided in the configuration but also query the system's Service Principle table for extra user assets.
11. **Server Tag** *(optional)* - Specify a custom tag for the SQL Server adapter connection that you have configured.
12. **MySQL Character Set** *(optional)* - Specify a custom character set (encoding) for connections to MySQL databases. Example values: 'utf8', 'latin1'. When no character set is specified, 'utf8' is used by default.<br />

<Callout icon="📘" theme="info">
  Note

  This option is only valid when **MySQL** is selected from the **Database Type** dropdown.
</Callout>

13. **Ignore entities in current connection that have not been seen in the last X hours** *(optional)* - Specify the number of hours, so that the system will not fetch entities that  were not  seen in the last x hours. When **Is Users Table** is configured, this refers to users; otherwise, this refers to devices.
14. **Delete entities in current connection that have not been returned in the last X hours** *(optional)* - Specify the number of hours, so that the system will delete entities that  were not  fetched in the last x hours. When **Is Users Table** is configured, this refers to users; otherwise this refers to devices.
15. **MSSQL Connection Timeout** *(optional)* - Specify a custom timeout in seconds for MSSQL connections.
16. **Multi-value fields delimiter** *(optional)* - Specify a delimiter to separate between values within the same column in the imported SQL table. When you specify a delimiter Axonius considers fields that contain the specified delimiter as multi-value fields. For example, ';'. Otherwise Axonius considers all imported fields as single-value fields.
17. **Allow empty values** - Select this option to allow the system to support assets with empty fields.  If an asset was created with a field that contained a value, when the SQL file subsequently contains an empty field with the same name, the device or user asset will display that field without a value in it.
18. **Aggregate devices by key** *(optional)* - Select a key to aggregate assets by. The default option results in the following string:
    `{id or hostname or serial or name or maccaddress}_{table_name}_{instance}_{hostname}_{serial}_{name}`
    Example:

```
table_name = "MyTable"
Device: {
  'id': 'id1',
  'serial': 'serial'
}
aggregation_key = "id_MyTable_serial"
```

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="sql server connection" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/sql%20server%20connection.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Set Time Zone** - Set the time zone of date/time field values fetched with this adapter. Default is UTC.
2. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections  for this adapter.
3. **Add dynamic date raw field** *(required, default: false)* - Select whether to duplicate each date field appearing in the MSSQL database as a text value. The name of the new field is appended with the ‘\_raw’ suffix.
4. **Parse Asset Name as Hostname when Hostname is missing** *(required, default: false)* - Select this option to use the Asset Name as the Hostname value when no Hostname value is provided.
5. **Parse entity fields dynamically** - This setting is enabled by default so that the adapter dynamically parses all of the fields of the entity fetched. Unselect to disable this setting.
6. **Custom Parsing** - see [Adapter Custom Parsing](/docs/adapter-custom-parsing) for more information.

<Callout icon="📘" theme="info">
  Note

  In the Raw Path parameter of Custom Parsing, it is recommended to copy the path directly from the JSON view inside the asset profile. See more details in the JSON and XML Advanced View section, under [Adapter Connections](/docs/asset-profile-page#adapter-connections).
</Callout>

7. **Ignore hostname if IP is present** - Select this option to ignore the hostname parsing if it contains an IP address from the asset's IP address list.
8. **Aggregate devices by key** - Select a key to aggregate devices by: Name, Hostname, IP address, MAC address, or Serial number.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Enabling TCP/IP for the SQL Server

In order to connect to the SQL instance, TCP must be enabled. By default,  Microsoft SQL or Microsoft SQL Express has TCP/IP access disabled. Perform the following on the SQL Server Configuration Manager to make sure that TCP/IP access is enabled on your server.

1. Open the **SQL Server Configuration Manager**.

   <Image align="center" alt="SQLServer1" border={false} width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SQLServer1.png" />

2. Under **SQLServer Network Configuration**,  click **Protocols for SQLEXPRESS** (or the equivalent for your SQL server).

   <Image alt="SQLTCP" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SQLTCP.png" />

3. If TCP/IP is set to 'Disabled', right click and select 'Enable'.

4. The system informs you that your changes will be saved, but that you need to stop and restart the SQL Service. Go to Services on your system and restart the SQL Service.

   <Image alt="SQLRestart" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SQLRestart.png" />

## Creating a Local Read-Only User for Microsoft SQL Server

To connect to the Microsoft SQL Server to create a Local Read-Only User, you can use Microsoft SQL Server Management Studio. If you don't have it on your local machine, you can probably find it on the machine the Microsoft SQL Server is installed on.

After connecting to the server, you should do the following:

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

### Related Enforcement Actions

* [SQL - Update Assets in Table](/docs/sql-update-asset-in-table)
* [SQL - Send Assets to Table](/docs/send-to-sql-table)