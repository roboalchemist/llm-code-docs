# Source: https://docs.axonius.com/docs/schneider-electric-ecostruxure.md

# Schneider Electric EcoStruxure IT Advisor

Schneider Electric EcoStruxure IT Advisor is asset and planning software that facilitates OpEx management.

<Callout icon="📘" theme="info">
  Note

  This adapter is for the IT Advisor. To fetch data from Schneider Datacenter see [Schneider Electric EcoStruxure IT](/docs/schneider-electric-ecostruxure-it) adapter.
</Callout>

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Schneider Electric EcoStruxure IT Advisor server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![EcoStruxure IT Advisor](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EcoStruxure%20IT%20Advisor.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices of sub type blades from Blades Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'blades' from the Blades Endpoint. Toggle off to not fetch devices of the subtype 'blades' from the Blades Endpoint.
2. **Fetch Devices of sub type servers from Server Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'servers' from the Server Endpoint. Toggle off to not fetch devices of the subtype 'servers' from the Server Endpoint.
3. **Fetch Devices of sub type blade\_enclosure from Blade Enclosure Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'blade\_enclosure' from the Blade Enclosure Endpoint. Toggle off to not fetch devices of the subtype 'blade\_enclosure' from the Blade Enclosure Endpoint.
4. **Fetch Devices of sub type network from Network Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'network' from the Network Endpoint. Toggle off to not fetch devices of the subtype 'network' from the Network Endpoint.
5. **Fetch Devices of sub type switch\_enclosure from Switch Enclosure Endpoint** *(default: true)* - By default this adapter fetches devices of the subtype 'switch\_enclosure' from the Switch Enclosure Endpoint. Toggle off to not fetch devices of the subtype 'switch\_enclosure' from the Switch Enclosure Endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Schneider Electric EcoStruxure IT Advisor REST Web Service API.

## Supported From Version

Supported from Axonius version 6.1