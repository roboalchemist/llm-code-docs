# Source: https://docs.prefect.io/v3/api-ref/python/prefect-server-models-configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# configuration

# `prefect.server.models.configuration`

## Functions

### `write_configuration` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/configuration.py#L11" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
write_configuration(db: PrefectDBInterface, session: AsyncSession, configuration: schemas.core.Configuration) -> orm_models.Configuration
```

### `read_configuration` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/prefect/server/models/configuration.py#L38" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_configuration(db: PrefectDBInterface, session: AsyncSession, key: str) -> Optional[schemas.core.Configuration]
```


Built with [Mintlify](https://mintlify.com).