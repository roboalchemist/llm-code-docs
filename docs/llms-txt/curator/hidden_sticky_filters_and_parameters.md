# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/hidden_sticky_filters_and_parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Hidden Sticky Filters and Parameters

> Configure invisible persistent filters and parameters that remain active across user sessions and dashboard navigation.

Hidden sticky filters and parameters are used to remember the filter/parameter values a user selects across the system,
without showing up in the filters list on a Dashboard.

You can blacklist sheets for the Hidden Filter to not apply to. The name should match the sheets' name in Tableau.

## To create a hidden sticky filter/parameter

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Settings** > **Tableau** > **Tableau Server Settings** in the left-hand menu.
4. Click the "General" tab at the top.
5. Expand the "Sticky Filters" section and toggle on "Use Hidden Sticky Filters".
6. Click to add a new item under hidden sticky filters or hidden sticky parameters section.
7. Enter the name of the filter/parameter.
8. Click the "Save" button.

## Filter Blacklists

If you have individual sheets that a filter should not be applied to Curator's Filter Blacklists can help here.
Curator provides two types of filter blacklists to control where filters are applied within Tableau Dashboards:
filter-specific blacklists and global sheet-specific blacklists.

### Filter-Specific Blacklists

A filter-specific blacklist allows you to prevent a specific Curator filter from being applied to selected sheets.
This requires the Curator filter to be present in the front-end.

To configure a filter-specific blacklist:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Filter** > select the filter that should not be applied to all sheets.
4. In the **Display Options** section, add one item to the **Sheet Blacklist** per sheet you want to exclude from the
   filter.

If multiple filters need to be excluded from the same set of sheets, you can create a reusable **Filter Blacklist
Group**:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backen`).
2. Log in if prompted.
3. Click on **Tableau** > **Filter Blacklists**.
4. Create a new blacklist group.
5. Name your blacklist group.
6. Add one item per sheet you do not want the filter to be applied to to the Sheet Blacklist.
7. Navigate to your Filter to apply the Filter Blacklist Group. Click on **Tableau** > **Filter** > select the filter
   that should not be applied to all sheets.
8. In the **Display Options** section, toggle on **Use Filter Blacklist Group**.
9. Select the Filter Blacklist group that you created in steps 3-6.

### Global Filter Sheet Blacklists

If you need to exclude sheets from a hidden sticky filter, a global filter blacklist must be used. This applies
to filters that are not explicitly present in the Curator UI but are set as sticky and therefore influence the
Dashboard on load with the last value set applied. Or because Hidden Sticky Filters or Parameters are enabled.

To configure a global filter blacklist:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backen`).
2. Log in if prompted.
3. Click on **Settings** > **Tableau** > **Tableau Server Settings**.
4. Open the Filters and Parameters section.
5. Add the respective sheets to the Global Filter Sheet Blacklist.

If you using Filter Blacklist is slowing down your Dashboard load performance, there is a workaround within
Tableau. Following the below steps is more performant on especially large Dashboards.

1. In Tableau Desktop (or Tableau Server Edit Mode), go to the sheet that the filter should not be applied on.
2. Duplicate the data source the filter field(s) comes from.
3. Replace the existing fields on your sheet with the fields from the duplicated data source.
4. **Rename the filter field**, regardless of whether used on your sheet or not. ***Note:*** If you are not using the
   filter field on your sheet, you may as well delete it from your duplicated data source. By renaming/deleting it, you
   ensure that the filter request will have no effect on this specific sheet.
5. Repeat for all other fields the sheet should not be filtered by.
6. Repeat for all sheets that should not listen to the filter(s).
7. Republish your Dashboard.
