# Source: https://docs.snowflake.com/en/release-notes/bcr-bundles/un-bundled/bcr-account-usage-and-info-schema-changes.md

# Dynamic tables: Changes to ACCOUNT_USAGE.TABLES and INFORMATION_SCHEMA.TABLES

## New column added

The ACCOUNT_USAGE.TABLES and INFORMATION_SCHEMA.TABLES views include the following new column:

| Column name | Data type | Description |
| --- | --- | --- |
| `is_dynamic` | Text | Indicates whether the table is a dynamic table. Valid values are YES or NO. |

## Changes to ACCOUNT_USAGE.TABLES

Beginning with the **8.9** release, the following changes to ACCOUNT_USAGE.TABLES are enabled:

Before the change:
:   Dynamic tables are not included in this view. For rows that represent dynamic tables, the
    value for the `is_insertable_into` column is `YES`.

    The ACCOUNT_USAGE.TABLES view doesn’t include the `is_dynamic` column.

After the change:
:   Dynamic tables are included in this view. For rows that represent dynamic tables, the values
    of the `table_type` and `is_insertable_into` columns are `BASE TABLE` and `NO`,
    respectively.

    The ACCOUNT_USAGE.TABLES view includes the `is_dynamic` column, defined above.

## Changes to INFORMATION_SCHEMA.TABLES

Beginning with the **8.9** release, the following changes to INFORMATION_SCHEMA.TABLES are enabled:

Before the change:
:   For rows that represent dynamic tables, the values of the `table_type` and `is_insertable_into`
    columns are `NULL` and `YES`, respectively.

    The INFORMATION_SCHEMA.TABLES view doesn’t include the `is_dynamic` column.

After the change:
:   For rows that represent dynamic tables, the values of the `table_type` and `is_insertable_into`
    columns are `BASE TABLE` and `NO`, respectively.

    The INFORMATION_SCHEMA.TABLES view includes the `is_dynamic` column, defined above.
