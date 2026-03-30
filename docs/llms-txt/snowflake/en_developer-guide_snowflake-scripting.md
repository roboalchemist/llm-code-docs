# Source: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/index.md

# Snowflake Scripting Developer Guide

Snowflake Scripting is an extension to Snowflake SQL that adds support for procedural logic. You can use Snowflake
Scripting syntax in [stored procedures](../stored-procedure/stored-procedures-overview.md) and
[user-defined functions (UDFs)](../udf/sql/udf-sql-procedural-functions.md). You can also use Snowflake
Scripting syntax outside of stored procedures and UDFs and stored procedures. The next topics explain how to use
Snowflake Scripting.

[Understanding blocks in Snowflake Scripting](blocks.md)
:   Learn the basic structure of Snowflake Scripting code.

[Working with variables](variables.md)
:   Declare and use variables.

[Returning a value](return.md)
:   Return values from stored procedures and an anonymous block.

[Working with conditional logic](branch.md)
:   Control flow with IF and CASE statements.

[Working with loops](loops.md)
:   Control flow with FOR, WHILE, REPEAT, and LOOP.

[Working with cursors](cursors.md)
:   Iterate through query results with a cursor.

[Working with RESULTSETs](resultsets.md)
:   Iterate over the result set returned by a query.

[Handling exceptions](exceptions.md)
:   Handle errors by handling and raising exceptions.

[Determining the number of rows affected by DML commands](dml-status.md)
:   Use global variables to determine the effect of data manipulation language (DML) commands.

[Getting the query ID of the last query](query-id.md)
:   Use the global variable SQLID to get the query ID of the last query.

[Examples for common use cases of Snowflake Scripting](use-cases.md)
:   Explore examples of Snowflake Scripting code for some common use cases.

[Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)
:   Run the Snowflake Scripting examples in SnowSQL, Snowsight and Python Connector code.
