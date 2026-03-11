# Source: https://docs.axonius.com/docs/rca.md

# Persistent Systems Radia Endpoint Manager

Persistent Systems Radia Endpoint Manager (formerly RCA) is an end-user device (PC and mobile device) lifecycle management tool for automating routine client-management tasks.

<Callout icon="📘" theme="info">
  Note

  Axonius considers the results imported from the SQL server as if these were received from a CSV file. This means  the imported data must include at least one column of required data as specified in the [CSV adapter - Which fields will be imported with a devices file?](/docs/csv#which-fields-can-be-populated-for-each-file-import-type)
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Server Host or IP Address** *(required)* - The hostname / domain of the Persistent Systems Radia Endpoint Manager server.
   For MSSQL:
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}`\\`{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port of the Persistent Systems Radia Endpoint Manager server.
   For MSSQL the required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **Database** *(required, default: RCA\_DATABASE)* - The database to connect to.
4. **SQL Server Table Name** *(required, default: DeviceConfig)* - The name of the table to fetch information from. Axonius runs a *'SELECT \* FROM \[\[specified value]]'* statement.
5. **Database Type** *(required, default: MSSQL)* - Select either **MSSQL** or **Oracle**.
6. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

7. **Password** *(required)* - The user's password. The password must not include ";".
8. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="PersistentSystemsRadia" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PersistentSystemsRadia.png" />

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

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.