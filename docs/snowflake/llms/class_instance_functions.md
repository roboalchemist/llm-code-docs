# Source: https://docs.snowflake.com/en/sql-reference/info-schema/class_instance_functions.md

# CLASS_INSTANCE_FUNCTIONS view

This Information Schema view displays a row for each function in a
[class](../snowflake-db-classes.md) instance.

See also:
:   [CLASS_INSTANCES view](class_instances.md),
    [CLASS_INSTANCE_PROCEDURES view](class_instance_procedures.md),
    [SHOW FUNCTIONS](../sql/show-functions.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| FUNCTION_NAME | VARCHAR | Name of the function. |
| FUNCTION_INSTANCE_NAME | VARCHAR | Name of the class instance to which the function belongs. |
| FUNCTION_INSTANCE_SCHEMA | VARCHAR | Name of the schema to which the class instance belongs. |
| FUNCTION_INSTANCE_DATABASE | VARCHAR | Name of the database to which the class instance belongs. |
| FUNCTION_OWNER | VARCHAR | Name of the role that owns the function. |
| ARGUMENT_SIGNATURE | VARCHAR | Type signature of the function’s arguments. |
| DATA_TYPE | VARCHAR | Data type of the return value. |
| CHARACTER_MAXIMUM_LENGTH | NUMBER | Maximum length in characters of string type return value. |
| CHARACTER_OCTET_LENGTH | NUMBER | Maximum length in bytes of string type return value. |
| NUMERIC_PRECISION | NUMBER | Numeric precision of numeric type return value. |
| NUMERIC_PRECISION_RADIX | NUMBER | Radix of precision of numeric type return value. |
| NUMERIC_SCALE | NUMBER | Scale of numeric type return value. |
| FUNCTION_LANGUAGE | VARCHAR | Language of the function. |
| FUNCTION_DEFINITION | VARCHAR | Function definition. |
| VOLATILITY | VARCHAR | Whether the function is volatile or immutable. |
| IS_NULL_CALL | VARCHAR | ‘YES’ if the function is called on null input. |
| IS_SECURE | VARCHAR | ‘YES’ if the function is [secure](../../developer-guide/secure-udf-procedure.md). |
| CREATED | TIMESTAMP_LTZ | Date and time when the function was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| COMMENT | VARCHAR | Comment for this function. |
| IS_EXTERNAL [1] | VARCHAR | ‘YES’ if the function is an [external function](../external-functions.md). |
| API_INTEGRATION [1] | VARCHAR | Name of the API integration object to authenticate the call to the proxy service. |
| CONTEXT_HEADERS [1] | VARCHAR | Context header information for the external function. |
| MAX_BATCH_ROWS [1] | NUMBER | Maximum number of rows in each batch sent to the proxy service. |
| COMPRESSION [1] | VARCHAR | Type of compression. |
| PACKAGES | VARCHAR | Packages requested by the function. |
| RUNTIME_VERSION | VARCHAR | Runtime version of the language used by the function. NULL if the function is SQL or JavaScript. |
| INSTALLED_PACKAGES | VARCHAR | All packages installed by the function. Output for Python functions only. |
| IS_MEMOIZABLE | VARCHAR | ‘YES’ if the function is memoizable, ‘NO’ otherwise. |

[1]
(1,2,3,4,5)

These fields apply only to [Writing external functions](../external-functions.md).

## Usage notes

* The view only displays objects for which the current role for the session has been granted
  an instance role with access privileges.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

## Examples

Retrieve the functions for class instances in the `mydatabase` database:

```sqlexample
SELECT function_name,
       function_instance_name AS instance_name,
       argument_signature,
       data_type AS return_value_data_type
    FROM mydatabase.INFORMATION_SCHEMA.CLASS_INSTANCE_FUNCTIONS;
```
