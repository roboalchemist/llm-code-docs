# Source: https://docs.axonius.com/docs/onetouch-io.md

# 1touch.io

1touch.io is a data discovery platform for identifying sensitive data flows and ensuring compliance.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the 1touch.io server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Residency** *(required)* - The geo distribution of data subjects discovered.

4. **URL Part** *(required)* - The string to connect to the data source.

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

6. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

7. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

8. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![1touch.io](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/1touch.io.png)

## Supported From Version

Supported from Axonius version 6.1