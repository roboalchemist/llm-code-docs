# Source: https://docs.snowflake.com/en/user-guide/querying-construct-at-runtime.md

# Constructing SQL at runtime

Snowflake supports several different techniques for constructing strings of SQL statements dynamically at runtime.
By using these techniques, you can specify more general and flexible SQL strings for use cases where the full text
of the SQL statements are unknown until runtime.

A stored procedure or application can accept user input and then use that input in a SQL statement. For example,
a table might store information about sales orders. An application or stored procedure might accept an order ID as
input and run a query that only returns the results for that specific order.

A developer can write stored procedure code or application code with SQL statements that contain placeholders, and
then bind variables to those placeholders in the code. These placeholders are called
[bind variables](../sql-reference/bind-variables.md). A developer can also write code that constructs SQL
statements from an input string (for example, by concatenating strings that contain a SQL command, parameters,
and values).

The following techniques are available for constructing SQL statements dynamically at runtime:

* The TO_QUERY function - This function takes
  a SQL string with optional parameters as input.
* Dynamic SQL - Code in a stored procedure or
  application takes input and constructs a dynamic SQL statement using this input. The code can be part of a
  [Snowflake Scripting](../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md) or
  [Javascript](../developer-guide/stored-procedure/stored-procedures-javascript.md)
  stored procedure, or a Snowflake Scripting anonymous block. You can also use this technique in your
  application code that uses a [Snowflake driver](../developer-guide/drivers.md) or the
  [Snowflake SQL API](../developer-guide/sql-api/index.md).

> **Note:**
>
> When programs construct SQL statements with user input, there are potential security risks, such as
> SQL injection. If inputs to SQL statements come from external sources, make sure they are validated.
> For more information, see [SQL injection](../developer-guide/stored-procedure/stored-procedures-usage.md).

## Use the TO_QUERY function

You can use the [TO_QUERY](../sql-reference/functions/to_query.md) function in the code for stored procedures and applications
that construct SQL statements dynamically. This table function takes a SQL string as input. Optionally, the
SQL string can contain parameters, and you can specify the arguments to pass to the parameters as
bind variables.

The following is a simple example that calls the function:

```sqlexample
SELECT COUNT(*) FROM TABLE(TO_QUERY('SELECT 1'));
```

```output
+----------+
| COUNT(*) |
|----------|
|        1 |
+----------+
```

The following example uses the TO_QUERY function in a stored procedure:

```sqlexample
CREATE OR REPLACE PROCEDURE get_num_results_tq(query VARCHAR)
RETURNS TABLE ()
LANGUAGE SQL
AS
DECLARE
  res RESULTSET DEFAULT (SELECT COUNT(*) FROM TABLE(TO_QUERY(:query)));
BEGIN
  RETURN TABLE(res);
END;
```

