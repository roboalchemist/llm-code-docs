# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/python/procedure-python-writing.md

# Writing the Python handler for a stored procedure

You can write Python code as the handler that executes when a stored procedure is called. This section describes the design of a
handler.

You can create a stored procedure from the handler code in several ways:

* Include the code in-line with the SQL statement that creates the procedure. Refer to [Keeping handler code in-line or on a stage](../../inline-or-staged.md).
* Copy the code to a stage and reference it there when you create the procedure. Refer to [Keeping handler code in-line or on a stage](../../inline-or-staged.md).
* Write the code in a Python worksheet and deploy the worksheet contents to a stored procedure. Refer to
  [Creating a stored procedure from a Python worksheet](procedure-python-create-worksheet.md).

## Planning to write your stored procedure

Stored procedures run inside Snowflake, and so you must plan the code that you write with that in mind.

* Limit the amount of memory consumed. Snowflake places limits on a method in terms of the amount of memory needed.
  For guidance, refer to [Designing Handlers that Stay Within Snowflake-Imposed Constraints](../../udf-stored-procedure-constraints.md).
* Make sure that your handler method or function is thread safe.
* Follow the rules and security restrictions. Refer to [Security Practices for UDFs and Procedures](../../udf-stored-procedure-security-practices.md).
* Decide whether you want the stored procedure to run with [caller’s rights or owner’s rights](../stored-procedures-rights.md).
* Consider the snowflake-snowpark-python version used to run stored procedures. Due to limitations in the stored procedures release process,
  the snowflake-snowpark-python library available in the Python stored procedure environment is usually one version behind the publicly
  released version. Use the following SQL to find out the latest available version:

  ```sqlexample
  SELECT * FROM information_schema.packages WHERE package_name = 'snowflake-snowpark-python' ORDER BY version DESC;
  ```

## Writing the method or function

When writing the method or function for the stored procedure, note the following:

* Specify the Snowpark `Session` object as the first argument of your method or function.
  When you call your stored procedure, Snowflake automatically creates a `Session` object and passes it to your stored procedure.
  (You cannot create the `Session` object yourself.)
* For the rest of the arguments and for the return value, use the Python types that correspond to
  [Snowflake data types](../../../sql-reference-data-types.md). Snowflake supports the Python data types listed in
  [SQL-Python Data Type Mappings for Parameters and Return Types](../../udf-stored-procedure-data-type-mapping.md).
* When you run an asynchronous child job from within a procedure’s handler — such as by using
  [DataFrame.collect_nowait](https://docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/api/snowflake.snowpark.DataFrame.collect_nowait)
  — “fire and forget” is not supported.

  In other words, if the handler issues a child query that is still running when the parent procedure job completes, the child job is
  canceled automatically.

## Handling errors

You can use the normal Python exception-handling techniques to catch errors within the procedure.

If an uncaught exception occurs inside the method, Snowflake raises an error that includes the stack trace for the exception. When
[logging of unhandled exceptions](../../logging-tracing/unhandled-exception-messages.md) is enabled, Snowflake logs data
about unhandled exceptions in an event table.

## Making dependencies available to your code

If your handler code depends on code defined outside the handler itself (such as code defined in a module) or on resource files, you can
make those dependencies available to your code by uploading them to a stage.
Refer to [Making dependencies available to your code](../../upload-dependencies.md), or for Python worksheets, refer to [Add a Python File from a Stage to a Worksheet](../../snowpark/python/python-worksheets.md).

If you create your stored procedure using SQL, use the IMPORTS clause when writing the
[CREATE PROCEDURE statement](../../../sql-reference/sql/create-procedure.md), to point to the dependency files.
