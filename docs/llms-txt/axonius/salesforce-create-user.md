# Source: https://docs.axonius.com/docs/salesforce-create-user.md

# Salesforce - Create User

**Salesforce - Create User** creates a user in Salesforce for

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

* **Use stored credentials from the Salesforce Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Salesforce](/docs/salesforce) adapter.
</Callout>

* **Profile ID** -  The ID for the in Salesforce. To retrieve this ID, in Salesforce GUI, navigate to Setup `>` Users `>` Profiles, and click a profile to populate the ID as a parameter in the URL in the address bar.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

* **Draft** - Select this option to create a draft user.
* **User enabled** - Select this option if you want the created user to be an active user.
* **Time Zone Sid Key** - Time zone sid key address for the created user.
* **Locale Sid Key** - Locale Sid key address for the created user.
* **Email Encoding Key** - Email encoding key address for the created user.
* **First Name** - First name of the created user.
* **Last Name** - Last name of the created user.
* **Email** - Email address for the created user.
* **Username** - Username for the created user.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** *(required)* - The full URL of the Salesforce server.

  * **User Name** and **Password** *(required)* - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **User Secret** *(required)* - The Salesforce security token associated with a user account to perform this action.

  * **Consumer Key** *(required)* - A consumer key associated with a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Consumer Secret** *(required)* - A consumer secret associated with a consumer key.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **2FA Secret Key** - The secret generated in Salesforce for setting up 2-factor authentication for the Salesforce user created for collecting SaaS Management data. For more information on how to generate this secret key, see [Set Up Two Factor Authentication](/docs/salesforce#set-up-two-factor-authentication).

  * **SSO Username** and **Password** - If your organization accesses Salesforce with an SSO provider (such as Google, Microsoft 365, Okta, etc.) enter your credentials for the SSO platform in the SSO Username and SSO Password fields.

  * **Use Unified Login Domain** - Select this option to use the `http://login.salesforce.com` URL for logging in instead of `sub-domain.salesforce.com` (if the main domain is a sandbox, the URL will be `test.salesforce.com`). This allows you to directly login with Salesforce credentials instead of using an external SSO.

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## APIs

Axonius uses the [Salesforce - Create a Record API](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/dome_sobject_create.htm).

## Required Permissions

The value supplied in **User Name** and **Consumer Key** must have permissions to create users in Salesforce users.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).