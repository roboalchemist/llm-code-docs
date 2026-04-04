# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_tag_on_current_column.md

Categories:
:   [System functions](../functions-system.md)

# SYSTEM$GET_TAG_ON_CURRENT_COLUMN

Returns the tag string value assigned to the column based upon the specified tag or NULL if a tag is not assigned to the specified column.

When the body of a [masking policy](../../user-guide/security-column-intro.md) or [projection policy](../../user-guide/projection-policies.md)
includes this function, the value of a tag assigned to a column can determine the return value of the policy assigned to that column.

## Syntax

```sqlsyntax
SYSTEM$GET_TAG_ON_CURRENT_COLUMN( '<tag_name>' )
```

## Arguments

`'tag_name'`
:   Identifier for the tag as a string.

    For example, if the tag is named `cost_center` use `'cost_center'` as the argument.

## Usage notes

* Currently, this function can only be used in a masking policy or projection policy condition to dynamically evaluate the tag string value
  set on a column.

  Snowflake returns an error while using the function in either a SELECT query, a row access policy, a view, or a user-defined function
  (UDF).
* Note that this function applies to all table-like objects (e.g. views).
* The tag must exist when calling this system function; otherwise, Snowflake returns the following error message:

  ```none
  Tag '<tag_name>' does not exist or not authorized.
  ```

## Examples

Masking policy
:   For a contextual example on how to use this function with a masking policy, see [Example 2: Protect column data based on the column tag string value](../../user-guide/tag-based-masking-policies.md).

Projection policy
:   When the following projection policy is assigned to a column, the value of the `tags.accounting_col` tag on that column must be
    `public` in order to project the column.

```sqlexample
CREATE PROJECTION POLICY mypolicy
AS () RETURNS PROJECTION_CONSTRAINT ->
CASE
  WHEN SYSTEM$GET_TAG_ON_CURRENT_COLUMN('tags.accounting_col') = 'public'
    THEN PROJECTION_CONSTRAINT(ALLOW => true)
  ELSE PROJECTION_CONSTRAINT(ALLOW => false)
END;
```
