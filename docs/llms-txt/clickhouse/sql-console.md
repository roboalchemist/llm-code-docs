# Source: https://clickhouse.ferndocs.com/cloud/get-started/sql-console.md

---
sidebar_title: SQL console
slug: /cloud/get-started/sql-console
description: Run queries and create visualizations using the SQL Console.
keywords:

- sql console
- sql client
- cloud console
- console
title: SQL console
doc_type: guide

---

SQL console is the fastest and easiest way to explore and query your databases in ClickHouse Cloud. You can use the SQL console to:

- Connect to your ClickHouse Cloud Services
- View, filter, and sort table data
- Execute queries and visualize result data in just a few clicks
- Share queries with team members and collaborate more effectively.

### Exploring tables [#exploring-tables]

### Viewing table list and schema info [#viewing-table-list-and-schema-info]

An overview of tables contained in your ClickHouse instance can be found in the left sidebar area. Use the database selector at the top of the left bar to view the tables in a specific database

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/bb541f32f37d6f8946235646ae4c05c810d2a75c374b856fb72a26163766853c/images/cloud/sqlconsole/table-list-and-schema.png" alt="table list and schema"/>
Tables in the list can also be expanded to view columns and types

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/92cde70d58261a898f9e7da046d74911ccedcb2a296760507c3ee83834e912e1/images/cloud/sqlconsole/view-columns.png" alt="view columns"/>

### Exploring table data [#exploring-table-data]

Click on a table in the list to open it in a new tab. In the Table View, data can be easily viewed, selected, and copied. Note that structure and formatting are preserved when copy-pasting to spreadsheet applications such as Microsoft Excel and Google Sheets. You can flip between pages of table data (paginated in 30-row increments) using the navigation in the footer.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0f0adb6f745e381cf1b5e968ff78706ee8ed12ce5d7a84744577709068328b0c/images/cloud/sqlconsole/abc.png" alt="abc"/>

### Inspecting cell data [#inspecting-cell-data]

The Cell Inspector tool can be used to view large amounts of data contained within a single cell. To open it, right-click on a cell and select 'Inspect Cell'. The contents of the cell inspector can be copied by clicking the copy icon in the top right corner of the inspector contents.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/18fd16d863740ff7d25c419874ecb9756dec5d04deb1d1df6c1690bb660bb346/images/cloud/sqlconsole/inspecting-cell-content.png" alt="inspecting cell content"/>

## Filtering and sorting tables [#filtering-and-sorting-tables]

### Sorting a table [#sorting-a-table]

To sort a table in the SQL console, open a table and select the 'Sort' button in the toolbar. This button will open a menu that will allow you to configure your sort. You can choose a column by which you want to sort and configure the ordering of the sort (ascending or descending). Select 'Apply' or press Enter to sort your table

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b80c055fba756d1452f5267e07e6291746729089d9cd1ff95c428868ad4bcc7e/images/cloud/sqlconsole/sort-descending-on-column.png" alt="sort descending on a column"/>

The SQL console also allows you to add multiple sorts to a table. Click the 'Sort' button again to add another sort.

<Note>
Sorts are applied in the order that they appear in the sort pane (top to bottom). To remove a sort, simply click the 'x' button next to the sort.
</Note>

### Filtering a table [#filtering-a-table]

To filter a table in the SQL console, open a table and select the 'Filter' button. Just like sorting, this button will open a menu that will allow you to configure your filter. You can choose a column by which to filter and select the necessary criteria. The SQL console intelligently displays filter options that correspond to the type of data contained in the column.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/10cbddd4ef2fda34d227f420d2acf1721ee7a08b206a8a724afcd3162818b4b8/images/cloud/sqlconsole/filter-on-radio-column-equal-gsm.png" alt="filter on the radio column equal to GSM"/>

When you're happy with your filter, you can select 'Apply' to filter your data. You can also add additional filters as shown below.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f8604968b7d0d6efcf39aa1d9817e8bb6c93bf7a08bdddbad241c1ad201431b3/images/cloud/sqlconsole/add-more-filters.png" alt="Add a filter on range greater than 2000"/>

Similar to the sort functionality, click the 'x' button next to a filter to remove it.

### Filtering and sorting together [#filtering-and-sorting-together]

