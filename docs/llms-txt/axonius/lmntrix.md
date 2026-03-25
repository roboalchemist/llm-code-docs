# Source: https://docs.axonius.com/docs/lmntrix.md

# LMNTRIX

LMNTRIX offers a security-as-a-service platform that provides threat detection and response capabilities.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the LMNTRIX server.
2. **Company ID** - *(required)*  You can generate the Company ID from the LMNTRIX dashboard.
3. **API Token** *(required)* - An API Token associated with the user account you want to use to fetch assets.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![lmntrix add connection](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/lmntrix%20add%20connection.png)

## APIs

Axonius uses the LMNTRIX API.

## Supported From Version

Supported from Axonius version 6.1