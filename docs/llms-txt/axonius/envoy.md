# Source: https://docs.axonius.com/docs/envoy.md

# Envoy

Envoy is a unified workplace platform that manages various aspects of physical workspaces.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.envoy.com`)* - The hostname or IP address of the Envoy server.

2. **Authentication Flow** - Select the authentication flow, either **Private App API key Flow** or **Private App Oauth2 Flow**. For more information, see [Get a token for private apps](https://developers.envoy.com/hub/docs/getting-an-access-and-refresh).
   **Private App API key Flow**:

   * **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

   **Private App Oauth2 Flow**:

   * **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
   * **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Envoy](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Envoy.png)

## APIs

Axonius uses the [Envoy API](https://developers.envoy.com/hub/reference/employees-1).

## Required Permissions

The following permissions are required in order to fetch assets:

SCOPE: token.refresh,employees.read,locations.read

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version  | Supported | Notes      |
| -------- | --------- | ---------- |
| Envoy v1 | Yes       | --         |
| Envoy v3 | No        | Deprecated |

## Supported From Version

Supported from Axonius version 6.1.34.0