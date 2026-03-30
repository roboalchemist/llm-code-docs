# Source: https://docs.axonius.com/docs/site24x7.md

# Site24x7

Site24x7 offers a performance monitoring solution for websites, servers, cloud environments, networks, applications, and users.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Domains & URLs

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Site24x7 server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account for which the **Refresh Token** has the [Required Permissions](#required-permissions) to fetch assets.

3. **Refresh Token** *(required)* - The token used for the connection.
   To generate the Client ID, Client Secret, and Refresh Token, see [Site24x7 Authentication (Parts 1-3)](https://www.site24x7.com/help/api/#authentication)

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Site24x7](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Site24x7.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Asset types to fetch** *(default: Server, Network Device)* - From the dropdown, select which asset types to fetch.
2. **Parse URLs as devices** - Select this option to parse URLs as devices, in addition to being parsed as URLs.
3. **Fetch Tags** - Select this option to fetch and fill monitor tags.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [Site24x7 API](https://www.site24x7.com/help/api/) and the [List of all Tags](https://www.site24x7.com/help/api/#list-of-all-tags) endpoint.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following HTTP/HTTPS ports:

* **80**
* **443**

## Required Permissions

The value supplied in [Client ID](#parameters) must have the  **Site24x7.Admin.Read** permission to fetch assets.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version         | Supported | Notes                                         |
| --------------- | --------- | --------------------------------------------- |
| API version 2.0 | Yes       | Future API versions to be backward compatible |

## Supported From Version

Supported from Axonius version 4.6