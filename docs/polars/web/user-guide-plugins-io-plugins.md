# Source: https://docs.pola.rs/user-guide/plugins/io_plugins/

Title: IO Plugins - Polars user guide

URL Source: https://docs.pola.rs/user-guide/plugins/io_plugins/

Markdown Content:
IO Plugins - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/plugins/io_plugins/#io-plugins)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 IO Plugins 

 Initializing search 

[pola-rs/polars](https://github.com/pola-rs/polars "Go to repository")

*   [Polars](https://docs.pola.rs/)
*   [Polars Cloud](https://docs.pola.rs/polars-cloud/)
*   [Polars on-premises](https://docs.pola.rs/polars-on-premises/)

[![Image 2: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide") Polars user guide  

[pola-rs/polars](https://github.com/pola-rs/polars "Go to repository")

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
            *   [Databases](https://docs.pola.rs/user-guide/io/database/)
            *   [Cloud storage](https://docs.pola.rs/user-guide/io/cloud-storage/)
            *   [Google BigQuery](https://docs.pola.rs/user-guide/io/bigquery/)
            *   [Hugging Face](https://docs.pola.rs/user-guide/io/hugging-face/)
            *   [Google Sheets (via Colab)](https://docs.pola.rs/user-guide/io/sheets_colab/)

        *   - [x] [Plugins](https://docs.pola.rs/user-guide/plugins/)  Plugins  
            *   [Expression Plugins](https://docs.pola.rs/user-guide/plugins/expr_plugins/)
            *   - [x]  IO Plugins  [IO Plugins](https://docs.pola.rs/user-guide/plugins/io_plugins/) Table of contents  
                *   [Use case](https://docs.pola.rs/user-guide/plugins/io_plugins/#use-case)
                *   [Example](https://docs.pola.rs/user-guide/plugins/io_plugins/#example)
                    *   [Parsing the schema](https://docs.pola.rs/user-guide/plugins/io_plugins/#parsing-the-schema)
                    *   [Writing the source](https://docs.pola.rs/user-guide/plugins/io_plugins/#writing-the-source)
                    *   [Taking it for a (very slow) spin](https://docs.pola.rs/user-guide/plugins/io_plugins/#taking-it-for-a-very-slow-spin)

                *   [Further reading](https://docs.pola.rs/user-guide/plugins/io_plugins/#further-reading)

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
*   [Use case](https://docs.pola.rs/user-guide/plugins/io_plugins/#use-case)
*   [Example](https://docs.pola.rs/user-guide/plugins/io_plugins/#example)
    *   [Parsing the schema](https://docs.pola.rs/user-guide/plugins/io_plugins/#parsing-the-schema)
    *   [Writing the source](https://docs.pola.rs/user-guide/plugins/io_plugins/#writing-the-source)
    *   [Taking it for a (very slow) spin](https://docs.pola.rs/user-guide/plugins/io_plugins/#taking-it-for-a-very-slow-spin)

*   [Further reading](https://docs.pola.rs/user-guide/plugins/io_plugins/#further-reading)

IO Plugins
==========

Besides [expression plugins](https://docs.pola.rs/user-guide/plugins/expr_plugins/), we also support IO plugins. These allow you to register different file formats as sources to the Polars engines. Because sources can move data zero copy via Arrow FFI and sources can produce large chunks of data before returning, we've decided to interface to IO plugins via Python for now, as we don't think the short time the GIL is needed should lead to any contention.

E.g. an IO source can read their dataframe's in rust and only at the rendez-vous move the data zero-copy having only a short time the GIL is needed.

Use case
--------

You want IO plugins if you have a source file not supported by Polars and you want to benefit from optimizations like projection pushdown, predicate pushdown, early stopping and support of our streaming engine.

Example
-------

So let's write a simple, very bad, custom CSV source and register that as an IO plugin. I want to stress that this is a very bad example and is only given for learning purposes.

First we define some imports we need:

```
# Use python for csv parsing.
import csv
import polars as pl
# Used to register a new generator on every instantiation.
from polars.io.plugins import register_io_source
from typing import Iterator
import io
```

### Parsing the schema

Every `scan` function in Polars has to be able to provide the schema of the data it reads. For this simple csv parser we will always read the data as `pl.String`. The only thing that differs are the field names and the number of fields.

```
def parse_schema(csv_str: str) -> pl.Schema:
    first_line = csv_str.split("\n")[0]

    return pl.Schema({k: pl.String for k in first_line.split(",")})
```

If we run this with small csv file `"a,b,c\n1,2,3"` we get the schema: `Schema([('a', String), ('b', String), ('c', String)])`.

```
>>> print(parse_schema("a,b,c\n1,2,3"))
Schema([('a', String), ('b', String), ('c', String)])
```

### Writing the source

Next up is the actual source. For this we create an outer and an inner function. The outer function `my_scan_csv` is the user facing function. This function will accept the file name and other potential arguments you would need for reading the source. For csv files, these arguments could be "delimiter", "quote_char" and such.

This outer function calls `register_io_source` which accepts a `callable` and a `schema`. The schema is the Polars schema of the complete source file (independent of projection pushdown).

The callable is a function that will return a generator that produces `pl.DataFrame` objects.

The arguments of this function are predefined and this function must accept:

*   `with_columns`

Columns that are projected. The reader must project these columns if applied

*   `predicate`

Polars expression. The reader must filter their rows accordingly.

*   `n_rows`

Materialize only n rows from the source. The reader can stop when `n_rows` are read.

*   `batch_size`

A hint of the ideal batch size the reader's generator must produce.

The inner function is the actual implementation of the IO source and can also call into Rust/C++ or wherever the IO plugin is written. If you want to see an IO source implemented in Rust, take a look at our [plugins repository](https://github.com/pola-rs/pyo3-polars/tree/main/example/io_plugin).

```
def my_scan_csv(csv_str: str) -> pl.LazyFrame:
    schema = parse_schema(csv_str)

    def source_generator(
        with_columns: list[str] | None,
        predicate: pl.Expr | None,
        n_rows: int | None,
        batch_size: int | None,
    ) -> Iterator[pl.DataFrame]:
        """
        Generator function that creates the source.
        This function will be registered as IO source.
        """
        if batch_size is None:
            batch_size = 100

        # Initialize the reader.
        reader = csv.reader(io.StringIO(csv_str), delimiter=',')
        # Skip the header.
        _ = next(reader)

        # Ensure we don't read more rows than requested from the engine
        while n_rows is None or n_rows > 0:
            if n_rows is not None:
                batch_size = min(batch_size, n_rows)

            rows = []

            for _ in range(batch_size):
                try:
                    row = next(reader)
                except StopIteration:
                    n_rows = 0
                    break
                rows.append(row)

            df = pl.from_records(rows, schema=schema, orient="row")
            n_rows -= df.height

            # If we would make a performant reader, we would not read these
            # columns at all.
            if with_columns is not None:
                df = df.select(with_columns)

            # If the source supports predicate pushdown, the expression can be parsed
            # to skip rows/groups.
            if predicate is not None:
                df = df.filter(predicate)

            yield df

    return register_io_source(io_source=source_generator, schema=schema)
```

### Taking it for a (very slow) spin

Finally we can test our source:

```
csv_str1 = """a,b,c,d
1,2,3,4
9,10,11,2
1,2,3,4
1,122,3,4"""

print(my_scan_csv(csv_str1).collect())

csv_str2 = """a,b
1,2
9,10
1,2
1,122"""

print(my_scan_csv(csv_str2).head(2).collect())
```

Running the script above would print the following output to the console:

```
shape: (4, 4)
┌─────┬─────┬─────┬─────┐
│ a   ┆ b   ┆ c   ┆ d   │
│ --- ┆ --- ┆ --- ┆ --- │
│ str ┆ str ┆ str ┆ str │
╞═════╪═════╪═════╪═════╡
│ 1   ┆ 2   ┆ 3   ┆ 4   │
│ 9   ┆ 10  ┆ 11  ┆ 2   │
│ 1   ┆ 2   ┆ 3   ┆ 4   │
│ 1   ┆ 122 ┆ 3   ┆ 4   │
└─────┴─────┴─────┴─────┘
shape: (2, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ str ┆ str │
╞═════╪═════╡
│ 1   ┆ 2   │
│ 9   ┆ 10  │
└─────┴─────┘
```

Further reading
---------------

*   [Rust example (distribution source)](https://github.com/pola-rs/pyo3-polars/tree/main/example/io_plugin)

[Previous Expression Plugins](https://docs.pola.rs/user-guide/plugins/expr_plugins/)[Next Introduction](https://docs.pola.rs/user-guide/sql/intro/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
