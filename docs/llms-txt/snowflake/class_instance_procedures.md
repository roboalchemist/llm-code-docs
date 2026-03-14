# Source: https://docs.snowflake.com/en/sql-reference/info-schema/class_instance_procedures.md

# CLASS_INSTANCE_PROCEDURES view

This Information Schema view displays a row for each procedure in a
[class](../snowflake-db-classes.md) instance.

See also:
:   [CLASS_INSTANCES view](class_instances.md),
    [CLASS_INSTANCE_FUNCTIONS view](class_instance_functions.md),
    [SHOW PROCEDURES](../sql/show-procedures.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| PROCEDURE_NAME | VARCHAR | Name of the stored procedure. |
| PROCEDURE_INSTANCE_NAME | VARCHAR | Name of the class instance to which the procedure belongs. |
| PROCEDURE_INSTANCE_SCHEMA | VARCHAR | Name of the schema to which the class instance belongs. |
| PROCEDURE_INSTANCE_DATABASE | VARCHAR | Name of the database to which the class instance belongs. |
| PROCEDURE_OWNER | VARCHAR | Name of the role that owns the stored procedure. |
| ARGUMENT_SIGNATURE | VARCHAR | Type signature of the stored procedure’s arguments. |
| DATA_TYPE | VARCHAR | Return value data type. |
| CHARACTER_MAXIMUM_LENGTH | NUMBER | Maximum length in characters of string return value. |
| CHARACTER_OCTET_LENGTH | NUMBER | Maximum length in bytes of string return value. |
| NUMERIC_PRECISION | NUMBER | Numeric precision of numeric return value. |
| NUMERIC_PRECISION_RADIX | NUMBER | Radix of precision of numeric return value. |
| NUMERIC_SCALE | VARCHAR | Scale of numeric return value. |
| PROCEDURE_LANGUAGE | VARCHAR | Language of the stored procedure. |
| PROCEDURE_DEFINITION | VARCHAR | Stored procedure definition. |
| CREATED | TIMESTAMP_LTZ | Date and time the stored procedure was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| COMMENT | VARCHAR | Comment for the stored procedure. |

## Usage notes

* The view only displays objects for which the current role for the session has been granted
  an instance role with access privileges.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

## Examples

Retrieve the procedures for instances in the `mydatabase` database:

```sqlexample
SELECT procedure_name,
       procedure_instance_name,
       argument_signature,
       data_type AS return_value_data_type
    FROM mydatabase.INFORMATION_SCHEMA.CLASS_INSTANCE_PROCEDURES;
```
