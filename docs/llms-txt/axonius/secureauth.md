# Source: https://docs.axonius.com/docs/secureauth.md

# SecureAuth

SecureAuth is an identity access management security solution that provides passwordless authentication, multi-factor authentication, SSO, and more.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SecureAuth server.

2. **Application ID** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Application Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SecureAuth" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SecureAuth.png" />

## APIs

Axonius uses the [Identity Management API](https://docs.secureauth.com/2104/en/identity-management-api-guide.html).

## Required Permissions

The value supplied in [Application Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.6