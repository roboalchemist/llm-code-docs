# Source: https://docs.axonius.com/docs/salesforce-update-ticket.md

# Salesforce - Update Ticket

**Salesforce - Update Ticket** updates the indicated tickets in Salesforce for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

* **Use stored credentials from the Salesforce Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Salesforce](/docs/salesforce) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** *(required)* - The full URL of the Salesforce server.

  * **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **User Secret** *(required)* - The Salesforce security token associated with a user account to perform this action.

  * **Consumer Key** *(required)* - A consumer key associated with a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Consumer Secret** *(required)* - A consumer secret associated with a consumer key.

  * **Authentication Flow** - The [authentication method](/docs/salesforce#authentication-methods) used to connect the adapter.
</Callout>

## Ticket Additional Settings

* **Additional fields** - Specify additional fields to be added as key/value pairs in a JSON format.\
  For example:

```json
{"field1": "value1", "field2": "value2"}
```

If one of the specified fields is invalid, the request might fail.

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

<br />

## Ticket Main Settings

* **Ticket Status** - Enter the updated ticket status.
* **Ticket Assignee** - Enter the assignee for the updated tickets.
* **Ticket Comments** - Enter comments to add to the tickets.
* **Ticket IDs To Update** - Ticket IDs are populated from Dynamic Values / IFTTT , or manually input  separated by a comma (,). See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## APIs

Axonius uses the [Salesforce API](https://developer.salesforce.com/docs/atlas.en-us.240.0.chatterapi.meta/chatterapi/quickreference_retrieve_info_for_list_of_users.htm).

## Required Permissions

* The value supplied in **User Name** and **Consumer Key** must have permissions to manage users, as per [Salesforce - Get User Information for Multiple Users](https://developer.salesforce.com/docs/atlas.en-us.240.0.chatterapi.meta/chatterapi/quickreference_retrieve_info_for_list_of_users.htm).

## Version Matrix

This Enforcement Action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| Salesforce 5.0 | Yes       |       |