# Source: https://docs.axonius.com/docs/perimeter81.md

# Perimeter 81

Perimeter 81 is a cloud-based secure access service edge (SASE) platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Perimeter 81 server.

2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. For information on how to generate an API Key, see [Getting Started](https://support.perimeter81.com/docs/api-getting-started)(Authentication and Authorization section).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Perimeter%2081](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Perimeter%2081.png)

## APIs

Axonius uses the [Perimeter 81 API](https://support.perimeter81.com/docs/api-getting-started).

## Required Permissions

In order to access the Perimeter 81 API, the user must belong to either the Premium Plus or Enterprise plan.

## Supported From Version

Supported from Axonius version 6.0