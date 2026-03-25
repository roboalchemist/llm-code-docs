# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/snapshot_sets.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/snapshot_sets.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snapshot_sets.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNAPSHOT_SETS view — *Deprecated*

This Account Usage view provides information about [snapshot sets](../../user-guide/backups.md) and their properties.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal system-generated identifier for the snapshot set. |
| NAME | VARCHAR | Name of the snapshot set |
| SCHEMA_ID | NUMBER | Internal system-generated identifier for the schema of the snapshot set. |
| SCHEMA_NAME | VARCHAR | Schema that the snapshot set belongs to |
| CATALOG_ID | NUMBER | Internal system-generated identifier for the database of the snapshot set. |
| CATALOG_NAME | VARCHAR | Database that the snapshot set belongs to. |
| OBJECT_KIND | VARCHAR | Type of object that the snapshot set is snapshotting. |
| OBJECT_ID | NUMBER | ID of object that the snapshot set is snapshotting. |
| OBJECT_NAME | VARCHAR | Name of object that the snapshot set is snapshotting. |
| OBJECT_SCHEMA_ID | NUMBER | ID of schema that contains the object being snapshotted by this snapshot set. |
| OBJECT_SCHEMA_NAME | VARCHAR | Name of schema that contains the object being snapshotted by this snapshot set. |
| OBJECT_CATALOG_ID | NUMBER | ID of database that contains the object being snapshotted by this snapshot set. |
| OBJECT_CATALOG_NAME | VARCHAR | Name of database that contains the object being snapshotted by this snapshot set. |
| SNAPSHOT_POLICY_ID | NUMBER | ID of snapshot policy attached to this snapshot set. |
| SNAPSHOT_POLICY_NAME | VARCHAR | Name of snapshot policy attached to this snapshot set. |
| SNAPSHOT_POLICY_SCHEMA_ID | NUMBER | ID of the schema that contains the snapshot policy. |
| SNAPSHOT_POLICY_SCHEMA_NAME | VARCHAR | Name of the schema that contains the snapshot policy. |
| SNAPSHOT_POLICY_CATALOG_ID | NUMBER | ID of the database that contains the snapshot policy. |
| SNAPSHOT_POLICY_CATALOG_NAME | VARCHAR | Name of the database that contains the snapshot policy. |
| OWNER | VARCHAR | Name of the role that owns the snapshot set. |
| OWNER_ROLE_TYPE | VARCHAR | Type of role that owns the snapshot set. Account role or Database role. |
| CREATED | TIMESTAMP_LTZ | Date and time when the snapshot set was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the snapshot set was deleted. |
| COMMENT | VARCHAR | Comment for the snapshot set. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
