# Source: https://docs.prefect.io/integrations/prefect-dbt/api-ref/prefect_dbt-cli-configs-snowflake.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# snowflake

# `prefect_dbt.cli.configs.snowflake`

Module containing models for Snowflake configs

## Classes

### `SnowflakeTargetConfigs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cli/configs/snowflake.py#L21" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Target configs contain credentials and
settings, specific to Snowflake.
To find valid keys, head to the [Snowflake Profile](https://docs.getdbt.com/reference/warehouse-profiles/snowflake-profile)
page.

**Attributes:**

* `connector`: The connector to use.

**Examples:**

Load stored SnowflakeTargetConfigs:

```python  theme={null}
from prefect_dbt.cli.configs import SnowflakeTargetConfigs

snowflake_target_configs = SnowflakeTargetConfigs.load("BLOCK_NAME")
```

Instantiate SnowflakeTargetConfigs.

```python  theme={null}
from prefect_dbt.cli.configs import SnowflakeTargetConfigs
from prefect_snowflake.credentials import SnowflakeCredentials
from prefect_snowflake.database import SnowflakeConnector

credentials = SnowflakeCredentials(
    user="user",
    password="password",
    account="account.region.aws",
    role="role",
)
connector = SnowflakeConnector(
    schema="public",
    database="database",
    warehouse="warehouse",
    credentials=credentials,
)
target_configs = SnowflakeTargetConfigs(
    connector=connector,
    extras={"retry_on_database_errors": True},
)
```

**Methods:**

#### `get_configs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cli/configs/snowflake.py#L81" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
get_configs(self) -> Dict[str, Any]
```

Returns the dbt configs specific to Snowflake profile.

**Returns:**

* A configs JSON.

#### `handle_target_configs` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-dbt/prefect_dbt/cli/configs/base.py#L128" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
handle_target_configs(cls, v: Any) -> Any
```

Handle target configs field aliasing during validation


Built with [Mintlify](https://mintlify.com).