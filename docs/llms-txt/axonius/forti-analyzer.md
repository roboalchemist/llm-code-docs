# Source: https://docs.axonius.com/docs/forti-analyzer.md

# Fortinet FortiAnalyzer

FortiAnalyzer is a centralized log management and analytics platform that provides log collection, correlation, analysis, and reporting from Fortinet devices and third-party syslog sources for security monitoring and compliance.

### Use Cases the Adapter Solves

* **Verify Fortinet Device Coverage:** Ensures all Fortinet firewalls, switches, and security appliances are sending logs to FortiAnalyzer, helping identify gaps in security monitoring and compliance coverage.
* **Monitor Log Collection Status:** Track which devices are actively sending logs and when they last reported, enabling proactive identification of devices that may have stopped logging due to configuration issues or connectivity problems.

### Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

The following data can be fetched by the adapter:

**Devices** - Fields such as Name, Hostname, Serial Number, Device Model

## Before You Begin

### Required Ports

TCP port 443 (HTTPS)

### Authentication Methods

The adapter authenticates using username and password credentials to obtain a session token.

### APIs

Axonius uses the [FortiAnalyzer JSON-RPC API](https://docs.fortinet.com/document/fortiportal/6.0.11/api-guide/751245/fortianalyzer). The following endpoints are called:

* `POST /jsonrpc` with `/sys/login/user` - Authenticate and obtain session token
* `POST /jsonrpc` with `/dvmdb/device` - Retrieve device information from Device Manager database
* `POST /jsonrpc` with `/logview/logstats` - Retrieve log statistics for each device

### Required Permissions

The API user must have the following permissions configured in FortiAnalyzer:

#### Minimum Required Permissions

* **JSON-RPC API access** - Enabled for the user account and requires read-write permissions.

<Callout icon="📘" theme="info">
  Note:

  * Since the adapter uses the JSON-RPC protocol, all requests — including those that only retrieve data — are sent using the POST method.

    Although read-write permissions are required for the API to function correctly, this does not automatically allow changes to be made. Any modifications are still governed by the user profile configuration and its associated restrictions.
</Callout>

* **Read access to Device Manager** - Permission to access `/dvmdb/*` endpoints for device enumeration
* **Read access to Log View** - Permission to access `/logview/*` endpoints for log statistics
* **ADOM access** - Access to all relevant Administrative Domains (ADOMs) if multiple ADOMs exist

#### Recommended Role

**Read-Only Administrator** or a custom role with these permissions.

### Supported From Version

Supported from Axonius version 8.0.15.2

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Fortinet FortiAnalyzer, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The base URL of your FortiAnalyzer instance. Include the protocol prefix (http\:// or https\://). \`
2. **User Name** - The username of the FortiAnalyzer administrator account with JSON-RPC API access and required permissions.
3. **Password** - The password for the FortiAnalyzer administrator account.

<br />

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/Fortianalyzer.png)

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.
   <br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

<br />

<br />

<br />

<br />