# Source: https://docs.axonius.com/docs/prtg-network-monitor.md

# PRTG Network Monitor

PRTG is a network monitoring application for Windows and Linux systems and servers, as well as miscellaneous hosts such as switches, routers, and other devices.

**Related Enforcement Actions:**

* [PRTG - Add/Remove Tags](/docs/prtg-update-tags)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the PRTG Network Monitor server.
2. **User Name** and **Passhash** *(optional)* - The credentials for a user account that has the  permissions to fetch assets.  Get the passhash from Setup -> Account Settings -> My Account. Click "Show passhash" and copy it.

<Callout icon="📘" theme="info">
  Note

  When **API Token** is not supplied, **User Name** and **Passhash** are required.
</Callout>

3. **API Token** *(optional)* - An API Token associated with a user account that has permissions to fetch assets. For information about how to create an API Token, see [PRTG Manual: API Keys](https://www.paessler.com/manuals/prtg/api_keys).

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **API Token** is required.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![PRTg.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PRTg.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Items per page** *(default: 500)* - Set the number of PRTG devices to fetch in each API request during pagination.
2. **Fetch device sysinfo**   - Select this option to fetch sysinfo for each device.
3. **Parse Hostname from 'host' field** - Select this option to parse the hostname from the 'host' field. This setting only applies if the value in the 'host' field is not recognized as an IP address.
4. **Fetch Parent Tags** -  Select this option to fetch Parent Tags data on each device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [PRTG API](https://www.paessler.com/manuals/prtg/application_programming_interface_api_definition).

## Supported From Version

Supported from Axonius version 4.5