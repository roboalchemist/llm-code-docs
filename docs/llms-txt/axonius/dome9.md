# Source: https://docs.axonius.com/docs/dome9.md

# Check Point CloudGuard

Check Point CloudGuard automates governance across multi-cloud assets and services including security posture assessment, misconfiguration detection, and enforcement of security best practices and compliance frameworks.

### Asset Types Fetched

* Devices
* Users
* Compute Services
* Load Balancers
* Databases
* Containers
* Disks
* Network/Firewall Rules

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key/API Secret

### APIs

Axonius uses the [CloudGuard API](https://api-v2-docs.dome9.com/#dome9-resources).
You can create an API key and secret by opening the [CloudGuard web application](https://secure.dome9.com/) and navigating to the **My Settings** section.

### Permissions

The value supplied in [API Key](#required-parameters) must be associated with credentials that have permissions to use RESTful HTTP requests.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Check Point CloudGuard server.

2. **API Key** - A V2 API key associated with a user account that has permissions to fetch assets.

3. **API Secret** - A V2 API secret associated with a user account that has permissions to fetch assets. For more details, see [APIs](/docs/dome9#apis).

<Image alt="Check%20Point%20CloudGuard" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Check%20Point%20CloudGuard.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch device findings** - Select this option to fetch device information from Check Point CloudGuard.
2. **Enabled asset types** - List of asset types that can be fetched. All the types are selected by default.
   * Clear asset types you do not want to fetch.
   * When you click in the box, a drop-down list appears. You can both select and clear asset types you do not want to fetch from here too.
3. **Fetch only billable asset types** - Select this option to filter assets based on billable property.
4. **Asset types to fetch as separate assets** - Select assets that you want to fetch as separate assets instead of as devices from the drop-down list.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>