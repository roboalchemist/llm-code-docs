# Source: https://docs.axonius.com/docs/beyondtrust-privilege-management-for-windows.md

# BeyondTrust Privilege Management OnPrem

BeyondTrust Privilege Management OnPrem delivers privilege management and application control, allowing organizations to eliminate admin rights across the entire business and enforce least privilege.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your BeyondTrust Privilege Management Reporting instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port used for the connection.
3. **Database** *(required)* - The name of the database inside the SQL Server (Usually starts with "CM\_").
4. **User Name** *(required)* - A user name with read-only permissions

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/sql-server#creating-a-local-read-only-user-for-microsoft-sql-server) .

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

5. **Password** *(required)* - The user's password. The password must not include ";".

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BeyondTrust%20Privilege%20Management%20OnPrem" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrust%20Privilege%20Management%20OnPrem.png" />

<Callout icon="📘" theme="info">
  Note

  This adapter requires “BeyondTrust Privilege Management Reporting” which is an “event centralization” utility of BeyondTrust EPM. The adapter is basically an MSSQL adapter and does not connect to the EPM directly.
</Callout>

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections  for this adapter.
2. **Get latest host** *(optional, default: False)* - Select to fetch only the latest record for each host. If option is not selected, all records for each host are fetched.

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