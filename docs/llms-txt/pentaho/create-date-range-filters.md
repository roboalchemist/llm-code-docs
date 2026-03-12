# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-date-range-filters.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-date-range-filters.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-date-range-filters.md

# Create date range filters

Date range filters enable you to show only data that meets the conditions of the filter in a report. For example, you can create filters to display data between 2010 and 2013, or all data after 2010. After you have applied your filter, the Analyzer report shows only data specified by the date ranges that you selected.

Perform the following steps to create date range filters:

1. Log in to the User Console, then open an existing analysis report that contains a time dimension or choose **Create New** > **New Analysis**.
2. For a new report, select the data source that you want to use and click **OK**.
3. Create the report with a time dimension, such as year or quarter.
4. Click the icon to **Add A Filter**, then drag the time dimension that you want to filter on to the **Filters** board.

   You can also right-click on the dimension and add it as a filter.
5. Choose one of these options to create your filter:
   * **Choose a commonly used time period**: Use this option to specify a time period. In this Filter on Quarters example, you have your time period specified. Click **OK** to apply the filter. This filter is dynamic and changes with the current date. The other date filters are static.

     ![Filter on Quarters dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-7cb721c330feb69e1797d58de0e4e8b9c83c2656%2FAnaFilterChooseTimeDiagBox.png?alt=media)

     **Note:** The **Choose a commonly used time period** and the **Between, After, Before** filters are available only if time dimension levels are set up with the 'AnalyzerDateFormat' annotation. For more information, see **Pentaho Schema Workbench** for details.
   * **Select from a list**: Use this option to select values from a list. You can use the single Right and Left Arrows to add or subtract one value at a time, or use the Double Right and Double Left Arrows to add or subtract all of the values in the list. Select **OK** to apply the filter to your report.

     ![Select from a list option](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-93c5ee653e76d3fdb1a2f248c1426405f9044beb%2FAnaFilteronQuartersDiagBox.png?alt=media)
   * **Select a range**: If you select this option, click the **Select from date picker** link to use the date picker calendars to select beginning and ending dates for your report data. Click **Apply**, then **OK**, to apply the filter to your report.

     ![Select a range option displays the date picker](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-ef79d89326fe739c19251dbb0f9ce7289962faa8%2FAnaFilterDatePickerCalendar.png?alt=media)

Once you select a date, the data is validated to make sure that your date ranges actually contain that date. Analyzer searches for the nearest time period, up to plus or minus 30 time periods, if no date is found the first time. You will not be able to save the date filter if no dates are found.

**Note:** When you create a date range filter using the 'Between (and incl.)' operator and parameterize it, as described in [Add Query Parameters in Analyzer Reports](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/add-query-parameters-to-analyzer-reports-task-article), you specify one parameter name, but two parameters are created. One parameter controls the start of the range, and another controls the end of the range. The start date parameter is **\<YourParameterName>\_START**, and the end date parameter is\*\*\<YourParameterName>\_END\*\*.
