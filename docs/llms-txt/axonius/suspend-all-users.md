# Source: https://docs.axonius.com/docs/suspend-all-users.md

# Axonius - Suspend All Entities in User

**Axonius - Suspend All Entities in User** deactivates all entities in Axonius users returned by the selected query or users selected on the relevant Users page.

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

## Required Permissions

The user account connecting to this Enforcement Action must have permissions to suspend users.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).