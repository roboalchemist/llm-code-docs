# Source: https://docs.axonius.com/docs/fireeye-endpoint-security-formerly-hx.md

# Trellix Endpoint Security (HX)

Trellix Endpoint Security (HX) detects and protects against unknown endpoint threats and exploits with integrated threat intelligence.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Networks

## Parameters

1. **Trellix Endpoint Security Domain** *(required)* - The hostname or IP Address of the Trellix Endpoint Security management server.
2. **Port** *(optional, default: 3000)* - The port used for the connection.
3. **User Name** and **Password** *(required)* - To submit API requests to Trellix Endpoint Security from Axonius, you need a valid user account on Trellix Endpoint Security associated with the *api\_admin* or *api\_analyst* role.

<Callout icon="📘" theme="info">
  Note

  For more details on creating a user account, see the "Trellix Endpoint Security System Administration Guide" in the Trellix Documentation Portal.
  For more details on the user roles, see the "HX Series REST API Guide".
</Callout>

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="fireeye endpoint.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/fireeye%20endpoint.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Avoid AWS duplications** - Select this option to avoid returning duplicate AWS machines when using the scroll API.
2. **Fetch Network Assets** - Select this option to fetch network assets.
3. **Enrich Devices with SysInfo** - Select this option to enrich devices with sysinfo data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>