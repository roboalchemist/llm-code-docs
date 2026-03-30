# Source: https://docs.axonius.com/docs/akamai-api-security.md

# Akamai API Security

Akamai API Security is a solution that provides continuous API discovery, runtime threat detection, and active testing to protect APIs across environments.

### Asset Types Fetched

* Domains & URLs

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* Client Token / Client Secret
* Access Token

All Application Security API endpoints require Akamai EdgeGrid authentication (token-based).

### APIs

Axonius uses the [Akamai Application Security API](https://techdocs.akamai.com/application-security/reference/api).

### Permissions

The credential must be assigned to an API Client that is granted access to the Application Security API.

#### Supported From Version

Supported from Axonius version 7.0.12

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Akamai API Security server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Access Token** - An Access Token associated with a user account that has the Required Permissions to fetch assets.

![AkamaiAPISecurity.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AkamaiAPISecurity.png)

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

* **Include Hidden APIs** - Select this option to include hidden APIs.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>