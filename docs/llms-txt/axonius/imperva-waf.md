# Source: https://docs.axonius.com/docs/imperva-waf.md

# Imperva WAF

Imperva Web Application Firewall (WAF) allows customers to monitor, filter, and block incoming and outgoing data packets from a web application or website.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Network/Firewall Rules

## Parameters

1. **Host Name or IP Address** *(required)* - The hostname or IP address of the Imperva WAF server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="ImpervaWAF" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ImpervaWAF.png" />

## Advanced Settings

* **Fetch web application inbound and outbound rules** - Select this option to fetch web application inbound and outbound rules that create a firewall entity.

<Callout icon="📘" theme="info">
  **Note**

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings)
</Callout>

## APIs

Axonius uses the [Imperva WAF API](https://docs.imperva.com/bundle/v14.7-waf-api-reference-guide/page/61914.htm).

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* 8083

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                  | Supported | Notes |
| ------------------------ | --------- | ----- |
| Imperva WAF 13.6.0.88\_0 | Yes       |       |

## Supported From Version

Supported from Axonius version 4.8