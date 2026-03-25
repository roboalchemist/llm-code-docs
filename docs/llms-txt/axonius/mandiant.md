# Source: https://docs.axonius.com/docs/mandiant.md

# Mandiant

Mandiant Advantage is a multi-vendor XDR platform that delivers Mandiant’s transformative expertise and frontline intelligence to security teams of all sizes.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications
* Domains & URLs

## Parameters

1. **Access Key** and **Secret Key** *(required)* - An API Key associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

2. **Project ID** *(optional)* - The Project ID of the account to fetch.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Mandiant" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Mandiant.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch vulnerabilities** *(default: true)* - Select this option to enrich the devices with ‘vulnerabilities’ data associated with the device. When this option is disabled, ‘vulnerabilities’ data for each device is not parsed and doesn't appear in the device's raw data.
2. **Fetch issues data** - Select this option to enrich the devices with ‘issues’ data associated with the device.
3. **Fetch technologies data** - Select this option to enrich the devices with ‘technologies’ data associated with the device.
4. **Fetch entities last seen in X days** *(required, default: 365 days)* - Fetch entities last seen by the number of days specified.
5. **Fetch only active entities** - Select this option to use `last_seen_after:configured_scan_count` query to fetch only active entities.
6. **Fetch entities details enrichment** - Select this option to add more details to the information fetched per each entity.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the Asm-api.yml API.

## Required Permissions

The values supplied in [**Access Key** and **Secret Key**](#parameters) must be associated with credentials that have Read permissions in order to fetch assets.

## Supported From Version

Supported from Axonius version 4.8