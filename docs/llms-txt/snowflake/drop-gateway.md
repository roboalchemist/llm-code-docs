# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-gateway.md

# DROP GATEWAY

Removes the specified [gateway](../../developer-guide/snowpark-container-services/gateway.md) from the current
or specified schema.

See also:
:   [CREATE GATEWAY](create-gateway.md) , [ALTER GATEWAY](alter-gateway.md), [SHOW GATEWAYS](show-gateways.md) , [DESCRIBE GATEWAY](desc-gateway.md)

## Syntax

```sqlsyntax
DROP GATEWAY [ IF EXISTS ] <name>
```

## Required parameters

`name`
:   Specifies the identifier for the gateway to be dropped.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Gateway | Required to drop the gateway. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops the gateway named `split_gateway`:

```sqlexample
DROP GATEWAY split_gateway;
```

```output
+-------------------------------------+
| status                              |
|-------------------------------------|
| SPLIT_GATEWAY successfully dropped. |
+-------------------------------------+
```