Note: If you use [Snowflake CLI](../developer-guide/snowflake-cli/index.md), [SnowSQL](snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE get_num_results_tq(query VARCHAR)
RETURNS TABLE ()
LANGUAGE SQL
AS
$$
DECLARE
  res RESULTSET DEFAULT (SELECT COUNT(*) FROM TABLE(TO_QUERY(:query)));
BEGIN
  RETURN TABLE(res);
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL get_num_results_tq('SELECT 1');
```

```output
+----------+
| COUNT(*) |
|----------|
|        1 |
+----------+
```

## Use dynamic SQL in stored procedures and applications

To construct SQL statements that take user input, you can use dynamic SQL in a
[Snowflake Scripting](../developer-guide/stored-procedure/stored-procedures-snowflake-scripting.md)
or [Javascript](../developer-guide/stored-procedure/stored-procedures-javascript.md) stored procedure, or in a Snowflake
Scripting anonymous block . You can also use dynamic SQL in your application code that uses a
[Snowflake driver](../developer-guide/drivers.md) or the [Snowflake SQL API](../developer-guide/sql-api/index.md).

This example creates a stored procedure with Snowflake Scripting. The stored procedure takes SQL text as input and constructs
a string containing a SQL statement by appending the text to it. The dynamic SQL is then executed using the
[EXECUTE IMMEDIATE](../sql-reference/sql/execute-immediate.md) command.

```sqlexample
CREATE OR REPLACE PROCEDURE get_num_results(query VARCHAR)
RETURNS INTEGER
LANGUAGE SQL
AS
DECLARE
  row_count INTEGER DEFAULT 0;
  stmt VARCHAR DEFAULT 'SELECT COUNT(*) FROM (' || query || ')';
  res RESULTSET DEFAULT (EXECUTE IMMEDIATE :stmt);
  cur CURSOR FOR res;
BEGIN
  OPEN cur;
  FETCH cur INTO row_count;
  RETURN row_count;
END;
```

Note: If you use [Snowflake CLI](../developer-guide/snowflake-cli/index.md), [SnowSQL](snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
CREATE OR REPLACE PROCEDURE get_num_results(query VARCHAR)
RETURNS INTEGER
LANGUAGE SQL
AS
$$
DECLARE
  row_count INTEGER DEFAULT 0;
  stmt VARCHAR DEFAULT 'SELECT COUNT(*) FROM (' || query || ')';
  res RESULTSET DEFAULT (EXECUTE IMMEDIATE :stmt);
  cur CURSOR FOR res;
BEGIN
  OPEN cur;
  FETCH cur INTO row_count;
  RETURN row_count;
END;
$$
;
```

The following example calls the procedure:

```sqlexample
CALL get_num_results('SELECT 1');
```

```output
+-----------------+
| GET_NUM_RESULTS |
|-----------------|
|               1 |
+-----------------+
```

Dynamic SQL supports bind variables. The following Snowflake Scripting example uses bind variables represented
by the `?` placeholders to construct SQL statements dynamically at runtime. This block selects data from the
following `invoices` table:

```sqlexample
CREATE OR REPLACE TABLE invoices (price NUMBER(12, 2));
INSERT INTO invoices (price) VALUES
  (11.11),
  (22.22);
```

Execute the anonymous block:

```sqlexample
DECLARE
  rs RESULTSET;
  query VARCHAR DEFAULT 'SELECT * FROM invoices WHERE price > ? AND price < ?';
  minimum_price NUMBER(12,2) DEFAULT 20.00;
  maximum_price NUMBER(12,2) DEFAULT 30.00;
BEGIN
  rs := (EXECUTE IMMEDIATE :query USING (minimum_price, maximum_price));
  RETURN TABLE(rs);
END;
```

Note: If you use [Snowflake CLI](../developer-guide/snowflake-cli/index.md), [SnowSQL](snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../developer-guide/python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](../developer-guide/snowflake-scripting/running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  rs RESULTSET;
  query VARCHAR DEFAULT 'SELECT * FROM invoices WHERE price > ? AND price < ?';
  minimum_price NUMBER(12,2) DEFAULT 20.00;
  maximum_price NUMBER(12,2) DEFAULT 30.00;
BEGIN
  rs := (EXECUTE IMMEDIATE :query USING (minimum_price, maximum_price));
  RETURN TABLE(rs);
END;
$$
;
```

```output
+-------+
| PRICE |
|-------|
| 22.22 |
+-------+
```

## Comparison of the techniques for constructing SQL dynamically

The following table describes the advantages and disadvantages of the techniques for constructing
SQL dynamically.

| Technique | Advantages | Disadvantages |
| --- | --- | --- |
| TO_QUERY function | *Simple syntax* Built-in error handling *Specific semantics for the use case of constructing SQL dynamically* Automatically determined result set | *Queries cannot be described or explained before execution* Only valid in the FROM clause of a SELECT statement * Snowflake specific |
| Dynamic SQL | *More general and flexible than the TO_QUERY function* Queries can be described or explained before execution | *More complex than the TO_QUERY function* Manual error handling |
