# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-compute-pool.md

# DROP COMPUTE POOL

Removes the specified [compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md) from the
account.

See also:
:   [CREATE COMPUTE POOL](create-compute-pool.md) , [ALTER COMPUTE POOL](alter-compute-pool.md), [DESCRIBE COMPUTE POOL](desc-compute-pool.md) , [SHOW COMPUTE POOLS](show-compute-pools.md)

## Syntax

```sqlsyntax
DROP COMPUTE POOL [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the compute pool to be dropped.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Compute pool |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When dropping a compute pool, Snowflake automatically aborts any running jobs. However, Snowflake does not drop running services.
  If services are running this command will fail. You need to explicitly drop all running services before dropping a compute pool.
  You can run [ALTER COMPUTE POOL … STOP ALL](alter-compute-pool.md), which drops both services and jobs. You can also use
  the [DROP SERVICE](drop-service.md) command to drop individual services.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops the compute pool named `tutorial_compute_pool`:

```sqlexample
DROP COMPUTE POOL tutorial_compute_pool;
```

```output
+---------------------------------------------+
| status                                      |
|---------------------------------------------|
| TUTORIAL_COMPUTE_POOL successfully dropped. |
+---------------------------------------------+
```
