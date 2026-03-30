# Source: https://docs.axonius.com/docs/cyera.md

# Cyera

Cyera is a data security platform that provides comprehensive data protection and governance solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Databases
* Object Storage

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.cyera.io`)* - The hostname or IP address of the Cyera server that Axonius can communicate with via the [Required Ports](#required-ports). From the dropdown, choose the appropriate API server according to your location.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has  permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cyera.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cyera.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Devices from Devices Endpoint** *(default: true)* - By default this adapter fetches devices from the Devices Endpoint. Toggle off to not fetch devices from the Devices Endpoint.
2. **Fetch Devices Last Seen in X Days** *(optional, default: 15)* - Fetch devices last seen by the number of days specified.
3. **Fetch Databases from Databases Endpoint** *(default: true)* - By default this adapter fetches databases from the Databases Endpoint. Toggle off to not fetch databases from the Databases Endpoint.
4. **Fetch Databases Last Seen in X Days** *(optional, default: 15)* - Fetch databases last seen by the number of days specified.
5. **Fetch ObjectStorage from Object Storage Endpoint** *(default: true)* - By default this adapter fetches object storage from the Object Storage Endpoint. Toggle off to not fetch object storage from the Object Storage Endpoint.
6. **Fetch Object Storages Last Seen in X Days** *(optional, default: 15)* - Fetch object storages last seen by the number of days specified.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Cyera API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.57.0