# Source: https://docs.axonius.com/docs/campaigns-page.md

# Access Reviews Page

## Introduction

Use **Access Reviews** to set up campaigns to assess the necessity of users' previously granted access to software, applications, and permissions in your organization. Campaigns allow you to carry out such assessments periodically and determine whether to approve or revoke user access.

For example, if your organization pays a large sum of money for Figma licenses, you can create a Campaign to determine which users should continue having a license and which users should have their license revoked.

## Access Reviews Page

When you open Access Reviews, the Campaigns page displays a list of all Campaigns in the system which are in your data scope, and supports the options to track the progress of existing Campaigns, create a new Campaign, edit a Campaign, or delete or terminate one or more Campaigns.
From the **Access Reviews** page, you can:

* View a list of all the Campaigns created in your data scope, view their information, monitor their status, and modify, delete, or terminate Campaigns, as required.
* [View the entire configuration of a selected Campaign](/docs/viewing-campaign-information).
* [Create a new Campaign](/docs/creating-a-new-campaign).
* [Manually run a Campaign](/docs/running-a-campaign#running-the-campaign) or [schedule a Campaign](/docs/running-a-campaign#scheduling-the-campaign) to automatically run at a later date.
* View a [Campaign's run history](/docs/viewing-campaign-run-history), including all Approvers' responses.

To open the Access Reviews page, in the left menu, select the **Access Reviews**  icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AccessReviewsIcon.png).
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CampaignsPage.png)

The total number of saved Campaigns is displayed above the left side of the table. For example, **Total 2**.

## Campaigns General Information

The **Access Reviews** page provides the following information for each Campaign, sorted in a **Start Date** descending order:

* **Campaign Name** - The name of the Campaign.
* **Query** - The query used to determine the Campaign target audience, applications, permissions, roles, and approvers.
* **Users** - The number of users returned by the query.
* **Applications** - The name and icons of applications returned by the query. If there are more than two applications, hover over the number (for example, **+2**) to display a list of the additional applications.
* **Approvers** - The number of approvers returned by the query.
* **Message Method** - The method used to send a message on the Campaign to Approvers. Available methods: **Slack**, **Teams**.
* **Revoke Action** - The type of action that is taken when the Approver decides to revoke a user's access to an application:
  * **Update in Axonius** - Writes to the Axonius **Campaigns Approval** custom field that the Campaign permissions are revoked. Does not take any actual action to revoke the license or permissions.
  * **Revoke Access** - Writes to the Axonius **Campaigns Approval** custom field that the Campaign permissions are revoked, and also performs an action to revoke the relevant application(s) from the User.
* **Status** - The status of the Campaign. Available statuses are:
  * **Draft** - One or more steps of the Campaign have been configured. The Campaign has not yet begun to run.
  * **Scheduled** - The Campaign is fully configured and scheduled to run on a specific date. The scheduled run date is displayed under **Start Date** (next column in the table).
  * **In Progress** - The Campaign has begun to run. The date and time when the run began is displayed under **Start Date** (next column in the table).
  * **Terminated** - The user stopped an *In Progress*  Campaign using the **Terminate** action. The date and time that the run terminated is displayed under **End Date**.
  * **Completed** - All Campaign responses have been submitted and required actions have been performed. Or, the configured **End Date** of the running Campaign has been reached.
* **Start Date** - The date and time that an *In Progress* Campaign started to run, or the date that a *Scheduled* Campaign is scheduled to begin running.
* **End Date** - The date and time that a running Campaign goes into *Completed* status, or the Campaign End Date, if configured, of a Campaign that has not yet completed.

## Searching and Filtering Campaigns

Filter the campaigns in the table to view only those that are relevant to you. For example, all campaigns that are set up to review a specific application. You can then create System Queries based on the filters and also save the filters as system queries for later use. Learn more about [System Queries based on filters](/docs/creating-queries-filters).

<Image alt="CampaignsFilter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CampaignsFilter.png" />

The following filters are available:

* **Search** - Search for any text in the Campaign fields.

* **Campaign Name** - The name or names of Campaigns.

* **Status** - The status or statuses of the Campaigns. Available statuses: **Draft**, **In Progress**, **Scheduled**, **Terminated**, **Completed**.

* **Query** - The query or queries used to define the Campaign.

* **Applications** - The application or applications returned by the Campaign query.

* **Message Method** - The message methods used to broadcast the Campaign. Available message methods: **Slack**, **Teams**.

