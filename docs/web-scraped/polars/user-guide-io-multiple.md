# Source: https://docs.pola.rs/user-guide/io/multiple/

Title: Multiple - Polars user guide

URL Source: https://docs.pola.rs/user-guide/io/multiple/

Markdown Content:
Multiple - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/io/multiple/#dealing-with-multiple-files)

[![Image 2: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Multiple 

 Initializing search 

[pola-rs/polars](https://github.com/pola-rs/polars "Go to repository")

*   [Polars](https://docs.pola.rs/)
*   [Polars Cloud](https://docs.pola.rs/polars-cloud/)
*   [Polars on-premises](https://docs.pola.rs/polars-on-premises/)

[![Image 3: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide") Polars user guide  

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
            *   - [x]  Multiple  [Multiple](https://docs.pola.rs/user-guide/io/multiple/) Table of contents  
                *   [Dealing with multiple files.](https://docs.pola.rs/user-guide/io/multiple/#dealing-with-multiple-files)
                *   [Reading into a single DataFrame](https://docs.pola.rs/user-guide/io/multiple/#reading-into-a-single-dataframe)
                *   [Reading and processing in parallel](https://docs.pola.rs/user-guide/io/multiple/#reading-and-processing-in-parallel)

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
*   [Dealing with multiple files.](https://docs.pola.rs/user-guide/io/multiple/#dealing-with-multiple-files)
*   [Reading into a single DataFrame](https://docs.pola.rs/user-guide/io/multiple/#reading-into-a-single-dataframe)
*   [Reading and processing in parallel](https://docs.pola.rs/user-guide/io/multiple/#reading-and-processing-in-parallel)

Multiple
========

Dealing with multiple files.
----------------------------

Polars can deal with multiple files differently depending on your needs and memory strain.

Let's create some files to give us some context:

 Python 

[`write_csv`](https://docs.pola.rs/api/python/stable/reference/api/polars.DataFrame.write_csv.html)

```
import polars as pl

df = pl.DataFrame({"foo": [1, 2, 3], "bar": [None, "ham", "spam"]})

for i in range(5):
    df.write_csv(f"docs/assets/data/my_many_files_{i}.csv")
```

Reading into a single `DataFrame`
---------------------------------

To read multiple files into a single `DataFrame`, we can use globbing patterns:

 Python 

[`read_csv`](https://docs.pola.rs/api/python/stable/reference/api/polars.read_csv.html)

```
df = pl.read_csv("docs/assets/data/my_many_files_*.csv")
print(df)
```

```
shape: (15, 2)
┌─────┬──────┐
│ foo ┆ bar  │
│ --- ┆ ---  │
│ i64 ┆ str  │
╞═════╪══════╡
│ 1   ┆ null │
│ 2   ┆ ham  │
│ 3   ┆ spam │
│ 1   ┆ null │
│ 2   ┆ ham  │
│ …   ┆ …    │
│ 2   ┆ ham  │
│ 3   ┆ spam │
│ 1   ┆ null │
│ 2   ┆ ham  │
│ 3   ┆ spam │
└─────┴──────┘
```

To see how this works we can take a look at the query plan. Below we see that all files are read separately and concatenated into a single `DataFrame`. Polars will try to parallelize the reading.

 Python 

[`show_graph`](https://docs.pola.rs/api/python/stable/reference/lazyframe/api/polars.LazyFrame.show_graph.html)

```
pl.scan_csv("docs/assets/data/my_many_files_*.csv").show_graph()
```

![Image 4](blob:http://localhost/c63bb0033087162889b138bdf8b8ad49)

Reading and processing in parallel
----------------------------------

If your files don't have to be in a single table you can also build a query plan for each file and execute them in parallel on the Polars thread pool.

All query plan execution is embarrassingly parallel and doesn't require any communication.

 Python 

[`scan_csv`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_csv.html)

```
import glob

import polars as pl

queries = []
for file in glob.glob("docs/assets/data/my_many_files_*.csv"):
    q = pl.scan_csv(file).group_by("bar").agg(pl.len(), pl.sum("foo"))
    queries.append(q)

dataframes = pl.collect_all(queries)
print(dataframes)
```

```
[shape: (3, 3)
┌──────┬─────┬─────┐
│ bar  ┆ len ┆ foo │
│ ---  ┆ --- ┆ --- │
│ str  ┆ u32 ┆ i64 │
╞══════╪═════╪═════╡
│ null ┆ 1   ┆ 1   │
│ ham  ┆ 1   ┆ 2   │
│ spam ┆ 1   ┆ 3   │
└──────┴─────┴─────┘, shape: (3, 3)
┌──────┬─────┬─────┐
│ bar  ┆ len ┆ foo │
│ ---  ┆ --- ┆ --- │
│ str  ┆ u32 ┆ i64 │
╞══════╪═════╪═════╡
│ ham  ┆ 1   ┆ 2   │
│ null ┆ 1   ┆ 1   │
│ spam ┆ 1   ┆ 3   │
└──────┴─────┴─────┘, shape: (3, 3)
┌──────┬─────┬─────┐
│ bar  ┆ len ┆ foo │
│ ---  ┆ --- ┆ --- │
│ str  ┆ u32 ┆ i64 │
╞══════╪═════╪═════╡
│ ham  ┆ 1   ┆ 2   │
│ null ┆ 1   ┆ 1   │
│ spam ┆ 1   ┆ 3   │
└──────┴─────┴─────┘, shape: (3, 3)
┌──────┬─────┬─────┐
│ bar  ┆ len ┆ foo │
│ ---  ┆ --- ┆ --- │
│ str  ┆ u32 ┆ i64 │
╞══════╪═════╪═════╡
│ spam ┆ 1   ┆ 3   │
│ null ┆ 1   ┆ 1   │
│ ham  ┆ 1   ┆ 2   │
└──────┴─────┴─────┘, shape: (3, 3)
┌──────┬─────┬─────┐
│ bar  ┆ len ┆ foo │
│ ---  ┆ --- ┆ --- │
│ str  ┆ u32 ┆ i64 │
╞══════╪═════╪═════╡
│ ham  ┆ 1   ┆ 2   │
│ null ┆ 1   ┆ 1   │
│ spam ┆ 1   ┆ 3   │
└──────┴─────┴─────┘]
```

[Previous JSON files](https://docs.pola.rs/user-guide/io/json/)[Next Hive](https://docs.pola.rs/user-guide/io/hive/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
