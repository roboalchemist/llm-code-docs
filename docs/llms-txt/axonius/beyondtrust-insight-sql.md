# Source: https://docs.axonius.com/docs/beyondtrust-insight-sql.md

# BeyondTrust BeyondInsight

BeyondTrust BeyondInsight provides discovery, management, auditing, and monitoring for any privileged credential.

**Related Enforcement Actions**

* [BeyondTrust BeyondInsight - Send Block Policy to SCP](/docs/beyond-trust-sql-send-block-policy-to-scp)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Server Host or IP Address** *(required)* - The DNS / IP Address of the Microsoft SQL Server your BeyondTrust BeyondInsight Database instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

5. **Password** *(required)* - The user's password. The password must not include ";".

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="BeyondTrust%20BeyondInsight" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrust%20BeyondInsight.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From version 4.6 Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

* **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of all connections  for this adapter.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [User Name](#parameters) must have Read permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.5

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.