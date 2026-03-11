# Source: https://docs.axonius.com/docs/change-vmware-carbon-black-cloud-policy-by-name.md

# VMware CB Cloud - Change Policy by Name

**VMware CB Cloud - Change Policy by Name**  changes the VMware Carbon Black Cloud (Carbon Black CB Defense) policy assigned to each entity that is the result of the saved query supplied as a trigger (or assets selected in the asset table).

<Callout icon="📘" theme="info">
  NOTE

  To use the **VMware CB Cloud - Change Policy by Name** action, you must successfully configure a [VMware Carbon Black Cloud](/docs/carbon-black-cb-defense) adapter connection.
</Callout>

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

1. **Policy name** *(required)* -  Specify the policy name to be assigned to the endpoint.
2. **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).