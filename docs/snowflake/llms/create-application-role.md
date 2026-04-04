# Source: https://docs.snowflake.com/en/sql-reference/sql/create-application-role.md

# CREATE APPLICATION ROLE

Creates a new application role or replaces an existing application role. Use application roles to
enable access control security for objects within an application object.

See [About application roles](../../developer-guide/native-apps/creating-setup-script.md) for more information.

> **Note:**
>
> Application roles are only valid within the context of an application object.

When creating an application role, you can grant privileges on objects to the application role.
Within the setup script, you can then grant the application role to other application roles.

After installing a Snowflake Native App, consumers can grant application roles to account roles to
enable access to the app.

With application roles, you can grant privileges on other objects within the application or
objects owned by the application in the consumer account.

Application roles are implicitly granted to the application owner WITH GRANT OPTION. The
application owner may grant these roles to account level roles, providing access to the
objects that are owned by the application.

Additionally, this command supports the following variants:

* CREATE OR ALTER APPLICATION ROLE: Creates a new application role if it doesn’t exist or
  alters an existing application role.

See also:
:   [ALTER APPLICATION ROLE](alter-application-role.md), [GRANT APPLICATION ROLE](grant-application-role.md),
    [REVOKE APPLICATION ROLE](revoke-application-role.md), [SHOW APPLICATION ROLES](show-application-roles.md), [CREATE OR ALTER <object>](create-or-alter.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] APPLICATION ROLE [ IF NOT EXISTS ] <name>
  [ COMMENT = '<string_literal>' ]
```

## Variant syntax

### CREATE OR ALTER APPLICATION ROLE

Creates a new application role if it doesn’t already exist, or transforms an existing application role
into the role defined in the statement. A CREATE OR ALTER APPLICATION ROLE statement follows the syntax rules of a
CREATE APPLICATION ROLE statement and has the same limitations as an [ALTER APPLICATION ROLE](alter-application-role.md)
statement.

```sqlsyntax
CREATE OR ALTER APPLICATION ROLE <name>
  [ COMMENT = '<string_literal>' ]
```

For more information, see CREATE OR ALTER APPLICATION ROLE usage notes.

## Required parameters

`name`
:   Specifies the identifier for the application role. This value must be unique within the application object
    in which the role is created.

    The identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    If the identifier is not fully qualified, in the form of `application_name.application_role_name`, the command creates the
    application role in the current application for the session.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the application role.

    Default: No value

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Application role | Required to execute a CREATE OR ALTER APPLICATION ROLE statement for an *existing* application role.  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## General usage notes

* The maximum number of application roles that can be created in an application object is 1000.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## CREATE OR ALTER APPLICATION ROLE usage notes

* All limitations of the [ALTER APPLICATION ROLE](alter-application-role.md) command apply.
* Setting or unsetting a tag is not supported; however, existing tags are not altered by a CREATE
  OR ALTER APPLICATION ROLE statement and remain unchanged.

## Examples

```sqlexample
CREATE APPLICATION ROLE app_role
  COMMENT = 'Application role for the Hello Snowflake application.';
```
