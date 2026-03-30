# Source: https://docs.axonius.com/docs/bastazo.md

# Bastazo

Bastazo is a security platform that offers comprehensive attack surface management solutions.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### Permissions

READ access permissions are required to the following endpoints:

* `/spartan/api/assets/cyber_asset/applicable_vulnerabilities/summary`

* `/spartan/api/adversaries/`

#### Supported From Version

Supported from Axonius version 6.1.67

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Bastazo server.
2. **API Key**  - An API Key associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Bastazo.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bastazo.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Enrich Assets Summary with Adversaries (available only for customers who purchased Exposures)** - Enable this option to enrich CVE information. Refer to [Vulnerability Enrichment](/docs/vulnerability-enrichment) for more information about this capability.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Related Enforcement Actions

* [Bastazo - Sync Cyber Assets](https://docs.axonius.com/axonius-help-docs/docs/bastazo-sync-cyber-assets)
* [Bastazo - Sync Software Assets](https://docs.axonius.com/axonius-help-docs/docs/bastazo-sync-software-assets)