# Source: https://docs.snowflake.com/en/sql-reference/functions/system_get_instance_family_placement_groups.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$GET_INSTANCE_FAMILY_PLACEMENT_GROUPS

Returns the list of placement groups supported for the specified
[instance family](../../developer-guide/snowpark-container-services/working-with-compute-pool.md)
for [Snowpark Container Services compute pool nodes](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).

## Syntax

```sqlsyntax
SYSTEM$GET_INSTANCE_FAMILY_PLACEMENT_GROUPS( '<instance_family>' )
```

## Arguments

`'instance_family'`
:   Instance family.

## Returns

Returns a VARCHAR value that contains the supported placement groups
formatted as a JSON array.

## Usage notes

* The returned list of placement group names is specific to your Snowflake account and the specified
  instance family. For more information, see [Compute pool placement](../../developer-guide/snowpark-container-services/working-with-compute-pool.md).
* Results don’t guarantee capacity. You might still run into insufficient capacity errors in a placement
  group even if an instance family is supported there.

## Examples

The following function returns the supported placement groups for the `GPU_NV_L` instance family:

```sqlexample
SELECT SYSTEM$GET_INSTANCE_FAMILY_PLACEMENT_GROUPS('GPU_NV_L');
```

Example output:

```output
+--------------------------------------------------------------+
| SYSTEM$GET_INSTANCE_FAMILY_PLACEMENT_GROUPS('GPU_NV_L')      |
|--------------------------------------------------------------|
| ["A","B","C","D"]                                            |
+--------------------------------------------------------------+
```

The `GPU_NV_L` instance family is available in the following placement
groups: `A`, `B`, `C` and `D`.
