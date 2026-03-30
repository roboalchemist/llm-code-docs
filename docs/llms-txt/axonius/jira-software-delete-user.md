# Source: https://docs.axonius.com/docs/jira-software-delete-user.md

# Jira Software - Delete User

<Callout icon="💡" theme="warn">
  Note

  In addition, this Enforcement Action requires the Jira Service Management (JSM) Standard, Premium, or Enterprise license and is not supported for free plans with the same capabilities.
</Callout>

**Jira Software - Delete User** deletes a user in Atlassian (formerly Jira Software) for each asset that matches the parameters of the selected saved query, and the other Enforcement Action settings or the assets selected on the relevant asset page.

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

* **Use stored credentials from Atlassian (formerly Jira Software) adapter** - Select this option to use the [Atlassian adapter](/docs/atlassian-jira-software) credentials.

  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

## Required Fields

These fields are required to run the Enforcement Action.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** - The full URL of the Jira server.

  * **User Name** - The user name for a user account that has the [Required Permissions](#required-permissions) to perform this Enforcement Action. Use only when accessing with the old API.

  * **API Token** - The API token to use when using the Jira API.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Jira API Version** *(default: V3)* - Select your Jira API version.

  * **Atlassian Admin API - Organization ID** and **Atlassian Admin API - API key**  - The organization ID and an organization API key generated for fetching SaaS data. Needed for fetching organizational data.

  * **Password** - The password for the Atlassian user account. Needed for fetching Settings from Atlassian.

  * **2FA Secret Key** - If you access Atlassian through an SSO solution that requires two-factor authentication, and you want to fetch Settings from Atlassian, you will need to  generate a secret key in that solution and paste it here. See instructions for performing this action in [Okta](/docs/okta#step-5-enable-multifactor-authentication-saas-management).
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<EC_Set_Scheduling />

## APIs

Axonius uses the [Jira Cloud Platform](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-users/#api-rest-api-3-user-delete) REST API.

## Permissions

The credentials used to connect to Atlassian must have the permissions needed to delete users in Atlassian.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).