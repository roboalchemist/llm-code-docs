# Source: https://docs.axonius.com/docs/update-tickets-servicenow.md

# ServiceNow - Update Tickets

**ServiceNow - Update Tickets** modifies existing tickets in ServiceNow that are related to:

* Assets matching the Enforcement Set query or assets selected on the relevant asset page. For example, if the action is triggered on asset type=Users, the action updates tickets linked to each user.
  * When triggered on any asset type except Tickets (for example, Users, Devices), this action updates related ServiceNow tickets based on your selection in the **Select Which Related Tickets To Update** dropdown (see below).
  * When triggered on asset type=Tickets, this action runs on all tickets resulting from the selected query. The **Select Which Related Tickets To Update** dropdown is not applicable in this scenario.

<Callout icon="📘" theme="info">
  Note

  The ServiceNow API returns a 200 status code upon successful procession of the request. However, if the syntax of a field like incident\_state is incorrect (for example, has a lowercase first letter), the update fails without any error message from the API. Therefore, it is crucial to ensure that all field values passed to ServiceNow adhere to the correct syntax. To mitigate this, you can write a JSON expression in **Additional fields (json format)** under the [**Additional Fields** section](#additional-fields) below to precisely define the values being sent, including case sensitivity.
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

* **Use stored credentials from ServiceNow adapter** - Select this option to use the [ServiceNow](/docs/servicenow) connected adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
</Callout>

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Connection And Credentials

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **ServiceNow Domain** - The full URL for your ServiceNow instance.

  * **User Name** and **Password** - To connect to ServiceNow, you need to create a user with action privileges to create and manage assets.

  * **OAuth Client ID** and **OAuth Client Secret** - The credentials for OAuth-based access to ServiceNow. Refer to [OAuth 2.0 with Inbound REST](https://community.servicenow.com/community?id=community_blog\&sys_id=56086e4fdb9014146064eeb5ca961957) for full details on how to obtain the OAuth Token.

  * **OAuth Refresh Token** - When using the OAuth method of authentication, enter the value of the Refresh Token issued by a ServiceNow instance. This token is used to obtain new access tokens without requiring the user to reauthenticate.

  * **OAuth Custom Endpoint Path** - Specify a custom endpoint path to be used instead of the default `oauth_token.do`.

  * **Enable sending OAuth requests as JSON** -  Enable sending the request in JSON format instead of the standard `www-form-urlencoded` format.

  * **Apigee URL** - The URL of the domain that the GET request is sent to for acquiring the Apigee token.

  * **Resource Apigee** - The specific resources that the Apigee token is configured to access.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

## Ticket Additional Settings

These fields are optional.

* **Additional fields (json format)** - Specify additional ServiceNow fields and their values as key/value pairs in JSON format. This is particularly useful for setting fields that are not explicitly listed above or for ensuring the correct syntax (including case sensitivity) of values such as incident\_state.

  Example:

  ```
   { "close_notes" : "Vulnerability Remediated by Axonius EC Action",
  "incident_state" : "Resolved",   
   "close_code": "Duplicate" }

  ```
* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

<Callout icon="📘" theme="info">
  Note

  When **Fetch dynamic dropdown values** is enabled for the ServiceNow adapter connection, **Placeholder text fields** (within the Field Mapping Wizard) will be populated with the available field names from ServiceNow.
</Callout>

## Ticket Main Settings

These fields are optional.

* **Ticket Status** - The status to set for the ServiceNow ticket.

<Callout icon="📘" theme="info">
  Note

  To populate the available options in the **Ticket Status** dripdown directly from the ServiceNow adapter, enable the **Fetch dynamic dropdown values** option in your ServiceNow adapter's **Advanced Configuration**.
</Callout>

* **Ticket Assignee** - The ServiceNow user assigned to process the ticket.

* **Ticket Comments** - Free-form text to add as a comment in the ServiceNow ticket.

* **Select Which Related Tickets To Update** - Relevant when this enforcement action runs on an asset category other than Tickets. Select which tickets to update.

* **Update tickets using CSV attachment** - When enabled, the CSV attachment on an existing ticket will be updated with a new CSV file. The old file is overwritten.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

<br />

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).