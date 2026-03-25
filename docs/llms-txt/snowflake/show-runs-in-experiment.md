# Source: https://docs.snowflake.com/en/sql-reference/sql/show-runs-in-experiment.md

# SHOW RUNS IN EXPERIMENT

Lists the runs in an [experiment](../../developer-guide/snowflake-ml/experiments.md).

See also:
:   [CREATE EXPERIMENT](create-experiment.md) , [ALTER EXPERIMENT](alter-experiment.md), [SHOW EXPERIMENTS](show-experiments.md) , [DROP EXPERIMENT](drop-experiment.md) , [SHOW RUN … IN EXPERIMENT](show-run-in-experiment.md)

## Syntax

```sqlsyntax
SHOW RUNS [ LIKE '<pattern>' ] IN EXPERIMENT <name>
```

## Parameters

`LIKE 'pattern'`
:   Optionally filters the command output by object name. The filter uses case-insensitive pattern matching, with support for SQL
    wildcard characters (`%` and `_`).

    For example, the following patterns return the same results:

    `... LIKE '%testing%' ...`

    `... LIKE '%TESTING%' ...`

    . Default: No value (no filtering is applied to the output).

`name`
:   Specifies the identifier of the experiment to inspect.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the run was created. |
| `name` | The identifier for the run. |
| `database_name` | The database that the run is stored in. |
| `schema_name` | The schema that the run is stored in. |
| `experiment_name` | The experiment that the run belongs to. |
| `metadata` | A JSON object containing the run status and metrics.  The `status` field of the run indicates if it’s `RUNNING` or `FINISHED`.  The `metrics` field reports the metrics of the run. Only the latest metric value (the one with the highest `step`) is included. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Experiment |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

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

* The command returns a maximum of ten thousand records for the specified object type, as dictated by the access privileges for the role
  used to execute the command. Any records above the ten thousand records limit aren’t returned, even with a filter applied.

  To view results for which more than ten thousand records exist, query the corresponding view (if one exists) in the [Snowflake Information Schema](../info-schema.md).

* Executing the command for schema-level objects only returns an object if the current role also has at least one privilege on the
  parent database and schema.
