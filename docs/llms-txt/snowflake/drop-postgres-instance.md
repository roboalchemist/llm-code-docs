# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-postgres-instance.md

# DROP POSTGRES INSTANCE

Removes the specified [Snowflake Postgres instance](../../user-guide/snowflake-postgres/about.md) from the account.

See also:
:   [CREATE POSTGRES INSTANCE](create-postgres-instance.md), [ALTER POSTGRES INSTANCE](alter-postgres-instance.md), [DESCRIBE POSTGRES INSTANCE](desc-postgres-instance.md), [SHOW POSTGRES INSTANCES](show-postgres-instances.md)

## Syntax

```sqlsyntax
DROP POSTGRES INSTANCE [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the Postgres instance to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Postgres instance |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Currently, dropped Postgres instances can’t be recovered; you must recreate them. However, if you have
  created a [fork](../../user-guide/snowflake-postgres/postgres-point-in-time-recovery.md) of the instance,
  the fork remains independent and unaffected. To make it easier to recreate instances later, you might use
  DESC POSTGRES INSTANCE to capture the details of each instance before dropping it.
* When this command is issued, Snowflake terminates the Postgres instance and releases the associated compute resources.
  Billing for compute resources stops after the instance is fully terminated.
* All data stored in the Postgres instance is permanently deleted. Ensure you have backed up any important data
  before dropping the instance.
* If the instance has [high availability](../../user-guide/snowflake-postgres/high-availability.md) enabled, the
  HA standby is also dropped along with the primary instance.
* If the instance has [read replicas](../../user-guide/snowflake-postgres/postgres-create-replica.md), those replicas
  are also dropped when the primary instance is dropped.
* [Forked instances](../../user-guide/snowflake-postgres/postgres-point-in-time-recovery.md) are independent copies.
  Dropping the source instance doesn’t affect any instances that were forked from it.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop a Postgres instance:

```sqlexample
DROP POSTGRES INSTANCE my_postgres;
```

Drop a Postgres instance only if it exists:

```sqlexample
DROP POSTGRES INSTANCE IF EXISTS my_postgres;
```

Use the [flow operator](../operators-flow.md) to find an instance to drop:

```sqlexample
-- Find the oldest instance
-- Then use SET and IDENTIFIER() to drop it
SET oldest_instance = (
  SHOW POSTGRES INSTANCES
    ->> SELECT "name"
        FROM $1
        ORDER BY "created_on"
        LIMIT 1
);

DROP POSTGRES INSTANCE IDENTIFIER($oldest_instance);
```

Find instances below a storage threshold before dropping:

```sqlexample
-- Identify small instances
SHOW POSTGRES INSTANCES
  ->> SELECT "name", "storage_size", "created_on"
      FROM $1
      WHERE "storage_size" < 50
      ORDER BY "storage_size";

DROP POSTGRES INSTANCE some_extremely_small_instance;
```

Check ownership before attempting to drop:

```sqlexample
SHOW GRANTS ON POSTGRES INSTANCE my_postgres;

-- Verify that you have OWNERSHIP privilege, then drop
DROP POSTGRES INSTANCE my_postgres;
```
