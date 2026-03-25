# Source: https://docs.axonius.com/docs/manageengine-network-configuration-manager.md

# ManageEngine Network Configuration Manager

ManageEngine Network Configuration Manager is multi-vendor network change & configuration management software for switches, routers, and firewalls.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Vulnerabilities, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ManageEngine Network Configuration Manager server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ManageEngine%20Network%20Configuration%20Manager](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageEngine%20Network%20Configuration%20Manager.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Device summary with Device vulnerabilities** - Enable this option to enrich the device summary with device vulnerabilities.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [ManageEngine Network Configuration Manager REST API](https://www.manageengine.com/network-configuration-manager/help/rest-api-ncm.html#Generating_API_key).

## Supported From Version

Supported from Axonius version 6.0