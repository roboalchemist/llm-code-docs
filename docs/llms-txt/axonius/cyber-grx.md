# Source: https://docs.axonius.com/docs/cyber-grx.md

# Global Risk Exchange

The Global Risk Exchange (formerly CyberGRX) is a collaborative risk exchange platform for managing third-party cyber risk assessments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Domain** *(required)* - The hostname or IP address of the Global Risk Exchange server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets. **The Client ID and Client Secret are used to generate a JWT token.**

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Global Risk Exchange](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Global%20Risk%20Exchange.png)

## APIs

Axonius uses the [CyberGRX API](https://api.cybergrx.com/).

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must be associated with credentials that have scope read:portfolio permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1