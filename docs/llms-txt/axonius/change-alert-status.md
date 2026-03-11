# Source: https://docs.axonius.com/docs/change-alert-status.md

# Axonius - Change Alert Status

**Axonius - Change Alert Status** changes the status of:

* Finding alert assets returned by the selected query or selected on the Finding Alerts page.

<Callout icon="📘" theme="info">
  Note

  The status changes on the Finding alerts assets as well as in the Findings module.
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

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Change status to** - From the dropdown, select one of the following statuses: **Open**, **In Progress**, **Closed**, or **Canceled**

For more details about other enforcement actions available, see [Action Library](/docs/action-library).