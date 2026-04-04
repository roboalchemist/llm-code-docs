# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/add-a-default-filter.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/adding-filters-to-an-analyzer-report/add-a-default-filter.md

# Add a default filter

As an administrator, you can add a default filter to Analyzer reports that is applied whenever a new report is created. This prevents users from adding large dimensions to reports that can impact server performance. Adding a default filter eliminates the step of having to add filters to each dimension to your report that you want filtered. Default filters are not applied to existing reports.

Perform the following steps to add a default filter to a report:

1. Add the filter(s) that you want to set as default to your report.
2. Click **More actions** and options and choose **Default Filters** > **Set for New Reports**.

   Other options are **Remove for New Reports** and **Reset to default.**

   The Alert dialog box displays.
3. Click **OK** to close the dialog box and set the default filters.

New reports based on the report you have modified will have the default filters applied. The **Remove for New Reports** command removes the filters for new reports. The **Reset to default** command removes any filters you have added to a report and sets the report back to the default filters.

**Note:** Filters that are added to a report in the chart view will display in the filters workspace, but are not saved in the default filters.
