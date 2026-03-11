# Source: https://docs.axonius.com/docs/gsuite-send-message.md

# Google Workspace - Send Direct Message to a Space

**Google Workspace - Send Message** sends a message via an adapter connection or a webhook for:

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

* **Use stored credentials from Google Workspace adapter** - Select this option to use the connected [Google Workspace](/docs/g-suite-by-google) adapter credentials.
  * When you select this option, the **Select Adapter Connection** dropdown is available, and you can choose which adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Google Workspace](/docs/g-suite-by-google) adapter connection.
</Callout>

* **Space ID** - Enter the ID of the space taken from the URL -[https://mail.google.com/mail/u/0/#chat/space/\*\*space](https://mail.google.com/mail/u/0/#chat/space/**space) ID\*\*
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

<Callout icon="💡" theme="warn">
  <br />

  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Email of an admin account to impersonate** - The email of your Google Workspace admin. The admin account must be in the same workspace as the connection for the Axonius Workspace adapter.

  * **Account Profile Name** - Enter the account profile name.

  * **JSON Key pair for the service account** - Upload the JSON file you have created for your service account. For more details, refer to [Google Workspace](/docs/g-suite-by-google) adapter.
</Callout>

* **Chat Header** *(default: Axonius Action Center)* - Type a header for the chat.
* **Chat Text** - Type the body of the chat.
* **Include List Entities in Chat Text** - Select this option to include list entities in the body of the chat.
* **Send CSV data** - Select this option to include a CSV file with the query results in the issue created. For Vulnerabilities, the first row shows the vulnerability information, and the next rows show the linked devices.

**Additional CSV Settings**

* **Split by asset entities**  -  Select to create a CSV file where each asset on a device is shown as a separate row. This separates each asset as the 'expand' option in the application. It separates each asset by its entity. For example, you will be able to know which values were fetched from each adapter connection.

  * If supplied, each value on a device or user is shown as a separate row.
  * If not supplied all values on a device are in the same cell on the CSV file.

* **Export CSV delimiter to use for multi-value fields** *(default:**Export CSV delimiter to use for multi-value fields** field under the **System Settings** section in the **[GUI Settings](/docs/gui-settings#system-settings)**)* - Specify a delimiter to separate between values within the same field of an exported CSV file, otherwise the delimiter defined in **Export CSV delimiter to use for multi-value fields** is used.

* **Maximum rows** *(default: 1048500)* - Specify the maximum number of rows to be included in the CSV file.  When you set a value here the generated CSV file will include the top x rows, based on the specified values. Otherwise, the generated CSV file will include the default maximum rows, set as 1048500.

* **Include associated devices (only for Aggregated Security Findings and Software)** - For Software and Aggregated Security Findings queries. Toggle on this option to include the associated devices with the preferred hostname as a predefined field for each Software or Aggregated Security Finding. When you create a CSV file with associated devices (for Aggregated Security Findings or Software),  if the exported query results are larger than the value set under Maximum rows (or the default value of 1048500), an appropriate notice is displayed at the end of the CSV file.

  * **Device fields** -  This option is available for Software and Aggregated Security Findings. Select the device fields to add. By default Preferred Host Name is selected. Click add to select more fields. At least one field must be selected. Click the bin icon to remove a device field.

* **Use Webhook URL instead of adapter connection (Send CSV and related settings will be ignored)** Send the message via Webhook instead of using the adapter connection.

## APIs

Axonius uses the following APIs:

* [Google Workspace - Send a message API](https://developers.google.com/chat/api/guides/v1/messages/create#python).

* [Google Chat API](https://console.cloud.google.com/apis/library/chat.googleapis.com?project=sys-96534398415828768375863552)

## Required Permissions

This action requires that you enter the following scope in your Google account's [Domain Wide Delegation](https://admin.google.com/ac/owl/domainwidedelegation?hl=en) for the Client ID used for this connection (inside the JSON file): **[https://www.googleapis.com/auth/chat.messages.create](https://www.googleapis.com/auth/chat.messages.create)**

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).