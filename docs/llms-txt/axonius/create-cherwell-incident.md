# Source: https://docs.axonius.com/docs/create-cherwell-incident.md

# Cherwell IT Service Management - Create Incident

**Cherwell IT Service Management - Create Incident**  (Create Cherwell Incident) creates an incident in Cherwell for:

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

* **Use stored credentials from the Cherwell adapter**   - Select this option to use credentials from the adapter connection. By default, the first connection is selected.

<Callout icon="📘" theme="info">
  NOTE

  * To use this option, you must successfully configure a [Cherwell IT Service Management](/docs/cherwell) adapter connection.

  * The user name and the password used for the adapter connection must be user with permissions to create new incidents.
</Callout>

* **Incident description**   - Specify an incident description.
* **Priority** *(required, default: 5)* - Specify the incident priority.
* **Instance Name**  - The Axonius node to use when connecting to the specified host. For more details, see [Connecting Additional Axonius Nodes](/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="default">
  ### Connection and Credentials

  * When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Cherwell Domain**   - The hostname or IP address of the Cherwell server.

  * **User Name** and **Password**  - The user name and the password of a user with permissions to create new incidents.

  * **Client ID**    - Enter the client ID created in the CSM Administrator. For details, see [Cherwell - Obtaining API Client IDs](https://help.cherwell.com/bundle/cherwell_rest_api_940_help_only/page/oxy_ex-1/content/system_administration/rest_api/csm_rest_obtaining_client_ids.html#ObtainingApiClientIds#OpenSwagger#ObtainingApiClientIds#OpenSwagger).

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional, default: empty)* - A proxy to use when connecting to the value supplied in **Cherwell Domain**.

  * If supplied, Axonius will utilize the proxy when connecting to the value supplied in **Cherwell Domain**.

  * If not supplied, Axonius will connect directly to the value supplied in **Cherwell Domain**.
</Callout>

* **Short description**   - Specify the incident title.

* **Add default incident description**   - Select whether to send the incident description to Cherwell.

  * If enabled, Axonius will include the default incident description (mentioned below) in the Cherwell incident.
  * If disabled, Axonius will not include the default incident description (mentioned below) in the Cherwell incident.

  **Message example:**
  *Alert - "test" for the following query has been triggered: Missing Sophos*

  *Alert Details*
  *The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query:4
  The previous number of devices was:4*

  *You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos*

* **Customer display name**   - Specify the customer display name.

  Multiple optional incident related settings  :

  1. **Source**
  2. **Service**
  3. **Category**
  4. **Subcategory**
  5. **Incident type**
  6. **Status**

<Callout icon="📘" theme="info">
  NOTE

  Since the valid values of the different parameters are customer specific, Axonius does not validate any of those parameters values. You must make sure inserted values are correct, otherwise, the request might fail.
</Callout>

* **Additional fields** *(optional, default: empty)* - Specify additional fields to be added as part of the incident as key/value pairs in a JSON format. For example:

```json
{"field1": "value1", "field2": "value2"}
```

.

* If supplied, Axonius will add the specified fields and values to the created incident. If one of the specified fields is invalid, the request might fail.
* If not supplied, Axonius will not add any additional fields to the created incident.
* **Send CSV data** - Select to include a CSV file with the query results in the issue created.

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

**Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).