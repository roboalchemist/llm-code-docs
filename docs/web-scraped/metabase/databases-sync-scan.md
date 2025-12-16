# Source: https://www.metabase.com/docs/latest/databases/sync-scan

<div>

1.  [Home](/docs/latest/)
2.  [Databases](/docs/latest/databases/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Syncing and scanning databases

Metabase periodically runs different types of queries on your data warehouse to stay up to date with your database's metadata. Knowing information about your data helps Metabase do things like display the right chart for the results automatically and populate dropdown menus in filter widgets.

-   [Sync database schema](#how-database-syncs-work): grabs database schema, table structures, fields, constraints (primary and foreign keys), and deactivates deleted tables.
-   [Scan field values](#how-database-scans-work): takes samples of column values to populate filter dropdown menus, find distinct values, and identify valid visualizations. Metabase doesn't store *complete* tables from your database.
-   [Fingerprinting](#how-database-fingerprinting-works): samples the first 10,000 rows of the table to compute statistics for each field in the sample depending on their type, notably: distinct values count, % of null values (all field types), average, median, min, max, and quartiles (numeric types).

## Initial sync, scan, and fingerprinting

When Metabase first connects to your database, it performs a [sync](#how-database-syncs-work) to determine the metadata of the columns in your tables and automatically assign each column a [semantic type](../data-modeling/semantic-types).

You can follow the progress of these queries from **Gear icon** \>**Admin settings** \> **Tools** \> **Tasks** and filtering by the various sync tasks.

Once the queries are done running, you can view and edit the synced metadata from **Admin settings** \> **Table Metadata**. For more info, see [editing metadata](../data-modeling/metadata-editing).

## Choose when syncs and scans happen

By default, Metabase does a lightweight hourly sync and an intensive daily scan of field values. If you have a large database, you might want to choose when syncs and scans happen.

1.  Click on the **Gear icon**.
2.  Select **Admin settings**.
3.  Go to **Databases**.
4.  Select your database.
5.  In the **Connection and sync** section, click on **Edit connection details**.
6.  Expand **Show advanced options**.
7.  Toggle **Choose when syncs and scans happen**.

From there, you can set schedules for syncs and scans.

### Database syncing

Options include:

-   The frequency of the [sync](#how-database-syncs-work): hourly (default) or daily.
-   The time to run the sync, in the timezone of the server where your Metabase app is running.

### Scanning for filter values

Scans will only include "active fields": fields that people have used within the past fourteen days. Metabase won't scan fields that haven't been used in over fourteen days. Fields that have become inactive will become active again when someone uses them, and Metabase will include them in the next scan.

Options include:

-   **Regularly, on a schedule** allows you to run [scan queries](#how-database-scans-work) at a frequency that matches the rate of change to your database. The time is set in the timezone of the server where your Metabase app is running. This is the best option for a small database or tables with distinct values that get updated often.
-   **Only when adding a new filter widget** is a great option if you want scan queries to run on demand. Turning this option **ON** means that Metabase will only scan and cache the values of the field(s) that are used when someone adds a new filter widget to a dashboard or SQL question (i.e., they add a parameter to their SQL query).
-   **Never, I'll do this manually if I need to** is an option for databases that are either prohibitively large or which never have new values added. Use the [Re-scan field values](#manually-scanning-column-values) button to run a manual scan and bring your filter values up to date.

Regardless of which option you pick, if you [set a field to use a dropdown list in filter widgets](../data-modeling/metadata-editing#filtering), Metabase will need to get values for that dropdown. Whenever someone uses that filter widget, Metabase will first look for cached values (valid for fourteen days) to populate that dropdown; otherwise, it will re-scan that field for the most up-to-date values.

## Manually syncing tables and columns

1.  Go to **Admin settings** \> **Databases** \> your database.
2.  Click **Sync database schema**.

## Manually scanning column values

To scan values from all the columns in a table:

1.  Go to **Admin settings** \> **Table Metadata** \> your database.
2.  Select the table that you want to bring up to date with your database.
3.  Click the **gear icon** at the top of the page.
4.  Click **Re-scan this table**.

To scan values from a specific column:

1.  Go to **Admin settings** \> **Table Metadata** \> your database.
2.  Select the table.
3.  Find the column you want to bring up to date with your database.
4.  Click the **gear icon** in the panel for that column.
5.  Click **Re-scan this field**.

## Clearing cached values for a table or field

To clear the [scanned field values for a table](#syncing-and-scanning-databases):

1.  Go to **Admin settings** \> **Table Metadata**.
2.  Select the database and table.
3.  Click the **gear icon** in the upper right.
4.  Click **Discard cached field values**.

You can also tell Metabase to forget the cached values for individual fields by clicking the **gear** icon on a field and clicking on **Discard cached field values**.

## Disabling syncing and scanning for specific tables

To prevent Metabase from running syncs and scans against a specific table, change the [table visibility](../data-modeling/metadata-editing#table-visibility) to **Hidden**:

1.  Go to **Admin settings** \> **Table Metadata** \> your database.
2.  Hover over the table name in the sidebar.
3.  Click the **eye** icon.

> Hiding a table will also prevent it from showing up in the [query builder](../questions/query-builder/editor) and [data reference](../exploration-and-organization/data-model-reference). People can still query hidden tables from the [SQL editor](../questions/native-editor/writing-sql).

## Syncing and scanning using the API

Metabase syncs and scans regularly, but if the database administrator has just changed the database schema, or if a lot of data is added automatically at specific times, you may want to write a script that uses the [Metabase API](../api) to force a sync or scan. The API provides two ways to initiate a sync or scan of a database:

### Sync or scan the database

You can use these endpoints by authenticating with a user ID and passing a session token in the header of your request.

-   **Sync database schema**: `/api/database//sync_schema`
-   **Re-scan field values**: `/api/database//rescan_values`

### Sync a single table

-   `/api/notify/db/` to tell Metabase to sync a database, or optionally a specific table.
-   `/api/notify/db//new-table` to sync a new table, without syncing the whole database. Requires `schema_name` and `table_name`.

To use this endpoint, you must pass a string via the `MB_API_KEY` environment variable. This string is distinct from Metabase's [API keys](../people-and-groups/api-keys).

We created the `notify` endpoint so that people could tell their Metabase to sync after an [ETL operation](/learn/grow-your-data-skills/data-landscape/etl-landscape) finishes.

See our [API docs](../api).

## How database syncs work

A Metabase **sync** is a query that gets a list of updated table and view names, column names, and column data types from your database:

``` highlight
SELECT
    TRUE
FROM
    "your_schema"."your_table_or_view"
WHERE
    1 <> 1
LIMIT 0
```

By default, this query runs against your database during setup and again every hour. This scanning query is fast with most relational databases but can be slower with MongoDB and some [community-built database drivers](../developers-guide/community-drivers). Syncing can't be turned off completely, otherwise Metabase wouldn't work.

Here's the kind of data that gets synced and why:

  What               Why
  ------------------ ----------------------------------------------
  Table names        Without tables, what are we even doing here?
  Field names        Without fields, same deal
  Field data types   Querying and type handling
  Primary keys       Table display, detailed views, auto-joins
  Foreign keys       Auto-joins and relationship visualization

## How database scans work

A Metabase **scan** is a query that caches the column *values* for filter dropdowns by looking at the first 1,000 distinct records from each table, in ascending order:

``` highlight
SELECT
    "your_table_or_view"."column" AS "column"
FROM
    "your_schema"."your_table_or_view"
GROUP BY
    "your_table_or_view"."column"
ORDER BY
    "your_table_or_view"."column" ASC
LIMIT 1000
```

For each record, Metabase only stores the first 100 kilobytes of text, so if you have data with 1,000 characters each (like addresses) and your column has more than 100 unique addresses, Metabase will only cache the first 100 values from the scan query.

Cached column values are displayed in filter dropdown menus. If people type in the filter search box for values that aren't in the first 1,000 distinct records or 100 kB of text, Metabase will run a query against your database to look for those values on the fly.

A scan is more intensive than a sync query, so it only runs once during setup and again once a day by default. If you [disable scans](#scanning-for-filter-values) entirely, you'll need to bring things up to date by running [manual scans](#manually-scanning-column-values).

To reduce the number of tables and fields Metabase needs to scan to stay current with your connected database, Metabase will only scan values for fields that someone has used in the last fourteen days.

Here's the kind of data that scans get and why:

  What                                             Why
  ------------------------------------------------ --------------------------------------------------------------
  Distinct values for category fields              Dropdown filter UI instead of text entry
  Cached values for active fields                  Improves filter UI experience
  Advanced field values (with filtering context)   Values when the data is restricted by row or column security

## Periodically refingerprint tables

> Periodic refingerprinting will increase the load on your database.

By default, Metabase only runs [fingerprinting](#how-database-fingerprinting-works) queries when you first connect your database.

Turn this setting on if you want Metabase to use larger samples of column values when making suggestions in the UI:

1.  Go to **Admin** \> **Databases** \> your database.
2.  Click on **Edit connection details**.
3.  Expand **Show advanced options**.
4.  Turn on **Periodically refingerprint tables**.

## How database fingerprinting works

The fingerprinting query looks at the first 10,000 rows from a given table or view in your database:

``` highlight
SELECT
    *
FROM
    "your_schema"."your_table_or_view"
LIMIT 10000
```

Metabase uses the results of this query to provide better suggestions in the Metabase UI (such as auto-binning).

To avoid putting strain on your database, Metabase only runs fingerprinting queries the [first time](#initial-sync-scan-and-fingerprinting) you set up a database connection.

By default, Metabase won't re-fingerprint your database after that initial fingerprinting. To re-fingerprint your data, you can turn ON [Periodically refingerprint tables](#periodically-refingerprint-tables).

Here's the kind of data that fingerprinting gets and why:

  What                                                                   Why
  ---------------------------------------------------------------------- ---------------------------------------------
  Distinct value count                                                   Determines field value caching strategy
  Min/max numeric values                                                 Binning in visualizations and range filters
  Date range (min/max dates)                                             Date filter defaults and timeline display
  Special type detection (URL, email, JSON, Geo data (like US States))   Field rendering and filtering
  Null value ratio                                                       Data quality assessment
  Average/median values                                                  Visualization defaults
  Text length metrics                                                    Hide long text fields from UI

## Further reading

Metabase doesn't do any caching or rate limiting during the sync and scan process. If your data appears to be missing or out of date, check out:

-   [Can't see tables](../troubleshooting-guide/cant-see-tables).
-   [Data in Metabase doesn't match my database](../troubleshooting-guide/sync-fingerprint-scan).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/databases/sync-scan.md) ]