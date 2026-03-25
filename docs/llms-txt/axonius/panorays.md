# Source: https://docs.axonius.com/docs/panorays.md

# Panorays

Panorays is a SaaS-based platform that enables companies to view, manage and engage on the security posture of their third-parties, vendors, suppliers, and business partners.

### Asset Types Fetched

* Devices
* Aggregated Security Findings
* SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### Permissions

The value supplied in [API Token](#required-parameters) must be associated with credentials that have permissions for the `suppliers` endpoint in order to fetch assets.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Panorays Domain** *(default: `https://api.panoraysapp.com`)* - The hostname or IP address of the Panorays server.
2. **API Token** - An API Token associated with a user account that has the Required Permissions to fetch assets.
3. **API RateLimit Window (seconds)** *(default: 1)* - Set the time frame for the rate limit to either 1 second or 60 seconds.

<Image alt="Panorays" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Panorays.png" />

### Optional Parameters

1. **Verify SSL** - Verify the SSL certificate offered by the value supplied in **Panorays Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Panorays Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch specific suppliers** - Enter a comma-separated list of specific suppliers to fetch.
2. **Fetch by Specific Portfolio** - Enter a comma-separated list of portfolio names to filter which suppliers to fetch.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>