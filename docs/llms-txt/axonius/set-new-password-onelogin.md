# Source: https://docs.axonius.com/docs/set-new-password-onelogin.md

# Set a New Password for User - OneLogin

**Set a New Password for User - OneLogin** creates a password for a user in OneLogin for:

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

* **Use stored credentials from OneLogin adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [OneLogin](/docs/onelogin) adapter connection.
</Callout>

* **New Password** - The new password set for the OneLogin user.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** -The hostname or IP address of the OneLogin server that Axonius can communicate with.

  * **Client ID** and **Client Secret**  - The credentials for a user account that has the permissions to perform this action.

  * **SSO Provider** - If your organization uses OneLogin for SSO, you can set this select this check box (selected by default). For more information, see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

* **Add comment field** - Enter a comment text to add event data to the user record. The default text is "User has been modified by Axonius". You can change it (for example -  "A new password was set").
* **Append the comment provided to the already existing comment** *(default: false)* - Select this option to append the comment provided in **Add comment field** to the existing comment instead of replacing it. If you leave this field unselected, the provided comment will replace the existing comment.
* **Add Date and Time to Comment** *(default: false)* - Select this to add date and time to the comment provided in **Add comment field**.

## APIs

Axonius uses the [OneLogin API](https://developers.onelogin.com/api-docs/1/users/set-password-in-cleartext).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

## Version Matrix

This Enforcement Action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version       | Supported |
| ------------- | --------- |
| OneLogin v1.0 | Yes       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).