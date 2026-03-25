# Source: https://docs.axonius.com/docs/push-system-notification.md

# Axonius - Push System Notification

**Axonius - Push System Notification** creates an alert (system notification) in Axonius for:

* Assets returned by the selected query or assets selected on the relevant asset page.

The alert is added to the Findings Center, in the **[Alerts History table](/docs/viewing-finding-information#viewing-the-alerts-of-a-finding)** of a Finding of the selected **Alert Category**.

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

* **Alert Category** - The category in the Findings Center where the Enforcement Action sends system notifications that are created in Axonius. From the dropdown, select one of the available Finding Center categories, such as Cyber Asset Management, Internal System, SaaS Management.

## Additional Fields

These fields are optional.

* **Alert Name** - Type a unique name for the Alert. Otherwise, the Alert is assigned the default name.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).