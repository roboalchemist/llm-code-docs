# Source: https://docs.axonius.com/docs/cisco-secure-access.md

# Cisco Secure Access

Cisco Secure Access is a tool that provides secure access to your network and devices. It allows you to manage and control access to your network and devices, ensuring that only authorized users can access them.

### Asset Types Fetched

* Devices
* Users
* SaaS Applications
* Domains & URLs
* Organizational Units
* Networks

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* Client ID/Client Secret

### APIs

Axonius uses the [Cisco Secure Access API](https://developer.cisco.com/docs/cloud-security/secure-access-api-reference-overview/).

### Permissions

You must configure a CSA account that has a Read-Only permission for the Keyscope - Reports `>` Utilities.

#### Supported From Version

Supported from Axonius version 6.1.59

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Cisco Secure Access server.

2. **Client ID** and **Client Secret** - The credentials for a user account that has the Required Permissions to fetch assets. For more information, see [Manage API Keys](https://developer.cisco.com/docs/cloud-security/secure-access-api-authentication/#manage-api-keys).

<Image alt="CiscoSecureAccess.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CiscoSecureAccess.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

### Endpoints Config

This section lists asset types and sub-types that the adapter can fetch from different endpoints. Enable each setting to fetch the specified asset type from the specified endpoint. For example:

* Enable **Fetch Devices of sub type roaming\_computer from Roaming Computers** to fetch Roaming Computer Devices from the Roaming Computers endpoint.
* Enable **Fetch URLs from Internal Domains** to fetch URL assets from the Internal Domains endpoint.
* **Exclude Deleted Users** - Select this option to not fetch deleted users.

Additional settings become available when you enable certain settings.

* For example, when you enable **Fetch Networks of sub type dns\_forwarder from DNS Forwarders**, the **DNS Forwarder Type** becomes available, where you can specify a DNS forwarder type (the default is *networkdnsforwarder*)

### Parser Config

1. **Use the label to identify deleted users** - Select this option to identify deleted users by the Label field.
2. **Capture User information from the raw label field** - Select this option to fetch user information from the Raw Label field.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>