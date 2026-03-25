# Source: https://docs.axonius.com/docs/armis.md

# Armis

Armis is an agentless device security platform to see and protect unmanaged and IoT devices.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications

## Parameters

1. **Armis Domain** *(required)* - The hostname or IP address of the Armis server.
2. **API Key** *(required)* - An API key associated with a user account that has permissions to fetch assets.
3. **Verify SSL** - Select to verify the SSL certificate offered by the value supplied in **Armis Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **Custom Query Suffix** *(optional)* - Specify a custom query suffix to append to the Artifactory Query Language (AQL) that the adapter processes. If left blank, the AQL defaults to: 'in:devices timeFrame:"`{days_ago}` days"'
5. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Armis Domain**.
6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Armis Domain** via the value supplied in **HTTPS Proxy**.
7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the value supplied in **Armis Domain** via the value supplied in **HTTPS Proxy**.

For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="armis" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-UP5WXEQB.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Armis tags include list** *(optional)* - Specify a comma-separated list of Armis tags.
   * If supplied, all connections for this adapter will only fetch devices tagged in Armis with the tags provided in this list.
   * If not supplied, the connection for this adapter will fetch all devices from Armis.
2. **Do not trust hostname data** *(required, default: true)*
   * If enabled, all connections for this adapter won't fetch the hostname from Armis.
   * If disabled, all connections for this adapter will fetch the hostname from Armis.
3. **Do not fetch devices without MAC address** *(required, default: true)* -  Select this option to exclude fetching devices without a MAC address.
4. **Gather last seen from approved data sources** *(optional)* - Enter one or more comma-separated values to gather the Last Seen value from. If not specified, Last Seen is gathered directly from the device attributes. If multiple last-seen values are present among the approved data sources, the most recent value is used.
5. **Number of parallel requests** *(required, default: 10)* - When operating asynchronously, specify the number of simultaneous API calls.
6. **Device Categories to Exclude from Fetch** *(optional)* - Enter one or more comma-separated device categories to exclude from the fetch.
7. **Exclude Devices With No OS** - Select to exclude devices that have an empty **OS Type** field.
8. **Fetch vulnerabilities** - Select to enable vulnerability fetch (fetched as Aggregated Security Findings).

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>