The SQL console allows you to filter and sort a table at the same time. To do this, add all desired filters and sorts using the steps described above and click the 'Apply' button.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/0d3b3ea65532c5c1f1795b24c9b8d7f23ca09dd9906752ed28cf49245f2e094a/images/cloud/sqlconsole/filtering-and-sorting-together.png" alt="Add a filter on range greater than 2000"/>

### Creating a query from filters and sorts [#creating-a-query-from-filters-and-sorts]

The SQL console can convert your sorts and filters directly into queries with one click. Simply select the 'Create Query' button from the toolbar with the sort and filter parameters of your choosing. After clicking 'Create query', a new query tab will open pre-populated with the SQL command corresponding to the data contained in your table view.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/be525ae407df3c40971db78ff0fcd5aa62b1ac75eee0d7998b11588378ec9a62/images/cloud/sqlconsole/create-a-query-from-sorts-and-filters.png" alt="Create a query from sorts and filters"/>

<Note>
Filters and sorts are not mandatory when using the 'Create Query' feature.
</Note>

You can learn more about querying in the SQL console by reading the (link) query documentation.

## Creating and running a query [#creating-and-running-a-query]

### Creating a query [#creating-a-query]

There are two ways to create a new query in the SQL console.

- Click the '+' button in the tab bar
- Select the 'New Query' button from the left sidebar query list

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/fe900bd73aeabd0b6ec98d19b8b4bee42d63063d64de58ff98624c69ce0f1645/images/cloud/sqlconsole/creating-a-query.png" alt="Creating a query"/>

### Running a query [#running-a-query]

To run a query, type your SQL command(s) into the SQL Editor and click the 'Run' button or use the shortcut `cmd / ctrl + enter`. To write and run multiple commands sequentially, make sure to add a semicolon after each command.

Query Execution Options
By default, clicking the run button will run all commands contained in the SQL Editor. The SQL console supports two other query execution options:

- Run selected command(s)
- Run command at the cursor

To run selected command(s), highlight the desired command or sequence of commands and click the 'Run' button (or use the `cmd / ctrl + enter` shortcut). You can also select 'Run selected' from the SQL Editor context menu (opened by right-clicking anywhere within the editor) when a selection is present.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/37c2e6a63c7296a0ded772bc1ffd625f2396a7eac73618835d28d2c0590c2ac4/images/cloud/sqlconsole/run-selected-query.png" alt="run selected query"/>

Running the command at the current cursor position can be achieved in two ways:

