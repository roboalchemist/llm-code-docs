# Source: https://docs.axonius.com/docs/securew2.md

# SecureW2 JoinNow

A suite of network security software that helps organizations deploy WPA2-Enterprise Wi-Fi security and utilize X. 509 certificates beyond Wi-Fi for VPN, Web/Browser authentication and SSL (DPI) Inspection.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.securew2.com`)* - The hostname or IP address of the SecureW2 JoinNow server.

2. **API Secret** *(required)* - An API Secret associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SEcureW2JoinNow.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SEcureW2JoinNow.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Async chunk size** - (*Default, 100*). Set a value for the chunk size of the async requests. This sets the number of requests that can be sent in parallel.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [SecureW2 JoinNow Connector API](https://cloud.securew2.com/resources/guides/SecureW2_JoinNow_Connector_API_Guide.pdf).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have permissions to fetch assets.
You need to generate a Management Services Token from SecureW2's API Token mechanism. Refer to 'Creating Management Services Token' in [SecureW2 JoinNow MultiOS and Connector Configuration Guide](https://cloud.securew2.com/resources/guides/SecureW2_JoinNow_MultiOS_Configuration_Guide.pdf)..

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                          | Supported | Notes |
| -------------------------------- | --------- | ----- |
| JoinNow Connector version 5.22.x | Yes       |       |

## Supported From Version

Supported from version 4.4