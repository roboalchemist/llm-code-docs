# Source: https://docs.axonius.com/docs/security-journey.md

# Security Journey

Security Journey is a secure coding training platform that offers hands‑on lessons, assessments, and a reporting API for capturing developer learning metrics.

### Asset Types Fetched

* Users

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key

### APIs

Axonius uses the [Security Journey Reporting API v3](https://help.securityjourney.com/security-journey-api-v3).

### Permissions

API Access requires you to be a Security Journey Admin to generate an API key.

#### Supported From Version

Supported from Axonius version 7.0.7

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Security Journey server.
2. **API Key** - An API Key associated with a user account that has the  Required Permissions to fetch assets.

![Security Journey.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Security%20Journey.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).