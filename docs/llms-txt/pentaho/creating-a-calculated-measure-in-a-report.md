# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/creating-a-calculated-measure-in-a-report.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/creating-a-calculated-measure-in-a-report.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/use-calculated-measures-in-analyzer-reports/creating-a-calculated-measure-in-a-report.md

# Creating a calculated measure in a report

To create a calculated measure within your report, create or open an existing report in Pentaho Analyzer. Be sure to select a base measure for which you would like to create a calculated measure and then add it to the **Layout** panel.

**Note:** To learn how to create a calculated measure in the data source, see [Adding a Calculated Measure to the Data Source](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-measures/add-a-calculated-measure-to-the-data-source-analyzer-measures).

1. Click the Down Arrow next to a base measure in the **Layout** panel, select **User Defined Measure** from the menu, and then select **Create Calculated Measure**.

   The Create Calculated Measure dialog box appears.

   ![Select this check box to save your calculated measure to the data source.](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-5df9f8b1a9a4f9b5467ea00a224410087d716630%2FAnalyzer_CreateCalculatedMeasure.png?alt=media)
2. In the **Display Name** field, enter a name for your calculated measure.
3. In the **Format** field, specify how you want the results of your measure to appear in your report. Optionally, edit the number of decimal places for the results.

   If you do not specify a format, the default value of the first base measure is used as the format.
4. In the right panel, enter the formula for your calculated measure.

   You can write the MDX statement, or you can use the list on the left to drag measures into the right panel. You can also use the symbol buttons below to help create your statement, or just use your keyboard to write the expression.
5. Select the **Calculate subtotals using measure formula** check box to use this calculated measure when adding up subtotals in your report.
6. (Optional) Select the **Apply to data source** check box to add the calculated measure to the data model.

   When you click **OK** to save this calculated measure, your calculated measure will also be saved to the data model. Once you save the report, the measure will now be available for other users to add to their reports.
7. Click **OK** to apply your calculated measure to your report, or click **Cancel** to close the dialog box without applying your changes.

   When you save your report, your calculated measure will also be saved with your report.

* If you have not saved the report yet, you can click the **Undo** button to remove the calculated measure, even if you selected to apply it to the data source.
* You can use hidden fields to create calculated measures. When you select the **Show Hidden Fields** option in the **View** menu for the **Available Fields** list, measures set as 'hidden' are available for selection in the Create Calculated Measure dialog box. To view hidden measures, you need the Manage Data Source permission. See [Hide and Unhide Available Fields](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/hide-and-unhide-fields) for additional details.
