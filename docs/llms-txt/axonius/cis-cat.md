# Source: https://docs.axonius.com/docs/cis-cat.md

# CIS-CAT Pro

CIS-CAT Pro is a tool for automating CIS Benchmark testing and reporting.

### Asset Types Fetched

* Devices, Databases

## Before You Begin

**Ports**

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

**Authentication Method**

* User Name/Password

### Permissions

The value supplied in [User Name](#required-parameters) must have Read access to SQL tables.

* The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
* If you are using a domain user, specify the domain and the user name in the following format: domain\username.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Server Host or IP Address** - The DNS / IP Address of the Microsoft SQL Server your CIS-CAT Pro instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}``{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(default: 1433)* - The required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **Database** *(default: ccpd)* - The name of the database inside the SQL Server.
4. **User Name** - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

5. **Password** - The user's password. The password must not include ";".
6. **Database Type** *(default: MSSQL)* - Select the database server as the source for data.

<Image alt="CIS_CAT" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CIS_CAT.png" />

<br />

### Optional Parameters

* **MySQL Character Set** - Specify a custom character set (encoding) for connections to MySQL databases. Example values: 'utf8', 'latin1'. When no character set is specified, 'utf8' is used by default.

<Callout icon="📘" theme="info">
  **Note**:

  This option is only valid when MySQL is selected from the **Database Type** dropdown.
</Callout>

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Specify the number of results per page received for a given SQL query to gain better control on the performance of all connections for this adapter.
2. **Parse devices with database field as Databases** - Select this option to parse devices with database field ("database.name") as Database assets.
3. **Aggregate Devices By Hostname** - Select this option to aggregate devices by hostname.
4. **Parse Benchmark By Latest Member** - Select this option to parse the latest benchmark from the value of the latest benchmark with a 'title\_value' of 'Level 1 - Member Server'.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| 2.2.3   | Yes       |       |

<br />

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.