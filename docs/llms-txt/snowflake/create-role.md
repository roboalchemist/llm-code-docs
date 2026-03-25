# Source: https://docs.snowflake.com/en/sql-reference/sql/create-role.md

# CREATE ROLE

Create a new role or replace an existing role in the system.

After creating roles, you can grant object privileges to the role and then grant the role to other roles or individual users to enable
access control security for objects in the system.

This command supports the following variants:

* CREATE OR ALTER ROLE: Creates a role if it doesn’t exist or alters an existing role.

See also:
:   [GRANT <privileges> … TO ROLE](grant-privilege.md), [GRANT ROLE](grant-role.md) , [GRANT OWNERSHIP](grant-ownership.md) , [DROP ROLE](drop-role.md) , [ALTER ROLE](alter-role.md) , [SHOW ROLES](show-roles.md)

    [CREATE OR ALTER <object>](create-or-alter.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] ROLE [ IF NOT EXISTS ] <name>
  [ COMMENT = '<string_literal>' ]
  [ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
```

## Variant syntax

### CREATE OR ALTER ROLE

Creates a new role if it doesn’t already exist, or transforms an existing role into the role defined in the statement.
A CREATE OR ALTER ROLE statement follows the syntax rules of a CREATE ROLE statement and has the same limitations as an
[ALTER ROLE](alter-role.md) statement.

```sqlsyntax
CREATE OR ALTER ROLE <name>
  [ COMMENT = '<string_literal>' ]
```

For more information, see CREATE OR ALTER ROLE usage notes.

## Required parameters

`name`
:   Identifier for the role; must be unique for your account.

    The identifier must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`COMMENT = 'string_literal'`
:   Specifies a comment for the role.

    Default: No value

`TAG ( tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ] )`
:   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

    The tag value is always a string, and the maximum number of characters for the tag value is 256.

    For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE ROLE | Account | Only the USERADMIN role, or a higher role, has this privilege by default. The privilege can be granted to additional roles as needed. |
| OWNERSHIP | Database role | Required to execute a CREATE OR ALTER ROLE statement for an *existing* role.  OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## General usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## CREATE OR ALTER ROLE usage notes

* All limitations of the [ALTER ROLE](alter-role.md) command apply.
* Setting or unsetting a tag is not supported; however, existing tags are not altered by a CREATE OR ALTER ROLE statement and remain
  unchanged.

## Examples

```sqlexample
CREATE ROLE myrole;
```
