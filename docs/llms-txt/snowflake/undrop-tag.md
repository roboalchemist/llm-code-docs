# Source: https://docs.snowflake.com/en/sql-reference/sql/undrop-tag.md

# UNDROP TAG

Restores the most recent version of a tag to the system.

For details about this command and tag references, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

See also:
:   [CREATE TAG](create-tag.md) , [ALTER TAG](alter-tag.md) , [DROP TAG](drop-tag.md) , [SHOW TAGS](show-tags.md)

## Syntax

```sqlsyntax
UNDROP TAG <name>
```

## Parameters

`name`
:   Identifier for the tag.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire
    identifier string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Tag | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on tag DDL and privileges, see [Access control privileges](../../user-guide/object-tagging/work.md).

## Usage notes

* Restoring tags is only supported in the current schema or current database, even if the table name is fully-qualified.
* If the tag was assigned to one or more objects when the [DROP TAG](drop-tag.md) command was executed, the UNDROP command
  restores the tag assignments to the objects. For details, see [Tag quotas](../../user-guide/object-tagging/introduction.md).
* If a tag with the same name already exists, an error is returned.

* UNDROP relies on the Snowflake [Time Travel](../../user-guide/data-time-travel.md) feature. An object can be restored only if
  the object was deleted within the [Data retention period](../../user-guide/data-time-travel.md). The default value is 24 hours.

## Example

The following example restores the most recent version of the tag named `cost_center`:

> ```sqlexample
> UNDROP TAG cost_center;
> ```
