# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/stored-procedures-overview.md

# Stored procedures overview

You can write stored procedures to extend the system with procedural code. With a procedure, you can use branching, looping, and other
programmatic constructs. You can reuse a procedure multiple times by calling it from other code.

With a stored procedure, you can:

* Automate tasks that require multiple database operations performed frequently.
* Dynamically create and execute database operations.
* Execute code with the privileges of the role that owns the procedure, rather than with the privileges of the role that runs the procedure.

  This allows the stored procedure owner to delegate the power to perform specified operations to users who otherwise could not do so.
  However, there are limitations on these owner’s rights stored procedures.

For example, imagine that you want to clean up a database by deleting data older than a specified date. You can execute the delete operation
multiple times in your code, each time deleting data from a specific table. You can put all of those statements in a single stored
procedure, then pass a parameter that specifies the cut-off date.

With the procedure deployed, you can call it to clean up the database. As your database changes, you can update the procedure to clean
up additional tables; if there are multiple users who use the new cleanup command, they can call one procedure, rather than remember
every table name and clean up each table individually.

A stored procedure is like a UDF, but the two differ in important ways. For more information, see
[Choosing whether to write a stored procedure or a user-defined function](../stored-procedures-vs-udfs.md).

A procedure is just one way to extend Snowflake. For others, see the following:

* [User-defined functions overview](../udf/udf-overview.md)
* [Writing external functions](../../sql-reference/external-functions.md)
* [Snowpark API](../snowpark/index.md)

## Supported languages and tools

You can create and manage stored procedures (and other Snowflake entities) by using any of multiple tools, depending on how you prefer to work.

| Language | Approach | Support |
| --- | --- | --- |
| **SQL**  With handler in Java, JavaScript, Python, Scala, or SQL Scripting | Write SQL code in Snowflake to create and manage Snowflake entities. Write the procedure’s logic in one of the supported handler languages. | [Java](java/procedure-java-overview.md)  [JavaScript](stored-procedures-javascript.md)  [Python](python/procedure-python-overview.md)  [Scala](scala/procedure-scala-overview.md)  [SQL Scripting](stored-procedures-snowflake-scripting.md) |
| **Java, Python, or Scala**  [Snowpark API](../snowpark/index.md) | On the client, write code for operations that are pushed to Snowflake for processing. | [Java](../snowpark/java/creating-sprocs.md)  [Python](../snowpark/python/creating-sprocs.md)  [Scala](../snowpark/scala/creating-sprocs.md) |
| **Command-line interface**  [Snowflake CLI](../snowflake-cli/index.md) | Use the command line to create and manage Snowflake entities, specifying properties as properties of JSON objects. | [Managing Snowflake objects](../snowflake-cli/objects/manage-objects.md) |
| **Python**  [Snowflake Python API](../snowflake-python-api/snowflake-python-overview.md) | On the client, write code that executes management operations on Snowflake. | [Managing stored procedures](../snowflake-python-api/snowflake-python-managing-functions-procedures.md) |
| **REST**  [Snowflake REST API](../snowflake-rest-api/snowflake-rest-api.md) | Make requests of RESTful endpoints to create and manage Snowflake entities. | [Manage procedures](../snowflake-rest-api/procedure/procedure-introduction.md) |

You write a procedure’s logic — its handler — in one of the supported languages. Once
you have a handler, you can [create a procedure](stored-procedures-creating.md) with a CREATE PROCEDURE command, then
[call the procedure](stored-procedures-calling.md) with a CALL statement.

From a stored procedure, you can return a single value or (where supported with the handler language) tabular data. For more information
about supported return types, see [CREATE PROCEDURE](../../sql-reference/sql/create-procedure.md).

When choosing a language, consider also the handler locations supported. Not all languages support referring to the handler on a stage
(the handler code must instead be in-line). For more information, see [Keeping handler code in-line or on a stage](../inline-or-staged.md).

| Language | Handler Location |
| --- | --- |
| Java | In-line or staged |
| JavaScript | In-line |
| Python | In-line or staged |
| Scala | In-line or staged |
| Snowflake Scripting | In-line |

