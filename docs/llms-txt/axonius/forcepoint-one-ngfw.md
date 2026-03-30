# Source: https://docs.axonius.com/docs/forcepoint-one-ngfw.md

# Forcepoint NGFW

Forcepoint NGFW is a next-generation firewall that provides advanced security features, including intrusion prevention, VPN, and centralized management to protect network environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Forcepoint NGFW server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Logging on](https://help.forcepoint.com/ngfw/en-us/7.0.0/smc_api_ug/GUID-8714C596-508C-4EF0-9ECC-3A265EC456AD.html).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Forcepoint NGFW.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Forcepoint%20NGFW.png)

## APIs

Axonius uses the [Forcepoint NGFW SMC API](https://help.forcepoint.com/ngfw/en-us/7.0.0/smc_api_ug/GUID-A37610B6-91C0-4FB4-9CD4-1F1EB0DBE474.html).

## Supported From Version

Supported from Axonius version 6.1.39