# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/advanced-topics/group-and-filter-data-in-interactive-reports/add-filters.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-interactive-reports-cp/advanced-topics/group-and-filter-data-in-interactive-reports/add-filters.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/advanced-topics/group-and-filter-data-in-interactive-reports/add-filters.md

# Add filters

Filters are used to restrict or limit data in a report, so that you can build the report to show only the information that you want to view.

For example, a typical report shows sales by product line. A time filter on **Quarter** restricts the data so that only sales for one quarter are shown. If you then add a regional filter for Europe, the report would display data pertaining to European sales for that quarter. If you add a filter on another field to exclude a product, the report would display data pertaining to European sales in that quarter, which are also not a part of the excluded product line.

The following steps describe how to add filters to an Interactive Report:

1. Click the plus sign next to **No Filters** on the toolbar near the top of the report.

   A workspace for filters appears at the top of the report.
2. From the **Available Fields** panel, drag fields into the **Filter Panel**.

   The Filter dialog box appears. Notice that the values associated with the field are listed in the dialog box. You can choose one of these values, or you can enable **Match a specific string** to filter the report on a specific string of data.
3. Select the value or values that you want from the **Add Selected** list and click the arrow to move it into the right pane.

   The value appears with a green check mark next to it in the right pane.
4. After you have selected all of the values that you need from the list, click **OK** to exit the dialog box.
5. Repeat this process for each field that you want to filter on.

   The report displays data for the chosen values only.
6. Save your report.

Your report is filtered and saved. You can click **Undo** or **Reset** to return to the previous version of the report.
