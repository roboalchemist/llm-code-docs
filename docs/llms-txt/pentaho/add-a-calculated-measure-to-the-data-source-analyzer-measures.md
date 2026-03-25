# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-measures/add-a-calculated-measure-to-the-data-source-analyzer-measures.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/add-a-calculated-measure-to-the-data-source-analyzer-measures.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/add-a-calculated-measure-to-the-data-source-analyzer-measures.md

# Add a calculated measure to the data source

Calculated measures are user-defined measures based on a user's customizations to base measures in the data model. By applying a formula, in this case an MDX statement, to a selected base measure, the user creates a calculated measure to use in the Analyzer report. You can save the calculated measure to the model from within Analyzer so you can use that new measure without reloading your report. In addition, after you save your report, other users can immediately benefit from your calculated measure.

When you create a calculated measure using a measure in the **Available Fields** list in Analyzer, it is added to the data source when you save your report. To create a calculated measure within Analyzer, create or open an existing report in Analyzer.

**Note:** When you save a calculated measure to the data source, you are making a change to the data model and not just to the report. As a result, when you save your report, the **Undo** and **Redo** buttons are unavailable. Therefore, it is recommended that you complete all your changes to the data model, including 'undoing' or 'redoing' those changes, prior to saving the report.

If you want to create a calculated measure to only use in a particular report, see [Creating a calculated measure in a report](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/creating-a-calculated-measure-in-a-report).

1. In the **Available Fields** list, click a measure to select it and then click the down arrow next to it.
2. From the shortcut menu which appears, select **Create Calculated Measure**.

   The Create Calculated Measure dialog box appears.

   ![Create Calculated Measure dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-80dfe1cd5459dcde9002d89dc9046b8ecc0acab1%2FAnalyzer_CreateCalcMeasureFromAvailList.png?alt=media)
3. In the **Name** field, enter a name for your calculated measure.
4. In the **Format** field, specify how you want the results of your measure to appear in your report.

   If needed, specify the number of decimal places for the results. If you do not specify a format, the default value of the first base measure is used as the format.
5. In the right panel, enter the formula for your calculated measure.

   You can write the MDX statement, or you can use the list on the left to drag measures into the right panel. You can also use the symbol buttons below to help create your statement, or just use your keyboard to write the expression.
6. Select the **Calculate subtotals using measure formula** check box to use this calculated measure when adding up subtotals in your report.
7. Click **OK** to save this calculated measure.

   When you save your report, your calculated measure will also be saved to the data model. Once you save the report, the measure will be available for future reports which use this data source.
8. (Optional) Click **Cancel** to close the dialog box without saving your changes.

You can use hidden fields to create calculated measures. When you select the **Show Hidden Fields** option in the **View** menu for the **Available Fields** list, measures set as 'hidden' are available for selection in the Create Calculated Measure dialog box. To view hidden measures, you need the **Manage Data Source** permission. See [Hide and Unhide Fields](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/hide-and-unhide-fields) for additional details.

To edit a calculated measure you have created and saved in Analyzer, see [Updating Calculated Measure Properties](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/editing-a-calculated-measure-in-the-report).
