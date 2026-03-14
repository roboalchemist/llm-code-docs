# Source: https://docs.snowflake.com/en/sql-reference/sql/create-session-policy.md

# CREATE SESSION POLICY

Creates a new session policy or replaces an existing session policy.

A session policy defines the idle session timeout period in minutes. Administrators can optionally set different timeout values for the
Snowflake web interface and other Snowflake clients.

After creating a session policy, apply the session policy to your Snowflake account using an [ALTER ACCOUNT](alter-account.md)
statement or a user using an [ALTER USER](alter-user.md) statement.

See also:
:   [Session Policy DDL Reference](../../user-guide/session-policies-managing.md)

## Syntax

```sqlsyntax
CREATE [OR REPLACE] SESSION POLICY [IF NOT EXISTS] <name>
  [ SESSION_IDLE_TIMEOUT_MINS = <integer> ]
  [ SESSION_UI_IDLE_TIMEOUT_MINS = <integer> ]
  [ ALLOWED_SECONDARY_ROLES = ( [ { 'ALL' | <role_name> [ , <role_name> ... ] } ] ) ]
  [ BLOCKED_SECONDARY_ROLES = ( [ { 'ALL' | <role_name> [ , <role_name> ... ] } ] ) ]
  [ COMMENT = '<string_literal>' ]
```

## Required parameters

`name`
:   Identifier for the session policy; must be unique for your account.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`SESSION_IDLE_TIMEOUT_MINS = integer`
:   For Snowflake clients and programmatic clients, the number of minutes in which a session can be idle before users must authenticate to
    Snowflake again. If a value is not specified, Snowflake uses the default value.

    The number of minutes can be any integer between `5` and `1440`, inclusive.

    Default: `240` (4 hours)

`SESSION_UI_IDLE_TIMEOUT_MINS = integer`
:   For Snowsight, the number of minutes in which a session can be idle before a user must authenticate to Snowflake again. If a
    value is not specified, Snowflake uses the default value.

    The number of minutes can be any integer between `5` and `1440`, inclusive.

    Default: `240` (4 hours)

`ALLOWED_SECONDARY_ROLES = ( [ { 'ALL' | role_name [ , role_name ... ] } ] )`
:   Specifies the allowed secondary roles for a session policy, if any.

    The possible values for the property are:

    `()`
    :   Disallows secondary roles.

    `('ALL')`
    :   Allows all secondary roles.

    `( role_name [ , role_name ... ] )`
    :   Allows the specified roles as secondary roles. The secondary roles can be user-defined account roles or system roles. Specify the
        role name as it is stored in Snowflake. For details, see [Identifier requirements](../identifiers-syntax.md).

    Default: `('ALL')`. If you do not set the property when you create a new session policy, all secondary roles are allowed.

`BLOCKED_SECONDARY_ROLES = ( [ { 'ALL' | role_name [ , role_name ... ] } ] )`
:   Specifies the blocked secondary roles for a session policy, if any. Blocked secondary roles take precedence over
    allowed secondary roles.

    The possible values for the property are:

    `()`
    :   Allows all secondary roles.

    `('ALL')`
    :   Disallows secondary roles.

    `( role_name [ , role_name ... ] )`
    :   Blocks the specified roles as secondary roles. The specified roles, and the roles granted to those roles, cannot be
        activated as secondary roles. These blocked roles can be user-defined account roles or system roles. Specify the
        role name as it is stored in Snowflake. For details, see [Identifier requirements](../identifiers-syntax.md).

    Default: `()`. If you do not set the property when you create a new session policy, all secondary roles are allowed.

`COMMENT = 'string_literal'`
:   Adds a comment or overwrites an existing comment for the session policy.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE SESSION POLICY | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on session policy DDL and privileges, see [Managing session policies](../../user-guide/session-policies-managing.md).

## Usage notes

* If you want to replace an existing session policy and need to see the current definition of the policy, call the
  [GET_DDL](../functions/get_ddl.md) function or run the [DESCRIBE SESSION POLICY](desc-session-policy.md) command.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

Create a session policy for your current account:

> ```sqlexample
> CREATE SESSION POLICY session_policy_prod_1
>   SESSION_IDLE_TIMEOUT_MINS = 30
>   SESSION_UI_IDLE_TIMEOUT_MINS = 30
>   COMMENT = 'session policy for use in the prod_1 environment'
> ;
> ```
