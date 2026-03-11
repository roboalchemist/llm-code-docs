# Source: https://docs.axonius.com/docs/rerunning-enforcement-sets-from-run-history.md

# Running Enforcement Sets from Run History

You can quickly run Enforcement Sets from the **Run History** page. This feature is particularly useful for running failed Enforcement Sets, without needing to navigate to the Enforcement Set itself to run it.

* Multiple runs of the same Enforcement Set trigger only one run.
* The Enforcement Set runs with the current configuration and not on the configuration set at the time of the past run.
* Existing runs continue in parallel to new runs.
* These runs are logged in the Run History same as the original runs.

**To run one or more Enforcement Sets from the Run History page**

1. In the **Run History** table, do either of the following:
   * Hover over the row of a single Enforcement Set run and then at the end of the row, click the **Run** icon![RunIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunIcon.png).
     A *1 enforcement task created* notification appears
   * Bulk select one or more Enforcement Set runs and then on the top right of the table, click the **Run** action ![RunAction](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunAction.png).
     * Select the checkboxes of the Enforcement Set runs that you want to run.
     * Alternatively, select all Enforcement Set runs on the page (mark the checkbox in the table header) or in the entire table (**Select All**).  (Click **Clear All** to undo this action and clear the entire table).
     * The **Run Multiple Enforcements** notification box opens. Click **Run the Enforcements** to confirm. An *n enforcement tasks created* notification appears, where n represents the number of selected Enforcement Sets.
     * The number of selected records is displayed next to the **Total** results. For example, **Total**  6/ 2 selected.

2. Click [**Run History**](/docs/view-ec-set-history) to track the progress of the run.