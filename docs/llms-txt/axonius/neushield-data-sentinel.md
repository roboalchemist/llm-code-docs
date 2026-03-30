# Source: https://docs.axonius.com/docs/neushield-data-sentinel.md

# NeuShield Data Sentinel

NeuShield Data Sentinel is a data protection tool that offers ransomware defense and data recovery capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Accounts/Tenants

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the NeuShield server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Refresh Token** *(required)* - Refresh token used by the client application to refresh the access token before it expires. For more information, see the NeuShield Data APIs documentation.

4. **Redirect URL** *(optional)* -  The URL-encoded redirect URL of the client application.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![NeuShield](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NeuShield.png)

## APIs

Axonius uses the NeuShield Data APIs.

## Required Permissions

The value supplied in [Client ID and Client Secret](#parameters) must be associated with credentials that have Data API permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 6.1.38.2