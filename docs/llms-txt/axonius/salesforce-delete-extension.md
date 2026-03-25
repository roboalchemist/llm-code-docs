# Source: https://docs.axonius.com/docs/salesforce-delete-extension.md

# Salesforce - Delete Extensions

**Salesforce - Delete Extensions** deletes extensions in Salesforce for:

* Assets that match the results of the selected saved query, and match the Enforcement Action Conditions, if defined or assets selected on the relevant asset page.

The EC knows which extensions to delete from the adapter name and Extension ID received from entity query.

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

* **Use stored credentials from the Salesforce adapter** - Select this option to use the first connected  adapter credentials.
  * **Select Adapter Connection** - Select which adapter connection to use for this Enforcement Action.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Title** *(default: Axonius-created ticket)* - Enter a title for the case. It is recommended to use a short description of the case as a title. The default title is "Axonius-created ticket".

* **Account ID** - ID of the account associated with this case.

* **Contact ID** - ID of the associated contact.

* **Description** - Enter a description of the case.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Domain** - The full URL of the Salesforce server.

  * **User Name** and **Password** - The credentials for a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **User Secret** - The Salesforce security token associated with a user account toperform this action.

  * **Consumer Key** - A consumer key associated with a user account that has the [Required Permissions](#required-permissions) to perform this action.

  * **Consumer Secret** - A consumer secret associated with a consumer key.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.
</Callout>

## APIs

Axonius uses the [Salesforce Developers](https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/intro_rest_resources.htm?q=query) API.

## Required Permissions

The value supplied in **User Name** and **Consumer Key** must have permissions to manage users, as per [Salesforce - Get User Information for Multiple Users](https://developer.salesforce.com/docs/atlas.en-us.240.0.chatterapi.meta/chatterapi/quickreference_retrieve_info_for_list_of_users.htm).

## Version Matrix

This Enforcement Action has only been tested with the versions marked as supported, but may work with other versions. Please contact [Axonius Support](mailto:support@axonius.com) if you have a version that is not listed and it is not functioning as expected.

| Version        | Supported | Notes |
| -------------- | --------- | ----- |
| Salesforce 5.0 | Yes       |       |

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).