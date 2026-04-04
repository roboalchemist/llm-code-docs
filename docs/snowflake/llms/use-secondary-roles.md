# Source: https://docs.snowflake.com/en/sql-reference/sql/use-secondary-roles.md

# USE SECONDARY ROLES

Specifies the active/current secondary roles for the session. The currently-active secondary roles set the context that determines whether
the current user has the necessary privileges to perform SQL actions.

Note that authorization to execute [CREATE <object>](create.md) statements to create objects is provided by the primary role.

For more information, see [secondary role enforcement](../../user-guide/security-access-control-overview.md).

See also:
:   [USE ROLE](use-role.md)

## Syntax

```sqlsyntax
USE SECONDARY ROLES {
      ALL
    | NONE
    | <role_name> [ , <role_name> ... ]
  }
```

## Parameters

`ALL`
:   All roles that have been granted to the user in addition to the current active primary role.

    Note that the set of roles is reevaluated when each SQL statement executes. If additional roles are granted to the user, and that user
    executes a new SQL statement, the newly granted roles are active secondary roles for the new SQL statement. The same logic applies to
    roles that are revoked from a user.

`NONE`
:   Disables secondary roles. The authorization for all SQL actions is provided via the primary role.

`role_name [ , role_name ... ]`
:   Activates the specified roles as secondary roles. The secondary roles can be user-defined account roles or system roles. Specify the role
    name as it is stored in Snowflake.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Usage notes

To use a role, the role must have been granted to the user.

## Examples

```sqlexample
USE SECONDARY ROLES ALL;
```

```sqlexample
USE SECONDARY ROLES test_role_1, test_role_2;
```
