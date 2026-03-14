# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-function-spcs.md

# DROP FUNCTION (Snowpark Container Services)

Removes the specified [service function](../../developer-guide/snowpark-container-services/working-with-services.md).

See also:
:   [Service functions](../../developer-guide/snowpark-container-services/working-with-services.md), [CREATE FUNCTION](create-function-spcs.md), [ALTER FUNCTION](alter-function-spcs.md), [DESC FUNCTION](desc-function-spcs.md)

## Syntax

```sqlsyntax
DROP FUNCTION [ IF EXISTS ] <name> ( [ <arg_data_type> , ... ] )
```

## Parameters

`name`
:   Specifies the identifier for the service function to drop. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case sensitive.

`arg_data_type [ , ... ]`
:   Specifies the data type of the argument(s), if any, for the service function. The argument types are necessary because service functions support name
    overloading (that is, two service functions in the same schema can have the same name) and the argument types are used to identify the UDF you
    wish to drop.

## Usage notes

* Dropped functions can’t be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

This demonstrates the DROP FUNCTION command:

```sqlexample
DROP FUNCTION my_echo_udf(VARCHAR);
```

Example output:

```output
+-----------------------------------+
| status                            |
|-----------------------------------|
| MY_ECHO_UDF successfully dropped. |
+-----------------------------------+
```
