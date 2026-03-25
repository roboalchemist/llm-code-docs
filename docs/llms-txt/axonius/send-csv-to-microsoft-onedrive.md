# Source: https://docs.axonius.com/docs/send-csv-to-microsoft-onedrive.md

# Microsoft Azure - Send CSV to Microsoft OneDrive

**Microsoft Azure - Send CSV to Microsoft OneDrive** creates a CSV file listing the assets returned by the selected query, or assets selected on the relevant asset page, and sends it to a specific path on Microsoft OneDrive.

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

* **User name** and **Password** - The credentials for a Microsoft Entra ID (Azure AD) user account that has [read and write permissions](#required-permissions) to the supplied OneDrive account.

<Callout icon="📘" theme="info">
  NOTE

  Axonius does not use the application authentication, as application permissions provides access to all files in the organization.
</Callout>

* **Tenant ID** - Microsoft Entra ID (Azure AD) ID.
* **Client ID** - The Application ID of the Axonius application.
* **File name** *(default: axonius\_data)* - The file name.
* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Additional Fields

These fields are optional.

* **Folder path** - Specify a folder path.
  * If supplied, the file will be created under the specified folder path.
  * If not supplied, the file will be created under the user's root drive.
* **Append date and time to file name**
  * If enabled, the date and time (in UTC) of enforcement action execution will be added as a suffix to the generated CSV file name. For example, *axonius\_data\_2020-01-06-16:48:13.csv*.
  * If disabled, the CSV file will be stored based on the specified/default file name.
* **Verify SSL** *(optional)* - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius. For more details, see [SSL Trust & CA Settings](https://docs.axonius.com/docs/certificate-settings#ssl-trust-ca-settings).
* **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

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

The value supplied in [**User Name**](#connection-settings) must be a Microsoft Entra ID (Azure AD) user account that has read and write permissions to the supplied OneDrive account.

1. In Azure AD, create a user for Axonius.

2. Login as the user and create an application. A user can register an application by default.

3. Copy the **Client ID** and **Tenant ID** from the application page.

4. In the **Request API permission** section, add GraphAPI and provide the following permissions:
   1. Delegated Permissions
   2. Files.ReadWrite.Al
   These permissions will allow the application an access only to the files that the user can access.
   <Image alt="image.png" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1760).png" />

5. Go to the **Authentication** section and enable the **Allow public client flow**.
   <Image alt="image.png" width="600px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image(1761).png" />

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).