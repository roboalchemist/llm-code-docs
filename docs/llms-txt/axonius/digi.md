# Source: https://docs.axonius.com/docs/digi.md

# Digi

Digi provides IoT solutions including hardware, software, and services for connecting and managing IoT devices and networks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Digi server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Digi](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Digi.png)

## APIs

Axonius uses the [Digi Remote Manager API](https://doc-remotemanager.digi.com/api/v1/).

## Supported From Version

Supported from Axonius version 6.1