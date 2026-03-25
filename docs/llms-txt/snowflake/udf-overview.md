# Source: https://docs.snowflake.com/en/developer-guide/udf/udf-overview.md

# User-defined functions overview

You can write user-defined functions (UDFs) to extend the system to perform operations that are not available through the
[built-in system-defined functions](../../sql-reference/intro-summary-operators-functions.md) provided by Snowflake. Once you create a UDF,
you can reuse it multiple times. A function always returns a value explicitly by specifying an expression, so it’s a good choice for
calculating and return a value.

You can use UDFs to extend built-in functions or to encapsulate calculations that are standard for your organization. UDFs you create
can be called in a way similar to built-in functions.

You write a UDF’s logic – its handler – in one of the supported languages. Once you have a handler,
you can [create a UDF](udf-creating-sql.md) using any of several tools included in Snowflake, then
[execute the UDF](udf-calling-sql.md).

A UDF is like a stored procedure, but the two differ in important ways. For more information, see
[Choosing whether to write a stored procedure or a user-defined function](../stored-procedures-vs-udfs.md).

A UDF is just one way to extend Snowflake. For others, see the following:

* [Stored procedures overview](../stored-procedure/stored-procedures-overview.md)
* [Writing external functions](../../sql-reference/external-functions.md)
* [Snowpark API](../snowpark/index.md)

## User-defined function variations

You can write a UDF in one of several variations, depending on the input and output requirements your function must meet.

