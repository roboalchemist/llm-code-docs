# Source: https://docs.axonius.com/docs/upguard-cyberrisk.md

# UpGuard CyberRisk

UpGuard CyberRisk provides third-party vendor risk and external cyber risk monitoring. The platform has two main modules: UpGuard BreachSight which monitors company external risk posture and Vendor Risk monitors and helps manages the risk posture of third party vendors.

### Asset Types Fetched

* Devices
* Aggregated Security Findings
* Users
* SaaS Applications
* Domains & URLs

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the following APIs:

* [UpGuard CyberRisk API](https://help.upguard.com/en/collections/2248373-upguard-api)
* [UpGuard CyberRisk Active risks](https://cyber-risk.upguard.com/api/docs#operation/risks)

### Permissions

To query the 'breaches' API Endpoint, the UpGuard instance needs to have 'identity breaches' enabled as a feature.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **UpGuard Domain** *(default: `https://cyber-risk.upguard.com`)* - Specify the URL of the UpGuard CyberRisk API.
2. **API Key** - Specify the API Key used for authentication.

<Image alt="UpGuard CyberRisk" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UpGuard%20CyberRisk.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Enrich devices with risks info** - Select this option to enrich the devices with risks data, using the endpoint [UpGuard CyberRisk Active risks](https://cyber-risk.upguard.com/api/docs#operation/risks).
2. **Fetch Vendors Domains** - Select this option to fetch all vendor domains (including vendor data).
3. **Fetch Users** - By default Axonius fetches users. Clear this option to not fetch users.
4. **Fetch SaaS Applications** - Select to fetch Saas Applications from the `/vendors` endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>