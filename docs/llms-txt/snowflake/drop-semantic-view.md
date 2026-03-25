# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-semantic-view.md

# DROP SEMANTIC VIEW

Removes the specified [semantic view](../../user-guide/views-semantic/overview.md) from the current/specified schema.

See also:
:   [CREATE SEMANTIC VIEW](create-semantic-view.md) , [ALTER SEMANTIC VIEW](alter-semantic-view.md) , [DESCRIBE SEMANTIC VIEW](desc-semantic-view.md) , [SHOW SEMANTIC VIEWS](show-semantic-views.md) , [SHOW SEMANTIC DIMENSIONS](show-semantic-dimensions.md) , [SHOW SEMANTIC DIMENSIONS FOR METRIC](show-semantic-dimensions-for-metric.md) , [SHOW SEMANTIC FACTS](show-semantic-facts.md) , [SHOW SEMANTIC METRICS](show-semantic-metrics.md)

## Syntax

```sqlsyntax
DROP SEMANTIC VIEW [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the semantic view to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Semantic view | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following example drops the semantic view named `my_semantic_view`:

```sqlexample
DROP SEMANTIC VIEW my_semantic_view;
```
