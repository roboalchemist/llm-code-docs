# Source: https://docs.axonius.com/docs/sccm-warehouse.md

# Microsoft Endpoint Configuration Manager (MECM) for Data Warehouse

Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM) is a comprehensive management solution for Microsoft Windows operating systems along with some capabilities for Linux, Mac OS, and mobile devices.

This adapter connects directly to the MECM data warehouse to pull additional device information such as installed software, patches, and collection.

**Use cases the adapter solves**

MECM is a powerful endpoint management solution that provides a robust inventory of our managed devices in Axonius. Even more importantly, by combining MECM with network/infrastructure data coming from additional adapters, we can identify unmanaged or even rogue devices on the network.

**Data retrieved by MECM**

Axonius  collects common device information such as the hostname, IPs, MAC address, and serial number. The adapter connects directly to the MECM MSSQL database to pull additional device information such as installed software, patches, and collection data.

**Enforcements**
Axonius can add assets to MECM collections directly in the Enforcement Center.
Related enforcement actions:[Microsoft System Center Configuration Manager (SCCM) - Add or Remove Assets to Collection](/docs/add-device-to-sccm-collection).

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the MECM for Data Warehouse server.

2. **Port** *(optional)* - The port of the SQL server instance where MECM for Data Warehouse is running.

3. **Database Name** *(optional)* - The name of the database inside the SQL Server (Usually starts with "CM\_").

4. **User Name** *(required)* - A user name with read-only permissions.<br />
   **Important Notes:**
   * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
   * If you are using a domain user, specify the domain and the user name in the following format: domain\username.

5. **Password** *(required)*  - The user's password. The password must not include ";".

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Microsoft MECM for Data Warehouse" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Microsoft%20MECM%20for%20Data%20Warehouse.png" />

## Required Ports

Axonius must be able to communicate with the MSSQL Server via one of the following ports:

* Microsoft SQL Server discovery port - 1433 (default for non SA users) 1434 (default for SA - SuperAdmin - users).
* The specific port for the supplied named instance, if relevant.
* Note that the port appended into the adapter configuration needs to match the global listening port of the SCCM database.

<Callout icon="📘" theme="info">
  Note

  The ports listed above are the standard default SCCM ports. However, these ports might be different if SCCM is deployed and configured with custom ports specified by the customer.
</Callout>

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.