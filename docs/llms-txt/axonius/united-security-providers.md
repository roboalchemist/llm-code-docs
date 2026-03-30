# Source: https://docs.axonius.com/docs/united-security-providers.md

# United Security Providers

United Security Providers is a Managed Security Services provider.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the United Security Providers server.

2. **API Token** *(required)* - An API Token associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![United%20Security%20Providers](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/United%20Security%20Providers.png)

## APIs

Axonius uses the USP NAS REST API.

## Required Permissions

A user with the user role ‘REST API’ can create an authentication-token in their user profile page. For more information, refer to the USP NAS REST API documentation.

## Supported From Version

Supported from Axonius version 6.0