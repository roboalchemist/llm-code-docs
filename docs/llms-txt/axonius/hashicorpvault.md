# Source: https://docs.axonius.com/docs/hashicorpvault.md

# HashiCorp Vault

HashiCorp Vault is a tool that provides secure storage and access management for sensitive data and secrets.

### Asset Types Fetched

* Users, Application Resources

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* API Key

### APIs

Axonius uses the following API endpoints:

* Users -[Read entity by ID](https://developer.hashicorp.com/vault/api-docs/secret/identity/entity#read-entity-by-id)
* Application Resources -[/sys/mounts](https://developer.hashicorp.com/vault/api-docs/system/mounts)

### Permissions

The API Key must be granted the appropriate permissions to make the API calls listed.

#### Supported From Version

Supported from Axonius version 6.1.70

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the HashiCorp Vault server. Should contain a prefix of http\:// or https\://.
2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. For more information, see [Authentication](https://developer.hashicorp.com/vault/api-docs#authentication).

![HashiCorp Vault.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/HashiCorp%20Vault.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Users from Entities Endpoint** - Enable this option to fetch users from the Entities endpoint. When enabled, the following setting can be configured:
   * **Enrich Entities Endpoint with Certificates Endpoint** - Enable this option to enrich the Entities endpoint with the Certificates endpoint.
2. **Fetch ApplicationResources of sub type mount from Mounts Endpoint** - Enable this option to fetch application resources of the subtype 'mount' from the Mounts endpoint.
3. **Fetch ApplicationResources of sub type certificate from Certificates Endpoint** - Enable this option to fetch application resources of the subtype 'certificate' from the Certificates endpoint.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>