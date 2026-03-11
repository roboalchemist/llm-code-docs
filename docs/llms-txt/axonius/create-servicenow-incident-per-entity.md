# Source: https://docs.axonius.com/docs/create-servicenow-incident-per-entity.md

# ServiceNow - Create Incident per Asset

**ServiceNow - Create Incident per Asset** creates an incident in ServiceNow for **each** entity that matches the parameters of the saved query supplied as a trigger (or from the entities selected in the asset table).

After this Enforcement Action creates a ServiceNow ticket for an asset, it returns the unique Incident Sys ID of the newly created ticket as an artifact (*artifact.incidentsysid.incidentsysid*). You can use this artifact within Workflows that run this Enforcement Action by copying it from the **Workflow Data** repository under **Artifacts data**.

<Image alt="ArtifactDataServiceNowCreateIncidentperAsset.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ArtifactDataServiceNowCreateIncidentperAsset.png" />

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

* **Use stored credentials from  ServiceNow adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  NOTE

  To use this option, you must successfully configure a [ServiceNow](/docs/servicenow) adapter connection.
</Callout>

* **Incident short description** - Specify the incident title.
* **Message severity** *(default: info)* - Select the message severity: info, warning or error.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

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

* **Split by field values** - Select a field to split assets by in the Assets table. Each incident will be split into multiple rows where each row lists a single field value - for example, a row with an incident per Security Finding (vulnerability) per Device.

* **Retry Count** *(default: 1)* - If the action fails, Axonius will retry to execute it this many times for each device.

* **Incident description** and **Map Axonius fields to fields in the description** - These fields allow you to create custom incident descriptions.

  * In **Incident description**, enter a description template that includes field placeholders for field mapping. The placeholder is enclosed by double `{{ }}`.
  * Then, in **Map Axonius fields to fields in the description**, enter the field placeholder in **Placeholder text fields** on the left and select an Axonius field in **Axonius fields** on the right. The value of the Axonius field is populated into the description in place of the placeholder text.

  In the example below, the template in **Incident description** maps the fields selected under **Axonius fields** into the placeholders *dev\_hostname*, *dev\_ip*, and *dev\_serial*. Each asset that matches the query parameters will have its data added to the incident description.

  <Image alt="ECDescriptionFieldMapping.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ECDescriptionFieldMapping.png" />

* Multiple optional incident-related settings:
  * **Incident Type**
  * **Caller ID**
  * **Requested for**
  * **Configuration item**
  * **Symptom**
  * **Assignment group**
  * **Category**
  * **Subcategory**

<Callout icon="📘" theme="info">
  Note

  As the valid values of these parameters are customer specific, Axonius does not validate any of these parameter's values. You must make sure inserted values are correct; otherwise, the request might fail.
</Callout>

* **Additional fields** - Specify additional fields to be added as part of the incident as key/value pairs in a JSON format.
  For example:
  ```
  {"field1": "value1", "field2": "value2"}.
  ```
  * If supplied, Axonius will add the specified fields and values to the created incident. If one of the specified fields is invalid, the request might fail.

* **Table name** *(default: incident)* - Specify the ServiceNow table name  in which the incident will be created.
  * If supplied, the incident will be created in the specified table name.
  * If not supplied, the incident will be created in the 'incident' table.

* **Link created task to another new table record** - Link this new task to another table with the following parameters:
  * Name of table to populate into *(default: sc\_req\_item)*
  * Field to base a relation on *(default: request)*
  * JSON entry to send

* **Create many entries based on "Split by field values"** - Creates a master ticket with one sub-ticket for each Security Finding or installation of the software.

* **Axonius to ServiceNow field mapping** - Field mapping allows you to map Axonius fields to the CMDB fields. The input should be key/value pairs in a JSON format.
  For example:
  ```
  {"axonius_field1":"servicenow_field1", "axonius_field2":"servicenow_field2"}
  ```

* **Send CSV data** *(required, default: False)*
  * If enabled, the created issue will include an attached CSV file with the query results.
  * If disabled, the created issue will not include an attached CSV file with the query results.

**Additional CSV Settings**

* **Split by asset entities**  -  Select to create a CSV file where each asset on a device is shown as a separate row. This separates each asset as the 'expand' option in the application. It separates each asset by its entity. For example, you will be able to know which values were fetched from each adapter connection.

  * If supplied, each value on a device or user is shown as a separate row.
  * If not supplied all values on a device are in the same cell on the CSV file.

* **Export CSV delimiter to use for multi-value fields** *(default:**Export CSV delimiter to use for multi-value fields** field under the **System Settings** section in the **[GUI Settings](/docs/gui-settings#system-settings)**)* - Specify a delimiter to separate between values within the same field of an exported CSV file, otherwise the delimiter defined in **Export CSV delimiter to use for multi-value fields** is used.

* **Maximum rows** *(default: 1048500)* - Specify the maximum number of rows to be included in the CSV file.  When you set a value here the generated CSV file will include the top x rows, based on the specified values. Otherwise, the generated CSV file will include the default maximum rows, set as 1048500.

* **Include associated devices (only for Aggregated Security Findings and Software)** - For Software and Aggregated Security Findings queries. Toggle on this option to include the associated devices with the preferred hostname as a predefined field for each Software or Aggregated Security Finding. When you create a CSV file with associated devices (for Aggregated Security Findings or Software),  if the exported query results are larger than the value set under Maximum rows (or the default value of 1048500), an appropriate notice is displayed at the end of the CSV file.

  * **Device fields** -  This option is available for Software and Aggregated Security Findings. Select the device fields to add. By default Preferred Host Name is selected. Click add to select more fields. At least one field must be selected. Click the bin icon to remove a device field.

* **Wrap request in incident\_object** - Select this option to wrap the outgoing request payload within an "incident\_object" for APIGEE integration.

* **Create ticket as flavor** - When selected, flavor ticket updates are fetched using the [ServiceNow Tickets Fetch](https://docs.axonius.com/axonius-help-docs/docs/servicenow-tickets-fetch) adapter.

***