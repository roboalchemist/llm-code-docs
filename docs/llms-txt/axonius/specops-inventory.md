# Source: https://docs.axonius.com/docs/specops-inventory.md

# Specops Inventory

Specops Inventory collects and reports information on hardware, software, registry, user settings, operating system, security data, and Active Directory data.

## Adapter Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Specops Inventory instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}`\\`{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)* - The port used for the connection.
3. **Database** *(required)* - The name of the database inside the SQL Server (Usually starts with "CM\_").
4. **User Name** *(required)* - A user name with read-only permissions .
   **Important Notes:**
   * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
   * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
5. **Password** *(required)*  - The user's password. The password must not include ";".

![Specops.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Specops.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters)
</Callout>

To configure the Specops adapter advanced settings, open the **Specops Inventory adapter** page, click **Advanced Settings**, and then click the **Specops Configuration** tab:

* **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control on the performance of all connections of for this adapter.

![SpecopsAdv.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SpecopsAdv.png)

<Callout icon="📘" theme="info">
  NOTE

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.