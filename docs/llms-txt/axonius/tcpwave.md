# Source: https://docs.axonius.com/docs/tcpwave.md

# TCPWave (IPAM)

TCPWave IPAM allows administrators to manage their DNS and DHCP infrastructure for on-premise and cloud environments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the TCPwave (IPAM) server.

2. **Authentication Token** *(required)* - An Authentication Token associated with a user account that has  permissions to fetch assets.  Generate the token using the [TCPwave API](https://www.tcpwave.com/rest#_authentication_token_management_resource).

3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * When enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is verified against the CA database inside of Axonius. When the SSL certificate can not be validated against the CA database inside  Axonius, the connection fails with an error.
   * When disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is not verified against the CA database inside Axonius.

4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * When supplied, Axonius uses the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * When not supplied, Axonius connects directly to the value supplied in **Host Name or IP Address**.

5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![TCPWave.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TCPWave.png)

## APIs

Axonius uses the [TCPWave API](https://www.tcpwave.com/rest).

## Required Ports

* **TCP port 443**

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                          | Supported | Notes |
| -------------------------------- | --------- | ----- |
| TCPWave RestAPI Version: 11.31P7 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.5