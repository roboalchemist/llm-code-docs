# Source: https://docs.snowflake.com/en/sql-reference/functions/system_remove_all_references.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$REMOVE_ALL_REFERENCES

Deletes all associations to the reference.

## Syntax

```sqlsyntax
SYSTEM$REMOVE_ALL_REFERENCES('<reference_name>')
```

## Arguments

**Required**

`'reference_name'`
:   The name of the reference as specified in the `manifest.yml` file of the app.
