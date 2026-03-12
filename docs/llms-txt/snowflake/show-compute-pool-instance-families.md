# Source: https://docs.snowflake.com/en/sql-reference/sql/show-compute-pool-instance-families.md

# SHOW COMPUTE POOL INSTANCE FAMILIES

Lists the available [compute pool instance families](../../developer-guide/snowpark-container-services/working-with-compute-pool.md)
that you can use to create a compute pool.

See also:
:   [CREATE COMPUTE POOL](create-compute-pool.md) , [ALTER COMPUTE POOL](alter-compute-pool.md)

## Syntax

```sqlsyntax
SHOW COMPUTE POOL INSTANCE FAMILIES
```

## Output

The command output provides compute pool instance family properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `name` | Instance family name. |
| `description` | Instance family description. |
| `vcpu` | Number of vCPUs that are accessible to the user. |
| `memory_gib` | Memory in GiB that is accessible to the user. |
| `storage_gib` | Storage in GiB that is accessible to the user. |
| `gpu` | Name of the GPU if applicable, else an empty string. |
| `gpu_count` | Count of GPUs if applicable, else 0. |
| `gpu_memory_gib` | GPU Memory available per GPU if applicable, else 0. |
| `current_node_usage` | Number of nodes of this type currently in use by your Snowflake account. |
| `message` | Additional information about the instance family. |

## Examples

The following command lists the compute pool instance families:

```sqlexample
SHOW COMPUTE POOL INSTANCE FAMILIES;
```
