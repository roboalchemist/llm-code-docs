# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/classes.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/classes.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/classes.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CLASSES view

This Account Usage view displays a row for each [class](../snowflake-db-classes.md)
in the account.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal/system-generated identifier for the class. |
| NAME | VARCHAR | Name of the class. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the class. |
| SCHEMA_NAME | VARCHAR | Name of the schema the class belongs to. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database of the class. |
| DATABASE_NAME | VARCHAR | Name of the database the class belongs to. |
| OWNER_NAME | VARCHAR | Name of the role that owns the class. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| CREATED | TIMESTAMP_LTZ | Date and time when the class was created. |
| DELETED | TIMESTAMP_LTZ | Date and time when the class was deleted. |
| COMMENT | VARCHAR | Comment for the class. |

## Usage notes

Latency for the view may be up to 180 minutes (3 hours).

## Examples

The following example finds all classes in the account:

```sqlexample
SELECT name, database_name, schema_name
  FROM SNOWFLAKE.ACCOUNT_USAGE.CLASSES;
```
