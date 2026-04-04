# Source: https://docs.pola.rs/user-guide/misc/arrow/

Title: consumer - Polars user guide

URL Source: https://docs.pola.rs/user-guide/misc/arrow/

Markdown Content:
Arrow producer/consumer - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/misc/arrow/#arrow-producerconsumer)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Arrow producer/consumer 

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
            *   [Databases](https://docs.pola.rs/user-guide/io/database/)
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
            *   - [x]  Arrow producer/consumer  [Arrow producer/consumer](https://docs.pola.rs/user-guide/misc/arrow/) Table of contents  
                *   [Using pyarrow](https://docs.pola.rs/user-guide/misc/arrow/#using-pyarrow)
                *   [Using the Arrow PyCapsule Interface](https://docs.pola.rs/user-guide/misc/arrow/#using-the-arrow-pycapsule-interface)
                    *   [Exporting data from Polars to pyarrow](https://docs.pola.rs/user-guide/misc/arrow/#exporting-data-from-polars-to-pyarrow)
                    *   [Importing data from pyarrow to Polars](https://docs.pola.rs/user-guide/misc/arrow/#importing-data-from-pyarrow-to-polars)
                    *   [Usage with other arrow libraries](https://docs.pola.rs/user-guide/misc/arrow/#usage-with-other-arrow-libraries)
                    *   [For library maintainers](https://docs.pola.rs/user-guide/misc/arrow/#for-library-maintainers)

                *   [Using Polars directly](https://docs.pola.rs/user-guide/misc/arrow/#using-polars-directly)

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
*   [Using pyarrow](https://docs.pola.rs/user-guide/misc/arrow/#using-pyarrow)
*   [Using the Arrow PyCapsule Interface](https://docs.pola.rs/user-guide/misc/arrow/#using-the-arrow-pycapsule-interface)
    *   [Exporting data from Polars to pyarrow](https://docs.pola.rs/user-guide/misc/arrow/#exporting-data-from-polars-to-pyarrow)
    *   [Importing data from pyarrow to Polars](https://docs.pola.rs/user-guide/misc/arrow/#importing-data-from-pyarrow-to-polars)
    *   [Usage with other arrow libraries](https://docs.pola.rs/user-guide/misc/arrow/#usage-with-other-arrow-libraries)
    *   [For library maintainers](https://docs.pola.rs/user-guide/misc/arrow/#for-library-maintainers)

*   [Using Polars directly](https://docs.pola.rs/user-guide/misc/arrow/#using-polars-directly)

Arrow producer/consumer
=======================

Using pyarrow
-------------

Polars can move data in and out of arrow zero copy. This can be done either via pyarrow or natively. Let's first start by showing the pyarrow solution:

 Python 

```
import polars as pl

df = pl.DataFrame({"foo": [1, 2, 3], "bar": ["ham", "spam", "jam"]})

arrow_table = df.to_arrow()
print(arrow_table)
```

```
pyarrow.Table
foo: int64
bar: large_string
----
foo: [[1,2,3]]
bar: [["ham","spam","jam"]]
```

Or if you want to ensure the output is zero-copy:

 Python 

```
arrow_table_zero_copy = df.to_arrow(compat_level=pl.CompatLevel.newest())
print(arrow_table_zero_copy)
```

```
pyarrow.Table
foo: int64
bar: string_view
----
foo: [[1,2,3]]
bar: [["ham","spam","jam"]]
```

Importing from pyarrow can be achieved with `pl.from_arrow`.

Using the Arrow PyCapsule Interface
-----------------------------------

As of Polars v1.3 and higher, Polars implements the [Arrow PyCapsule Interface](https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html), a protocol for sharing Arrow data across Python libraries.

### Exporting data from Polars to pyarrow

To convert a Polars `DataFrame` to a `pyarrow.Table`, use the `pyarrow.table` constructor:

Note

This requires pyarrow v15 or higher.

 Python 

```
import polars as pl
import pyarrow as pa

df = pl.DataFrame({"foo": [1, 2, 3], "bar": ["ham", "spam", "jam"]})
arrow_table = pa.table(df)
print(arrow_table)
```

```
pyarrow.Table
foo: int64
bar: string_view
----
foo: [[1,2,3]]
bar: [["ham","spam","jam"]]
```

To convert a Polars `Series` to a `pyarrow.ChunkedArray`, use the `pyarrow.chunked_array` constructor.

 Python 

```
arrow_chunked_array = pa.chunked_array(df["foo"])
print(arrow_chunked_array)
```

```
[
  [
    1,
    2,
    3
  ]
]
```

You can also pass a `Series` to the `pyarrow.array` constructor to create a contiguous array. Note that this will not be zero-copy if the underlying `Series` had multiple chunks.

 Python 

```
arrow_array = pa.array(df["foo"])
print(arrow_array)
```

```
[
  1,
  2,
  3
]
```

### Importing data from pyarrow to Polars

We can pass the pyarrow `Table` back to Polars by using the `polars.DataFrame` constructor:

 Python 

```
polars_df = pl.DataFrame(arrow_table)
print(polars_df)
```

```
shape: (3, 2)
┌─────┬──────┐
│ foo ┆ bar  │
│ --- ┆ ---  │
│ i64 ┆ str  │
╞═════╪══════╡
│ 1   ┆ ham  │
│ 2   ┆ spam │
│ 3   ┆ jam  │
└─────┴──────┘
```

Similarly, we can pass the pyarrow `ChunkedArray` or `Array` back to Polars by using the `polars.Series` constructor:

 Python 

```
polars_series = pl.Series(arrow_chunked_array)
print(polars_series)
```

```
shape: (3,)
Series: '' [i64]
[
    1
    2
    3
]
```

### Usage with other arrow libraries

There's a [growing list](https://github.com/apache/arrow/issues/39195#issuecomment-2245718008) of libraries that support the PyCapsule Interface directly. Polars `Series` and `DataFrame` objects work automatically with every such library.

### For library maintainers

If you're developing a library that you wish to integrate with Polars, it's suggested to implement the [Arrow PyCapsule Interface](https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html) yourself. This comes with a number of benefits:

*   Zero-copy exchange for both Polars Series and DataFrame
*   No required dependency on pyarrow.
*   No direct dependency on Polars.
*   Harder to cause memory leaks than handling pointers as raw integers.
*   Automatic zero-copy integration other PyCapsule Interface-supported libraries.

Using Polars directly
---------------------

Polars can also consume and export to and import from the [Arrow C Data Interface](https://arrow.apache.org/docs/format/CDataInterface.html) directly. This is recommended for libraries that don't support the Arrow PyCapsule Interface and want to interop with Polars without requiring a pyarrow installation.

*   To export `ArrowArray` C structs, Polars exposes: `Series._export_arrow_to_c`.
*   To import an `ArrowArray` C struct, Polars exposes `Series._import_arrow_from_c`.

[Previous Comparison with other tools](https://docs.pola.rs/user-guide/misc/comparison/)[Next Generating Polars code with LLMs](https://docs.pola.rs/user-guide/misc/polars_llms/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
