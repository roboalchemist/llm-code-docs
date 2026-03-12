# Source: https://docs.snowflake.com/en/sql-reference/sql/create-organization-user.md

# CREATE ORGANIZATION USER

Creates a new [organization user](../../user-guide/organization-users.md).

See also:
:   [ALTER ORGANIZATION USER](alter-organization-user.md) , [DROP ORGANIZATION USER](drop-organization-user.md) , [SHOW ORGANIZATION USERS](show-organization-users.md)

## Syntax

```sqlsyntax
CREATE ORGANIZATION USER [ IF NOT EXISTS ] <name>
  [ objectProperties ]
```

Where:

> ```sqlsyntax
> objectProperties ::=
>   EMAIL = '<string>'
>   LOGIN_NAME = '<string>'
>   DISPLAY_NAME = '<string>'
>   FIRST_NAME = '<string>'
>   MIDDLE_NAME = '<string>'
>   LAST_NAME = '<string>'
>   COMMENT = '<string>'
> ```

## Required parameters

`name`
:   Identifier for the organization user; must be unique for your organization.

    The identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`EMAIL = 'string'`
:   Email address of the user.

## Optional parameters

`LOGIN_NAME = 'string'`
:   Name that the user enters to log into the system. Login names for users must be unique across your entire organization. It cannot match the login name in a regular account that tries to import the organization user.

    A login name can be any string, including spaces and non-alphanumeric characters, such as exclamation points (`!`), percent signs
    (`%`), and asterisks (`*`); however, if the string contains spaces or non-alphanumeric characters, it must be enclosed in single
    or double quotes. Login names are always case insensitive.

    Snowflake allows specifying different user and login names to enable using common identifiers (for example, email addresses) for login.

    Default: User’s name/identifier (that is, if no value is specified, the value specified for `name` is used as the login name)

`DISPLAY_NAME = 'string'`
:   Name displayed for the user in the Snowflake web interface.

    Default: User’s name/identifier (that is, if no value is specified, the value specified for `name` is used as the display name)

`FIRST_NAME = 'string'` , . `MIDDLE_NAME = string` , . `LAST_NAME = 'string'`
:   First, middle, and last name of the user.

    Default: `NULL`

`COMMENT = 'string'`
:   Description of the user.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ORGANIZATION USER | ACCOUNT | By default, only the GLOBALORGADMIN and USERADMIN system roles in the organization account have this privilege. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

Create an organization user and set the EMAIL property:

```sqlexample
CREATE ORGANIZATION USER joe EMAIL = 'joe.davis@example.com';
```
