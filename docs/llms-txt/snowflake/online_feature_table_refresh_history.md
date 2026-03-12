# Source: https://docs.snowflake.com/en/sql-reference/account-usage/online_feature_table_refresh_history.md

# ACCOUNT_USAGE.ONLINE_FEATURE_TABLE_REFRESH_HISTORY

This Account Usage view displays information for online feature table refresh history.

See also:
:   [ONLINE_FEATURE_TABLE_REFRESH_HISTORY](../functions/online-feature-table-refresh-history.md) (Information Schema)

## Columns

| Column | Data type | Description |
| --- | --- | --- |
| `NAME` | TEXT | Name of the online feature table. |
| `SCHEMA_NAME` | TEXT | Name of the schema that contains the online feature table. |
| `DATABASE_NAME` | TEXT | Name of the database that contains the online feature table. |
| `QUALIFIED_NAME` | TEXT | Fully qualified name of the online feature table. |
| `STATE` | TEXT | Status of the refresh for the online feature table. The status can be one of the following:   *`EXECUTING`: refresh in progress.* `SUCCEEDED`: refresh completed successfully. *`FAILED`: refresh failed during execution.* `CANCELLED`: refresh was canceled before completion. |
| `STATE_CODE` | TEXT | Code representing the current state of the refresh. |
| `STATE_MESSAGE` | TEXT | Description of the current state of the refresh. |
| `REFRESH_START_TIME` | TIMESTAMP_LTZ | Time when the refresh job started. |
| `REFRESH_END_TIME` | TIMESTAMP_LTZ | Time when the refresh completed. |
| `REFRESH_TRIGGER` | TEXT | One of:   *`SCHEDULED`: normal background refresh to meet target lag.* `MANUAL`: user/task ran `ALTER ONLINE FEATURE TABLE <name> REFRESH` command. * `CREATION`: refresh performed during the creation DDL statement, triggered by the creation of the online feature table. |
| `REFRESH_ACTION` | TEXT | One of:   *`NO_DATA`: no new data in base tables. Doesn’t apply to the initial refresh of newly created online feature tables regardless of whether or not the base tables have data.* `REINITIALIZE`: base table changed. *`FULL`: Full refresh, because refresh mode of the online feature table is set to FULL.* `INCREMENTAL`: normal incremental refresh. |

## Usage notes

* Online Feature Table refresh history in this view may lag by up to 3 hours.
* To query this view, use a role that is granted the SNOWFLAKE database role USAGE_VIEWER.
* The [ONLINE_FEATURE_TABLE_REFRESH_HISTORY](../functions/online-feature-table-refresh-history.md) function offers up-to-date refresh history.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE_VIEWER database role | SNOWFLAKE database | Required to query Account Usage views. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).
