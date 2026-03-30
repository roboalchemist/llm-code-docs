# Source: https://docs.axonius.com/docs/palo-alto-networks-cortex-xdr.md

# Palo Alto Networks Cortex XDR

Palo Alto Networks Cortex XDR is a detection and response app that natively integrates network, endpoint, and cloud data to detect threats and stop sophisticated attacks.

### Asset Types Fetched

* Devices, Aggregated Security Findings, Users, Software, Roles, Groups, SaaS Applications, Alerts/Incidents

## Before You Begin

**Ports**

* TCP port 80/443

**Authentication Method**

* API Key ID / API Key

### APIs

Axonius uses the [Cortex XDR APIs](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Cortex-XDR-API-Overview).

For details on generating an **Advanced Security Level API**,  see [Get Started with Cortex XDR APIs](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-Cortex-XDR-APIs).

### Permissions

The value supplied in [API Key](#required-parameters) must be associated with credentials that have permissions for the following in order to fetch assets:

**Assets**:
Network config - View

Compliance - View

Asset Inventory - View

**Endpoint**:
Endpoint Admin - View,

(View/Edit for EC)

<Callout icon="📘" theme="info">
  Note

  To fetch assets from XDR version 4.x and above, or the XSIAM product, you must have the **Endpoint Admin - Agent Administrations** permission.
</Callout>

Device Control - View,  (View/Edit for EC)

**Incident Response**
Investigations

Query Center - View

Personal Query Library - View

Host Insights - View

## Connecting the Adapter in Axonius

To connect the adapter in Axonius, provide the following parameters:

### Required Parameters

1. **Cortex XDR Domain** - The hostname of the Palo Alto Networks Cortex XDR API server. Example: `api-CUSTOMER.xdr.us.paloaltonetworks.com`
2. **API Key ID** and **API Key** - Specify the API key and the API key ID of an **Advanced Security Level API**, as generated in Cortex XDR app. A standard API key will not work — this integration requires an Advanced Security level API key. For more details on generating an Advanced Security Level API, see [Get Started with Cortex XDR APIs](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-Cortex-XDR-APIs).

![Palo Alto Networks Cortex XDR](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Palo%20Alto%20Networks%20Cortex%20XDR.png)

### Optional Parameters

1. **URL Base Path** - Specify the fully qualified domain name (FQDN). For more details, see [Get Started with Cortex XDR APIs](https://docs-cortex.paloaltonetworks.com/r/Cortex-XDR-REST-API/Get-Started-with-Cortex-XDR-APIs).
2. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).
3. **HTTPS Proxy** - Connect the adapter to a proxy instead of directly connecting it to the domain.

To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adding-a-new-adapter-connection).

## Advanced Settings

<Callout icon="📘" theme="info">
  Note

  Advanced settings can either apply to all connections for this adapter, or to a specific connection. Refer to [Advanced Configuration for Adapters](/docs/advanced-configuration-for-adapters).
</Callout>

1. **Query timeframe configuration in seconds** - Use this setting  to set  a timeframe in seconds to  search in for all XQL queries.
2. **Fetch policies** - Select whether to fetch policies.
3. **Do not fetch devices with disconnected status** - Select to not fetch devices that have the 'Disconnected' status.
4. **Fetch software information** - Select whether to fetch information about installed software.
5. **Fetch daemon information** - Select this option to fetch daemon information for each device.
   1. **XQL filter for daemon records** - When you enable **Fetch daemon information** this field is enabled and you can enter a Custom XQL filter to append to the daemon query. In this way you can can narrow down the daemon query to fetch only the daemons you need. This is useful in large environments.
6. **Fetch DNS information** - Toggle on this option to enrich devices with DNS query information. When you toggle on this option, two additional options are available
   * **XQL timeframe for DNS records** *(optional)* - Specify the XQL for DNS record Timeframe.
   * **XQL filter for DNS records** - Specify the XQL to filter the included DNS records.
7. **Fetch vulnerability information** - Select this option to fetch vulnerability information for devices.
8. **Fetch device users information** - Select this option to fetch a list of users per device.
9. **Fetch device serial number** - Select this option to fetch the device serial number.
10. **Fetch manual protection pause** - Select this option to fetch the manual protection pause field.
11. **Use Cortex XDR in Agent Versions Name** - Select this option to use Cortex XDR in the Agent Versions Name.
12. **Fetch Incidents and Alerts** - Select this option to fetch incidents and alerts.
13. **Fetch XDRC Devices** - Select this option to fetch XCDR devices using the following query:
    ```
    config timeframe=1d
    | dataset = collectoragents
    | filter (Status = """Connected""")
    | fields *
    ```
14. **Different enrichment settings** - Select the following options to enrich Devices with different data types:
    * Listening ports, Fetch running processes, Fetch scheduled tasks, Fetch loaded modules, Fetch browser extensions, recent executables

<Callout icon="📘" theme="info">
  Note

  To learn more about **Adapter Configuration** tab advanced settings, see [Adapter Advanced Settings](/docs/advanced-settings).
</Callout>

### Related Enforcement Actions

* [Palo Alto Networks Cortex XDR - Isolate/Unisolate Assets](/docs/isolateunisolate-in-palo-alto-networks-cortex-xdr)
* [PANW Cortex XDR - Add or Remove Tag to/from Assets](/docs/tag-asset-in-palo-alto-networks-cortex-xdr)
* [PANW Cortex XDR - Run Script](/docs/paloalto-xdr-run-script)
* [PANW Cortex XDR - Scan Endpoints](https://docs.axonius.com/axonius-help-docs/docs/paloalto-xdr-scan-endpoints)