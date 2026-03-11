# Source: https://docs.axonius.com/docs/cornerstone.md

# Cornerstone

Cornerstone is an AI-powered talent management software that helps businesses to recruit, train, and manage their employees.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Cornerstone server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information about how to generate these credentials, see [Authentication](https://csod.dev/guides/getting-started/authentication.html#register-an-application).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Cornerstone](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Cornerstone.png)

## APIs

Axonius uses the following APIs:

* [Cornerstone API](https://csod.dev/guides/getting-started/)
* [Cornerstone Core and HR APIs](https://csod.dev/reference/core-hr/)

## Required Permissions

One of the following API permissions is required for basic Cornerstone configuration:

* Employee API - View
* Employee API - View - Constrainable

## Supported From Version

Supported from Axonius version 6.1.27.0