# Source: https://docs.axonius.com/docs/send-to-https-log-server.md

# HTTPS Log Server - Send Log Message

**HTTPS Log Server - Send Log Message** creates a log message with a custom description and/or the action results summary (incident description) in an HTTPS log server. It also creates optional JSON messages with the asset data (device or user) for each of the assets in the query results or  a JSON file with data about the system entity queried, for queries created  on Activity logs and Fetch History using filters.

To use this action, you must enable the **Use HTTPS logs** setting and configure the HTTPS Logs host and port. For more details, see [Configuring HTTPS Log Settings](/docs/configuring-https-log-settings).

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

The incident description message includes the Enforcement Set name, the triggered query, the condition for executing the Enforcement (if it exists), and number of current and previous results.

## Message Example

The following text is a sample message.

***

*Alert - "test" for the following query has been triggered: Missing Sophos*

*Alert Details*
*The alert was triggered because: The number of entities is above 0
The number of devices returned by the query:4
The previous number of devices was:4*

\_You can view the query and its results here: `https://myaxoniusinstance.axonius.com` Sophos

***

## Additional Settings

These fields are optional.

* **HTTPS logs host** and **Port** - For information, refer to [Configuring HTTPS Log Settings](/docs/configuring-https-log-settings).
* **Authorization Header** - If the HTTPS log server message requires user authentication, specify the required HTTP authorization request in the  field.
  * If supplied, Axonius will pass the specified authorization header information with the HTTP request.
  * If not supplied, Axonius will not pass any additional information with the HTTP request.

<Callout icon="📘" theme="info">
  Note

  A value for **Authorization Header** must be provided even if "Use HTTPS logs setting" is enabled in System Settings with an "Authorization Header" provided there.  The Enforcement Action does not pick up the Authorization Header from the Settings page. See [Configuring HTTPS Log Settings](/docs/configuring-https-log-settings).
</Callout>

* **Extra headers around message (JSON format)** - Use this setting to add a JSON formatted string that can be added to the HTTPS Log JSON thus enabling efficient integration with tools that accept input of JSON. The input should appear as follows:
  ```
   {"index": 12345, "sourcetype": "_json"}
  ```
* **Max retries** - The maximum number of retries to perform if connection to the HTTPS logging server is not successful.
* **Backoff for retries in seconds** -  The number of seconds to wait between retries, using exponential backoff.
* **Description** - Specify an optional description.
  * If supplied, Axonius will include the specified description in HTTPS log server message.
  * If not supplied, Axonius will not include any custom description in HTTPS log server message.
* **Send result details** - Select whether to send additional messages to the HTTPS log server with the details of the results.
  * If enabled, Axonius will send a JSON file with details of the results.
  * If disabled, Axonius will not send details of the results.
* **Add default incident description** - Select whether to send the incident description to the HTTPS log server.
  * If enabled, Axonius will include the default incident description (mentioned above) in HTTPS log server message.
  * If disabled, Axonius will not include the default incident description (mentioned above) in HTTPS log server message.
* **Send CSV data** - Select whether to send the ran query data in a CSV format to the HTTPS log server.
  * If enabled, Axonius will include the query data in a CSV format in HTTPS log server message.
  * If disabled, Axonius will not include the query data in HTTPS log server message.

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

**Json field name replacement map (JSON format)** - Enter fields in JSON format so that all occurrences of the specified keys in the JSON output of device data are replaced with the respective values (requires “Send result details” to be TRUE).  Example of the format to enter is

```json

{
  "specific_data.data.": "",
  "adapters_data.data.azure_ad_adapter.id": "Azure AD Device ID"
}
```

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).