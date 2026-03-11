# Source: https://docs.axonius.com/docs/extreme-cloud-iq-site-engine.md

# ExtremeCloud IQ Site Engine

ExtremeCloud IQ Site Engine is an IT operations tool for web-based reporting, network analysis, troubleshooting, and helpdesk.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the ExtremeCloud IQ Site Engine server.

2. **Port** *(required)* - The port used for the connection.

3. **User Name** and **Password** *(required)* - The credentials for a user account that has permission to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ExtremeCloud%20IQ%20Site%20Engine](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ExtremeCloud%20IQ%20Site%20Engine.png)

## APIs

Axonius uses the [ExtremeCloud IQ Site Engine API](https://emc.extremenetworks.com/content/oneview/docs/connect/docs/netsight_device_web_service/ov_connect_netsightdevice_method_getalldevices.htm).

## Supported From Version

Supported from Axonius version 6.0