# Source: https://docs.axonius.com/docs/godaddy.md

# GoDaddy

GoDaddy is a domain registrar that also offers additional services such as website building and management, website and email hosting, SSL security, and more.

The GoDaddy adapter enables Axonius to fetch and catalog domains, providing visibility into their registration details and DNS configuration.

## Asset Types Fetched

* Devices
* Domains & URLs
* Certificates

## Before You Begin

### Required Permissions

An API key must be associated with Read-Only credentials that have permissions to fetch assets.

### APIs

Axonius uses the [Brandsight API](https://developer.brandsight.com/#tag/Domains).

### Supported From Version

This adapter is supported from Axonius version 4.6.

## Connection Parameters

1. **GoDaddy Base URL** *(required, default: `https://api.godaddy.com`)* - Enter the hostname or IP address of the GoDaddy server.
2. **API Key** and **Secret Key** *(optional)* - Enter the API credentials associated with a user account that has permissions to fetch assets.
3. **Brandsight (GoDaddy v2) API Key** and **Brandsight (GoDaddy v2) Secret Key** *(optional)* - Enter the Brandsight (GoDaddy v2) API credentials associated with a user account that has permission to fetch domains.
4. **Brandsight Customer ID** *(optional)* - Enter the Brandsight customer identifier.
5. **Entitlement ID** *(optional)* - Enter the Entitlement ID to be used in certificates fetching.
6. **Use GoDaddy v2 API** - Select whether to use the GoDaddy v2 API.

<Callout icon="📘" theme="info">
  Note

  When **Use GoDaddy v2 API** is not selected, **API Key** and **Secret Key** are required. When **Use GoDaddy v2 API** is selected, **Brandsight (GoDaddy v2) API Key** and **Brandsight (GoDaddy v2) Secret Key** are required.
</Callout>

7. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

8. **HTTPS Proxy** *(optional)* - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

9. **HTTPS Proxy User Name** *(optional)* - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

10. **HTTPS Proxy Password** *(optional)* - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<Image alt="GoDaddy" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/GoDaddy.png" />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch all domain record types (A, TXT, MX, CNAME)** - Select this option to fetch all the records of type A, TXT, MX, and CNAME for all domains using the [Domains API](https://developer.godaddy.com/doc/endpoint/domains#/v1/recordGet).
2. **Fetch Records as Devices** - Select this option to fetch DNS records for each domain as devices.
3. **Fetch Certificates** - Select this option to fetch certificates as assets.
4. **Keep fetch URLs also as devices (Legacy Mode)** - Select this option to keep fetching URLs also as devices.
5. **Exclude domains without a public IP** *(default: true)* - By default Axonius excludes domains without a public IP. Clear this option to include domains without a public IP.
6. **DNS server IP** - Specify the DNS server IP to use for translating a hostname to IP.
7. **Perform DNS lookup with chain** - Select this option to resolve the full DNS chain for fetched domains. When enabled, the adapter follows DNS records (such as CNAMEs) to their final destination, populating the final IP addresses.