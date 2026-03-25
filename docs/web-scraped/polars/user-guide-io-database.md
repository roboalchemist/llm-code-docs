# Source: https://docs.pola.rs/user-guide/io/database/

Title: Databases - Polars user guide

URL Source: https://docs.pola.rs/user-guide/io/database/

Markdown Content:
Databases - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/io/database/#databases)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Databases 

 Initializing search 

[pola-rs/polars * py-1.39.0 * 37.7k * 2.7k](https://github.com/pola-rs/polars "Go to repository")

*   [Polars](https://docs.pola.rs/)
*   [Polars Cloud](https://docs.pola.rs/polars-cloud/)
*   [Polars on-premises](https://docs.pola.rs/polars-on-premises/)

[![Image 2: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide") Polars user guide  

[pola-rs/polars * py-1.39.0 * 37.7k * 2.7k](https://github.com/pola-rs/polars "Go to repository")

*   - [x]  Polars   Polars  
    *   - [x] [User guide](https://docs.pola.rs/)  User guide  
        *   [Getting started](https://docs.pola.rs/user-guide/getting-started/)
        *   [Installation](https://docs.pola.rs/user-guide/installation/)
        *   - [x] [Concepts](https://docs.pola.rs/user-guide/concepts/)  Concepts  
            *   [Data types and structures](https://docs.pola.rs/user-guide/concepts/data-types-and-structures/)
            *   [Expressions and contexts](https://docs.pola.rs/user-guide/concepts/expressions-and-contexts/)
            *   [Lazy API](https://docs.pola.rs/user-guide/concepts/lazy-api/)
            *   [Streaming](https://docs.pola.rs/user-guide/concepts/streaming/)

        *   - [x] [Expressions](https://docs.pola.rs/user-guide/expressions/)  Expressions  
            *   [Basic operations](https://docs.pola.rs/user-guide/expressions/basic-operations/)
            *   [Expression expansion](https://docs.pola.rs/user-guide/expressions/expression-expansion/)
            *   [Casting](https://docs.pola.rs/user-guide/expressions/casting/)
            *   [Strings](https://docs.pola.rs/user-guide/expressions/strings/)
            *   [Lists and arrays](https://docs.pola.rs/user-guide/expressions/lists-and-arrays/)
            *   [Categorical data and enums](https://docs.pola.rs/user-guide/expressions/categorical-data-and-enums/)
            *   [Structs](https://docs.pola.rs/user-guide/expressions/structs/)
            *   [Missing data](https://docs.pola.rs/user-guide/expressions/missing-data/)
            *   [Aggregation](https://docs.pola.rs/user-guide/expressions/aggregation/)
            *   [Window functions](https://docs.pola.rs/user-guide/expressions/window-functions/)
            *   [Folds](https://docs.pola.rs/user-guide/expressions/folds/)
            *   [User-defined Python functions](https://docs.pola.rs/user-guide/expressions/user-defined-python-functions/)
            *   [Numpy functions](https://docs.pola.rs/user-guide/expressions/numpy-functions/)

        *   - [x] [Transformations](https://docs.pola.rs/user-guide/transformations/)  Transformations  
            *   [Joins](https://docs.pola.rs/user-guide/transformations/joins/)
            *   [Concatenation](https://docs.pola.rs/user-guide/transformations/concatenation/)
            *   [Pivots](https://docs.pola.rs/user-guide/transformations/pivot/)
            *   [Unpivots](https://docs.pola.rs/user-guide/transformations/unpivot/)
            *   - [x]  Time series   Time series  
                *   [Parsing](https://docs.pola.rs/user-guide/transformations/time-series/parsing/)
                *   [Filtering](https://docs.pola.rs/user-guide/transformations/time-series/filter/)
                *   [Grouping](https://docs.pola.rs/user-guide/transformations/time-series/rolling/)
                *   [Resampling](https://docs.pola.rs/user-guide/transformations/time-series/resampling/)
                *   [Time zones](https://docs.pola.rs/user-guide/transformations/time-series/timezones/)

        *   - [x] [Lazy API](https://docs.pola.rs/user-guide/lazy/)  Lazy API  
            *   [Usage](https://docs.pola.rs/user-guide/lazy/using/)
            *   [Optimizations](https://docs.pola.rs/user-guide/lazy/optimizations/)
            *   [Schema](https://docs.pola.rs/user-guide/lazy/schemas/)
            *   [DataType Expressions](https://docs.pola.rs/user-guide/lazy/datatype_exprs/)
            *   [Query plan](https://docs.pola.rs/user-guide/lazy/query-plan/)
            *   [Query execution](https://docs.pola.rs/user-guide/lazy/execution/)
            *   [Sources and sinks](https://docs.pola.rs/user-guide/lazy/sources_sinks/)
            *   [Multiplexing queries](https://docs.pola.rs/user-guide/lazy/multiplexing/)
            *   [GPU Support](https://docs.pola.rs/user-guide/lazy/gpu/)

        *   - [x] [IO](https://docs.pola.rs/user-guide/io/)  IO  
            *   [CSV](https://docs.pola.rs/user-guide/io/csv/)
            *   [Excel](https://docs.pola.rs/user-guide/io/excel/)
            *   [Parquet](https://docs.pola.rs/user-guide/io/parquet/)
            *   [JSON files](https://docs.pola.rs/user-guide/io/json/)
            *   [Multiple](https://docs.pola.rs/user-guide/io/multiple/)
            *   [Hive](https://docs.pola.rs/user-guide/io/hive/)
            *   - [x]  Databases  [Databases](https://docs.pola.rs/user-guide/io/database/) Table of contents  
                *   [Read from a database](https://docs.pola.rs/user-guide/io/database/#read-from-a-database)
                    *   [Difference between read_database_uri and read_database](https://docs.pola.rs/user-guide/io/database/#difference-between-read_database_uri-and-read_database)
                    *   [Engines](https://docs.pola.rs/user-guide/io/database/#engines)
                        *   [ConnectorX](https://docs.pola.rs/user-guide/io/database/#connectorx)
                        *   [ADBC](https://docs.pola.rs/user-guide/io/database/#adbc)

                *   [Write to a database](https://docs.pola.rs/user-guide/io/database/#write-to-a-database)
                    *   [Engines](https://docs.pola.rs/user-guide/io/database/#engines_1)
                        *   [SQLAlchemy](https://docs.pola.rs/user-guide/io/database/#sqlalchemy)
                        *   [ADBC](https://docs.pola.rs/user-guide/io/database/#adbc_1)

            *   [Cloud storage](https://docs.pola.rs/user-guide/io/cloud-storage/)
            *   [Google BigQuery](https://docs.pola.rs/user-guide/io/bigquery/)
            *   [Hugging Face](https://docs.pola.rs/user-guide/io/hugging-face/)
            *   [Google Sheets (via Colab)](https://docs.pola.rs/user-guide/io/sheets_colab/)

        *   - [x] [Plugins](https://docs.pola.rs/user-guide/plugins/)  Plugins  
            *   [Expression Plugins](https://docs.pola.rs/user-guide/plugins/expr_plugins/)
            *   [IO Plugins](https://docs.pola.rs/user-guide/plugins/io_plugins/)

        *   - [x]  SQL   SQL  
            *   [Introduction](https://docs.pola.rs/user-guide/sql/intro/)
            *   [SHOW TABLES](https://docs.pola.rs/user-guide/sql/show/)
            *   [SELECT](https://docs.pola.rs/user-guide/sql/select/)
            *   [CREATE](https://docs.pola.rs/user-guide/sql/create/)
            *   [Common Table Expressions](https://docs.pola.rs/user-guide/sql/cte/)

        *   - [x]  Migrating   Migrating  
            *   [Coming from Pandas](https://docs.pola.rs/user-guide/migration/pandas/)
            *   [Coming from Apache Spark](https://docs.pola.rs/user-guide/migration/spark/)

        *   - [x]  Misc   Misc  
            *   [Ecosystem](https://docs.pola.rs/user-guide/ecosystem/)
            *   [Multiprocessing](https://docs.pola.rs/user-guide/misc/multiprocessing/)
            *   [Visualization](https://docs.pola.rs/user-guide/misc/visualization/)
            *   [Styling](https://docs.pola.rs/user-guide/misc/styling/)
            *   [Comparison with other tools](https://docs.pola.rs/user-guide/misc/comparison/)
            *   [Arrow producer/consumer](https://docs.pola.rs/user-guide/misc/arrow/)
            *   [Generating Polars code with LLMs](https://docs.pola.rs/user-guide/misc/polars_llms/)

        *   [GPU Support [Open Beta]](https://docs.pola.rs/user-guide/gpu-support/)

    *   - [x]  API   API  
        *   [Reference guide](https://docs.pola.rs/api/reference/)

    *   - [x]  Development   Development  
        *   - [x] [Contributing](https://docs.pola.rs/development/contributing/)  Contributing  
            *   [IDE configuration](https://docs.pola.rs/development/contributing/ide/)
            *   [Test suite](https://docs.pola.rs/development/contributing/test/)
            *   [Continuous integration](https://docs.pola.rs/development/contributing/ci/)
            *   [Code style](https://docs.pola.rs/development/contributing/code-style/)

        *   [Versioning](https://docs.pola.rs/development/versioning/)

    *   - [x]  Releases   Releases  
        *   - [x] [Upgrade guides](https://docs.pola.rs/releases/upgrade/)  Upgrade guides  
            *   [Version 1](https://docs.pola.rs/releases/upgrade/1/)
            *   [Version 0.20](https://docs.pola.rs/releases/upgrade/0.20/)
            *   [Version 0.19](https://docs.pola.rs/releases/upgrade/0.19/)

        *   [Changelog](https://docs.pola.rs/releases/changelog/)

*   - [x] [Polars Cloud](https://docs.pola.rs/polars-cloud/)  Polars Cloud  
    *   [Getting started](https://docs.pola.rs/polars-cloud/quickstart/)
    *   [Connect to your cloud](https://docs.pola.rs/polars-cloud/connect-cloud/)
    *   - [x]  Queries   Queries  
        *   [Execute remote query](https://docs.pola.rs/polars-cloud/run/remote-query/)
        *   [Distributed queries](https://docs.pola.rs/polars-cloud/run/distributed-engine/)
        *   [Query profiling](https://docs.pola.rs/polars-cloud/run/query-profile/)
        *   [Glossary](https://docs.pola.rs/polars-cloud/run/glossary/)

    *   - [x]  Integrations   Integrations  
        *   - [x] [Orchestration](https://docs.pola.rs/polars-cloud/integrations/)  Orchestration  
            *   [Airflow](https://docs.pola.rs/polars-cloud/integrations/airflow/)
            *   [Dagster](https://docs.pola.rs/polars-cloud/integrations/dagster/)
            *   [Prefect](https://docs.pola.rs/polars-cloud/integrations/prefect/)
            *   [AWS Lambda](https://docs.pola.rs/polars-cloud/integrations/lambda/)

    *   - [x]  Concepts   Concepts  
        *   - [x]  Context   Context  
            *   [Compute context introduction](https://docs.pola.rs/polars-cloud/context/compute-context/)
            *   [Reconnect to compute cluster](https://docs.pola.rs/polars-cloud/context/reconnect/)
            *   [Plugins and custom libraries](https://docs.pola.rs/polars-cloud/context/plugins/)
            *   [Proxy mode](https://docs.pola.rs/polars-cloud/context/proxy-mode/)

        *   - [x]  Organizations   Organizations  
            *   [Set up organization](https://docs.pola.rs/polars-cloud/organization/organizations/)
            *   [Start trial period](https://docs.pola.rs/polars-cloud/organization/start-trial/)
            *   [Payment and billing](https://docs.pola.rs/polars-cloud/organization/billing/)
            *   [Manage members](https://docs.pola.rs/polars-cloud/organization/members/)

        *   - [x]  Workspaces   Workspaces  
            *   [Workspace configuration](https://docs.pola.rs/polars-cloud/workspace/settings/)
            *   [Manage team](https://docs.pola.rs/polars-cloud/workspace/team/)

        *   - [x]  Authentication   Authentication  
            *   [Logging in](https://docs.pola.rs/polars-cloud/explain/authentication/)
            *   [Using service accounts](https://docs.pola.rs/polars-cloud/explain/service-accounts/)

        *   - [x]  Providers   Providers  
            *   - [x]  AWS   AWS  
                *   [Infrastructure](https://docs.pola.rs/polars-cloud/providers/aws/infra/)
                *   [Permissions](https://docs.pola.rs/polars-cloud/providers/aws/permissions/)

        *   - [x]  Misc   Misc  
            *   [CLI](https://docs.pola.rs/polars-cloud/cli/)
            *   [Public datasets](https://docs.pola.rs/polars-cloud/public-datasets/)
            *   [FAQ](https://docs.pola.rs/polars-cloud/faq/)
            *   [API Reference](https://docs.cloud.pola.rs/)

    *   - [x]  API   API  
        *   [Reference guide](https://docs.cloud.pola.rs/)

*   - [x] [Polars on-premises](https://docs.pola.rs/polars-on-premises/)  Polars on-premises  
    *   - [x]  Kubernetes   Kubernetes  
        *   [Getting started](https://docs.pola.rs/polars-on-premises/kubernetes/getting-started/)

    *   - [x]  Bare-metal   Bare-metal  
        *   [Getting started](https://docs.pola.rs/polars-on-premises/bare-metal/getting-started/)
        *   - [x]  Configuration   Configuration  
            *   [Config file reference](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/reference/)
            *   [License](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/license/)
            *   [Profiling and host metrics](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/monitoring/)
            *   [Resource limits](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/resource-limits/)
            *   [Shuffle data](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/shuffle-data/)
            *   [Anonymous results](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/anonymous-results/)
            *   [Network addresses](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/network-addresses/)
            *   [Static leader configuration](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/static-leader/)
            *   [Example configurations](https://docs.pola.rs/polars-on-premises/bare-metal/configuration/example-configurations/)

        *   [Environment variables](https://docs.pola.rs/polars-on-premises/bare-metal/environment-variables/)
        *   [Python environment](https://docs.pola.rs/polars-on-premises/bare-metal/python-environment/)

 Table of contents  
*   [Read from a database](https://docs.pola.rs/user-guide/io/database/#read-from-a-database)
    *   [Difference between read_database_uri and read_database](https://docs.pola.rs/user-guide/io/database/#difference-between-read_database_uri-and-read_database)
    *   [Engines](https://docs.pola.rs/user-guide/io/database/#engines)
        *   [ConnectorX](https://docs.pola.rs/user-guide/io/database/#connectorx)
        *   [ADBC](https://docs.pola.rs/user-guide/io/database/#adbc)

*   [Write to a database](https://docs.pola.rs/user-guide/io/database/#write-to-a-database)
    *   [Engines](https://docs.pola.rs/user-guide/io/database/#engines_1)
        *   [SQLAlchemy](https://docs.pola.rs/user-guide/io/database/#sqlalchemy)
        *   [ADBC](https://docs.pola.rs/user-guide/io/database/#adbc_1)

Databases
=========

Read from a database
--------------------

Polars can read from a database using the `pl.read_database_uri` and `pl.read_database` functions.

### Difference between `read_database_uri` and `read_database`

Use `pl.read_database_uri` if you want to specify the database connection with a connection string called a `uri`. For example, the following snippet shows a query to read all columns from the `foo` table in a Postgres database where we use the `uri` to connect:

 Python 

[`read_database_uri`](https://docs.pola.rs/api/python/stable/reference/api/polars.read_database_uri.html)

```
import polars as pl

uri = "postgresql://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database_uri(query=query, uri=uri)
```

On the other hand, use `pl.read_database` if you want to connect via a connection engine created with a library like SQLAlchemy.

 Python 

[`read_database`](https://docs.pola.rs/api/python/stable/reference/api/polars.read_database.html)

```
import polars as pl
from sqlalchemy import create_engine

conn = create_engine(f"sqlite:///test.db")

query = "SELECT * FROM foo"

pl.read_database(query=query, connection=conn.connect())
```

Note that `pl.read_database_uri` is likely to be faster than `pl.read_database` if you are using a SQLAlchemy or DBAPI2 connection as these connections may load the data row-wise into Python before copying the data again to the column-wise Apache Arrow format.

### Engines

Polars doesn't manage connections and data transfer from databases by itself. Instead, external libraries (known as _engines_) handle this.

When using `pl.read_database`, you specify the engine when you create the connection object. When using `pl.read_database_uri`, you can specify one of two engines to read from the database:

*   [ConnectorX](https://github.com/sfu-db/connector-x) and
*   [ADBC](https://arrow.apache.org/docs/format/ADBC.html)

Both engines have native support for Apache Arrow and so can read data directly into a Polars `DataFrame` without copying the data.

#### ConnectorX

ConnectorX is the default engine and [supports numerous databases](https://github.com/sfu-db/connector-x#sources) including Postgres, Mysql, SQL Server and Redshift. ConnectorX is written in Rust and stores data in Arrow format to allow for zero-copy to Polars.

To read from one of the supported databases with `ConnectorX` you need to activate the additional dependency `ConnectorX` when installing Polars or install it manually with

```
$ pip install connectorx
```

#### ADBC

ADBC (Arrow Database Connectivity) is an engine supported by the Apache Arrow project. ADBC aims to be both an API standard for connecting to databases and libraries implementing this standard in a range of languages.

It is still early days for ADBC so support for different databases is limited. At present, drivers for ADBC are only available for [Postgres](https://pypi.org/project/adbc-driver-postgresql/), [SQLite](https://pypi.org/project/adbc-driver-sqlite/) and [Snowflake](https://pypi.org/project/adbc-driver-snowflake/). To install ADBC, you need to install the driver for your database. For example, to install the driver for SQLite, you run:

```
$ pip install adbc-driver-sqlite
```

As ADBC is not the default engine, you must specify the engine as an argument to `pl.read_database_uri`.

 Python 

[`read_database_uri`](https://docs.pola.rs/api/python/stable/reference/api/polars.read_database_uri.html)

```
uri = "postgresql://username:password@server:port/database"
query = "SELECT * FROM foo"

pl.read_database_uri(query=query, uri=uri, engine="adbc")
```

Write to a database
-------------------

We can write to a database with Polars using the `pl.write_database` function.

### Engines

As with reading from a database above, Polars uses an _engine_ to write to a database. The currently supported engines are:

*   [SQLAlchemy](https://www.sqlalchemy.org/) and
*   Arrow Database Connectivity (ADBC)

#### SQLAlchemy

With the default engine SQLAlchemy you can write to any database supported by SQLAlchemy. To use this engine you need to install SQLAlchemy and Pandas

```
$ pip install SQLAlchemy pandas
```

In this example, we write the `DataFrame` to a table called `records` in the database

 Python 

[`write_database`](https://docs.pola.rs/api/python/stable/reference/api/polars.DataFrame.write_database.html)

```
uri = "postgresql://username:password@server:port/database"
df = pl.DataFrame({"foo": [1, 2, 3]})

df.write_database(table_name="records",  connection=uri)
```

In the SQLAlchemy approach, Polars converts the `DataFrame` to a Pandas `DataFrame` backed by PyArrow and then uses SQLAlchemy methods on a Pandas `DataFrame` to write to the database.

#### ADBC

ADBC can also be used to write to a database. Writing is supported for the same databases that support reading with ADBC. As shown above, you need to install the appropriate ADBC driver for your database.

 Python 

[`write_database`](https://docs.pola.rs/api/python/stable/reference/api/polars.DataFrame.write_database.html)

```
uri = "postgresql://username:password@server:port/database"
df = pl.DataFrame({"foo": [1, 2, 3]})

df.write_database(table_name="records", connection=uri, engine="adbc")
```

[Previous Hive](https://docs.pola.rs/user-guide/io/hive/)[Next Cloud storage](https://docs.pola.rs/user-guide/io/cloud-storage/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
