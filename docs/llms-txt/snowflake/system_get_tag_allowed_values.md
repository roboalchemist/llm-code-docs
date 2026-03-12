# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_tag_allowed_values.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_TAG_ALLOWED_VALUES

Returns a comma-separated list of string values that can be set on a [supported object](../../user-guide/object-tagging/introduction.md), or NULL
to indicate the tag key does not have any specified string values and accepts all [possible](../../user-guide/object-tagging/introduction.md) string
values.

See also:
:   [Set a list of allowed tag values](../../user-guide/object-tagging/work.md) , [TAGS view](../account-usage/tags.md)

## Syntax

```sqlsyntax
SYSTEM$GET_TAG_ALLOWED_VALUES('<name>')
```

## Arguments

`name`
:   The fully-qualified name of the tag key as a string.

## Usage notes

* The role that calls this function must have either the USAGE privilege on the parent database and schema of the tag or the global APPLY
  TAG on ACCOUNT permission.
* Snowflake returns NULL when you pass the SNOWFLAKE.CORE.SEMANTIC_CATEGORY system tag as an argument in the function because there is not
  an allowed values constraint with this tag.

## Examples

Query the allowed tag values for the tag key named `cost_center`, which resides in the database named `governance` and the schema named
`tags`:

> ```sqlexample
> select system$get_tag_allowed_values('governance.tags.cost_center');
> ```
