# Source: https://docs.axonius.com/docs/bitdefender-gravityzone-business-security.md

# Bitdefender GravityZone Business Security

Bitdefender GravityZone Business Security uses machine learning and heuristics to protect against malware, phishing, ransomware, exploits and zero-days.

### Asset Types Fetched

* Devices, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### Generating an API Key

To generate an API key in Bitdefender:

1. Login to a Bitdefender Control Center account with full administrator privileges.
2. In the upper-right corner of the console, click the username and select **My Account**.
3. Navigate to the Control Center API section and click **Add**.

<Image align="center" alt="BitDef_apilocation" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BitDef_apilocation.png" />

4. Verify that the **Network API** option is selected.

<Image align="center" alt="image" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1043).png" />

5. Click **Save** to generate a key for the selected API.

### Permissions

Consult with your vendor for permissions for reading the objects.

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Bitdefender Domain** - The hostname of the API server. Use: `https://cloud.gravityzone.bitdefender.com`
2. **Access URL Base Path** *(default: api)* - Specify the access URL base path.
3. **API Key** - An API Key associated with a user account that has permissions to fetch assets. For details, see [Generating an API Key](#generating-an-api-key).

<Image alt="Bitdefender" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Bitdefender.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Do not fetch Organizational Units** - Select this option to exclude devices defined as Organizational Units.
2. **Fetch only managed** - Select this option to fetch only managed devices.
3. **Fetch installed patches** - Select this option to fetch installed patches. ‘Patch Management’ must be enabled under ‘Enabled APIs’ in order to configure this setting.
4. **Fetch missing patches** - Select this option to fetch missing patches. ‘Patch Management’ must be enabled under ‘Enabled APIs’ in order to configure this setting.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>