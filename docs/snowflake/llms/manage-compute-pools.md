# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/services/manage-compute-pools.md

# Managing compute pools

A compute pool is a collection of one or more virtual machine (VM) nodes on which Snowflake runs your
Snowpark Container Services jobs and services.

For more information about compute pools, see [Snowpark Container Services: Working with compute pools](../../snowpark-container-services/working-with-compute-pool.md).

This topic shows how to do the following tasks with services:

* Create a compute pool
* Create a compute pool from a project definition
* Suspend and resume a compute pool
* Set and unset a compute pool’s properties or parameters
* Stop all services in a compute pool

For common operations, such as listing or dropping, Snowflake CLI uses `snow object` commands as described in [Managing Snowflake objects](../objects/manage-objects.md).

## Create a compute pool

To create a compute pool named “pool_1” composed of two CPUs with 4 GB of memory, enter a
[spcs pool create](../command-reference/spcs-commands/compute-pool-commands/create.md) command similar to the following:

```snowcli
snow spcs compute-pool create "pool_1" --min-nodes 2 --max-nodes 2 --family "CPU_X64_XS"
```

For more information about instance families, see the SQL `CREATE COMPUTE POOL` command.

## Create a compute pool from a project definition

You can create a compute pool from a `snowflake.yml` project definition file and then executing the `snow spcs compute-pool deploy` command.

The following shows a sample `snowflake.yml` project definition file:

```yaml
definition_version: 2
entities:
  my_compute_pool:
    type: compute-pool
    identifier:
      name: my_compute_pool
    min_nodes: 1
    max_nodes: 2
    instance_family: CPU_X64_XS
    auto_resume: true
    initially_suspended: true
    auto_suspend_seconds: 60
    comment: "My compute pool"
    tags:
      - name: my_tag
        value: tag_value
```

The following table describes the properties of a compute pool project definition.

Compute pool project definition properties

| Property | Definition |
| --- | --- |
| **type**  *required*, *string* | Must be `compute-pool`. |
| **identifier**  *optional*, *string* | Snowflake identifier for the entity. The value can have the following forms:   *String identifier text  ```yaml   identifier: my-compute-pool```  Both unquoted and quoted identifiers are supported. To use quoted identifiers, include the surrounding quotes in the YAML value (for example, `"My Compute Pool"`).* Object  ```yaml   identifier:     name: my-compute-pool     schema: my-schema # optional     database: my-db # optional```  **Note:** An error occurs if you specify a `schema` or `database` and use a fully qualified name in the `name` property (such as `mydb.schema1.my-app`). |
| **instance_family**  *required*, *string* | Name of the instance family. For a list of available instance families, see the [CREATE COMPUTE POOL INSTANCE_FAMILY](../../../sql-reference/sql/create-compute-pool.md) parameter. |
| **min_nodes**  *optional*, *string* | Minimum number of nodes for the compute pool. This value must be greater than 0.  Default: `1` |
| **max_nodes**  *optional*, *int* | Maximum number of nodes for the compute pool. |
| **auto_resume**  *optional*, *boolean* | Whether to automatically resume a compute pool when a service or job is submitted to it.  Default: `True` |
| **initially_suspended**  *optional*, *boolean* | Whether the compute pool is created initially in the suspended state. If `true`, Snowflake doesn’t provision any nodes requested for the compute pool at the compute pool creation time.  Default: `False` |
| **auto_suspend_seconds**  *optional*, *int* | Number of seconds of inactivity after which you want Snowflake to automatically suspend the compute pool.  Default: `3600` |
| **comment**  *optional*, *string* | Comments to associate with the compute pool. |
| **tags**  *optional*, *Tag sequence* | Tag names and values for the compute pool. For more information, see [Tag quotas](../../../user-guide/object-tagging/introduction.md) |

To create and deploy the compute pool to a stage, do the following:

1. Change your current directory to the directory containing the project definition file.
2. Run a `snow spcs compute-pool deploy` command similar to the following:

   ```snowcli
   snow spcs compute-pool deploy
   ```

   ```output
   +---------------------------------------------------------------------+
   | key    | value                                                      |
   |--------+------------------------------------------------------------|
   | status | Compute pool MY_COMPUTE_POOL successfully created.         |
   +---------------------------------------------------------------------+
   ```

## Suspend and resume a compute pool

> **Note:**
>
> The current role must have OPERATE privilege on the compute pool to suspend or resume it.

To suspend a compute pool, enter a command similar to the following:

```snowcli
snow spcs compute-pool suspend tutorial_compute_pool
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

To resume a suspended compute pool, enter a command similar to the following:

```snowcli
snow spcs compute-pool resume tutorial_compute_pool
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

## Set and unset a compute pool’s properties or parameters

> **Note:**
>
> The current role must have MODIFY privilege on the compute pool to set properties.

To set a property or parameter, enter a command similar to the following:

```snowcli
snow spcs compute-pool set tutorial_compute_pool --min-nodes 2 --max-nodes 4
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

To reset a property or parameter to its default value, enter a command similar to the following:

```snowcli
snow spcs compute-pool unset tutorial_compute_pool --auto-resume
```

```output
+-------------------------------------------+
| key    | value                            |
|--------+----------------------------------|
| status | Statement executed successfully. |
+-------------------------------------------+
```

## Stop all services in a compute pool

Stopping a compute pool deletes all of the services running on the compute pool; however, it does not stop the compute pool itself.

To stop a compute pool, enter a [spcs compute-pool stop-all](../command-reference/spcs-commands/compute-pool-commands/stop-all.md) command similar to the following:

```snowcli
snow spcs compute-pool stop-all "pool_1"
```
