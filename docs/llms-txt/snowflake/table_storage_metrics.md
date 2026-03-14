# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/table_storage_metrics.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/table_storage_metrics.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/table_storage_metrics.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# TABLE_STORAGE_METRICS view

This Account Usage view displays table-level storage utilization information, which is used to calculate the storage billing for each table in the account, including tables that have been dropped, but are still incurring storage costs.

In addition to table metadata, the view displays the number of storage bytes billed for each table. Snowflake breaks down the bytes into the following categories:

* Active bytes, representing data in the table that can be queried.
* Deleted bytes that are still accruing storage charges because they have not been purged yet from the system. These bytes are classified into the following sub-categories:

  > * Bytes in Time Travel (recently deleted, but still within the Time Travel retention period for the table).
  > * Bytes in Fail-safe (deleted bytes that are past the Time Travel retention period, but within the Fail-safe period for the table).
  > * Bytes retained for clones (deleted bytes that are no longer in Time Travel or Fail-safe, but are still retained because clones of the table reference the bytes).

In other words, rows are maintained in this view until the corresponding tables are no longer billed for any storage, regardless of various states that the data in the tables may be in (active, Time Travel, Fail-safe, or retained for clones).

For more details about data storage in tables, see [Data storage considerations](../../user-guide/tables-storage-considerations.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | Internal/system-generated identifier for the table. |
| TABLE_NAME | VARCHAR | Name of the table. |
| TABLE_SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema of the table. |
| TABLE_SCHEMA | VARCHAR | Schema that the table belongs to. |
| TABLE_CATALOG_ID | NUMBER | Internal/system-generated identifier for the database of the table. |
| TABLE_CATALOG | VARCHAR | Database that the table belongs to. |
| CLONE_GROUP_ID | NUMBER | Unique identifier for the oldest clone ancestor of this table. Same as ID if the table is not a clone. |
| IS_TRANSIENT | VARCHAR | ‘YES’ if table is transient or temporary, otherwise ‘NO’. Transient and temporary tables have no Fail-safe period. |
| ACTIVE_BYTES | NUMBER | Bytes owned by (and billed to) this table that are in the active state for the table. For Iceberg table storage, active bytes aren’t billed to *Iceberg* tables. For more information, see [Iceberg table billing](../../user-guide/tables-iceberg.md). |
| TIME_TRAVEL_BYTES | NUMBER | Bytes owned by (and billed to) this table that are in the Time Travel state for the table. |
| FAILSAFE_BYTES | NUMBER | Bytes owned by (and billed to) this table that are in the Fail-safe state for the table. |
| RETAINED_FOR_CLONE_BYTES | NUMBER | Bytes owned by (and billed to) this table that are retained after deletion because they are referenced by one or more clones of this table, or by [WORM backups](../../user-guide/backups.md) that contain the table. |
| DELETED | BOOLEAN | TRUE if table has been dropped or recreated. |
| TABLE_CREATED | TIMESTAMP_LTZ | Date and time when the table was created. |
| TABLE_DROPPED | TIMESTAMP_LTZ | Date and time when the table was dropped. NULL if table has not been dropped. |
| TABLE_ENTERED_FAILSAFE | TIMESTAMP_LTZ | Date and time when the table, if dropped, entered the Fail-safe state, or NULL. In this state, the table cannot be restored using UNDROP. For transient tables, which aren’t recoverable using Fail-safe, this column indicates when the time travel retention period has passed. |
| SCHEMA_CREATED | TIMESTAMP_LTZ | Date and time when the schema for the table was created. |
| SCHEMA_DROPPED | TIMESTAMP_LTZ | Date and time when the schema for the table was dropped. |
| CATALOG_CREATED | TIMESTAMP_LTZ | Date and time when the database for the table was created. |
| CATALOG_DROPPED | TIMESTAMP_LTZ | Date and time when the database for the table was dropped. |
| COMMENT | VARCHAR | Comment for the table. |
| INSTANCE_ID | NUMBER | Internal/system-generated identifier for the instance which the object belongs to. |
| ARCHIVE_STORAGE_COOL_ACTIVE_BYTES | NUMBER | The number of bytes in the cool storage tier owned by (and billed to) this table that are in the active state for the table. |
| ARCHIVE_STORAGE_COLD_ACTIVE_BYTES | NUMBER | The number of bytes in the cold storage tier owned by (and billed to) this table that are in the active state for the table. |
| ARCHIVE_STORAGE_COOL_TIME_TRAVEL_BYTES | NUMBER | The number of bytes in the cool storage tier owned by (and billed to) this table that are in the Time Travel state for the table. |
| ARCHIVE_STORAGE_COLD_TIME_TRAVEL_BYTES | NUMBER | The number of bytes in the cold storage tier owned by (and billed to) this table that are in the Time Travel state for the table. |
| ARCHIVE_STORAGE_COOL_FAILSAFE_BYTES | NUMBER | The number of bytes owned by (and billed to) this table in the COOL storage tier that are in the Fail-safe state for the table. |
| ARCHIVE_STORAGE_COLD_FAILSAFE_BYTES | NUMBER | The number of bytes owned by (and billed to) this table in the COLD storage tier that are in the Fail-safe state for the table. |
| ARCHIVE_STORAGE_COOL_EARLY_DELETION_PENALTY_BYTES | NUMBER | The number of penalty bytes deleted early and billed for) that are in the COOL storage tier. For more information, see [minimum storage duration charges](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). |
| ARCHIVE_STORAGE_COLD_EARLY_DELETION_PENALTY_BYTES | NUMBER | The number of penalty bytes deleted early and billed for) that are in the COLD storage tier. For more information, see [minimum storage duration charges](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). |

