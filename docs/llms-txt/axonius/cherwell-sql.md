# Source: https://docs.axonius.com/docs/cherwell-sql.md

# Cherwell IT Service Management (SQL)

Cherwell IT Service Management Database is a service desk platform enabling automation for process workflows, supporting tasks, and related approvals.
The Cherwell IT Service Management Database adapter uses SQL to fetch information about devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Cherwell IT Service Management Database instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **Database** *(required, default: MGTPCSM)* - The name of the database inside the SQL Server.
4. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

5. **Password** *(required)* - The user's password. The password must not include ";".
6. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image align="center" alt="Cherwell.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cherwell.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections for this adapter.

2. **CI type name include list** *(optional)* - Specify a comma-separated list of CI types ([Configuration Items, such as: computer or mobile device.](https://cherwellsupport.com/WebHelp/es/5.0/23293.htm)) in Cherwell.
   * If supplied, all connections for this adapter will only collect devices of the CI types provided in this list.
   * If not supplied, all connections for this adapter will not collect any devices of any CI type.

3. **Use Last Reconciled as Last Seen**
   * If enabled, all connections for this adapter will map Cherwell's **Last Reconciled** field as the device's **Last Seen** field.
   * If disabled, all connections for this adapter will not map Cherwell's **Last Reconciled** field as the device's **Last Seen** field.

4. **Use Last Discovery as Last Seen** - If enabled, all connections for this adapter will map Cherwell's **Last Discovery** field as the device's **Last Seen** field.

5. **Status include list** *(optional)* - Only fetch devices with the specified status. Enter a list of statuses separated by commas.

6. **Parse Device Model values as Device Model Family fields**  - Select this option to parse the vendor model into the “device model family”  field instead of device model.

7. **Fetch only deployed devices**
   * If enabled, all connections for this adapter will fetch only deployed devices.
   * If disabled, all connections for this adapter will fetch all device types.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.