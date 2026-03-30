# Source: https://docs.axonius.com/docs/pentera-platform.md

# Pentera

Pentera recons and maps web-facing attack surface assets. This includes domains, web interfaces, IPs, networks, and gateways.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Pentera server.

2. **Client ID** *(required)* - The credentials for a user account that has permission to fetch assets.

3. **TGT** *(required)* - The token from Pentera UI in Administration.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Pentera](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Pentera.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Last Scan Date (in days)** *(optional, default: 90)* - Specify the number of days since the last scan.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Supported From Version

Supported from Axonius version 6.0