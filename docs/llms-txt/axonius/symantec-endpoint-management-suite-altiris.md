# Source: https://docs.axonius.com/docs/symantec-endpoint-management-suite-altiris.md

# Symantec Endpoint Management Suite (Altiris)

The Symantec Endpoint Management Suite (formerly Altiris) enables organizations to take control, uncover savings, and ensure compliance of IT assets, by giving a picture of assets throughout their lifecycle.

The Symantec Endpoint Management Suite adapter uses SQL to fetch information about devices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Software
* SaaS Applications

## Parameters

1. **MSSQL Server** *(required)* - The DNS / IP Address of the Microsoft SQL Server your Symantec Endpoint Management Suite instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)*  - The port used for the connection.
3. **Database** *(required, default: Symantec\_CMDB)* - The name of the database inside the SQL Server (Usually starts with "CM\_").
4. **User Name** *(required)* - A user name with read-only permissions.<br />
   **Important Notes:**
   * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
   * If you are using a domain user, specify the domain and the user name in the following format: domain\username.
5. **Password** *(required)*  - The user's password. The password must not include ";".

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SymantecEndPointMaangementSuite.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SymantecEndPointMaangementSuite.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control on the performance of all connections  for this adapter.
2. **Parse BIOS Serial Number as Device Manufacturer Serial** - When selected, the BIOS Serial is also used to populate the **Device Manufacturer Serial** field.
3. **Use nonlock in query** - Select  this option to fetch from Altiris tables without locking them.
4. **Fetch encryptions** - Select this option to fetch encryptions.
5. **Fetch only installed software** - Select this option to fetch only installed software.
6. **Collections memberships to fetch** - Enter a list of collection names. If the device is a member of those collections, the collection names will be added to a field called "Collections Memberships" in the device.
7. **Fetch local admin group members** - Select this option to enrich each device with its local admin group members and show this on the Devices page.
8. **Alternative Views** - You can fetch data about devices from Symantec Endpoint Management Suite views, instead of tables. To fetch data from Views, enter the name of the view from which you want to fetch data  in the relevant fields. If you leave these fields blank, Axonius fetches data about devices from the tables.

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