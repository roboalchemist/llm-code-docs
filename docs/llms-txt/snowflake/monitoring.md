# Source: https://docs.snowflake.com/en/connectors/servicenow/monitoring.md

# Source: https://docs.snowflake.com/en/developer-guide/native-apps/monitoring.md

# Source: https://docs.snowflake.com/en/developer-guide/declarative-sharing/monitoring.md

# Source: https://docs.snowflake.com/en/sql-reference/monitoring.md

# MONITORING schema

In the SNOWFLAKE database, the MONITORING schema contains views that provide historical usage data for your account.

## MONITORING views

The MONITORING schema provides the following views:

| View | Notes |
| --- | --- |
| [ICEBERG_ACCESS_ERRORS](monitoring/iceberg_access_errors.md) | Data is retained for 14 days. |

## Accessing views in the MONITORING schema

The MONITORING_VIEWER database role has the SELECT privilege on all views in the MONITORING schema.

The MONITORING_VIEWER database role is granted to the PUBLIC role in all Snowflake accounts containing a shared SNOWFLAKE
database.

## General usage notes

* The Snowflake-specific views are subject to change. Avoid selecting all columns from these views. Instead, select the columns that you want.
  For example, if you want the `name` column, use `SELECT name`, rather than `SELECT *`.
* The rows returned in a query of a view depend on the privileges granted to the user’s current role. When you query a view in
  the MONITORING schema, only objects for which the current role has been granted access privileges are returned.
