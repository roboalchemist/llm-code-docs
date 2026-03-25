# Source: https://docs.axonius.com/docs/send-csv-to-box.md

# Box - Send CSV

**Box - Send CSV** creates a CSV file with the assets returned by the selected query or assets selected on the relevant asset page and sends it to a specific path on Box.

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

* **Box Platform private key configuration file** - The private key configuration file that provides the [Required Permissions](#required-permissions) to fetch assets.

* **Use stored credentials from Box Platform adapter** - Select this option to use credentials from the adapter connection. By default, the first connection is selected.
  * When you select this option, the **Select Adapter Connection** drop-down becomes available. Select the adapter connection to use for this Enforcement Action.

<Callout icon="📘" theme="info">
  Note

  To use this option, you must successfully configure a [Box Platform](/docs/box) adapter connection.
</Callout>

* **Folder ID** - The folder ID. If the supplied folder ID is 0, the file will be created in the root folder of the app account. Otherwise, the file will be created in the supplied folder ID.
* **File name** *(default: axonius\_data)* -The file name.

## Additional Fields

These fields are optional.

<Callout icon="💡" theme="warn">
  ## Connection and Credentials

  When **Use stored credentials from the adapter** is toggled off, some of the connection fields below are required to create the connection, while other fields are optional.

  * **Box Platform private key configuration file** - the private key configuration file that provides the [Required Permissions](/docs/send-csv-to-box#required-permissions) to fetch assets.
</Callout>

* **Append date and time to file name**
  * If enabled, the date and time (in UTC) of enforcement action execution will be added as a suffix to the generated CSV file name. For example, *axonius\_data\_2020-01-06-16:48:13.csv*.
  * If disabled, the CSV file will be stored based on the specified/default file name.

* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

* **Gateway Name** -  Select the Gateway through which to connect to perform the action.

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

* **Send file compressed** - Compress the CSV into a GZIP file before sending.

## APIs

Axonius uses the following BOX APIs:

* [Upload file](https://developer.box.com/reference/post-files-content/) - for file size up to 20MB.
* [Create upload session](https://developer.box.com/reference/post-files-upload-sessions/) - for file size over 20MB.

## Required Permissions

The value supplied in [**Box Platform private key configuration file**](/docs/send-csv-to-box#additional-fields) refers to the generated private key configuration file for your Custom App using JWT authentication:

1. **Set up a Custom App** - Set up a Custom App using JWT authentication. For details, see [Box Guides - Setup with JWT](https://developer.box.com/guides/authentication/jwt/jwt-setup/).
2. **Create Box Platform private key configuration file** - After a Custom App has been created to use JWT authentication, there is an option available in the Developer Console to have Box create a configuration file. This file will include the keypair as well as a number of other application details that are used during authentication.

   1. Click on the "Configuration" option from the left sidebar in your application and scroll down to the "Add and Manage Public Keys" section.

   <Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1023)(728).png" />

   2. Click the "Generate a Public/Private Keypair" button to have Box generate a keypair. This will trigger the download of a JSON configuration file that you can move to your application code.
   3. Upload this file as the **Box Platform private key configuration file**.
3. **Application Scopes** - The configured app must have the following application scopes:
   * Read all files and folders stored in Box
   * Read and write all files and folders stored in Box

<Image align="center" alt="image.png" border={false} width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1748).png" />

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).