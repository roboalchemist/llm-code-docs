# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/tags.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/tags.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# TAGS view

This Account Usage view lists the tags in an account.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| TAG_ID | NUMBER | The local identifier of a tag. |
| TAG_NAME | TEXT | The name of a tag. |
| TAG_SCHEMA_ID | NUMBER | The local identifier of the tag schema. |
| TAG_SCHEMA | TEXT | The name of schema in which the tag exists. |
| TAG_DATABASE_ID | NUMBER | The local identifier of the database in which the tag exists. |
| TAG_DATABASE | TEXT | The name of the database in which the tag exists. |
| TAG_OWNER | TEXT | The name of the role that owns the tag. |
| TAG_COMMENT | VARIANT | Comments for the tag, if any. |
| CREATED | TIMESTAMP_LTZ | Date and time when the tag was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the tag was dropped, or the date and time when its parents were dropped. |
| ALLOWED_VALUES | VARIANT | Specifies the possible string values that can be assigned to the tag when the tag is set on an [object](../../user-guide/object-tagging/introduction.md) or NULL if the tag does not have any specified allowed values. For details, see [Set a list of allowed tag values](../../user-guide/object-tagging/work.md). |
| OWNER_ROLE_TYPE | TEXT | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| PROPAGATE | VARCHAR | Indicates whether the tag is configured for automatic propagation. Possible values are the following:   *NULL — Tag is not propagated.* `ON_DEPENDENCY` — Tag is propagated when there is an object dependency (for example, creating a view from a tagged table). *`ON_DATA_MOVEMENT` — Tag is propagated when there is data movement (for example, using a CTAS statement to create a table   from a tagged table).* `ON_DEPENDENCY_AND_DATA_MOVEMENT` — Tag is propagated for both object dependencies and data movement. |
| ON_CONFLICT | VARCHAR | If the tag is configured for automatic propagation, indicates what happens when the value of the tag being propagated conflicts with the value that was specified when the tag was manually applied to the same object. For more information, see [Tag propagation conflicts](../../user-guide/object-tagging/propagation.md). |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).

* The view only displays objects for which the current role for the session has been granted access privileges.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

## Examples

Return the tag references for your Snowflake account:

> ```sqlexample
> select * from snowflake.account_usage.tags
> order by tag_name;
> ```
