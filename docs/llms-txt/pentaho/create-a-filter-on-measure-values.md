# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-a-filter-on-measure-values.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-a-filter-on-measure-values.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-a-filter-on-measure-values.md

# Create a filter on measure values

In Pentaho Analyzer, when you create a filter on measure values, specify one or more measure fields and one level field which indicates the values to filter. Later, if you remove the level field from the report, then the measure filter is also removed.

Note the following restrictions when applying filters on measure values which may affect your report:

* You can have only one measure filter on a report at any given time.
* Calculated fields cannot be used.
* When the report is generated, the measure filter is applied after any other filters.

You can filter report data by applying conditions to the measure fields in the data in two ways:

* **Greater/Less Than, Equal to, etc.**
* **Top 10, etc.**

Perform the following steps to filter on a measure value in an Analyzer report:

1. Log in to the User Console. Click **Browse Files** to browse to the location of your Analyzer report and open the report.
2. Click the **Add a Filter** icon, then drag a field from the **Available fields** panel (or click and drag a field or column from the report) that you want to use as a filter into the **Filters** workspace.

   The Filter dialog box appears.
3. Select the **Greater/Less Than, Equal to, etc.** option and/or the **Top 10, etc.** option to filter the report on a specific measure data.

   **Note:** If your measure filter specifies both a **Greater/Less Than, Equal to, etc.** and a **Top 10, etc.** component at the same time, the **Greater/Less Than, Equal to, etc.** component is applied before the **Top 10, etc.** component.

   ![Measure Filter dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-42426c5c7010cc60949cc1cdf24acb27331e9a33%2FAnalyzer_AnalysisReport_MeasureFilterDialog.png?alt=media)
4. If you selected **Greater/Less Than, Equal to, etc.**, do the following:

   1. In the first field (measure), select the member dimension that you want to use from the drop-down menu, such as **Quantity** or **Sales**.
   2. In the second field (filter), select the measure that you want to use from the drop-down menu, such as **Greater Than** or **Equals**.
   3. In the third field (level), enter the value for the measure.

   ![Measure filter selection](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-1624c1ad709c68c180d9c5a21f19b25d1cd4c07c%2FAnalyzer_AnalysisReport_MeasureFilterSelection.png?alt=media)
5. If you selected **Top 10, etc.**, consider if you want to filter from the top or bottom of your list. Then do the following:

   1. In the first field, select **Top** or **Bottom** from the drop-down menu, and then enter the number of items for the member dimension you are filtering.
   2. Click in the **by \[measure]** field and from the drop-down menu, select the member dimension that you want to use for the filter.

   ![Measure filter selection for Top 10 filter](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-d6081791a6081a902c9c9b87b9a33308e66180af%2FAnalyzer_AnalysisReport_MeasureFilterSelectionTop10.png?alt=media)
6. Click **OK** to apply the filter to your report.

   After generating, your report displays with the fields matching those values.
7. Save your report.

   You can click **Undo** or **Reset** to return to the previous version of the report.
