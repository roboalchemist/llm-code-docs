# Source: https://docs.snowflake.com/en/developer-guide/udf/sql/udf-sql-procedural-functions.md

# Snowflake Scripting UDFs

Snowflake supports SQL user-defined functions (UDFs) that contain Snowflake Scripting procedural language.
These UDFs are called *Snowflake Scripting UDFs*.

Snowflake Scripting UDFs can be called in a SQL statement, such as a SELECT statement or INSERT statement.
Therefore, they are more flexible than a Snowflake Scripting stored procedure, which can only be called in
a SQL [CALL](../../../sql-reference/sql/call.md) command.

## General usage

A Snowflake Scripting UDF evaluates procedural code and returns a scalar (that is, single) value.

You can use the following subset of [Snowflake Scripting](../../snowflake-scripting/index.md)
syntax in Snowflake Scripting UDFs:

* [Blocks](../../snowflake-scripting/blocks.md)
* [Variables](../../snowflake-scripting/variables.md)
* [RETURN command](../../snowflake-scripting/return.md)
* [Conditional logic](../../snowflake-scripting/branch.md)
* [Loops](../../snowflake-scripting/loops.md)
* [Exceptions](../../snowflake-scripting/exceptions.md)

## Supported data types

Snowflake Scripting UDFs support the following data types for both input arguments and
return values:

* [Numeric data types](../../../sql-reference/data-types-numeric.md) (for example, INTEGER, NUMBER, and FLOAT)
* [String & binary data types](../../../sql-reference/data-types-text.md) (for example, VARCHAR and BINARY)
* [Date & time data types](../../../sql-reference/data-types-datetime.md) (for example, DATE, TIME, and TIMESTAMP)
* [Logical data types](../../../sql-reference/data-types-logical.md) (for example, BOOLEAN)

Snowflake Scripting UDFs support the following data types for input arguments only:

* [Semi-structured data types](../../../sql-reference/data-types-semistructured.md) (for example, VARIANT, OBJECT, and ARRAY)
* [Structured data types](../../../sql-reference/data-types-structured.md) (for example, ARRAY, OBJECT, and MAP)

## Limitations

The following limitations apply to Snowflake Scripting UDFs:

* The following types of Snowflake Scripting syntax aren’t supported in Snowflake Scripting UDFs:

  * [Cursors](../../snowflake-scripting/cursors.md)
  * [RESULTSETs](../../snowflake-scripting/resultsets.md)
  * [Asynchronous child jobs](../../snowflake-scripting/asynchronous-child-jobs.md)
* SQL statements aren’t supported in Snowflake Scripting UDFs (including SELECT, INSERT, UPDATE, and so on).
* Snowflake Scripting UDFs can’t be defined as table functions.
* The following expression types aren’t supported in Snowflake Scripting UDFs:

  * User-defined functions
  * Aggregation functions
  * Window functions
* Snowflake Scripting UDFs can’t be used when creating a materialized view.
* Snowflake Scripting UDFs can’t be used when creating row access policies and masking policies.
* Snowflake Scripting UDFs can’t be used to specify a default column value.
* Snowflake Scripting UDFs can’t be used in a COPY INTO command for data loading and unloading.
* Snowflake Scripting UDFs can’t be memoizable.
* Snowflake Scripting UDFs have a limit of 500 input arguments.
* You can’t [log messages](../../logging-tracing/logging.md) for Snowflake Scripting UDFs.

## Examples

The following examples create and call Snowflake Scripting UDFs:

* Create a Snowflake Scripting UDF with variables
* Create a Snowflake Scripting UDF with conditional logic
* Create a Snowflake Scripting UDF with a loop
* Create a Snowflake Scripting UDF with exception handling
* Create a Snowflake Scripting UDF that returns a value for an INSERT statement
* Create a Snowflake Scripting UDF called in WHERE and ORDER BY clauses

### Create a Snowflake Scripting UDF with variables

Create a Snowflake Scripting UDF that calculates profit based on the values of two arguments:

```sqlexample
CREATE OR REPLACE FUNCTION calculate_profit(
  cost NUMBER(38, 2),
  revenue NUMBER(38, 2))
RETURNS number(38, 2)
LANGUAGE SQL
AS
DECLARE
  profit NUMBER(38, 2) DEFAULT 0.0;
BEGIN
  profit := revenue - cost;
  RETURN profit;
END;
```

> **Note:**
>
> If you use [Snowflake CLI](../../snowflake-cli/index.md), [SnowSQL](../../../user-guide/snowsql.md),
> the Classic Console, or the `execute_stream` or `execute_string` method in
> [Python Connector](../../python-connector/python-connector.md) code, this example requires minor
> changes. For more information, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../snowflake-scripting/running-examples.md).

Call `calculate_profit` in a query:

```sqlexample
SELECT calculate_profit(100, 110);
```

