# Source: https://docs.axonius.com/docs/cscdomainmanager.md

# CSCDomainManager

CSCDomainManager is a web-based portfolio management platform consolidating domains alongside social media usernames, SSL digital certificates, and DNS. Integrate CSCDomainManager with the Axonius Cybersecurity Asset Management Platform.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Domains & URLs
* Certificates

## Adapter Parameters

1. **CSC API Server** *(required, default: `https://apis.cscglobal.com`)* - Enter the CSC API host.
2. **Zone Name** *(optional)* - Enter the DNS zone name. If left blank, all domains are fetched from a single CSCDomainManager connection.

<Callout icon="📘" theme="info">
  Note

  You have to enter a value either for the **Zone Name** or the **Account Number** in     order to fetch data.
</Callout>

4. **User Token** *(required)* - Enter the user token supplied by CSC (such as: xxxx-xxxx-xxxx-xxxx-xxxx-xxxx-xxxx).
5. **API Key** *(required)* - Enter the API key supplied by CSC.
6. **Account Number** *(optional)* - Enter the number of your CSGGlobal account to fetch all devices from all zone names.

<Callout icon="📘" theme="info">
  Note

  You have to enter a value either for the **Zone Name** or the **Account Number** in     order to fetch data.
</Callout>

1. Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** *(optional)* - Enter a proxy to use when connecting to the **CSC API Server**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![CSCDomain.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CSCDomain.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Get Zones** *(required, default: True)* - Select this option to fetch the domain’s zone information.
2. **Get Domain Info** - Select this option to fetch the domain information.
3. **Get Certificates as Assets** - Select this option to fetch certificates as assets.
4. **Use "qualifiedDomainName" field to fill Domain** - Select this option to use the "qualifiedDomainName" field to fill the Domain field (instead of using the “domain”).

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## APIs

Axonius uses the [DomainManager API (v2.0)](https://www.cscglobal.com/cscglobal/docs/dbs/domainmanager/api-v2/).