* **Revoke Action** - The action used to revoke the Campaigns: **Update in Axonius** or **Revoke Access** (see explanation in [Campaigns General Information](/docs/campaigns-page#campaigns-general-information)).

* **From - To** - The Campaigns that were created in the specified period of time.
  * To set the date range, select two dates.
  * To filter Campaigns only for a specific date, select the same date twice.
  * Click **Select Time** in the date range picker to include specific times in the date range.
  * Click **Ok** to set the Date Range filter.

* Select **Clear All** to clear all selections in a specific filter.

* Select **Reset**  to clear all filters and display all Campaigns.

## Viewing Campaign Details

You can click any *In Progress*, *Scheduled*, *Completed*, or *Terminated* Campaign in the table on the Campaigns page to open its **Campaign** drawer. Learn more about [Campaign details](/docs/viewing-campaign-information) shown in the **Campaign** drawer.

## Viewing Campaign Run History

Click an *In Progress*, *Scheduled*, *Completed*, or *Terminated* Campaign on the Campaigns page to open its [run history](/docs/viewing-campaign-run-history).

## Creating a New Campaign

Above the Filter area on the right, select **Create Campaign** to begin creating a Campaign with the **Create New Campaign** wizard. Learn how to [create a new Campaign](/docs/creating-a-new-campaign).

## Campaign Actions

You can perform the following actions on Campaigns in the system:

* [**Edit**](#editing-a-campaign) - Modify the configuration of a Campaign that is in *Draft* status.
* [**Terminate**](#terminating-campaigns) - Manually end one or more running Campaigns (in *In Progress* status).
* [**Delete**](#deleting-campaigns) - Delete one or more Campaigns that have not yet begun to run (in *Draft* or *Scheduled* status).

### Editing a Campaign

From the **Campaigns** table, you can edit a Campaign that is in *Draft*  status. This includes modifying the configuration in any of the three wizard steps, or beginning to run the Campaign or scheduling the Campaign run from the Summary step 4 in the wizard.

<Callout icon="📘" theme="info">
  Note

  To edit a Campaign, an Edit Enforcement Center permission is required.
</Callout>

**To edit a Campaign**

1. In the **Campaigns** table, hover over the row of a Campaign, and then at the end of the row, click the **Edit** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionsHover-EditIcon.png) or select the checkbox of the Campaign that you want to edit (the number of selected records (1) is displayed next to the **Total** results: **Total**  1 / 1 selected), and then on the top right of the table, click **Edit** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditAction.png).

2. The first step of the wizard opens. Wait for the **Query Preview** to be generated, and then click any wizard step to make changes. From Step 4, you can also click **Run Campaign** to begin running the Campaign, or **Schedule Campaign** to schedule the Campaign run for a later date. After making a modification, a popup notification appears on the bottom right of the step notifying that **Changes saved** or **Saving changes failed**.

3. When done, click **Close**. The Campaigns page opens, showing the modifications made to the Campaign.

### Terminating Campaigns

From the **Campaigns** page, you can manually terminate one or more *In Progress* (running) Campaigns. After you confirm termination, the action is irreversible and the selected Campaigns are permanently terminated.

<Callout icon="📘" theme="info">
  Note

  You can also terminate an *In Progress* campaign from the header of its [Campaign drawer](/docs/viewing-campaign-information).
</Callout>

**To terminate one or more Campaigns**

1. In the **Campaigns** table, do either of the following:
   * Hover over the row of a single Campaign (in *In Progress* status), and then at the end of the row, click the **Terminate** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TerminateIcon.png).
   * Bulk terminate one or more Campaigns and then on the top right of the table, click the **Terminate** action ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TerminateAction.png).

     * Select the checkboxes of the Campaigns that you want to terminate (in *In Progress* status).
     * Select all Campaigns on the page (mark the checkbox in the table header) or in the table (**Select All**).  (You can click **Clear All** to undo this action and clear the entire table). This is only relevant when all Campaigns on the page or table are in *In Progress* status.

     The number of selected records is displayed next to the **Total** results. For example, **Total**  6/ 2 selected.
2. The system asks you to confirm the termination of the selected Campaigns. This action is irreversible. Click **Terminate** to confirm.

The selected Campaigns are terminated. A popup notifies that the Campaigns terminated successfully. In the table, the **Status** of the Campaign changes to *Terminated* and the **End Date** is filled with the date and time.

### Deleting Campaigns

From the **Campaigns** table, you can delete one or more Campaigns that haven't yet begun to run (i.e., in *Draft* or *Scheduled* status), provided that you have Enforcement Set permissions. Once you confirm deletion, the action is irreversible and the selected Campaigns are permanently deleted.

<Callout icon="📘" theme="info">
  Note

  You can also delete a *Scheduled* campaign from the header of its [Campaign drawer](/docs/viewing-campaign-information).
</Callout>

**To delete one or more Campaigns**

1. In the **Campaigns** table, do either of the following:
   * Hover over the row of a single Campaign (in *Draft* or in *Scheduled* status), and then at the end of the row, click the **Delete** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteIconB.png).
   * Bulk delete one or more Campaigns and then on the top right of the table, click the **Delete** action ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DeleteAction\(1\).png).

     * Select the checkboxes of the Campaigns that you want to delete (in *Draft* or in *Scheduled* status).
     * Select all Campaigns on the page (mark the checkbox in the table header) or in the table (**Select All**).  (You can click **Clear All** to undo this action and clear the entire table). This is only relevant when all Campaigns on the page or table are in *Draft* or in *Scheduled* status.

     The number of selected records is displayed next to the **Total** results. For example, **Total**  6/ 2 selected.
2. The system asks you to confirm the deletion of the selected Campaigns. This action is irreversible. Click **Delete** to confirm.
   The selected Campaigns are deleted. A popup notifies that the Campaigns were successfully deleted. The selected Campaigns are completely deleted from the system and no longer appear on the table.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).