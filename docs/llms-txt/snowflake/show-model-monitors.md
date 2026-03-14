# Source: https://docs.snowflake.com/en/sql-reference/sql/show-model-monitors.md

# SHOW MODEL MONITORS

Lists all [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md) that you can access in
the current or specified schema and displays information about each one.

See also:
:   [CREATE MODEL MONITOR](create-model-monitor.md),
    [ALTER MODEL MONITOR](alter-model-monitor.md),
    [DESCRIBE MODEL MONITOR](desc-model-monitor.md),
    [DROP MODEL MONITOR](drop-model-monitor.md)

## Syntax

```sqlsyntax
SHOW MODEL MONITORS
[ LIKE <pattern> ]
[ IN
    {
      ACCOUNT                  |

      DATABASE                 |
      DATABASE <database_name> |

      SCHEMA                   |
      SCHEMA <schema_name>     |
      <schema_name>
    }
 ]
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

`[ IN ... ]`
:   Optionally specifies the scope of the command. Specify one of the following:

    `ACCOUNT`
    :   Returns records for the entire account.

    `DATABASE`, . `DATABASE db_name`
    :   Returns records for the current database in use or for a specified database (`db_name`).

        If you specify `DATABASE` without `db_name` and no database is in use, the keyword has no effect on the output.

        > **Note:**
        >
        > Using SHOW commands without an `IN` clause in a database context can result in fewer than expected results.
        >
        > Objects with the same name are only displayed once if no `IN` clause is used. For example, if you have table `t1` in
        > `schema1` and table `t1` in `schema2`, and they are both in scope of the database context you’ve specified (that is, the database
        > you’ve selected is the parent of `schema1` and `schema2`), then SHOW TABLES only displays one of the `t1` tables.

    `SCHEMA`, . `SCHEMA schema_name`
    :   Returns records for the current schema in use or a specified schema (`schema_name`).

        `SCHEMA` is optional if a database is in use or if you specify the fully qualified `schema_name` (for example, `db.schema`).

        If no database is in use, specifying `SCHEMA` has no effect on the output.

    If you omit `IN ...`, the scope of the command depends on whether the session currently has a database in use:

    * If a database is currently in use, the command returns the objects you have privileges to view in the database. This has the
      same effect as specifying `IN DATABASE`.
    * If no database is currently in use, the command returns the objects you have privileges to view in your account. This has the
      same effect as specifying `IN ACCOUNT`.

## Output

The command output provides model monitor properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the model monitor was created. |
| `name` | Name of the model monitor. |
| `database_name` | Database in which the model monitor is stored. |
| `schema_name` | Schema in which the model monitor is stored. |
| `warehouse_name` | Warehouse used to monitor the model. |
| `refresh_interval` | The refresh interval (target lag) for triggering refresh of the model monitor. |
| `aggregation_window` | The aggregation window for calculating metrics. |
| `model_task` | The task of the model being monitored, either TABULAR_BINARY_CLASSIFICATION or TABULAR_REGRESSION. |
| `monitor_state` | The state of the model monitor:   *ACTIVE: The model monitor is active and operating correctly.* SUSPENDED: Model monitoring is paused. *PARTIALLY_SUSPENDED: An error condition in which one of the underlying tables has stopped refreshing at the expected interval. See DESCRIBE for more details.* UNKNOWN: An error condition in which the state of the underlying tables cannot be identified. |
| `source` | String representation of a JSON object detailing the source table or view on which aggregations are based. If the table does not exist or is not accessible, the value is an empty string. See Table JSON object specification. |
| `baseline` | String representation of a JSON object detailing baseline table being used for monitoring, of which a clone is embedded in the model monitor object. See Table JSON object specification. |
| `model` | String representation of a JSON object containing information specifically about the model being monitored. See Model JSON object specification. |
| `comment` | Comment about the model monitor. |

### Table JSON object specification

The following is an example of the JSON representation of a table, view, or other table-like object, as used by the `source` and `baseline` columns in the command output:

| `name` | Name of the source or baseline table or view. |
| --- | --- |
| `database_name` | Database in which the table or view is stored. |
| `schema_name` | Schema in which the table or view is stored. |
| `status` | The status of the table:   *ACTIVE: The table or view is accessible by the user.* MASKED: The current user does not have access to the table or view. Values of other fields appear masked (that is, as a series of asterisks). *DELETED: The table or view has been deleted.* NOT_SET: The property has not been set. Only applicable for baseline data. |

### Model JSON object specification

The following is an example of the JSON representation of a model, as used by the `model` column in the command output:

| Field | Description |
| --- | --- |
| `model_name` | Name of the model being monitored. |
| `version_name` | Version name of the model version being monitored. |
| `function_name` | Name of the specific function being monitored in the specified model version. |
| `database_name` | Database in which the model is stored. |
| `schema_name` | Schema in which the model is stored. |
| `model_status` | The status of the model. Can be ACTIVE, MASKED, or DELETED. MASKED indicates that the user does not have access to the model; other fields show as a series of asterisks. |
| `version_status` | The status of the model version. Can be ACTIVE or DELETED. (MASKED is not a valid status for a model version, because they do not have access control.) |

## Access control requirements

| Privilege | Target |
| --- | --- |
| Any | Model monitor |

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
