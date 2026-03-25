# Source: https://docs.axonius.com/docs/akassets-enrichment.md

# Enrich Asset Data - AKAssets

<Callout icon="📘" theme="info">
  This note remains unpublished.
</Callout>

**Enrich Asset Data - AKAssets** runs a AKAssets enriches assets retrieved from the saved query supplied as a trigger (or from the assets selected in the asset table).

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

* **Use stored credentials from the AKAssets adapter** - Select this option to use the first connected AKAssets adapter credentials.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Domain** - The AKAssets domain or IP address.
* **Certificate File** -
* **Key File** -
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the Openapi - AKAssets.json API.

## Required Permissions

The values supplied in [Connection Settings](#parameters) above must have read/write permissions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).