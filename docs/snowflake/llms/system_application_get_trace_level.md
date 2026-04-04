# Source: https://docs.snowflake.com/en/sql-reference/functions/system_application_get_trace_level.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$APPLICATION_GET_TRACE_LEVEL

Returns the trace level for the specified object. The following objects are supported:

* Functions
* Schemas
* Stored procedures
* Versioned schemas

## Syntax

```sqlsyntax
SYSTEM$APPLICATION_GET_TRACE_LEVEL( '<schema_name>.<object_name>' )
```

## Arguments

`'schema_name.object_name'`
:   The name of schema (or versioned schema) and object you want to determine the log
    level for.

## Usage notes

* This function can only be called by a Snowflake Native App and must be run as the APP_PRIMARY
  role.

## Examples

```sqlexample
SELECT SYSTEM$APPLICATION_GET_TRACE_LEVEL('my_schema');
```
