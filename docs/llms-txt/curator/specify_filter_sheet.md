# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/specify_filter_sheet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Specify Filter Sheet

> Configure which specific worksheet or sheet should be used as the source for filter controls and options.

Curator provides the ability to get your filter options from the data. The standard dynamic filtering looks at the first
worksheet loaded. However, you may have multiple data sources compromising your Dashboard or a slow-loading worksheet
you want to avoid. Use the steps below to specify a worksheet to improve load time and narrow the scope of the data
that Curator has to retrieve to populate your filter values.

## To enable Specify Filter Sheet

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Dashboards** in the left-hand menu.
4. Click on the Dashboard you want to edit.
5. Click the Misc tab.
6. Toggle on the Specify Filter Sheet option in the Filters & Parameters section.

This will display two additional fields "Filter Worksheet" and "Use Summary Data". The "Filter Worksheet" field will
allow you to specify the name of the worksheet to pull from. The switch for "Use Summary Data" uses a quicker API call
that pulls from the Summary Data rather than all of the Underlying Data. To determine if what you're looking for is in
the Summary Data you will need to View Data within your workbook on Tableau Desktop.
