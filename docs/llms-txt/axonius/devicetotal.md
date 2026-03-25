# Source: https://docs.axonius.com/docs/devicetotal.md

# DeviceTotal

DeviceTotal is an agentless attack surface management solution.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.devicetotal.com`)* - The hostname or IP address of the DeviceTotal server.

2. **Customer ID** *(required)* - The customer ID for a user account provided by DeviceTotal that has the permissions to fetch assets.

3. **Access Token** *(required)* -An Access Token associated with a user account that has permissions to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![DeviceTotal](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeviceTotal.png)

## APIs

Axonius uses the [DeviceTotal API](https://api.devicetotal.com/docs).

## Supported From Version

Supported from Axonius version 6.1