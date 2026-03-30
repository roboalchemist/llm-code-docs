# Source: https://docs.axonius.com/docs/nagios-xi.md

# Nagios XI

Nagios XI provides enterprise server and network monitoring.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Nagios XI URL** *(required)* - The URL of the Nagios XI server that Axonius can communicate with via the [Required Ports](#required-ports). The format of the **Nagios XI URL** should begin with http\:// or https\:// and the port of their Nagios XI server (if it is not a default port). Do not enter the 'nagiosxi' suffix from the url to this field.
2. **API Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets. The API Key is available in the account information page in Nagios.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).
   * When enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** is verified against the CA database inside of Axonius. When the SSL certificate can not be validated against the CA database inside Axonius, the connection fails with an error.
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
7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

![NagiosXI.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NagiosXI\(1\).png)

## Required Ports

Axonius must be able to communicate with the value supplied in [API Key](#parameters) via the following ports:

* **TCP port 80/443**

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have 'Enable API Access' permissions to fetch assets, and have access to read hosts and services.

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| Nagios XI 5 and higher | Yes       |       |

## Supported From Version

Supported from Axonius version 4.4