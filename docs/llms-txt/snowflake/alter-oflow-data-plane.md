# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-oflow-data-plane.md

# ALTER OPENFLOW DATA PLANE

Modifies an Openflow data plane integration.

See also:
:   [DESCRIBE OPENFLOW DATA PLANE INTEGRATION](desc-oflow-data-plane-integration.md), [SHOW OPENFLOW DATA PLANE INTEGRATIONS](show-oflow-data-plane-integration.md),

## Syntax

```sqlsyntax
ALTER OPENFLOW DATA PLANE INTEGRATION <name>
    SET EVENT_TABLE = '<database>.<schema>.<tablename>';
```

## Parameters

`name`
:   Specifies the identifier (name) for the Openflow data plane integration being altered.

`SET ...`

> Specifies the properties to set for the DATA PLANE INTEGRATION.
>
> `EVENT_TABLE = 'event table name'`
> :   Fully qualified name of the event table to associate with the Openflow data plane integration.

## Usage notes

* Openflow data plane integrations cannot be created directly, but rather are created when a deployment is created.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP or MODIFY | On the OPENFLOW DATA PLANE INTEGRATION being modified. |  |

## Examples

Alter an OPENFLOW DATA PLANE INTEGRATION to specify a specific event table.

```sqlexample
SHOW OPENFLOW DATA PLANE INTEGRATIONS;

ALTER OPENFLOW DATA PLANE INTEGRATION OPENFLOW_DATAPLANE_63600E17_5D91_4C56_BFC8_54FA0AXXXXXX
    SET EVENT_TABLE = 'openflow.openflow.openflow_events';
```
