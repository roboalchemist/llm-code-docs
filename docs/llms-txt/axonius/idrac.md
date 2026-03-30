# Source: https://docs.axonius.com/docs/idrac.md

# Dell iDRAC

The Integrated Dell Remote Access Controller (iDRAC) is designed for secure local and remote server management and helps IT administrators deploy, update and monitor Dell EMC PowerEdge servers.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the [Redfish API for Integrated Dell Remote Access Controller (iDRAC)](https://developer.dell.com/apis/2978/versions/4.xx/docs/0WhatsNew.md).

### Permissions

The user name and password should have the appropriate permissions to make the API calls listed.

#### Supported From Version

Supported from Axonius version 4.4

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - Enter one or more comma-separated hostnames, IP addresses or CIDR blocks of the Dell iDRAC server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.

![Dell iDRAC.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dell%20iDRAC.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the values supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to the values supplied in **Host Name or IP Address**.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the values supplied in **Host Name or IP Address** via the values supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the values supplied in **Host Name or IP Address** via the values supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Async chunks in parallel** *(required, default: 50)* - Specify the number of asynchronous chunks that will run in parallel.
2. **Timeout for a new connection in seconds** *(optional, default: 30)* - Specify a custom timeout in seconds for Dell iDRAC connections.
3. **Use SKU as device serial** - Select this option to use SKU as a serial number.
4. **Fetch storage instance data** - Select this option to fetch storage devices from Dell iDRAC.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                  | Supported | Notes |
| ------------------------ | --------- | ----- |
| iDRAC version 4.40.00.00 | Yes       |       |