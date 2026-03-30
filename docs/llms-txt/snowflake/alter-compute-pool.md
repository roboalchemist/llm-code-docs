# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-compute-pool.md

# ALTER COMPUTE POOL

Modifies the properties of an existing
[compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

See also:
:   [CREATE COMPUTE POOL](create-compute-pool.md) , [DESCRIBE COMPUTE POOL](desc-compute-pool.md), [DROP COMPUTE POOL](drop-compute-pool.md) , [SHOW COMPUTE POOLS](show-compute-pools.md)

## Syntax

```sqlsyntax
ALTER COMPUTE POOL [ IF EXISTS ] <name> { SUSPEND | RESUME }

ALTER COMPUTE POOL [ IF EXISTS ] <name> STOP ALL  [ OF TYPE <workload_type> [ , ... ] ]

ALTER COMPUTE POOL [ IF EXISTS ] <name> SET [ MIN_NODES = <num> ]
                                            [ MAX_NODES = <num> ]
                                            [ AUTO_RESUME = { TRUE | FALSE } ]
                                            [ AUTO_SUSPEND_SECS = <num> ]
                                            [ PLACEMENT_GROUP = '<placement_group_name>' ]
                                            [ INSTANCE_FAMILY = <instance_family_name> ]
                                            [ TAG <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ]
                                            [ COMMENT = '<string_literal>' ]

ALTER COMPUTE POOL [ IF EXISTS ] <name> UNSET { AUTO_SUSPEND_SECS |
                                                AUTO_RESUME       |
                                                PLACEMENT_GROUP   |
                                                COMMENT
                                              }
                                              [ , ... ]
```

## Parameters

`name`
:   Specifies the identifier for the compute pool to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`{ SUSPEND | RESUME }`
:   Suspends a compute pool or resumes a previously suspended compute pool. When you suspend a compute pool, Snowflake suspends all services in that compute pool,
    but the jobs continue to run until they reach a terminal state (DONE or FAILED), after which the compute pool nodes are released.

`STOP ALL  OF TYPE workload_type [ , ... ]`
:   Drops all services and cancels jobs executing in the compute pool. Snowflake then removes all the containers from the compute pool. If the optional `OF TYPE` clause is specified, Snowflake only stops the services of the specified workload types. For a list of available workload types, see [ALLOWED_SPCS_WORKLOAD_TYPES](../parameters.md).

    The filter is case-insensitive.

`SET ...`
:   Sets one or more specified properties or parameters for the compute pool:

    `MIN_NODES = num`
    :   Specifies the minimum number of compute pool nodes.

    `MAX_NODES = num`
    :   Specifies the maximum number of compute pool nodes.

    `AUTO_RESUME = { TRUE | FALSE }`
    :   Specifies whether to automatically resume a compute pool when a service or job is submitted to it. If AUTO_RESUME is FALSE,
        you need to explicitly resume the compute pool (using ALTER COMPUTE POOL <name> RESUME) before you can start a service or
        job on the compute pool.

    `AUTO_SUSPEND_SECS = num`
    :   Number of seconds of inactivity after which you want Snowflake to automatically suspend the compute pool. Inactivity means
        no services and no jobs running on any node in the compute pool.

    `TAG tag_name = 'tag_value' [ , tag_name = 'tag_value' , ... ]`
    :   Specifies the [tag](../../user-guide/object-tagging/introduction.md) name and the tag string value.

        The tag value is always a string, and the maximum number of characters for the tag value is 256.

        For information about specifying tags in a statement, see [Tag quotas](../../user-guide/object-tagging/introduction.md).

    `PLACEMENT_GROUP = placement_group_name`
    :   Identifies the [placement group of the compute pool](../../developer-guide/snowpark-container-services/working-with-compute-pool.md). Use the [SHOW COMPUTE POOLS](show-compute-pools.md)
        and [DESCRIBE COMPUTE POOL](desc-compute-pool.md)
        commands to review the assignment of the compute pool into placement groups.

        You can also set `placement_group` to `DISTRIBUTED`. In this case, Snowflake attempts to distribute compute pool nodes across all available placement groups to maintain an even distribution across multiple placement groups so that the groups are more fault tolerant. For more information, see [Compute pool placement](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

    `INSTANCE_FAMILY = instance_family_name`
    :   Identifies the type of machine you want to provision for the nodes in the compute pool. The machine type determines the amount of compute resources in the compute pool and, therefore, the number of credits consumed while
        the compute pool is running. For a list of available instance family names, see [instance families](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

        INSTANCE_FAMILY can be altered only when a compute pool is fully suspended. Upon resuming, Snowflake uses the new instance type to provision the compute pool.

    `COMMENT = 'string_literal'`
    :   Specifies a comment for the compute pool.

`UNSET ...`
:   Specifies one or more properties and/or parameters to unset for the compute pool,
    which resets them to the defaults. For more information, see
    [CREATE COMPUTE POOL](create-compute-pool.md):

    * `AUTO_SUSPEND_SECS`
    * `AUTO_RESUME`
    * `PLACEMENT_GROUP`: The placement group can only be unset when the compute pool is fully suspended.
    * `COMMENT`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OPERATE | Compute pool | To suspend or resume a compute pool, the role requires these permissions. |
| MODIFY | Compute pool | To alter the compute pool and set properties, the role requires this permission. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example sets the MAX_NODES and AUTO_RESUME properties for a compute pool:

```sqlexample
ALTER COMPUTE POOL tutorial_compute_pool SET
  MAX_NODES = 5
  AUTO_RESUME = FALSE
```

The following example sets the “CPU_X64_S” as the INSTANCE_FAMILTY for a compute pool. Because the compute pool must be stopped to change the instance family, the compute pool is first suspended:

```sqlexample
ALTER COMPUTE POOL tutorial_compute_pool SUSPEND;
ALTER COMPUTE POOL tutorial_compute_pool SET
  INSTANCE_FAMILY = CPU_X64_S;
ALTER COMPUTE POOL tutorial_compute_pool RESUME;
```
