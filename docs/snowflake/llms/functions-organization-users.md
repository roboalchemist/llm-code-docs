# Source: https://docs.snowflake.com/en/sql-reference/functions-organization-users.md

# Organization user and organization user group functions

The following functions help you work with [organization users and organization user groups](../user-guide/organization-users.md).

| Function | Description |
| --- | --- |
| [CURRENT_ORGANIZATION_USER](functions/current_organization_user.md) | Indicates whether the current user in the session was imported from an organization user. |
| [IS_ORGANIZATION_USER](functions/is_organization_user.md), . [IS_USER_IMPORTED (SYS_CONTEXT function)](functions/is_user_imported.md) | Tests whether a specific user was imported from an organization user. |
| [IS_ORGANIZATION_USER_GROUP](functions/is_organization_user_group.md), . [IS_GROUP_IMPORTED (SYS_CONTEXT function)](functions/is_group_imported.md) | Tests whether a specific role was imported from an organization user group. |
| [IS_ORGANIZATION_USER_GROUP_IN_SESSION](functions/is_organization_user_group_in_session.md), . [IS_GROUP_ACTIVATED (SYS_CONTEXT function)](functions/is_group_activated.md) | Tests whether a specific imported role is in the role hierarchy of the user’s current session. |
| [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](functions/sys_context_snowflake_organization.md) | Returns information about organization users and organization user groups. |
| [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION_SESSION namespace)](functions/sys_context_snowflake_organization_session.md) | Returns information about the current session and the current organization user in the session. |
| [SYSTEM$LINK_ORGANIZATION_USER](functions/system_link_organization_user.md) | Links an organization user with an existing user object so it can be managed as an organization user going forward. |
| [SYSTEM$LINK_ORGANIZATION_USER_GROUP](functions/system_link_organization_user_group.md) | Links an organization user group with an existing access control role so it can be managed as a organization user group going forward. |
| [SYSTEM$UNLINK_ORGANIZATION_USER](functions/system_unlink_organization_user.md) | Unlinks a user object from an organization user so it can be managed as a local user going forward. |
| [SYSTEM$UNLINK_ORGANIZATION_USER_GROUP](functions/system_unlink_organization_user_group.md) | Unlinks an access control role from an organization user group so it can be managed as a local role going forward. |
