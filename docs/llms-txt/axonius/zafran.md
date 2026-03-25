# Source: https://docs.axonius.com/docs/zafran.md

# Zafran

Zafran is a security platform that provides comprehensive attack surface management solutions.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Vulnerability Instances, Vulnerabilities, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://api.zafran.io`)* - The hostname or IP address of the Zafran server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![Zafran](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Zafran.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Devices query** *(optional)* - Enter a valid ZQL query, if applicable.
2. **Enrich Devices with Findings: Vulnerabilities: Download** - Enable this option to enrich devices with vulnerabilities findings.
3. **Enrich Devices with Remediations: Download** - Enable this option to enrich devices with remediations data.
4. **Findings: Vulnerabilities: Status - applies context on the following endpoints: Findings: Vulnerabilities: Download**
   * **Export Timeout** *(optional, default: 120)* - Specify the maximum number of minutes to wait for the Vulnerabilities export to finish before giving up and continuing to the Devices fetch.
5. **Findings: Vulnerabilities: Export - applies context on the following endpoints: Findings: Vulnerabilities: Status**
   * **Findings: Vulnerabilities: Export: Last Days** *(optional, default: 1)* - Specify the number of vulnerabilities reported within the last x days.
   * **Findings: Vulnerabilities: Export: add filter string** *(optional)* - Enter a valid ZQL to filter options in addition to the above last x days.
6. **Remediations: Status - applies context on the following endpoints: Remediations: Download**
   * **Remediations Export Timeout** *(optional, default: 120)* - Specify the maximum number of minutes to wait for the Remediations export to finish before giving up and continuing to the Devices fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Zafran API.

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* **TCP port 443**

## Supported From Version

Supported from Axonius version 6.1.47.0