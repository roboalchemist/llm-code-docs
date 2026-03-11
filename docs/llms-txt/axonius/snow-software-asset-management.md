# Source: https://docs.axonius.com/docs/snow-software-asset-management.md

# Snow Software Asset Management

Snow Software provides Software Asset Management (SAM) products and services to reduce the risk, cost, and complexity associated with software assets and licensing.

## Parameters

1. **Snow Domain** *(required)* - The hostname or IP address of the Snow Software server.
2. **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.
3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="SnowSoftwareAsset.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SnowSoftwareAsset.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch applications** *(required, default: False)* - Select this option to fetch installed applications.
2. **Fetch custom fields** - Select this option to get full object details. This option performs requests per asset.
3. **Fetch agreements** - Select this option to get agreements for the customer ID and add it to all devices
4. **Entities per page** *(default 200)* - Set pagination assets per page.
5. **Applications async requests count** *(default: 50)* - Set async requests when fetching applications.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Required Permissions

The value supplied in [Username](#parameters) must have read access to devices.

The username and password for a Snow License Manager (SLM) user account assigned to **API Users** role. User accounts are managed in the **Snow Management and Configuration Center**.