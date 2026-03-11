# Source: https://docs.axonius.com/docs/zscaler-zdx.md

# Zscaler ZDX

Zscaler Digital Experience (ZDX) is a  monitoring solution providing end-to-end visibility and troubleshooting of end-user performance issues for any user or application, regardless of location.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Software
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Zscaler ZDX server.

2. **API Key** and **API Secret** *(required)* - The API credentials associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Maximum requests per hour** *(default: 1000)* - Specify a rate limit for the number of requests per hour to be sent to Zscaler ZDX.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settingss).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Zscaler_ZDX" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Zscaler_ZDX.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch devices locations** - Select this option to fetch locations.
* **Fetch installed software** - Select this option to fetch installed software.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ZDX Reports API](https://help.zscaler.com/zdx/reports#/devices-get).

To access the ZDX API, you need to:

* [Create an API key](https://help.zscaler.com/zdx/managing-zdx-api-keys)
* Be a ZDX Advanced Plan User

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version | Supported | Notes |
| ------- | --------- | ----- |
| v3.4    | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7