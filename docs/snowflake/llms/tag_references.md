# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/tag_references.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/tag_references.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/tag_references.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# TAG_REFERENCES

Returns a table in which each row displays an association between a tag and value.

The associated tag and value are the result of a direct association to an object or through [tag inheritance](../../user-guide/object-tagging/inheritance.md).

## Syntax

```sqlsyntax
TAG_REFERENCES( '<object_name>' , '<object_domain>' )
```

## Arguments

`'object_name'`
:   Name of the referenced object if the tag association is on the object.

`'object_domain'`
:   Domain of the reference object, such as a table or view, if the tag association is on the object. For columns, the domain is `COLUMN`
    if the tag association is on a column.

    Use one of the following values:

    > * `'ACCOUNT'`
    > * `'ALERT'`
    > * `'BACKUP POLICY'`
    > * `'BACKUP SET'`
    > * `'COLUMN'`
    > * `'COMPUTE POOL'`
    > * `'CORTEX AGENT'`
    > * `'DATABASE'`
    > * `'DATABASE ROLE'`
    > * `'FAILOVER GROUP'`
    > * `'FUNCTION'`
    > * `'INTEGRATION'`
    > * `'INSTANCE'`
    > * `'NETWORK POLICY'`
    > * `'PROCEDURE'`
    > * `'REPLICATION GROUP'`
    > * `'ROLE'`
    > * `'SCHEMA'`
    > * `'SHARE'`
    > * `'SNAPSHOT POLICY'` (deprecated; prefer `'BACKUP POLICY'`)
    > * `'SNAPSHOT SET'` (deprecated; prefer `'BACKUP SET'`)
    > * `'SNOWFLAKE INTELLIGENCE'`
    > * `'STAGE'`
    > * `'STREAM'`
    > * `'TABLE'`: Use this for all table-like objects such as views, materialized views, and external tables.
    > * `'TASK'`
    > * `'USER'`
    > * `'WAREHOUSE'`

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
| OBJECT_DATABASE | TEXT | Database name of the referenced object for database and schema objects. If the object is not a database or schema object, the value is empty. |
| OBJECT_SCHEMA | TEXT | Schema name of the referenced object (for schema objects). If the referenced object is not a schema object (e.g. warehouse), this value is empty. |
| OBJECT_NAME | TEXT | Name of the reference object if the tag association is on the object. |
| DOMAIN | TEXT | Domain of the reference object (e.g. table, view) if the tag association is on the object. If the tag association is on a column, the domain is COLUMN. |
| COLUMN_NAME | TEXT | Name of the referenced column; not applicable if the tag association is not a column. |

## Examples

Retrieve the list of tags associated with the table `my_table`:

> ```sqlexample
> select *
>   from table(my_db.information_schema.tag_references('my_table', 'table'));
> ```

Retrieve the list of tags associated on the column `result`:

> ```sqlexample
> select *
>   from table(my_db.information_schema.tag_references('my_table.result', 'COLUMN'));
> ```
