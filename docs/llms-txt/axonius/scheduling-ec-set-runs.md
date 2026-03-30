# Source: https://docs.axonius.com/docs/scheduling-ec-set-runs.md

# Scheduling Enforcement Set Runs

Axonius supports scheduling an Enforcement Set to run at specified times and under certain conditions. Scheduling criteria are available at the bottom of every Enforcement Set drawer.

You can prioritize multiple Enforcement Sets that are scheduled to run at the same time every global discovery cycle, so that they run in the  order of their assigned priorities. Learn more on how to [set the run priority levels of Enforcement Sets](#setting-the-run-priority).

In a multi-action Enforcement Set, you can also automate the execution of a Post, Success, or Failure Enforcement action to run at a later time. Learn more on [how to delay Enforcement Action runs](/docs/create-ec-set#delaying-enforcement-action-execution).

**To schedule an Enforcement Set run**

1. In the **Create Enforcement Set** drawer, select the **Select Schedule** tab.
2. Under the **Select a Schedule Plan** page that opens, select **On**. A dropdown opens for choosing the run schedule, and the [**Additional Conditions** section](#configuring-additional-run-conditions) is displayed, and can be expanded to set more scheduling conditions.

<Image alt="SchedulePlanOn" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-B4QFZ1DD.png" />

3. [Select a schedule plan and configure it](#configuring-a-schedule-plan).

## Configuring a Schedule Plan

From the **Schedule Plan** dropdown, select a relevant schedule.

<Image alt="Schedule2" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule2.png" />

Each schedule plan is explained in the following sections.

### Every Global Discovery Cycle (Default)

This schedule plan runs the Enforcement Set on the same schedule as the Global Discovery Cycle, at the end of the cycle. See [Discovery Cycle](/docs/discovery-cycle) for more information about Discovery Cycles.
You can [set the run priority level](#setting-the-run-priority) of one or more Enforcement Sets configured to run every Global Discovery Cycle, directly from the **Enforcements** page.

<Callout icon="📘" theme="info">
  Note

  The Enforcement Set runs during the last phase of the Discovery Cycle after adapter fetches are finished, even if they are not successful. You can enable the **Only when following adapter connections successfully completed fetch earlier in discovery cycle** option (see below) to ensure that the Enforcement Set runs only if the adapter fetches are completed successfully.
</Callout>

You can also determine when the schedule plan ends. For more information, see **Ending the Enforcement Set Schedule Plan**.

### Schedule Once

This schedule plan enables a one-time run of the Enforcement Set. Select the date and time on which you want to run it.

<Image alt="Schedule3" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule3.png" />

### Weekly on \[Current Day]

This schedule plan runs the Enforcement Set once a week on the current day. For example, if you set this schedule on a Monday, the dropdown displays a "Weekly on Monday" option.
Under **Run time**, select the exact hour at which you want the run to occur (the default is 13:00). You can also schedule it to run immediately by selecting **Now**.
If you have multiple Enforcement Sets, schedule them to run at different times to reduce network traffic.

<Image alt="Schedule4" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule4.png" />

### Every 12 Hours

This schedule plan runs the Enforcement Set every 12 hours. The runs occur at 00:00 and 12:00.

### Daily

This schedule plan runs the Enforcement Set every day. Under **Run time**, select the exact hour at which you want the run to occur.

### Custom

Use this schedule plan to set a flexible, custom schedule to run your Enforcement Set. With a custom schedule plan, you can:

* Repeat runs every X hours, days, weeks, or months.
* Run the Enforcement Set only on specific days. Upon enabling this toggle, a bar with a tile for each weekday appears. Select the tiles of the days you want to run the Enforcement Set on.
* Run the Enforcement Set only between specific hours.

<Image alt="Schedule7" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule7.png" />

The default option is **Repeat every X hours**. Here you can set specific days and a specific range of hours to run the Enforcement Set. In the example below, we set the run to repeat every one hour, and occur only on Monday and Wednesday, between 08:00 and 14:00:

<Image alt="Schedule8" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule8(1).png" />

<Callout icon="📘" theme="info">
  Note

  In the **Repeat every X hours / days / weeks / months** setting, the value of X must be larger than 0, and the maximum value is 24. Fractions are also possible, for example - Repeat every 0.5 hours.
</Callout>

Select the **Repeat every X days/weeks** to set the run time and also set it to run only on specific days.

Select the **Repeat every X months** to either:

* Schedule the run to occur on every First/Second/Third/Fourth/Fifth weekday of the month. For example - every second Monday of the month:

<Image alt="Schedule10" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule10.png" />

* Schedule the run to occur on a specific day or several specific days of the month. For example - every 15th and 22th of the month:

<Image alt="Schedule11" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Schedule11.png" />

Click the **x** icon next to each day to remove it from the list.
You can also set the Run Time, as explained above.

### Every Successful Adapter Fetch

This schedule plan runs the Enforcement Set following each successful fetch of a single selected adapter connection. This is relevant for adapter fetches from within or outside the Discovery Cycle.
From the **Select Connection** dropdown of configured adapter connections in the system, select a single adapter connection.

<Image alt="ScheduleadapterFetch" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ScheduleadapterFetch.png" />

### Scheduling the Run for the End of the Cycle

If the scheduled run overlaps with a Discovery Cycle, enabling the **Wait until cycle ends** option postpones the run until the end of the cycle. This option is available for all schedule plans except for the default [**Every Global Discovery Cycle**](/docs/scheduling-ec-set-runs#every-global-discovery-cycle-default) and **Every successful adapter fetch**.
Before choosing **Wait until cycle ends**, decide whether running the Enforcement Set on up-to-date data significantly justifies delaying its execution. For example: An Enforcement Set that creates CMDB assets is scheduled to run daily at 11:00. Enabling the Wait until cycle ends option guarantees that this Enforcement Set runs after all assets are fully updated by all adapters and correlations.

<Callout icon="📘" theme="info">
  Note

  The **Wait until cycle ends** option is not relevant when no Discovery Cycle is running at the scheduled trigger time of the Enforcement Set.
</Callout>

### Ending the Enforcement Set Schedule Plan

<Callout icon="📘" theme="info">
  Note

  This option is not available for the **Schedule Once** schedule plan.
</Callout>

To set when the schedule plan ends, select one of the following options:

* **Never** *(default)* - The plan never ends.
* **On** - Select the date on which the plan will end.
* **After** - You can choose to end the plan after X months / days / weeks / occurrences.

<Image alt="EndSchedulePlan" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-BH8SMGQX.png" />

After you set the schedule plan to end after a certain time period (the third option), the system displays the time remaining for this plan. For example, if you set it to end after 3 months, the system displays *Remaining: 3 Months*, and after one month it changes to *Remaining: 2 Months*. The count starts from the moment you click **Save and Run**.
To keep the schedule plan for longer, click **Reset Count**. For example -  if you set the plan to end after 3 months, and after one month, you want it to run for 3 more months, click **Reset Count** and the display will change back to *Remaining: 3 Months*.

<Callout icon="💡" theme="warn">
  Important

  You must click **Save and Run** to be able to select **Reset Count** later.
</Callout>

## Configuring Additional Run Conditions

To set additional conditions for running the Enforcement Set, expand the **Additional Conditions** section. You can add as many conditions as required.

<Image alt="ScheduleAdditionalConditions" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ScheduleAdditionalConditions.png" />

These additional conditions include the following:

* [Running the Enforcement Set on a limited number of results](#limiting-results).

* [Triggering the Enforcement Set only if the selected additional conditions are met](#setting-triggering-conditions).

<Callout icon="📘" theme="info">
  Note

  There is an OR relationship between all the scheduling conditions, meaning that the Enforcement Set runs if even only one of the selected conditions exists.
</Callout>

### Limiting Results

You can run the Enforcement Set on a limited number of assets resulting from the query:

* The top N results.
* Added entities since the last run.

**To limit the run**

1. Under **Limit Results**, select either or both these options, as required:
   * **Run on top N results only** - Runs the Enforcement Set only on the first N assets that match the query. Sorting the query results may result in a different set of top N results.

   * **Run on added entities only** - Runs the Enforcement Set only on assets discovered since the last run.

#### Running the Enforcement Set Only on Added Entities

Every time an Enforcement Set is triggered to run, the following happens:

1. The query defined in the Enforcement Set runs and returns a list of assets.
2. The Enforcement Set runs against that list of assets.
3. The list of assets is saved.

When the **Run on added entities only** checkbox is selected, the list of assets returned in the query (from the second run onward) is compared to the previous run's asset list. Only assets that appear in the new list but were not in the previous list are included in this run.

<Callout icon="📘" theme="info">
  Note

  The first Enforcement Set run is always on all assets matching the query.
</Callout>

**Example**: An Enforcement Set is configured to run on query "devices with AD admin permissions" at the end of every discovery cycle and the **Run on added entities only** checkbox is selected.

* At the end of the first discovery cycle (first run), the query returns assets A, B, and C. So the Enforcement Set runs on assets A, B, and C.
* At the end of the second discovery cycle (second run), the query returns assets B, C, and D. So the Enforcement Set runs only on asset D.

### Setting Triggering Conditions

You can define to trigger the Enforcement Set based on one or more of the following:

* The number of assets returned from the query.
* The number of assets compared to the last run.
* If the selected adapter connections fetched successfully.

#### Checking the Number of Assets

You can select to trigger the Enforcement Set if the number of assets returned from the query is above a certain number, below a certain number, or in a range of numbers (select both options).

**To run the Enforcement Set based on the number of assets returned from the query**

1. Under **Number of Assets**, select one or more of the following options:
   * **If number of assets is above N** - Type a number (N) in the text box. The Enforcement Set runs only when the asset count is above this number. When N is 0 (zero) and no assets match the query, the Enforcement Set is not run.
   * **If number of assets is below N** - Type a number (N)  in the text box. The Enforcement Set runs only when the asset count is below this number.

#### Comparing to Last Run

You can select to trigger the Enforcement Set only if the number of assets returned from the query is more or less than the previous run.
**To run the Enforcement Set based on the number of assets returned from the query compared to the last run**

1. Under **Last Run Comparison**, select one or more of the following options:
   * **If assets have been added since the last execution** - The Enforcement Set runs only if the asset count is higher than the previous run.
   * **If assets have been removed since the last execution** - The Enforcement Set runs only if the asset count is less than the previous run.

<Callout icon="📘" theme="info">
  Note

  If this is the first run, even if you select one of these options, the Enforcement Set runs on all assets that match the Enforcement Set query.
</Callout>

#### Checking Adapter Connections

Select the **Only if the following adapter connections successfully completed** condition to trigger the Enforcement Set run only if selected adapter connections successfully complete their fetches. This ensures that the Enforcement Set runs only on updated asset data.

This condition is available for:

* The **Every global discovery cycle** schedule plan.
* All other schedule plans (except **Every successful adapter fetch**) that have the **Wait until cycle ends** option enabled.

<Callout icon="📘" theme="info">
  Note:

  When you enable this condition and select adapter connections from the dropdown, and then disable this condition, the selected adapter connections are remembered, even without saving them. When you re-enable this condition, the remembered adapter connections are listed.
</Callout>

**To run the Enforcement Set based on adapter connections with successful fetching**

1. Under **Adapter Fetches**, select the **Only if the following adapter connections successfully completed** option, and in the **Select Connections** dropdown, do one of the following:
   * Select an adapter. This selects all its adapter connections. In this case the adapter and all its connections are marked with a checkmark.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterFetchesSelectAdapter.png)

   * Expand an adapter and select one or more of its adapter connections. In this case, the checkbox of the adapter is colored black, and the selected adapter connections are marked with a checkmark.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AdapterFetchesSelectAdapterConnections.png)

## Setting the Run Priority

By default, all Enforcement Sets scheduled to run every global discovery cycle run in the order that they are submitted. You can control the order that Enforcement Sets run by assigning them a run priority level. This is of significance when multiple Enforcement Sets running at the same time are dependent on each other. For example, when an Enforcement Set that removes assets and one that creates CMDB assets in third party systems run at the same time.
Enforcement Sets of a higher priority level run before those of lower priority levels. Run Priorities range from 1 (highest priority; first to run) to 200 (lowest priority; last to run). By default, all runs have priority level 5.  All Enforcement Sets of the same run priority are run in a discovery cycle in the order that they are submitted.
From the **Action Center** page, you can [edit inline the run priority of a single Enforcement Set](#editing-inline-the-run-priority-of-a-single-enforcement-set), or from the **More Actions** menu,[change the priority of one or more Enforcement Sets](#changing-the-run-priority-of-enforcement-sets).

### Editing Inline the Run Priority of a Single Enforcement Set

**To edit inline the run priority of a single Enforcement Set**

1. In the table on the [**Enforcements** page](/docs/enforcement-center-page) , hover over the run priority of an Enforcement Set and click the pencil icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/PencilIcon.png)

<Image alt="RunPriorityInlineEdit" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunPriorityInlineEdit.png" />

The **Edit Run Priority** dialog opens with the current run priority selected.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/EditInlineRunPriority.png)

2. From the dropdown, select the new run priority (1-200), and then click **Save Changes**. The run priority of the Enforcement Set is updated in the Enforcement Sets table **Priority** column.

### Changing the Run Priority of Enforcement Sets

Use an action to change the run priority of one or more Enforcement Sets with **Scheduling Type`=`Every global discovery cycle**.

<Callout icon="📘" theme="info">
  Note

  The **Change Run Priority** action is disabled in the following cases:

  * When you select all Enforcement Sets.

  * If any of your selected Enforcement Sets are not scheduled every global discovery cycle.

  In this case, the **Change Run Priority** tooltip notifies: *Your selection includes sets with different schedules, set order selection is limited to discovery cycle scheduled sets only*
</Callout>

**To change the run priority of Enforcement Sets**

1. In the table on the [**Enforcement Sets** page](/docs/enforcement-center-page), do one of the following:

   * To change the run priority of a single Enforcement Set: Hover over the row of an Enforcement Set, and then at the end of the row, from the 3-dot **More Actions** menu, click the **Change Run Priority** action ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeRunPriorityAction.png).

   * To change the run priority of one or more Enforcement Sets: Select the checkboxes of the Enforcement Sets that you want to change their run priority and then on the top right of the table, from the 3-dot **More Actions** menu, click the **Change Run Priority** action ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeRunPriorityAction.png).

   Ensure that the selected Enforcement Sets have **Scheduling Type`=`Every global discovery cycle**. The number of selected Enforcement Sets is displayed next to **Total** above the left side of the table (see screen below).

   <Image alt="ActionsMenuNewRunPriority" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ActionsMenuNewRunPriority.png" />

   The **Change Run Priority** dialog opens with the current run priority selected. In the case that you selected Enforcement Sets of different run priorities, dialog opens with **Multiple priorities** selected, as in the screen below, where the selected Enforcement Sets have run priorities 5,4, and 5.

<Image alt="ChangeRunPriority" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ChangeRunPriority.png" />

2. In the **Change Run Priority** dialog, select from the dropdown, the new priority level (1-200), and then click **Apply**. The run priority of the selected Enforcement Sets is updated in the table.

## Managing Enforcement Sets Sechduling

Use the **Manage Scheduling> Turn Scheduling On / Turn Scheduling Off** action to turn on or off scheduling of one or more Enforcement Sets directly from the Enforcement Sets table.
When you turn off scheduling, the system saves the Scheduling settings so that if you later turn on scheduling, the Enforcement Sets will be configured once again with these settings.
![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ManageSchedulingActions.png)

<Callout icon="📘" theme="info">
  Note

  * The **Turn Scheduling Off** action is disabled if all selected Enforcement Actions are configured with no scheduling.
  * The **Turn Scheduling On** action is disabled if all selected Enforcement Actions are configured with scheduling.
  * For a selection of Enforcement Actions - some with scheduling and some without, **Turn Scheduling Off** and **Turn Scheduling On** are both enabled. Clicking **Turn Scheduling Off** does not affect Enforcement Actions already configured without scheduling and **Turn Scheduling On** does not affect those with scheduling.
</Callout>

**To turn on/off the scheduling of Enforcement Sets**

1. In the table on the [**Enforcements** page](/docs/enforcement-center-page), hover over the row of an Enforcement Set or select the checkboxes of one or more Enforcement Sets, and then, from the 3-dot **More Actions** menu, click **Manage Scheduling> Turn Scheduling On / Turn Scheduling Off**.
   The number of selected Enforcement Sets is displayed next to **Total** above the left side of the table.

2. In the confirmation dialog that opens, click **Turn Scheduling Off** / **Turn Scheduling On**.
   Scheduling is enabled/disabled for the selected Enforcement Sets. The **Scheduling Type** column in the table is updated accordingly.

   <Image alt="RepeatEveryXDays" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RepeatEveryXDays.png" />