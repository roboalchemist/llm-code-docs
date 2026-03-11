# Source: https://docs.axonius.com/docs/epo-add-asset.md

# Trellix ePolicy Orchestrator (ePO) - Add Assets

**Trellix ePolicy Orchestrator (ePO) - Add Assets** adds assets (systems) to a specified Trellix server System Tree group for:

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Trellix ePolicy Orchestrator (ePO) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

  <Callout icon="📘" theme="info">
    Note

    To use this option, you must successfully configure a [Trellix ePolicy Orchestrator (ePO)](/docs/mcafee-epolicy-orchestrator-epo) adapter connection.
  </Callout>

* **Group Name** - Enter the name of the group under which you want to create the assets.

* **Source ID** and **Source Type** - These parameters are arbitrary values for you to provide when you add the systems. They will be stored in the database to record which source detected or added any given system. For example, **Source Type** can simply be 'Axonius'.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host**  - The hostname of the Trellix ePolicy Orchestrator (ePO) server that Axonius can communicate with.

  * **Port**  - Use TCP port 8443.

  * **User** and **Password** - The credentials for a user account that has permissions to fetch assets.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Trellix API](https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide/page/GUID-97D84153-17CF-4482-8586-042887B5D25D.html).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

The account used for this action must have permission to edit groups in Trellix.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).