# Source: https://docs.axonius.com/docs/windows-server-update-services-wsus-sql.md

# Windows Server Update Services (WSUS) SQL

Windows Server Update Services (WSUS) - SQL, previously Software Update Services (SUS), enables administrators to manage the distribution of updates and hotfixes released for Microsoft products.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **WSUS SQL Server** -  The hostname / domain of the WSUS SQL server.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **WSUS SQL Server Port** *(optional)* - The port of the WSUS SQL Server. Default 1443.
3. **User Name** *(required)* - The credentials for a user account that has read access to the WSUS SQL Server.

<Callout icon="📘" theme="info">
  NOTE

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

4. **Password** *(required)* - Password of a user that has read access to the WSUS SQL Server. The password must not include ";".

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="WSUSSQL" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WSUSSQL.png" />

## Required Ports

* 1433 or SQL Configured Port.

## APIs

[Using WSUS Views](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/bb410149\(v=vs.85\))

## Required Permissions

The value supplied in [User Name](#parameters) read  permissions to the WSUS SQL Database. If possible, a user that belongs to the WSUS Administrator Group.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.
* If the adapter configuration fails with the following error messages:
  * `Error reading share default path: ADMIN$, check if the share default path is accessibe by the configured user - Details: Invalid message received from Windows Server.."}]`
  * `Error message": "Kerberos login failed - Error: Empty Domain not allowed in Kerberos"`
    Do either of the following:
    * Ensure the user provided in the **User Name** field is a domain admin with admin permissions.
    * Ensure the [Required Ports](/docs/windows-server-update-services-wsus-sql#required-ports) are open.
    * Ensure the user provided in the **User Name** field has the following permission: `IsConnectionSecureForApiRemoting: True`
    * Try to enable any of the following optional parameters: **Use SSL for WSUS Service Connection** and **Do Not Pass Arguments to Get-WsusServer**