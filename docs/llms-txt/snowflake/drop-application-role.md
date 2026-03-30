# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-application-role.md

# DROP APPLICATION ROLE

Removes the specified application role from the system.

See also:
:   [CREATE APPLICATION ROLE](create-application-role.md) , [ALTER APPLICATION ROLE](alter-application-role.md) , [SHOW APPLICATION ROLES](show-application-roles.md)

## Syntax

```sqlsyntax
DROP APPLICATION ROLE [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the application role to drop. If the identifier contains spaces or
    special characters, the entire string must be enclosed in double quotes. Identifiers enclosed
    in double quotes are also case-sensitive.

## Usage notes

* This command can only be run within the context of an application created using the Native
  App Framework.
* Dropped application roles cannot be recovered; they must be recreated within the application.
* Application roles are not versioned. When dropping an application role from a setup script,
  you must ensure that no running version of the application relies upon the role being
  dropped. Snowflake recommends to either avoid dropping application roles that may be in use or to
  wait until the version that depends on the role being dropped has itself also been
  dropped.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

> ```sqlexample
> DROP APPLICATION ROLE APP_ROLE;
> ```
