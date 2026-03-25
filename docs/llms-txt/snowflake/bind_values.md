# Source: https://docs.snowflake.com/en/sql-reference/functions/bind_values.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# BIND_VALUES

This INFORMATION_SCHEMA table function returns information about the values of
[bind variables](../bind-variables.md) used in queries.

## Syntax

```sqlsyntax
BIND_VALUES( <query_id> )
```

## Arguments

`query_id`
:   The string identifier of a query that includes one or more bind variables.

    Snowflake query IDs are unique strings that resemble `01b71944-0001-b181-0000-0129032279f6`.

    If NULL, an empty table is returned.

## Usage notes

* Returns bind variable values for queries that are run by the current user. Also returns bind variable values for queries
  that are run by any user when the role that is currently active in a user’s session, or a higher role in a hierarchy,
  has the MONITOR or OPERATE privilege on the user-managed warehouses where the queries were run. For more information,
  see [Virtual warehouse privileges](../../user-guide/security-access-control-privileges.md).
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the
  function name must be fully qualified. For more information, see [Snowflake Information Schema](../info-schema.md).
* This function can return all queries run in the past seven days.
* This function might not return the bind values or might return an error for the following scenarios:

  * The [ALLOW_BIND_VALUES_ACCESS](../parameters.md) account-level parameter is set to `FALSE`.
  * The bind variables have large values that exceed Snowflake storage thresholds.
  * The queries have a large number of bind variables that exceed Snowflake storage thresholds.
  * The bind variables contain sensitive data. The extraction and processing are done on a best-effort basis, and
    whether data is considered sensitive depends on the context.
  * The function call specifies a query that includes [array binds](../bind-variables.md).
  * The function call specifies a query that doesn’t exist.
  * The function call specifies a query that has expired and is no longer in the query history.

## Output

The BIND_VALUES table function produces one row for each bind variable that is used in the specified query. Each row contains the
following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| QUERY_ID | VARCHAR | The ID of the query. |
| POSITION | NUMBER | For positional bind variables, the position of the bind variable. The field is NULL for named bind variables. |
| NAME | VARCHAR | For named bind variables, the name of the bind variable. The field is NULL for positional bind variables. |
| TYPE | VARCHAR | The Snowflake data type of the bind variable. |
| VALUE | VARCHAR | The value of the bind variable. Bind values that contain more than 100,000 characters are truncated. |

## Examples

See [Retrieve bind variable values](../bind-variables.md).
