# Source: https://docs.axonius.com/docs/menmice-dns-management.md

# Men&Mice DNS Management

Men\&Mice DNS Management is a Network Management platform providing secure, centralized, and resilient control of DNS across diverse platforms.

<Callout icon="📘" theme="info">
  NOTE

  Axonius uses the [Men & Mice Web Service REST API](https://www.menandmice.com/resources/rest-api/)
</Callout>

**Related Enforcement Actions:**

* [Men\&Mice - Subnet Location Enrichment](/docs/men-and-mice-subnet-enrichment)

## Adapter Parameters

1. **MenAndMice Domain** *(required)* - The hostname of the Men\&Mice server.

2. **User Name** and **Password** *(required)* - The user name and password for an account that has read access to the API.

3. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![MenNdMice.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MenNdMice.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Fetch devices** - Fetches devices from the Devices endpoint.

2. **Fetch DNS Zones as assets** - Fetches devices from the DNSZones endpoint.

3. **Fetch Users** - Fetches users from the Users endpoint.

4. **Fetch IPAM Records**  -   Select this option to fetch IPAM Records as devices.

5. **Fetch DHCP servers** - check this to fetch DHCP servers as assets.

6. **Fetch DNS servers** - check this to fetch DNS servers as assets.

7. **Fetch DNS records** - check this to fetch DNS records as assets.

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>