# Source: https://docs.axonius.com/docs/whitehat.md

# Black Duck Continuous Dynamic (formerly NTT Application Security)

Black Duck Continuous Dynamic (formerly NTT Application Security/WhiteHat Security) is a Dynamic Application Security Testing (DAST) tool that provides automated dynamic analysis to identify runtime vulnerabilities during application testing and development workflows.

## Asset Types Fetched

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg" /> Devices | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Findings.svg" /> Aggregated Security Findings | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Users.svg" /> Users | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Software.svg" /> Software | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Roles.svg" /> Roles | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Groups.svg" /> Groups | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/SaaS_Application.svg" /> SaaS Applications | <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Alerts_Incidents.svg" /> Alerts/Incidents

## Before You Begin

### APIs

Axonius uses the [API Assets API v2.0 - Retrieve API Asset Information](https://apidocs.whitehatsec.com/whs/reference/getapiassetsreq-1).

### Required Ports

* **TCP port 80, 443**

### Required Permissions

* ReadOnly

### Supported From Version

Supported from Axonius version 4.7

## Connecting the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the NTT Application Security server.

2. **API Key** - An API Key associated with a user account that has permissions to fetch assets. To obtain an API key generate it through the application's console. See [Authentication](https://apidocs.whitehatsec.com/whs/docs/authentication).

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BlackDuckContinuous_connection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch asset findings**  - Select to fetch findings for each asset.
2. **Fetch site credentials** - Select this option to fetch site credentials.
3. **Fetch found links from the recent scan** - Select this option to fetch links found from the most recent scan.
4. **Fetch asset BLA information** - Select asset BLA information to fetch from the list, ('Details', 'Statistics', 'History', 'Capacity', 'Information')
5. **Number of assets per request** *(optional, default: 50)* - Set the number of assets to fetch in the API response from the WhiteHat API. This configuration is recommended in order to reduce the adapter memory usage when it is too high. The minimum value is 1; the maximum value is 200.
6. **Fetch vulnerabilities from source** - Select this option to fetch vulnerabilities. They will be parsed as Application Development Exposures generic asset.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## Version Matrix

This adapter was only tested with the versions marked as supported, but may work with other versions. Contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed, which is not functioning as expected.

| Version                | Supported | Notes |
| ---------------------- | --------- | ----- |
| WhiteHat version 1.0.0 | Yes       |       |

<br />