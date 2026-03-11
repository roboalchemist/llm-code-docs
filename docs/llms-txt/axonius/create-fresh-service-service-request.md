# Source: https://docs.axonius.com/docs/create-fresh-service-service-request.md

# Freshservice - Create Service Request per Asset

**Freshservice - Create Service Request**  creates a service request in Freshservice for each of the:

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

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from Freshservice Adapter** - Select this option to use [Freshservice](/docs/freshservice) connected adapter credentials.
  When you select this option, the **Select Adapter Connection** drop-down is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure a [Freshservice](/docs/freshservice) adapter connection.
</Callout>

* **Ticket requester email** - Specify an email address of the requesting person to create the ticket. If no contact exists with this email address in Freshservice, it will be added as a new contact.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

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

* **Create Incident API version** - Select the version of Freshservice API to use to create the ticket. The default is V2.
* **Subject** *(default: Axonius-created incident)* - Specify the ticket title.
* **Ticket description** *(default: Incident created by Axonius)* - Specify a ticket description.

<Callout icon="📘" theme="info">
  Message example

  Alert - "test" for the following query has been triggered: Missing Sophos

  Alert Details
  The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query: 4
  The previous number of devices was: 4

  You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos
</Callout>

* **Priority** *(default: low)* - Select the ticket priority: low, medium, high, urgent.
* **Group Name or Group ID** - Enter a Group Name or Group ID the ticket should be assigned to. When you choose group name, Axonius will search all groups for the group ID.
* **Ticket Category** *(free text)* - Some groups have a category validation, and this field may be required.
* **Custom fields (JSON format)** -   Custom fields to add to this incident described in the following JSON format:

```json
`{"customfieldXYZ":{"value":"VALUE YOU WANT"}} or {"customfieldXYZ"{"id""ID YOU WANT"}}`
```

<Callout icon="📘" theme="info">
  Note:

  If a custom field is already configured by this Enforcement Action, the new custom value is ignored.
</Callout>

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Permissions

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).