# Source: https://docs.axonius.com/docs/symantec-endpoint-protection-12x.md

# Symantec Endpoint Protection 12.x

Symantec Endpoint Protection 12.x manages events, policies, and registration for the client computers that connect to customer networks.

<Callout icon="📘" theme="info">
  Note

  This page describes how to connect Symantec Endpoint Protection 12.x deployments. To connect Symantec Endpoint Protection 14.x, see [Symantec Endpoint Protection 14.x](/docs/symantec-endpoint-protection).
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Adapter Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Symantec Endpoint Protection 12.x  instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port used for the connection.
3. **Database** *(required)* - The name of the database inside the SQL Server (Usually starts with "CM\_").
4. **User Name** *(required)* - A user name with read-only permissions.<br />
   **Important Notes:**
   * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
   * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
5. **Password** *(required)*  - The user's password. The password must not include ";".

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SymantecEndPoint12.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SymantecEndPoint12.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query to gain better control on the performance of all connections for this adapter.
2. **Fetch scans** - Select this option to fetch scans information for each device.
3. **Fetch groups** - Select this option to fetch groups for each device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.