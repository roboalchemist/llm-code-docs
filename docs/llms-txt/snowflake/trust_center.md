# Source: https://docs.snowflake.com/en/sql-reference/trust_center.md

# TRUST_CENTER schema

In the SNOWFLAKE database, the TRUST_CENTER schema contains views that contain data about the
[Trust Center extensions](../user-guide/trust-center/trust-center-extensions.md).

## TRUST_CENTER views

The TRUST_CENTER schema provides the following views:

| View | Notes |
| --- | --- |
| [EXTENSIONS](trust_center/extensions.md) | Data is retained for 14 days. |

## Accessing views in the TRUST_CENTER schema

The SNOWFLAKE.TRUST_CENTER_VIEWER or SNOWFLAKE.TRUST_CENTER_ADMIN application role can execute SELECT
operations on the views in this schema.

## General usage notes

* The Snowflake-specific views are subject to change. Avoid selecting all columns from these views. Instead, select the columns that you want.
  For example, if you want the `name` column, use `SELECT name`, rather than `SELECT *`.
* The rows that are returned in a query of a view depend on the privileges that are granted to the user’s current role.
  When you query a view in the TRUST_CENTER schema, only objects for which the current role is granted access
  privileges are returned.
