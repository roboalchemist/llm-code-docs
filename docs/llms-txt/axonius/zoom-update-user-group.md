# Source: https://docs.axonius.com/docs/zoom-update-user-group.md

# Zoom - Update User Group

**Zoom -Update User Group** Updates a user group in Zoom for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from  Zoom adapter** - Select this option to use the first Zoom connected adapter credentials.[Zoom](/docs/zoom)

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Action.

* **Zoom Domain** - The domain for the Zoom account.

* **Group name** - Enter the name of the group you want to update.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Account ID** *(Required)* -  Zoom account ID.

  * **OAuth Client ID** and **OAuth Client Secret** *(Required)* - Zoom uses Server-to-Server OAuth authentication method, enter the Account ID, OAuth Client ID, and OAUth Client Secret to be used to authenticate the request. For more details, see [Create a Server-to-Server OAuth App](https://marketplace.zoom.us/docs/guides/build/server-to-server-oauth-app/#create-a-server-to-server-oauth-app)

  * **Zoom Account ID** - Enter the Zoom Subdomain in the following format: "https//\[account].zoom.us"

  * **User Name** and **Password** *(required)* - The credentials for a user account that has the Required Permissions to perform this action.

  * **2FA Secret Key** - The secret generated in Zoom for setting up 2-factor authentication for the Zoom user created for fetching SaaS data.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Zoom Users](https://developers.zoom.us/docs/api/rest/reference/user/methods/#operation/userUpdate) API.

## Required Ports

Axonius must be able to communicate via the following ports:

* Port 80
* Port 443

## Required Permissions

Only admin users can Update User Groups. Some operations can only be done by Zoom.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).