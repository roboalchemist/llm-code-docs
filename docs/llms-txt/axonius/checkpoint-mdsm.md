# Source: https://docs.axonius.com/docs/checkpoint-mdsm.md

# Check Point Multi-Domain Security Management (MDSM)

Check Point Multi-Domain Security Management (MDSM) is a centralized platform that provides comprehensive security management across multiple domains.

The Check Point MDSM adapter enables Axonius to fetch and consolidate device details from multiple security domains, ensuring centralized visibility into security gateways, servers, and host configurations.

## Asset Types Fetched

* Devices

## Before You Begin

### Required Ports

* TCP Port 443

### Authentication Methods

* API Key
* Login Credentials

### Required Permissions

* **Management API Login** - The user account used for the connection must have the Management API Login permission enabled in their permission profile.

  <Callout icon="💡" theme="warn">
    Important

    Check Point permission profiles distinguish between SmartConsole (GUI) access and Management API access. This setting must be explicitly enabled to allow API connections, even for read-only users.
  </Callout>
* **Read-Only Access** - At a minimum, the user requires Read-Only permissions for the asset domains.
* **System Domain Permissions** - If you are using the System Domain configuration, ensure the user has permissions to view the System Domain and all underlying domains.

### Verifying Permissions in the Check Point SmartConsole

1. Go to **Manage & Settings > Permissions & Administrators > Permission Profiles**.
2. Ensure the assigned profile has **Read-Only** access to the relevant domains.
3. Under **Management**, ensure **Management API Login** is selected.

### APIs

Axonius uses the <Anchor label="Check Point Management API" target="_blank" href="https://sc1.checkpoint.com/documents/latest/APIs/?#introduction~v2%20">Check Point Management API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 6.1.54.0.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Check Point MDSM server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Authentication Type** - Select Authentication type, either **API Key** (default) or **Login Credentials**.
   * **API Key**:
     * **API Key** - An API Key associated with a user account that has permissions to fetch assets.
   * **Login Credentials**:
     * **User Name** and **Password** - The credentials for a user account that has  permission to fetch assets.

<Image align="center" alt="Check Point MDSM - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Check_Point_MDSM_Add_Connection.png" className="border" />

### Optional Parameters

1. **System Domain** - Select this option to fetch data from the System Domain level (all domains). If enabled, the **Multi-Checkpoint Domain** configuration (below) is ignored.

   <Callout icon="📘" theme="info">
     Note

     Fetching from the System Domain runs requests on all domains and may return data with fewer details compared to querying specific domains.
   </Callout>
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
4. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
5. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.
6. **Multi-Checkpoint Domain** - Specify the Multi-Checkpoint domain name to fetch data from. This is useful if you have multiple domains configured in Check Point and you want to send the fetch request only to a specific one. This setting is ignored if **System Domain** (above) is selected.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch Devices of sub type server from Gateways and Servers** - Select this option to fetch devices classified as server subtypes from the gateways and servers data source.
2. **Fetch Devices of sub type host from Host Details** - Select this option to fetch devices classified as host subtypes from host details.

## Version Matrix

This adapter was tested only with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| API v2  | Yes       | --    |

<br />