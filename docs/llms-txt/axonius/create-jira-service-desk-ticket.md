# Source: https://docs.axonius.com/docs/create-jira-service-desk-ticket.md

# Jira Service Management - Create Ticket

<Callout icon="📘" theme="info">
  Notice

  This Enforcement Action replaces [Jira - Create Issue](/docs/create-jira-issue), which was deprecated.
</Callout>

<Callout icon="💡" theme="warn">
  Note

  This Enforcement Action requires the Jira Service Management (JSM) Standard, Premium, or Enterprise license.\
  However, if you have Jira Data Center without this license will be able to use its credentials in this action configuration.
</Callout>

**Jira Service Management - Create Ticket**  creates one incident in Jira Service Management for:

* Each asset returned by the selected query or assets selected on the relevant asset page.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

<Callout icon="📘" theme="info">
  Notes

  * Details for all devices are included in the ticket message as well as the CSV.

  * Some environments may need to allow proxy access from the primary node to the hosted Jira instance. Additionally, the following domains may also need to be allowed:

  * [http://api.atlassian.net/](http://api.atlassian.net/)

  * [https://automation.atlassian.com/](https://automation.atlassian.com/)
</Callout>

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

* **Use stored credentials from Jira Service Management (Service Desk) adapter**  - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down is available, and you can and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Jira Service Management](/docs/en/atlassian-jira-service-desk) adapter connection.
</Callout>

* **Request description** - Specify a description for the request. The maximum allowed length for this description is 30,000 characters.
* **Request summary** - Specify a summary for the created issue.
* **Issue type** - Indicate the issue type.
* **Project key** - Specify or select the desired project in Jira Service Management where the issue will be created.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Host Name or IP Address**  - The hostname or IP address of the Jira Service Management server.

  * **Jira Service Management API version**   - Specify the Jira Service Management API version.

  * **User Name** and **API Token** - The credentials to connect to Jira Service Management. **User Name** is optional when not using the Cloud API.

  * **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

  * **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

  * **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the server using the  **HTTPS Proxy**.

  * **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

  * **Use Cloud API** - Select this option to explicitly specify that the enforcement should use the Cloud API instead of Jira Server API.  When the user uses the cloud API, the default host name or IP address should be [https://api.atlassian.com](https://api.atlassian.com). Even when left unselected, the action will attempt to use the cloud API if the domain specified is “api.atlassian.com”.
</Callout>

* **Use full URL** - Select this option if the URL references to a specific endpoint. For example: *[https://my-jira.com/jira](https://my-jira.com/jira)*.
* **Assignee** - Enter a user name or email address to which to assign the incident. It is recommended to use the user's email address.
* **Use assignee name instead of ID** *(default: enabled)* - When **Assignee** has a value, Jira Service Management will search for the assignee by username or email address, depending on which is entered. When not selected, enter the user ID in the **Assignee** field.
* **Labels** - Comma-separated labels that will be added to the tickets.
* **Components** - Comma-separated components that will be added to the tickets.
* **Custom fields (JSON format)** -   Custom fields to add to this incident described in the following JSON format:

```json
`{"customfieldXYZ":{"value":"VALUE YOU WANT"}} or {"customfieldXYZ"{"id""ID YOU WANT"}}`
```

<Callout icon="📘" theme="info">
  Note:

  If a custom field is already configured by this Enforcement Action, the new custom value is ignored.
</Callout>

* **Send created issue link to webhook URL** - Specify the webhook URL where the created Jira Service Management issue link will be sent, instead of within Jira Service Management. Axonius will send the message specified in the **Webhook content** field to the specified webhook URL.
* **Webhook content** - Specify the webhook content in JSON format. This content will be sent to the specified webhook URL.

<Callout icon="📘" theme="info">
  Note

  * The default content is:

  ```json
  {"text": "Created issue link is:< >"}
  ```

  * \< > - will include the Jira  Service Management issue URL.
</Callout>

* **Related parent ticket key** - Enter the key of the related parent ticket. The key usually includes the project key (string) and a sequential number, for example, "CT-1960".

* **Fetch created issue to Axonius** *(default: enabled)* - Select this option to enable the system to automatically retrieve information about newly created Jira issues and ingest that data into Axonius.

* **Create ticket as flavor** - Select this option to fetch ticket updates from the Jira Service Management Fetch Tickets adapter if you don't have a Jira Service Desk license. This requires enabling the **Fetch EC Action ticket updates** option in the [Jira Service Management (Service Desk) Fetch Tickets adapter](/docs/jira-fetch-tickets).

* **Send CSV data** - When selected, a CSV file with the query results is attached to the ticket.

* **Add default incident description** - Select whether to send the incident description to Jira Service Management.
  **Message example:**
  *Alert - "test" for the following query has been triggered: Missing Sophos*

  *Alert Details*
  *The alert was triggered because: The number of entities is above 0
  The number of devices returned by the query:4
  The previous number of devices was:4*

  *You can view the query and its results here: [https://demo-latest.axonius.com/devices?view=Missing](https://demo-latest.axonius.com/devices?view=Missing) Sophos*

* **Add a summary line of each Asset to the Description** - When selected, adds a one-line summary for each asset included in the ticket. For devices: hostname, os type, and serial number. For users: user, hostname, OS type, and serial number.

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

* **Append CSV data to request description** - Select this option to automatically add the data from your CSV file to the end of the text that you already entered in the **Request description** field (see above). Note that if adding the CSV data makes the description longer than the 30,000-character limit, the CSV data will be shortened to fit within the limit.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

## Required Permissions

The stored credentials, or those provided in [Connection and Credentials](#connection-and-credentials), must have the following permission(s) to perform this Enforcement Action:

* Action privileges

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).