# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/filters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filters

> Configure and implement filters to enable users to interactively control dashboard content and focus on specific data subsets.

Filters in Curator provide a powerful way to refine and control the data displayed in Dashboards, giving you expansive
capabilities beyond what is natively available with the tools you're embedding.  You can share filters across
multiple dashboards, placing your users back into their browsing context without having to constantly re-set filters,
even integrating filters across different BI platforms to unify this experience regardless of the tool you're embedding.

With this guide to Filters, we will explain how to configure and manage your filters, providing you with details on
which settings are best for all the scenarios you may encounter.

***

## To Create a filter

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Filters** in the left-hand menu.
4. Click the "New Filter" button.
5. Find the details of how to set up filters in the following [overview](#overview-of-filter-settings)

## Overview of Filter Settings

### Filter Fields

<img src="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=cf1399273615ce028f2c390e3f02902b" alt="Overview of the top section - Filter fields" data-og-width="1011" width="1011" data-og-height="507" height="507" data-path="assets/images/embedding_using_analytics/filters_parameters/filter_fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?w=280&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=6cfc5e6bb4f3f0dd90d46be531e8dd5b 280w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?w=560&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f11a79c33f3622c29f487c6904a621c1 560w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?w=840&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=c0f99813eb5ba53a50ad20919c84b42c 840w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?w=1100&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=400c39abf5a54f72b98d44281af3590c 1100w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?w=1650&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=f0391922da744390a2d6216745bd5c2d 1650w, https://mintcdn.com/interworks/x0r9dMo3GyjABFAR/assets/images/embedding_using_analytics/filters_parameters/filter_fields.png?w=2500&fit=max&auto=format&n=x0r9dMo3GyjABFAR&q=85&s=ba0f1575787c955125c8a0e04a4e763c 2500w" />

* **Display Name**: The name visible to users when interacting with the filter.
* **Filter Type**: The type of filter (e.g. Single-select, Multi-select, Date) to control this field.
* **Filter Category** (optional): Allows you to group filters into sections in the filter pane. See the
  [Filter Categories Section](/embedding_using_analytics/filters_parameters/filter_categories)
  for more information.
* **Field Name Mapping**: Links the filter to a specific field in the analytics platform.
* Once your Field Name Mapping is verified, you will see a teal notice appear confirming the filter has been found
  on your BI platform. If your Field Name Mapping could not be verified, a yellow notice appears. Use the **Check
  All Tableau Site** button if you are certain that the field name exists on a different Site.

### Dashboards

* Assign filters en-masse to specific Dashboards. The filter will show as a Curator filter inside the Curator toolbar
  when you load a given Dashboard. You can also add filters to a specific Dashboard via the "Filters" tab on the edit
  Dashboard page.

### Secondary Data Source

In most cases, this toggle should remain **off**. It is only required in specific scenarios where filtering needs to
be applied to a field that is not part of the primary data source on your Tableau sheet but comes from a secondary
data source. You can identify secondary data source fields in Tableau by the orange check mark in editing mode.

If you need to filter on a field marked with this orange check mark:

1. Enable the **Specify a Secondary Data Source** toggle.
2. Enter the name of the secondary data source (as displayed in the workbook) into the input field that appears.
   The filter will then be sent to Tableau in the format of `datasource_name.filter_field_name`.
   This ensures that the filter is correctly applied across your data sources.

## Display Options

1. **Sticky Filter**
   * Saves filter selections per user for consistent filtering across Dashboards. This
     is using browser cookies which will be applied to any Dashboard that uses the specified
     field name from the specified field name mapping. I.e. it is not only applied to the
     Dashboards selected in the [Dashboards](#dashboards) section above.

2. **Add "All" Option**
   * Adds an "All" selection option for Single Select filters. If there is no "All" option for the single select
     filter, the first value of the field will be shown even if not yet selected. Once you started filtering you
     can only reset the filter by using the toolbar button "Reset".

3. **Get Filter Options from Data**
   * Pulls options directly from the data source to populate the filter options for a given dropdown. This will
     slow down the Dashboard's load time if the Dashboard contains a lot of data. This process can be
     sped up by enabling "Specify Filter Sheet" from a Dashboard's backend settings. See the
     [Specify Filter Sheet Section](/embedding_using_analytics/filters_parameters/specify_filter_sheet)
     for more information.  If this field is disabled, you must add items via the Options list (manually)
     otherwise the filter will contain no options for users to select and they will only see "No results found".

4. **Cache Filter Options**
   * This saves the dropdown options via Curator's cache on a user basis and will retrieve options in a more
     performant manner.  However, the list of options may be stale given the time you set the cache to. The cache
     begins the first time a user loads the options, and is not related to the underlying Dashboard's data-refresh
     schedule, so ensure you only enable this setting for dropdowns that rarely see new data.
   * **Cache Expiration Options**: 4 Hours, 1 Day, 1 Week

5. **Filter-Blacklist**
   * If you have a Filter Blacklist set up, it can be reused by toggling on **Use Filter-Blacklist Group**.
     Once enabled, you can select from you existing Blacklist Groups to be applied on this filter.
   * Note, if you either don't have a Filter Blacklist Group set up or only want specific sheets to be
     blacklisted, i.e. the filter to not be applied on this sheet, add the sheet names as individual items
     to the **Sheet Blacklist** list.
   * More information in Filter Blacklists can be found under [Hidden Sticky Filters
     and Parameters](/embedding_using_analytics/filters_parameters/hidden_sticky_filters_and_parameters)

## Filter Types

### Single Select

* Allows the frontend user to select only a single value for this filter.

### Multi-Select

* Allows the frontend user to select multiple values for this filter.

### Date

* Allows the frontend user to pick a date from the standard date picker widget. The date format
  is displayed based on the users locale settings. To successfully filter for dates make sure that the
  Tableau Dashboard is published with the correct specific locale settings or with automatic locale detection.

### Date Range

* Allows the frontend user to pick a start and an end date from the standard date picker widget. The date
  format is displayed based on the users locale settings. To successfully filter for dates make sure that the
  Tableau Dashboard is published with the correct specific locale settings or with automatic locale detection.

### Relative Date Filters

* Works similarly to Tableau's Relative Date Filters where you get a slider to dynamically update to show a
  time period relative to when you open the view, such as the current week, the year to date, or the past 10 days.
  Relative date filters make it easy to create views that always show the most recent data ([cf. Tableau Relative
  Date Filters](https://help.tableau.com/current/pro/desktop/en-us/qs_relative_dates.htm)).
* When you use a Relative Date Filter you will get more options to configure your filter:
* **Direction**: Filter by Past or Future.
* **Scale**: Choose Days, Months, Quarters, or Years.
* **Range**: Specify the maximum relative date range.

### Boolean

* Allows the frontend user to select between True and False.

## More on Filters

### URL Filters

* You can apply filters and parameters by appending `key=value` pairs to URLs to pre-filter Dashboards. E.g.
  my-Curator.com/Dashboard/superstore?region=North will pre-filter my Superstore Dashboard to only show the North region.
* Automatically applied when using Curator or Tableau filter UI.
* **Important**: Disabling "Ignore filter and parameter changes from Dashboard" prevents
  [Report Builder](/embedding_using_analytics/report_builder/overview_and_enabling_report_builder)
  from capturing filters.

### Evaluation of Filters

In this order, filters are evaluated:

* **URL filters** - Values that are appended to the Curator URL in your browser (e.g. `?Region=South`)
* **Preloaded sticky filters** - Filters identified via the Tableau Server Settings.
* **Cookie-based sticky filters** - Browser-session stored filters, also managed via Tableau Server Settings.
* **Published filter settings** - The default state of the Dashboard.

In case of any conflicting values, the first evaluation is considered the correct one.  For example, if one of your
users has been browsing around and setting their **Region** filter to *North* and that drops a *Cookie-based sticky
filter* in their browser, when they return to the page, the filter will be evaluated as `Region=North` by default.
However, if they are emailed a link from a colleague sharing an insight and the URL is sent over with `?Region=South`
when they click on the link, the Dashboard will be filtered to Region=South since *URL filters* are evaluated first
taking precedence over the *Cookie-based sticky filters*

***

## Troubleshooting Filters

### Filter Options are not visible

* Verify that either "Get Filter Options from Data" or the manual Options list is configured.

### I want to apply a filter across Dashboards but I do not want to show the Curator Filter UI

* Use [Hidden Sticky Filters](/embedding_using_analytics/filters_parameters/hidden_sticky_filters_and_parameters)
  instead

### My view is empty after I switched tabs on my dashboards

* If your view loads briefly and then suddenly turns blank, then a filter is probably being applied that should
  not be applied. That can happen if you either track filter and parameter changes in the url (a) or you have a
  sticky filter enabled (b) which should not be applied to this view.
  * a) Turn on **Ignore Filter and Parameter Changes from Dashboard** on the Dashboard level which
    will stop adding the changes to the url. When you switch tabs, the filter and parameter actions need to be
    defined in the Workbook itself. However please note, that turning this on will break Report Builder's functionality.
  * b) Apply Filter Blacklists to prevent filters being applied on specific sheets. However, this
    does not currently work with Hidden Sticky Filters and Parameters.

### Date Filters show differently for my global users

* That is not necessarily an issue because Curator can handle locale date formats.
* Locale-specific formats (e.g., DD/MM/YYYY, MM/DD/YYYY) depend on:
  * Browser language settings.
  * Tableau User Language and Region settings.
* As long as your Workbook is flexible with date formats, Curator will handle dates for your different users and
  present them the format they are used to based on their settings.

### Date Filters do not filter properly

* This is mostly due to a locale mismatch: Ensure browser and Tableau settings align. You have three options:

1. When you have multiple regions that are working with your Dashboard, make sure that the Workbook's locale is
   set to automatic when published to Tableau. It will then adjust to your users location which Curator will also
   look pick up and then send the date in the expected format.
2. If you require a specific format you can also force the browser to use the specific locale date format instead
   which again Curator will pick up.
3. You can also use dates in YYYY-MM-DD format and it will ignore any browser or Workbook settings and just handle
   dates correctly in that format.
