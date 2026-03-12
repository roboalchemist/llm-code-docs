# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-fields/managing-fields-in-large-reports.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/managing-fields-in-large-reports.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/managing-fields-in-large-reports.md

# Managing fields in large reports

You can add fields that have an arbitrary number of values, but large reports will be truncated. Truncated table reports differ from full reports in the following ways:

* The **Report Status Bar** displays the number of rows/columns shown versus the number of rows/columns in the full report. Cells will be cut until the number of cells is less than or equal to 2000. Note that this limit can be increased by your administrator. Rows are cut first, down to a minimum of 10 rows, followed by columns. This technique ensures that you still generate a useful sample of the row values despite the truncation.
* **Subtotals** and **Grand Totals** do not display in truncated reports
* A message at the end of the report informs you of the truncation. Note that the data in the cells does not change because of the truncation.

For charts, there is a maximum value of plot points which can be displayed on any axis. This limit is different depending on the type of chart and based on the amount of data which can reasonably fit on a screen. You can change this limit in Chart Options.
