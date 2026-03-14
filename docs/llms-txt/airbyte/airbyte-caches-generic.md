# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/caches/airbyte-caches-generic.md

# Module airbyte.caches.generic

Copy Page

A Generic SQL Cache implementation.

## Classes[​](#classes "Direct link to Classes")

`GenericSQLCacheConfig(**data: Any)` : Allows configuring 'sql\_alchemy\_url' directly.

Initialize the cache and backends.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* airbyte.caches.base.CacheBase
* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* airbyte.\_writers.base.AirbyteWriterInterface
* abc.ABC

### Class variables[​](#class-variables "Direct link to Class variables")

`model_config` :

`sql_alchemy_url: SecretString | str` :
