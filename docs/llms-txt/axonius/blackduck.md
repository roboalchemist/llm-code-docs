# Source: https://docs.axonius.com/docs/blackduck.md

# Black Duck

Black Duck is a software composition analysis tool for managing open source risks.

## Asset Types Fetched

* Aggregated Security Findings
  , SaaS Applications
  , Application Services
  , Application Resources

## Before You Begin

### APIs

Axonius uses the [Black Duck API](https://verint.app.blackduck.com/doc/SDK/API_List1.html).

### Required Ports

* **TCP port 443**

### Required Permissions

The API key you use to connect the adapter must be associated with a user account that has the Read and Write Access scope.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Black Duck server that Axonius can communicate with via the [Required Ports](#required-ports).

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. Note that when creating the API token, the “Read and Write Access” scope option must be enabled.

![](https://files.readme.io/9d519380f1a5c04337424c908e7d05c4361a7c7a7a3cbc8e9dd50b0cfaec0974-image.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

<br />

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>