# Source: https://docs.snowflake.com/en/user-guide/data-quality-monitor.md

# Track the use of data metric functions

## List your DMFs

Use the [SHOW DATA METRIC FUNCTIONS](../sql-reference/sql/show-data-metric-functions.md) or [SHOW FUNCTIONS](../sql-reference/sql/show-functions.md) command to list data metric functions (DMFs)
in your account, database, or schema. For example, to list all DMFs in the account, execute the following:

```sqlexample
SHOW DATA METRIC FUNCTIONS IN ACCOUNT;
```

Alternatively, you can query the [Information Schema FUNCTIONS view](../sql-reference/info-schema/functions.md) or the
[Account Usage FUNCTIONS view](../sql-reference/account-usage/functions.md) to list your DMFs in the specified database or your account.

The `is_data_metric` column specifies whether the function is a DMF.

## List objects associated with a DMF

You can call the [DATA_METRIC_FUNCTION_REFERENCES](../sql-reference/functions/data_metric_function_references.md)
Information Schema table function to identify the tables or views associated with a given DMF.

To return a row for each object (table or view) that has the DMF named `count_positive_numbers` set on that table or
view, execute the following:

> ```sqlexample
> USE DATABASE governance;
> USE SCHEMA INFORMATION_SCHEMA;
> SELECT *
>   FROM TABLE(
>     INFORMATION_SCHEMA.DATA_METRIC_FUNCTION_REFERENCES(
>       METRIC_NAME => 'governance.dmfs.count_positive_numbers'
>     )
>   );
> ```

You can also query the [DATA_METRIC_FUNCTION_REFERENCES](../sql-reference/account-usage/data_metric_function_references.md)
Account Usage view to determine these associations.

## List DMFs associated with an object

You can call the [DATA_METRIC_FUNCTION_REFERENCES](../sql-reference/functions/data_metric_function_references.md)
Information Schema table function to identify the DMFs associated with a given table or view.

To return a row for each DMF assigned to the table named `hr.tables.empl_info`, execute the following:

> ```sqlexample
> USE DATABASE governance;
> USE SCHEMA INFORMATION_SCHEMA;
> SELECT *
>   FROM TABLE(
>     INFORMATION_SCHEMA.DATA_METRIC_FUNCTION_REFERENCES(
>       REF_ENTITY_NAME => 'hr.tables.empl_info',
>       REF_ENTITY_DOMAIN => 'table'
>     )
>   );
> ```

You can also query the [DATA_METRIC_FUNCTION_REFERENCES](../sql-reference/account-usage/data_metric_function_references.md)
Account Usage view to determine these associations.
