# Source: https://docs.axonius.com/docs/censys-asm.md

# Censys ASM

Learn about Censys ASM, its use cases, asset types fetched, setup, and connection parameters for Axonius.

Censys ASM is a tool designed to provide attack surface management by identifying and monitoring threats and exposures.

### Asset Types Fetched

Devices, Software, Activities,  SaaS Applications, Domains & URLs, Certificates, Application Resources

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

API Key

### APIs

Axonius uses the following APIs:

* GET /v1​/assets​/hosts
* GET /v1​/assets​/certificates
* GET /v1​/assets​/domains
* GET /v1​/assets​/subdomains
* POST /v1/logbook-cursor
* GET /v1​/logbook

For more information, see [https://app.censys.io/api-docs](https://app.censys.io/api-docs).

### Permissions

The following permissions are required:

The value supplied in [API Key](#parameters) must be associated with credentials that have Teams API Key permissions in order to fetch assets.

#### Supported From Version

Supported from Axonius version 6.1

## Connecting the Adapter in Axonius

Navigate to the Adapters page, search for Censys ASM, and click on the adapter tile.

Click **Add Connection**.

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** - The hostname or IP address of the Censys ASM server.

2. **API Key** - An API Key associated with a user account that has the Required Permissions to fetch assets.

![Censys ASM](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/adapters/CensysASM.png)

<br />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note:

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

**Endpoints Config**  - Configure the Endpoints from which to fetch data

1. **Fetch Devices from device** *(default: Enabled)* — Enable this option to fetch host assets from the devices endpoint.
2. **Fetch URLs of sub type url from url** - Select this option to fetch and parse URL assets.
3. **Fetch URLs of sub type domain from domain\_url** — Enable this option to fetch and parse domain assets as Domain & URL assets. When disabled, domain data is only fetched as Application Resources.
4. **Fetch Certificates from certificate** *(default: Enabled)* — Enable this option to fetch certificate assets from the certificates endpoint.
5. **Fetch ApplicationResources from application\_resource** - Select this option to fetch Application resources
6. **Fetch AuditActivities from logbook** - Select this option to fetch Audit Activities.

**Parser Config**

1. **Parse Host Name From Reverse DNS**  - Select this option to parse the hostname from the `reverseDNs` instead of from the `forwardDNS`
2. **Filter URLs from Devices by valid TLD (com, info, gov, org, net, online, to, io, host)** - Select this option so that  assets with a valid Top Level Domain are only parsed as URL assets. When you do not select this option some assets may be parsed both as devices and as URLs.

<br />

<br />