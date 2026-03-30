# Source: https://docs.axonius.com/docs/findings-center-page.md

# Findings Center

Use the **Findings Center**  to:

* View and manage all Findings in your system.
* View a centralized summary of information about each Finding in your system, including the source of the Finding, the number of alerts it has so far created, as well as information on the latest alert created by the Finding.
* View alerts triggered by each Finding originating from the Findings Center.
* View system alerts triggered by each Finding originating from Enforcement Sets.
* Create new custom Findings.

<Callout icon="📘" theme="info">
  Note

  By default, Admin users have access to the **Findings Center**. In order to use this module, **Findings** permissions must be assigned. In addition, **View notifications** under **System Management** must be cleared.
</Callout>

Whenever a threshold is crossed, the system sends an alert directly to the **Findings Center** under the Finding that triggered it. You can view the triggered alerts in one place - the  **Findings Center**, instead of actively having to check various places, for instance opening dashboards every day to see if there have been significant changes in any of them. You can also use the alerting system to notify teams when a milestone is met or about ongoing remediation efforts.

The  **Findings Center** supports all query and entity types - assets and system events (such as adapter fetches and activity logs), enabling you to monitor and manage the Axonius system itself.

**To open the Findings Center**

* In the Axonius Platform side menu, click the Findings Center icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingsIcon.png) <br />
  The **Findings Center** opens, displays in the main pane a table of  **All Findings** defined in the system.
  ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingsCenterwithCategoryPaneB.png)

  * If one or more alerts have been triggered in the Findings Center since you last visited it, a blue notification dot appears on the Findings Center icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NotificationDotOnIcon.png) in the side menu. This dot is removed once you open the Findings Center page.
  * Findings are organized in the left [Category pane](#category-pane) according to their categories.

## Findings Table

From the [Category pane](#category-pane), you can open the Findings page of any category to see its Findings.
The **Findings** table on this page lists the Findings of that category.

<Callout icon="📘" theme="info">
  Note

  The **All Findings** category opens a table with all Findings defined in Axonius.
</Callout>

* When a Finding is created, it is added to the bottom of the table in the Findings Center.
* When a Finding triggers an alert it moves to the top row of the table and a New label ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewBadge.png) is displayed under its **Latest Alert Status**.
* When you move a Finding to *Closed* status, it moves to below those in *Open* status.
* When you move a Finding to *In Progress* or *Canceled* status, it moves to below those in *Closed* status.

This means that the Findings table is organized as follows:

* The Findings in *Open* status that triggered alerts are sorted on the top part of the table in descending order of when they triggered their last alert, meaning that the Finding that last triggered an alert is on top of the table.
* The Findings moved to *Closed* status appear below those in *Open* status in descending order of when they triggered their last alert.
* The Findings moved to *In Progress* and *Canceled* status appear below those in *Closed* status.
* The Findings that did not yet trigger an alert are sorted on the bottom part of the table in ascending order of when they were added to the Findings Center. This means that the last Finding added to the Findings Center, which has not yet triggered an alert, is on the bottom row of the table.

The Findings table provides the following information for each unmuted Finding:

* **Finding Name** - The name assigned to the Finding.
* **Message** - The system message that notified about the alert. Hover over the tooltip to display a detailed description of the alert.
* **Latest Alert ID** - The ID of the latest alert triggered by this Finding.
* **Latest Alert Status** - The status of the latest alert triggered by the Finding. Available statuses: *Open*, *In Progress*, *Closed*, *Canceled*.
  * A **New** label ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewBadge.png) indicates that this Finding triggered an alert in *Open* status since the last time you visited this Findings page. The Finding is bumped to the top of the list.
  * The label is removed when you click the Finding to open its **Finding Info** drawer.
  * All labels are removed from all Findings when you leave the Findings page.
  * You can [manually change the status of the latest alert](#inline-editing-the-status-of-the-latest-alert) without having to navigate to the Alerts History page.
* **Latest Alert Created** - The timestamp in UTC of the latest alert triggered by the Finding.
* **Severity** - Severity of the Finding. Available options are: *Informational*, *Low*, *Medium*, *High*, *Critical*. The severity of an alert is equivalent to the severity of the Finding that triggered it. The severity of Findings from sources other than Findings Center is fixed per source and is not user configurable.
* **Check and Notify** - The schedule according to which the Finding is configured to check the entity. Relevant for Findings originating from the Findings Center. N/A for other Findings.
* **Asset Type** - The asset type that the Finding is configured to check. This is the Module selected in the Trigger Condition.
* **Source** - The source of the Finding. For example, Findings Center, Enforcement Center, System. Learn more about the various [alert sources](/docs/viewing-alert-information).
* **Category** - The category of the Finding.
* **Total Alerts** - The number of times that the Finding checked that the condition exists and created an alert until and including the most recent notification. Alerts created during muting of notifications are only added to the count the next time an alert is created with notification.

## Category Pane

The Category pane on the left side of the Findings Center page organizes the Findings by category. This organization enables you to easily find related Findings. <br />
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CategoryPane.png)

The following are the available Findings categories:

* **All Findings** - Includes all Findings from all categories. Note that you cannot classify a Finding with the **All Findings** category.
* **Cyber Asset Management** - By default, alerts from Enforcement actions are accessed through this category.
* **Internal System** - Alerts from system settings can be accessed from the Findings of this category.
* **SaaS Management** - Visible if SaaS management is enabled.
* **Identity Management** - Visible if Identity management is enabled.

To the right of each category is displayed either:

