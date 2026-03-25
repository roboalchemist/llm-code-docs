# Source: https://docs.snowflake.com/en/sql-reference/functions/system_schedule_async_replication_group_refresh.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH

Starts a refresh operation for a replication group or a failover group, in the background.
You can call this function in a stored procedure to begin one or more refresh operations
and continue doing work while the refreshes are in progress.

See also:
:   [Replication groups and failover groups](../../user-guide/account-replication-intro.md),
    [ALTER REPLICATION GROUP](../sql/alter-replication-group.md),
    [ALTER FAILOVER GROUP](../sql/alter-failover-group.md),
    [REPLICATION_GROUP_REFRESH_HISTORY view](../organization-usage/replication_group_refresh_history.md)

## Syntax

```sqlsyntax
SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH(<replication_group_name>)
SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH(<failover_group_name>)
```

## Arguments

`'replication_group_name'` or `'failover_group_name'`
:   The name of the replication group or failover group to refresh.

## Usage notes

* This function has the same effect as an
  ALTER REPLICATION GROUP … REFRESH or ALTER FAILOVER GROUP … REFRESH command,
  but doesn’t wait for the operation to complete.
* Only account administrators (that is, users with the ACCOUNTADMIN role) can execute this function.
* This function must be executed from the secondary account.

## Examples

Start refreshing two failover groups simultaneously:

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> SELECT SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH('failover_group_1');
> SELECT SYSTEM$SCHEDULE_ASYNC_REPLICATION_GROUP_REFRESH('failover_group_2');
> ```
