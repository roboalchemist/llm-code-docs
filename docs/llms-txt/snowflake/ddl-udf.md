# Source: https://docs.snowflake.com/en/sql-reference/ddl-udf.md

# DDL for user-defined functions, external functions, and stored procedures

UDFs (user-defined functions) and stored procedures are two programming constructs that allow you to extend Snowflake SQL.

## UDF management

UDFs can be used to perform operations that are not available via the system-defined functions provided by Snowflake. Snowflake provides the following DDL
commands for creating and managing UDFs:

* [CREATE FUNCTION](sql/create-function.md)
* [ALTER FUNCTION](sql/alter-function.md)
* [DROP FUNCTION](sql/drop-function.md)
* [DESCRIBE FUNCTION](sql/desc-function.md)
* [SHOW USER FUNCTIONS](sql/show-user-functions.md)

> **Note:**
>
> UDFs can contain Java, JavaScript, Python, and SQL; however, DDL and DML operations are not supported in UDFs.

## External function management

External functions can be used to perform operations that are not available via the system-defined functions provided
by Snowflake. External functions are a type of UDF, but their syntax is different enough that they have their own
CREATE, ALTER, and SHOW statements.

Snowflake provides the following DDL commands for creating and managing external functions:

* [CREATE EXTERNAL FUNCTION](sql/create-external-function.md)
* [ALTER FUNCTION](sql/alter-function.md)
* [DROP FUNCTION](sql/drop-function.md)
* [SHOW EXTERNAL FUNCTIONS](sql/show-external-functions.md)
* [DESCRIBE FUNCTION](sql/desc-function.md)

External functions use API integrations. Snowflake provides the following DDL commands for creating and managing
API integrations:

* [CREATE API INTEGRATION](sql/create-api-integration.md)
* [ALTER API INTEGRATION](sql/alter-api-integration.md)
* [DROP INTEGRATION](sql/drop-integration.md)
* [SHOW INTEGRATIONS](sql/show-integrations.md)
* [DESCRIBE INTEGRATION](sql/desc-integration.md)

## Stored procedure management

Snowflake provides the following DDL commands for creating and managing stored procedures:

* [CREATE PROCEDURE](sql/create-procedure.md)
* [ALTER PROCEDURE](sql/alter-procedure.md)
* [DROP PROCEDURE](sql/drop-procedure.md)
* [SHOW PROCEDURES](sql/show-procedures.md)
* [DESCRIBE PROCEDURE](sql/desc-procedure.md)

In addition, Snowflake provides the following command for using stored procedures:

* [CALL](sql/call.md)
