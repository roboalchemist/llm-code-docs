# Source: https://docs.axonius.com/docs/akamai-kona-waf.md

# Akamai Kona WAF

Akamai Kona Web Application Firewall (WAF) provides protection against web application attacks including SQL injections, cross-site scripting, and remote file inclusion.

The Akamai Kona WAF adapter provides Axonius with visibility into your publicly accessible assets, including domain, URL, and security configuration data.

## Asset Types Fetched

* Devices
* Domains & URLs
* Network/Firewall Rules

## Before You Begin

### Required Ports

* TCP port 80/443

### Authentication Methods

* Client Token/Client Secret
* Access Token

### Required Permissions

The adapter connection requires an API user with permissions to retrieve firewall configurations, security files, and property manager data.

### APIs

Axonius uses the <Anchor label="Akamai Application Security API" target="_blank" href="https://techdocs.akamai.com/application-security/reference/api">Akamai Application Security API</Anchor> to retrieve asset data.

### Supported from Version

This adapter is supported from Axonius version 4.6.

## Connection Parameters

To connect the adapter in Axonius, provide the following parameters.

### Required Parameters

1. **Host Name or IP Address** - Enter the hostname or IP address of the Akamai Kona WAF server.

2. **Client Token** and **Client Secret**  - Enter the credentials for a user account that has permissions to fetch assets.

3. **Access Token** - Enter an API key associated with a user account that has permissions to fetch assets.

![Akamai](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Akamai.png)

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

2. **HTTPS Proxy** - Enter an HTTPS proxy address to connect the adapter to a proxy instead of directly connecting it to the domain.

3. **HTTPS Proxy User Name** - Enter the user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

4. **HTTPS Proxy Password** - Enter the password to use when connecting to the server using the **HTTPS Proxy**.

To learn about additional optional/common adapter connection parameters, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

<br />

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  * Advanced settings can apply to either all connections of this adapter, or to a specific connection. For more detailed information, see [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
  * For more general information about advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

1. **Fetch Firewall** *(default: false)* - Select this option to fetch firewalls.
2. **Fetch URLs** *(default: false)* - Select this option to fetch URLs.
3. **Fetch Dynamic IP Firewall & Network Lists** *(default: false)* - Select this option to fetch dynamic IP firewall and network lists, using the following endpoints:

   * <Anchor label="Get IP/Geo Firewall settings" target="_blank" href="https://techdocs.akamai.com/application-security/reference/get-policy-ip-geo-firewall">Get IP/Geo Firewall settings</Anchor>
   * <Anchor label="Get a network list" target="_blank" href="https://techdocs.akamai.com/network-lists/reference/get-network-list">Get a network list</Anchor>

   For this configuration to work properly, make sure that the “Fetch Firewall” configuration is also enabled.
4. **Fetch Rules tree and hostnames list from Property Manager** *(default: false)* - Select this option to create a URL entity, identify the Akamai property and version, list its hostnames, and retrieve the final edge URL and rule configuration.
5. **Parse URL IPs** *(default: false)* - Select this option to parse IPs for URL assets.
6. **Parse Devices** *(default: true)* – Select this option to parse assets as devices. For existing connections, this is enabled by default to preserve previous data modeling. For new connections, this is disabled by default, and assets are instead parsed as Domains & URLs.
7. **Parse hostname as URL name** - Select this option to parse the hostname as the URL name.