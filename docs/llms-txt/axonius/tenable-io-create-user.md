# Source: https://docs.axonius.com/docs/tenable-io-create-user.md

# Tenable Vulnerability Management - Create User

**Tenable Vulnerability Management - Create User** creates a new user in Tenable Vulnerability Management for:

* Users (only) returned by the selected query or assets selected on the relevant asset page.

## Required Fields

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Tenable Vulnerability Management  adapter** - Enable this option to use credentials from the adapter connection (mandatory). By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Tenable Vulnerability Management](/docs/tenableio) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Draft** - When selected, the user is only created in Axonius.
* **Role Permissions** - Select a role permission from the list to assign to the user.
* **First Name, Last Name, Email, Username** - Additional personal details of the user.
* **First-login password generation method** - Select whether this user should set its first-long password manually, or if this password should be generated automatically.
  * If you select **Manual Password**, enter a value in the **Password** field. The password must meet the following requirements: Minimum length of 12 characters; at least one uppercase letter; at least one lowercase letter; at least one number; and at least one special character (!, @, #, $, %, etc.).

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Tenable Vulnerability Management domain** -  The IP address or hostname of your Tenable Vulnerability Management management server.

  * **Access API key** and **Secret API key** - These values must be created in the Tenable Vulnerability Management console. To generate an API key in theTenable Vulnerability Management console, see [Generate an API Key](https://docs.tenable.com/vulnerability-management/Content/Settings/my-account/GenerateAPIKey.htm).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Justification reason** - Enter the reason for creating this user.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Tenable Create User API](https://developer.tenable.com/reference/users-create). Use the `POST /users` API endpoint.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Administrator \[64] user role

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).