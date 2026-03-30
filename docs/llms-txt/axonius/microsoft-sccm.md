# Source: https://docs.axonius.com/docs/microsoft-sccm.md

# Microsoft Endpoint Configuration Manager (MECM)

Microsoft Endpoint Configuration Manager (MECM) (formerly SCCM) is a comprehensive management solution for Microsoft Windows operating systems along with some capabilities for Linux, Mac OS, and mobile devices.

**Use cases the adapter solves**

MECM is a powerful endpoint management solution that provides a robust inventory of our managed devices in Axonius. Even more importantly, by combining MECM with network/infrastructure data coming from additional adapters, we can identify unmanaged or even rogue devices on the network.

**Data retrieved by MECM**

Axonius  collects common device information such as the hostname, IPs, MAC address, and serial number. The adapter connects directly to the MECM MSSQL database to pull additional device information such as installed software, patches, and collection data.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Software, SaaS Applications

## Before You Begin

### Authentication Methods

To connect the adapter, you can use either of the following authentication methods:

* **SQL Auth** - Requires a User Name and Password.
* **Kerberos with Password** - Requires User Name, Password, Realm, and Kerberos KDC.
* **Kerberos with Keytab** - Requires User Name, Keytab, Realm, and Kerberos KDC.
  See [Connecting the Adapter in Axonius](/docs/microsoft-sccm#connecting-the-adapter-in-axonius) for more information.

### Required Ports

Axonius must be able to communicate with the MSSQL Server via one of the following ports:

* Microsoft SQL Server discovery port - 1433 (default for non SA users) 1434 (default for SA - SuperAdmin - users).
* The specific port for the supplied named instance, if relevant.
* The port appended into the adapter configuration needs to match the global listening port of the SCCM database.

<Callout icon="📘" theme="info">
  Note

  The ports listed above are the standard default SCCM ports. However, these ports might be different if SCCM is deployed and configured with custom ports specified by the customer.
</Callout>

## Connecting the Adapter in Axonius

### Required Parameters

1. **MECM/MSSQL Server** - The DNS / IP Address of the Microsoft SQL Server your MECM instance is using.
   * To use a specific named instance, the value supplied should be in the following format: `{server_host}\{instance_name}`.
   * If no instance is supplied, the default instance will be used.
2. **Port** - The port used for the connection. The default is 1433. See [Required Ports](/docs/microsoft-sccm#required-ports) for more information.
3. **Database** - The name of the database inside the SQL Server (Usually starts with "CM\_").
4. **Authentication Method** - Select an authentication method and provide additional parameters accordingly:

<Tabs>
  <Tab title="SQL Auth">
    1) \*\*User Name\*\* - A user name with read-only permissions .

       * The best practice is to create a dedicated SQL local user for Axonius usage. For details, see [Creating a Local Read-Only User  for Microsoft SQL Server](/docs/microsoft-sql-server-mssql#creating-a-local-readonly-user-for-microsoft-sql-server).
       * If you are using a domain user, specify the domain and the user name in the following format: domain\username.

    2) **Password**  - The user's password. The password must not include ";".
  </Tab>

  <Tab title="Kerberos with Password">
    1. **Realm** - The domain in which your Kerberos authentication server has the authority to authenticate users.
    2. **Kerberos KDC** - The FQDN for the server or domain controller responsible for the KDC (Kerberos Distribution Center).
    3. **User Name** and **Password** - See SQL Auth.
  </Tab>

  <Tab title="Kerberos with Keytab">
    1. **Realm** - The domain in which your Kerberos authentication server has the authority to authenticate users.
    2. **Kerberos KDC** - The FQDN for the server or domain controller responsible for the KDC (Kerberos Distribution Center).
    3. **User Name** - See See SQL Auth.
    4. **Keytab** - Click **Upload File** to upload a Keytab file.
  </Tab>
</Tabs>

<br />

<Image alt="MECM_parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/MECMAdapter.png" />

### Optional Parameters

1. **Use SSL** - Select whether to use SSL.
2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Use Reverse DNS** *(only when using a Kerberos authentication)* - When a Kerberos client connects to a server, it needs to build the SPN (service principal name; for example, `MSSQLSvc/server.domain.com:1433`). However, If you only know the IP address of the server, you can try a reverse DNS lookup to resolve the IP back into a hostname. This hostname will then be used in the Kerberos ticket request. If the reverse DNS is misconfigured, Kerberos might generate the wrong SPN, and the authentication will fail.

<Callout icon="📘" theme="info">
  Note

  Generally, you don't need to enable **Use Reverse DNS** unless you have a network configuration that requires it.
</Callout>

3. **Do not fetch devices without 'Last Seen'** - Select whether to fetch devices without a Last Seen date.
   * If enabled, this adapter connection will not fetch devices if they do not have a Last Seen indication.
   * If disabled, this adapter connection will fetch devices even if they do not have a Last Seen indication.
4. **Only include Devices where Client Installed is True** - Select whether to only include devices when the **ClientInstalled** option in MECM is 'True'.
   * If enabled, this adapter connection will only fetch devices if they have a ClientInstalled indication.
   * If disabled, this adapter connection will fetch devices even if they do not have a ClientInstalled indication.
5. **Read Only Connection** - Select this option to pass down the parameter “APPLICATIONINTENT=READONLY" to the underlying driver, preventing the connection from modifying any data on the database.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch only active devices (Active0 = 1)** - Select to fetch only active devices where the value of Active0 is 1.

2. **Exclude IPv6 addresses** - Select whether to fetch IPv6 addresses. If cleared, the connections for this adapter will fetch both IPv4 and IPv6 addresses.

3. **Device id chunk size** - Set the device batch size (Number of devices) that is processed.

4. **SQL page size** *(required, default: 1000)* - Set the SQL page size that sent as part of the SQL connection.

5. **Machine domain  Include list** *(optional)* - Specify a comma-separated list of SCCM domains. If empty, the connections for this adapter will collect devices from any domain.

6. **Fetch v\_GS\_ADD\_REMOVE\_PROGRAMS software legacy table**  - Select whether to fetch installed software information from v\_GS\_ADD\_REMOVE\_PROGRAMS software legacy table.

7. **Fetch files path table** *(required, default: true)* - Select whether to fetch installed software path from the files path table. If cleared, the fetch process for this adapter will be faster.

8. **Find software independent files in the system (matching Regex)** - Enter a regex expression to search for and fetch files in the device’s software table that usually would not be retrieved because they are   ‘independent’ (i.e. executables or other script files not related to any specific software). The data fetched here is displayed in the ‘Software Independent Files’ field. You can only use this option if you enabled ‘Fetch files path table’.

9. **Fetch v\_GS\_INSTALLED\_SOFTWARE table** *(required, default: true)* - Select whether to fetch installed software from the v\_GS\_INSTALLED\_SOFTWARE table. If cleared, the fetch process for this adapter will be faster.

10. **Fetch DEVICE\_INSTALLEDAPPLICATIONS\_DATA table** - Select whether to fetch installed software from the DEVICE\_INSTALLEDAPPLICATIONS\_DATA table.

11. **Fetch INSTALLED\_EXECUTABLE\_DATA table** - Select whether to fetch installed software from the INSTALLED\_EXECUTABLE\_DATA table.

12. **Fetch vSMS\_SUMDeploymentStatusPerAsset table** *(default: false)* - Select this option to fetch data from the 'vSMS\_SUMDeploymentStatusPerAsset' table for each asset.

13. **Parse all compliance status history per device** *(required, default: true)* - Select whether to parse historical compliance status information to the Current Compliance Status field.

14. **Parse the latest compliance status per device** *(required, default: true)* - Select whether to parse the latest compliance status information to the Current Compliance field.

15. **Fetch software update compliance with the following statuses** - Select up to 4 statuses from the dropdown list: Detection Status Unknown, Not Applicable, Required/Missing, Already Installed/Compliant. The adapter will fetch only the selected statuses.

16. **Allowed Collections** *(optional)* - Provide a list of collections to limit the fetch to.

17. **Fetch services information** *(required, default: true)* - Select whether to fetch services information for each device. If cleared, the fetch process for this adapter will be faster.

18. **Fetch v\_GS\_SOFTWAREPRODUCT software table** *(required, default: true)* - Select whether to fetch executable files from the v\_GS\_SOFTWAREPRODUCT table. If cleared, the fetch process for this adapter will be faster.

19. **Fetch EP\_AntimalwareHealthStatus Windows Defender AV definition table** *(optional)* - Select whether to fetch Windows Defender Health Status from the EP\_AntimalwareHealthStatus.

20. **Fetch devices from the following additional tables** *(optional)* - Enter a comma- separated list of SQL tables from which additional device information is fetched. If parameter is empty, no additional device information will be fetched for this connection.
    * To be considered a valid table, it should have:
      * a column called "ResourceID" or "MachineID" as the device identifier
      * less than or equal to 100 columns
      * be in the default database (same that has v\_GS\_COMPUTER\_SYSTEM, v\_GS\_INSTALLED\_SOFTWARE,  table as e.g.)

    * This feature will fetch all the lines in the table that are associated with devices and add them as a field with the name “Table: `{table_name}`” on device-specific information.

21. **Fetch online data table** *(required, default: true)* - Select whether to fetch fields from the v\_CollectionMemberClientBaselineStatus SCCM table. When you select this parameter, Axonius fetches  online data from the following fields: CNIsOnline, CNLastOnlineTime, CNLastOfflineTime, CNIsOnInternet, CNAccessMP

22. **MSSQL Connection Timeout** *(required, default: 30)* - Specify the number of minutes that elapse before the MSSQL connection times out.

23. **Populate "Device:Last Used User" only for users seen within the past X days** - Specify the number of past days from which you want the adapter to populate the Last Used User field in the Devices table.

24. **Populate Installed Software: Last Used On for software used within the past number of days, greater than 0.** *(optional, default: 90)* -
    * When the number entered is greater than 0, the SCCM adapter will fetch results from the **Installed Software: Last Used On** field in SCCM if the installed software was used within the specified number of days.
    * If the field value is zero or empty, **Installed Software: Last Used On** information won’t be retrieved and the SCCM adapter will have a faster fetch.

25. **Custom Admin Data Table Name** *(optional)* - Enter a table name. The table must be in the same database as defined in the adapter connection. This configuration should only be set if the customer is missing Local Admin Data in their SCCM device records. The columns that the user provides are mapped to columns in Axonius and need to be named as shown below in the mapping column.

    <Table align={["left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Axonius field name
          </th>

          <th style={{ textAlign: "left" }}>
            Name mapped to in Custom Admin Data Table
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            Asset ID
          </td>

          <td style={{ textAlign: "left" }}>
            ResourceID
            MachineID
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Name
          </td>

          <td style={{ textAlign: "left" }}>
            account0
            User0
            Account0
            Name00
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Domain
          </td>

          <td style={{ textAlign: "left" }}>
            domain0
            Domain0
            Domain00
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            SID
          </td>

          <td style={{ textAlign: "left" }}>
            SID0
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            User Type
          </td>

          <td style={{ textAlign: "left" }}>
            Category0
            Account00
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Account Type
          </td>

          <td style={{ textAlign: "left" }}>
            Type0
            Type00
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Status
          </td>

          <td style={{ textAlign: "left" }}>
            Enabled0
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Group
          </td>

          <td style={{ textAlign: "left" }}>
            name0
            LocalSecurityGroup0
            Name0
            Name00
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            Last Updated
          </td>

          <td style={{ textAlign: "left" }}>
            Timestamp
            TimeKey
          </td>
        </tr>
      </tbody>
    </Table>

    <br />

26. **Fetch licenses** - Select this option to fetch SCCM licenses.

27. **Don't fetch software reported as uninstalled by SCCM** *(required, default: true)* - Select whether to fetch software reported as uninstalled by SCCM.

28. **Use "Resource\_Domain\_OR\_Workgr0" as device domain** *(required, default: false)* - By default, the adapter uses the "Full\_Domain\_Name0" field as the device domain. Select this option to use the "Resource\_Domain\_OR\_Workgr0" field instead.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Troubleshooting

* **"Login failed"** - If you are using a domain user, in the **User Name** field, specify the domain and the user name in the following format: domain\username.

### Related enforcement actions

* [Microsoft System Center Configuration Manager (SCCM) - Add or Remove Assets to Collection](/docs/add-device-to-sccm-collection)(Deprecated)
* [Microsoft MECM - Add or Remove Devices to Collection](/docs/add-or-remove-device-in-sccm)
* [Microsoft MECM - Deploy Package to Devices](https://docs.axonius.com/axonius-help-docs/docs/deploy-package-in-sccm)
* [Microsoft MECM - Delete Devices](https://docs.axonius.com/axonius-help-docs/docs/delete-device-in-sccm)