# Source: https://docs.axonius.com/docs/jumpcloud.md

# JumpCloud

JumpCloud is a Directory-as-a-Service (DaaS) solution to authenticate, authorize, and manage users, devices, and applications via a common directory in the cloud.

## Asset Types Fetched

* Devices, Users, Software, All Application Extensions, All Application Extension Instances, SaaS Applications, Admin Managed Extensions, Application Addons, User Initiated Extensions, Admin Managed Extension Instances, Application Addon Instances, Application Keys, User Initiated Extension Instances

## APIs

Axonius uses the [JumpClod v2.0 API](https://docs.jumpcloud.com/api/2.0/index.html#tag/Graph/operation/policystatuses_systemsList).

## Connecting the Adapter in Axonius

### Required Parameters

1. **JumpCloud Domain** - Keep as *'[https://console.jumpcloud.com](https://console.jumpcloud.com)'*.
2. **API Key** - Use the API key you have generated. For details on generating a new API key, see [JumpCloud APIs on JumpCloud Support Center](https://support.jumpcloud.com/customer/portal/articles/2429680-jumpcloud-apis).
3. **Fetch Devices From All Apple MDMs** - Select whether to fetch devices from all Apple MDMs or not.

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/JumpCloudConnect.png)

### Optional Parameters

1. **Apple MDM ID** - Enter the Apple MDM ID in order to fetch devices from the `api/v2/applemdms/{apple_mdm_id}/devices` endpoint.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

* **Fetch System Policy Statuses Per Device** - Select to fetch system policy statuses for each device.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** t
</Callout>