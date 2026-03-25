# Source: https://docs.snowflake.com/en/sql-reference/functions/tag_references_with_lineage.md

Categories:
:   [Account Usage table functions](../account-usage.md) , [Table functions](../functions-table.md)

# TAG_REFERENCES_WITH_LINEAGE

Returns a table in which each row displays an association between the specified tag and the Snowflake object to which the tag is associated.

The associated tag and Snowflake object are the result of both a direct association to an object and
[tag inheritance](../../user-guide/object-tagging/inheritance.md).

## Syntax

```sqlsyntax
TAG_REFERENCES_WITH_LINEAGE( '<name>' )
```

## Arguments

`'name'`
:   The fully qualified name of the tag.

    The fully qualified name must specify the parent tag database and tag schema for the tag in the following format:

    > `<tag_database>.<tag_schema>.<tag_name>`

## Usage notes

* Results are only returned for the role that has access to the specified object.
* This function doesn’t support system tags used by sensitive data classification.
* When calling an Account Usage table function, the session must have an Account Usage schema in use. For more details, see
  [Account Usage](../account-usage.md).
* Similar to the Account Usage views, please account for latency when calling this table function. The expected latency for this table
  function is similar to the latency for the [TAG_REFERENCES](../account-usage.md) view.

## Output

The function returns the following columns:

| Column | Data Type | Description |
| --- | --- | --- |
| TAG_DATABASE | TEXT | The database in which the tag is set. |
| TAG_SCHEMA | TEXT | The schema in which the tag is set. |
| TAG_ID | NUMBER | Internal/system-generated identifier for the tag. |
| TAG_NAME | TEXT | The name of the tag. This is the `key` in the `key = 'value'` pair of the tag. |
| TAG_VALUE | TEXT | The value of tag. This is the `'value'` in the `key = 'value'` pair of the tag. |
| LEVEL | TEXT | The object domain on which the tag is set. |
| OBJECT_DATABASE | TEXT | Database name of the referenced object for database and schema objects. If the object is not a database or schema object, the value is empty. |
| OBJECT_SCHEMA | TEXT | Schema name of the referenced object (for schema objects). If the referenced object is not a schema object (e.g. warehouse), this value is empty. |
| OBJECT_ID | NUMBER | Internal/system-generated identifier for the object. |
| OBJECT_NAME | TEXT | Name of the referenced object if the tag association is on the object. |
| OBJECT_DELETED | TIMESTAMP_LTZ | Date and time when the associated object or column was dropped, or if the parent object is dropped. |
| DOMAIN | TEXT | Domain of the reference object (e.g. table, view) if the tag association is on the object. If the tag association is on a column, the domain is COLUMN. |
| COLUMN_ID | NUMBER | Internal/system-generated identifier for the column. |
| COLUMN_NAME | TEXT | Name of the referenced column; not applicable if the tag association is not a column. |
| APPLY_METHOD | TEXT | Specifies how the tag got assigned to the object. Possible values include the following:   *`CLASSIFIED`: The tag was automatically applied to a column that was classified as containing sensitive data. See [About tag mapping](../../user-guide/classify-auto.md).* `INHERITED`: The object inherited the tag from an object higher up in the Snowflake securable object hierarchy. See [Tag inheritance](../../user-guide/object-tagging/inheritance.md). *`MANUAL`: Someone manually set the tag on the object using a CREATE <object> or ALTER <object> command. See [Set a tag](../../user-guide/object-tagging/work.md).* `PROPAGATED`: The tag was automatically propagated from one object to another. See [Automatic tag propagation with user-defined tags](../../user-guide/object-tagging/propagation.md). *`NULL`: Legacy record.* `NONE`: Legacy record. |

## Examples

Retrieve the list of tag associations for the `cost_center` tag:

```sqlexample
select *
  from table(snowflake.account_usage.tag_references_with_lineage('MY_DB.MY_SCHEMA.COST_CENTER'));
```

> **Note:**
>
> The tag name must be written in uppercase letters.
