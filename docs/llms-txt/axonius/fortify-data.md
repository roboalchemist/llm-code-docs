# Source: https://docs.axonius.com/docs/fortify-data.md

# FortifyData

FortifyData is a threat exposure management platform for identifying, monitoring, and managing cyber risk.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the FortifyData server.
2. **Portfolio ID** *(optional)* - Enter a Portfolio ID, so that the adapter will fetch devices from all the companies under the portfolio.
3. **Company ID** *(optional)*  - Enter  the Company ID  of the specific company from which  you want to receive data.

<Callout icon="📘" theme="info">
  Note

  You must supply either a **Portfolio ID** or a **Company ID**.
</Callout>

5. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.
   To generate an API Key, see [FortifyData API Reference](https://api.fortifydata.com/).

6. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

7. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

8. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

9. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

10. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="FortifyData" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FortifyData.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

**Fetch vulnerabilities**  -  Select this option to fetch vulnerabilities.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [FortifyData API](https://api.fortifydata.com/).

## Supported From Version

Supported from Axonius version 4.7