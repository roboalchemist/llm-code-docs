# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/creating-analyzer-reports/create-an-analyzer-report.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/creating-analyzer-reports/create-an-analyzer-report.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/create-an-analyzer-report.md

# Create an Analyzer report

Pentaho Analyzer automatically fetches data in real time as you add and remove fields, so you may find it easier to build a report with the **Auto Refresh** feature turned off. Then you can design your report layout first, including calculations and filtering, without querying the database automatically after each change. Just click the auto refresh icon in the tool bar to toggle **Auto Refresh** on or off, or you can click the **Refresh Report** button at any time.

To create a new report, perform the following steps:

1. From User Console Home, click **Create New**, then **Analysis Report**.
2. Choose a data source for the report from the Select Data Source dialog box, then click **OK**.
3. From the **Available Fields** pane on the left, click and drag an object to the **Rows** or **Columns** area in the **Layout** panel.

   The data row or column appears in the table workspace.

   **Note:** You can remove an object from a row or column by dragging it from the **Layout** panel back to the **Available Fields** list.
4. In the list of fields, click and drag a measure to the **Measures** area in the **Layout** pane.

   The measure appears as a column in the table workspace.
5. If you want to rename or reformat your columns, right-click a column and choose **Column Name** and **Format** from the menu.

   The Edit Column window appears.

   **Note:** You can also sort the data in your columns by clicking and choosing a sort-order from the drop-down menu.
6. Choose a format from the **Format** drop-down box, or choose a [visualization](https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/creating-analyzer-reports/visualizations-for-analyzer) from the drop-down menu. Click **Refresh Report** if you need to, then click **OK**.
7. Click **Save As**. Type a file name for your report and choose a location to save it in, then click **OK**.

The new Analyzer report is created and saved in a location of your choice.
