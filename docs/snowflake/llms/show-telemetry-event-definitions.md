# Source: https://docs.snowflake.com/en/sql-reference/sql/show-telemetry-event-definitions.md

# SHOW TELEMETRY EVENT DEFINITIONS

Lists the [event definitions](../../developer-guide/native-apps/event-definition.md) for the specified app.

## Syntax

```sqlsyntax
SHOW TELEMETRY EVENT DEFINITIONS IN APPLICATION <name>
```

## Parameters

`name`
:   Specifies the identifier for the app. If the identifier contains
    spaces, special characters, or mixed-case characters, the entire string must be enclosed
    in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Output

Shows information about the event definitions for an app.

| Column | Description |
| --- | --- |
| `name` | The name of the event definition. Event definition names begin with the `SNOWFLAKE$` prefix. |
| `type` | The type of event definition. See [Configure event definitions for an app](../../developer-guide/native-apps/event-definition.md) for more information. |
| `sharing` | Specifies if the event definition is `MANDATORY` or `OPTIONAL`. |
| `status` | Specifies if the event definition is enabled in the consumer account. |

## Usage notes

* The command doesn’t require a running warehouse to execute.
* The command only returns objects for which the current user’s current role has been granted at least one access privilege.
* The MANAGE GRANTS access privilege implicitly allows its holder to see every object in the account. By default, only the account
  administrator (users with the ACCOUNTADMIN role) and security administrator (users with the SECURITYADMIN role) have the
  MANAGE GRANTS privilege.

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Example

```sqlexample
SHOW TELEMETRY EVENT DEFINITIONS IN APPLICATION hello_snowflake;
```

```output
+--------------------------+----------------+---------------+--------------+
|   name                   |   type         |   sharing     |   status     |
+--------------------------+----------------+---------------+--------------+
|   SNOWFLAKE$DEBUG_LOGS   |   DEBUG_LOGS   |   OPTIONAL    |   ENABLED    |
|   SNOWFLAKE$TRACES       |   TRACES       |   MANDATORY   |   ENABLED    |
+--------------------------+----------------+---------------+--------------+
```