| Variation | Description |
| --- | --- |
| User-defined function (UDF) | Also known as a *scalar function*, returns one output row for each input row. The returned row consists of a single column/value. |
| User-defined aggregate function (UDAF) | Operates on values across multiple rows to perform mathematical calculations such as sum, average, counting, finding minimum or maximum values, standard deviation, and estimation, as well as some non-mathematical operations. |
| User-defined table function (UDTF) | Returns a tabular value for each input row. |
| Vectorized user-defined function (UDF) | Receive batches of input rows as [Pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and return batches of results as [Pandas arrays](https://pandas.pydata.org/docs/reference/api/pandas.array.html) or [Series](https://pandas.pydata.org/docs/reference/series.html). |
| Vectorized user-defined table function (UDTF) | Receive batches of input rows as [Pandas DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) and return tabular results. |

## Supported languages and tools

You can [create](udf-creating-sql.md) and manage UDFs (and other Snowflake entities) by using any of multiple
tools, depending on how you prefer to work.

| Language | Approach | Support |
| --- | --- | --- |
| **SQL**  With handler in Java, JavaScript, Python, Scala, or SQL | Write SQL code in Snowflake to create and manage Snowflake entities. Write the function’s logic in one of the supported handler languages. | Java:  [UDF](java/udf-java-introduction.md), [UDTF](java/udf-java-tabular-functions.md)  JavaScript:  [UDF](javascript/udf-javascript-introduction.md), [UDTF](javascript/udf-javascript-tabular-functions.md)  Python:  [UDF](python/udf-python-introduction.md), [UDAF](python/udf-python-aggregate-functions.md), [UDTF](python/udf-python-tabular-functions.md), [Vectorized UDF](python/udf-python-batch.md), [Vectorized UDTF](python/udf-python-tabular-vectorized.md)  Scala:  [UDF](scala/udf-scala-introduction.md)  SQL:  [UDF](sql/udf-sql-introduction.md), [UDTF](sql/udf-sql-tabular-functions.md) |
| **Java, Python, or Scala**  [Snowpark API](../snowpark/index.md) | On the client, write code for operations that are pushed to Snowflake for processing. | Java:  [UDF](../snowpark/java/creating-udfs.md), [UDTF](../snowpark/java/creating-udfs.md)  Python:  [UDF](../snowpark/python/creating-udfs.md), [UDAF](../snowpark/python/creating-udafs.md), [UDTF](../snowpark/python/creating-udtfs.md), [Vectorized UDF or UDTF](../snowpark/python/creating-udfs.md)  Scala:  [UDF](../snowpark/scala/creating-udfs.md), [UDTF](../snowpark/scala/creating-udfs.md) |
| **Command-line Interface**  [Snowflake CLI](../snowflake-cli/index.md) | Use the command line to create and manage Snowflake entities, specifying properties as properties of JSON objects. | [Managing Snowflake objects](../snowflake-cli/objects/manage-objects.md) |
| **Python**  [Snowflake Python API](../snowflake-python-api/snowflake-python-overview.md) | On the client, Execute commands to create the function with Python, writing the function’s handler in one of the supported handler languages. | [Managing user-defined functions (UDFs)](../snowflake-python-api/snowflake-python-managing-functions-procedures.md) |
| **REST**  [Snowflake REST API](../snowflake-rest-api/snowflake-rest-api.md) | Make requests of RESTful endpoints to create and manage Snowflake entities. | [Manage user-defined functions](../snowflake-rest-api/user-defined-function/user-defined-function-introduction.md) |

When choosing a language, consider also the following:

* **Handler locations supported.** Not all languages support referring to the handler on a stage (the handler code must instead be in-line).
  For more information, see [Keeping handler code in-line or on a stage](../inline-or-staged.md).
* **Whether the handler results in a UDF that’s sharable.** A sharable UDF can be used with the Snowflake
  [Secure Data Sharing](../../user-guide/data-sharing-intro.md) feature.

| Language | Handler Location | Sharable |
| --- | --- | --- |
| Java | In-line or staged | No [1] |
| JavaScript | In-line | Yes |
| Python | In-line or staged | No [2] |
| Scala | In-line or staged | No [3] |
| SQL | In-line | Yes |

[1]

For more information about limits on sharing Java UDFs, see [General limitations](java/udf-java-limitations.md).

[2]

For more information about limits on sharing Python UDFs, see [General limitations](python/udf-python-limitations.md).

[3]

For more information about limits on sharing Scala UDFs, see [Scala UDF limitations](scala/udf-scala-limitations.md).

## Considerations

* If a query calls a UDF to access staged files, the operation fails with a user error if the SQL statement also queries a view that
  calls any UDF or UDTF, regardless of whether the function in the view accesses staged files or not.
* UDTFs can process multiple files in parallel; however, UDFs currently process files serially. As a workaround,
  group rows in a subquery using the [GROUP BY](../../sql-reference/constructs/group-by.md) clause. See [Process a CSV with a UDTF](../../user-guide/unstructured-data-java.md)
  for an example.
* Currently, if staged files referenced in a query are modified or deleted while the query is running, the function call fails with an
  error.
* If you specify the [CURRENT_DATABASE](../../sql-reference/functions/current_database.md) or [CURRENT_SCHEMA](../../sql-reference/functions/current_schema.md) function in the
  handler code of the UDF, the function returns the database or schema that contains the UDF, not the database or schema in use for
  the session.

## UDF example

Code in the following example creates a UDF called `addone` with a handler written in Python. The handler function is
`addone_py`. This UDF returns an `int`.

```sqlexample-python
CREATE OR REPLACE FUNCTION addone(i INT)
  RETURNS INT
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.12'
  HANDLER = 'addone_py'
AS $$
def addone_py(i):
 return i+1
$$;
```

Code in the following example executes the `addone` UDF.

```sqlexample
SELECT addone(3);
```

## Guidelines and constraints

Snowflake constraints:
:   You can ensure stability within the Snowflake environment by developing within Snowflake constraints. For
    more information, see [Designing Handlers that Stay Within Snowflake-Imposed Constraints](../udf-stored-procedure-constraints.md).

Naming:
:   Be sure to name functions in a way that avoids collisions with other functions. For more information, see
    [Naming and overloading procedures and UDFs](../udf-stored-procedure-naming-conventions.md).

Arguments:
:   Specify the arguments and indicate which arguments are optional. For more information, see
    [Defining arguments for UDFs and stored procedures](../udf-stored-procedure-arguments.md).

Data type mappings:
:   For each handler language, there’s a separate set of mappings between the language’s data types and the SQL types
    used for arguments and return values. For more about the mappings for each language, see [Data Type Mappings Between SQL and Handler Languages](../udf-stored-procedure-data-type-mapping.md).

## Handler writing

Handler languages:
:   For language-specific content on writing a handler, see Supported languages and tools.

External network access:
:   You can access external network locations with
    [external network access](../external-network-access/external-network-access-overview.md). You can create secure
    access to specific network locations external to Snowflake, then use that access from within the handler code.

Logging, tracing, and metrics:
:   You can record code activity by
    [capturing log messages, trace events, and metrics data](../logging-tracing/logging-tracing-overview.md),
    storing the data in a database you can query later.

## Security

You can grant privileges on objects needed for them to perform specific SQL actions with a UDF or UDTF. For more information, see
[Granting privileges for user-defined functions](udf-access-control.md)

Functions share certain security concerns with stored procedures. For more information, see the following:

* You can help a procedure’s handler code execute securely by following the best practices described in
  [Security Practices for UDFs and Procedures](../udf-stored-procedure-security-practices.md)
* Ensure that sensitive information is concealed from users who should not have access to it. For more information, see
  [Protecting Sensitive Information with Secure UDFs and Stored Procedures](../secure-udf-procedure.md)

## Handler code deployment

When creating a function, you can specify its handler – which implements the function’s logic – as code in-line with the function
definition or as code external to the definition, such as code packaged and copied to a stage.

For more information, see [Keeping handler code in-line or on a stage](../inline-or-staged.md).
