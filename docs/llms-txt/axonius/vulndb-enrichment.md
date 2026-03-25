# Source: https://docs.axonius.com/docs/vulndb-enrichment.md

# VulnDB Enrichment

VulnDB is a vulnerability intelligence platform that offers detailed information on software, hardware, and third-party library vulnerabilities to support risk assessment and remediation efforts.

### Asset Types Fetched

This adapter enriches Devices with CVE information.

#### Supported From Version

Supported from Axonius version 7.0.4

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the VulnDB server.
2. **Client ID** and **Client Secret**  - The credentials for a user account that has permissions to fetch assets.

![VulnDB\_parameters](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-W6CLR442.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).