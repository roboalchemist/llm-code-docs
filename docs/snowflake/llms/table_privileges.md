# Source: https://docs.snowflake.com/en/sql-reference/info-schema/table_privileges.md

# TABLE_PRIVILEGES view

This Information Schema view displays a row for each table privilege that has been granted to each role in the specified (or current) database.

For more information about roles and privileges, see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

See also:
:   [APPLICABLE_ROLES view](applicable_roles.md) , [ENABLED_ROLES view](enabled_roles.md) , [OBJECT_PRIVILEGES view](object_privileges.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| GRANTOR | VARCHAR | Role who granted the table privilege |
| GRANTEE | VARCHAR | Role to whom the table privilege is granted |
| GRANTED_TO | VARCHAR | Type of object that has been granted the privilege |
| TABLE_CATALOG | VARCHAR | Database containing the table on which the privilege is granted |
| TABLE_SCHEMA | VARCHAR | Schema containing the table on which the privilege is granted |
| TABLE_NAME | VARCHAR | Name of the table on which the privilege is granted |
| PRIVILEGE_TYPE | VARCHAR | Type of the granted privilege |
| IS_GRANTABLE | VARCHAR | Whether the privilege was granted WITH GRANT OPTION |
| WITH_HIERARCHY | VARCHAR | Not applicable for Snowflake. |
| CREATED | TIMESTAMP_LTZ | Creation time of the privilege |

## Usage notes

* The view only displays objects for which the current role for the session has been granted access privileges.
* The PRIVILEGE_TYPE column contains Snowflake privilege types. For example, the owner of a table has the OWNERSHIP privilege, rather than each of the separate privileges (e.g. SELECT, INSERT, DELETE,
  UPDATE).
