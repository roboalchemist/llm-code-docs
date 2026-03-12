# Source: https://docs.snowflake.com/en/sql-reference/functions/system_supported_dbt_versions.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$SUPPORTED_DBT_VERSIONS

Returns a JSON array containing the versions that Snowflake supports for dbt Projects.

For more information, see [Supported dbt Core versions for dbt Projects on Snowflake](../../user-guide/data-engineering/dbt-projects-on-snowflake-dbt-core-versions.md).

## Syntax

```sqlsyntax
SYSTEM$SUPPORTED_DBT_VERSIONS()
```

## Arguments

None.

## Returns

Returns a JSON array containing the versions that Snowflake supports for dbt Projects.

## Examples

To view supported versions for your dbt projects, run the following SQL command:

```sqlexample
SELECT SYSTEM$SUPPORTED_DBT_VERSIONS();
```

```output
[{"dbt_version":"1.9.4","type":"dbt Core"},{"dbt_version":"1.10.15","type":"dbt Core"}]
```
