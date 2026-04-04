# Source: https://docs.snowflake.com/en/sql-reference/info-schema/indexes.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/indexes.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# INDEXES view

This Account Usage view displays a row for each index defined in the specified (or current) database.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | ID of the index. |
| NAME | TEXT | Name of the index. |
| TABLE_ID | NUMBER | ID of the hybrid table. |
| TABLE_NAME | TEXT | Name of the hybrid table. |
| SCHEMA_ID | TEXT | ID of the schema to which the hybrid table belongs. |
| SCHEMA_NAME | TEXT | Schema to which the hybrid table belongs. |
| DATABASE_ID | NUMBER | ID of the database to which the hybrid table belongs. |
| DATABASE_NAME | TEXT | Database to which the hybrid table belongs. |
| OWNER | TEXT | Owner of the hybrid table. |
| IS_UNIQUE | TEXT | With `YES` or `NO`, indicates whether this index is a unique index. |
| CONSTRAINT_NAME | TEXT | Name of the constraint that is associated with this index. |
| STATUS | TEXT | Latest status of this index. |
| CREATED | TIMESTAMP_LTZ | Time of creation for this index. |
| DELETED | TIMESTAMP_LTZ | Date and time when the hybrid table was dropped. |
| OWNER_ROLE_TYPE | TEXT | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |

## Usage notes

Latency for the view may be up to 180 minutes (3 hours).
