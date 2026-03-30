# Source: https://docs.axonius.com/docs/extreme-networks-extremewireless-wing.md

# Extreme Networks ExtremeWireless WiNG

Extreme Networks ExtremeWireless WiNG is a WLAN operating system designed to scale efficiently from the smallest networks to large, geographically dispersed deployments.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Extreme Networks ExtremeWireless WiNG server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the required permissions to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
5. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
6. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * If supplied, Axonius will authenticate with this value when connecting to the value supplied in **HTTPS Proxy**.
   * If not supplied, Axonius will not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1226\).png)

## APIs

Axonius uses the following Extreme Networks ExtremeWireless WiNG REST APIs:

* [Release 5.9.3](https://documentation.extremenetworks.com/WiNG/5.9.3/9035701_WiNG_5_9_3_REST_API_GettingStartedGuide.pdf)
* [Release 7.1](https://documentation.extremenetworks.com/WiNG/7.1/REST_API/GUID-71A6D962-BDCA-4B12-A22D-44032AA0B42C.shtml)

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version                                                             | Supported | Notes |
| ------------------------------------------------------------------- | --------- | ----- |
| Extreme Networks ExtremeWireless WiNG (5.x series) 5.9.2 and higher | Yes       |       |
| Extreme Networks ExtremeWireless WiNG (7.x series) 7.1 and higher   | Yes       |       |