# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-a-comparison-filter-on-a-numeric-level.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-a-comparison-filter-on-a-numeric-level.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/create-a-comparison-filter-on-a-numeric-level.md

# Create a comparison filter on a numeric level

Comparison filters allow you to only show data that meets the conditions of compared numeric dimension levels.

For example, if you have a 'Credit Score' level in a customer dimension, you can create a filter such as "Credit Score > 600" to include only customers whose credit score is greater than 600. After you have applied your filter, the Analyzer report displays only data specified by the comparison ranges that you selected.

**Note:** The list of comparison operators does not include 'Equals', 'Not Equals', and 'Is Not Empty' because the same filter behavior can be achieved with the 'Includes' and 'Excludes' filters.

Perform the following steps to add a comparison filter to an Analyzer report:

1. Log in to the User Console. Click **Browse Files** to browse to the location of your Analyzer report and open the report.
2. Click the **Add a Filter** icon, then drag a field from the **Available Fields** panel (or click and drag a field or column from the report) that you want to use as a filter into the **Filters** workspace.

   The Filter dialog box appears. Notice that the values associated with the field are listed in the dialog box.
3. Select the **Greater / Less Than, Between, etc.** option.

   ![Filter dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-2a2bd402d609454f7c8187ce16a1301f3ed3cb79%2FAnalyzer_ComparisonFilterDialog.png?alt=media)
4. Click **Greater Than**, then select the comparison operator that you want to use from the drop-down menu. Select **Greater Than**, **Less Than**, **Greater Than or Equals**, **Less Than or Equals**, or **Between**.
5. Enter the value or value range that you want to use as a filter. Click **OK** to apply the filter to your report.

   After generating, your report displays with the fields matching those values.
6. Save your report.

   You can click **Undo** or **Reset** to return to the previous version of the report.
