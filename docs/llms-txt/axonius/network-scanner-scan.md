# Source: https://docs.axonius.com/docs/network-scanner-scan.md

# Axonius Network Discovery - Scan

**Axonius Network Discovery - Scan** scans Devices IP addresses for:

* Assets returned by the selected query or assets selected on the relevant asset page.

Note that Axonius Network Discovery is unable to enrich MAC addresses if the target address is not in the same subnet as the scanning node.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the [Axonius Network Discovery](https://docs.axonius.com/axonius-help-docs/docs/network-scanner) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

    <Callout icon="📘" theme="info">
      To use this option, you must successfully configure a [Axonius Network Discovery](https://docs.axonius.com/axonius-help-docs/docs/network-scanner) adapter connection.
    </Callout>

* **Ports to Scan** *(default: Top 100)* - Set the number of ports to scan, either 'Top 100', 'Top 1000' or `Full’ for all ports (1-65535); or `Custom only' - in this case, only the custom ports listed under **Custom ports to scan** (see [Additioanl Fields](/docs/network-scanner-scan#additional-fields)) are scanned.

* **Fetch certificate data from hosts** - Select whether to disable certificate data fetch from hosts (default) or fetch them in Background Fetch.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Additional Fields

These fields are optional.

* **Ports to Exclude From Scan (Comma Separated)** - Enter a comma separated lists of ports to exclude from the scan.
* **Custom ports to scan (use coma or hyphen)** - You can add custom ports to scan, either specific ports separated by commas, or a range of ports separated by hyphens.
  * If you select Top 100 or Top 1000 in the **Ports to scan** required field, the system will scan those ports, and in addition it will scan any ports listed in this field.
  * If you only want to scan the ports listed in this field, select **Custom only** in the **Ports to scan** drop down.
* **Comma separated list of new DNS resolvers** - Add a comma separated list of DNS resolvers. The system will then use them to get the DNS name of the device from the IP address.
* **Also Enrich Other Adapters Ports** *(default: True)* -  When this option is enabled, ports that were already aggregated in the asset by other adapters are further scanned by the Axonius Network Discovery adapter. This is useful for cases where the transport and application layers were not fully detected in previous enrichments.
* **Timeout for scanning a single device (seconds)** - Enter a number of seconds after which the device scan will time out.

## APIs

Axonius Network Discovery uses the following open source tools:

* [naabu](https://github.com/projectdiscovery/naabu)
* [sx](https://github.com/v-byte-cpu/sx)
* [zgrab2](https://github.com/zmap/zgrab2)
* [p0f](https://lcamtuf.coredump.cx/p0f3/)

For more details about other enforcement actions available, see [Action Library](/docs/action-library).