# Source: https://docs.axonius.com/docs/recorded-future-asi.md

# Recorded Future Attack Surface Intelligence

Recorded Future Attack Surface Intelligence maps and monitors your exposed digital assets in real time, helping you proactively reduce risk — unlike the core platform, which focuses on external threats, this tool reveals your attack surface from an attacker’s perspective.

### Asset Types Fetched

* Devices
* Vulnerabilities
* SaaS Applications

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Token

### APIs

Axonius uses the [Recorded Future API](https://docs.recordedfuture.com/reference/get-started).

### Permissions

The following permissions are required:

* **API Access Level**:
  * The API key must have permission to:
    * List projects via `GET /v2/projects`
    * Fetch asset data via `POST /v2/projects/{project_id}/assets/_search`
* **Minimum Required Access**:
  * Project-level read access

  * Asset visibility/read permissions for IPs and domains

#### Supported From Version

Supported from Axonius version 7.0.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.securitytrails.com`)* - The hostname or IP address of the Recorded Future server.
2. **API Token**  - An API Token associated with a user account that has the Required Permissions to fetch assets.

<Image alt="Recorded Future ASI.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Recorded%20Future%20ASI.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).