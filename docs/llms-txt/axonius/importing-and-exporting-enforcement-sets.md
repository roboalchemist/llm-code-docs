# Source: https://docs.axonius.com/docs/importing-and-exporting-enforcement-sets.md

# Importing and Exporting Enforcement Sets

Use the Import/Export Enforcement Sets capability to share enforcement sets with other users, different data scopes, and  across Axonius environments. You can import or export multiple enforcement sets at the same time.

## Permissions

The following permissions are required to import or export enforcement sets:

* Add/Import Enforcement
* Export Enforcement

Refer to the [Action Center Permissions List](/docs/en/permissions-list#enforcement-center) to learn more.

## Importing Enforcement Sets

**To import one or more enforcement sets from the Action Center page**

1. From the Create Enforcement Set dropdown, click **Import Enforcement Set**.

2. If a query or other data already exists in the environment to which you are importing the workflow, a warning dialog is displayed.

   <Image align="center" border={false} width="450px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/action_center/ECSetImportConflictWarning.png" />

3. For each instance of conflict, select how you want to resolve it:
   1. **Save as copy** -  Creates a copy of the item.
   2. **Overwrite** - Overwrites the existing item with the one being imported.

4. Click **Import**. The imported workflow is added to the Workflows page, and the selections from the previous step are implemented.

It is recommended to refresh the page once the import process is finished to ensure the new enforcement sets appear in the table.

If the import process fails, an **Import Failed** dialog appears, detailing the reason for the failure. The possible reasons are:

* File size exceeded maximum size
* The file is not a ZIP file
* Invalid  or corrupted import file
* There is no enforcement set to import

You can try again by selecting another file (click **Select Another File**).

## Exporting Enforcement Sets

You can export one or more enforcement sets at a time.

**To export one enforcement set:**

1. To export a single enforcement set, hover over the enforcement set you want to export, click the 3-dot menu for that enforcement set, and select **Export**.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/action_center/ECSetsExportSingle.png" />
2. A pop-up notifies you that credentials and sensitive inputs are excluded and must be reconfigured when reimporting this enforcement set. To continue and export, click **Export**. The selected enforcement set is exported to a ZIP file.

**To export multiple enforcement sets:**

1. Select the checkboxes of all the enforcement sets you want to export, click the 3-dot menu above the table, and select **Export**.

   <Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/action_center/ECSetsExportMultiple.png" />
2. A pop-up notifies you that credentials and sensitive inputs are excluded and must be reconfigured when reimporting these enforcement sets. To continue and export, click **Export**. The selected enforcement sets are exported in a ZIP file.

<br />