# Source: https://docs.axonius.com/docs/okta-update-rule.md

# Okta - Update rule

**Okta - Update Rule** updates rules in Okta for:

* Assets returned by the selected query or users selected on the Users page.

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

* **Use stored credentials from the Okta Adapter** - Select this option to use credentials from the Okta adapter. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Okta](/docs/okta) adapter connection.
</Callout>

* **Rule assets (AQL query)** - Axonius Query Language query that describes the assets to which the rule applies.
* **Group assets (AQL query)** - Axonius Query Language query that describes the assets to which the rule applies.
* **Raw Criteria** - Enter the Okta query that defines which identities are governed by the rule. This will be translated into AQL.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Draft** - Create the rule only in Axonius.
* **Active** - When selected, the rule is created and set to Active status.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Core Okta API](https://developer.okta.com/docs/reference/core-okta-api/).

## Permissions

The value supplied in [Okta API Key](#parameters) must have write or admin permissions.

## Required Ports

Axonius must be able to communicate with the value supplied in [Connection Settings](#Connection-Settings) via the following ports:

* TCP port 443
* TCP port 80

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| Okta 4.5 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).