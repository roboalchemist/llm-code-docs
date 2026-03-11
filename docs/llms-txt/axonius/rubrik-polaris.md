# Source: https://docs.axonius.com/docs/rubrik-polaris.md

# Rubrik Security Cloud

Rubrik provides data security and data protection on a single platform, including: Zero Trust Data Protection, ransomware investigation, incident containment, sensitive data discovery, and orchestrated application recovery.

### Asset Types Fetched

* Devices, Users, Databases, File Systems, Accounts/Tenants, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client ID / Client Secret

### APIs

Axonius uses the [Rubrik GraphQL API](https://rubrikinc.github.io/rubrik-api-documentation/reference/).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 4.8

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

* **Host Name or IP Address** - The hostname or IP address of the Rubrik Security Cloud server.

<Image alt="RubrikPolaris" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RubrikPolaris.png" />

### Optional Parameters

1. **Client ID** and **Client Secret** - The Rubrik Security Cloud Client ID and Client Secret. To generate client credentials, see [Adding a service account](https://docs.rubrik.com/en-us/saas/saas/adding_a_service_account.html).

2. **Subscription Name** - The 0365 Subscription Name.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

5. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

6. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch users** *(required, default: true)* - By default this adapter fetches users. Clear this option to not fetch users.
2. **Parse cluster nodes as devices** - Select this option to parse the cluster nodes from the cluster raw as devices.
3. **Object types to parse location as name** - Enter a list of object types to parse asset name and hostname from the device location. This setting only works for devices that have the asset type field with the value `edge`.
4. **Parse name and hostname from location** - Select this option to parse `Asset Name` and `Host Name` from `Node Location`.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>