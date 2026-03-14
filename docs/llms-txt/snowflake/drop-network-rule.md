# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-network-rule.md

# DROP NETWORK RULE

Removes the specified network rule from the system.

See also:
:   [CREATE NETWORK RULE](create-network-rule.md) , [ALTER NETWORK RULE](alter-network-rule.md) , [SHOW NETWORK RULES](show-network-rules.md) , [DESCRIBE NETWORK RULE](desc-network-rule.md)

## Syntax

```sqlsyntax
DROP NETWORK RULE [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the network rule to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in
    double quotes are case-sensitive.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Network Rule | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Dropped network rules can’t be recovered; they must be recreated.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop a network rule named `myrule`:

> ```sqlexample
> DROP NETWORK RULE myrule;
> ```
