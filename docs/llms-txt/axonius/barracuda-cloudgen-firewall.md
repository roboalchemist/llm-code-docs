# Source: https://docs.axonius.com/docs/barracuda-cloudgen-firewall.md

# Barracuda CloudGen Firewall

Barracuda CloudGen Firewall provides real-time network protection against a broad range of network threats, vulnerabilities, and exploits.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Barracuda CloudGen Firewall.

2. **Port** *(required)* - The API port selected by the customer for REST API requests.

3. **API Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   To generate an API token, see [Barracuda CloudGen Firewall REST API](https://campus.barracuda.com/product/cloudgenfirewall/doc/96025925/rest-api/?sl=AYUqatEBrUlGJ8M9rn5O\&so=4).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Barracuda_CloudGen_Firewall" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Barracuda_CloudGen_Firewall.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  From Version 4.6, Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch users from last x seconds** *(required, default: 300)* - Enter the latest number of seconds to fetch users.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Barracuda CloudGen Firewall REST API](https://campus.barracuda.com/product/cloudgenfirewall/doc/96025925/rest-api/?sl=AYUqatEBrUlGJ8M9rn5O\&so=4).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with Administration account credentials for REST API Authentication.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version         | Supported | Notes |
| --------------- | --------- | ----- |
| 8.0 and greater | Yes       | --    |

## Supported From Version

Supported from Axonius version 4.7