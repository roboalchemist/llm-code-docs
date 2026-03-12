# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/hive/ddls/tables.md

# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/tables.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/tables.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/tables.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# TABLES view

This Account Usage view displays a row for each table and view in the account.

See also:
:   [COLUMNS view](columns.md) , [VIEWS view](views.md), [TABLES view](../info-schema/tables.md) (Information Schema)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| TABLE_ID | NUMBER | Internal, Snowflake-generated identifier for the table. |
| TABLE_NAME | VARCHAR | Name of the table. |
| TABLE_SCHEMA_ID | NUMBER | Internal, Snowflake-generated identifier of the schema for the table. |
| TABLE_SCHEMA | VARCHAR | Schema that the table belongs to. |
| TABLE_CATALOG_ID | NUMBER | Internal, Snowflake-generated identifier of the database for the table. |
| TABLE_CATALOG | VARCHAR | Database that the table belongs to. |
| TABLE_OWNER | VARCHAR | Name of the role that owns the table. |
| TABLE_TYPE | VARCHAR | Indicates the table type. Valid values are `BASE TABLE`, `TEMPORARY TABLE`, `EXTERNAL TABLE`, `EVENT TABLE`, `VIEW`, or `MATERIALIZED VIEW`. |
| IS_TRANSIENT | VARCHAR | Indicates whether the table is transient. |
| CLUSTERING_KEY | VARCHAR | Column(s) and/or expression(s) that comprise the clustering key for the table. |
| ROW_COUNT | NUMBER | Number of rows in the table. |
| BYTES | NUMBER | Number of bytes accessed by a scan of the table. |
| RETENTION_TIME | NUMBER | Number of days that historical data is retained for Time Travel. |
| SELF_REFERENCING_COLUMN_NAME | VARCHAR | Not applicable for Snowflake. |
| REFERENCE_GENERATION | VARCHAR | Not applicable for Snowflake. |
| USER_DEFINED_TYPE_CATALOG | VARCHAR | Not applicable for Snowflake. |
| USER_DEFINED_TYPE_SCHEMA | VARCHAR | Not applicable for Snowflake. |
| USER_DEFINED_TYPE_NAME | VARCHAR | Not applicable for Snowflake. |
| IS_INSERTABLE_INTO | VARCHAR | Not applicable for Snowflake. |
| IS_TYPED | VARCHAR | Not applicable for Snowflake. |
| COMMIT_ACTION | VARCHAR | Not applicable for Snowflake. |
| CREATED | TIMESTAMP_LTZ | Date and time when the table was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered by a DML, DDL, or background metadata operation. See Usage Notes. |
| LAST_DDL | TIMESTAMP_LTZ | Timestamp of the last DDL operation performed on the table or view.  All supported table/view DDL operations update this field:   * { CREATE | ALTER | DROP | UNDROP } TABLE * { CREATE | ALTER | DROP } VIEW   All ALTER TABLE operations update this field, including setting or unsetting a table parameter (for example, COMMENT, DATA_RETENTION_TIME, etc.) and changes to table columns (ADD / MODIFY / RENAME / DROP).  For more information, see the Usage Notes. |
| LAST_DDL_BY | VARCHAR | The current username for the user who executed the last DDL operation. If the user has been dropped, shows `DROPPED_USER(<id>)`.  For dropped users, you can join the `<id>` with the USER_ID column in the USERS view of the ACCOUNT_USAGE or ORGANIZATION_USAGE schema. |
| DELETED | TIMESTAMP_LTZ | Date and time when the table was dropped. |
| AUTO_CLUSTERING_ON | VARCHAR | Status of Automatic Clustering for a table. For details, see [Viewing the Automatic Clustering status for a table](../../user-guide/tables-auto-reclustering.md). |
| COMMENT | VARCHAR | Comment for the table. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the object, for example `ROLE`. . If a Snowflake Native App owns the object, the value is `APPLICATION`. . Snowflake returns NULL if you delete the object because a deleted object does not have an owner role. |
| INSTANCE_ID | NUMBER | Internal/system-generated identifier for the instance which the object belongs to. |
| IS_ICEBERG | VARCHAR | Indicates whether the table is an [Iceberg table](../../user-guide/tables-iceberg.md). Valid values are `YES` or `NO`. |
| IS_DYNAMIC | VARCHAR | Indicates whether the table is a [dynamic table](../../user-guide/dynamic-tables-about.md). Valid values are `YES` or `NO`. |
| IS_HYBRID | VARCHAR | Indicates whether the table is a [hybrid table](../../user-guide/tables-hybrid.md). Valid values are `YES` or `NO`. |
| ARCHIVE_STORAGE_COOL_ROW_COUNT | NUMBER | The number of rows that are in the COOL storage tier. |
| ARCHIVE_STORAGE_COOL_BYTES | NUMBER | The number of bytes accessed by retrieving data from the COOL storage tier. |
| ARCHIVE_STORAGE_COLD_ROW_COUNT | NUMBER | The number of rows that are in the COLD storage tier. |
| ARCHIVE_STORAGE_COLD_BYTES | NUMBER | The number of bytes accessed by retrieving data from the COLD storage tier. |

