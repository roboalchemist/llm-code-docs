# Source: https://docs.axonius.com/docs/intel-471-enrichment.md

# Intel 471 Enrichment

Intel 471 Enrichment provides cyber threat intelligence to assess, identify, and manage potential risks.

<Callout icon="📘" theme="info">
  Note

  This adapter was previously called **Intel 471**.
</Callout>

## Types of Assets Fetched

This adapter fetches vulnerabilities and enriches them with CVE information.

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Intel 471 server that Axonius can communicate with.
2. **Email Address** *(required)* - An email address associated with a user account that has permissions to fetch assets.
3. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Intel471 Add Connection(1)](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Intel471%20Add%20Connection\(1\).png)

## APIs

Axonius uses the [Intel 471 API](https://titan.intel471.com/api/docs-openapi/).

## Supported From Version

Supported from Axonius version 6.1