# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/backup_sets.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/backup_sets.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/backup_sets.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# BACKUP_SETS view

This Account Usage view provides information about [backup sets](../../user-guide/backups.md) and their properties.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal system-generated identifier for the backup set. |
| NAME | VARCHAR | Name of the backup set |
| SCHEMA_ID | NUMBER | Internal system-generated identifier for the schema of the backup set. |
| SCHEMA_NAME | VARCHAR | Schema that the backup set belongs to. |
| CATALOG_ID | NUMBER | Internal system-generated identifier for the database of the backup set. |
| CATALOG_NAME | VARCHAR | Database that the backup set belongs to. |
| OBJECT_KIND | VARCHAR | Type of object that the backup set is backing up. |
| OBJECT_ID | NUMBER | ID of object that the backup set is backing up. |
| OBJECT_NAME | VARCHAR | Name of object that the backup set is backing up. |
| OBJECT_SCHEMA_ID | NUMBER | ID of schema that contains the object that is backed up by this backup set. |
| OBJECT_SCHEMA_NAME | VARCHAR | Name of schema that contains the object that is backed up by this backup set. |
| OBJECT_CATALOG_ID | NUMBER | ID of database that contains the object that is backed up by this backup set. |
| OBJECT_CATALOG_NAME | VARCHAR | Name of database that contains the object that is backed up by this backup set. |
| BACKUP_POLICY_ID | NUMBER | ID of backup policy attached to this backup set. |
| BACKUP_POLICY_NAME | VARCHAR | Name of backup policy attached to this backup set. |
| BACKUP_POLICY_SCHEMA_ID | NUMBER | ID of the schema that contains the backup policy. |
| BACKUP_POLICY_SCHEMA_NAME | VARCHAR | Name of the schema that contains the backup policy. |
| BACKUP_POLICY_CATALOG_ID | NUMBER | ID of the database that contains the backup policy. |
| BACKUP_POLICY_CATALOG_NAME | VARCHAR | Name of the database that contains the backup policy. |
| OWNER | VARCHAR | Name of the role that owns the backup set. |
| OWNER_ROLE_TYPE | VARCHAR | Type of role that owns the backup set. Account role or Database role. |
| CREATED | TIMESTAMP_LTZ | Date and time when the backup set was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the backup set was deleted. |
| COMMENT | VARCHAR | Comment for the backup set. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
