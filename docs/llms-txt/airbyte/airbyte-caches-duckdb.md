# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/caches/airbyte-caches-duckdb.md

# Module airbyte.caches.duckdb

Copy Page

A DuckDB implementation of the PyAirbyte cache.

## Usage Example[​](#usage-example "Direct link to Usage Example")

```
from airbyte as ab
from airbyte.caches import DuckDBCache

cache = DuckDBCache(
    db_path="/path/to/my/duckdb-file",
    schema_name="myschema",
)
```

## Classes[​](#classes "Direct link to Classes")

`DuckDBCache(**data: Any)` : A DuckDB cache.

Initialize the cache and backends.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* airbyte.\_processors.sql.duckdb.DuckDBConfig
* airbyte.caches.base.CacheBase
* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* airbyte.\_writers.base.AirbyteWriterInterface
* abc.ABC

### Descendants[​](#descendants "Direct link to Descendants")

* airbyte.caches.motherduck.MotherDuckCache

### Class variables[​](#class-variables "Direct link to Class variables")

`model_config` :

`paired_destination_config_class: ClassVar[type | None]` : DestinationDuckdb(destination\_path: 'str', DESTINATION\_TYPE: 'Final\[Duckdb]' = \<Duckdb.DUCKDB: 'duckdb'>, motherduck\_api\_key: 'Optional\[str]' = None, schema: 'Optional\[str]' = None)

`paired_destination_name: ClassVar[str | None]` :

`DuckDBConfig(**data: Any)` : Configuration for DuckDB.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[`ValidationError`]\[pydantic\_core.ValidationError] if the input data cannot be validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

### Ancestors (in MRO)[​](#ancestors-in-mro-1 "Direct link to Ancestors (in MRO)")

* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* abc.ABC

### Descendants[​](#descendants-1 "Direct link to Descendants")

* airbyte.caches.duckdb.DuckDBCache
* airbyte.caches.motherduck.MotherDuckConfig

### Class variables[​](#class-variables-1 "Direct link to Class variables")

`db_path: Path | str` : Normally db\_path is a Path object.

The database name will be inferred from the file name. For example, given a `db_path` of `/path/to/my/duckdb-file`, the database name is `my_db`.

`model_config` :

### Methods[​](#methods "Direct link to Methods")

`get_sql_alchemy_url(self) ‑> airbyte.secrets.base.SecretString` : Return the SQLAlchemy URL to use.

`get_sql_engine(self) ‑> Engine` : Return the SQL Alchemy engine.

This method is overridden to ensure that the database parent directory is created if it doesn't exist.
