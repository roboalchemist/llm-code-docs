# Source: https://docs.axonius.com/docs/claroty.md

# Claroty CTD

Claroty CTD discovers assets and monitors communication patterns for Industrial Control System networks.

## Assets Types Fetched

This adapter fetches the following types of assets:

* Devices, Aggregated Security Findings, Software, SaaS Applications

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Claroty Domain** *(required)* - The hostname of the Claroty server.

2. **User Name** and **Password** *(required)* - The credentials for a user account that has the permissions to fetch assets.

<Image alt="Claroty" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Claroty.png" />

### Optional Parameters

1. **Tenant Tag** *(optional)* - Automatically tag with the value specified, all devices discovered by this specific adapter connection.

2. **Rate Limit (requests per second)** *(integer)*- Enter a value to configure the number of requests the adapter is allowed to make each second. The default is no value, meaning no limit is set.

3. **Verify SSL** - Select whether to verify the SSL certificate offered by the value supplied in **Claroty Domain**. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

4. **HTTPS Proxy** *(optional)* - A proxy to use when connecting to the value supplied in **Claroty Domain**.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply for all connections for this adapter, or you can set different advanced settings and/or  different scheduling for a specific connection, refer to ​[Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Exclude IPv6 addresses** - Select whether to fetch IPv6 addresses.
   * If enabled, all connections for this adapter will fetch only IPv4 addresses.
   * If disabled, all connections for this adapter will fetch both IPv4 and IPv6 addresses.
2. **Virtual zone exclude list** *(optional)* - Enter a comma-separated list of Claroty virtual zones.
   * If supplied, all connections for this adapter will not fetch devices from virtual zones which are any of the comma-separated list of Claroty virtual zones that have been defined in this field.
   * If not supplied, all connections for this adapter will fetch devices with any Claroty virtual zone.
3. **Do not fetch devices with no IP address** - Select whether to fetch devices without an IP address.
4. **Do not fetch devices with no MAC address** - Select whether to fetch devices without a MAC address.
   * If enabled, all connections for this adapter will not fetch devices if they do not have a MAC address.
   * If disabled, all connections for this adapter will fetch devices even if they do not have a MAC address.
5. **Fetch only Unicast Devices** - Select whether to fetch only unicast devices.
6. **Fetch vulnerabilities** - Select this option to fetch vulnerabilities and add them to the matching devices.
7. **Additional insights to fetch** - Enter names of insights you want to enrich device data with. The adapter will query these insights and add the relevant fields to the Devices table.
8. **Exclude fetched devices with greater than "x" IP address** *(optional, default: 0)* - Exclude devices that are greater than the specified number of IP addresses. By default, a device is fetched, even if more than 1 IP address exists.
9. **Exclude fetched devices with greater than "x" MAC address** *(optional, default: 0)* - Exclude devices that are greater than the specified number of MAC  addresses. By default, a device is fetched, even if more than 1 MAC address exists.
10. **Fetch ghost devices** - From the dropdown, select how to fetch ghost devices, either *Fetch only ghost devices*, *Fetch only non-ghost devices* or *Fetch both*.
11. **Fetch installed programs** - Select this option to fetch installed programs.
12. **Specific fields** *(optional)* - Enter a list of specific fields to fetch. If the specified fields have values, only those fields will be fetched.