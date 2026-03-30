# Source: https://docs.axonius.com/docs/create-incident-pagerduty.md

# Create Incident - PagerDuty

**Create Incident - PagerDuty** creates an incident in PagerDuty for:

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
* **Split Tickets By** - When enabled, group assets into different tickets based on a shared attribute. Click the adapter icon to select an adapter (or Aggregated), and then click the **Select Adapter Field** box to select the asset field used to generate a separate ticket for each unique value.

  <Callout icon="📘" theme="info">
    Note

    * The **Split Tickets By** option appears only in ticket creation actions, and does not appear in ticket-per-asset creation or ticket update actions.
    * For assets containing multiple values, the system uses only the first value to perform the split.
  </Callout>

<br />

* **Use stored credentials from the PagerDuty adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a [PagerDuty IT Service Management](/docs/cherwell) adapter connection.

  * The user name and the password used for the adapter connection must be user with permissions to create new incidents.
</Callout>

* **Title** - Specify an incident title.
* **Requester Email** - The email of the user requesting the incident.
* **Service ID** - The ID of the service associated with the incident.
* **Service Type** - The type of service associated with the incident.
* **Priority ID** - The ID of the priority value.
* **Priority Type** *(required, default: 5)* - Specify the incident priority.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

<Callout icon="📘" theme="info">
  Note

  Valid Service and Priority IDs can be attained using these webpages with a valid API token:

  * [Service IDs](https://developer.pagerduty.com/api-reference/0fa9ad52bf2d2-list-priorities)

  * [Priority IDs](https://developer.pagerduty.com/api-reference/e960cca205c0f-list-services)

  It is recommended to use the user token of an administrator to get these IDs.
  In PagerDuty, go to **User Profile** `>` **Account Settings** `>` **User Token**.
</Callout>

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address** *(required, default: api.pagerduty.com)* - The hostname or IP address of the PagerDuty server that Axonius can communicate with via the [Required Ports](/docs/pagerduty#required-ports).

  * **Token** *(required)* - An API Key associated with a user account that has the [Required Permissions](/docs/pagerduty#required-permissions) to perform this action. The API token for this adapter is static and in power of the PagerDuty user

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Gateway Name** -  Select the Gateway through which to connect to perform the action.
</Callout>

* **Urgency** - Select the urgency level from the list.

* **Brief Description** - Specify an incident description.

* **Add default ticket description** - Select whether to send the incident description to PagerDuty.
  * If enabled, Axonius will include the default incident description (mentioned below) in the PagerDuty incident.
  * If disabled, Axonius will not include the default incident description (mentioned below) in the PagerDuty incident.

* **Allow fields with multiple values in the field mapping** - When selected, allows parsing multiple Axonius values into one vendor field (many to one) while concatenating the values with a separator "|".
  For example:
  * If the field mapping is: "description: \<Host Name>, description: \<Mail>"

  * Then the output will be: "description: \<Host Name>|\<Mail> "

* **Map Axonius fields to adapter fields** - Use the **Field Mapping Wizard**   to map Axonius fields to fields in external systems. In this way, you can transfer data found in Axonius into the external system as part of the configuration of relevant enforcement actions. The wizard shows you which fields exist on the Axonius system, allowing you to map them easily.

<Callout icon="📘" theme="info">
  Note:

  For details, see <Anchor label="Axonius to External Field Mapping" target="_blank" href="https://docs.axonius.com/docs/axonius-to-cmdb-field-mapping#/">Axonius to External Field Mapping</Anchor>.
</Callout>

## APIs

Axonius uses the [PagerDuty API](https://developer.pagerduty.com/api-reference/a7d81b0e9200f-create-an-incident).

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

`incidents.write`

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).