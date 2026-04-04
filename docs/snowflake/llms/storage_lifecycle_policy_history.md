# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/storage_lifecycle_policy_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/storage_lifecycle_policy_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/storage_lifecycle_policy_history.md

Categories:
:   [Table functions](../functions-table.md) (Information Schema)

# STORAGE_LIFECYCLE_POLICY_HISTORY

Returns execution history for [storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies.md)
in your account within the last 14 days.

Use this table function to query the most recent policy executions (completed or still running), in descending order by
execution end time. For more information about monitoring storage lifecycle policies, see
[Monitor storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-monitoring.md).

See also:
:   [CREATE STORAGE LIFECYCLE POLICY](../sql/create-storage-lifecycle-policy.md) , [ALTER STORAGE LIFECYCLE POLICY](../sql/alter-storage-lifecycle-policy.md) , [DROP STORAGE LIFECYCLE POLICY](../sql/drop-storage-lifecycle-policy.md)

## Syntax

**By object**

```sqlsyntax
STORAGE_LIFECYCLE_POLICY_HISTORY(
  REF_ENTITY_NAME => '<string>',
  REF_ENTITY_DOMAIN => '<string>'
  [, TIME_RANGE_START => <constant_expr> ]
  [, TIME_RANGE_END => <constant_expr> ]
  [, RESULT_LIMIT => <integer> ] )
```

**By storage lifecycle policy**

```sqlsyntax
STORAGE_LIFECYCLE_POLICY_HISTORY(
  POLICY_NAME => '<string>'
  [, TIME_RANGE_START => <constant_expr> ]
  [, TIME_RANGE_END => <constant_expr> ]
  [, RESULT_LIMIT => <integer> ] )
```

## Arguments

> **Note:**
>
> Specify one of the following options when you call the function:
>
> * REF_ENTITY_NAME and REF_ENTITY_DOMAIN: Retrieves the execution history for all storage lifecycle policies attached to
>   an object (table).
> * POLICY_NAME: Retrieves the execution history for a particular storage lifecycle policy specified by name.

**Required:**

`REF_ENTITY_NAME => 'string'`
:   The identifier for the object (table) that the execution occurred on; for example, the name of the
    table that the storage lifecycle policy is attached to.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive. For more information, see [Identifier requirements](../identifiers-syntax.md).

`REF_ENTITY_DOMAIN => 'string'`
:   The object type to which the storage lifecycle policy is attached:

    * `'Table'`: Specifies that the storage lifecycle policy is attached to a table.

`POLICY_NAME => 'string'`
:   The identifier of a storage lifecycle policy to retrieve execution history for.
    If you don’t specify a policy name, you must specify values for REF_ENTITY_NAME and REF_ENTITY_DOMAIN.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

**Optional:**

`TIME_RANGE_START => constant_expr`, . `TIME_RANGE_END => constant_expr`
:   Time range, within the last 14 days, in which the policy execution occurred.

    If neither parameter is specified, the function returns rows (up to the RESULT_LIMIT) for the latest policy executions in descending
    order by END_TIME.

`RESULT_LIMIT => integer`
:   The maximum number of rows returned by the function.

    Range: `1` to `1000`

    Default: `1000`.

## Returns

The function returns execution history records for storage lifecycle policies. Each record contains information about the
policy execution, including the policy name, associated table, execution state, start and end times, and execution results.

For detailed column descriptions, see Output.

## Output

The function returns the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| POLICY_DB | VARCHAR | The name of the database that contains the policy. |
| POLICY_SCHEMA | VARCHAR | The name of the schema that contains the policy. |
| POLICY_NAME | VARCHAR | The name of the policy. |
| REF_ENTITY_DB | VARCHAR | The name of the database that contains the object that the policy is attached to. |
| REF_ENTITY_SCHEMA | VARCHAR | The name of the schema that contains the object that the policy is attached to. |
| REF_ENTITY_NAME | VARCHAR | The name of the object that the policy is attached to. |
| REF_ENTITY_DOMAIN | VARCHAR | The domain (type) of the object that the policy is attached to; for example, `Table`. |
| STATE | VARCHAR | The state of the policy execution: `QUEUED`, `EXECUTING`, `SUCCEEDED`, or `FAILED`. |
| START_TIME | TIMESTAMP_LTZ | Earliest timestamp of when any task in the policy execution started. |
| END_TIME | TIMESTAMP_LTZ | Latest timestamp of when any task in the policy execution completed. |
| EXECUTION_RESULT | VARIANT | JSON object that contains the results of the jobs run during the policy execution. For more information, see EXECUTION_RESULT fields. |
| POLICY_BODY | VARCHAR | The body of the storage lifecycle policy. |

### EXECUTION_RESULT fields

The `EXECUTION_RESULT` column is a JSON object that includes nested objects for each task type in the policy execution:

