# Source: https://docs.axonius.com/docs/scheduling-workflow-runs.md

# Scheduling Workflow Runs

Axonius supports scheduling Workflows to run at specified times. This is relevant only for Workflows with a scheduled triggering Action. You can also [configure when the schedule plan ends](#ending-the-workflow-schedule-plan).

## Scheduling Workflow Runs

This section describes the available schedule plans for Workflows with a Scheduled triggering action.

**To schedule a Workflow run**

1. In the **Trigger Type** pane of a **Scheduled** action, under **Select a Schedule Plan**, choose from the dropdown a schedule plan.

![WFScheduledOptions.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/WFScheduledOptions.png)

Each schedule plan is explained in the following sections.

### Every Global Discovery Cycle (Default)

This schedule plan runs the Workflow at the end of each Global Discovery Cycle. Refer to [Discovery Cycle](/docs/discovery-cycle) for more information.

### Schedule Once

This schedule plan runs the Workflow once at a selected date and time.

<Callout icon="📘" theme="info">
  Note

  If scheduling for the current day, select a time later than the current time.
</Callout>

**To set the one-time run**

1. In **Select date and time**, click the Calendar icon.
2. In the calendar that opens, select the date and optionally the time.
3. Click **Ok**.

![SchedulePlanOnce.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanOnce.png)

### Weekly on \[Current Day]

This schedule plan runs the Workflow once a week on the current day. For example, if you set this schedule on a Wednesday, the dropdown displays a **Weekly on Wednesday** option.

Under **Run time**, select the exact hour to run (default is 13:00) or choose **Now** to run immediately.

<Callout icon="📘" theme="info">
  Note

  Schedule multiple workflows at different times to reduce network traffic.
</Callout>

![SchedulePlanWeekly.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanWeekly.png)

### Every 12 Hours

This schedule plan runs the Workflow every 12 hours. The runs occur at 00:00 and 12:00.

### Daily

This schedule plan runs the Workflow daily. Under **Run time**, select the hour at which you want the run to occur. The default run time is 13:00.

### Custom

Use this schedule plan to set a flexible, custom schedule to run your Workflow. With a custom schedule plan, you can:

* Repeat runs every X hours, days, weeks, or months (X `>` 0, max 24, fractions allowed, for example - Repeat every 0.5 hours).
* Run the Workflow on specific days. Upon enabling this toggle, a bar with a tile for each weekday appears. Select the tiles of the run days.
* Run the Workflow only between specific hours.

![SchedulePlanCustom.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanCustom.png)

The default option is **Repeat every 2 hours**. Here you can set specific days and a specific range of hours to run the Workflow. In the example below, the run is set to repeat every two hours on Mondays and Wednesdays, between 08:00 and 14:00.

![SchedulePlanCustomExample1.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanCustomExample1.png)

Select **Repeat every X days** or **Repeat every X weeks** to set the run time and also set it to run only on specific days.

<Callout icon="📘" theme="info">
  Note

  When you set the schedule to run every two days and the run day does not fall on one of the  selected specific days ()if configured), the Workflow doesn't run on that day.
</Callout>

Select the **Repeat every X months** to either:

* Schedule the run to occur on every First/Second/Third/Fourth/Fifth weekday of the month. For example - every second Monday of the month:

![SchedulePlanCustomExample2.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanCustomExample2.png)

* Schedule the run to occur on a specific day or several specific days of the month. For example - every 6th and 22th of the month:

![SchedulePlanCustomExample3.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanCustomExample3.png)

Click the **x** icon next to each day to remove it from the list.
You can also set the Run Time, as explained above.

### Every Successful Adapter Fetch

This schedule plan runs the Workflow after each successful fetch of a single selected adapter connection. This is relevant for adapter fetches from within or outside the Discovery Cycle.
From the **Select Connection** dropdown of configured adapter connections in the system, select a single adapter connection.

![SchedulePlanAdapterFetch.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SchedulePlanAdapterFetch.png)

## Scheduling the Workflow Run for the End of the Cycle

If the scheduled run overlaps with a Discovery Cycle, enabling the **Wait until cycle ends** option postpones the run until the end of the cycle. This option is available for all schedule plans except for the default [**Every Global Discovery Cycle**](/docs/new-scheduling-enforcement-set-runs#every-global-discovery-cycle-default) and **Every successful adapter fetch**.
Before choosing **Wait until cycle ends**, decide whether running the Workflow on up-to-date data significantly justifies delaying its execution.

<Callout icon="📘" theme="info">
  Note

  The **Wait until cycle ends** option is not relevant when no Discovery Cycle is running at the scheduled trigger time of the Workflow.
</Callout>

## Ending the Workflow Schedule Plan

<Callout icon="📘" theme="info">
  Note

  This option is not available for the **Schedule Once** schedule plan.
</Callout>

To set when the schedule plan ends, select one of the following options:

* **Never** *(default)* - The plan never ends.
* **On** - Select the date on which the plan will end.
* **After** - End the plan after X months, days, weeks, or occurrences.

![EndSchedulePlan](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/image-BH8SMGQX.png)

* After you set the schedule plan to end after a certain time period (the third option), the system displays the time remaining for this plan. For example, if you set it to end after 3 months, the system displays *Remaining: 3 Months*, and after one month it changes to *Remaining: 2 Months*. The count starts from the moment you click **Save and Run**.

* Click **Reset Count** to extend the schedule. For example -  if you set the plan to end after 3 months, and after one month, you want it to run for 3 more months, click **Reset Count** and the display will change back to *Remaining: 3 Months*.

<Callout icon="💡" theme="warn">
  Important

  You must click **Save and Run** to be able to select **Reset Count** later.
</Callout>