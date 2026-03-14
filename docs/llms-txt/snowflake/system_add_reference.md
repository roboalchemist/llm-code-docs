# Source: https://docs.snowflake.com/en/sql-reference/functions/system_add_reference.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ADD_REFERENCE

Called by a Snowflake Native App to associate a consumer reference string to a reference definition. The app can use this
association to access the consumer object. The reference string passed to this system function is the value returned by the
[SYSTEM$REFERENCE](system_reference.md) function, which represents a consumer object.

For information about using this function in an app, see
[Request references and object-level privileges from consumers](../../developer-guide/native-apps/requesting-refs.md).

This function supports both single and multi-valued references. The function returns an
error if an association has already been created using the same value specified by
`reference_name`.

## Syntax

```sqlsyntax
SYSTEM$ADD_REFERENCE('<reference_name>', '<reference_string>')
```

## Arguments

`'reference_name'`
:   The name of the reference as specified in the `manifest.yml` file of the app.

`'reference_string'`
:   The system-generated ID of the reference to the object in the consumer account.
