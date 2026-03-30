# Source: https://docs.axonius.com/docs/tenable-nessus.md

# Tenable Nessus

Tenable Nessus is a vulnerability scanning platform for auditors and security analysts.

## Asset Types Fetched

* Devices, Aggregated Security Findings, SaaS Applications, Domains & URLs

## Parameters

1. **Host Address** *(required)* - The hostname or IP address of the Tenable Nessus server.
2. **Port** *(optional)*
3. **User Name** and **Password** *(optional)* - The credentials for a user account that has the permissions to fetch assets.

<Callout icon="📘" theme="info">
  Note

  If **Access API Key** and **Secret API Key** are not supplied, you must specify **User Name** and **Password**.
</Callout>

4. **Access API Key** and **Secret API Key** *(optional)* - An API Key associated with a user account that has permissions to fetch assets. For details, see [Tenable Nessus - Generate an API Key](https://docs.tenable.com/nessus/Content/GenerateAnAPIKey.htm).

<Callout icon="📘" theme="info">
  Note

  If **User Name** and **Password** are not supplied, you must specify **Access API Key** and **Secret API Key**.
</Callout>

5. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

![nessus.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/nessus.png)

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Scan IDs  include list** *(optional, default: empty)* - Specify a comma-separated list of Tenable Nessus scan IDs.
   * If supplied, all connections for this adapter will only collect devices discovered by Tenable Nessus scan IDs provided in this list.
   * If not supplied, all connections for this adapter will collect devices discovered by any Tenable Nessus scan.
2. **Only get devices with MAC, Hostname or correlatable IP address** *(required, default: False)* - Choose whether to exclude fetching devices without MAC address, without hostname and without an IP address that can be correlated to other existing IP address.
   * If enabled, all connections for this adapter will only fetch devices having at least one of the following:
     * MAC address
     * Hostname
     * IP address that can be correlated with an existing IP address in Axonius.
   * If disabled, all connections for this adapter will fetch devices even if those do not have MAC address, no hostname and no IP address that can be correlated to other existing IP address.
3. **Do not fetch devices with no MAC address and no hostname** - Select whether to exclude fetching devices without a MAC address and without a hostname.
4. **Fetch agents endpoint** - Select this option to fetch agents (the Tenable Nessus endpoint called agents) as devices.
5. **Fetch plugin output**- Select this option to fetch plugin output.
6. **Fetch scans from the last X days** - Specify the number of days from which to   fetch scan data.
7. **Fetch only enabled scans** - Select this option to only fetch scans with the status ‘enabled’.
8. **Insert both CVE and Plugin as Security Findings** - Select this option to enable having both the following behaviors for the Vuln ID field within the Security Findings complex field: add the plugin as a value and split the field by the CVE value.
9. **Parse Netbios name as the asset name. Scan name is the fallback option** - Select this option to use the Netbios name of the asset as the asset name. If it does not exist, the Scan name will be used.
10. **Classify Attack Surface Discovery assets as Domains & URLs** - Select this option to parse Attack Surface Discovery assets as Domains & URLs (instead of parsing them as Devices). This is useful for better organizing and managing your external attack surface.

<Callout icon="📘" theme="info">
  Note

  For details on general advanced settings under the **Adapter Configuration** tab, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

## **Related Enforcement Actions:**

* [Nessus - Add IPs to Scan](/docs/nessus-add-ips-to-scan)
* [Nessus - Delete Account](https://docs.axonius.com/enforcements/docs/nessus-delete-account)
* [Nessus - Add Agent to Agent Group](https://docs.axonius.com/enforcements/docs/nessus-add-agent-to-agent-group)
* [Nessus - Delete Agent](https://docs.axonius.com/axonius-help-docs/docs/nessus-delete-agent)

<br />