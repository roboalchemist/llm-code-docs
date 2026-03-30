# Source: https://docs.axonius.com/docs/hpdm.md

# HP Device Manager (HPDM)

HP Device Manager (HPDM) is an enterprise-class application for managing and administrating thin client devices on large- and small-scale networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Server Host or IP Address** *(required)* - The DNS / IP Address of the Microsoft SQL Server HP Device Manager instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}` `{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The required ports are:
   * Microsoft SQL Server discovery port - 1433.
   * The specific port for the supplied named instance, if relevant.
3. **Database** *(required, default: HPDM)* - The name of the database inside the SQL Server.
4. **User Name** *(required)* - The credentials for a user account that has the required permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  * The best practice is to create a dedicated SQL local user for Axonius usage. For details on creating an Axonius user for Microsoft SQL Server, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).

  * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
</Callout>

5. **Password** *(required)* - The user's password. The password must not include ";".

6. **Database Type** *(required, default: MSSQL)* - Select either **MSSQL** or **PostgreSQL** as the database type.

7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="HPDM(1)" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HPDM(1).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control on the performance of all connections for this adapter.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [HP Device Manager 5.0 Administrator's Guide](https://ftp.ext.hp.com/pub/hpdm/Documentation/AdminGuide/5.0/HP_Device_Manager_5.0.3_Administrator_Guide_en_US.pdf).

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version            | Supported | Notes |
| ------------------ | --------- | ----- |
| 5.0.3 docs version | Yes       |       |

## Supported from Version

Supported from Axonius version 4.5

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.