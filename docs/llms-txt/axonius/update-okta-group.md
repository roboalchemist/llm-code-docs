# Source: https://docs.axonius.com/docs/update-okta-group.md

# Okta - Update Group

**Okta - Update Group** updates a group in Okta for:

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

* **Use stored credentials from the Okta Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Okta](/docs/okta) adapter connection.
</Callout>

* **Name** - The name of the new group.
* **Description** - A description of the new group.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Okta URL**   - The hostname or IP address of the Okta server. This field format is '\[instance].okta.com'.

  * **Authentication** - The type of authentication to use.

  * **Okta API Key (Access via API Token)** - An API key, created in the admin panel. For details, see [Creating an API Token in Okta](/docs/okta#creating-an-api-token-in-okta).

  * **Okta Client ID (Access via OAuth2)** - Client ID of the service app. This is required when OAuth2 is selected in the Authentication drop-down.

  * **Okta JWK Private/Public Keys** - The JSON web key which was generated and assigned in the OAuth 2.0 service app integration in the Admin Console of Okta. This is required when OAuth2 is selected in the Authentication drop-down.

  * **Throttling rate percentage** *(default: 10)* - Specify the threshold percentage of the Okta API rate limit when connecting to the value supplied in Okta URL. Axonius will stop the data fetch when the API rate limit reaches the supplied value.

  * **Number of parallel requests** *(default: 75)* - Specify the maximum parallel requests that will be created when connecting to the value supplied in Okta URL.

  * **Admin URL** - The hostname or IP address of the Okta admin server. This field format is '\[instance]-admin.okta.com'.

  * **Admin Username** - The value you enter in the User Name field in Okta for the new user you created to allow Axonius to fetch SaaS Management data.

  * **Admin Password** - The password you set for the new user in Okta.

  * **2FA Secret Key** - The secret generated in Okta for setting up 2-factor authentication for the Okta user created for collecting SaaS Management data.

  * **SSO Provider** - If your organization uses Okta for SSO, you can set this select this check box (selected by default). For more information, see Connecting your SSO Solution Provider Adapter.

  * **Department Field** *(default: department)* - This is the mapping of the department value for the Okta authentication object. Check if your organization's 'department' value is different from the default value ('department').

  * **User Filter Params** - You can use the Okta Expression language to filter a subset of users (for example, users who belong to specific departments) to be retrieved by the Okta adapter and displayed in Axonius.

  * **Filters users by group name** - Enter a group name to only fetch users from the specific group. Refer to Configuring a Group in Okta for details.

  * **Add users inside the devices** - Select this option to fetch the devices with the users.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Core Okta API](https://developer.okta.com/docs/reference/core-okta-api/).

## Permissions

The value supplied in [Okta API Key](#connection-and-credentials) must have write or admin permissions.

## Required Ports

Axonius must be able to communicate with the following ports:

* TCP port 443
* TCP port 80

## Version Matrix

This adapter has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axoniuscom) if you have a version that is not listed and it is not functioning as expected.

| Version  | Supported | Notes |
| -------- | --------- | ----- |
| Okta 4.5 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).