```output
+----------------------------+
| CALCULATE_PROFIT(100, 110) |
|----------------------------|
|                      10.00 |
+----------------------------+
```

You can use the same Snowflake Scripting UDF and specify columns for the arguments. First,
create a table and insert data:

```sqlexample
CREATE OR REPLACE TABLE snowflake_scripting_udf_profit(
  cost NUMBER(38, 2),
  revenue NUMBER(38, 2));

INSERT INTO snowflake_scripting_udf_profit VALUES
  (100, 200),
  (200, 190),
  (300, 500),
  (400, 401);
```

Call `calculate_profit` in a query and specify the columns for the arguments:

```sqlexample
SELECT calculate_profit(cost, revenue)
  FROM snowflake_scripting_udf_profit;
```

```output
+---------------------------------+
| CALCULATE_PROFIT(COST, REVENUE) |
|---------------------------------|
|                          100.00 |
|                          -10.00 |
|                          200.00 |
|                            1.00 |
+---------------------------------+
```

### Create a Snowflake Scripting UDF with conditional logic

Create a Snowflake Scripting UDF that uses conditional logic to determine the department name
based on an input INTEGER value:

```sqlexample
CREATE OR REPLACE function check_dept(department_id INTEGER)
RETURNS VARCHAR
LANGUAGE SQL
AS
BEGIN
  IF (department_id < 3) THEN
    RETURN 'Engineering';
  ELSEIF (department_id = 3) THEN
    RETURN 'Tool Design';
  ELSE
    RETURN 'Marketing';
  END IF;
END;
```

> **Note:**
>
> If you use [Snowflake CLI](../../snowflake-cli/index.md), [SnowSQL](../../../user-guide/snowsql.md),
> the Classic Console, or the `execute_stream` or `execute_string` method in
> [Python Connector](../../python-connector/python-connector.md) code, this example requires minor
> changes. For more information, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../snowflake-scripting/running-examples.md).

Call `check_dept` in a query:

```sqlexample
SELECT check_dept(2);
```

```output
+---------------+
| CHECK_DEPT(2) |
|---------------|
| Engineering   |
+---------------+
```

You can use a [SQL variable](../../../sql-reference/session-variables.md) in an argument when you
call a Snowflake Scripting UDF. The following example sets a SQL variable and then uses the
variable in a call to the `check_dept` UDF:

```sqlexample
SET my_variable = 3;

SELECT check_dept($my_variable);
```

```output
+--------------------------+
| CHECK_DEPT($MY_VARIABLE) |
|--------------------------|
| Tool Design              |
+--------------------------+
```

### Create a Snowflake Scripting UDF with a loop

Create a Snowflake Scripting UDF that uses a loop to count all numbers up to a target number provided
in an argument and calculate the sum of all of the numbers counted:

```sqlexample
CREATE OR REPLACE function count_to(
  target_number INTEGER)
RETURNS VARCHAR
LANGUAGE SQL
AS
DECLARE
  counter INTEGER DEFAULT 0;
  sum_total INTEGER DEFAULT 0;
BEGIN
  WHILE (counter < target_number) DO
    counter := counter + 1;
    sum_total := sum_total + counter;
  END WHILE;
  RETURN 'Counted to ' || counter || '. Sum of all numbers: ' || sum_total;
END;
```

> **Note:**
>
> If you use [Snowflake CLI](../../snowflake-cli/index.md), [SnowSQL](../../../user-guide/snowsql.md),
> the Classic Console, or the `execute_stream` or `execute_string` method in
> [Python Connector](../../python-connector/python-connector.md) code, this example requires minor
> changes. For more information, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../snowflake-scripting/running-examples.md).

Call `count_to` in a query:

```sqlexample
SELECT count_to(10);
```

```output
+---------------------------------------+
| COUNT_TO(10)                          |
|---------------------------------------|
| Counted to 10. Sum of all numbers: 55 |
+---------------------------------------+
```

### Create a Snowflake Scripting UDF with exception handling

Create a Snowflake Scripting UDF that declares an exception and then raises the exception:

```sqlexample
CREATE OR REPLACE FUNCTION raise_exception(input_value INTEGER)
RETURNS VARCHAR
LANGUAGE SQL
AS
DECLARE
  counter_val INTEGER DEFAULT 0;
  my_exception EXCEPTION (-20002, 'My exception text');
BEGIN
  WHILE (counter_val < 12) DO
    counter_val := counter_val + 1;
    IF (counter_val > 10) THEN
      RAISE my_exception;
    END IF;
  END WHILE;
  RETURN counter_val;
EXCEPTION
  WHEN my_exception THEN
    IF (input_value = 1) THEN
      RETURN 'My exception caught: ' || sqlcode;
    ELSEIF (input_value = 2) THEN
      RETURN 'My exception caught with different path: ' || sqlcode;
    END IF;
    RETURN 'Default exception handling path: ' || sqlcode;
END;
```

