# Source: https://docs.axonius.com/docs/gsuite-remove-users-from-group.md

# Google Workspace - Remove Users From Group

**Google Workspace - Remove Users From Group** removes users from a Google Workspace group for:

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

* **Group email address**  - The email address of the Google Workspace group from which the member will be removed.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Email of an admin account to impersonate** - The email of your Google Workspace admin.

  * **Account Profile Name** - Google user name for retrieving SaaS data. [https://admin.google.com/ac/accountsettings/profile](https://admin.google.com/ac/accountsettings/profile)

  * **JSON Key pair for the service account** - Upload the JSON file you created for your service account. For more details, refer to [Google Workspace ](/docs/g-suite-by-google) adapter.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Google Workspace - Directory API: Group Members](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members/delete).

## Required Permissions

This action requires permission to remove a user from a group.

Also, this action requires that you enter the following scope in your Google account's [Domain Wide Delegation](https://admin.google.com/ac/owl/domainwidedelegation?hl=en) for the Client ID used for this connection (inside the JSON file):
'[https://www.googleapis.com/auth/admin.directory.group](https://www.googleapis.com/auth/admin.directory.group)'

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).