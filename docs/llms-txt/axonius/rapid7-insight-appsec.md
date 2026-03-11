# Source: https://docs.axonius.com/docs/rapid7-insight-appsec.md

# Rapid7 Insight AppSec

Rapid7 Insight AppSec performs black-box security testing to identify vulnerabilities, triage vulnerabilities, prioritize actions, and remediate application risk.

## Asset Types Fetched

* Devices, Aggregated Security Findings, Business Applications, SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - This is the URL of the Rapid7 Insight AppSec server. The format of the URL contains the region your Rapid7 Insight instance is hosted, followed by the Rapid7 Insight domain. Lastly, a suffix containing the product abbreviation and API version is required to fetch data.

For an example, where the Rapid7 Insight instance is hosted in the US-1 region, the URL would be [https://us.api.insight.rapid7.com/ias/v1](https://us.api.insight.rapid7.com/ias/v1).

More information about the Rapid7 Supported Regions is available here:[https://docs.rapid7.com/insight/product-apis/#supported-regions](https://docs.rapid7.com/insight/product-apis/#supported-regions)

2. **API Key** *(required)* - An API Key associated with a user account that has permissions to fetch assets. For information about how to create an API Key, see [Managing Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys/).

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Rapid7 InsightAppSec" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Rapid7%20InsightAppSec.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config

1. **Fetch BusinessApplications from Apps** - Enable to fetch Apps as Business Applications asset type.
   1. **Enrich Apps with Scans** - Enable to fetch the asset’s Last Scan information, parsed into the following fields:
      * Last Scan: Submit time
      * Last Scan: Completion time
      * Last Scan: Duration (Completion Time - Submit Time)
      * Last Scan: Status
2. **Fetch Devices from Devices** - Enable to fetch Devices from the Devices endpoint.
   1. **Enrich Devices with Scans** - See explanation above.

<br />

## APIs

Axonius uses the [InsightAppSec API (v1)](https://help.rapid7.com/insightappsec/en-us/api/v1/docs.html#tag/Vulnerabilities/operation/get-vulnerabilities).

## Supported From Version

Supported from Axonius version 6.1