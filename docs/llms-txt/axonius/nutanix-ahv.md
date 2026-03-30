# Source: https://docs.axonius.com/docs/nutanix-ahv.md

# Nutanix AHV

Nutanix AHV is a hypervisor included with the Enterprise Cloud OS. AHV delivers flexible migrations, security hardening, automated data protection and disaster recovery, and analytics.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices, Compute Images

## Parameters

1. **Nutanix Domain** - The hostname of the Nutanix AHV server.
2. **User Name** and **Password** - The user name and password for an account that has read access to the API.
3. **API Version** *(required, default: V2)* - Select the [API version](/docs/nutanix-ahv#apis) that you want the Nutanix AHV adapter to access.
4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![nutanix.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/nutanix.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Only Powered On Devices** - Select whether to fetch only devices that are powered on.
2. **Parse Serial from Block Serial** - Select whether to parse the serial field from the 'block\_serial' raw data instead of 'serial'. **Note**: This setting is only available for API V2 connection.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Depending on what you select in the [**API Version** parameter](/docs/nutanix-ahv#parameters), Axonius uses the associated API endpoints.

| API Version | Endpoint                                                                                                                           |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| V2          | [Prism Element API v2: VMs](https://www.nutanix.dev/api_references/prism-v2-0/#/ZG9jOjQ1Mg-introduction)                           |
|             | [Prism Element API v2: Hosts](https://www.nutanix.dev/api_references/prism-v2-0/#/ZG9jOjQ1Mg-introduction)                         |
| V3          | [Prism Central API v3: VMs](https://www.nutanix.dev/api_references/prism-central-v3/#/1249f40c4f9db-get-a-list-of-existing-v-ms)   |
|             | [Prism Central API v3: Hosts](https://www.nutanix.dev/api_references/prism-central-v3/#/1249f40c4f9db-get-a-list-of-existing-v-ms) |