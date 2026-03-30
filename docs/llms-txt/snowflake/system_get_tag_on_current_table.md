# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_tag_on_current_table.md

Categories:
:   [System functions](../functions-system.md)

# SYSTEM$GET_TAG_ON_CURRENT_TABLE

Returns the tag string value assigned to the table based upon the specified tag or NULL if a tag is not assigned to the specified table.

Use this function in the [masking policy](../../user-guide/security-column-intro.md) conditions or the
[row access policy](../../user-guide/security-row-intro.md) conditions.

## Syntax

```sqlsyntax
SYSTEM$GET_TAG_ON_CURRENT_TABLE( '<tag_name>' )
```

## Arguments

`'tag_name'`
:   Identifier for the tag as a string.

    For example, if the tag is named `cost_center` use `'cost_center'` as the argument.

## Usage notes

* Currently, this function can only be used in a masking policy or row access policy condition to dynamically evaluate the tag string value
  set on a table.

  Snowflake returns an error while using the function in a SELECT query, view, materialized view, or a user-defined function (UDF).
* Note that this function applies to all table-like objects (e.g. views).
* The tag must exist when calling this system function; otherwise, Snowflake returns the following error message:

  ```none
  Tag '<tag_name>' does not exist or not authorized.
  ```

## Examples

For a contextual example on how to use this function, see [Example 3: Protect a table based on the table tag string value](../../user-guide/tag-based-masking-policies.md).
