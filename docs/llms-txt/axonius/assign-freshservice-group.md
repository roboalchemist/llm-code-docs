# Source: https://docs.axonius.com/docs/assign-freshservice-group.md

# Freshservice - Add or Remove User from Group

**Freshservice - Add or Remove User from Group**  adds or removes users from groups in Freshservice for assets retrieved from the saved query supplied as a trigger (or from the assets selected in the asset table).

<Callout icon="📘" theme="info">
  Note

  All Freshservice field names are case sensitive. To check a field name, fetch the asset with a *curl* command and check the RAW data in Axonius. See [Service Desk API for Developers | Freshservice](https://api.freshservice.com/#view_an_asset).
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

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from the Freshservice adapter** - Select this option to use the first connected Freshservice adapter credentials.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a [Freshservice](/docs/freshservice) adapter connection.

  * The API key used for the adapter connection must be for a user with permissions to modify groups.
</Callout>

## Required Fields

These fields must be filled in to run the Enforcement Set.

* **Group IDs (comma separated)** - Enter a comma separated list of group IDs. The users will be added or removed from the identified groups.
* **Add/Remove assignment** - Select the action to perform.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).
  <br />

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Freshservice domain**   - The hostname or IP address of the Freshservice server.

  * **API Key**   – Specify the API Key provided by Freshservice.

  * **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy**  - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Throttle API Requests** -  Select this option to only use 90% of the API total rate limit bandwidth. For example: If a customer has 3000 total API calls allowed per hour, axonius will only produce 2700 calls, and leave the remaining 10% available.
</Callout>

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).