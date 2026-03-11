# Source: https://docs.axonius.com/docs/gsuite-change-browser-ou.md

# Google Workspace - Change Browser OU

**Google Workspace - Change Browser OU** moves a web browser into an OU in Google Workspace for:

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

* **Use stored credentials from Google Workspace adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Google Workspace](/docs/g-suite-by-google) adapter connection.
</Callout>

* **ORG Unit Path** - The path to the OU into which you want to move the web browser. The format must contain all levels of the OU hierarchy separated by a "/" character starting with the root level (which is represented by the "/" character).
  If you need to move the users to the root OU, enter only the / character in this field.
  ![GoogleOUs](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/GoogleOUs.png)

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Email of an admin account to impersonate** - The email of your Google Workspace admin.

  * **JSON Key pair for the service account** - Upload the JSON file you have created for your service account. For more details, refer to [Google Workspace ](/docs/g-suite-by-google) adapter.

  * **Get OAuth Apps** - Select this option to fetch the OAuth applications used by each user.

  * **Fetch Cloud Identity Devices** - Select this option to fetch Cloud Identity devices.

  * **Fetch Chrome Browsers** - Select this option to fetch Chrome browsers information.

  * **Fetch Calendars** - Select this option to fetch users' calendars.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to fetch assets.

  * **Login URL** - The hostname or IP address of the Google server.

  * **2FA Secret Key** - The secret generated in Google Workspace for setting up 2-factor authentication for the Google Workspace user created for collecting SaaS Management data.

  * **SSO Provider** - If your organization uses Google Workspace for SSO, you can select this check box. For more information, see [Connecting your SSO Solution Provider Adapter](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).

  * **Proxy address** - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Proxy port** - The port for the proxy server.

  * **Proxy username** - The user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in Proxy address.

  * **Proxy password** - The password to use when connecting to the server using the Proxy.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Google Workspace - Manage user accounts API](https://developers.google.com/admin-sdk/directory/v1/guides/manage-users).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* The **Get OAuth Apps** option requires addition of the following scope to your Google Workspace (G Suite) admin account: **[https://www.googleapis.com/auth/admin.directory.user.security](https://www.googleapis.com/auth/admin.directory.user.security)**

* The **Fetch Cloud Identity Devices** option requires the following:

  * Addition of the following scope to your Google Workspace (G Suite) admin account: **[https://www.googleapis.com/auth/cloud-identity.devices.readonly](https://www.googleapis.com/auth/cloud-identity.devices.readonly)**
  * Enabling the Cloud Identity API.

* The **Fetch Chrome Browsers** option requires an additional privilege to your Google Workspace (G Suite) admin account: **[https://www.googleapis.com/auth/admin.directory.device.chromebrowsers.readonly](https://www.googleapis.com/auth/admin.directory.device.chromebrowsers.readonly)**

* The **Fetch Calendars** option requires the following:

  * An additional privilege to your Google Workspace (G Suite) admin account: **[https://www.googleapis.com/auth/calendar](https://www.googleapis.com/auth/calendar)**

  * Enabling the Cloud Identity API.

For more information on adding a privilege/scope to your Google Workspace (G Suite) admin account, refer to [Configure the OAuth Scopes](/docs/g-suite-by-google#6).
For more information on enabling the Cloud Identity API, refer to [Enable Cloud API](/docs/g-suite-by-google#4).

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).