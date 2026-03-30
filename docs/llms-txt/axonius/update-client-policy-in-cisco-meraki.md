# Source: https://docs.axonius.com/docs/update-client-policy-in-cisco-meraki.md

# Cisco Meraki - Update Client Policy

**Cisco Meraki - Update Client Policy** updates the Client Policy in Cisco Meraki for each of the entities that are the result of the saved query supplied as a trigger (or devices selected in the asset table).

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

* **Use stored credentials from Cisco Meraki adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Cisco Meraki](/docs/cisco-meraki) adapter connection.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Device Policy** - Select a Device Policy. The following policies are available, 'whitelisted', 'blocked', 'normal', 'group policy'.
* **Policy Name** - Enter a Policy Name.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **CiscoMeraki Domain** - The full URL of the Cisco Meraki server.

  * **API Prefix** and **API Key** - If necessary, include how these are generated or obtained.

  * **VLAN Exclude List** - Enter a list of VLANs from which devices are not fetched.

  * **Exclude No VLAN Clients** - Select to not fetch devices which are not associated with a VLAN.

  * **SSID Exclude List** - Specify a comma-separated list of SSIDs.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).