# Source: https://docs.axonius.com/docs/create-airtable-user.md

# Airtable - Create User

**Airtable - Create User** creates an Airtable user for:

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

<Callout icon="📘" theme="info">
  Note

  To use this Enforcement Action, you must successfully configure an [Airtable Enterprise](/docs/airtable-enterprise) adapter connection.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Airtable Enterprise adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Airtable Enterprise](/docs/airtable-enterprise) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **First Name** - The new user's first name.
* **Last Name** - The new user's last name.
* **Email** - The new users email address.
* **Username** - The username by which the new user will be known in Datadog.
* **First-login password generation method** - The method used to generate the first login password for the user to gain access. When **Manual password** is selected, enter a password in the **Password** field. This password will be used by all new users created by this Enforcement Action until they change it.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP address** *(default: api.airtable.com)* - The hostname or IP address of the Airtable Enterprise server.

  * **Base ID** - Enter the Base ID.

  * **API Secret Key** - The API Secret Key associated with a user account that can create users.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Airtable | Everyone's app platform](https://airtable.com/developers/web/api/create-scim-user) API.

## Required Permissions

The user account connecting to Airtable Enterprise must have Base Editor permissions to perform operations on records:

* `data.records:read`
* `data.records:write`

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).