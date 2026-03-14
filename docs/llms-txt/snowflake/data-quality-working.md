# Source: https://docs.snowflake.com/en/user-guide/data-quality-working.md

# Use SQL to set up data metric functions

This topic describes how to use SQL to associate a data metric function (DMF) with a table or view so it runs at regular
intervals. It also describes how to call a DMF directly, for example, if you want to test a DMF before associating it with a table or view.

> **Note:**
>
> To use a user interface to set up data quality checks, which includes associating a DMF with a table, see [Use Snowsight to set up data quality checks](data-quality-ui-setup.md).

## Associate a DMF

You can associate a DMF with a table or view to automatically call it on regular intervals. When associating the DMF, you specify which
columns are passed to the DMF as arguments.

Use an [ALTER TABLE](../sql-reference/sql/alter-table.md) or [ALTER VIEW](../sql-reference/sql/alter-view.md) command to associate a DMF and specify which
columns are passed as arguments. For example, the following command associates the NULL_COUNT system DMF with table `t`. When the
DMF runs, it will return the number of NULL values in the column `c1`.

```sqlexample
ALTER TABLE t
  ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.NULL_COUNT
    ON (c1);
```

Some DMFs don’t accept a column as an argument. For example, to associate the ROW_COUNT system DMF with view `v2`, run the following command:

```sqlexample
ALTER VIEW v2
  ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.ROW_COUNT
    ON ();
```

The [ACCEPTED_VALUES](../sql-reference/functions/dmf_accepted_values.md) DMF contains a lambda expression as well as the column name, which
allows you to check how many records do not match an expected value. For example, the following statement associates the function with table
`t1` so the function returns the number of records where the value of the column `age` is *not* equal to five.

```sqlexample
ALTER TABLE t1
  ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.ACCEPTED_VALUES ON (age, age -> age = 5);
```

### Drop a DMF from an object

You can drop a DMF using an ALTER TABLE or ALTER VIEW command. For example:

> ```sqlexample
> ALTER TABLE t
>   DROP DATA METRIC FUNCTION governance.dmfs.count_positive_numbers
>     ON (c1, c2, c3);
> ```

## Adjust the schedule for DMFs

The [DATA_METRIC_SCHEDULE](../sql-reference/parameters.md) object parameter for a table, view, or materialized view controls how often DMFs run. By default, the schedule is set to one hour.
All data metric functions on a table or view follow the same schedule.

You can use the following approaches to schedule your DMF to run:

* Set the DMF to run after a specified number of minutes.
* Use a cron expression to schedule the DMF to run at a particular frequency.
* Use a trigger event to schedule the DMF to run when there is a [DML change](../sql-reference/sql-dml.md) to the table, such as
  inserting a new row into the table. However:

  * The [reclustering of tables](tables-auto-reclustering.md) doesn’t trigger a DMF to run.
  * The trigger approach is only available for certain kinds of tables. For more information, see
    [ALTER TABLE … SET DATA_METRIC_SCHEDULE](../sql-reference/sql/alter-table.md).

For example:

Set the data metric function schedule to run every 5 minutes:

> ```sqlexample
> ALTER TABLE hr.tables.empl_info SET
>   DATA_METRIC_SCHEDULE = '5 MINUTE';
> ```

Set the data metric function schedule to run at 8:00 AM daily:

> ```sqlexample
> ALTER TABLE hr.tables.empl_info SET
>   DATA_METRIC_SCHEDULE = 'USING CRON 0 8 * * * UTC';
> ```

Set the data metric function schedule to run at 8:00 AM on weekdays only:

> ```sqlexample
> ALTER TABLE hr.tables.empl_info SET
>   DATA_METRIC_SCHEDULE = 'USING CRON 0 8 * * MON,TUE,WED,THU,FRI UTC';
> ```

Set the data metric function schedule to run three times daily at 0600, 1200, and 1800 UTC:

> ```sqlexample
> ALTER TABLE hr.tables.empl_info SET
>   DATA_METRIC_SCHEDULE = 'USING CRON 0 6,12,18 * * * UTC';
> ```

Set the data metric function to run when a general DML operation, such as inserting a new row, modifies the table:

> ```sqlexample
> ALTER TABLE hr.tables.empl_info SET
>   DATA_METRIC_SCHEDULE = 'TRIGGER_ON_CHANGES';
> ```

You can use the [SHOW PARAMETERS](../sql-reference/sql/show-parameters.md) command to view the DMF schedule for a supported table object:

