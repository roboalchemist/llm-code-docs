# Source: https://docs.axonius.com/docs/tag-rapid7-nexpose-insightvm-assets.md

# Rapid7 - Add or Remove Tag to/from Assets

**Rapid7 - Add or Remove Tag to/from Assets** adds or removes the supplied tag name to or from the Rapid7 Nexpose and InsightVM assets returned by the selected query or assets selected on the relevant asset page.

This action only supports Rapid7 Nexpose and InsightVM assets (the blue adapter), i.e. assets that have a *nexpose\_Adapter.id* field.

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

* **Use stored credentials from the Rapid7 Nexpose and InsightVM adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this action, you must successfully configure a [Rapid7 Nexpose and InsightVM](/docs/rapid7-nexpose) adapter connection.
  </Callout>

* **Tag name** - Specify the tag to be add/removed to or from Rapid7 InsightVM assets. Tags that you specify to add **must already exist** in Rapid7.

* **Add or remove tag** - Select the action type:
  * **Add tag** - to add tags.
  * **Remove tag** - to remove tags.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Create tag if it does not exist** - When enabled, if a tag is not found by the name specified for **Tag name** it will be created. This option only applies when **Add Tag** is selected.

  <Callout icon="📘" theme="info">
    Note

    Tags created in this manner have their type set to "custom" when the field **Add Tag type** (see below) is empty. If the **Add Tag type** field has a value, the tag type will use that value.
  </Callout>

* **Add Tag type** - Enter a tag type to add, for example: Owner, Location, etc.

* **Remove tag type** - Enable to remove the "tag type" attribute from the assets.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).