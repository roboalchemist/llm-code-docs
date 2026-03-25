# Source: https://docs.snowflake.com/en/user-guide/dynamic-tables-manual-refresh.md

# Manually refresh dynamic tables

You can manually refresh a dynamic table to include the latest data without waiting for the next [scheduled refresh](dynamic-tables-refresh.md).
This is useful for one-time updates or when a table has a large target lag and the next refresh occurs much later.

> **Tip:**
>
> Avoid frequent manual refreshes on dynamic tables with downstream dynamic tables that are expected to refresh according to target lag.
> These kinds of manual refreshes can cause scheduled refreshes to skip and prevent downstream tables from updating.

To manually refresh, use the ALTER DYNAMIC TABLE … REFRESH command or Snowsight as shown in the following steps:

SQLSnowsight

```sqlexample
ALTER DYNAMIC TABLE my_dynamic_table REFRESH
```

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Select Monitoring » Dynamic Tables.
3. In the list, find your dynamic table, and then select  » Refresh Manually.

For situations that require precise refresh timing, such as aligning refreshes with external system schedules or batch processing windows, you
can use a task with a CRON expression to trigger the refresh.

For example:

```sqlexample
-- Create the task
CREATE TASK my_dt_refresh_task
  WAREHOUSE = my_wh
  SCHEDULE = 'USING CRON 0 0 * * * America/Los_Angeles' -- Example: daily at midnight PST
  COMMENT = 'Daily 5pm PT manual refresh of my_dynamic_table'
  AS
    ALTER DYNAMIC TABLE my_dynamic_table REFRESH;

-- Enable the task
ALTER TASK my_dt_refresh_task RESUME;

-- Show the task
SHOW TASKS LIKE 'my_dt_refresh_task';
```

```output
+------------+-----------------+-------------------------------------+---------------+-------------+--------------+-------------------------------------------------+-----------|-------------------------------------------+------------------+---------+----------------------------------------------+-----------+-----------------------------+-------------------+-------------------------------|-------------------+-----------------+--------+---------------------+-----------------------+---------------------+-----------------+----------------------------+-----------------+
| CREATED_ON | NAME            | ID                                  | DATABASE_NAME | SCHEMA_NAME | OWNER        | COMMENT                                         | WAREHOUSE | SCHEDULE                                  | [ ] PREDECESSORS | STATE   | DEFINITION                                   | CONDITION | ALLOW_OVERLAPPING_EXECUTION | ERROR_INTEGRATION | LAST_COMMITTED_ON             | LAST_SUSPENDED_ON | OWNER_ROLE_TYPE | CONFIG | TASK_RELATIONS      | LAST_SUSPENDED_REASON | SUCCESS_INTEGRATION | SCHEDULING_MODE | TARGET_COMPLETION_INTERVAL | EXECUTE_AS_USER |
|------------+-----------------+-------------------------------------+---------------+-------------+--------------+-------------------------------------------------+-----------+-------------------------------------------+------------------+---------+----------------------------------------------+-----------+-----------------------------+-------------------+-------------------------------+-------------------+-----------------+--------+---------------------+-----------------------+---------------------+-----------------+----------------------------+-----------------|
| 2025-10-02 | DT_REFRESH_TASK | 01bf6f0d-690f-f373-0000-000000025e3d| mydb          | my_schema   | ACCOUNTADMIN | Daily 5pm PT manual refresh of my_dynamic_table | mywh      | USING CRON 0 17 * * * America/Los_Angeles | []               | Started | ALTER DYNAMIC TABLE my_dynamic_table REFRESH | null      | false                       | null              | 2025-10-02 05:08:52.897 +0000 | null              | ROLE            | null   | {"Predecessors":[]} | null                  | null                | null            | null                       | null            |
+------------+-----------------+-------------------------------------+---------------+-------------+--------------+-------------------------------------------------+-----------|-------------------------------------------+------------------+---------+----------------------------------------------+-----------+-----------------------------+-------------------+-------------------------------|-------------------+-----------------+--------+---------------------+-----------------------+---------------------+-----------------+----------------------------+-----------------+
```

For most cases, Snowflake recommends using target lag, which optimizes refresh frequency and can reduce costs compared to fixed CRON schedules
that might run unnecessarily.
