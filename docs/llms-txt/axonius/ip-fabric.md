# Source: https://docs.axonius.com/docs/ip-fabric.md

# IP Fabric

IP Fabric is a network management system used to discover, verify, visualize and document large scale networks.

## Parameters

1. **IP Fabric Domain** *(required)* - The hostname or IP address of the IP Fabric server that  Axonius can communicate with via the [Required Ports](#required-ports). For example: *[https://ipfabric.axonius.lan](https://ipfabric.axonius.lan)*.
2. **User Name** and **Password** *(optional, preferred option)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. Use either **User Name** and **Password** or **API Key**. Refer to [API Keys](https://docs.ipfabric.io/api/#header-api-keys) for information on obtaining the **API Key**.
3. **API Key** - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. Use either **API Key** or **User Name** and **Password**.
4. **API Version** *(optional)* - Select the version of the IP Fabric API.
5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![IPFabric.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IPFabric.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch assets from hosts table** - Select this option to fetch assets from the hosts table.
2. **Ignore assets without hostname** - Select this option to not fetch devices if they do not have a hostname.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

Ignore assets without hostname - Select this option to not fetch devices if they do not have a hostname

## APIs

Axonius uses [IP Fabric API](https://docs.ipfabric.io/api/).

## Required Ports

Axonius must be able to communicate with the value supplied in [IP Fabric Domain](#parameters) via the following ports:

* 443 (HTTPS)

## Required Permissions

The value supplied in [User Name](#parameters) must have read access to devices.
Every user has their granted scope that allows them to access a different part of the IP Fabric application. The scope required is 'read' that provides access to read-only data.

For more details, see [IP Fabric API - Authorization](https://docs.ipfabric.io/api/#header-authorization).