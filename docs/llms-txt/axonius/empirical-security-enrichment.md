# Source: https://docs.axonius.com/docs/empirical-security-enrichment.md

# Empirical Security Enrichment

Empirical Security provides vulnerability intelligence and exploitation activity data to enhance CVE analysis and prioritization.

### Asset Types Fetched

This adapter doesn't fetch any assets but enriches data on vulnerabilities and vulnerable software.

### APIs

Axonius uses the [Empirical Security API](https://app.empiricalsecurity.com/).

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Empirical Security server.
2. **Client ID** and **Client Secret** - See [detailed instructions](https://docs.empiricalsecurity.com/empirical-security/authentication) on how to generate these parameters.

<Image alt="connection parameters" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/EmpiricalSecurityAddConnection.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Host Name or IP Address**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-setting).
2. **HTTPS Proxy** - A proxy to use when connecting to the value supplied in **Host Name or IP Address**.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
5. **Logs contain user information** - If logs contain user data, select this option to fetch users instead of devices.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).