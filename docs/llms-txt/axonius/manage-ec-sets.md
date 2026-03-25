# Source: https://docs.axonius.com/docs/manage-ec-sets.md

# Managing Enforcement Sets

The folder pane on the left side of the **Enforcements** page allows you to easily manage Enforcement Sets.

<Image border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnforcementFoldersPaneNew(1).png" />

## Working with Folders

Use the **Folders** pane to organize your Enforcement Sets into folders, which you can create and name according to your needs. This organization enables you to easily find related Enforcement Sets.
You can search for a folder using the Search box at the top of the **Folder** pane.

The following are the default system folders:

* **All Enforcements** - This folder includes all Enforcement Sets in the system that you're authorized to see. This includes Enforcement Sets from all the folders listed below, including **Shared Enforcements**, **Drafts**, **Quick Actions**, and more. Note that you cannot save Enforcement Sets directly to the **All Enforcements** folder.
* **Shared Enforcements** - This folder includes Enforcement Sets that you have access to or that you created from the Action Center (using the **Create Enforcement Set** button) or from the **Actions** menu on an Asset page (**Enforce> Create Enforcement**). You can create new folders and subfolders under the **Shared Enforcements** folder. Enforcement Sets in a subfolder also appear in the parent folder.
* **Quick Actions** - This folder includes all Enforcement Sets, which are automatically created when you run Quick Actions (AKA Quick Enforcement Actions) on selected assets from an Assets page and then select one of the following from the **Actions** menu:
  * [**Create Ticket**](/docs/devices-actions#create-ticket)
  * [**Add Custom Field**](/docs/working-with-custom-data#adding-custom-fields-to-query-or-filter-results-with-a-quick-enforcement-action)
  * [**Tag**](/docs/working-with-tags#adding-tags-to-query-or-filter-results-with-a-quick-enforcement-action)
* **Findings Notification Enforcements** - This folder includes Enforcement Sets created by External Notifications in Findings Rules. After they are created, these Enforcement Sets are disabled and cannot be edited or run.
* **Predefined Enforcements sets** - This folder includes Axonius-provided Enforcement Sets that you can use as a basis for a new Enforcement Set. Learn more on [how to use Predefined Enforcement Sets](/docs/using-predefined-enforcement-sets).
* **Drafts** - This folder includes saved Enforcement Sets that are not fully configured.
* **System Enrichments** - This folder exists on SM (SaaS Management product) enabled machines. The following predefined Enforcement Sets are automatically created in the Axonius system and placed in this folder:
  * **System enrichment - Activity status** - Generates the **Activity Status** field  (sets to *Active* or *Inactive*) in the **User Extensions** module.

  * **System enrichment - Is Managed by SSO** - Generates the **Is Managed By SSO** field (sets to *Yes* or *No*) in the **Users** module.
* **Field Mappings** - The Enforcement Sets which the Field Mappings are based on.

The following describes some rules regarding the system folders:

* The Enforcement Sets in the **Predefined Enforcement Sets** folder are Read Only and cannot be modified or removed. You can save them as regular Enforcement Sets.
* You can add and remove Enforcement Sets to/from **Shared Enforcements**, **Drafts**, or **Quick Actions** folders.
* If you want to pause **System Enrichments** actions, select the relevant Enforcement Sets in the folder, and pause their schedules (**Manage Scheduling> Turn Scheduling Off**) instead of deleting them.
* You cannot delete or rename system folders, including **All Enforcements**, **Shared Enforcements**, **Quick Actions**, **Findings Notification Enforcements**, **Predefined Enforcements sets**, **Drafts**, **System Enrichments**, and **Field Mappings**.
* Under the **Shared Enforcements** folder only, you can create up to five levels of subfolders, as necessary. When you hover over a **Shared Enforcements** subfolder, the Folders menu appears. From here, you can create a new subfolder, rename a subfolder, or delete a subfolder.

<Image alt="EnforcementCenterManageFoldersNew" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EnforcementCenterManageFoldersNew.png" />

### Creating a New Folder

You can create new subfolders (up to five levels) under the **Shared Enforcements** folder.

**To create a new folder**

1. Hover over a folder.
2. Click the Folders menu. The Folders menu opens (see above screen).
3. Select **New Folder**. A new folder called 'untitled folder' is created inside the folder you selected.
4. Click the Folder menu again, and select **Rename** to give a more appropriate name to your folder.

### Renaming Folders

You can rename a subfolder that is located under the Shared Enforcements folder.

**To rename a folder**

1. Hover over a folder.
2. Click the Folders menu. The Folders menu opens (see above screen).
3. Select **Rename** and give a new name to the folder.

### Moving Folders

You can move subfolders within the Shared Enforcements folder.

**To move a subfolder**

* Click and drag the folder/subfolder to a different folder.

### Deleting Folders

You can delete any subfolders that you have created under Shared Enforcements. System folders cannot be deleted.

**To delete a folder**

1. Hover over a folder.
2. Click the Folders menu. The Folders menu opens (see above screen).
3. Click **Delete**.

<Callout icon="📘" theme="info">
  IMPORTANT

  Deleting a folder **does delete** all Enforcement Sets in the folder. This cannot be undone. To delete the folder but keep the Enforcement Sets, move them to another folder and then delete the folder you don't want.
</Callout>

### Moving Enforcement Sets to Another Folder

You can move selected enforcement sets from the **Shared Enforcements** folder or subfolder (or from the All Enforcements folder), to another **Shared Enforcements** subfolder.  You cannot move Enforcement Sets from the **Drafts**, **Quick Actions** or **Predefined Enforcements sets** subfolders.

**To move Enforcement Sets to another folder**

1. In the table on the [**Enforcement Sets** page](/docs/enforcement-center-page), do one of the following:
   * To move a single enforcement set: Hover over the row of an Enforcement Set, and then at the end of the row, from the 3-dot **More Actions** menu, click the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MoveToFolderAction.png) action.

   * To move one or more enforcement sets: Select the checkboxes of the Enforcement Sets that you want to move and then on the top right of the table, from the 3-dot **More Actions** menu, click the![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/MoveToFolderAction.png) action.

A Folder List dropdown opens.

<Image alt="FolderListDropdown" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FolderListDropdown.png" />

2. Use the vertical and horizontal scrollbars to find the destination folder you want or search for a specific folder by entering part or all of its name in **Search Folders**.
3. Click the destination folder, and then click **Move**. The Enforcement Sets are moved to the selected folder.