# Source: https://docs.axonius.com/docs/scopnet.md

# ScopNET

ScopNET provides an agent-free solution for the prevention of unauthorized access to corporate networks, integrating switches, routers and firewalls to detect alien devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Microsoft Key Management Service (KMS) instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}`\\`{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port used for the connection.
3. **Database** *(required)* - The name of the database inside the SQL Server.
4. **Username** *(required)* - A user name that has the [Required Permissions](#required-permissions) to fetch assets.
5. **Password** *(required)*  - The user's password. The password must not include ";".
6. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1638\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections for this adapter.
2. **Do not fetch devices with no hostname** *(required, default: true)* - Select whether to exclude devices that do not have a hostname.
   * If enabled, all connections for this adapter will not fetch devices that do not have hostnames.
   * If disabled, all connections for this adapter will fetch devices, even those do not have hostnames.

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Required Permissions

The value supplied in [Username](#parameters) must have read access to devices.

* The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
* If you are using a domain user, specify the domain and the user name in the following format: domain\username.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.