* `EXPIRE`: Contains results for expiration operations (permanently deleting rows).
* `ARCHIVE`: Contains results for archiving operations (moving rows to archive storage).
* `EXPIRE_ARCHIVE`: Contains results for expiration operations (permanently deleting rows from archive storage).

Each nested object can contain the following fields, where specific fields apply to specific task types:

| Field name | Description |
| --- | --- |
| START_TIME | Individual task start timestamp. |
| END_TIME | Individual task end timestamp |
| STATE | Individual task status: `SUCCEEDED` or `FAILED`. |
| ROWS_EXPIRED | (EXPIRE task only) The number of rows permanently deleted from active storage. |
| ROWS_ARCHIVED | (ARCHIVE task only) The number of rows archived to storage. |
| ROWS_EXPIRED_FROM_ARCHIVE | (EXPIRE_ARCHIVE task only) The number of rows permanently deleted from archive storage. |
| ERROR_MESSAGE_CODE | The code identifying the type of error encountered during task execution. |
| ERROR_MESSAGE | A detailed error message. |

Example `EXECUTION_RESULT` body:

```output
EXECUTION_RESULT =
{
  “EXPIRE”: {
    “start_time”: "Thu, 27 Jun 2024 02:57:57 -0700",
    “end_time”: "Thu, 27 Jun 2024 02:58:01 -0700",
    “state”: "SUCCEEDED",
    “rows_expired”: 100,
    “error_message_code”: null,
    “error_message”: null
  }
}
```

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY STORAGE LIFECYCLE POLICY | Global | If the role that calls the function has this privilege, Snowflake returns all policy executions related to all policies and their associated tables in the Snowflake account. |
| APPLY | Storage lifecycle policy | To view the executions for a policy, a role must also have the OWNERSHIP privilege on the table(s) associated with the policy. This privilege is not required if a role has the global APPLY STORAGE LIFECYCLE POLICY privilege. |
| OWNERSHIP | Table | To view the executions for a policy, a role must also have the APPLY privilege on the policy associated with the table. This privilege is not required if a role has the global APPLY STORAGE LIFECYCLE POLICY privilege. |

## Usage notes

* Results are returned based on the privileges granted to the role that executes the query:

  * If the role has the global APPLY STORAGE LIFECYCLE POLICY privilege, Snowflake returns all policy executions related to any policy and
    table associations in the account.
  * If the role has the APPLY privilege on a specific storage lifecycle policy, Snowflake returns executions for that policy
    only for objects that are owned by the role that calls the function.
  * If the role has either the APPLY privilege or the OWNERSHIP privilege on the policy,
    but does *not* have the OWNERSHIP privilege on the table that the policy is attached to,
    Snowflake doesn’t show policy executions for the policy in the results.
  * If the role has no policy privileges, but has the OWNERSHIP privilege on the table that a policy is attached to, Snowflake returns an error
    message and doesn’t return any policy executions.

## Examples

Specify the `REF_ENTITY_NAME` and `REF_ENTITY_DOMAIN` arguments to
retrieve the storage lifecycle policy history for
a table named `t1`:

```sqlexample
SELECT * FROM
  TABLE (
    INFORMATION_SCHEMA.STORAGE_LIFECYCLE_POLICY_HISTORY(
      REF_ENTITY_NAME => 'my_db.my_schema.t1',
      REF_ENTITY_DOMAIN => 'Table'
    )
  );
```

Retrieve the storage lifecycle policy history for
each table that has the policy named `slp` associated with it, and
limit the results to 100 rows:

```sqlexample
SELECT * FROM
  TABLE(
    INFORMATION_SCHEMA.STORAGE_LIFECYCLE_POLICY_HISTORY(
      POLICY_NAME => 'my_db.my_schema.slp',
      RESULT_LIMIT => 100
    )
  );
```

Retrieve the 100 most recent executions for a specified policy, scheduled within the last hour:

```sqlexample
SELECT * FROM
TABLE(
  INFORMATION_SCHEMA.STORAGE_LIFECYCLE_POLICY_HISTORY(
    POLICY_NAME => 'my_db.my_schema.slp',
    TIME_RANGE_START => DATEADD('HOUR', -1, CURRENT_TIMESTAMP()),
    RESULT_LIMIT => 100
  )
);
```

Retrieve the policy execution history for a given table within a 30-minute time range:

```sqlexample
SELECT * FROM
TABLE (
  INFORMATION_SCHEMA.STORAGE_LIFECYCLE_POLICY_HISTORY(
    REF_ENTITY_NAME => 'my_db.my_schema.t1',
    REF_ENTITY_DOMAIN => 'Table',
    TIME_RANGE_START => TO_TIMESTAMP_LTZ('2024-07-08 12:00:00.000 -0700'),
    TIME_RANGE_END => TO_TIMESTAMP_LTZ('2024-07-08 12:30:00.000 -0700')
  )
);
```
