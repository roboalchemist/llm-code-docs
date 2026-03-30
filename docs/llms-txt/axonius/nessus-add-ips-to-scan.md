# Source: https://docs.axonius.com/docs/nessus-add-ips-to-scan.md

# Nessus - Add IPs to Scan

**Nessus - Add IPs to Scan** adds the IP addresses to an existing Nessus scan for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

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

* **Use stored credentials from the Tenable Nessus adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Tenable Nessus](/docs/tenable-nessus) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Use public IP addresses** - Select to add public IP addresses. This option is useful when needing to scan IP addresses from cloud providers, like AWS.
* **Use private IP addresses** - Select to only add private IP addresses.
* **Use hostnames** - Hostnames from query results will be sent to scan in Nessus.
* **Exclude IPv6 addresses** - When enabled, Axonius will add only IPv4 addresses. Otherwise, both IPv4 and IPv6 addresses will be added.
* **Scan ID** - Scan ID created on Nessus.
* **Source Adapter** - Specify an adapter name as it appears in Axonius to send specific adapter IP data. For example, for the Tenable Nessus adapter, enter `nessus_adapter`. When specified, the Enforcement Action will send adapter IP data only from the specific adapter listed. Otherwise, IP data from all adapters is sent. To find the adapter name, click ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterIcon.png) to go to the Adapters page, view the page for the relevant adapter and in the page URL will be the adapter name in the format `<adaptername>-adapter`.

<Image align="center" alt="Nessus-AdapterURL.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Nessus-AdapterURL.png" />

<Callout icon="💡" theme="warn">
  ## Connection Parameters

  If **Use stored credentials from the Tenable Nessus Adapter** is disabled, these fields are required:

  * **Host Address** - The address of the Nessus host.

  * **Port** - The port to use to connect to the Nessus host.

  * **User Name** and **Password** - The credentials for a user account that has the required permissions to add IP addresses.

  * **Access API Key** and **Secret API Key** - These values must be created in the Tenable.io console. To generate an API key in the Tenable.io console, see [Generate an API Key (Tenable Nessus 10.7)](https://docs.tenable.com/nessus/Content/GenerateAnAPIKey.htm).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [pyTenable 1.4.22](https://pytenable.readthedocs.io/en/stable/) API.

## Required Ports

Axonius must be able to communicate with the values supplied in **Connection Parameters** via the following ports:

* 80
* 443

## Required Permissions

The values supplied in [Connection Parameters](#connection-parameters) above must have permission to write. See [Tenable Permissions](https://developer.tenable.com/docs/permissions) for more information.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).