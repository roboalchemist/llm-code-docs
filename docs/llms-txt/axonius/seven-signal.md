# Source: https://docs.axonius.com/docs/seven-signal.md

# 7SIGNAL Mobile Eye

7SIGNAL Mobile Eye is a Wi-Fi performance management and monitoring SaaS application that helps enterprises optimize wireless device connectivity.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the 7SIGNAL Mobile Eye server.

2. **API Client ID** and  **API Client Secret** *(required)* - **API Client ID** and   **API Client Secret** associated with a user account that has permissions to fetch assets. Refer to [7SIGNAL API ](https://www.7signal.com/info/api) for details of how to obtain them.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![7SignalMobileEye](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/7SignalMobileEye.png)

## APIs

Axonius uses the [7SIGNAL API](https://www.7signal.com/info/api).

## Supported From Version

Supported from Axonius version 4.8