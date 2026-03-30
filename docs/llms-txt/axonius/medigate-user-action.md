# Source: https://docs.axonius.com/docs/medigate-user-action.md

# Medigate by Claroty - User Actions

**Medigate by Claroty - User Actions** performs one of the selected user actions for:

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

* **Use stored credentials from the Medigate adapter** -  Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Medigate](/docs/medigate) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Medigate Domain** - The full URL of the Medigate server.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action. Use only when accessing with the old API.

  * **API Token** - The API token to use when using the new Medigate API.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Action to perform** - Select the action to perform:
  * **Set Labels** - Fill in these fields:
    * **Labels To Add** - Enter the labels to add.
    * **Labels To Remove** - Enter the labels to remove.
  * **Set Assignees** - Fill in these fields:
    * **Usernames To Add** - Enter the usernames to add.
    * **Usernames To Remove** - Enter the usernames to remove.
  * **Set Notes** - Fill in these fields:
    * **Note** - Enter note text.
    * **Action** - Select whether to append to an existing note or overwrite the existing note.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The values supplied in [Connection Parameters](#connection-parameters) above must have  permissions to perform the selected actions.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).