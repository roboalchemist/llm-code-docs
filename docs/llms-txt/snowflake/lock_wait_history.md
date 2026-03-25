# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/lock_wait_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/lock_wait_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# LOCK_WAIT_HISTORY view

This Account Usage view includes the history of [transactions](../transactions.md) that wait on locks.
For details, see [Analyzing blocked transactions with the LOCK_WAIT_HISTORY view](../transactions.md).

## Columns

| OBJECT_ID | NUMBER | Internal/system-generated identifier for the blocking object (such as a table) on which the transaction is waiting for a lock. |
| --- | --- | --- |
| LOCK_TYPE | VARCHAR | Type of lock. Valid values are `PARTITION`, `STREAM`, `TABLE`, and `ROW`. `ROW` is shown for hybrid table locks. |
| OBJECT_NAME | VARCHAR | Identifier for the object (such as a table) on which the transaction is waiting for a lock. `ROW` is shown for hybrid table locks. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the object on which the transaction is waiting for a lock. `0` is shown for hybrid tables. |
| SCHEMA_NAME | VARCHAR | Identifier for the schema of the object on which the transaction is waiting for a lock. NULL is shown for `ROW` locks. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database of the object on which the transaction is waiting for a lock. |
| DATABASE_NAME | VARCHAR | Identifier for the database of the object on which the transaction is waiting for a lock. |
| QUERY_ID | VARCHAR | Internal/system-generated identifier for the SQL statement that is waiting on the lock. |
| TRANSACTION_ID | NUMBER | Internal/system-generated [identifier for the transaction](../transactions.md) with the statement that is waiting on the lock. Can be joined with the [QUERY_HISTORY view](query_history.md) for additional details about the statements in the transaction. |
| REQUESTED_AT | TIMESTAMP_LTZ | Timestamp when the lock was requested by the transaction waiting for the lock. |
| ACQUIRED_AT | TIMESTAMP_LTZ | Timestamp when the lock was acquired by the transaction holding the lock. |
| BLOCKER_QUERIES | VARIANT | JSON array of objects. Each object is a blocker query with the following properties:   *`is_snowflake`: TRUE if the query is a background process run by Snowflake (e.g., automatic maintenance of   materialized views).* `query_id`: Query ID of the current statement in the blocker transaction that blocked the statement. Empty if   `is_snowflake` is true. * `transaction_id`: ID of the blocker transaction. Empty if `is_snowflake` is true.   There may be up to 20 objects in this array. |

## Usage notes

* The first blocker query ID that is returned in the `blocker_queries` array is the ID of the query that was being executed
  in the transaction that holds the lock when the transaction waiting for the lock started waiting.
  Note that it is possible that queries prior to that query in the blocker transaction also acquired the lock and should be investigated.
* Each row in the output represents a transaction waiting on a lock. Note that there may be other transactions ahead
  of that transaction, waiting on the same lock.

## Examples

Find all the blocked transactions that requested locks within the past 24 hours:

```sqlexample
SELECT query_id, object_name, transaction_id, blocker_queries
  FROM SNOWFLAKE.ACCOUNT_USAGE.LOCK_WAIT_HISTORY
  WHERE requested_at >= DATEADD('hours', -24, CURRENT_TIMESTAMP());
```

For additional examples, see [Analyzing blocked transactions with the LOCK_WAIT_HISTORY view](../transactions.md).
