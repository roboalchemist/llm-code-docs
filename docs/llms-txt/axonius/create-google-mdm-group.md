# Source: https://docs.axonius.com/docs/create-google-mdm-group.md

# Google Workspace - Create Group

**Google Workspace - Create Group** creates a new group in the Google Workspace for:

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

* **Use stored credentials from Google Workspace (G Suite) adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Google Workspace](/docs/g-suite-by-google) adapter connection.
</Callout>

* **Name** - The group name.
* **Description** - A description of the group.
* **Email** - The email address of the admin responsible for the group.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Email of an admin account to impersonate** - The email of your Google Workspace (G Suite) admin. The address must be an actual email address of an admin user that is associated with the service principal that was created.

  * **Account Profile Name** - Google user name for retrieving SaaS data. [https://admin.google.com/ac/accountsettings/profile](https://admin.google.com/ac/accountsettings/profile)

  * **JSON Key pair for the service account** - Upload the JSON file you created for your service account. For more details, refer to [Google Workspace ](/docs/g-suite-by-google) adapter.

  * **Get OAuth Apps** - Select this option to fetch the OAuth applications used by each user.

  * **Fetch Cloud Identity Devices** - Select this option to fetch Cloud Identity devices.

  * **Fetch Chrome Browsers** - Select this option to fetch Chrome browsers information.

  * **Fetch Calendars** - Select this option to fetch users' calendars.

  * **Username** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Login URL** *(default: `https://accounts.google.com`)* - The hostname or IP address of the Google server.

  * **2FA Secret Key** - The secret generated in Google Workspace for setting up 2-factor authentication for the Google Workspace user created for collecting SaaS Management data.

  * **SSO Provider** - If your organization uses Google Workspace for SSO, you can select this checkbox. For more information, see [Connecting your SSO Solution Provider](/docs/adding-a-new-adapter-connection#connecting-your-sso-solution-provider-adapter).

  * **Proxy address** - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Proxy port** - The port for the proxy server.

  * **Proxy username** - The user name to use when connecting to the value supplied in Host Name or IP Address via the value supplied in Proxy address.

  * **Proxy password** - The password to use when connecting to the server using the Proxy.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Manage roles  |  Admin console  |  Google for Developers ](https://developers.google.com/admin-sdk/directory/v1/guides/manage-roles#get_existing_roles) API.

## Required Permissions

This enforcement action requires the following permissions:

* [Authentication Scope](https://www.googleapis.com/auth/admin.directory.rolemanagement)

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).