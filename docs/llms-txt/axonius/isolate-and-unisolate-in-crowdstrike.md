# Source: https://docs.axonius.com/docs/isolate-and-unisolate-in-crowdstrike.md

# CrowdStrike Falcon - Isolate and Unisolate Assets

**CrowdStrike Falcon - Isolate**   quarantines each of the assets (endpoints) retreived from the saved query supplied as a trigger (or devices that have been selected in the asset table), from the network.

**CrowdStrike Falcon - Unisolate**  restores full network connectivity to each of the assets (endpoints) retrieved from the saved query supplied as a trigger.

<Callout icon="📘" theme="info">
  NOTE

  To use the actions below, you must successfully configure a [CrowdStrike Falcon](/docs/crowdstrike-falcon) adapter connection.
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

## Isolate in CrowdStrike Falcon

These fields refer to **CrowdStrike Falcon - Isolate**.

### Required Fields

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

### Required Permissions

See [CrowdStrike Falcon adapter - Required Permissions](/docs/crowdstrike-falcon#required-permissions).

## Unisolate in CrowdStrike Falcon

These fields refer to **CrowdStrike Falcon - Unisolate**.

### Required Fields

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

### Required Permissions

See [CrowdStrike Falcon adapter - Required Permissions](/docs/crowdstrike-falcon#required-permissions).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).