## Usage notes

* Latency for the view may be up to 90 minutes.
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

* The view does not recognize the MANAGE GRANTS privilege and consequently may show less information compared to a SHOW command executed by a user who holds the MANAGE GRANTS privilege.
* Querying the `SUM(BYTES)` for a table does not represent the total storage usage, because the amount does not include Time Travel and Fail-safe usage.
* Using the value in the LAST_ALTERED column for Time Travel is *not* recommended and can return unexpected results for the following
  reaons:

  * Time Travel can only be used to query historical data modified by a [DML operation](../../user-guide/data-time-travel.md).
  * The LAST_ALTERED column inludes both DML and DDL operations (see the next usage note).
  * For DML operations, the value in the LAST_ALTERED column is the timestamp at the beginning of the statement execution rather than
    the time of the commit of the transaction containing this statement.
* The LAST_ALTERED column is updated when the following operations are performed on an object:

  * DDL operations.
  * DML operations (for tables only). This column is updated even when no rows are affected by the DML statement.
  * Background maintenance operations on metadata performed by Snowflake.

  For views and tables, use the LAST_DDL column for the last modification time for an object.
* The value in the LAST_DDL column is updated as follows:

  > * When a table or view is created, the LAST_DDL timestamp is the same as the CREATED timestamp.
  > * When a table or view is dropped, the LAST_DDL timestamp is the same as the DELETED timestamp.
  > * Last DDL data is not available for operations that occurred before the columns were
  >   [added](../../release-notes/bcr-bundles/2023_01/bcr-891.md). The new DDL fields contain `null` until a DDL operation is executed.
  > * For replicated databases, the LAST_DDL and LAST_DDL_BY fields are only updated for objects in the primary database. After failover, the
  >   LAST_DDL and LAST_DDL_BY fields are updated for DDL operations for the tables and views in the newly promoted primary database. These
  >   fields will remain unchanged for objects in the now secondary database.
  > * For objects in secondary databases that are newly created during a refresh operation, these fields are `null`.
* The LAST_ALTERED column does not necessarily indicate the last refreshed time for external tables.
  To retrieve the last refreshed time for an auto-refreshed external table, you can use the
  [SYSTEM$EXTERNAL_TABLE_PIPE_STATUS](../functions/system_external_table_pipe_status.md) function, which returns
  information such as the timestamp of the last file Snowflake has registered.

## Examples

Retrieve the total size (in bytes) of all active tables in all schemas in your account:

```sqlexample
SELECT table_schema, SUM(bytes)
  FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES
  WHERE deleted IS NULL
  GROUP BY table_schema;
```
