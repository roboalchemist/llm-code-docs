# Source: https://docs.axonius.com/docs/uptycs.md

# Uptycs

Uptycs is an osquery-powered security analytics platform pairs a universal agent with analytics for fleet visibility, intrusion detection, incident investigation, vulnerability management & compliance for Linux, macOS, Windows, containers, and cloud workloads.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Uptycs server.

2. **Customer ID** *(required)* - The customer ID obtained from Uptycs portal.

3. **API Key** and **API Secret** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![image.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image\(1369\).png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Page size** *(default: 200)* - Enter a value for the page size for API pagination.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [API Key and API Secret](#parameters) must be associated with credentials that have read access to devices.

API Key and API Secret can be obtained from the company's Uptycs administrator. A user with administrator privileges can generate a key and secret for other users.