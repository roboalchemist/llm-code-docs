# Source: https://docs.snowflake.com/en/sql-reference/functions/last_query_id.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# LAST_QUERY_ID

Returns the ID of a specified query in the current session. If no query is specified, the most recent
query is returned.

> **Tip:**
>
> Instead of using this function with the [RESULT_SCAN](result_scan.md) function to process the results of a
> previous command, you can use the [pipe operator](../operators-flow.md) (`->>`). That way,
> you can run the command and process its result set in a single step.

## Syntax

```sqlsyntax
LAST_QUERY_ID( [ <num> ] )
```

## Arguments

`num`
:   Specifies the query to return, based on the position of the query (within the session).

    Default: `-1`

## Usage notes

* Positive numbers start with the first query that was run in the session. For example:

  * `LAST_QUERY_ID(1)` returns the first query.
  * `LAST_QUERY_ID(2)` returns the second query.
  * `LAST_QUERY_ID(6)` returns the sixth query.
* Negative numbers start with the most recent query in the session. For example:

  * `LAST_QUERY_ID(-1)` returns the most recent query (equivalent to `LAST_QUERY_ID()`).
  * `LAST_QUERY_ID(-2)` returns the second most recent query.
* The last LAST_QUERY_ID function considers all statements that were run within the current session,
  including child statements (for example, statements that were executed as part of a stored procedure,
  anonymous block, or [pipe operator](../operators-flow.md) statement). If you want to
  get the query ID of a statement based only on its position in a series of statements, consider using
  the pipe operator. For more complex use cases, we recommend using the
  [global variable SQLID](../../developer-guide/snowflake-scripting/query-id.md) in Snowflake Scripting blocks.

## Examples

Return the ID for the most recent query:

```sqlexample
SELECT LAST_QUERY_ID();
```

Return the ID for the first query that was run in the session:

```sqlexample
SELECT LAST_QUERY_ID(1);
```
