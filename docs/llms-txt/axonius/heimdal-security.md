# Source: https://docs.axonius.com/docs/heimdal-security.md

# Heimdal Security

Heimdal Security protects organizations and home users against malware attacks.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Heimdal Security server that Axonius can communicate with via the [Required Ports](#required-ports).
2. **Customer ID**  *(required)* - The customer ID.
3. **Personal API Key** *(required)* - An API Key associated with a user account that has Permissions to fetch assets.
4. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * When enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is verified against the CA database inside of Axonius. When the SSL certificate can not be validated against the CA database inside  Axonius, the connection fails with an error.
   * When disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is not verified against the CA database inside Axonius.
5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * When supplied, Axonius uses the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * When not supplied, Axonius connects directly to the value supplied in **Host Name or IP Address**.
6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.
8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![HeimdalSecurity.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HeimdalSecurity.png)

## APIs

Axonius uses the [Heimdal Security APIs](https://support.heimdalsecurity.com/hc/en-us/articles/360001462138-Heimdal-Security-APIs), 'New API'.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 4.4