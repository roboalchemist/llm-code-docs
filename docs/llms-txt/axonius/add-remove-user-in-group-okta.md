# Source: https://docs.axonius.com/docs/add-remove-user-in-group-okta.md

# Okta - Add or Remove Users to/from Group

**Okta - Add or Remove Users to/from Group**  adds or removes users to or from an Okta group for each user returned by the selected query or assets selected on the relevant asset page to an Okta group.

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

<Callout icon="📘" theme="info">
  Note

  To use the actions below, you must have Okta users in your Axonius environment.
</Callout>

* **Use stored credentials from the Okta Adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure an [Okta](/docs/okta) adapter connection.
</Callout>

* **Group Member Operation** - Select the operation to perform either 'Add User To Group' or  'Remove User From Group'
* **Group Name** - the name of the group to which the user will be added or removed from.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Authentication** *(default: API Key)* - The type of authentication to use.

  * **Okta API Key (Access via API Token)** - An API key, created in the admin panel. For details, see [Creating an API Token in Okta](/docs/okta#creating-an-api-token-in-okta).

  * **Okta Client ID (Access via OAuth2)** - Client ID of the service app. This is required when OAuth2 is selected in the Authentication drop-down.

  * **Okta JWK Private/Public Keys** - The JSON web key which was generated and assigned in the OAuth 2.0 service app integration in the Admin Console of Okta. This is required when OAuth2 is selected in the Authentication drop-down.

  * **Throttling rate percentage** *(default: 10)* - Specify the threshold percentage of the Okta API rate limit when connecting to the value supplied in Okta URL. Axonius will stop the data fetch when the API rate limit reaches the supplied value.

  * **Number of parallel requests** *(default: 75)* - Specify the maximum parallel requests that will be created when connecting to the value supplied in Okta URL.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Okta Groups API](https://developer.okta.com/docs/reference/api/groups/#response-example-12).

## Permissions

The value supplied in [Okta API Key](#parameters) must have write or admin permissions

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).