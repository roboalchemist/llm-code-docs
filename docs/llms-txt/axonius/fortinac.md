# Source: https://docs.axonius.com/docs/fortinac.md

# FortiNAC

FortiNAC is a network access control solution that provides protection against IoT threats, control of third-party devices, and automated responses to networking events.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the FortiNAC server.

2. **API Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="FortiNAC" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FortiNAC.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Do not fetch devices without a MAC Address** - Select this option to not fetch devices that do not have  a MAC address.

2. **Do not fetch devices without a Hostname** - Select this option to not fetch devices that do not have a Hostname.

3. **Fetch ports** - Select this option to fetch the ports from the Fortinac system and add it to the information on the device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the:

* FortiNAC REST v2 API
* FortiNAC REST Schema API

## Required Permissions

The value supplied in [API Token](#parameters) must be associated with  credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.6