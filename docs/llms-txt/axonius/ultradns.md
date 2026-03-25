# Source: https://docs.axonius.com/docs/ultradns.md

# Neustar UltraDNS

Neustar UltraDNS is a cloud-based authoritative DNS service.

### Asset Types Fetched

* Devices, Domains & URLs

## Before You Begin

**Ports**

* TCP port 443

**Authentication Method**

* User Name/Password

### APIs

Axonius uses the <Anchor label="Neustar UltraDNS REST API" target="_blank" href="https://ultra-portalstatic.ultradns.com/static/docs/REST-API_User_Guide.pdf">Neustar UltraDNS REST API</Anchor>.

### Permissions

The value supplied in [User Name](#required-parameters) must be allocated in the Reporting user group.

#### Supported From Version

Supported from Axonius version 4.5

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Host Name or IP Address** *(default: `https://api.ultradns.com`)* - The hostname or IP address of the UltraDNS server.
2. **User Name** and **Password** - The credentials for a user account that has the permissions to fetch assets.

<Image alt="UltraDNS" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/UltraDNS.png" />

### Optional Parameters

1. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
2. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.
3. **HTTPS Proxy User Name** - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.
4. **HTTPS Proxy Password** - The password to use when connecting to the server using the **HTTPS Proxy**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Aggregate Only A Record IP Addresses**  - If selected, will only add the IP for aggregation if the RDATA type is an A record. If cleared, any record will attempt to add an IP for aggregation.
2. **Add unresolved IP Addresses of a PTR record type** - Select this option to fetch and enrich unresolved IPs to a DNS PTR record (asset), since this information does not come in a PTR record.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>