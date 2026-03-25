# Source: https://docs.axonius.com/docs/send-csv-to-sharepoint.md

# SharePoint - Send CSV

**SharePoint - Send CSV** creates a CSV file listing the assets returned by the selected query, or assets selected on the relevant asset page, and sends it to a specific path on SharePoint.

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

These fields must be configured to run the Enforcement Action.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Use stored credentials from SharePoint adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [SharePoint](/docs/sharepoint) adapter connection.
</Callout>

* **Folder path** - Specify the **full** folder path. If the path is incorrect or incomplete, the action will fail. Usually, the folder path starts with ‘Documents/’, for example: *Documents/test\_folder*.
* **File name** - The CSV file name.
* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

## Additional Fields

These fields are optional.

* **Authentication Method** - Select the Authentication Method, either **User Credentials**, **Client Credentials**, or **Client REST Credentials**. When SharePoint Password Manager is enabled, see [Configuration to Use when SharePoint Password Manager is Enabled](/docs/send-csv-to-sharepoint#configuration-to-use-when-sharepoint-password-manager-is-enabled) below.
  * **User Credentials** - Enter the values for:
    * **User Name** - Enter the user name for the user account used to connect to SharePoint.
    * **Password** - Enter the password for the user account used to connect to SharePoint.
  * **Client Credentials** - Enter the values for:
    * **Client ID** - Enter the client ID.
    * **Client Secret** - Enter the client secret.
  * **Client REST Credentials** - Enter values for:
    * **Host Name or IP Address** *(default: graph.microsoft.com)* - - The host name or IP address used to check the Client REST Credentials. Use either the default value or one of the following values: *[http://microsoftgraph.chinacloudapi.cn](http://microsoftgraph.chinacloudapi.cn)* or *[http://graph.microsoft.us](http://graph.microsoft.us)*.
    * **Tenant** - Enter the tenant name.
    * **Client ID** - Enter the client ID.
    * **Client Secret** - Enter the client secret.

* **Site URL** - The URL of the SharePoint site, for example: `https://mydomain.sharepoint.com/sites/mysite`.

* **SharePoint Host Name** - The host name of the SharePoint site, for example: *mydomain.sharepoint.com*.

* **Site Name** - The site name of the SharePoint site, for example: `mysite`.

* **Append date and time to file name**
  * If enabled, the date and time (in UTC) of enforcement action execution will be added as a suffix to the generated CSV file name. For example, `axonius_data_2020-01-06-16:48:13.csv`.
  * If disabled, the CSV file will be stored based on the specified/default file name.

* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **Create CSV even if no data is returned in the query** - Select whether to create and send a CSV file even if the query does not return any results.

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

## Configuration to Use when SharePoint Password Manager is Enabled

When SharePoint Password Manager is enabled, use the following configuration settings.

Select **Client REST Credentials** as the authentication method. Use the **Site Name** and **SharePoint Host Name** fields.

For example:

* **Host Name** - `https://demo-account.sharepoint.com/sites/TEST2/Shared%20Documents/Forms/TestItems.aspx`
* **Site Name**  - `TEST2`
* **Sharepoint Host Name** - `demo-account.sharepoint.com`

In the configuration, change */Shared Documents/LB5347 Files/PowerBI/GAP Report/All GAP* to *Documents/LB5347 Files/PowerBI/GAP Report/All GAP*. Be sure to leave off the leading */*.

## APIs

Axonius uses the [SharePoint REST operations via the Microsoft Graph REST API](https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph)
Refer to [Get access without a user](https://learn.microsoft.com/en-us/graph/auth-v2-service?view=graph-rest-1.0) for details on obtaining credentials.

To fetch users Axonius uses the [SharePoint List Users endpoint.](https://learn.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0\&tabs=http#optional-query-parameters)

## Required Ports

Axonius must be able to communicate with the value supplied in [Host Name or IP Address](#parameters) via the following ports:

* TCP port 80/443

## Required Permissions

The credentials used to run this Enforcement Action require the following SharePoint permission:

* `Sites.FullControl.All` (permission type: Application)

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).