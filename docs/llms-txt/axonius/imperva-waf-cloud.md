# Source: https://docs.axonius.com/docs/imperva-waf-cloud.md

# Imperva WAF Cloud

Imperva Web Application Firewall (WAF) Cloud allows customers to monitor, filter, and block incoming and outgoing data packets from a web application or website.

The Imperva WAF Cloud adapter enables Axonius to fetch and catalog web application security assets, including sites, policies, and security incidents, ensuring comprehensive visibility into application protection and compliance.

## Asset Types Fetched

* Devices
* Domains and URLs
* Network/Firewall Rules
* Alerts/Incidents

## Before You Begin

### Required Ports

* TCP port 443

### Required Permissions

The user account associated with the API Key must have read permissions to the account or sub-accounts that you want to fetch.

### APIs

Axonius uses the <Anchor label="Imperva Cloud Application Security v1/v3 API" target="_blank" href="https://docs.imperva.com/bundle/cloud-application-security/page/cloud-v1-api-definition.htm">Imperva Cloud Application Security v1/v3 API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 4.8.

## Connection Parameters

### Required Parameters

1. **Host Name or IP Address** *(default: `https://my.imperva.com`)* - Enter the hostname or IP Address of the Imperva WAF Cloud server.

2. **API ID** - Enter the credentials for a user account that has the permissions to fetch assets.

3. **API Key** - Enter an API key associated with a user account that has permissions to fetch assets. Refer to [Imperva API Key Management](https://docs.imperva.com/bundle/cloud-application-security/page/settings/api-keys.htm#CreateandmanageAPIkeys) for information on how to get the API key.

<Image align="center" alt="Imperva WAF Cloud adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Imperva_WAF_Cloud_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

In **Advanced Configuration**, expand **Endpoints Config** to access the following advanced settings:

* **Fetch Devices from Sites** - Enable to fetch sites as device assets.
  * **Enrich Sites with Data Centers** *(default: true; under Fetch Devices from Sites)* - Enable (default) to enrich site **devices** with data centers information.
  * **Enrich Sites with Asset Policies** *(default: true; under Fetch Devices from Sites)* - Enable to enrich site **devices** with policies.
  * **Enrich Sites with APIs** *(under Fetch Devices from Sites)* - Enable to enrich site **devices** with APIs and API endpoints.
  * **Enrich Sites with Domains** - Enable this to enrich Site devices with Domains & URLs data.
* **Fetch Firewall from Policies** - Enable to fetch network/firewall rules assets from policies.

  <Callout icon="💡" theme="warn">
    **For Exposures customers only:**

    The data received by enabling **Fetch Firewall from Policies** can be used and analyzed in the [External Exposures](https://docs.axonius.com/axonius-help-docs/docs/external-exposures) module.
  </Callout>
* **Fetch URLs from Sites** - Enable to fetch URLs configured on the sites.
  * **Enrich Sites with Data Centers** *(under Fetch URLs from Sites)* - Enable to enrich the **fetched URL** assets with the parent site's data center information.
  * **Enrich Sites with Asset Policies** *(under Fetch URLs from Sites)* - Enable to enrich the **fetched URL** assets with the parent site's asset policies.
  * **Enrich Sites with APIs** *(under Fetch URLs from Sites)* - Enable to enrich the **fetched URL** assets with the parent site's APIs and API endpoints.
* **Fetch Incidents from Insights** - Enable to fetch security incidents from Imperva Insights.