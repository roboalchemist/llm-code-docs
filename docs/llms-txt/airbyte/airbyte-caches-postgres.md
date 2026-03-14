# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/caches/airbyte-caches-postgres.md

# Module airbyte.caches.postgres

Copy Page

A Postgres implementation of the PyAirbyte cache.

## Usage Example[​](#usage-example "Direct link to Usage Example")

```
from airbyte as ab
from airbyte.caches import PostgresCache

cache = PostgresCache(
    host="myhost",
    port=5432,
    username="myusername",
    password=ab.get_secret("POSTGRES_PASSWORD"),
    database="mydatabase",
)
```

## Classes[​](#classes "Direct link to Classes")

`PostgresCache(**data: Any)` : Configuration for the Postgres cache.

Also inherits config from the JsonlWriter, which is responsible for writing files to disk.

Initialize the cache and backends.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* airbyte.\_processors.sql.postgres.PostgresConfig
* airbyte.caches.base.CacheBase
* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* airbyte.\_writers.base.AirbyteWriterInterface
* abc.ABC

### Class variables[​](#class-variables "Direct link to Class variables")

`model_config` :

`paired_destination_config_class: ClassVar[type | None]` : DestinationPostgres(database: 'str', host: 'str', username: 'str', DESTINATION\_TYPE: 'Final\[Postgres]' = \<Postgres.POSTGRES: 'postgres'>, disable\_type\_dedupe: 'Optional\[bool]' = False, drop\_cascade: 'Optional\[bool]' = False, jdbc\_url\_params: 'Optional\[str]' = None, password: 'Optional\[str]' = None, port: 'Optional\[int]' = 5432, raw\_data\_schema: 'Optional\[str]' = None, schema: 'Optional\[str]' = 'public', ssl: 'Optional\[bool]' = False, ssl\_mode: 'Optional\[SSLModes]' = None, tunnel\_method: 'Optional\[DestinationPostgresSSHTunnelMethod]' = None, unconstrained\_number: 'Optional\[bool]' = False)

`paired_destination_name: ClassVar[str | None]` :

### Methods[​](#methods "Direct link to Methods")

`clone_as_cloud_destination_config(self) ‑> airbyte_api.models.destination_postgres.DestinationPostgres` : Return a DestinationPostgres instance with the same configuration.

`PostgresConfig(**data: Any)` : Configuration for the Postgres cache.

Also inherits config from the JsonlWriter, which is responsible for writing files to disk.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[`ValidationError`]\[pydantic\_core.ValidationError] if the input data cannot be validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

### Ancestors (in MRO)[​](#ancestors-in-mro-1 "Direct link to Ancestors (in MRO)")

* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* abc.ABC

### Descendants[​](#descendants "Direct link to Descendants")

* airbyte.caches.postgres.PostgresCache

### Class variables[​](#class-variables-1 "Direct link to Class variables")

`database: str` :

`host: str` :

`model_config` :

`password: SecretString | str` :

`port: int` :

`username: str` :

### Methods[​](#methods-1 "Direct link to Methods")

`get_sql_alchemy_url(self) ‑> airbyte.secrets.base.SecretString` : Return the SQLAlchemy URL to use.
