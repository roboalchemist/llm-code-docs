# Source: https://docs.axonius.com/docs/software-approval-list.md

# Software Registry

Use the **Software Registry** to manage software enrichments and maintain a list of approved or unapproved software in your organization, whether installed on devices or not. Additional approval statuses are also available. These enrichments can then be a basis for follow-up actions (send notification on discovered unapproved software, remove unapproved software, etc.).

You can add or update software in the Software Registry either manually or by uploading a CSV file based on a CSV template. All the enrichment fields also appear in the **[Software](/docs/software)** table, for better management and tracking of the software inventory.

## Required Permissions

* You must have **Manage Software Approval List** permissions to view the Software Registry page.

* Only users with **Edit Software** permissions can modify the **Software Status** field in the software inventory.

## Software Registry Display Rules

The Software Registry serves as a dedicated space for viewing and handling both discovered and managed software, including software approval statuses.

An asset appears in the [Software Registry table](/docs/software-registry#software-registry-table) if it meets either of the following rules:

* **Manual** or **External Entry** - The source is any value other than the **Software** page, such as Manual, CSV file, or relevant adapters.
* **Approval Status** - The software has been assigned any value in the **Approval Status** field, regardless of how it was added to the system. For the list of approval statuses, see [Manually Adding Software](/docs/software-registry#manually-adding-software).

These display rules ensure that software imported from external repositories or manually defined by administrators remains visible in the Software Registry, even if it is not currently detected on any device in your environment.

## Software Registry Sources

In addition to manual uploads, you can populate the Software Registry by connecting to particular adapters. This allows you to continuously synchronize software data and approval statuses from external CMDBs or file repositories.

Supported sources:

* **CSV Adapter** - Use the [CSV - Software Inventory](/docs/software-inventory-csv) adapter to synchronize hosted files containing software inventory and approval statuses. This is particularly useful for maintaining a "Source of Truth" list that persists in the Software Registry regardless of device discovery.
* **ServiceNow** – Map ServiceNow CMDB fields directly to the Axonius Software Registry fields.  For configuration details, see [Enriching Software Assets with ServiceNow CMDB Data](/docs/enriching-software-assets-with-servicenow-cmdb-data).
* **Custom Parsing** – You can upload a list of files from adapters and use [Adapter Custom Parsing](/docs/adapter-custom-parsing) to map them to the **Approval Status** field, automatically adding them to the Software Registry.

## Software Registry Table

<Callout icon="📘" theme="info">
  Note

  Initially, the **Software Registry** table is not populated. To populate the table with data, see [Populating the Software Registry](#populating-the-software-registry).
</Callout>

<Image align="center" alt="Software Registry table" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/software/Software_Registry.png" className="border" />

The **Software Registry** table contains the following columns:

* **Installed Software: Software Name** - The name of the software (as it appears on the software page).
* **Installed Software: Software Vendor** - The name of the software vendor.
* **Approval Status** - The approval status: **Approved**, **Not Approved**, **For Review**, **Risk Accepted**, or **Under Investigation**. For more details on these status types, see [Manually Adding Software](/docs/software-approval-list#manually-adding-software).
* **Installed Software: Software Version** - The software version.
* **Installed Software: Version Approval Status** - Approval for the version level. Does not have to match the approval status of the software level.
* **Detection Status** - Displays whether this software appears in your environment, thus presented in the Software table.
* **Software Registry: Source** - Shows how the software was added:
  * **Software Page** - Entered by **Edit Approval Status** in the Software table.
  * **Manual** - Entered by the **Add Software** button in the Software Registry.
  * **Imported** - Imported to the Software Registry using **Import CSV file**.
  * **Adapter**- Imported into the Software Registry from external products via configured adapters.
* **Software Category** - Displays one or more categories for the software that are the most suitable for that software, enriched by Axonius Catalog.
* **Owner** - The owner of the application in the organization. Usually it is the administrator with the highest-level administrator privileges.
* **License Quantity** - The number of purchased units of the software license.
* **License Start Date** - The start date of the software license.
* **License End Date** - The end date of the software license.
* **Installed Software: End of Life** - The date the software reaches end-of-life and is no longer sold by the publisher.
* **Installed Software: End of Support** - The date this software reaches end-of-support.
* **Tags** - Displays one or more user-defined labels for the software. Refer to [Working with Tags](/docs/working-with-tags) to learn more about adding tags.
* **Software Registry: Last Modified** - The time and date the software was last modified.
* **Software Registry: Last Modified By** - The person who last modified the software information.
* **Inactive License Count** - Displays a calculation of inactive licenses by subtracting the installed device count from the licenses entered manually. A negative value means installations exceed licenses. Field is empty if no value was entered in the License Quantity field in the Software Registry.

<Callout icon="📘" theme="info">
  Note

  Each row in the Software Registry table is expanded by each individual version (similar to the Versions View of the Software table).
</Callout>

## Populating the Software Registry

From the **Software** page, click **Software Registry**. The **Software Registry** pages is displayed.

The first time you use this feature, the page that opens is empty. Use [Import CSV](/docs/software-approval-list#importing-a-CSV-file) or [Add Software](/docs/software-approval-list#manually-adding-software) to populate the list.

### Importing a CSV File

You can import a CSV file that contains a list of software from the top of the page.

1. To upload the file, click **Import CSV**. ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ImportCSVbttn.png)

   A browse dialog opens.
2. Select a CSV file and click **Open**.

<Callout icon="💡" theme="warn">
  Important

  * In order to import the CSV file, you must use a template. You cannot export the CSV, change the data, and then upload. Click here to download the template:
    [software\_registry\_template.csv](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Files/software_registry_template.csv)

  * The CSV always overrides existing software name, software vendor, and versions in the Software Registry.

  * You cannot enter a version in the CSV without filling in a row representing the software itself (software without a version). The upload will fail if the row with the software (without a version) is missing.
</Callout>

#### CSV template

1. **Name** (required) - Name of the software.
2. **Vendor** - Name of the software vendor.
3. **Approval Status** - The exact approval values for the software (Approved/Not Approved).
4. **Software Category** - The exact matching values from existing software categories (capitalization). Possible values are a closed list (see dropdown list in the **Add Software** form).
5. **Owner** - A valid email address for the software.
6. **Version** - The software version number in free text.
7. **License Start Date** - Date in the `YYYY-MM-DD` format.
8. **License End Date** - Date in the `YYYY-MM-DD` format.
9. **End of Life** - Date in the `YYYY-MM-DD` format.
10. **End of Support** - Date in the `YYYY-MM-DD` format.
11. **License Quantity** - Integer.

<Image alt="CSV Template.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CSV%20Template.png" />

### Manually Adding Software

1. Click **Add Software**. The **Add Software** drawer opens for **Step 1: Name and Vendor**.

2. Enter the Software Name (required) and the Vendor (optional).

3. Click **Next**, the **Step 2 - Settings and Version Management** drawer opens.
   ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SR%20Add%20Software%20Settings%20and%20Versions%20Mgmt.png)

4. Under **General Settings**, select the applicable **Approval Status** for the added software:
   * **Approved** - The software is authorized for installation and use within the organization.
   * **Not Approved** - The software is prohibited or unauthorized for use within the organization.
   * **For Review** - The software has been identified but is currently waiting for evaluation to determine its compliance or security status. This is often the default state for newly discovered software.
   * **Risk Accepted** - The software has known risks such as vulnerabilities or policy violations, but the organization has granted an exception to allow its use (for example, for critical legacy business functions).
   * **Under Investigation** - The software is being actively analyzed by the security team or other authorized team, typically due to suspicious behavior, unknown origins, or potential security concerns.

     <Image align="center" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/software/Select_Approval_Status.png" className="border" />

5. Select and define any other optional setting.

6. You can have a different Approval Status for each software version, under **Version Management**.

<Callout icon="📘" theme="info">
  Note

  The approval status under **Version Management** does not have to match the approval status at the software level.
</Callout>

7. Click **Save**. The software now appears on the list.

### Importing Software from Adapters

In addition to manual entry and CSV file uploads, you can expand the Software Registry by importing software data or lists of files from the [CSV - Software Inventory](/docs/software-inventory-csv) or [ServiceNow](/docs/enriching-software-assets-with-servicenow-cmdb-data) adapters. This enables you to:

* Import and synchronize software data and approval statuses from external sources into the Software Registry even when it is not discovered on a device.
* Define which specific fields and information are brought over from the selected adapters via the user interface or [Adapter Custom Parsing](/docs/adapter-custom-parsing).

To import software repositories into the Software Registry using an external adapter:

1. **Configure the adapter connection:**
   1. In the Axonius left navigation panel, click the **Adapters**.
   2. Search for and select the adapter you wish to use as a software source.
   3. Click **Add Connection** or edit an existing connection.
2. **Enable software fetching:**
   1. In the **Connection Configuration** drawer, locate the setting to enable software information fetching.
   2. Ensure the connection is **Active** so that it pulls data during the discovery cycle.
3. **Define the presentation logic** (optional):
   1. Use the interface provided within the adapter's **Advanced Settings** or the **Software Registry** configuration drawer to define which adapter fields (such as version, vendor, or category) should be mapped to the Software Registry.
4. **Save and fetch**:
   1. Click **Save and Fetch** to initiate the import.
   2. After the fetch is complete, the software appears in the Software Registry with the **Source** labeled as **Adapter**.

## Searching and Filtering

You can filter the Software that is displayed.

<Image alt="SR Filters.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SR%20Filters.png" />

The following filters are available:

* **Installed Software: Software Name** - Display software with a specific name.
* **Installed Software: Software Vendor** - Display software from a specific vendor.
* **Approval Status** - Display either software that is 'Approved' or 'Not Approved'.
* **Installed Software: Software Version** - Display software from a specific version.
* **Installed Software: Version Approval Status** - Display software's approval for the version level.
* **Detection Status** - Display whether the software appears in the Software table (installed on a device).
* **Software Registry: Source** - Display how the software was added.
* **Software Registry: Last Modified By** - Display the person who last modified the software information.

Click **+ Filter** to add or remove filters.
Click **Reset** to clear all the filters and display all software.

## Software Registry Table Actions

### Editing the Approval Status

1. To edit the Approval Status, hover over a row. The **Edit Approval Status** button is displayed.
2. Click **Edit Approval Status** and then set it to the required approval status.
3. You can also select one or more items and select **Edit Approval Status** from the top of the page.

### Editing the Software

You can edit the information about the software.

1. To edit the software information, hover over a row, and the **Edit Software** button is displayed, or select an item and click **Edit Software**.
2. The **Edit Software - Settings and Version Management** drawer opens.
3. You can update the following general settings: Approval Status, Software Category, Owner, Tags, License Quantity, and/or License Start/End Date. You can also manage the approval status of specific versions.

<Callout icon="📘" theme="info">
  Note

  * You cannot edit a software’s name or its vendor name.
  * You can duplicate the software along with its Software Registry data to another asset.
</Callout>

4. To successfully add a software version, you must fill in at least one of the following fields: **Approval Status**, **License Quantity**, **License Start/End Date**, **End-of-Life Date**, or **End-of-Support Date**. If these fields are not filled in, the software version will still be saved.
5. Click **Save**  to save your changes.

<Image alt="SR Edit Software.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SR%20Edit%20Software.png" />

### Duplicating the Software

1. To duplicate the software, hover over a row or select an item and then click **More Actions**.

2. Select **Duplicate Software**, the **Add Software** drawer opens.

3. Enter the new **Software Name** (required) and **Vendor** name (optional) to ensure there are no duplicates in the system.

4. Click **Next**.

5. The **Add Software - Settings and Version Management** drawer opens.

6. Update the settings and then click **Save**.

### Deleting a Row

Hover over a row and click **Delete**, or select one or more rows and click **Delete**.
The software is removed from the **Software Registry**, and all its enrichment data is removed from the Software table. **Tags** is the only field that isn’t deleted (assuming they existed in the Software Registry before the deletion).

<Callout icon="📘" theme="info">
  Note

  All version enrichment information is also deleted when a software is deleted from the Software Registry.
</Callout>

All other Software table actions are available in the Software Registry table as well:

<Image align="center" alt="SR table actions.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SR%20table%20actions.png" className="border" />

## Exporting the Software Registry

You can export the Software Registry to a CSV file.

**To export the results to a CSV file:**

* On the **Software Registry** page, on the right side above the table, click **Export CSV**.
  The CSV file is automatically downloaded with a name format as:
  “axonius-manual*software*.csv”

When you set a filter, only the filtered data is exported to the CSV file.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).

<br />

<br />