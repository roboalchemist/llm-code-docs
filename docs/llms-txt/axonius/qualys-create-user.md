# Source: https://docs.axonius.com/docs/qualys-create-user.md

# Qualys - Create User

**Qualys - Create User** creates a new user in Qualys for:

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

* **Use stored credentials from the Qualys Cloud Platform adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Qualys Cloud Platform](/docs/qualys-cloud-platform) adapter connection.
</Callout>

* **User Role** - Provide the user's role: Manager, Unit Manager, Scanner, Reader, Contact, or Administrator.
* **Business Unit** - Specify the user's business unit.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Draft** - When enabled, changes are made within Axonius only.
* **Use enforcement field value only if asset value is missing** - When enabled, the Enforcement field values are used only if there they have no value in the asset itself.
* Add different user details such as First and Last Name, Job Title, Email Address, etc.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Qualys Cloud Platform domain** - The full URL of the Qualys Cloud Platform server.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **OpenID Token** - See [Qualys Onboarding Process](https://docs.qualys.com/en/tc/api/get_started/get_started.htm) for details on how to obtain this token.

  * **Qualys Tags Include List** - Specify a comma-separated list of Qualys tags. When supplied, the connection for this adapter will only fetch devices tagged in Qualys with the tags provided in this list.

  * **API Rate Limit (Requests per Hour)** - Specify a rate limit for the number of requests per hour to be sent to Qualys. Note that this setting is applicable only for the Global IT Asset Inventory API.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Qualys Add User API](https://docs.qualys.com/en/vm/api/users/users/add_user.htm).

## Required Ports

Axonius must be able to communicate via the following ports:

* HTTPS port 443

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* One of the following roles: Manager, Administrator, or Unit Manager.
  * **Manager**: Can add or edit any user account in the subscription (no limitations).
  * **Administrator**: Can add or edit user accounts, except for those with a Manager or Administrator role.
  * **Unit Manager**: Can add or edit user accounts only within their own business unit; cannot manage users outside their unit.

<Callout icon="📘" theme="info">
  Note

  When configuring the connection to use for this action, ensure the account’s role matches the intended operation and be aware of each role’s scope and limitations.
</Callout>

## Version Matrix

This Enforcement Action was tested only with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version          | Supported | Notes |
| ---------------- | --------- | ----- |
| Qualys API v2.0+ | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).