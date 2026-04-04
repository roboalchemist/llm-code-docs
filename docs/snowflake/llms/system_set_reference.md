# Source: https://docs.snowflake.com/en/sql-reference/functions/system_set_reference.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$SET_REFERENCE

Called by a Snowflake Native App to associate a consumer reference string to a reference definition.
The app can use this association to access the consumer object. The reference string passed to this system function is the value returned by the
[SYSTEM$REFERENCE](system_reference.md) function, which represents a consumer object.

This function only supports a single-valued reference. If an association has already been created using the same reference name, the existing association is overwritten.

## Syntax

```sqlsyntax
SYSTEM$SET_REFERENCE('<reference_name>', '<reference_string>')
```

## Arguments

**Required**

`'reference_name'`
:   The name of the reference as specified in the `manifest.yml` file of the app.

`'reference_string'`
:   The system-generated ID of the reference to the object in the consumer account.
