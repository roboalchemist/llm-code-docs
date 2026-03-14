# Source: https://docs.snowflake.com/en/sql-reference/info-schema/applicable_roles.md

# APPLICABLE_ROLES view

This Information Schema view displays one row for each role grant applied to the currently authenticated user.

For more information about roles and grants, see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

See also:
:   [ENABLED_ROLES view](enabled_roles.md) , [OBJECT_PRIVILEGES view](object_privileges.md) , [TABLE_PRIVILEGES view](table_privileges.md) , [GRANTS_TO_USERS view](../account-usage/grants_to_users.md) ,
    [GRANTS_TO_ROLES view](../account-usage/grants_to_roles.md) , [SHOW GRANTS](../sql/show-grants.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| GRANTEE | VARCHAR | Role or user to whom the privilege is granted |
| ROLE_NAME | VARCHAR | Name of the role |
| ROLE_OWNER | VARCHAR | Owner of the role |
| IS_GRANTABLE | VARCHAR | Whether this role can be granted to others |

## Usage notes

The view does not display any information about [database roles](../../user-guide/security-access-control-considerations.md).
