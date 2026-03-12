# Source: https://docs.prefect.io/integrations/prefect-dbt/api-ref/prefect_dbt-cli-configs-postgres.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# postgres

# `prefect_dbt.cli.configs.postgres`

Module containing models for Postgres configs

## Classes

### `PostgresTargetConfigs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cli/configs/postgres.py#L16" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Target configs contain credentials and
settings, specific to Postgres.
To find valid keys, head to the [Postgres Profile](https://docs.getdbt.com/reference/warehouse-profiles/postgres-profile)
page.

**Attributes:**

* `credentials`: The credentials to use to authenticate; if there are
  duplicate keys between credentials and TargetConfigs,
  e.g. schema, an error will be raised.

**Methods:**

#### `get_configs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cli/configs/postgres.py#L47" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_configs(self) -> Dict[str, Any]
```

Returns the dbt configs specific to Postgres profile.

**Returns:**

* A configs JSON.

#### `handle_target_configs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cli/configs/base.py#L128" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handle_target_configs(cls, v: Any) -> Any
```

Handle target configs field aliasing during validation


Built with [Mintlify](https://mintlify.com).