# Source: https://docs.axonius.com/docs/disable-users-in-okta.md

# Okta - Disable Users

**Okta - Disable Users** can suspend, deactivate or delete each user returned by the selected query or assets selected on the relevant asset page.

<Callout icon="📘" theme="info">
  Note

  To use this action, you must have Okta users in your Axonius environment.
</Callout>

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

* **Action to perform on Okta Users** - Select the action to perform on the Okta users, either to suspend, deactivate or delete the users.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Okta URL**   - The hostname or IP address of the Okta server. This field format is '\[instance].okta.com'.

  * **Okta API Key**   - An API key, created in the admin panel. For details, see [Creating an API Token in Okta](/docs/okta#creating-an-api-token-in-okta).

  * **Number of parallel requests** *(default: 75)* - Specify the maximum parallel requests that will be created when connecting to the value supplied in Okta URL.

  * **API rate limit threshold percentage** *(default: 10)* - Specify the threshold percentage of the Okta API rate limit when connecting to the value supplied in Okta URL. Axonius will stop the data fetch when the API rate limit reaches the supplied value.

  * **HTTPS Proxy**  - A proxy to use when connecting to the value supplied in **Okta URL**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

## APIs

Axonius uses the [Core Okta API](https://developer.okta.com/docs/reference/core-okta-api/).

## Permissions

The value supplied in [Okta API Key](#connection-and-credentials) must have write or admin permissions

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