# Source: https://docs.snowflake.com/en/sql-reference/info-schema/hybrid_tables.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/hybrid_tables.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# HYBRID_TABLES view

This Account Usage view displays a row for each hybrid table defined in the specified (or current) database.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | ID of the hybrid table. |
| NAME | TEXT | Name of the hybrid table. |
| SCHEMA_ID | NUMBER | ID of the schema to which the hybrid table belongs. |
| SCHEMA_NAME | TEXT | Schema to which the hybrid table belongs. |
| DATABASE_ID | NUMBER | ID of the database to which the hybrid table belongs. |
| DATABASE_NAME | TEXT | Database to which the hybrid table belongs. |
| OWNER | TEXT | Owner of the hybrid table. |
| ROW_COUNT | NUMBER | Approximate row count of the hybrid table. |
| BYTES | NUMBER | Approximate size in bytes of the row store of the hybrid table. |
| RETENTION_TIME | NUMBER | Retention time for data in the hybrid table. |
| CREATED | TIMESTAMP_LTZ | Creation time of the hybrid table. |
| LAST_ALTERED | TIMESTAMP_LTZ | Last time this hybrid table was altered by a DDL statement, a TRUNCATE or INSERT OVERWRITE statement, or a compaction job. Note that regular DML operations are not recorded here. |
| DELETED | TIMESTAMP_LTZ | Date and time when the hybrid table was dropped. |
| COMMENT | TEXT | Comment for the hybrid table. |
| OWNER_ROLE_TYPE | TEXT | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |

## Usage notes

Latency for the view may be up to 180 minutes (3 hours).
