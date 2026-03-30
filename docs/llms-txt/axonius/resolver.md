# Source: https://docs.axonius.com/docs/resolver.md

# Resolver

Resolver is a risk management and incident response platform that provides risk assessment, incident tracking, and reporting tools for businesses.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users
* Roles
* Groups

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Resolver server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For more details, see [API Keys](https://help.resolver.com/help/api-keys).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Resolver](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Resolver.png)

## APIs

Axonius uses the [Resolver Core API](https://help.resolver.com/help/api-keys).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have admin or super-admin permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1