- Select 'At Cursor' from the extended run options menu (or use the corresponding `cmd / ctrl + shift + enter` keyboard shortcut

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f96a9014e3bd0b312a0a254aebb263f6a26a84024eb68779ac68b72af6fe61a2/images/cloud/sqlconsole/run-at-cursor-2.png" alt="run at cursor"/>

- Selecting 'Run at cursor' from the SQL Editor context menu

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c48f3f2c111f445f3c1c788f76bfba4bba78b9f5f6a4b3945ace0f16eb91f56a/images/cloud/sqlconsole/run-at-cursor.png" alt="run at cursor"/>

<Note>
The command present at the cursor position will flash yellow on execution.
</Note>

### Canceling a query [#canceling-a-query]

While a query is running, the 'Run' button in the Query Editor toolbar will be replaced with a 'Cancel' button. Simply click this button or press `Esc` to cancel the query. Note: Any results that have already been returned will persist after cancellation.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/2434b1ca499a343a2ee6f8f36e6851dd3af155a9d9fe09aa6f89785e15e3ff4c/images/cloud/sqlconsole/cancel-a-query.png" alt="Cancel a query"/>

### Saving a query [#saving-a-query]

Saving queries allows you to easily find them later and share them with your teammates. The SQL console also allows you to organize your queries into folders.

To save a query, simply click the "Save" button immediately next to the "Run" button in the toolbar. Input the desired name and click "Save Query".

<Note>
Using the shortcut `cmd / ctrl` + s will also save any work in the current query tab.
</Note>

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/630c3ace869d422af23a4dbb76f8ff6359e2899e1e07f666790b1c6ca3ae3552/images/cloud/sqlconsole/sql-console-save-query.png" alt="Save query"/>

Alternatively, you can simultaneously name and save a query by clicking on "Untitled Query" in the toolbar, adjusting the name, and hitting Enter:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b8b9222ee7858b8688fef0c433b26952dd012d43edb7c6a2aa6b527011e9a5ba/images/cloud/sqlconsole/sql-console-rename.png" alt="Rename query"/>

### Query sharing [#query-sharing]

The SQL console allows you to easily share queries with your team members. The SQL console supports four levels of access that can be adjusted both globally and on a per-user basis:

- Owner (can adjust sharing options)
- Write access
- Read-only access
- No access

After saving a query, click the "Share" button in the toolbar. A modal with sharing options will appear:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d7e753acbc92029a78b1af7d2fb63a2f0c59c20a03e8609f062e198077572caa/images/cloud/sqlconsole/sql-console-share.png" alt="Share query"/>

To adjust query access for all organization members with access to the service, simply adjust the access level selector in the top line:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/801c6efcd7ee6d1fcf896f56f89ccffcece3861b31ea770880336e00a1b6470c/images/cloud/sqlconsole/sql-console-edit-access.png" alt="Edit access"/>

After applying the above, the query can now be viewed (and executed) by all team members with access to the SQL console for the service.

To adjust query access for specific members, select the desired team member from the "Add a team member" selector:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/b70f79828e501f4050d06958263ad9f324a265dd3677f38b3765411773640443/images/cloud/sqlconsole/sql-console-add-team.png" alt="Add team member"/>

After selecting a team member, a new line item should appear with an access level selector:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/304a92bbc79d3d4a0129b3622c419a37ea7c3512913d4d4f0317dde0e6a90203/images/cloud/sqlconsole/sql-console-edit-member.png" alt="Edit team member access"/>

### Accessing shared queries [#accessing-shared-queries]

If a query has been shared with you, it will be displayed in the "Queries" tab of the SQL console left sidebar:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/419bc2d592f49f87f0a3d761ea1f232cc2ef3dbe8266644fd20c11d5d024d749/images/cloud/sqlconsole/sql-console-access-queries.png" alt="Access queries"/>

### Linking to a query (permalinks) [#linking-to-a-query-permalinks]

Saved queries are also permalinked, meaning that you can send and receive links to shared queries and open them directly.

Values for any parameters that may exist in a query are automatically added to the saved query URL as query parameters. For example, if a query contains `{start_date: Date}` and `{end_date: Date}` parameters, the permalink can look like: `https://console.clickhouse.cloud/services/:serviceId/console/query/:queryId?param_start_date=2015-01-01&param_end_date=2016-01-01`.

## Advanced querying features [#advanced-querying-features]

### Searching query results [#searching-query-results]

After a query is executed, you can quickly search through the returned result set using the search input in the result pane. This feature assists in previewing the results of an additional `WHERE` clause or simply checking to ensure that specific data is included in the result set. After inputting a value into the search input, the result pane will update and return records containing an entry that matches the inputted value. In this example, we'll look for all instances of `breakfast` in the `hackernews` table for comments that contain `ClickHouse` (case-insensitive):

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/10abd91c708cbecae33df7991cabeae72ff78466e80998f6a3201c33b910ebd3/images/cloud/sqlconsole/search-hn.png" alt="Search Hacker News Data"/>

Note: Any field matching the inputted value will be returned. For example, the third record in the above screenshot does not match 'breakfast' in the `by` field, but the `text` field does:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/6a708cfd3b47d1cbd67b58b388ea717d9e3cd1b9f969b1b91b96c000788ef7b8/images/cloud/sqlconsole/match-in-body.png" alt="Match in body"/>

### Adjusting pagination settings [#adjusting-pagination-settings]

By default, the query result pane will display every result record on a single page. For larger result sets, it may be preferable to paginate results for easier viewing. This can be accomplished using the pagination selector in the bottom right corner of the result pane:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/c8400b510b282e99df4397eded79273b1d80e0e0a132ded5344b6554683c67da/images/cloud/sqlconsole/pagination.png" alt="Pagination options"/>

Selecting a page size will immediately apply pagination to the result set and navigation options will appear in the middle of the result pane footer

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/d73622a6db18fa9a55c4da9ef8329cc11b74cd07e258d8f2a103ecc5af474680/images/cloud/sqlconsole/pagination-nav.png" alt="Pagination navigation"/>

### Exporting query result data [#exporting-query-result-data]

Query result sets can be easily exported to CSV format directly from the SQL console. To do so, open the `•••` menu on the right side of the result pane toolbar and select 'Download as CSV'.

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/93cfdfbcf5c7129196f8b3b10582692e6f76ab8e83d4905d07e1ddabeb89e7ea/images/cloud/sqlconsole/download-as-csv.png" alt="Download as CSV"/>

## Visualizing query data [#visualizing-query-data]

Some data can be more easily interpreted in chart form. You can quickly create visualizations from query result data directly from the SQL console in just a few clicks. As an example, we'll use a query that calculates weekly statistics for NYC taxi trips:

```sql
SELECT
   toStartOfWeek(pickup_datetime) AS week,
   sum(total_amount) AS fare_total,
   sum(trip_distance) AS distance_total,
   count(*) AS trip_total
FROM
   nyc_taxi
GROUP BY
   1
ORDER BY
   1 ASC
```

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/e82a91fec03ecfceea1710cd11418143735acaeb0bf6bcb5ed66d4473ca8342a/images/cloud/sqlconsole/tabular-query-results.png" alt="Tabular query results"/>

Without visualization, these results are difficult to interpret. Let's turn them into a chart.

### Creating charts [#creating-charts]

To begin building your visualization, select the 'Chart' option from the query result pane toolbar. A chart configuration pane will appear:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/f703bfddfa3ad6d86b66131fde488e1c57bc39e953c66667147e3709533f482d/images/cloud/sqlconsole/switch-from-query-to-chart.png" alt="Switch from query to chart"/>

We'll start by creating a simple bar chart tracking `trip_total` by `week`. To accomplish this, we'll drag the `week` field to the x-axis and the `trip_total` field to the y-axis:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/29ccc4192eb1b5d5b5b048aecf6a9b25cf138bb1fb010b0b15f786b9ae389ccf/images/cloud/sqlconsole/trip-total-by-week.png" alt="Trip total by week"/>

Most chart types support multiple fields on numeric axes. To demonstrate, we'll drag the fare_total field onto the y-axis:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/cec5e7f71a9d65feda52d3c5a4437e82253fa419fb01c8a15bc3cb62e06b70a9/images/cloud/sqlconsole/bar-chart.png" alt="Bar chart"/>

### Customizing charts [#customizing-charts]

The SQL console supports ten chart types that can be selected from the chart type selector in the chart configuration pane. For example, we can easily change the previous chart type from Bar to an Area:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/5818a48ee5b2e08f05e31b28b56491c01a2d7cc771bfb4632e9300e2bf58e7fa/images/cloud/sqlconsole/change-from-bar-to-area.png" alt="Change from Bar chart to Area"/>

Chart titles match the name of the query supplying the data. Updating the name of the query will cause the Chart title to update as well:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/af44dfb7c3b3035d93e345b2408c8061e302f3dfd02de64d2d86a6ecfa1af61a/images/cloud/sqlconsole/update-query-name.png" alt="Update query name"/>

A number of more advanced chart characteristics can also be adjusted in the 'Advanced' section of the chart configuration pane. To begin, we'll adjust the following settings:

- Subtitle
- Axis titles
- Label orientation for the x-axis

Our chart will be updated accordingly:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/40270f845a9341ad8978df80836953ed743e1e2c76255b259ec74e0c91656f52/images/cloud/sqlconsole/update-subtitle-etc.png" alt="Update subtitle etc."/>

In some scenarios, it may be necessary to adjust the axis scales for each field independently. This can also be accomplished in the 'Advanced' section of the chart configuration pane by specifying min and max values for an axis range. As an example, the above chart looks good, but in order to demonstrate the correlation between our `trip_total` and `fare_total` fields, the axis ranges need some adjustment:

<img src="https://files.buildwithfern.com/clickhouse.docs.buildwithfern.com/dfa6f98e0ca79c56be09748977c440b1f51cd750a3729d0a569d3698b8595eae/images/cloud/sqlconsole/adjust-axis-scale.png" alt="Adjust axis scale"/>
