# Source: https://docs.axonius.com/docs/lock-device.md

# Jamf Pro - Lock User's Device

**Jamf Pro - Lock User's Device** locks the user's device for:

* Users returned by the selected user query or users selected on the relevant asset page.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Jamf Pro adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Jamf Pro](/docs/jamf-pro) adapter connection.
</Callout>

* **Passcode** - The code pre-configured in Jamf to confirm the requester can run the “lock device” command.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Jamf Domain** - The hostname of the Jamf Pro server. This field format is 'https\://\[instance].jamfcloud.com'.

  * **User Name** and **Password** - The credentials for a user account that has the permissions to perform this Enforcement Action.

  * **HTTP Proxy** and **HTTPS Proxy** (*optional*) - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **Tenant Tag** (*optional*) - Specify a tag name.

  * **Bypass SSO** - Switch on if SSO is enabled and the created user account should be logged directly to Jamf Pro.

  * **2FA Secret Key** (*optional*) - The secret generated in Jamf Pro for setting up 2-factor authentication for the adapter user created to collect SaaS Management data.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).