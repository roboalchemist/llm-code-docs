# Source: https://docs.axonius.com/docs/nautobot.md

# Nautobot

Nautobot is a network documentation and automation platform for managing network resources.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Nautobot server.

2. **Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Nautobot](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nautobot.png)

<br />

<br />

Advanced Settings
Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​Advanced Configuration for Adapters.

Prefixes (optional, default: disabled) - Enable fetching network prefixes from the Nautobot IPAM (IP Address Management) module. When enabled, the adapter will fetch network prefix data from the /api/ipam/prefixes endpoint and populate the Networks asset type in Axonius.
To learn more about Adapter Configuration tab advanced settings, see Adapter Advanced Settings.

## APIs

Axonius uses the [Nautobot REST API](https://docs.nautobot.com/projects/core/en/stable/user-guide/platform-functionality/rest-api/overview/).

## Supported From Version

Supported from Axonius version 6.1