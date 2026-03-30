# Source: https://docs.axonius.com/docs/mandiant-enrichment.md

# Mandiant Enrichment

Mandiant is a cybersecurity platform offering threat intelligence, incident response, and security consulting services to detect and mitigate advanced cyber threats.

### Asset Types Fetched

This adapter enriches Devices and Aggregated Security Findings with CVE information from Mandiant.

## Before You Begin

### APIs

Axonius uses the Mandiant Threat Intelligence v4.0 API.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Mandiant server.
2. **API Key** and **API Secret** - The API key and secret associated with a user account that has permissions to fetch assets.
3. **Application Name** - Name of the integration used by Mandiant.

<Image align="center" alt="MandiantEnrichmentParams" border={false} width="800px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-S3442U3Z.png" />

### Optional Parameters

The following parameters are optional:

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy**   - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password**   - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).