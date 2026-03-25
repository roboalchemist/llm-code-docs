# Source: https://docs.axonius.com/docs/actzero.md

# ActZero

ActZero is a managed detection and response (MDR) tool that provides proactive, rapid, and automated services against cyber threats.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Act Zero server.

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![ActZero](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActZero.png)

## APIs

Axonius uses the [ActZero API](https://api.actzero.ai/api-docs/index.html#).

## Supported From Version

Supported from Axonius version 6.1.30.0