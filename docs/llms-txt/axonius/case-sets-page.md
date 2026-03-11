# Source: https://docs.axonius.com/docs/case-sets-page.md

# Case Sets Page

The **Case Sets** page provides a centralized summary of all saved Case Sets, allowing you to manage them, view their last run status, and more. You can also manually initiate a run of an existing Case Set or create a new one.

## Required Permissions

To interact with Case Sets, specific permissions are necessary:

* To view a Case Set, list of Case Sets, or Run History:
  * View Enforcement Center
  * View Case Management
  * View user accounts and roles  (under Users Management)
  * View Enforcement Tasks
* To create or edit a Case Set:
  * View Enforcement Center
  * View Enforcement Tasks
  * View user accounts and roles (under Users Management) - for the list of Assignees
  * Edit Enforcement
  * Run Enforcement
  * View Case Management (to view the Cases page)
  * Add Case Management (to add entries to the Cases page)
  * Edit Case Management (to edit the Cases page)
* To delete a Case Set (from the Case Sets page):
  * Delete Case Management
  * Delete Enforcement
  * Terminate Enforcement Tasks

<Image alt="CaseSets.png" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CaseSets.png" />

## The Case Sets Table

The table lists Case Sets with the following details:

* **Structure** - Icons representing the Case Set structure, including 'Create new case', 'Create Ticket', and 'Create Incident' Enforcement Action icons.

* **Name** - The assigned name of the Case Set.

* **Scheduling Type** - How often or when the Case Set is configured to run.

* **Total Runs** – The total number of times the Case Set has run.

* **Last Run** – The date and time of the Case Set's most recent run.

* **Last Run Status** – The outcome of the last run. For example: Completed, Failed, Partially completed.

* **Last Updated** – The date and time (UTC) the Case Set was last modified.

* **Query Name** - The name of the query that defines the assets the Case Set runs on, as configured in the Select Assets step.

## Creating a Case Set

**To create a new Case Set**

1. Click **Create Case Set**.
2. Use the **Create a Case Set** wizard that opens [to create a new Case Set](/docs/creating-a-case-set).

## Case Set Actions

You can perform the following actions on Case Sets in the system:

### Editing a Case Set

From the **Case Sets** table, you can modify a Case Set's configuration or initiate a run.

<Callout icon="📘" theme="info">
  Note

  * You cannot modify the Case Set's name or the asset type that the query runs on (in step 1 of the wizard).

  * Scheduling changes take effect from the time you apply them. For instance, if you change a weekly schedule to bi-weekly, the new schedule continues based on the original creation date, not a reset.

  * If a user has read-only permission, clicking a row in the table opens the wizard in read-only mode, i.e., all wizard steps are visible but disabled for editing.
</Callout>

**To edit a Case Set**

1. In the **Case Sets** table, click the row of the Case Set that you want to edit. The **Edit a Case Set** wizard opens on step 1.
2. Click any wizard step to make changes in it. In Step 1, you can only select a different query on which to run the Case Set. In this case, the **Query Preview** updates immediately to reflect the count and composition of the new asset criteria.
3. Click **Save** at any step to save your changes or click **Save and Run** in the final step to save changes and immediately run the Case Set.

### Running Case Sets

From the **Case Sets** page, you can manually run one or more Case Sets and track their progress on the Run History page.

**To run Case Sets**

1. Hover over a single Case Set, or select one or more Case Sets.
2. Click the **Run** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunIcon.png) icon or action.

### Deleting Case Sets

From the **Case Sets** page, you can delete one or more Case Sets. Once you confirm deletion, this action is irreversible, and the selected Case Sets are permanently removed from the system.

<Callout icon="📘" theme="info">
  Note

  When deleting a Case Set, all its associated post actions and recurrences are also deleted and stopped.
</Callout>

**To delete Case Sets**

1. Hover over a single Case Set, or select one or more Case Sets.
2. Click the **Delete** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteIconB.png) icon or action.
3. In the confirmation dialog that opens, click **Delete Case Set**/**Delete Case Sets**. The selected Case Sets are completely removed from the system and no longer appear on the table.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).