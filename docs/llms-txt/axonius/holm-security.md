# Source: https://docs.axonius.com/docs/holm-security.md

# Holm-Security

Holm Security is a cybersecurity platform that provides vulnerability management, attack surface visibility, compliance reporting, and risk assessment across external and internal digital assets.

### Use Cases the Adapter Solves

* **Asset Inventory & Discovery**: Maintain an accurate inventory of all devices and network assets with detailed information including operating systems, network interfaces, and device states.
* **Vulnerability Risk Management**: Identify and track devices with vulnerabilities across your infrastructure, including vulnerability counts, severity levels, and CVSS scores to prioritize remediation efforts.

### Asset Types Fetched

* Devices

## Data Retrieved through the Adapter

The following data can be fetched by the adapter:

**Devices** Fields such as: Hostname, Device Name, Device UID/UUID, Operating System details (Family, Name, Version, Build).

## Before You Begin

### Required Ports

* TCP port 443 (HTTPS)

### Authentication Methods

**Token Authentication** - The adapter uses API Token authentication.

### APIs

Axonius uses the Holm Security API. The following endpoints are called:

**Device Management:**

* `GET /devices`
* `GET /net-assets`

### Required Permissions

The API user must have the following permissions in the Holm Security platform:

#### API Access Permissions

* **API Token with appropriate permissions** - The token must be configured with explicit permissions during creation
* **Read access to devices** - Permission to retrieve device information via the `/devices` endpoint
* **Read access to network assets** - Permission to retrieve network asset information via the `/net-assets` endpoint
* **Full account access** - Required to create or manage API tokens within the Security Center

**Note:** The exact permission names and role requirements should be confirmed with your Holm Security administrator or Holm Security support, as detailed API permission documentation may not be publicly available. Each API token has explicit permissions that must be configured during the token creation process.

### Supported From Version

Supported from Axonius version 8.0.15.2

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Holm Security, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - \_(Default: `https://se-api.holmsecurity.com`.) \_   The base URL of your Holm Security API. Should contain a prefix of `http://` or `https://`.
2. **API Token** - The API token generated from your Holm Security Security Center. The token must have appropriate permissions configured

<br />

![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/HolmSEcurity.png)

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**

<br />

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

<br />

<br />

<br />