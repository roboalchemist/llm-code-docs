# Source: https://docs.axonius.com/docs/forescout-switch-plugin.md

# Forescout Switch Plugin

Forescout Switch Plugin is a component of the ForeScout CounterACT Network Module and provides switch to endpoint information as well as VLAN and ACL management capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Forescout Switch Plugin server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Client ID** *(optional)* - A Switch API client ID. This should contain the s-oauth-client.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ConnectionParameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-OHET05WN.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use X field for Host Name/Asset Name** - Enter the field and path from the raw JSON to use for the Host Name/Asset Name.
2. **Remove Prefix from Host Name/Asset Name** - Enter a list of possible prefixes that need to be removed from the Asset Name and Host Name fields.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Forescout Switch API](https://docs.forescout.com/bundle/switch-api-8-4-htg/page/about-the-switch-api.html).

To work with the Forescout Switch API, you must define IP address range(s) that can access REST API Web features. Follow the steps in [Set Up Web Access](https://docs.forescout.com/bundle/switch-api-8-4-htg/page/t-switch-api-web-access.html). When adding an IP Address range, either add **REST APIs** for all IPs, or specify the Axonius IP.

## Required Permissions

The **User Name** used to connect to the adapter must have a Switch API Read permission. See [About the Switch API](https://docs.forescout.com/bundle/switch-api-8-4-htg/page/about-the-switch-api.html) for more information.

## Supported From Version

Supported from Axonius version 6.0