## Temporary procedures

You can create a procedure that is discarded after you use it. You might find this useful when you don’t
need the procedure to be available in a durable way, such as for multiple sessions or to multiple users.

In addition, creating a procedure in one of the following ways doesn’t require the CREATE PROCEDURE privilege, so these approaches are more broadly available to users:

* Create a temporary stored procedure that persists for only the current session, then is dropped.

  The following Snowflake tools support creating a temporary procedure:

  * [CREATE PROCEDURE](../../sql-reference/sql/create-procedure.md) with the TEMP or TEMPORARY parameter
  * The Snowpark API for [Java](../snowpark/java/creating-sprocs.md), [Python](../snowpark/python/creating-sprocs.md),
    or [Scala](../snowpark/scala/creating-sprocs.md)
* Create an anonymous procedure that you call immediately, and which is dropped immediately.

  * To create a procedure and immediately call it in a single SQL statement, use the [CALL (with anonymous procedure)](../../sql-reference/sql/call-with.md) syntax.

## Stored procedure example

Code in the following example creates a stored procedure called `myproc` with a Python handler called `run`.

```sqlexample-python
CREATE OR REPLACE PROCEDURE myproc(from_table STRING, to_table STRING, count INT)
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.12'
  PACKAGES = ('snowflake-snowpark-python')
  HANDLER = 'run'
as
$$
def run(session, from_table, to_table, count):
  session.table(from_table).limit(count).write.save_as_table(to_table)
  return "SUCCESS"
$$;
```

Code in the following example calls the stored procedure `myproc`.

```sqlexample
CALL myproc('table_a', 'table_b', 5);
```

## Guidelines and constraints

Tips:
:   For tips on writing stored procedures, see [Working with stored procedures](stored-procedures-usage.md).

Snowflake constraints:
:   You can ensure stability within the Snowflake environment by developing within Snowflake constraints. For more information, see
    [Designing Handlers that Stay Within Snowflake-Imposed Constraints](../udf-stored-procedure-constraints.md).

Naming:
:   Be sure to name procedures in a way that avoids collisions with other procedures. For more information, see
    [Naming and overloading procedures and UDFs](../udf-stored-procedure-naming-conventions.md).

Arguments:
:   Specify the arguments for your stored procedure and indicate which arguments are optional. For more information, see
    [Defining arguments for UDFs and stored procedures](../udf-stored-procedure-arguments.md).

Data type mappings:
:   For each handler language, there’s a separate set of mappings between the language’s data types and the SQL types used for arguments and
    return values. For more about the mappings for each language, see [Data Type Mappings Between SQL and Handler Languages](../udf-stored-procedure-data-type-mapping.md).

## Handler writing

Handler languages:
:   For language-specific content on writing a handler, see Supported languages and tools.

External network access:
:   You can access external network locations with
    [external network access](../external-network-access/external-network-access-overview.md). You can create secure
    access to specific network locations external to Snowflake, then use that access from within the handler code.

Logging and tracing:
:   You can record code activity by [capturing log messages and trace events](../logging-tracing/logging-tracing-overview.md),
    storing the data in a database you can query later.

## Security

Whether you choose to have a stored procedure run with caller’s rights or owner’s rights can impact the information it has access to and
the tasks it may be allowed to perform. For more information, see [Understanding caller’s rights and owner’s rights stored procedures](stored-procedures-rights.md).

Stored procedures share certain security concerns with user-defined functions (UDFs). For more information, see the following:

* You can help a procedure’s handler code execute securely by following the best practices described in
  [Security Practices for UDFs and Procedures](../udf-stored-procedure-security-practices.md)
* Ensure that sensitive information is concealed from users who should not have access to it. For more information, see
  [Protecting Sensitive Information with Secure UDFs and Stored Procedures](../secure-udf-procedure.md)

## Handler code deployment

When creating a procedure, you can specify its handler – which implements the procedure’s logic – as code in-line with the CREATE
PROCEDURE statement or as code external to the statement, such as compiled code packaged and copied to a stage.

For more information, see [Keeping handler code in-line or on a stage](../inline-or-staged.md).