* A New label ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/NewBadge.png) if at least one Finding in the category triggered new alerts since the last time you visited the Findings Center. On the left of each New label appears the number of new alerts triggered by Findings in that category. This is the number of New labels that you see in the Findings table of that category.

* Opening a category with a New label opens the category's Findings table with a New label in the **Latest Alert Status** column of each Finding that has new alerts. This ensures that you can identify the Findings with new alerts and review them one by one. When you leave the table of a category (except for the **All Findings** category), the New label is removed from all Findings in the table of that category. The label near the category (except for the **All Findings** category) is removed when you open the category's Findings page.

* Labels are removed from all categories when all the specific categories (under **All Findings**) have been opened or you leave the Findings Center.

* You can search for a category using the **Search** box at the top of the **Category** pane.

## Findings Retention

The Findings Center page always displays the latest 100,000 Findings.

## Searching and Filtering

You can filter the Findings in the system. You can then use the filters to create queries based on the filters and also save them as queries which can be used later on.[Read more about queries based on filters.](/docs/creating-queries-filters)

<Image alt="FindingsFilter" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/FindingsFilter.png" />

<Callout icon="📘" theme="info">
  Note

  * The filters show only those options that appear in the Findings table.

  * For each filter with a dropdown selection, you can select one or more options.

  * If you want to filter by many options, you can click **Select All** to select all options, and then click those options that you want to clear.
</Callout>

The following filters are available:

* **Search Findings** -  Enter free text to search for Findings by Finding name.

* **Latest alert status** - The status of the latest alert triggered by the Findings.

* **Severity** - The severity of the Finding.

* **Category** - The category of the Finding.

* **Asset Type** - Select one or more asset types on which the Findings run. The system returns all relevant Findings.

* **From - To** - Select the period of time for which to display the latest alerts triggered by Findings.

* Click **From** and select the date and optionally the time (right pane) from which to display results. Repeat for **To** and then click **OK**.

  * Both **From** and **To** dates must be filled in and be earlier than or on the current date.
  * Click the arrows to the left/right of the Month/Year header to open the previous/next month's or year's calendar page.
  * To filter results only for a specific date, select the same date twice.

  <Image align="center" border={false} src="https://files.readme.io/6b19ca195289e1ee67a949b991005bec6fc46d86a40a9b080d92b17d01ead376-FromToFilter.png" />

You can click the following to perform quick actions on filters:

* **Select All** - Selects all options in a specific filter.
* **Clear All** - Clears all selections in a specific filter.
* **Reset** - Clears all filters and displays the entire table.

## Performing Actions on Findings

### Creating a New Finding

From the Findings Center, you can create a new Finding to check assets of a selected type for specific criteria. The new Finding is added to the bottom of the Findings table. Learn [how to create and configure a new Finding](/docs/creating-a-finding).

### Inline Editing the Status of the Latest Alert

In the **Findings** table, you can use inline editing to manually change the status of the **Latest Alert Status** of a Finding, without having to open the **Finding info** drawer and navigate to its **Alerts History** page.
After beginning to actively investigate the cause of the alert, you can manually change the status to *In Progress*. Then, depending on the results of your investigation, you can change the status to *Closed* or *Canceled*.
All status changes are logged in the audit log.
For example: alert id 123 active\_directory\_adapter status was changed from *Open* to *In Progress*.

**To change the status of the latest Alert of a Finding**

1. In the **Findings** table, hover over the entry in the **Latest Alert Status** column, and click the **Change Status** ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeStatusIcon.png) icon.
2. In the **Change Status** dialog that opens, from the dropdown, select the new status:
   * **Open** - You viewed the cause of the alert.
   * **In Progress** - You have started investigating the cause of the alert.
   * **Closed** - The problem causing the alert has been solved.
   * **Canceled** - The alert is false positive.

<Image alt="ChangeStatusDropdown" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeStatusDropdown.png" />

3. Click **Change Status**. The alert moves to below the *Open* alerts in the table and its alert status changes accordingly.

### Creating a Case From a Finding

Directly from the [Findings table](#findings-table), you can create a Case based on a Finding.
Learn [how to Create a Case from the Findings Center](/docs/creating-a-case-from-the-findings-center-new).

### Deleting Findings

Directly from the [Findings table](#findings-table), you can delete one or more Findings (Custom). Learn [how to delete Findings](/docs/managing-findings#deleting-findings).

### Deactivating Findings

Directly from the [Findings table](#findings-table), you can deactivate one or more Findings (Custom). Learn [how to deactivate Findings](/docs/managing-findings#deactivating-findings).

### Duplicating a Finding

You can create a new Finding that copies the configuration of an existing one. Duplicating a Finding is useful if you want to create a new Finding similar to an existing one.

**To duplicate a Finding**

1. In the **Findings** table, do one of the following:
   * Hover over the row of a Finding, and then at the end of the row, click the **Duplicate** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DuplicateIcon\(1\).png).
   * Select the checkbox next to a single Finding, and then on the top right of the table, click the **Duplicate** action ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DuplicateAction\(1\).png).

The 'Make a copy of ' dialog opens. The Finding name provided is *Copy of* . Change the name if you like.

2. Click **Create a Copy**. The **Duplicate Finding** drawer opens with all fields and  configurations from the original Finding populated. Only the name has been changed (with the 'Copy of' prefix).

3. Make any necessary changes to the new Finding's configuration, and then click **Duplicate**.  A pop-up notification message informs that the Finding was created successfully. The new Finding now appears in the Findings table.

***

For general information about working with tables, refer to [Working with Tables](https://docs.axonius.com/docs/working-with-tables).