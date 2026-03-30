# Source: https://docs.axonius.com/docs/forti-manager.md

# FortiManager

FortiManager is a centralized management platform that provides configuration management, policy provisioning, device monitoring, and firmware management for Fortinet network and security devices, available as both an on-premises deployment and a cloud-hosted service.

The FortiManager adapter provides Axonius with visibility into network and security devices managed through Fortinet's centralized management platform, supporting both on-premises and cloud deployments.

## Asset Types Fetched

* Devices
* Users
* Network/Firewall Rules
* Alerts/Incidents
* Network Routes

## Data Retrieved through the Adapter

The adapter retrieves information to provide visibility into your publicly accessible assets. The retrieved data for each asset type may include:

* **Devices** - Data such as centralized configuration, policy provisioning, device monitoring, and firmware management for Fortinet devices.
* **Users** - Information regarding users managed within the Policy & Objects section.
* **Network/Firewall Rules** - Detailed firewall policy and object data.
* **Alerts/Incidents** - Log and report information for security monitoring.

## Before You Begin

### Required Ports

* TCP Port 443

### Authentication Methods

* IAM User Credentials - The adapter authenticates using a **Username** and **Password** for an API user account created in the Fortinet Identity and Access Management (IAM) portal.

### Required Permissions

The adapter connection requires that the IAM user has at least **Read-Only** access to the following sections in FortiManager:

* **Device Management** - To retrieve information on managed devices.
* **Policy & Objects** - To retrieve user and firewall policy data.
* **Log & Report** - To retrieve security alerts and incident logs.

### APIs

Axonius uses the <Anchor label="FortiManager API" target="_blank" href="https://docs.fortinet.com/document/fortimanager/7.6.0/api-best-practices/500458/introduction">FortiManager API</Anchor> to retrieve asset data.

### Generating FortiManager Credentials

1. Log in to the Fortinet IAM portal.
2. Create a **Permission Profile** that grants at least **Read-Only** access to the relevant **Administrative Domains (ADOMs)** and specific modules.
3. Ensure the profile includes access to **Device Management**, **Policy & Objects**, and **Log & Report**.
4. Create an **IAM API** user and assign it to the Permission Profile.
5. Record the **Username** and **Password** for use in the Axonius connection.

### Supported from Version

This adapter is supported from Axonius version 8.0.12.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name** - Enter the hostname or IP address of the FortiManager server.
2. **User Name** - Enter the IAM username.
3. **Password** - Enter the password associated with the IAM user.

<Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/FortiManager_Add_Connection.png" className="border" />

### Optional Parameters

1. **Port** - Enter the specific port for the connection if different from the default.
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.
4. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in HTTPS Proxy.
5. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the HTTPS Proxy.
6. **Is Hosted On Cloud** - Enable this option if the adapter should connect to FortiManager via FortiCloud hosting.

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

* **DHCP lease time (seconds)** - Enter the duration in seconds for the DHCP lease tracking. By entering a value in this field, you are instructing the adapter to track the validity of the asset's IP assignment for that specific timeframe. If left empty, the adapter relies on its own default internal logic or the data provided directly by the FortiManager API.
* **Interfaces exclude list** - Enter specific network interfaces to exclude from the fetch.
* **Vmware interfaces exclude list** - Enter specific VMware network interfaces to exclude.
* **Do not fetch OS Type field** *(default: false)* - Enable this to skip fetching the operating system type for devices.
* **Allow IPSEC VPN devices** *(default: false)* - Enable this to include IPSEC VPN devices in the fetch.
* **Fetch managed Fortigate devices** *(default: false)* - Enable this to retrieve data for FortiGate devices managed by the console.
* **Use Fortigate new OS version parser** *(default: false)* - Enable this to use the updated parsing logic for FortiOS versions.
* **Fetch firewall rules** *(default: true)* - Enable this to retrieve firewall policy data.
* **Maximum number of chunks** - Enter the maximum number of data chunks allowed for the fetch (default: 50).
* **Fetch VPN SSL Sessions as Devices** *(default: false)* - Enable this to treat SSL VPN sessions as separate device assets.
* **Parse Global Interfaces as Network Interfaces** *(default: false)* - Enable this to map global interface data to standard network interface fields.
* **Use fetch time for the "Last Seen" field** *(default: false)* - Enable this to set the "Last Seen" timestamp to the current fetch time.