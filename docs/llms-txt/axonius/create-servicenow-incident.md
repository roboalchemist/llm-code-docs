# Source: https://docs.axonius.com/docs/create-servicenow-incident.md

# ServiceNow - Create Incident

The **ServiceNow - Create Incident** action creates an incident in ServiceNow for:

* Assets returned by the selected query or assets selected on the relevant asset page.

After this Enforcement Action creates the ServiceNow ticket, it returns the unique Incident Sys ID of the newly created ticket as an artifact (*artifact.incidentsysid.incidentsysid*). You can use this artifact within Workflows that run this Enforcement Action by copying it from the **Workflow Data** repository under **Artifacts data**.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ArtifactDataServiceNowCreateIncident.png" />

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

* **Use stored credentials from  ServiceNow adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
</Callout>

* **Incident short description** - Specify the incident title.
* **Incident description** - Specify an incident description.
* **Message severity** - Select the message severity.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **ServiceNow Domain** - URL for the ServiceNow admin panel.

  * **User Name** and **Password** - To connect to ServiceNow, you will need to create a user with action privileges.

  * **OAuth Client ID** and **OAuth Client Secret**   - The OAuth Client ID and Client Secret for OAuth access to ServiceNow. Refer to [OAuth 2.0 with Inbound REST](https://community.servicenow.com/community?id=community_blog\&sys_id=56086e4fdb9014146064eeb5ca961957) for full details on how to obtain the OAuth Token.

  * **OAuth Refresh Token** - When using the OAuth method of authentication, enter the value of the Refresh Token issued by a ServiceNow instance.

  * **OAuth Custom Endpoint Path** - Specify a custom endpoint path to be used instead of the default `oauth_token.do`.

  * **Enable sending OAuth requests as JSON** -  Enable to  to send the request in JSON format instead of the standard `www-form-urlencoded` format.

  * **Apigee URL** - The URL of the domain that the get request is sent to for acquiring APIgee token.

  * **Resource Apigee** - The resources you want the APIgee to access.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.
</Callout>

* **Add link to Saved Query to the incident short description** - When selected, a link to the saved query defined as the trigger for the enforcement set will be appended to the short description of the created incident.
* **Add default incident description** - When selected, Axonius will include the default incident description (mentioned below) in the ServiceNow incident.

  Example message:

  ```
  _Alert - "test" for the following query has been triggered: Missing Sophos_

  _Alert Details_
  _The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query:4
  The previous number of devices was:4_

  _You can view the query and its results here: https://demo-latest.axonius.com/devices?view=Missing Sophos_
  ```
* **Multiple optional incident related settings** - Enter information for the fields you want to add to the incident:
  * **Incident Type**
  * **Caller ID**
  * **Requested for**
  * **Symptom**
  * **Assignment group**
  * **Category**
  * **Subcategory**

<Callout icon="📘" theme="info">
  NOTE

  Since the valid values of the different parameters are customer specific, Axonius does not validate any of those parameters values. You must make sure inserted values are correct, otherwise, the request might fail.
</Callout>

* **Additional fields** - Specify additional fields to be added as part of the incident as key/value pairs in a JSON format.
  For example:
  ```
  {"field1": "value1", "field2": "value2"}
  ```
  * If supplied, Axonius will add the specified fields and values to the created incident. If one of the specified fields is invalid, the request might fail.
  * If not supplied, Axonius will not add any additional fields to the created incident.
* **Send CSV as attachment**
  * If enabled, the created incident will include an attached CSV file with the query results.
  * If disabled, the created incident will not include an attached CSV file with the query results.

<Callout icon="📘" theme="info">
  NOTE

  This field is relevant only for **Create ServiceNow Incident** action and is not part of the **Create ServiceNow Incident Per Entity** action settings.
</Callout>

* **Include only added entities in attached CSV**
  * If enabled, the attached CSV file with the query results will only contain information about the assets added in the trigger query since the previous execution of the enforcement task.
  * If disabled, the attached CSV file with the query results will contain information about all the relevant assets.

<Callout icon="📘" theme="info">
  NOTE

  This checkbox is relevant only when **Send CSV as attachment** is True.
</Callout>

* **Send created incident link to webhook URL** - Specify the webhook URL where the created ServiceNow incident link will be sent.
  * When supplied, Axonius will send the message specified in the **Webhook content** field to the specified webhook URL.
  * When left empty, Axonius will only create the ServiceNow incident.

<Callout icon="📘" theme="info">
  NOTE

  This field is relevant only for **Create ServiceNow Incident** action and is not part of the **Create ServiceNow Incident Per Entity** action settings.
</Callout>

* **Webhook content** - Specify the webhook content in a JSON format.
  * The default webhook content in JSON format is:
    *`{"text": "Created incident link is:<ISSUE_LINK>"}`*
  * When supplied, Axonius sends the specified content to the specified webhook URL. Otherwise, Axonius will only create the ServiceNow incident.

<Callout icon="📘" theme="info">
  NOTE

  * \<ISSUE\_LINK> - will include the ServiceNow incident URL.

  * This field is relevant only for **Create ServiceNow Incident** action and is not part of the **Create ServiceNow Incident Per Entity** action settings.
</Callout>

* **Table name** *(default: incident)* - Specify the ServiceNow table name in which the incident will be created.
* **Wrap request in incident\_object** - Select this option to wrap the outgoing request payload within an "incident\_object" for APIGEE integration.
* **Link created task to another new table record** - Link the newly created incident to another new incident in the table.
  * **Name of table to populate into** *(default: sc\_req\_item)* - Fill in the name of the table.
  * **Field to base a relation on** *(default: request)* - Fill in the field to use as a base for the relation.
  * **JSON entry to send** - Fill the XML value field in ServiceNow.
  * **Create many entries based on "Split by field values"** - Creates a master ticket with one sub-ticket for each Security Finding or installation of the software.
* **Create ticket as flavor** - When selected, flavor ticket updates are fetched using the [ServiceNow Tickets Fetch](https://docs.axonius.com/axonius-help-docs/docs/servicenow-tickets-fetch) adapter.

<Accordion title="Additional CSV Settings" icon="fa-info-circle">
  - **Split by asset entities** - Select to create a CSV file where each asset on a device is shown as a separate row. This separates each asset as the 'expand' option in the application. It separates each asset by its entity. For example, you will be able to know which values were fetched from each adapter connection. If you do not select this option, all values on a device are in the same cell on the CSV file.
  - **Split by field values**  - Choose field value - For complex fields and lists you can create a CSV file where the values of complex fields and lists are represented as separate rows in the file. From the drop-down box select the value that you want to display in the file, 'Tags' for instance. Only fields that have been discovered are available. For example, if you export by Installed Software, you will be able to see each installed Software name and its version.
  - **Don't split complex objects into columns**  - When selected, complex objects appear in a single column in JSON format. By default, each field in a complex object is split into a separate column in the CSV file.
  - **Export CSV delimiter to use for multi-value fields** \*(default: **Export CSV delimiter to use for multi-value fields** field under the **System Settings** section in the **[UI Settings](https://docs.axonius.com/docs/configuring-user-interface-settings)** - Specify a delimiter to separate between values within the same field of an exported CSV file, otherwise the delimiter defined in **Export CSV delimiter to use for multi-value fields** is used.
  - **Maximum rows** *(default: 1048500)* - Specify the maximum number of rows to be included in the CSV file.  When you set a value here the generated CSV file will include the top x rows, based on the specified values. Otherwise, the generated CSV file will include the default maximum rows, set as 1048500.  (note that this value is the maximum value supported by Excel, setting a higher value generates a file that can't be displayed fully or correctly in Excel)
  - **Include associated devices (only for Aggregated Security Findings and Software)** - For Software and Aggregated Security Findings queries. Toggle on this option to include the associated devices with the preferred hostname as a predefined field for each software or Aggregated Security Finding.   When you create a CSV file with associated devices (for Aggregated Security Findings or Software),  if the exported query results are larger than the value set under Maximum rows (or the default value of 1048500), an appropriate notice is displayed at the end of the CSV file.
    * **Device fields** -  This option is available for Software and Aggregated Security Findings. Select the device fields to add. By default Preferred Host Name is selected. Click add to select more fields. At least one field must be selected. Once you select fields, you can drag and drop to rearrange in the order that you want them to appear in the CSV file. Click the bin icon to remove a device field.
  - **Include Associated fetch events (only for Fetch History)** - For Adapter Fetch History queries, select this option to include details of the associated Fetch Events in the CSV file that is created.
  - **Exclude parent complex objects columns** *(default: Disabled)* - Enable this option to hide the parent field of complex fields in exported files.
</Accordion>

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the necessary permissions to perform this enforcement action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).