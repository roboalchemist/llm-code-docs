# Source: https://docs.axonius.com/docs/mbam.md

# Microsoft BitLocker Administration and Monitoring (MBAM)

Microsoft BitLocker Administration and Monitoring (MBAM) provides a simplified administrative interface for BitLocker Drive Encryption. BitLocker offers protection against data theft or data exposure for computers that are lost or stolen,  encrypting all data that is stored on the Windows operating system volumes and drives and configured data drives.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **SCCM/MSSQL Server** - The DNS / IP Address of the Microsoft SQL Server your Microsoft BitLocker Administration and Monitoring (MBAM) instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** *(optional, default: 1433)*. - The port used for the connection.
3. **Database** - The name of the database inside the SQL Server (Usually starts with "CM\_").
4. **User Name** - A user name with read-only permissions.
   **Important Notes:**
   * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
   * If you're using a domain user, specify the domain and the user name in the following format: domain\username.
5. **Password** - The user's password. The password must not include ";".

<Image align="center" alt="MBAM" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/MSBitLockerAdmin%26Mon.png" />

### Optional Settings

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **SQL pagination** *(required, default: 1000)* - Set the number of results per page received for a given SQL query, to gain better control of the performance of connections for this adapter.

## Required Ports

Axonius must be able to communicate with the MSSQL Server via the following ports:

* Microsoft SQL Server discovery port - 1433.
* The specific port for the supplied named instance, if relevant.

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.