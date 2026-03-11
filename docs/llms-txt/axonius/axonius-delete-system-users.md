# Source: https://docs.axonius.com/docs/axonius-delete-system-users.md

# Axonius - Delete System Users

**Axonius - Delete System Users** deletes accounts of system users for:

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

* **Action name**  - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** - Not relevant for this action.

* **Use stored credentials from  Axonius Users Adapter** - Select this option to use [Axonius Users](/docs/axonius-users) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Axonius Users](/docs/axonius-users) adapter connection.
</Callout>

* **Abort if user count exceeds the defined limit** *(default: 10)* - Specify the user count limit to abort the action.
  * If the number of users exceeds the specified number, the action is aborted and none of the users are deleted.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Axonius Domain** - The URL for the **Axonius instance**.

  * **API Key** and **API Secret** - An API Key and API Secret associated with a user account that has the [Required Permissions](#required-permissions) to perform this action.. To learn how to obtain an API Key and API Secret, refer to [Get an API Key docs](/docs/api).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

## Required Permissions

The value supplied in [API Key and API Secret](#parameters) must be associated with a user that is assigned to a role with the following permissions:

* User Management: View user accounts and roles, edit users, and delete users

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).