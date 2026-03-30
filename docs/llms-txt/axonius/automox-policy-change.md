# Source: https://docs.axonius.com/docs/automox-policy-change.md

# Automox - Change Policy

**Automox - Change Policy** change the Automox policy for:

* Assets that match the selected saved query, and
* Match the Enforcement Action Conditions, if defined.
  or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure an [Automox](/docs/automox) adapter connection.
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

This fields must be configured to run the Enforcement Set.

* **Policy ID** - The Automox policy ID
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).