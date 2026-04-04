# Source: https://docs.snowflake.com/en/sql-reference/info-schema/enabled_roles.md

# ENABLED_ROLES view

This Information Schema view displays a row for each currently-enabled role in the session. A role is enabled if it is currently in use in the session or it has been granted to the role that is currently
in use.

For more information about roles, see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

See also:
:   [APPLICABLE_ROLES view](applicable_roles.md) , [OBJECT_PRIVILEGES view](object_privileges.md) , [TABLE_PRIVILEGES view](table_privileges.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ROLE_NAME | VARCHAR | Name of the role |
| ROLE_OWNER | VARCHAR | Owner of the role |

## Usage notes

* The view only displays objects for which the current role for the session has been granted access privileges.
* The view always displays the PUBLIC role because it is always enabled.
* The view does not display any information about [database roles](../../user-guide/security-access-control-considerations.md).
