# Source: https://docs.axonius.com/docs/create-freshservice-ticket.md

# Freshservice - Create Ticket

**Freshservice - Create Ticket** creates a Freshservice ticket for:

* Assets returned by the selected query or assets selected on the relevant asset page.

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

## Required Fields

These fields are required to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from Freshservice Adapter** - Select this option to use [Freshservice](/docs/freshservice) connected adapter credentials.
  When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure a [Freshservice](/docs/freshservice) adapter connection.
</Callout>

* **Action Choice** - Select the action to perform:
  * Create Ticket
  * Create Change Request
* **Ticket requester email**  - Specify an email address of the requesting person to create the ticket. If no contact exists with this email address in Freshservice, it will be added as a new contact.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional  Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Freshservice domain**  – The hostname of the Freshservice server.

  * **API key**   – Specify the API Key provided by Freshservice.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **Throttle API Requests** -  Select this option to only use 90% of the API total rate limit bandwidth. For example: If a customer has 3000 total API calls allowed per hour, axonius will only produce 2700 calls, and leave the remaining 10% available.
</Callout>

* **Create Incident API version** - Select the version of Freshservice API to use to create the ticket. V1 of the FreshService API is deprecated, and will no longer be supported after May 2023.
* **Subject** *(default: Axonius-created incident)* - Specify the ticket title.
* **Ticket description** *(default: Incident created by axonius)* - Specify a ticket description.
* **Priority** *(default: low)* - Specify the ticket priority:  low, medium, high, or urgent.
* **Group Name or Group ID** - Specify a group ID or group name to which the ticket should be assigned. When you choose a group name, Axonius will search all groups for the group ID with the specific name. Searching for the group ID is only supported if the   credentials of the EC user are Super Admin.​
* **Ticket Category** *(free text)* - Some groups have a category validation, and this field may be required.
* **Custom fields (JSON format)** -   Custom fields to add to this incident described in the following JSON format:

```json
`{"customfieldXYZ":{"value":"VALUE YOU WANT"}} or {"customfieldXYZ"{"id""ID YOU WANT"}}`
```

<Callout icon="📘" theme="info">
  Note:

  If a custom field is already configured by this Enforcement Action, the new custom value is ignored.
</Callout>

* **Add default ticket description** - Select whether to send the configured default ticket description to Freshservice.

<Callout icon="📘" theme="info">
  Message example

  Alert - "test" for the following query has been triggered: Missing Sophos

  Alert Details
  The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query: 4
  The previous number of devices was: 4

  You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos
</Callout>

* **Add Asset names to description** - The names of the assets included in the ticket will be inserted into the ticket description, separated by a comma.
* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).