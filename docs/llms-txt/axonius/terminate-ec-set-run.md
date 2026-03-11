# Source: https://docs.axonius.com/docs/terminate-ec-set-run.md

# Terminating an Enforcement Set Run

From the **Run History** page, you can manually terminate one or more *In Progress* (running) or *Pending* (waiting to run) Enforcement Sets.

An Enforcement Set can include several Enforcement Actions. When an Enforcement Set that includes more than one Enforcement Action is terminated, one or more of the following can happen for any Action in that Enforcement Set:

* An Action fully completed its run - This Action’s changes remain and cannot be undone.
* An Action is currently running - The Action is stopped. Any change made by this action before it was terminated remains and cannot be undone.
* An Action has not started to run *(Pending)* - No changes to any asset are made, and the Action does not run.

<Callout icon="📘" theme="info">
  Note

  There is no *undo* for Enforcement Actions. After you confirm termination, the action is irreversible and the selected runs are permanently terminated.
</Callout>

**To terminate one or more Enforcement Set runs**

1. From the [**Enforcements** page](using-the-ec-page#opening-the-enforcements-page), click **Run History**.

2. In the **Run History** table, do either of the following:
   * Hover over the row of a single Enforcement Set run (in *In Progress* or *Pending* status), and then at the end of the row, click the **Terminate** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TerminateIcon.png).
   * Bulk select one or more Enforcement Set runs and then on the top right of the table, click the ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/TerminateIcon.png) **Terminate Task** action.\
     This option is available only when one of the selected Enforcement Sets has a result (under the **Result** column) of *In Progress* or *Pending*.
     * Select the checkboxes of the Enforcement Set runs that you want to terminate.
     * Select all Enforcement Set runs on the page (mark the checkbox in the table header) or in the entire table (**Select All**).  (You can click **Clear All** to undo this action and clear the entire table.)
       The number of selected records is displayed next to the **Total** results. For example, **Total**  6/ 2 selected.

3. The system asks you to confirm the termination of the selected Enforcement Set runs. This action is irreversible. Click **Terminate** to confirm.
   A notification pop-up appears specifying the number of Enforcement Set runs that were terminated. In the table, the **Result** of the Enforcement Set runs changes to *Terminated*, and the **End Time** is filled with the date and time.