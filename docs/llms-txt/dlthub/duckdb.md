# Source: https://dlthub.com/docs/dlt-ecosystem/destinations/duckdb.md

---
title: DuckDB
description: DuckDB `dlt` destination
keywords: [duckdb, destination, data warehouse]
---

# DuckDB

## Install dlt with DuckDB
**To install the dlt library with DuckDB dependencies, run:**
```sh
pip install "dlt[duckdb]"
```

## Destination capabilities
The following table shows the capabilities of the Duckdb destination:

| Feature | Value | More |
|---------|-------|------|
| Preferred loader file format | insert_values | [File formats](../file-formats/) |
| Supported loader file formats | insert_values, parquet, jsonl, model | [File formats](../file-formats/) |
| Has case sensitive identifiers | False | [Naming convention](../../general-usage/naming-convention#case-sensitive-and-insensitive-destinations) |
| Supported merge strategies | delete-insert, upsert, scd2, insert-only | [Merge strategy](../../general-usage/merge-loading#merge-strategies) |
| Supported replace strategies | truncate-and-insert, insert-from-staging | [Replace strategy](../../general-usage/full-loading#choosing-the-correct-replace-strategy-for-your-full-load) |
| Sqlglot dialect | duckdb | [Dataset access](../../general-usage/dataset-access/dataset) |
| Supports tz aware datetime | True | [Timestamps and Timezones](../../general-usage/schema#handling-of-timestamp-and-time-zones) |
| Supports naive datetime | True | [Timestamps and Timezones](../../general-usage/schema#handling-of-timestamp-and-time-zones) |

*This table shows the supported features of the Duckdb destination in dlt.*


## Setup guide

**1. Initialize a project with a pipeline that loads to DuckDB by running:**
```sh
dlt init chess duckdb
```

**2. Install the necessary dependencies for DuckDB by running:**
```sh
pip install -r requirements.txt
```

**3. Run the pipeline:**
```sh
python3 chess_pipeline.py
```

## Supported version
`dlt` supports `duckdb` versions starting from **0.9**. Below are a few notes on problems with particular versions observed
in our tests:
* `1.2.0` and `1.3.2` are verified stable versions where tests consistently pass
* `iceberg_scan` does not work on `duckdb` > 1.2.1 < 1.3.3 and azure blob storage (certain functions are not implemented)
* don't use `1.3.0` (decimal problem, seg faults on windows, crashes (segfault) on certain tests using azure blob storage)
* [segfault on windows will be fixed in 1.4](https://github.com/duckdb/duckdb/issues/17971)

## Write disposition
All write dispositions are supported.

## Data loading
`dlt` will load data using large INSERT VALUES statements by default. Loading is multithreaded (20 threads by default). If you are okay with installing `pyarrow`, we suggest switching to Parquet as the file format. Loading is faster (and also multithreaded).

### Data types
`duckdb` supports various [timestamp types](https://duckdb.org/docs/sql/data_types/timestamp.html). These can be configured using the column flags `timezone` and `precision` in the `dlt.resource` decorator or the `pipeline.run` method.

- **Precision**: Supported precision values are 0, 3, 6, and 9 for fractional seconds. Note that `timezone` and `precision` cannot be used together; attempting to combine them will result in an error.
- **Timezone**:
  - Setting `timezone=False` maps to `TIMESTAMP`.
  - Setting `timezone=True` (or omitting the flag, which defaults to `True`) maps to `TIMESTAMP WITH TIME ZONE` (`TIMESTAMPTZ`).

#### Example precision: TIMESTAMP_MS

```py
@dlt.resource(
    columns={"event_tstamp": {"data_type": "timestamp", "precision": 3}},
    primary_key="event_id",
)
def events():
    yield [{"event_id": 1, "event_tstamp": "2024-07-30T10:00:00.123"}]

pipeline = dlt.pipeline(destination="duckdb")
pipeline.run(events())
```

#### Example timezone: TIMESTAMP

```py
@dlt.resource(
    columns={"event_tstamp": {"data_type": "timestamp", "timezone": False}},
    primary_key="event_id",
)
def events():
    yield [{"event_id": 1, "event_tstamp": "2024-07-30T10:00:00.123+00:00"}]

pipeline = dlt.pipeline(destination="duckdb")
pipeline.run(events())
```

### Names normalization
`dlt` uses the standard **snake_case** naming convention to keep identical table and column identifiers across all destinations. If you want to use the **duckdb** wide range of characters (i.e., emojis) for table and column names, you can switch to the **duck_case** naming convention, which accepts almost any string as an identifier:
* New line (`\n`), carriage return (`\r`), and double quotes (`"`) are translated to an underscore (`_`).
* Consecutive underscores (`_`) are translated to a single `_`

Switch the naming convention using `config.toml`:
```toml
[schema]
naming="duck_case"
```

or via the env variable `SCHEMA__NAMING` or directly in the code:
```py
dlt.config["schema.naming"] = "duck_case"
```
:::warning
**duckdb** identifiers are **case insensitive** but display names preserve case. This may create name collisions if, for example, you load JSON with
`{"Column": 1, "column": 2}` as it will map data to a single column.
:::


## Supported file formats
You can configure the following file formats to load data into duckdb:
* [insert-values](../file-formats/insert-format.md) is used by default.
* [Parquet](../file-formats/parquet.md) is supported.
:::note
`duckdb` cannot COPY many Parquet files to a single table from multiple threads. In this situation, dlt serializes the loads. Still, that may be faster than INSERT.
:::
* [JSONL](../file-formats/jsonl.md)

:::tip
`duckdb` has [timestamp types](https://duckdb.org/docs/sql/data_types/timestamp.html) with resolutions from milliseconds to nanoseconds. However,
only the microseconds resolution (the most commonly used) is time zone aware. `dlt` generates timestamps with timezones by default, so loading parquet files
with default settings will fail (`duckdb` does not coerce tz-aware timestamps to naive timestamps).
Disable the timezones by changing the `dlt` [Parquet writer settings](../file-formats/parquet.md#writer-settings) as follows:
```sh
DATA_WRITER__TIMESTAMP_TIMEZONE=""
```
to disable tz adjustments.
:::

## Supported column hints

`duckdb` can create unique indexes for columns with `unique` hints. However, **this feature is disabled by default** as it can significantly slow down data loading.

## Destination configuration

By default, a DuckDB database will be created in the current working directory with a name `<pipeline_name>.duckdb` (`chess.duckdb` in the example above).

The `duckdb` credentials do not require any secret values. [You are free to pass the credentials and configuration explicitly](../../general-usage/destination.md#pass-explicit-credentials). For example:
```py
# will load data to files/data.db (relative path) database file
p = dlt.pipeline(
  pipeline_name='chess',
  destination=dlt.destinations.duckdb("files/data.db"),
  dataset_name='chess_data',
  dev_mode=False
)

# will load data to /var/local/database.duckdb (absolute path)
p = dlt.pipeline(
  pipeline_name='chess',
  destination=dlt.destinations.duckdb("/var/local/database.duckdb"),
  dataset_name='chess_data',
  dev_mode=False
)
```
Named `duckdb` destinations will create a database file in current working directory as `<destination_name>.duckdb`. For example:
```py
# will load data to files/data.db (relative path) database file
p = dlt.pipeline(
  pipeline_name='chess',
  destination=dlt.destinations.duckdb(destination_name="chessdb"),
  dataset_name='chess_data',
)
```
creates database `chessdb.duckdb`.

:::warning
Avoid naming dataset the same as database. That will confuse `duckdb` binder as both catalog and schema are the same. For
example:
```py
pipeline = dlt.pipeline(
        pipeline_name="dummy",
        destination="duckdb",
        dataset_name="dummy",
    )
```
will create database `dummy.duckdb` and schema (dataset) `dummy` which get confused resulting in Binder Error.
:::

The destination accepts a `duckdb` connection instance via `credentials`, so you can also open a database connection yourself and pass it to `dlt` to use.

```py
import duckdb

db = duckdb.connect()
p = dlt.pipeline(
  pipeline_name="chess",
  destination=dlt.destinations.duckdb(db),
  dataset_name="chess_data",
  dev_mode=False,
)

# Or if you would like to use an in-memory duckdb instance
db = duckdb.connect(":memory:")
p = pipeline_one = dlt.pipeline(
  pipeline_name="in_memory_pipeline",
  destination=dlt.destinations.duckdb(db),
  dataset_name="chess_data",
)

# print(p.run(chess()))

print(db.sql("DESCRIBE;"))

# Example output
# ââââââââââââ¬ââââââââââââââââ¬ââââââââââââââââââââââ¬âââââââââââââââââââââââ¬ââââââââââââââââââââââââ¬ââââââââââââ
# â database â    schema     â        name         â     column_names     â     column_types      â temporary â
# â varchar  â    varchar    â       varchar       â      varchar[]       â       varchar[]       â  boolean  â
# ââââââââââââ¼ââââââââââââââââ¼ââââââââââââââââââââââ¼âââââââââââââââââââââââ¼ââââââââââââââââââââââââ¼ââââââââââââ¤
# â memory   â chess_data    â _dlt_loads          â [load_id, schema_nâ¦  â [VARCHAR, VARCHAR, â¦  â false     â
# â memory   â chess_data    â _dlt_pipeline_state â [version, engine_vâ¦  â [BIGINT, BIGINT, VAâ¦  â false     â
# â memory   â chess_data    â _dlt_version        â [version, engine_vâ¦  â [BIGINT, BIGINT, TIâ¦  â false     â
# â memory   â chess_data    â my_table            â [a, _dlt_load_id, â¦  â [BIGINT, VARCHAR, Vâ¦  â false     â
# ââââââââââââ´ââââââââââââââââ´ââââââââââââââââââââââ´âââââââââââââââââââââââ´ââââââââââââââââââââââââ´ââââââââââââ
```

:::note
Be careful! The in-memory instance of the database will be destroyed once your Python script exits.
:::

This destination accepts database connection strings in the format used by [duckdb-engine](https://github.com/Mause/duckdb_engine#configuration).

You can configure a DuckDB destination with [secret / config values](../../general-usage/credentials) (e.g., using a `secrets.toml` file)
```toml
destination.duckdb.credentials="duckdb:///_storage/test_quack.duckdb"
```
The **duckdb://** URL above creates a **relative** path to `_storage/test_quack.duckdb`. To define an **absolute** path, you need to specify four slashes, i.e., `duckdb:////_storage/test_quack.duckdb`.

You can also skip the schema and just pass the path directly:
```toml
destination.duckdb.credentials="_storage/test_quack.duckdb"
```

You can also place the database in the working directory of the pipeline by passing **:pipeline:** as path. The
database will be named `<pipeline_name>.duckdb`.

1. Via `config.toml`
```toml
destination.duckdb.credentials=":pipeline:"
```

2. In Python code
```py
p = dlt.pipeline(
  pipeline_name="my_pipeline",
  destination=dlt.destinations.duckdb(":pipeline:"),
)
```

### Additional configuration
Unique indexes may be created during loading if the following config value is set:
```toml
[destination.duckdb]
create_indexes=true
```

You can load extensions and set pragmas, [local and global config](https://duckdb.org/docs/stable/configuration/overview.html#global-configuration-options) options by adding those to the configuration:
```toml
[destination.duckdb.credentials]
extensions=["spatial"]
pragmas=["enable_progress_bar", "enable_logging"]

[destination.duckdb.credentials.global_config]
azure_transport_option_type=true

[destination.duckdb.credentials.local_config]
errors_as_json=true
```
The configuration above will LOAD extension **spatial** (but it will not install it), apply the global config (`SET GLOBAL azure_transport_option_type=true`), then pragmas (`PRAGMA enable_logging`) and local config (`SET SESSION errors_as_json=true`) at the end.
Internally, `dlt` opens new `duckdb` connection and then dispenses separate sessions to worker threads via `cursor()` (even if the calling thread is the same as the one that creates connection). Extensions and global config are applied only once - to the "original" connection and are automatically propagated to sessions.

Note that you can use environment variables to pass dictionaries and lists: those must be passed as Python literals (not JSON!). See below:

You can also pass additional options in code:
```py
import os
import duckdb
from dlt.destinations.impl.duckdb.configuration import DuckDbCredentials

# install spatial
duckdb.sql("INSTALL spatial;")

# use Python list literal to pass complex env variable
os.environ["DESTINATION__DUCKDB__CREDENTIALS__PRAGMAS"] = '["enable_logging"]'

dest_ = dlt.destinations.duckdb(
    DuckDbCredentials("duck.db", extensions=["spatial"], local_config={"errors_as_json": True})
)
```
Code above install **spatial** (`dlt` only loads extension) and passes duckdb credentials to the destination constructor. Database file is **duck.db**, logging and error messages as `json` are enabled.

## Data access after loading
After loading, it is available in **read/write** mode via `with pipeline.sql_client() as con:`, which is a wrapper over `DuckDBPyConnection`. See [duckdb docs](https://duckdb.org/docs/api/python/overview#persistent-storage) for details. If you want to **read** data, use [pipeline.dataset()](../../general-usage/dataset-access/dataset) instead of `sql_client`.


## dbt support
This destination [integrates with dbt](../transformations/dbt/dbt.md) via [dbt-duckdb](https://github.com/jwills/dbt-duckdb), which is a community-supported package. The `duckdb` database is shared with `dbt`. In rare cases, you may see information that the binary database format does not match the database format expected by `dbt-duckdb`. You can avoid this by updating the `duckdb` package in your `dlt` project with `pip install -U`.

NOTE: extensions, pragmas and configs are not propagated from `dlt` configuration to the dbt profile at this moment.

### Syncing of `dlt` state
This destination fully supports [dlt state sync](../../general-usage/state#syncing-state-with-destination).

## Additional Setup guides
- [Load data from GitHub to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/github/load-data-with-python-from-github-to-duckdb)
- [Load data from IBM Db2 to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/sql_database_db2/load-data-with-python-from-sql_database_db2-to-duckdb)
- [Load data from Fivetran to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/fivetran/load-data-with-python-from-fivetran-to-duckdb)
- [Load data from Klaviyo to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/klaviyo/load-data-with-python-from-klaviyo-to-duckdb)
- [Load data from Azure Cloud Storage to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/filesystem-az/load-data-with-python-from-filesystem-az-to-duckdb)
- [Load data from Coinbase to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/coinbase/load-data-with-python-from-coinbase-to-duckdb)
- [Load data from Harvest to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/harvest/load-data-with-python-from-harvest-to-duckdb)
- [Load data from Imgur to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/imgur/load-data-with-python-from-imgur-to-duckdb)
- [Load data from PostgreSQL to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/sql_database_postgres/load-data-with-python-from-sql_database_postgres-to-duckdb)
- [Load data from Salesforce to DuckDB in python with dlt](https://dlthub.com/docs/pipelines/salesforce/load-data-with-python-from-salesforce-to-duckdb)

