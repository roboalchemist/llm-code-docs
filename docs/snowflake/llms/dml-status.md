# Source: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/dml-status.md

# Determining the number of rows affected by DML commands

After a [DML command](../../sql-reference/sql-dml.md) is executed (excluding the [TRUNCATE TABLE](../../sql-reference/sql/truncate-table.md)
command), Snowflake Scripting sets the following global variables. You can use these variables to determine if the last DML
statement affected any rows.

| Variable | Description |
| --- | --- |
| `SQLROWCOUNT` | Number of rows affected by the last DML statement.  This is equivalent to [`getNumRowsAffected()`](../stored-procedure/stored-procedures-api.md "getNumRowsAffected") in JavaScript stored procedures. |
| `SQLFOUND` | `true` if the last DML statement affected one or more rows. |
| `SQLNOTFOUND` | `true` if the last DML statement affected zero rows. |

> **Note:**
>
> The [2025_01 behavior change bundle](../../release-notes/bcr-bundles/2025_01_bundle.md) changes the behavior
> of these variables. When the bundle is enabled, the variables return NULL when a non-DML statement is executed
> after the last DML statement in a Snowflake Scripting block or stored procedure. The bundle is enabled by
> default. For more information about the behavior change, see [Snowflake Scripting: Changes to global variables](../../release-notes/bcr-bundles/2025_01/bcr-1850.md).
>
> If the bundle is disabled, you can [enable it in your account](../../release-notes/bcr-bundles/managing-behavior-change-releases.md) by
> executing the following statement:
>
> ```sqlexample
> SELECT SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2025_01');
> ```
>
> To disable the bundle, execute the following statement:
>
> ```sqlexample
> SELECT SYSTEM$DISABLE_BEHAVIOR_CHANGE_BUNDLE('2025_01');
> ```

The examples in this section use the following table:

```sqlexample
CREATE OR REPLACE TABLE my_values (value NUMBER);
```

The following example uses the `SQLROWCOUNT` variable to return the number of rows affected by the last
DML statement (the INSERT statement).

```sqlexample
BEGIN
  LET sql_row_count_var INT := 0;
  INSERT INTO my_values VALUES (1), (2), (3);
  sql_row_count_var := SQLROWCOUNT;
  SELECT * from my_values;
  RETURN sql_row_count_var;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET sql_row_count_var INT := 0;
  INSERT INTO my_values VALUES (1), (2), (3);
  sql_row_count_var := SQLROWCOUNT;
  SELECT * from my_values;
  RETURN sql_row_count_var;
END;
$$;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|               3 |
+-----------------+
```

The following example uses the `SQLFOUND` and `SQLNOTFOUND` variables to return the number of rows affected by the
last DML statement (the UPDATE statement).

```sqlexample
BEGIN
  LET sql_row_count_var INT := 0;
  LET sql_found_var BOOLEAN := NULL;
  LET sql_notfound_var BOOLEAN := NULL;
  IF ((SELECT MAX(value) FROM my_values) > 2) THEN
    UPDATE my_values SET value = 4 WHERE value < 3;
    sql_row_count_var := SQLROWCOUNT;
    sql_found_var := SQLFOUND;
    sql_notfound_var := SQLNOTFOUND;
  END IF;
  SELECT * from my_values;
  IF (sql_found_var = true) THEN
    RETURN 'Updated ' || sql_row_count_var || ' rows.';
  ELSEIF (sql_notfound_var = true) THEN
    RETURN 'No rows updated.';
  ELSE
    RETURN 'No DML statements executed.';
  END IF;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET sql_row_count_var INT := 0;
  LET sql_found_var BOOLEAN := NULL;
  LET sql_notfound_var BOOLEAN := NULL;
  IF ((SELECT MAX(value) FROM my_values) > 2) THEN
    UPDATE my_values SET value = 4 WHERE value < 3;
    sql_row_count_var := SQLROWCOUNT;
    sql_found_var := SQLFOUND;
    sql_notfound_var := SQLNOTFOUND;
  END IF;
  SELECT * from my_values;
  IF (sql_found_var = true) THEN
    RETURN 'Updated ' || sql_row_count_var || ' rows.';
  ELSEIF (sql_notfound_var = true) THEN
    RETURN 'No rows updated.';
  ELSE
    RETURN 'No DML statements executed.';
  END IF;
END;
$$;
```

When the anonymous block runs, the `SQLFOUND` variable is `true` because the UPDATE statement updates two rows.

```output
+-----------------+
| anonymous block |
|-----------------|
| Updated 2 rows. |
+-----------------+
```

Query the table to see the current values:

```sqlexample
SELECT * FROM my_values;
```

```output
+-------+
| VALUE |
|-------|
|     4 |
|     4 |
|     3 |
+-------+
```

Run the same anonymous block again, and the results are the following:

* The UPDATE statement is executed because there is a value in the table that is greater than `2`. That is,
  the IF condition is satisfied.
* The `SQLNOTFOUND` variable is `true` because no rows are updated. The UPDATE statement doesn’t update
  any rows because none of the values in the table are less than `3` (specified in the WHERE clause).

The query returns the following output:

```output
+------------------+
| anonymous block  |
|------------------|
| No rows updated. |
+------------------+
```

Now, update the table to set all of the values to `1`:

```sqlexample
UPDATE my_values SET value = 1;

SELECT * FROM my_values;
```

```output
+-------+
| VALUE |
|-------|
|     1 |
|     1 |
|     1 |
+-------+
```

Run the same anonymous block again, and the UPDATE statement isn’t executed because none of the values
in the table are greater than `2`. That is, the IF condition isn’t satisfied, so the UPDATE statement
doesn’t execute.

```output
+-----------------------------+
| anonymous block             |
|-----------------------------|
| No DML statements executed. |
+-----------------------------+
```
