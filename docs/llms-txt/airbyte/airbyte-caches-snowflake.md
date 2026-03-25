# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/caches/airbyte-caches-snowflake.md

# Module airbyte.caches.snowflake

Copy Page

A Snowflake implementation of the PyAirbyte cache.

## Usage Example[​](#usage-example "Direct link to Usage Example")

# Password connection:

```
from airbyte as ab
from airbyte.caches import SnowflakeCache

cache = SnowflakeCache(
    account="myaccount",
    username="myusername",
    password=ab.get_secret("SNOWFLAKE_PASSWORD"), # optional
    warehouse="mywarehouse",
    database="mydatabase",
    role="myrole",
    schema_name="myschema",
)
```

# Private key connection:

```
from airbyte as ab
from airbyte.caches import SnowflakeCache

cache = SnowflakeCache(
    account="myaccount",
    username="myusername",
    private_key=ab.get_secret("SNOWFLAKE_PRIVATE_KEY"),
    private_key_passphrase=ab.get_secret("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE"), # optional
    warehouse="mywarehouse",
    database="mydatabase",
    role="myrole",
    schema_name="myschema",
)
```

# Private key path connection:

```
from airbyte as ab
from airbyte.caches import SnowflakeCache

cache = SnowflakeCache(
    account="myaccount",
    username="myusername",
    private_key_path="path/to/my/private_key.pem",
    private_key_passphrase=ab.get_secret("SNOWFLAKE_PRIVATE_KEY_PASSPHRASE"), # optional
    warehouse="mywarehouse",
    database="mydatabase",
    role="myrole",
    schema_name="myschema",
)
```

## Classes[​](#classes "Direct link to Classes")

`SnowflakeCache(**data: Any)` : Configuration for the Snowflake cache.

Initialize the cache and backends.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* airbyte.\_processors.sql.snowflake.SnowflakeConfig
* airbyte.caches.base.CacheBase
* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* airbyte.\_writers.base.AirbyteWriterInterface
* abc.ABC

### Class variables[​](#class-variables "Direct link to Class variables")

`dedupe_mode: RecordDedupeMode` :

`model_config` :

`paired_destination_config_class: ClassVar[type | None]` : DestinationSnowflake(database: 'str', host: 'str', role: 'str', schema: 'str', username: 'str', warehouse: 'str', credentials: 'Optional\[AuthorizationMethod]' = None, DESTINATION\_TYPE: 'Final\[Snowflake]' = \<Snowflake.SNOWFLAKE: 'snowflake'>, disable\_type\_dedupe: 'Optional\[bool]' = False, jdbc\_url\_params: 'Optional\[str]' = None, raw\_data\_schema: 'Optional\[str]' = None, retention\_period\_days: 'Optional\[int]' = 1, use\_merge\_for\_upsert: 'Optional\[bool]' = False)

`paired_destination_name: ClassVar[str | None]` :

`SnowflakeConfig(**data: Any)` : Configuration for the Snowflake cache.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[`ValidationError`]\[pydantic\_core.ValidationError] if the input data cannot be validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

### Ancestors (in MRO)[​](#ancestors-in-mro-1 "Direct link to Ancestors (in MRO)")

* airbyte.shared.sql\_processor.SqlConfig
* pydantic.main.BaseModel
* abc.ABC

### Descendants[​](#descendants "Direct link to Descendants")

* airbyte.caches.snowflake.SnowflakeCache

### Class variables[​](#class-variables-1 "Direct link to Class variables")

`account: str` :

`data_retention_time_in_days: int | None` :

`database: str` :

`model_config` :

`password: SecretString | None` :

`private_key: SecretString | None` :

`private_key_passphrase: SecretString | None` :

`private_key_path: str | None` :

`role: str` :

`username: str` :

`warehouse: str` :

### Methods[​](#methods "Direct link to Methods")

`get_sql_alchemy_url(self) ‑> airbyte.secrets.base.SecretString` : Return the SQLAlchemy URL to use.

`get_vendor_client(self) ‑> object` : Return the Snowflake connection object.
