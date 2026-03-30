# Source: https://docs.axonius.com/docs/n-able.md

# N-able

N-able provides integrated monitoring, management, security, and ticketing for managed service providers.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Software, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the N-able server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **JWT Token** *(optional)* - The token for REST API. For information about how to create the token, see [Creating an API Only User in N-central](https://www.youtube.com/watch?v=bk2BFIo_Wfw).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![N-able](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/N-able.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch asset info for each device** - Select this option to fetch asset information for each device.
2. **Asset info categories** - Select asset info categories from the dropdown to choose the data categories to fetch for each device. When nothing is selected, then all categories are fetched. This option is only relevant when *Fetch asset info for each device* is selected.
3. **Fetch custom properties for each device** - Select this option to fetch device custom properties. This option is only relevant when *JWT Token* is enabled in [Parameters](/docs/n-able#parameters).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [N-able N-central API](https://documentation.n-able.com/N-central/troubleshooting/Content/kb/Accessing-N-able-N-central-API-functions.htm).

## Supported From Version

Supported from Axonius version 4.5