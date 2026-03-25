# Source: https://docs.axonius.com/docs/anomali-threatstream.md

# Anomali ThreatStream

Anomali ThreatStream is a threat intelligence management platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Anomali ThreatStream server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Anomali%20Threatstream](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Anomali%20Threatstream.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices from Devices Endpoint** *(default: true)*  - By default, Axonius fetches devices. Toggle off this option to not fetch devices.
2. **Fetch Users from Users Endpoint** *(default: true)* - By default, Axonius fetches users. Toggle off this option to not fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Anomali ThreatStream API](https://support.axonius.com/attachments/token/4oX7g2hwjDlYllnQSnYe5hMob/?name=ThreatStream+API+Reference+Guide.pdf).

## Required Permissions

User ID and API key are required to access ThreatStream through the APIs. These credentials are obtained from your ThreatStream Org Admin.

## Supported From Version

Supported from Axonius version 6.0