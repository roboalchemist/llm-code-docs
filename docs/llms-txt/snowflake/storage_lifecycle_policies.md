# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/storage_lifecycle_policies.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/storage_lifecycle_policies.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# STORAGE_LIFECYCLE_POLICIES view

This Account Usage view displays [storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies.md).
Each row in this view corresponds to a different storage lifecycle policy.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| NAME | TEXT | Name of the storage lifecycle policy. |
| ID | NUMBER | Internal/system-generated identifier for the storage lifecycle policy. |
| SCHEMA_ID | TEXT | Internal/system-generated identifier for the schema in which the policy resides. |
| SCHEMA | TEXT | Schema to which the storage lifecycle policy belongs. |
| DATABASE_ID | TEXT | Internal/system-generated identifier for the database in which the policy resides. |
| DATABASE | TEXT | Database to which the storage lifecycle policy belongs. |
| OWNER | TEXT | Name of the role that owns the storage lifecycle policy. |
| SIGNATURE | TEXT | Type signature of the storage lifecycle policy’s arguments. |
| RETURN_TYPE | TEXT | Return value data type. |
| BODY | TEXT | Storage lifecycle policy definition. |
| COMMENT | TEXT | Comments entered for the storage lifecycle policy. |
| CREATED_ON | TIMESTAMP_LTZ | Date and time when the storage lifecycle policy was created. |
| LAST_ALTERED_ON | TIMESTAMP_LTZ | Date and time when the storage lifecycle policy was last altered. |
| DELETED_ON | TIMESTAMP_LTZ | Date and time when the storage lifecycle policy was dropped. |
| OPTIONS | OBJECT | Storage lifecycle policy options, including ARCHIVE_FOR_DAYS (number of days to keep data in current tier) and ARCHIVE_TIER (target storage tier). |

## Usage notes

* Latency for the view may be up to 120 minutes (2 hours).
