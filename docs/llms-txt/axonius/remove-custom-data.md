# Source: https://docs.axonius.com/docs/remove-custom-data.md

# Axonius - Remove Custom Data from Assets

**Axonius - Remove Custom Data from Assets** removes a custom field from assets returned by the selected query or assets selected on the relevant asset page. For list fields, this Action can also be configured to remove specific values from a list.

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

* **Field name** - Type or select from the dropdown, the custom field name from which to remove the value.

<Callout icon="📘" theme="info">
  Note

  * This action shows all existing custom data fields except for adapter labels.

  * The behavior of removing custom Asset Fields is identical to removing custom Complex Object Fields.
</Callout>

* **Action condition** - From this dropdown, select one of the following:
  * Select *Remove Entire Field* to remove the entire field from all relevant assets.
  * Select *Remove Specific Values* to set specific values to remove from list fields. When you select this option, the **Field value** box appears. Enter the values to remove from the field. If the original tag in the system starts or ends with a space, it will be removed from the system, even if you enter it without a space.

<Callout icon="📘" theme="info">
  Note

  * When you select **Remove Entire Field**:

  * If the selected custom field doesn't exist on the asset, the action succeeds.

  * If the selected custom field already exists on the asset, its value is removed, and the action succeeds.

  * When you select **Remove Specific Values**:

  * If the field is a Date field, you must enter the UTC value.

  * If the field doesn't exist - the action succeeds.

  * If the field is not of the type List - the action fails.

  * If the field does exist, but the value that you want to remove doesn't exist anymore - the action is marked as success.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).