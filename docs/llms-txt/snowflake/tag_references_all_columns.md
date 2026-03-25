# Source: https://docs.snowflake.com/en/sql-reference/functions/tag_references_all_columns.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# TAG_REFERENCES_ALL_COLUMNS

Returns a table in which each row displays the tag name and tag value assigned to a specific column.

This function returns every tag set on every column in a given table or view, whether the tag is directly assigned to a column or through
[tag inheritance](../../user-guide/object-tagging/inheritance.md).

## Syntax

```sqlsyntax
TAG_REFERENCES_ALL_COLUMNS( '<object_name>' , '<object_domain>' )
```

## Arguments

`'object_name'`
:   Name of the referenced object if the tag association is on the object.

    This argument supports the names for tables and views.

`'object_domain'`
:   Domain of the referenced object.

    Snowflake supports one domain for this function: `TABLE`.

    Note that the domain `TABLE` must be used for all objects that contain columns, even if the object name is a view
    (i.e. view, materialized view).

## Usage notes

* Results are only returned for a role that has access to the specified object.

  To view references for [system tags](../../user-guide/classify-intro.md) associated with sensitive data classification, use a role
  with IMPORTED PRIVILEGES on the shared SNOWFLAKE database.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function
  must use the fully-qualified object name. For more details, see [Snowflake Information Schema](../info-schema.md).

## Output

The function returns the following columns:

| Column | Data Type | Description |
| --- | --- | --- |
| TAG_DATABASE | TEXT | The database in which the tag is set. |
| TAG_SCHEMA | TEXT | The schema in which the tag is set. |
| TAG_NAME | TEXT | The name of the tag. This is the `key` in the `key = 'value'` pair of the tag. |
| TAG_VALUE | TEXT | The value of the tag. This is the `'value'` in the `key = 'value'` pair of the tag. |
| APPLY_METHOD | TEXT | Specifies how the tag got assigned to the object. Possible values include the following:   *`CLASSIFIED`: The tag was automatically applied to a column that was classified as containing sensitive data. See [About tag mapping](../../user-guide/classify-auto.md).* `INHERITED`: The object inherited the tag from an object higher up in the Snowflake securable object hierarchy. See [Tag inheritance](../../user-guide/object-tagging/inheritance.md). *`MANUAL`: Someone manually set the tag on the object using a CREATE <object> or ALTER <object> command. See [Set a tag](../../user-guide/object-tagging/work.md).* `PROPAGATED`: The tag was automatically propagated from one object to another. See [Automatic tag propagation with user-defined tags](../../user-guide/object-tagging/propagation.md). *`NULL`: Legacy record.* `NONE`: Legacy record. |
| LEVEL | TEXT | The object domain on which the tag is set. |
| OBJECT_DATABASE | TEXT | The database name containing the table or view. |
| OBJECT_SCHEMA | TEXT | The schema name containing the table or view. |
| OBJECT_NAME | TEXT | The name of the table or view. |
| DOMAIN | TEXT | This value should be `COLUMN` since this function returns all tags set on all columns in the table or view. |
| COLUMN_NAME | TEXT | The name of the column that the tag is set on. |

## Examples

Retrieve the list of tags that are assigned to every column in the table `my_table`:

> ```sqlexample
> select *
>   from table(my_db.information_schema.tag_references_all_columns('my_table', 'table'));
> ```
