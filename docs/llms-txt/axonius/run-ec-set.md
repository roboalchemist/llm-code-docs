# Source: https://docs.axonius.com/docs/run-ec-set.md

# Running Enforcement Sets

Enforcement Sets can be run automatically on a schedule or manually. To learn more about scheduling Enforcement Set runs, see [Scheduling Enforcement Set Runs](/docs/scheduling-ec-set-runs). An Enforcement Set can be run only when the following conditions are met:

* The **Main Action** and the **query** are configured.
* The **Main Action** is not being edited.
* The **query** is not being edited.
* **Success / Failure / Post Actions** are not being edited or created.
* The Enforcement Set is from the **Shared Enforcements** folder.

**To run one or more Enforcement Sets manually**

1. In the table on the [**Enforcements** page](using-the-ec-page#opening-the-enforcements-page), do one of the following:
   * Hover over the row of an Enforcement Set to run, and then at the end of the row, click the **Run** icon ![RunIcon](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunIcon.png).
     A popup notification appears: *1 enforcement task created*.
   * Select the checkboxes of the Enforcement Sets that you want to run, and then on the top right of the table, click the **Run** action ![RunAction](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/RunAction.png). The number of selected Enforcement Sets is displayed next to the total results above the left side of the table. You can also select all records in the table or clear your entire selection.
     * When you select one Enforcement Set to run, a pop-up notification appears: *1 enforcement task created*.
     * When you select more than one Enforcement Set to run, the **Run Multiple Enforcements** notification box opens. Click **Run the Enforcements** to confirm running the selected Enforcement Sets. A pop-up notification appears: *n enforcement tasks created*, where n is the number of Enforcement Sets selected.
       The selected Enforcement Sets with a query configured will run.
2. To see the results of the run, click [**Run History**](/docs/view-ec-set-history).