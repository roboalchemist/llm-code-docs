# Source: https://docs.axonius.com/docs/rapid7-insightidr.md

# Rapid7 InsightIDR

Rapid7’s InsightIDR is a security center for incident detection and response, authentication monitoring, and endpoint visibility.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Alerts/Incidents

## Parameters

1. **Domain** *(required)* - The Domain of the Rapid7 InsightIDR server. The Domains are defined in the [Rapid7 InisghtIDR API](https://docs.rapid7.com/insight/product-apis/#section-supported-regions) according to your country code in the format of  ​https\://\<REGION\_CODE>.api.insight.rapid7.com.

2. **API Key** *(required)* - An API Key associated that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Domain**. For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Domain**.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Domain** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Domain** via the value supplied in **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="IDR" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-9I6ZQYVU.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Ignore stale assets** *(optional)* - Select to not fetch assets with an Agent Status of "Stale" into Axonius. A stale agent has not seen its status in at least 15 days.
2. **Ignore offline assets** *(optional)* - Select to not fetch assets with an Agent Status of "Offline" into Axonius. An offline agent has sent its status within the last 15 days but not in the last 10 minutes.
3. **Ignore public IPs** *(default: false)* - By default Axonius parses the public IP addresses. Select this option to ignore Public IP addresses.
4. **Ignore assets with no hostname** *(default: false)* - Select to avoid fetching devices with no hostmae.
5. **GraphQL page size** *(required, default: 200)* - Specify the number of entities returned per page request. The minimum value is 1; the maximum value is 200.
6. **Use agent data last update time as last seen** - Select whether to use the agent data last update time for the **Last Seen** parameter.
7. **Use FQDN as Host Name** - Select whether to use the FQDN as a Host Name for devices.
8. **Fetch alerts from Investigations** - Select to fetch security alerts from Rapid7 InsightIDR investigations, in addition to standard device data. They will be fetched as Alerts/Incidents assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [InsightIDR REST API](https://docs.rapid7.com/insightidr/insightidr-rest-api/).

## Required Permissions

The value supplied in [API Key](#parameters) must be associated with an Organization API key that has permissions to fetch assets.