# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/snapshot_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/snapshot_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snapshot_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNAPSHOT_POLICIES view — *Deprecated*

This Account Usage view provides information about [snapshot policies](../../user-guide/backups.md)
and their properties.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal system-generated identifier for the snapshot policy. |
| NAME | VARCHAR | Name of the snapshot policy. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the snapshot policy. |
| SCHEMA_NAME | VARCHAR | Schema that the snapshot policy belongs to. |
| CATALOG_ID | NUMBER | Internal system-generated identifier for the database of the snapshot policy. |
| CATALOG_NAME | VARCHAR | Database that the snapshot policy belongs to. |
| SCHEDULE | VARCHAR | Schedule for snapshot creation. |
| EXPIRE_AFTER_DAYS | NUMBER | Days after snapshot creation when snapshot should be expired and automatically deleted. |
| HAS_RETENTION_LOCK | VARCHAR | Indicates whether the policy includes a retention lock. Y if the policy has a retention lock; N otherwise.  Retention lock protects snapshots from being deleted by anyone for the defined retention period. The retention lock also prevents the retention period from being decreased on the policy. |
| OWNER | VARCHAR | Name of the role that owns the snapshot policy. |
| OWNER_ROLE_TYPE | VARCHAR | Type of role that owns the snapshot policy. Account role or Database role. |
| CREATED | TIMESTAMP_LTZ | Date and time when the snapshot policy was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| DELETED | TIMESTAMP_LTZ | Date and time when the snapshot policy was deleted. |
| COMMENT | VARCHAR | Comment for the snapshot policy. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.
