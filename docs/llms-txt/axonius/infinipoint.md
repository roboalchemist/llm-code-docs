# Source: https://docs.axonius.com/docs/infinipoint.md

# Infinipoint

Infinipoint is a cloud-based automated cyber hygiene platform that enables continuous detection and remediation of risks across the organization’s IT assets.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
  , Aggregated Security Findings
  , Users
  , Software
  , SaaS Applications

## Parameters

1. **Host Name or IP Address** *(required, default: `https://console.infinipoint.io`)* - The hostname or IP address of the Infinipoint server.
2. **API Key** and **API Secret** *(required)* - An API Key associated with a user account that has the required permissions to fetch assets.
3. **Verify SSL** *(required, default: False)* - Verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](../global-settings#ssl-trust-amp-ca-settings).
   * If enabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will be verified against the CA database inside of Axonius. If the SSL certificate can not be validated against the CA database inside of Axonius, the connection will fail with an error.
   * If disabled, the SSL certificate offered by the value supplied in **Host Name or IP Address** will not be verified against the CA database inside of Axonius.
4. **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
   * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Host Name or IP Address**.
   * If not supplied, Axonius will connect directly to the value supplied in **Host Name or IP Address**.
5. For details on the common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="image.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1073).png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

Fetch additional data - Select the additional data you want to fetch from the drop-down (Software, Services, Vulnerabilities)

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>