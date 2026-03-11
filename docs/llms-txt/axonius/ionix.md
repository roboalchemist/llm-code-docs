# Source: https://docs.axonius.com/docs/ionix.md

# IONIX (formerly Cyberpion)

IONIX (formerly Cyberpion) is a SaaS-based external attack surface management solution.

### Asset Types Fetched

* Vulnerabilities, SaaS Applications, Domains & URLs, Application Services

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the following API endpoints:

* Domains - root endpoint for devices: /api/v1/remediation/action-items/open/
* Asset risk: /api/v1/discovery/org-assets/export-discovery-evidence
* Vulnerabilities: /api/v1/remediation/action-items/all/detailed
* Discovery date: /api/v1/discovery/org-assets (used mostly to get first\_seen)
* Tests - /api/v1/tests

### Permissions

Consult with your vendor for permissions for the exact permissions to fetch the objects.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - Enter `https://api.portal.ionix.io` for the hostname or IP address of the IONIX server.

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets.

<Image alt="IONIX" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/IONIX.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch URLs from Org Assets Endpoint** *(default: enabled)* - Enable this option to fetch URLs from the Org Assets endpoint. When this setting is enabled, the settings below may be configured.
   * **Org Asset Types** *(default: Domain, Sub Domain, Managed Domain)* - From the dropdown, select one or more org asset types.
   * **Enrich Org Assets Endpoint with Discovery Evidence Endpoint**
   * **Enrich Org Assets Endpoint with Action Items Endpoint**
   * **Enrich Org Assets Endpoint with Tests Endpoint**
2. **Fetch ApplicationServices from Cloud Assets Endpoint** *(default: enabled)* - Enable this option to fetch application services from the Cloud Assets endpoint. When this setting is enabled, the settings below may be configured.
   * **Enrich Cloud Assets Endpoint with Cloud Asset Details Endpoint** -  When this setting is enabled, the setting below may be configured.
     * **Cloud Asset Types** - From the dropdown, select one or more cloud asset types.
   * **Enrich Cloud Assets Endpoint with Discovery Evidence Endpoint**
   * **Enrich Cloud Assets Endpoint with Action Items Endpoint**
   * **Enrich Cloud Assets Endpoint with Tests Endpoint**

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>