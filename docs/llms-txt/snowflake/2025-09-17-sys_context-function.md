# Source: https://docs.snowflake.com/en/release-notes/2025/other/2025-09-17-sys_context-function.md

# Sep 17, 2025: New SYS_CONTEXT function for getting context about applications, sessions, and organizations

You can call the new [SYS_CONTEXT](../../../sql-reference/functions/sys_context.md) function to get context information about:

* [The current application](../../../sql-reference/functions/sys_context_snowflake_application.md)
* [The current environment](../../../sql-reference/functions/sys_context_snowflake_environment.md) (for example, the current account or
  region)
* [The current session](../../../sql-reference/functions/sys_context_snowflake_session.md)

For example, you can:

* Determine if an application role is activated.
* Identify the client, driver, or library that is calling the function.
* Determine if the function is being called by a person, task, or SPCS service.

You can also get context information about
[organizations](../../../sql-reference/functions/sys_context_snowflake_organization.md), including information about the
[organization information related to the session](../../../sql-reference/functions/sys_context_snowflake_organization_session.md). For
example, you can:

* Determine if an organization user or group has been imported.
* Determine if the role representing an organization user group is activated.
* Identify the name of the organization user who started the session.

> **Note:**
>
> Getting context information about organizations is in [Preview](../../preview-features.md).

For more information, see [SYS_CONTEXT](../../../sql-reference/functions/sys_context.md).
