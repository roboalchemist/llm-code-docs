# Source: https://docs.curator.interworks.com/embedding_using_analytics/tableau_dashboards/data_export.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Export

> Enable and configure multiple data export options for end-users to extract data from Curator dashboards.

There are multiple ways for end-users to export data from Curator.  The current Dashboard data-exports all utilize
Tableau's standard export functionality with some optional overrides.  Check out the options below for all available
data exports you can find in Curator.

## Export CSV/Excel

Curator supports the ability to set various options when exporting data to CSV or Excel.  This functionality is supported
in large part by Tableau's native export capabilities, but Curator allows a more seamless export experience when some
guardrails are needed.

### Enable or Disable Export to CSV / Excel

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab and expand the Toolbar Buttons (Tableau Actions) section.
4. Toggle the switch to enable/disable Export CSV (or Export Excel) and click the "Save" button.

### Specify a worksheet when users export to CSV / Excel

If you would like to explicitly guide users to download data from a worksheet on your Dashboard (e.g. a hidden sheet
containing only the data you want them to have access to) you may find this feature very useful.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Tableau** > **Dashboards** section from the left-hand menu and select an existing Dashboard or
   create a new one.
3. Click on the **Advanced** tab and toggle OFF the "Show Worksheet Options for Data Exports" feature.
4. This will populate a dropdown below the Show Worksheet Options for Data Exports" option called
   "CSV / Excel Worksheet Export".
5. Select your worksheet from this list.
6. Click the save button.

### Enable or Disable specifying a worksheet for export CSV / Excel

By default Curator allows users to select which worksheet to export data from (reflecting the same default behavior on
Tableau Server).  However we offer additional configuration which you can see in the previous steps above.  If you would
like to disable this feature so Curator exports the first-available-worksheet follow the steps below.

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab and expand the Toolbar Buttons (Tableau Actions) section.
4. Toggle "Worksheet Select (CSV and Excel Exports)" to enable/disable worksheet selection options globally.
5. Click the save button.

## View Data

Frequently, users need to be able to view the underlying data within a Dashboard to get more details on the data they're
looking at.  The View Data option exposes this row-level data, and allows users to export this data as well.

### Enable or Disable View Underlying Data

1. Login to the backend of your Curator instance (e.g. `http://curatorexample.com/backend`).
2. Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
3. Click on the **Features** tab and expand the Toolbar Buttons (Tableau Actions) section.
4. Toggle the switch to enable/disable Export Data and click the "Save" button.
