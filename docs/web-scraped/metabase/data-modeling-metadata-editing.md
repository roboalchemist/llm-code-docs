# Source: https://www.metabase.com/docs/latest/data-modeling/metadata-editing

<div>

1.  [Home](/docs/latest/)
2.  [Data Modeling](/docs/latest/data-modeling/start)

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

# Table metadata admin settings

*Admin settings \> Table metadata*

![Table metadata settings](./images/table-metadata-settings.png)

Metabase lets you add and edit metadata for your tables and columns.

The **Table metadata settings only affect the way Metabase displays the data. None of the settings change the data in your database.**

Admins can grant access to these metadata settings to other groups. See [table metadata permissions](../permissions/data#manage-table-metadata-permissions).

## Table settings

*Admin settings \> Table metadata \> Database \> Table*

You can search for tables, or use the tree navigation to find each of your connected databases and their tables.

### Table display name and description

To edit a table's display name or description in the table metadata tab, click into the box that contains the current table name or description and edit it. Changes will be saved automatically once you click out of the box.

Descriptions are displayed in Metabase's [data reference](../exploration-and-organization/data-model-reference) and tooltips when view the table. Decscriptions help people find the right table for their use case.

### Table sync options

Actions you can take to refresh the schema or field values. For more, check out [syncs and scans](../databases/sync-scan).

#### Sync table schema

If you've made changes to this table in the underlying database that aren't showing up in Metabase yet, re-syncing the table schema can fix that.

To update the values in your filter dropdown menus, refresh or reset the cached values.

#### Scan field values

Metabase uses these values to populate dropdown filters. You can also [scan values for a specific field](#scan-values-for-a-specific-field).

#### Discard cached field values

Clears cached values. Metabase will pull new values for display in your [filter widgets](#filtering).

### Table sorting

You can sort the fields in a table in different ways:

-   Automatically (Metabase decides for you)
-   By how they appear in the database
-   Alphabetically
-   Custom order (just drag and drop to rearrange, then click "Done")

### Table visibility

You can toggle the visibility of a table by clicking on the **eye** icon next to the table name in the left sidebar navigation tree in the Table metadata tab.

**Hidden tables** won't show up in the [query builder](../questions/query-builder/editor) or [data reference](../exploration-and-organization/data-model-reference). **But this is not a permissions feature**: hidden tables can still be used in SQL questions if someone knows the name of the table. For example, `SELECT * FROM table_name` from the [SQL editor](../questions/native-editor/writing-sql) would return results. To prevent people from writing queries against specific tables, see [data permissions](../permissions/data).

To hide **all of the tables in a database** (say, if you've migrated to a new database), click on the **eye** icon next to the database name in the sidebar.

## Field settings

*Admin settings \> Table Metadata \> Database \> Table \> Field*

Fields are also known as Columns (see the [difference between fields and columns](/learn/grow-your-data-skills/data-fundamentals/database-basics#columns-vs-fields)).

## Field name and description

To change the *global* display name of a column in Metabase, click on the name of the column. For example, you could display "auth.user" as "User" to make the column more readable. People can also use [models](./models) to give columns a display name that's local to the model.

To add a description, click into the box below the column name. Descriptions are displayed in the [data reference](../exploration-and-organization/data-model-reference) to help people interpret the column's values. You should consider adding a description if your column contains:

-   Abbreviations or codes
-   Zeroes, nulls, or blank values
-   Placeholder values, like `9999-99-99`

## Field preview

![Field filtering preview](./images/field-filtering-preview.png)

Click the preview button to see sample data from that field.

-   Table preview
-   Detail
-   Filtering

## Scan values for a specific field

*Admin settings \> Table Metadata \> Database \> Table \> Field*

To scan or discard field values for a specific field, click on the **Field values** button. Metabase uses these values to populate dropdown menus in filter widgets. (Values aren't dropped from your database.)

## Field data

*Admin settings \> Table Metadata \> Database \> Table \> Field*

### Field name

This is the name of the field in the database itself. You can't change it in Metabase.

### Data type

This is the data type of the field in the database. You can't change the data type in Metabase, but you can cast certain data types to another data type.

### Cast to a specific data type

If you want Metabase to treat a text or number column as a datetime column, you can cast it to that type. Casting data types won't affect the original data types in your database.

For example, say you have a "Created At" column with a string [data type](/learn/grow-your-data-skills/data-fundamentals/data-types-overview) in your database. If you want to:

-   Create relative date filters, such as "Created At = Last week".
-   Use "Created At" with formulas like [datetimeAdd](../questions/query-builder/expressions/datetimeadd).

You can cast that string to a Date type.

Casting options include:

**Text to datetime casting options**:

-   ISO8601-\>Date
-   ISO8601-\>Datetime
-   ISO8601-\>Time

**Numeric to datetime casting options**:

-   UNIXMicroSeconds-\>DateTime
-   UNIXMilliSeconds-\>DateTime
-   UNIXNanoSeconds-\>DateTime
-   UNIXSeconds-\>DateTime

**Text to numeric casting options**:

-   String-\>Integer
-   String-\>Float

**Other options**:

-   Float-\>Integer
-   Datetime-\>Date

If Metabase doesn't support the casting option you need, you can [create a SQL question](../questions/native-editor/writing-sql#starting-a-new-sql-query) that casts the data and [save it as a model](./models#create-a-model-from-a-saved-question), or create a view directly in your database.

## Field metadata

*Admin settings \> Table Metadata \> Database \> Table \> Field*

### Semantic type

You can change the [semantic type](../data-modeling/semantic-types) to give people more context and enable additional functionality, such as displaying text as an image (if the text is an image URL. Another example: you could set an Integer as a "Score" so people have a better idea what those integers indicate.

The semantic types you can choose from depend on the data type. If none of the options describe the values in the column, you can set this setting to "No semantic type".

See [semantic types](../data-modeling/semantic-types).

## Field behavior

*Admin settings \> Table Metadata \> Database \> Table \> Field*

### Field visibility

-   **Everywhere**: By default, users can see all of the columns in a table.
-   **Only in detail views**: The detail view is the view you seen when you expand a single row in a table. This will hide lengthy text from question results. This setting is applied by default if a column's values have an average length of more than 50 characters. For example, you could use this setting on a column like "Customer Comments" if you already have a column for "Customer Rating".
-   **Do not include**: Columns won't show up in the query builder or data reference. You can set this option on sensitive columns (such as PII) or irrelevant columns. But this visibility option is a simple omit/hide option; **it's not a permissions feature**. These columns are still accessible for people with native query privileges; they can write `SELECT hidden_column FROM table` or `SELECT * FROM table` in the [SQL editor](../questions/native-editor/writing-sql) and they'll be able to view these fields and their values.

To restrict what data people can view and query, see [data permissions](../permissions/data).

### Filtering

The **Filtering** setting changes a column's default [filter widget](../dashboards/filters). Options include:

-   **Search box**: Display a search box and suggest autocompletions for values in that column that match the search term(s).
-   **A list of all values**: Display a search box, as well as a dropdown menu with checkboxes for values. If the number of distinct values exceeds 1000, however, Metabase will instead display a search box. See [Changing a search box filter to a dropdown filter](#changing-a-search-box-filter-to-a-dropdown-filter).
-   **Plain input box**: Display a search box, but don't suggest autocompletions.

The settings here will also affect dashboard filters. For example, if you set this to plain input box, you won't be able to set up a dashboard filter that has a dropdown menu. See [dropdown list](../dashboards/filters#dropdown-list).

#### Changing a search box filter to a dropdown filter

The dropdown filter widget can be finicky, because Metabase needs to run a [scan](../databases/sync-scan#how-database-scans-work) to get the list of values for the dropdown menu. If you're having trouble:

1.  Set the [Semantic type](#semantic-type) to "Category".
2.  Set [Filtering](#filtering) to "A list of all values".

When you change a default filter to a dropdown filter, you'll trigger a database query that gets the first 1,000 distinct values (ordered ascending) for that column. Metabase will cache the first 100kB of text to display in the dropdown menu.

If you have columns with more than 1,000 distinct values, or columns with text-heavy data, we recommend setting **Filtering** to "Search box" instead.

### Display values

You can map another column connected by a foreign key relationship, like mapping a `Product_ID` column to instead display the name of the product.

#### Mapping values to foreign keys

You can map another column connected by a foreign key relationship, like mapping a Product_ID column to instead display the name of the product.

#### Mapping numbers to custom values

Say you have a column with values 1, 2, and 3. You could instead display "low", "medium", and "high".

For this option to be available, you'll need to set the [filtering](#filtering) settings to "A list of all values".

Select "Custom mapping" from the dropdown menu. For each value in the column, enter a display value under **Mapped values**.

## Field formatting

*Admin settings \> Table Metadata \> Database \> Table \> Field*

See [Field formatting](./formatting#field-formatting).

## Unfold JSON

See [Working with JSON](./json-unfolding).

## Further reading

-   [Keeping your analytics organized](/learn/metabase-basics/administration/administration-and-operation/same-page)
-   [Data modeling tutorials](/learn/metabase-basics/getting-started/models)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/data-modeling/metadata-editing.md) ]