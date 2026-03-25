# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-tag.md

# DROP TAG

Removes a tag from the system.

For information about this command and tag references, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

See also:
:   [CREATE TAG](create-tag.md) , [ALTER TAG](alter-tag.md) , [SHOW TAGS](show-tags.md) , [UNDROP TAG](undrop-tag.md)

## Syntax

```sqlsyntax
DROP TAG [ IF EXISTS ] <name>
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

* Prior to dropping a tag, determine all of the objects the tag is assigned to by calling the Account Usage table function
  [TAG_REFERENCES_WITH_LINEAGE](../functions/tag_references_with_lineage.md).
* A tag can be dropped if it is currently assigned to an [object](../../user-guide/object-tagging/introduction.md). If dropping the tag was
  unintentional, execute an [UNDROP TAG](undrop-tag.md) command. Note that the UNDROP TAG command restores the tag assignments
  prior to the DROP TAG operation.
* A tag cannot be dropped if a masking policy is [assigned](alter-tag.md) to the tag.

  In this scenario, unset the masking policy from the tag first and then execute the DROP TAG statement.
* For more information on tag DDL authorization, see [required privileges](../../user-guide/object-tagging/work.md).

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Example

The following example drops a tag:

> ```sqlexample
> DROP TAG cost_center;
> ```
