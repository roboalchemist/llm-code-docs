# Source: https://docs.axonius.com/docs/tripwire-ip360.md

# Tripwire IP360

Tripwire IP360 is a vulnerability management solution that provides comprehensive asset discovery, risk-based vulnerability assessment, and integration with security systems to prioritize remediation efforts.

### Asset Types Fetched

* Devices
* Vulnerabilities
* Users
* SaaS Applications
* Networks

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the Tripwire IP360 REST API.

### Permissions

The API user must have:

* Access to AssetView APIs (`/assetview/api/assets`)
* Access to Vulnerability and User data
* Access to `/rest/v1/*` endpoints (for users and networks)
* Ability to enumerate asset IDs and trigger queries per asset

Permissions must allow:

* Asset discovery
* Vulnerability listing
* User listing
* Network metadata access

#### Supported From Version

Supported from Axonius version 7.0.11

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Tripwire IP360 server.
2. **User Name** and **Password**  - The credentials for a user account that has the  Required Permissions to fetch assets.

<Image alt="TripwireIP360.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TripwireIP360.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).