> **Note:**
>
> If you use [Snowflake CLI](../../snowflake-cli/index.md), [SnowSQL](../../../user-guide/snowsql.md),
> the Classic Console, or the `execute_stream` or `execute_string` method in
> [Python Connector](../../python-connector/python-connector.md) code, this example requires minor
> changes. For more information, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../snowflake-scripting/running-examples.md).

Call `raise_exception` in a query and specify `1` for the input value:

```sqlexample
SELECT raise_exception(1);
```

```output
+-----------------------------+
| RAISE_EXCEPTION(1)          |
|-----------------------------|
| My exception caught: -20002 |
+-----------------------------+
```

Call `raise_exception` in a query and specify `2` for the input value:

```sqlexample
SELECT raise_exception(2);
```

```output
+-------------------------------------------------+
| RAISE_EXCEPTION(2)                              |
|-------------------------------------------------|
| My exception caught with different path: -20002 |
+-------------------------------------------------+t
```

Call `raise_exception` in a query and specify `NULL` for the input value:

```sqlexample
SELECT raise_exception(NULL);
```

```output
+-----------------------------------------+
| RAISE_EXCEPTION(NULL)                   |
|-----------------------------------------|
| Default exception handling path: -20002 |
+-----------------------------------------+
```

### Create a Snowflake Scripting UDF that returns a value for an INSERT statement

Create a Snowflake Scripting UDF that returns a value that is used in an INSERT statement. Create the table
that the values will be inserted into:

```sqlexample
CREATE OR REPLACE TABLE test_sql_udf_insert (num NUMBER);
```

Create a SQL UDF that returns a numeric value:

```sqlexample
CREATE OR REPLACE FUNCTION value_to_insert(l NUMBER, r NUMBER)
RETURNS number
LANGUAGE SQL
AS
BEGIN
  IF (r < 0) THEN
    RETURN l/r * -1;
  ELSEIF (r > 0) THEN
    RETURN l/r;
  ELSE
    RETURN 0;
END IF;
END;
```

> **Note:**
>
> If you use [Snowflake CLI](../../snowflake-cli/index.md), [SnowSQL](../../../user-guide/snowsql.md),
> the Classic Console, or the `execute_stream` or `execute_string` method in
> [Python Connector](../../python-connector/python-connector.md) code, this example requires minor
> changes. For more information, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../snowflake-scripting/running-examples.md).

Call `value_to_insert` in multiple INSERT statements:

```sqlexample
INSERT INTO test_sql_udf_insert SELECT value_to_insert(10, 2);
INSERT INTO test_sql_udf_insert SELECT value_to_insert(10, -2);
INSERT INTO test_sql_udf_insert SELECT value_to_insert(10, 0);
```

Query the table to view the inserted values:

```sqlexample
SELECT * FROM test_sql_udf_insert;
```

```output
+-----+
| NUM |
|-----|
|   5 |
|   5 |
|   0 |
+-----+
```

### Create a Snowflake Scripting UDF called in WHERE and ORDER BY clauses

Create a Snowflake Scripting UDF that returns a value that is used in a WHERE or ORDER BY clause.
Create a table and insert values:

```sqlexample
CREATE OR REPLACE TABLE test_sql_udf_clauses (p1 INT, p2 INT);

INSERT INTO test_sql_udf_clauses VALUES
  (100, 7),
  (100, 3),
  (100, 4),
  (NULL, NULL);
```

Create a SQL UDF that returns a numeric value that is the product of the multiplication
of two input values:

```sqlexample
CREATE OR REPLACE FUNCTION get_product(a INTEGER, b INTEGER)
RETURNS VARCHAR
LANGUAGE SQL
AS
BEGIN
  RETURN a * b;
END;
```

> **Note:**
>
> If you use [Snowflake CLI](../../snowflake-cli/index.md), [SnowSQL](../../../user-guide/snowsql.md),
> the Classic Console, or the `execute_stream` or `execute_string` method in
> [Python Connector](../../python-connector/python-connector.md) code, this example requires minor
> changes. For more information, see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../../snowflake-scripting/running-examples.md).

Call `get_product` in the WHERE clause of a query to return the rows
where the product is greater than `350`:

```sqlexample
SELECT *
  FROM test_sql_udf_clauses
  WHERE get_product(p1, p2) > 350;
```

```output
+-----+----+
|  P1 | P2 |
|-----+----|
| 100 |  7 |
| 100 |  4 |
+-----+----+
```

Call `get_product` in the ORDER BY clause of a query to order
the results from the lowest to the highest product returned by
the UDF:

```sqlexample
SELECT *
  FROM test_sql_udf_clauses
  ORDER BY get_product(p1, p2);
```

```output
+------+------+
|  P1  | P2   |
|------+------|
| 100  | 3    |
| 100  | 4    |
| 100  | 7    |
| NULL | NULL |
+------+------+
```
