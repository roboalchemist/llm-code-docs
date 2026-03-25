# Source: https://docs.axonius.com/docs/netspyglass.md

# NetSpyGlass

NetSpyGlass provides real-time network mapping, monitoring, visualization, and analytics for multi-vendor data center and WAN network operators.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NetSpyGlass server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Network ID** *(optional)* - The ID of the network scanned for assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NetSpyGlass](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NetSpyGlass.png)

## APIs

Axonius uses the [NetSpyGlass JSON API](https://docs.netspyglass.com/3.0.x/json_api.html).
To obtain the API token refer to [User Authentication](https://docs.netspyglass.com/2.1.x/authentication.html?highlight=auth). In 2.6.3. Using access tokens for script access to API: ”Access tokens are defined in the configuration file, parameter api.accessTokens”

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443/80**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| NetSpyGlass JSON AP V3 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5