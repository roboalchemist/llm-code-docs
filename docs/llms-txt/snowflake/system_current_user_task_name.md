# Source: https://docs.snowflake.com/en/sql-reference/functions/system_current_user_task_name.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$CURRENT_USER_TASK_NAME

Returns the name of the task currently executing when invoked from the statement or stored procedure defined by the task.

## Syntax

```sqlsyntax
SYSTEM$CURRENT_USER_TASK_NAME()
```

## Arguments

None.

## Examples

Insert the name of the current task into a table along with the current time:

> ```sqlexample
> CREATE TASK mytask
>   WAREHOUSE = mywh,
>   SCHEDULE = '5 MINUTE'
> AS
>   INSERT INTO mytable(ts, task) VALUES(CURRENT_TIMESTAMP, SYSTEM$CURRENT_USER_TASK_NAME());
>
> SELECT * FROM mytable;
>
> +-------------------------+------------------------------------+
> | TS                      | TASK                               |
> |-------------------------+------------------------------------|
> | 2018-11-15 07:41:33.463 | MYDB.PUBLIC.MYTASK                 |
> +-------------------------+------------------------------------+
> ```
