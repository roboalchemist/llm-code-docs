# Source: https://docs.axonius.com/docs/watchtowr.md

# watchTowr

The watchTowr platform provides Continuous Automated Red Teaming (CART) and Attack Surface Management (ASM) to help businesses discover high-impact vulnerabilities.

The watchTowr adapter enables Axonius to fetch and catalog devices, vulnerabilities, SaaS applications, and cloud-related resources, ensuring comprehensive visibility into your external attack surface and high-impact vulnerabilities.

## Asset Types Fetched

This adapter fetches the following types of assets:

* Devices
* Vulnerabilities
* SaaS Applications
* Domains and URLs
* Containers
* Object Storage
* Application Resources

## Before You Begin

### Authentication Methods

* API Key (API Token)

### Required Permissions

The API key must be associated with a user account that has permissions to access and read the Integrations and Client API sections of the watchTowr organization portal.

### APIs

Axonius uses the watchTowr Platform Client API to retrieve asset data.

<Callout icon="📘" theme="info">
  Note

  You can find API documentation and access details within your watchTowr organization portal and through the watchTowr developer resources.
</Callout>

### Supported From Version

This adapter is supported from Axonius version 6.0.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the watchTowr server.

2. **API Key** - Enter the API key associated with a user account that has permissions to fetch assets.

3. **Business Unit IDs** - Enter the business unit IDs from which to retrieve the data.

<Image align="center" alt="watchTowr adapter - Add Connection" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/watchTowr_Add_Connection.png" className="border" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name**  - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

By default, the adapter enriches users via various endpoints. Expand **Endpoints Config`>`** to open the following settings for configurable endpoints:

1. **Fetch URLs of sub type domain from Domains Endpoint** (*default: true*) - By default, this adapter fetches devices of the subtype `domain` from the Domains endpoint. Toggle off to not fetch devices of the subtype `domain` from the Domains endpoint.
2. **Fetch Domains in the last X days** (*optional, default: 15*) - Enter the number of days back to fetch data from the Domains endpoint.
3. **Enrich Domains Endpoint with Findings Endpoint** (*default: true*) - Toggle on to enrich domain data with vulnerability information from the Findings endpoint.
4. **Fetch URLs of sub type subdomain from Subdomains Endpoint** (*default: true*) - By default, this adapter fetches devices of the `subtype` subdomain from the Subdomains endpoint. Toggle off to not fetch devices of the `subtype` subdomain from the Subdomains endpoint.
5. **Fetch Subdomains in the last X days** (*optional, default: 15*) - Enter the number of days back to fetch data from the Subdomains endpoint.
6. **Enrich Subdomains Endpoint with Findings Endpoint** (*default: true*) - Toggle on to enrich subdomain data with vulnerability information from the Findings endpoint.
7. **Fetch ObjectStorage from Cloud Storage Endpoint** (*default: false*) - Toggle on to fetch ObjectStorage from the Cloud Storage endpoint.
8. **Fetch Cloud Storage in the last X days** (*optional, default: 15*) - Enter the number of days back to fetch Cloud Storage.
9. **Fetch Containers from Containers Endpoint** (*default: false*) – Toggle on to fetch Containers from the Containers endpoint.
10. **Fetch Containers in the last X days** (*optional, default: 15*) - Enter the number of days back to fetch data from the Containers endpoint.
11. **Fetch ApplicationResources from Repositories Endpoint** (*default: false*) - Toggle on to fetch ApplicationResources from the Repositories endpoint.
12. **Fetch Repositories in the last X days** (*optional, default: 15*) - Enter the number of days back to fetch data from the Repositories endpoint.
13. **Fetch Devices from IP Addresses Endpoint** (*default: true*) - By default, this adapter fetches devices of the subtype `ip_address` from the IP Addresses endpoint. Toggle off to not fetch devices of the subtype `ip_address` from the IP Addresses endpoint.
14. **Fetch IP Addresses in the last X days** (*optional, default: 15*) - Enter the number of days back to fetch data from the IP Addresses endpoint.
15. **Enrich IP Addresses Endpoint with Findings Endpoint** (*default: true*) - Toggle on to enrich IP address data with vulnerability information from the Findings endpoint.