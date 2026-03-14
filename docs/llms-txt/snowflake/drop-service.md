# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-service.md

# DROP SERVICE

Removes the specified
[Snowpark Container Services service](../../developer-guide/snowpark-container-services/working-with-services.md) from the current
or specified schema. The containers for the service are terminated.

See also:
:   [CREATE SERVICE](create-service.md) , [ALTER SERVICE](alter-service.md), [SHOW SERVICES](show-services.md) , [DESCRIBE SERVICE](desc-service.md)

## Syntax

```sqlsyntax
DROP SERVICE [ IF EXISTS ] <name> [ FORCE ]
```

## Required parameters

`name`
:   Specifies the identifier for the service to be dropped.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Optional parameters

`FORCE`
:   Drops the service (including job services) and the associated block storage volumes.

    If `FORCE` is not specified and the service uses a
    [block storage volume](../../developer-guide/snowpark-container-services/block-storage-volume.md)
    an error is returned.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Service |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops the service named `my_tutorial`:

```sqlexample
DROP SERVICE my_tutorial;
```

```output
+-----------------------------------+
| status                            |
|-----------------------------------|
| MY_TUTORIAL successfully dropped. |
+-----------------------------------+
```
