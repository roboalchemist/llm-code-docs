# Source: https://docs.axonius.com/docs/flexera-it-asset-management.md

# Flexera IT Asset Management

Flexera lets enterprises gain visibility and control of IT assets, reduce ongoing software costs, and maintain continuous license compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications
* Containers

## Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Flexera instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}`\\`{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port used for the connection.
3. **Database Name** *(required)* - The name of the database inside the SQL Server. The common value is 'FNMSCompliance'.
4. **Inventory Database Name** *(optional)* - Specify the name of the Inventory Database that you want to fetch the software version, description, vendor, software path, and software name.
5. **Database Type** *(required)* - Select the database server as the source for data: **IM** or **FNMP**.  The common value is 'FNMP'.
6. **User Name** *(required)* - A user name that has the [Required Permissions](#required-permissions) to fetch assets.
7. **Password** *(required)* - The user's password. The password must not include ";".

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![FlexeraIT\_23-1-22](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FlexeraIT_23-1-22.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query to gain better control on the performance of all connections  for this adapter.
2. **Remove duplicate hardware name** - Select this option to avoid fetching multiple times devices with the same host name.
3. \*\*Do not fetch devices without 'Last Seen`** *(required, default: true)* - Select whether to exclude devices that do not have `last seen' indication.
4. **Use AssetStatusID from the Asset Table** - Select whether the **Status** field uses the value in the **Asset.AssetStatusID** or **AssetStatus.StatusDefaultValue**.
   * If not selected, the Status obtains its value from the **AssetStatus.StatusDefaultValue**.
   * If selected, the Status obtains its value from the **Asset.AssetStatusID** of the Asset table.
5. **Do not fetch hostnames containing specific strings** - Enter strings separated by commas. Devices that contain any of the strings will not be fetched.
6. **Do not pull devices with ComplianceComputer.AssetID == NULL** - Select this option to not pull devices with "ComplianceComputer.AssetID == NULL".
7. **Query to fetch** - From the drop-down select the query from which to fetch devices.  Select either **Basic Query** which includes mostly data from the ComplianceComputer table, or select **Additional Asset Information** which also includes data from the Asset table.
8. **Fetch Containers from FNMS** - Select this option to fetch containers from the FNMS database.
9. **FNMP Software table name** *(optional, default: InstalledSoftwareData)* - Enter the table name for software when using the FNMP database.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [FlexNet Manager Suite API](https://docs.flexera.com/FlexNetManagerSuite2023R2/EN/Schema/index.html#SysRef/schema/ComplianceSchema/Compliance.Logic.CoreTables/reference/ContainerInstance.html).

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.

* The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
* If you are using a domain user, specify the domain and the user name in the following format: domain\username.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.