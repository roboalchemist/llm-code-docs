# Source: https://docs.axonius.com/docs/dazz.md

# Dazz

Dazz provides automated remediation processes for applications, code, clouds, and infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://app.dazz.io`)* - The hostname or IP address of the Dazz server.

2. **Client ID** and **Client Secret** *(required)* - The credentials for a user account that has permission to fetch assets. For information about how to obtain these credentials, see [My API keys](https://app.dazz.io/auth/docs?redirect=%2Fdocs%2Fmy-api-keys).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Dazz](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dazz.png)

## APIs

Axonius uses the following APIs:

* [Dazz API Start Guide](https://docs.dazz.io/docs/api-start-guide)
* [Dazz API Playground](https://app.dazz.io/playground)

## Supported From Version

Supported from Axonius version 6.1