## Usage notes

* Latency for the view may be up to 90 minutes.
* Storage metrics for hybrid tables are not tracked in this view. For information about storage consumption for hybrid tables,
  see [Evaluate cost for hybrid tables](../../user-guide/tables-hybrid-cost.md).
* > **Note:**
  >
  > With [BCR-2127](../../release-notes/bcr-bundles/2025_07/bcr-2127.md),
  > this view includes new columns for storage lifecycle policies.
  > To view storage lifecycle policy columns, you must enable the 2025_07 behavior change bundle
  > in your account.
  >
  > To [enable this bundle in your account](../../release-notes/bcr-bundles/managing-behavior-change-releases.md),
  > execute the following statement:
  >
  > ```sqlexample
  > SELECT SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2025_07');
  > ```

* `ID` and `CLONE_GROUP_ID`:

  > * `ID` does not change for a table throughout its lifecycle, including if the table is renamed or dropped.
  > * `CLONE_GROUP_ID` is the ID of the oldest ancestor of a clone, including if the table has been dropped, but is still accruing storage costs. For example:
  >
  >   > 1. Table `t2` is cloned from `t1`.
  >   > 2. Table `t3` is cloned from `t2`.
  >
  >   All three tables list the `ID` for `t1` as their `CLONE_GROUP_ID`, even if `t1` is dropped and eventually purged from Snowflake.
  > * If the IDs are identical, the table is not a clone.
  > * Storage bytes are always owned by, and therefore billed to, the table where the bytes were initially added. If the table is then cloned, storage metrics for these initial bytes never transfer
  >   to the clones, even if the bytes are deleted from the source table.
* Cloned tables share the same underlying storage (at the micro-partition level) until either the original table or cloned table is modified. With each change made to either table, the table takes
  “ownership” of the changed bytes.
* Dropped tables are displayed in the view as long as they still incur storage costs:

  > * Dropped tables retain their active storage metrics, indicating how many bytes will be active if the table is restored.
  > * Dropped tables in the Time Travel retention period for the table can be restored using the UNDROP command.
  > * Dropped tables in Fail-safe (`TABLE_ENTERED_FAILSAFE` is not `NULL`) will potentially display `NULL` values in most columns, except for:
  >
  >   > ID columns:
  >   > :   `ID` , `CLONE_GROUP_ID`
  >   >
  >   > Bytes columns:
  >   > :   `ACTIVE_BYTES` , `TIME_TRAVEL_BYTES` , `FAILSAFE_BYTES` , `RETAINED_FOR_CLONE_BYTES`
  >
  >   These tables cannot be restored using the UNDROP command.
* When data is deleted from a table with a Time Travel retention period of 0 days, asynchronous background processes purge the active bytes
  or move them directly into Fail-safe storage, depending on the table type. This may take a short time to complete. During that time, the
  `TIME_TRAVEL_BYTES` column may contain a non-zero value even when the Time Travel retention period is 0 days.
* `FAILSAFE_BYTES` denotes bytes that have passed beyond Time Travel. All such bytes are billed to the current table.
* If multiple rows have the same value in the `TABLE_NAME` column, this indicates that multiple versions of the table exist. A version is created each time a table is dropped and a new table
  with the same name is created, including when a [CREATE OR REPLACE TABLE](../sql/create-table.md) command is issued on an existing table. Note that the current version will have a
  `NULL` value for the `TABLE_DROPPED` column; all other versions will have a timestamp value. This is important to note because each version of a table incurs storage costs associated with
  Time Travel (and Fail-safe, if the table is permanent).
* Any data in the `DELETED` column prior to August 2018 may not be accurate.
* In some cases, active bytes might include bytes for data in a dropped column. For more information,
  see the [usage notes](../sql/alter-table.md) for ALTER TABLE.
* For Iceberg tables:

  * Snowflake doesn’t bill for [Iceberg table](../../user-guide/tables-iceberg.md) storage.
    For more information, see [Iceberg table billing](../../user-guide/tables-iceberg.md).
  * If the table is externally managed and uses [row-level deletes](../../user-guide/tables-iceberg-manage.md),
    this view might display inaccurate storage utilization information.
