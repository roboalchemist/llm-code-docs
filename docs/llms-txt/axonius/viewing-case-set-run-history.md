# Source: https://docs.axonius.com/docs/viewing-case-set-run-history.md

# Viewing Case Set Run History

The **Run History** page provides a comprehensive overview of all past Case Set runs, helping you quickly understand the outcome of each run. You can also click a Run to view its details.

<Image align="center" alt="CaseSetsRunHistory.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CaseSetsRunHistory.png" className="border" />

## Accessing the Run History Page

You can open the **Run History** page of all Case Sets directly from the **Case Sets** page.

**To open the run history**

* **Same tab:** In the upper-right corner of the [**Case Sets** page](/docs/case-sets-page), click the **Case Sets Run History** link.  Use the browser's Back arrow to return to the **Case Sets** page.

<Image align="center" alt="RunHistoryButtonCaseSet.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunHistoryButtonCaseSet.png" className="border" />

* **New tab:** In the upper-right corner of the [**Case Sets** page](/docs/case-sets-page), right-click the **Case Sets Run History** link and from the context menu that opens, click **Open in new tab**.

<Image align="center" alt="RunHistoryButtonCaseSetNewTab.png" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunHistoryButtonCaseSetNewTab.png" className="border" />

## Elements of the Run History Page

The **Run History** page comprises the following main elements:

* Search/Filter bar - For refining displayed results.
* Total runs performed - Displays the number of runs matching current criteria.
* Run History table - A detailed list of Case Set runs.

### Run History Table

Each row in the Run History table represents a single Case Set run and includes the following fields by default:

* **Structure** -  Icons indicating the Enforcement actions used in the Case Set. Hovering over the icons displays a table of icons in the structure and their Enforcement Action names.

* **Run** - 'Run' followed by the run ID number.

* **Case Set Name** – The name of the Case Set.

* **Scheduling** - The configured schedule. Learn more on [scheduling options (similar to Enforcement Set)](/docs/scheduling-ec-set-runs#configuring-a-schedule-plan).

* **Result** - The outcome of the run (Completed, Delayed, Failed, In Progress, Partially, Pending,Terminated).

* **Query Name** – The saved query that determines on which assets the Case Set was run.

* **Start Time** – The date and time the run began.

* **End Time** – The date and time the run concluded.

* **Duration** - The calculated total fetch duration in HH:MM:SS.ss format.

* **Affected Assets** - The total number of assets matching the query.

* **Success** – The number of assets on which the Case Set ran successfully.

* **Failed** - The number of assets on which the Case Set failed.

* **Discovery Cycle** - The identifier of the discovery cycle in which the activity occurred. This is presented as the start date and time of the discovery cycle.

### Filtering the Run History Table

You can filter the Run History table using the following criteria:

* **Search** - Free-text search across all text fields.

* **Name** - Filter by Case Set name.

* **Action Name** - Filter by included Enforcement Actions.

* **Result** - Filter by Case Set run outcome:
  * **Completed** - Shows all Case Set runs that have finished.

  * **Delayed** - Shows all Case Sets scheduled to run at a later time.

  * **Failed** - Shows all Case Sets where all Actions failed.

  * **In Progress** - Shows all Case Sets that are still running.

  * **Partially** - Shows all Case Sets where at least one action (but not all) failed.

  * **Pending** - Shows all Case Sets that are queued to run.

  * **Terminated** - Shows all Case Sets whose run was terminated.

* **Duration** - From the dropdown, select an operator (**Equal to**, **Greater than**, or **Less than**) and enter the time duration (in HH:MM:SS.ss) format) that you want to filter.
  * To set fractional seconds, highlight **ss** and enter a number up to 99.
  * To set seconds, highlight **SS** and enter a number up to 59.
  * To set minutes, highlight **MM** and enter a number up to 59.
  * To set hours, highlight **HH** and enter a number up to 99.

<Image align="center" alt="SelectOperator" border={true} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SelectOperator.png" className="border" />

<Callout icon="📘" theme="info">
  Note

  It can be very useful to filter the Run History table by **Duration** to view all the runs that were lengthier than expected. These "bad" runs can then be examined to check out if there is a problem, and if yes, attempt to resolve it.
</Callout>

* **Discovery Cycle** - Filter by specific Discovery Cycle(s).
* **Start time, End time** - Filter by the date the Case Set was run.

The total number of Case Set runs matching the selected criteria is displayed on the top left, below the Filter bar. When no search criteria is selected, the total results represent the total number of runs.

### Run History Retention

The Run History page always displays the most recent 100,000 runs.

### Identifying and Stopping Planned Future Actions

The Case Sets **Run History** page enables you to observe the roadmap of actions for a specific run and force-stop them if necessary.

1. Navigate to the Case Sets **Run History** page.
2. Select a specific run from the list to open its details.
3. Review the **Structure** section to identify the status of scheduled actions:
   * **Scheduled** - The action is planned to run once the trigger condition is met.
   * **Triggered** - The action has already been initiated.
   * **Terminated** - The action was manually stopped and will not execute.
4. To stop all remaining automation for this specific run, click **Terminate Run**.
5. In the confirmation dialog, click **Yes, Terminate**.

   <Image align="center" border={false} width="70% " src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/img/case_management/Yes%20-%20Terminate.png" />