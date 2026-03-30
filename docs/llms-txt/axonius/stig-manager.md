# Source: https://docs.axonius.com/docs/stig-manager.md

# STIG Manager

STIG Manager is a compliance management tool that offers automated security compliance checks and reporting.

### Asset Types Fetched

* Devices

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the following APIs:

* [stigman-watcher](https://github.com/NUWCDIVNPT/stigman-watcher)
* [STIG Manager’s documentation](https://stig-manager.readthedocs.io/en/latest/)

### Permissions

Most endpoints require OAuth tokens with specific scopes, including:
`stig-manager:collection:read` for read operations

#### Supported From Version

Supported from Axonius version 6.1.70

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the STIG Manager server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Auth Domain** - The unique identifier for an OAuth 2.0 authorization server.

<Image border={false} src="https://files.readme.io/cbde4cedbf4128bd970698076dff051f22ff7355843bc9e05296d3bb2c454bac-image.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config - Collections

1. **Collection IDs** - Enter comma-separated list of Collection IDs you want to fetch data from.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>