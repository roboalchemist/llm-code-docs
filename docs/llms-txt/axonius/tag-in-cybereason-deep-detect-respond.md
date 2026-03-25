# Source: https://docs.axonius.com/docs/tag-in-cybereason-deep-detect-respond.md

# Cybereason Deep Detect & Respond - Add Tag to Assets

**Cybereason Deep Detect & Respond - Add Tag to Assets** adds a specified tag in Cybereason to each device that is retrieved from the saved query supplied as a trigger (or devices that were selected in the asset table).

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

* **Use stored credentials from the Cybereason Deep Detect & Respond adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use the action below, you must successfully configure a [Cybereason Deep Detect & Respond](/docs/cybereason-deep-detect-respond) adapter connection.
  </Callout>

* **Tag name** and **Tag value** - Specify a tag name and value to be added on all relevant entities.

  <Callout icon="📘" theme="info">
    Note

    If the added tag already exists on the device, it will be overridden.
  </Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).