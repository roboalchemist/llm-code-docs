# Source: https://docs.axonius.com/docs/lansweeper.md

# Lansweeper

Lansweeper is an IT asset management and Network Inventory software tool for Windows, Linux, Mac, and Network devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Lansweeper instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port used for the connection.
3. **Database** *(required)* - The name of the database inside the SQL Server (usually starts with "CM\_").
4. **User Name** *(required)* - A user name with read-only permissions.
   **Important Notes:**
   * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/sql-server#creating-a-local-read-only-user-for-microsoft-sql-server).
   * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
5. **Password** *(required)*  - The user's password. The password must not include ";".
6. **TDS Driver Version** *(optional, default: 8.0)* - Specify which TDS Driver version to use, either 7.0 or 8.0.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Lansweeper.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Lansweeper.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(optional, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control on the performance of all connections of for this adapter.
2. **Do not fetch devices with no MAC address** - Select this option to not fetch devices that don't have a MAC address.
3. **Display only fetched Windows assets** - Select this option to only fetch devices having a Windows asset type.
4. **List of tags to parse as fields** - Enter a list of tags to parse as fields.
5. **Add adapter tags as dynamic fields** - Select this option to add adapter tags as dynamic fields.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.