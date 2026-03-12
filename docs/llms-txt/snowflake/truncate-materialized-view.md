# Source: https://docs.snowflake.com/en/sql-reference/sql/truncate-materialized-view.md

# TRUNCATE MATERIALIZED VIEW

Removes all rows from a materialized view, but leaves the view intact (including all privileges and constraints on the materialized view).

Note that this is different from [DROP MATERIALIZED VIEW](drop-materialized-view.md), which removes the materialized view from the system.

See also:
:   [ALTER MATERIALIZED VIEW](alter-materialized-view.md) , [CREATE MATERIALIZED VIEW](create-materialized-view.md)

## Syntax

```sqlsyntax
TRUNCATE MATERIALIZED VIEW <name>
```

## Parameters

`name`
:   Specifies the identifier for the materialized view to truncate. If the identifier contains spaces or special characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive (e.g. `"My Object"`).

    If the materialized view identifier is not fully-qualified (in the form of `db_name.schema_name.materialized_view_name`
    or `schema_name.materialized_view_name`), then the command looks for the materialized view in the current schema for the
    session.

## Usage notes

* Snowflake no longer supports truncation of materialized views.
* If you truncate a materialized view, the background maintenance service automatically updates the materialized view. If
  any queries are executed on the view while it is in the process of being updated, Snowflake ensures consistent results
  by retrieving any rows, as needed, from the base table.

  However, the maintenance service uses computing resources to update the materialized view and it is usually more efficient
  (i.e. less costly) to let an out-of-date materialized view “catch up” naturally over time than to truncate the view. As such,
  we do not generally recommend truncating a materialized view.
* Although each query on the view will still show up-to-date results, the query might run more slowly as Snowflake
  updates the materialized view or looks up data in the base table.

## Examples

This feature has been obsoleted.
