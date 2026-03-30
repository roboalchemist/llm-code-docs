# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/tips-for-using-calculated-measures.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/tips-for-using-calculated-measures.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/tips-for-using-calculated-measures.md

# Tips for using calculated measures

Keep the following guidelines in mind when working with calculated measures in Pentaho Analyzer.

* When you add a calculated measure to the data source, it is available for anyone using that data source in Analyzer. This calculated measure appears and functions like any other base measure. If you do not add your calculated measure to a data source, it will only appear in the one report where is was added.
* If you create a calculated measure just for your report, but later decide that you want other users to have access to it, then you can add the calculated measure to the data source using one of the following methods:

  | From the . . .                                                                                                                                                                                         | Do this:                                                                                     |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
  | **Layout** panel                                                                                                                                                                                       | Click the Down Arrow next to the calculated measure, and then select **Add to Data Source**. |
  | **Report** panel                                                                                                                                                                                       | Right-click the calculated measure, and then select **Add to Data Source**.                  |
  | [In the Properties dialog box](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/editing-a-calculated-measure-in-the-report) | Select the **Apply to data source** check box.                                               |
* If you create a calculated measure and add it to the data source, but have not yet saved the report, you can use the **Undo** button to undo those actions, which will remove the calculated measure. Conversely, you can use the **Redo** button to reapply those actions.

  **Note:** When you click **Undo**, actions are removed in the reverse order in which they were applied, so any actions performed after adding the calculated measure will be undone first.
* If you add a calculated measure to the data source, you can view and edit its properties from the **Available Fields** list. See [Updating Calculated Measure Properties](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-measures) to learn how.
