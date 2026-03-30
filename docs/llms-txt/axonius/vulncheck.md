# Source: https://docs.axonius.com/docs/vulncheck.md

# VulnCheck

VulnCheck is a cybersecurity platform that identifies and assesses vulnerabilities within IT infrastructure for threat management.

## Asset Types Fetched

This adapter does not fetch any assets but enriches data on Security Findings.

## Before You Begin

### APIs

Axonius uses the [VulnCheck API](https://docs.vulncheck.com/api).

### Required Ports

* **TCP port 443**

### Supported From Version

Supported from Axonius version 6.1

## Deploying the Adapter in Axonius

### Required Parameters

1. **Host Name or IP Address** *(default: api.vulncheck.com)* - The hostname or IP address of the VulnCheck server.

2. **API Token** - To generate an API Token, follow these steps in your [VulnCheck account page](https://docs.vulncheck.com/getting-started/api-tokens#issue-an-api-token):
   1. Go to **Tokens & SSH Keys** under your user profile in the top right.
   2. Select **Create Token**.
   3. Enter a **Label** and choose a **Token Icon** to help remember what the API token is intended to be used for.
   4. Once you create the token, you will be able to see the its value. Note that this is the only time you will be able to see it, so ensure to copy and paste it in Axonius.

<Image border={false} src="https://files.readme.io/fe4075773ad0e398963413a5e0cf2b2b4cf49e55bc24364587f0a7ad07e85a2d-image.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

Enable the following settings to enrich the vulnerabilities fetched by VulnCheck with different data:

1. **Enrich KEV data with NVD2 data**
2. **Parse VulnCheck XDB data**
3. **Fetch Security Advisories**

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

[VulnCheck - Enrich CVE Data](/docs/en/vulncheck-enrich-cve-data)