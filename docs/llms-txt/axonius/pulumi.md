# Source: https://docs.axonius.com/docs/pulumi.md

# Pulumi Cloud Engineering Platform

Pulumi provides an Infrastructure as Code solution for Developers and Infrastructure Teams, enabling them to build, deploy, and manage cloud applications and infrastructure using various languages, tools, and engineering practices.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Users

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Pulumi server.

2. **API Token** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** *(required, default: false)* - Select to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **Organization** *(optional, default: empty)* - Specify the name of the organization.

5. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * When supplied, Axonius uses the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * When not supplied, Axonius connects directly to the value supplied in **Host Name or IP Address**.

6. **HTTPS Proxy User Name** *(optional, default: empty)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional, default: empty)* - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
   * When supplied, Axonius authenticates with this value when connecting to the value supplied in **HTTPS Proxy**.
   * When not supplied, Axonius does not perform authentication when connecting to the value supplied in **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Pulumi" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Pulumi.png" />

## APIs

Axonius uses the [Pulumi API](https://www.pulumi.com/docs/reference/service-rest-api/#list-users).

## Supported From Version

Supported from Axonius version 4.5