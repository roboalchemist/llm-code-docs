# Source: https://docs.axonius.com/docs/kenna-security-platform.md

# Kenna Security Platform

Kenna Security Platform is a vulnerability assessment solution that provides risk scoring, prioritization, and benchmarking.

**Related Enforcement Actions**

* [Kenna - Add Tags to Assets](/docs/add-kenna-tags)
* [Kenna - Remove Tags from Assets](/docs/remove-kenna-tags)
* [Kenna - Replace Tag in Assets](/docs/replace-kenna-tag)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* Software
* SaaS Applications

## Parameters

1. **Kenna Security Platform URL** *(required, default: `https://api.kennasecurity.com`)* - The URL for the Kenna Security Platform admin panel.

2. **API Token** *(required)*  – Specify your account API key or an API token you have created.

3. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Kenna Security Platform URL**. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

7. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image align="center" alt="Kenna" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Kenna.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Use export API** - Select whether to use the data\_export endpoint.
   * If enabled, all connections for this adapter will fetch data from the data\_export endpoint. This setting enables fetching more than 10,000 assets.
   * If disabled, all connections for this adapter will fetch data from the assets, vulnerabilities and fixes endpoints. Those endpoints are limited to 10,000 assets (results).
2. **Export full data** *(default false)* - Select this option to fetch additional  Vulnerability date fields from Kenna in order to display them in charts. You need to select **Use export API** in order to select this option.
3. **Fetch device vulnerabilities and fixes** - Select whether to fetch vulnerability and fixes information for devices. Otherwise, only device information is fetched.
4. **Skip fixes when fetching vulnerabilities** - Select whether to skip fix data when fetching vulnerabilities. Note that the **Fetch device vulnerabilities and fixes** setting needs to be enabled if you select this.
5. **Do not fetch devices with no MAC address, no hostname and no NetBIOS** - Select whether to exclude fetching devices without a MAC address and without a hostname and without NetBIOS.
6. **Do not ingest heavy fields** - Select this option to not parse the "Open Ports Vulnerabilities: Vulnerability Solution" field.
7. **Severity level to fetch** - Select which severity level to fetch from 1 to 10.
8. **Fetch CVE Enrichments from Kenna VI+** Select to enrich Vulnerability Instances with data from Kenna Vulnerability Intelligence+.
9. **Do not fetch devices with no MAC address and no hostname** - Select whether to exclude fetching devices without a MAC address and without a hostname.

## APIs

Axonius uses the [Kenna Security Platform API](https://apidocs.kennasecurity.com/reference#list-assets).

Locate and change your API token by logging in and clicking your company's name in the upper right-hand corner. From the dropdown, select **API Keys**. Your API token is the first listing in the table located in the Applications page.

## Required Ports

Axonius must be able to communicate with the value supplied in [API Token](#parameters) via the following ports:

* **HTTPS port 443**