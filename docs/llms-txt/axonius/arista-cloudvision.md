# Source: https://docs.axonius.com/docs/arista-cloudvision.md

# Arista CloudVision

CloudVision Portal (CVP) is the web-based GUI for the CloudVision platform, which enables network-wide workload orchestration and workflow automation.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password for Cloud

### APIs

Axonius uses the [CloudVision Inventory API](https://aristanetworks.github.io/cloudvision-apis/examples/rest/inventory/).

### Permissions

Consult with your vendor for permissions for reading the objects.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Arista CloudVision server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **Token** is not supplied, **User Name** and **Password** are required.
</Callout>

3. **Token** - An API Key associated with a user account that has permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  When **User Name** and **Password** are not supplied, **Token** is required.
</Callout>

4. **Version** *(default: Arista V2)* - Select the API version, either Arista V1 or Arista V2.

<Image alt="CloudVision" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CloudVision.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch Vulnerabilities (Arista V2 only)** - Select this option to fetch vulnerabilities as assets.
2. **Fetch Location (Arista V2 only)** - Select this option to fetch location data.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>