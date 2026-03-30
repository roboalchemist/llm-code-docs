# Source: https://docs.axonius.com/docs/saner-now.md

# SecPod SanerNow

SecPod SanerNow is an integrated platform that helps businesses secure system devices and monitor potential threats across digital assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the SecPod SanerNow server.

2. **Account ID** and **API Key** *(required)* - Account ID and API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![SecPod%20SanerNow(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SecPod%20SanerNow\(1\).png)

## APIs

Axonius uses the SanerNow Web Services Integration API.

## Required Permissions

The value supplied in [Account ID](#parameters) must be associated with credentials that have super administrator or MSP user permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.0