> ```sqlexample
> SHOW PARAMETERS LIKE 'DATA_METRIC_SCHEDULE' IN TABLE hr.tables.empl_info;
> ```
>
> ```output
> +----------------------+--------------------------------+---------+-------+------------------------------------------------------------------------------------------------------------------------------+--------+
> | key                  | value                          | default | level | description                                                                                                                  | type   |
> +----------------------+--------------------------------+---------+-------+------------------------------------------------------------------------------------------------------------------------------+--------+
> | DATA_METRIC_SCHEDULE | USING CRON 0 6,12,18 * * * UTC |         | TABLE | Specify the schedule that data metric functions associated to the table must be executed in order to be used for evaluation. | STRING |
> +----------------------+--------------------------------+---------+-------+------------------------------------------------------------------------------------------------------------------------------+--------+
> ```

For view and materialized view objects, specify `TABLE` as the object domain and check the schedule as follows:

> ```sqlexample
> SHOW PARAMETERS LIKE 'DATA_METRIC_SCHEDULE' IN TABLE mydb.public.my_view;
> ```

> **Note:**
>
> There is a 10-minute lag from when you modify the DMF from a table for any scheduling changes to take effect on previous DMFs that are
> assigned to the table. However, new DMF assignments to the table are not subject to the 10 minute delay. Plan the DMF scheduling and DMF
> unsetting operations carefully to align with your expected [DMF costs](data-quality-intro.md).
>
> Additionally, when you evaluate the DMF results, such as by querying the
> [DATA_QUALITY_MONITORING_RESULTS](../sql-reference/local/data_quality_monitoring_results.md) view, specify the `measurement_time`
> column in your query as the basis for the evaluation. There is an internal process that initiates the DMF evaluation, and it is possible
> that table updates, such as INSERT operations, can occur between the scheduled time and the measurement time. When you use the
> `measurement_time` column, you have a more accurate assessment of the DMF results because the measurement time indicates the
> evaluation time of the DMF.

## Suspend DMFs

You can suspend a DMF to prevent it from running even though it is associated with a table. Alternatively, you can suspend all DMFs
associated with a table with a single statement.

* **To suspend a specific DMF** associated with a table, modify the association to set the SUSPEND parameter. For example:

  ```sqlexample
  ALTER TABLE t1
    MODIFY DATA METRIC FUNCTION SNOWFLAKE.CORE.NULL_COUNT ON ( col1 )
      SUSPEND;
  ```

  To resume running the DMF, use another MODIFY DATA METRIC FUNCTION statement to set the RESUME parameter.
* **To suspend all DMFs** associated with a table, set the table’s schedule to an empty string. For example:

  ```sqlexample
  ALTER TABLE t1 SET DATA_METRIC_SCHEDULE = '';
  ```

  To resume the DMFs, set the DATA_METRIC_SCHEDULE parameter to a valid value.

## Call a DMF manually

Calling a DMF directly can be useful to test the output of the DMF before associating it with a table or view.

Use the following syntax to call a DMF:

```sqlsyntax
SELECT <data_metric_function>(<query>)
```

Where:

`data_metric_function`
:   Specifies a system- or user-defined DMF.

`query`
:   Specifies a SQL query on a table or view.

    The columns projected by the query must match the column arguments in the DMF signature.

> **Note:**
>
> The following system DMFs don’t follow this syntax because they don’t take any arguments:
>
> * [DATA_METRIC_SCHEDULED_TIME (system data metric function)](../sql-reference/functions/dmf_data_metric_schedule_time.md)
> * [ROW_COUNT (system data metric function)](../sql-reference/functions/dmf_row_count.md)

For example, to call a custom DMF `count_positive_numbers`, which accepts three columns as arguments, run the following command:

```sqlexample
SELECT governance.dmfs.count_positive_numbers(
  SELECT c1, c2, c3
  FROM t);
```

For example, to call the [NULL_COUNT (system data metric function)](../sql-reference/functions/dmf_null_count.md) system DMF to view the number of NULL values
in the `ssn` column, run the following command:

```sqlexample
SELECT SNOWFLAKE.CORE.NULL_COUNT(
  SELECT ssn
  FROM hr.tables.empl_info);
```

If a custom DMF accepts arguments from multiple tables, each query that projects a column must be enclosed in parentheses. For example, if
you want to manually call the REFERENTIAL_CHECK DMF, execute the following:

```sqlexample
SELECT referential_check( (SELECT id FROM salesorders), (SELECT id FROM salespeople) );
```
