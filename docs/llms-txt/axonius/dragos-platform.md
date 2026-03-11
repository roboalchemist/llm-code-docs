# Source: https://docs.axonius.com/docs/dragos-platform.md

# Dragos Platform

The Dragos Platform identifies ICS network assets, malicious activity, and provides guidance to investigate incidents.

**Related Enforcement Actions:**

* [Update Assets - Dragos Platform](https://docs.axonius.com/docs/update-dragos-platform-asset)

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Aggregated Security Findings
* SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required)* - The Host Name or IP Address of the Dragos Platform server.

2. **API ID** and **API Secret** *(required)* - An API for a user account that has the permissions to fetch assets. Refer to Dragos SiteStore API guide for Details of how to create these credentials.

3. **API Version** *(optional, default: v3)*  - Select the API version, either v3 or v4.

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="Dragos.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Dragos.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Parallel Requests Count** *(required, default: 5)* - Specify the maximum number of parallel requests all connections for this adapter will create when connecting to the value supplied in Dragos Host Name or IP Address.
2. **Fetch internal devices only** - Select to only fetch devices where the internal flag is set to 'True'. Devices with a public IP address will not be fetched.
3. **Fetch Vulnerabilities** - When checked, the adapter will also fetch vulnerabilities. This requires "VulnerabilityDetectionRead" privilege from the API users

<Callout icon="📘" theme="info">
  Note

  For details about general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>