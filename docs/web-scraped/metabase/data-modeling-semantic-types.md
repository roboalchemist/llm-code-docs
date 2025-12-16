# Source: https://www.metabase.com/docs/latest/data-modeling/semantic-types

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

# Data types and semantic types

Metabase distinguishes between two types of column metadata: data types and field types.

-   [**Data types**](#data-types) are the underlying column type as defined in your database, like `Date` or `Text`. Metabase reads the data types during the [database sync process](../databases/sync-scan).
-   [**Semantic types**](#semantic-types), also called **field types**, are labels that describe how the data should be interpreted. For example, if you have a column with a data type of `Text` that you use to store emails, you can add a semantic type of `Email` to let people (and Metabase) know what kind of text the column stores.

Data and semantic types determine how Metabase formats the data, which charts are available, how the filters work, and other functionality.

## Data types

Data types are the underlying column types as defined in your database. Metabase reads the data types during the [database sync process](../databases/sync-scan). Because Metabase connects to many different databases, it uses its own type hierarchy under the hood, so that it can, for example, handle date fields in databases as different as PostgreSQL and MongoDB.

The main data types in Metabase:

  Data Type    Example database types
  ------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Numeric      `INTEGER`, `FLOAT`
  Temporal     `DATE`, `TIMESTAMP`
  Text         `VARCHAR`, `TEXT`
  Text-like    MongoDB `BSONID`, Postgres `Enum`
  Boolean      Boolean
  Collection   `JSON`, BigQuery `RECORD`, MongoDB `Object`

Metabase currently doesn't support array types. On columns containing arrays, you'll only be able to filter by **Is empty** or **Is not empty**.

For some fields, you can tell Metabase to [cast the field to a different data type](#editing-data-and-semantic-types) (for example, changing a text type to a date type).

## Semantic types

You can think of semantic types as adding meaning and context to a field to communicate its purpose and enable [additional functionality](#what-data-and-semantic-types-enable). Available semantic types depend on the underlying data types.

### Semantic types for any field

-   **Entity key.** Used to indicate that the field uniquely identifies each row. Could be a Product ID, serial number, etc.

-   **Foreign key.** Used to refer to an Entity key of another table to connect data from different tables that are related. For example, in a Products table, you might have a Customer ID field that points to a Customers table, where Customer ID is the Entity key. If you want to use [linked filters on dashboards](../dashboards/linked-filters), you must set up foreign key relationships.

### Semantic types for numeric fields

-   Quantity
-   Score
-   Percentage
-   Financial
    -   Currency
    -   Discount
    -   Income
-   Location
    -   Latitude
    -   Longitude
-   Category

### Semantic types for temporal fields

-   Creation date
-   Creation time
-   Creation timestamp
-   Joined date
-   Joined time
-   Joined timestamp
-   Birthday

### Semantic types for text fields

-   Entity name
-   Email
    -   URL
    -   Image URL
    -   Avatar URL
-   Category
-   Name
-   Title
-   Description
-   Product
-   Source
-   Location
    -   City
    -   State
    -   Country
    -   ZipCode

### Semantic types for collection fields

-   Field containing JSON.

    See [Working with JSON](./json-unfolding).

## Editing data and semantic types

Admins, and people with [permission to manage table metadata](../permissions/data#manage-table-metadata-permissions), can cast data types and edit semantic types in the Admin settings' Table Metadata tab.

### Cast data types

Data types can't be edited in Metabase directly, but you can cast certain [data types to different types](./metadata-editing#cast-to-a-specific-data-type) so that, for example, Metabase will interpret a text data type as a date type.

Changes made in Table Metadata apply across your entire Metabase. However, if you build a query in the query builder, you can use type casting custom expressions like [`date()`](../questions/query-builder/expressions-list#date) or [`integer()`](../questions/query-builder/expressions-list#integer) to cast a string to a different type just in your query.

### Semantic types don't change the data types

You can pick a semantic type compatible with the underlying data type in [table metadata settings](./metadata-editing#semantic-type).

Semantic types only add meaning; they should not be used for type casting. For example, if you set a text field's semantic type to "Quantity", Metabase will still treat the field as a text field. Instead, apply semantic types to tell Metabase how to format or visualize the field (like telling Metabase that a numeric value represents a percentage).

## What data and semantic types enable

### Display format

Some semantic types change the way the data in the field is displayed.

Formatting settings from Table Metadata settings will be applied across your Metabase, but people can change them for individual charts.

  Semantic type            Format
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Percentage               Displayed as percentage, for example 0.75 will be displayed as 75%
  Currency                 On charts and in detail view, the values are prepended by the currency symbol, e.g., `$134.65`. By default in the table view, the currency symbol is only displayed in the header, but you can change the metadata formatting settings to show the symbol for every row.
  Latitude/Longitude       Displayed as coordinates, e.g., `0.00000000° N`
  Email                    Display as a `mailto` link
  URL                      Can format as a clickable link
  Image URL                Can display as an image. See [table format settings](../questions/visualizations/table#display-as)
  Avatar URL               Can display as avatar circle image. See [table format settings](../questions/visualizations/table#display-as)
  Field containing JSON    In detail view, display as prettified JSON
  Entity and Foreign key   Highlighted in table view

### Visualizations

When you create a question in the query builder, Metabase will automatically choose the most suitable chart for you based on the data types and the semantic types of the field in the "Group by" step (you can change the chart type later).

  Group by data type     Automatic chart
  ---------------------- -----------------
  Text/Category          Bar chart
  Temporal               Line chart
  Numeric - binned       Bar chart
  Numeric - not binned   Table
  Boolean                Bar chart
  No aggregation         Table

Additionally, if you use location semantic types:

  Group by semantic type            Functionality
  --------------------------------- --------------------------
  Latitude/Longitude - binned       Grid map
  Latitude/longitude - not binned   Pin map
  Country                           World region map
  State                             United States region map

### Extract values from columns

For some fields, you can quickly extract values from columns using [shortcuts in table view](../questions/visualizations/table#extract-domain-subdomain-host-or-path) or in the [custom expression editor](../questions/query-builder/expressions) in the query builder:

  Group by data type    Extract
  --------------------- -----------------------------------------
  URL semantic types    Extract host, domain, subdomain, path
  Email semantic type   Extract host, domain
  Temporal data types   Extract date parts like month, day, etc

### X-rays

When you [X-ray](../exploration-and-organization/x-rays) a table, model, or entity, Metabase considers both the data type and the field type to display different charts that summarize that data.

### Field Filters

Knowing what field types are and how they work is helpful when using [field filters](/learn/metabase-basics/querying-and-dashboards/sql-in-metabase/field-filters), as you can only create field filters for [certain field types](../questions/native-editor/field-filters#when-to-use-a-field-filter-variable-vs-a-basic-variable).

### JSON unfolding

See [Working with JSON](./json-unfolding).

## Set semantic types in models to enable people to explore results with the query builder

You can set field types for [models](./models), which helps Metabase understand how to work with data in models built using SQL. If you set each column type in a SQL model, people will be able to explore that model using the query builder and drill-through menus.

With records that include integer entity keys, you can also configure text fields in models to [surface individual records in search](./models#surface-individual-records-in-search-by-matching-against-this-column).

## Further Reading

-   [Exploring data with Metabase's data browser](/learn/metabase-basics/querying-and-dashboards/data-browser).
-   [The Table Metadata page: editing metadata](./metadata-editing).
-   [Field Filters: create smart filter widgets for SQL questions](/learn/metabase-basics/querying-and-dashboards/sql-in-metabase/field-filters).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/data-modeling/semantic-types.md) ]