# Source: https://docs.axonius.com/docs/trend-micro-conformity.md

# Trend Micro Conformity

Trend Micro Conformity provides real-time monitoring, automated security and compliance checks, and auto-remediation for cloud infrastructure.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Trend Micro Conformity server.

2. **API Key** *(required)* and **Password** *(optional)* - The API credentials associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![TrendMicroConformite](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TrendMicroConformite.png)

## APIs

Axonius uses the [Trend Micro Cloud One API](https://cloudone.trendmicro.com/docs/conformity/api-reference).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with credentials that have Read-only permissions to fetch assets.

## Supported From Version

Supported from Axonius version 4.7