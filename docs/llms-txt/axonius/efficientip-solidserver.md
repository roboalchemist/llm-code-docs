# Source: https://docs.axonius.com/docs/efficientip-solidserver.md

# EfficientIP SOLIDserver DDI

EfficientIP SOLIDserver DDI suite is designed to deliver virtual and hardware appliances for critical DNS-DHCP-IPAM services.

### Use Cases the Adapter Solves (optional)

* **Detecting Unmanaged Assets**: Identify devices within DNS, DHCP, and IPAM records that are not currently managed by security agents or scanners.
* **IP Address Management Visibility**: Analyze and track IP address allocations and lease history to maintain an accurate inventory of network devices.
* **Verifying Network Coverage**: Verify that all active network segments and DNS resource records are accounted for in the broader asset management strategy.

### Asset Types Fetched

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Devices.svg) Devices | ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/icons/Networks.svg) Networks

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

### APIs

Axonius uses the [SOLIDserverRest for Python](https://gitlab.com/efficientip/solidserverrest/) API.

<br />

#### Supported From Version

Supported from Axonius version 4.4

<br />

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for EfficientIP SOLIDserver DDI, and click on the adapter tile.\
Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the EfficientIP SOLIDServer DDI server.
2. **User Name** and **Password** - The credentials for a user account that has the Required Permissions to fetch assets.
3. **Connection Label** - A label to help you distinguish between multiple connections for the same adapter. See [Connection label](/docs/adding-a-new-adapter-connection#setting-adapter-connection-parameters).

<Image align="center" alt="EfficientIP SOLIDserver DDI connection screen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/BackBox.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.
5. **Select Gateway** – Select the [Axonius Gateway](https://docs.axonius.com/docs/installing-axonius-gateway) to use when connecting adapters whose sources are only accessible by an internal network and not from the primary Axonius instance, which may be an Axonius-hosted (SaaS) instance or Customer-hosted (on-premises / private cloud). To use this option, you need to set up an Axonius Gateway.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Treat first-three-segments of device name/FQDN as hostname** - Select whether to treat the first three dash-separated-segments of a device's name as a hostname. When you select this option, devices with three or more  dash-separated segments in their name will have their hostname truncated to the first three segments, for example,

   * one-two-thr33-four--.mydomain.com -> hostname = one-two-thr33
   * one-two.mydomain.com -> hostname = one-two.mydomain.com
2. **Fetch DNS servers as devices** - Select this option to fetch DNS servers and their Zones as devices.
3. **Fetch Resource Records (RRs) as devices** - Select this option to fetch DNS Resource Records as devices.
4. **Fetch DHCP scopes, scope options, ranges, leases, and statics as devices** - Select which DHCP elements  to fetch as devices.
5. **Page size per request** - Enter a value to set the page set of every request of the adapter to the set number (default is 1000).