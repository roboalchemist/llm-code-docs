# Source: https://docs.pola.rs/user-guide/io/hugging-face/

Title: Hugging Face - Polars user guide

URL Source: https://docs.pola.rs/user-guide/io/hugging-face/

Published Time: Thu, 12 Mar 2026 14:44:20 GMT

Markdown Content:
Hugging Face - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/io/hugging-face/#hugging-face)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Hugging Face 

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
            *   - [x]  Hugging Face  [Hugging Face](https://docs.pola.rs/user-guide/io/hugging-face/) Table of contents  
                *   [Scanning datasets from Hugging Face](https://docs.pola.rs/user-guide/io/hugging-face/#scanning-datasets-from-hugging-face)
                    *   [Path format](https://docs.pola.rs/user-guide/io/hugging-face/#path-format)
                    *   [Authentication](https://docs.pola.rs/user-guide/io/hugging-face/#authentication)
                    *   [Examples](https://docs.pola.rs/user-guide/io/hugging-face/#examples)
                        *   [CSV](https://docs.pola.rs/user-guide/io/hugging-face/#csv)
                        *   [NDJSON](https://docs.pola.rs/user-guide/io/hugging-face/#ndjson)
                        *   [Parquet](https://docs.pola.rs/user-guide/io/hugging-face/#parquet)
                        *   [IPC](https://docs.pola.rs/user-guide/io/hugging-face/#ipc)

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
*   [Scanning datasets from Hugging Face](https://docs.pola.rs/user-guide/io/hugging-face/#scanning-datasets-from-hugging-face)
    *   [Path format](https://docs.pola.rs/user-guide/io/hugging-face/#path-format)
    *   [Authentication](https://docs.pola.rs/user-guide/io/hugging-face/#authentication)
    *   [Examples](https://docs.pola.rs/user-guide/io/hugging-face/#examples)
        *   [CSV](https://docs.pola.rs/user-guide/io/hugging-face/#csv)
        *   [NDJSON](https://docs.pola.rs/user-guide/io/hugging-face/#ndjson)
        *   [Parquet](https://docs.pola.rs/user-guide/io/hugging-face/#parquet)
        *   [IPC](https://docs.pola.rs/user-guide/io/hugging-face/#ipc)

Hugging Face
============

Scanning datasets from Hugging Face
-----------------------------------

All cloud-enabled scan functions, and their `read_` counterparts transparently support scanning from Hugging Face:

| Scan | Read |
| --- | --- |
| [scan_parquet](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html) | [read_parquet](https://docs.pola.rs/api/python/stable/reference/api/polars.read_parquet.html) |
| [scan_csv](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_csv.html) | [read_csv](https://docs.pola.rs/api/python/stable/reference/api/polars.read_csv.html) |
| [scan_ndjson](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_ndjson.html) | [read_ndjson](https://docs.pola.rs/api/python/stable/reference/api/polars.read_ndjson.html) |
| [scan_ipc](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_ipc.html) | [read_ipc](https://docs.pola.rs/api/python/stable/reference/api/polars.read_ipc.html) |

### Path format

To scan from Hugging Face, a `hf://` path can be passed to the scan functions. The `hf://` path format is defined as `hf://BUCKET/REPOSITORY@REVISION/PATH`, where:

*   `BUCKET` is one of `datasets` or `spaces`
*   `REPOSITORY` is the location of the repository, this is usually in the format of `username/repo_name`. A branch can also be optionally specified by appending `@branch`
*   `REVISION` is the name of the branch (or commit) to use. This is optional and defaults to `main` if not given.
*   `PATH` is a file or directory path, or a glob pattern from the repository root.

Example `hf://` paths:

| Path | Path components |
| --- | --- |
| hf://datasets/nameexhaustion/polars-docs/iris.csv | Bucket: datasets Repository: nameexhaustion/polars-docs Branch: main Path: iris.csv [Web URL](https://huggingface.co/datasets/nameexhaustion/polars-docs/tree/main/) |
| hf://datasets/nameexhaustion/polars-docs@foods/*.csv | Bucket: datasets Repository: nameexhaustion/polars-docs Branch: foods Path: *.csv [Web URL](https://huggingface.co/datasets/nameexhaustion/polars-docs/tree/foods/) |
| hf://datasets/nameexhaustion/polars-docs/hive_dates/ | Bucket: datasets Repository: nameexhaustion/polars-docs Branch: main Path: hive_dates/ [Web URL](https://huggingface.co/datasets/nameexhaustion/polars-docs/tree/main/hive_dates/) |
| hf://spaces/nameexhaustion/polars-docs/orders.feather | Bucket: spaces Repository: nameexhaustion/polars-docs Branch: main Path: orders.feather [Web URL](https://huggingface.co/spaces/nameexhaustion/polars-docs/tree/main/) |

### Authentication

A Hugging Face API key can be passed to Polars to access private locations using either of the following methods:

*   Passing a `token` in `storage_options` to the scan function, e.g. `scan_parquet(..., storage_options={'token': '<your HF token>'})`
*   Setting the `HF_TOKEN` environment variable, e.g. `export HF_TOKEN=<your HF token>`

### Examples

#### CSV

 Python 

[`scan_csv`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_csv.html)

```
print(pl.scan_csv("hf://datasets/nameexhaustion/polars-docs/iris.csv").collect())
```

```
shape: (150, 5)
┌──────────────┬─────────────┬──────────────┬─────────────┬───────────┐
│ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width ┆ species   │
│ ---          ┆ ---         ┆ ---          ┆ ---         ┆ ---       │
│ f64          ┆ f64         ┆ f64          ┆ f64         ┆ str       │
╞══════════════╪═════════════╪══════════════╪═════════════╪═══════════╡
│ 5.1          ┆ 3.5         ┆ 1.4          ┆ 0.2         ┆ setosa    │
│ 4.9          ┆ 3.0         ┆ 1.4          ┆ 0.2         ┆ setosa    │
│ 4.7          ┆ 3.2         ┆ 1.3          ┆ 0.2         ┆ setosa    │
│ 4.6          ┆ 3.1         ┆ 1.5          ┆ 0.2         ┆ setosa    │
│ 5.0          ┆ 3.6         ┆ 1.4          ┆ 0.2         ┆ setosa    │
│ …            ┆ …           ┆ …            ┆ …           ┆ …         │
│ 6.7          ┆ 3.0         ┆ 5.2          ┆ 2.3         ┆ virginica │
│ 6.3          ┆ 2.5         ┆ 5.0          ┆ 1.9         ┆ virginica │
│ 6.5          ┆ 3.0         ┆ 5.2          ┆ 2.0         ┆ virginica │
│ 6.2          ┆ 3.4         ┆ 5.4          ┆ 2.3         ┆ virginica │
│ 5.9          ┆ 3.0         ┆ 5.1          ┆ 1.8         ┆ virginica │
└──────────────┴─────────────┴──────────────┴─────────────┴───────────┘
```

See this file at [https://huggingface.co/datasets/nameexhaustion/polars-docs/blob/main/iris.csv](https://huggingface.co/datasets/nameexhaustion/polars-docs/blob/main/iris.csv)

#### NDJSON

 Python 

[`scan_ndjson`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_ndjson.html)

```
print(pl.scan_ndjson("hf://datasets/nameexhaustion/polars-docs/iris.jsonl").collect())
```

```
shape: (150, 5)
┌──────────────┬─────────────┬──────────────┬─────────────┬───────────┐
│ sepal_length ┆ sepal_width ┆ petal_length ┆ petal_width ┆ species   │
│ ---          ┆ ---         ┆ ---          ┆ ---         ┆ ---       │
│ f64          ┆ f64         ┆ f64          ┆ f64         ┆ str       │
╞══════════════╪═════════════╪══════════════╪═════════════╪═══════════╡
│ 5.1          ┆ 3.5         ┆ 1.4          ┆ 0.2         ┆ setosa    │
│ 4.9          ┆ 3.0         ┆ 1.4          ┆ 0.2         ┆ setosa    │
│ 4.7          ┆ 3.2         ┆ 1.3          ┆ 0.2         ┆ setosa    │
│ 4.6          ┆ 3.1         ┆ 1.5          ┆ 0.2         ┆ setosa    │
│ 5.0          ┆ 3.6         ┆ 1.4          ┆ 0.2         ┆ setosa    │
│ …            ┆ …           ┆ …            ┆ …           ┆ …         │
│ 6.7          ┆ 3.0         ┆ 5.2          ┆ 2.3         ┆ virginica │
│ 6.3          ┆ 2.5         ┆ 5.0          ┆ 1.9         ┆ virginica │
│ 6.5          ┆ 3.0         ┆ 5.2          ┆ 2.0         ┆ virginica │
│ 6.2          ┆ 3.4         ┆ 5.4          ┆ 2.3         ┆ virginica │
│ 5.9          ┆ 3.0         ┆ 5.1          ┆ 1.8         ┆ virginica │
└──────────────┴─────────────┴──────────────┴─────────────┴───────────┘
```

See this file at [https://huggingface.co/datasets/nameexhaustion/polars-docs/blob/main/iris.jsonl](https://huggingface.co/datasets/nameexhaustion/polars-docs/blob/main/iris.jsonl)

#### Parquet

 Python 

[`scan_parquet`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_parquet.html)

```
print(
    """\
shape: (4, 3)
┌────────────┬────────────────────────────┬─────┐
│ date1      ┆ date2                      ┆ x   │
│ ---        ┆ ---                        ┆ --- │
│ date       ┆ datetime[μs]               ┆ i32 │
╞════════════╪════════════════════════════╪═════╡
│ 2024-01-01 ┆ 2023-01-01 00:00:00        ┆ 1   │
│ 2024-02-01 ┆ 2023-02-01 00:00:00        ┆ 2   │
│ 2024-03-01 ┆ null                       ┆ 3   │
│ null       ┆ 2023-03-01 01:01:01.000001 ┆ 4   │
└────────────┴────────────────────────────┴─────┘
"""
)
```

```
shape: (4, 3)
┌────────────┬────────────────────────────┬─────┐
│ date1      ┆ date2                      ┆ x   │
│ ---        ┆ ---                        ┆ --- │
│ date       ┆ datetime[μs]               ┆ i32 │
╞════════════╪════════════════════════════╪═════╡
│ 2024-01-01 ┆ 2023-01-01 00:00:00        ┆ 1   │
│ 2024-02-01 ┆ 2023-02-01 00:00:00        ┆ 2   │
│ 2024-03-01 ┆ null                       ┆ 3   │
│ null       ┆ 2023-03-01 01:01:01.000001 ┆ 4   │
└────────────┴────────────────────────────┴─────┘
```

See this folder at [https://huggingface.co/datasets/nameexhaustion/polars-docs/tree/main/hive_dates/](https://huggingface.co/datasets/nameexhaustion/polars-docs/tree/main/hive_dates/)

#### IPC

 Python 

[`scan_ipc`](https://docs.pola.rs/api/python/stable/reference/api/polars.scan_ipc.html)

```
print(pl.scan_ipc("hf://spaces/nameexhaustion/polars-docs/orders.feather").collect())
```

```
shape: (10, 9)
┌────────────┬───────────┬───────────────┬──────────────┬───┬─────────────────┬─────────────────┬────────────────┬─────────────────────────┐
│ o_orderkey ┆ o_custkey ┆ o_orderstatus ┆ o_totalprice ┆ … ┆ o_orderpriority ┆ o_clerk         ┆ o_shippriority ┆ o_comment               │
│ ---        ┆ ---       ┆ ---           ┆ ---          ┆   ┆ ---             ┆ ---             ┆ ---            ┆ ---                     │
│ i64        ┆ i64       ┆ str           ┆ f64          ┆   ┆ str             ┆ str             ┆ i64            ┆ str                     │
╞════════════╪═══════════╪═══════════════╪══════════════╪═══╪═════════════════╪═════════════════╪════════════════╪═════════════════════════╡
│ 1          ┆ 36901     ┆ O             ┆ 173665.47    ┆ … ┆ 5-LOW           ┆ Clerk#000000951 ┆ 0              ┆ nstructions sleep       │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ furiously am…           │
│ 2          ┆ 78002     ┆ O             ┆ 46929.18     ┆ … ┆ 1-URGENT        ┆ Clerk#000000880 ┆ 0              ┆ foxes. pending accounts │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ at th…                  │
│ 3          ┆ 123314    ┆ F             ┆ 193846.25    ┆ … ┆ 5-LOW           ┆ Clerk#000000955 ┆ 0              ┆ sly final accounts      │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ boost. care…            │
│ 4          ┆ 136777    ┆ O             ┆ 32151.78     ┆ … ┆ 5-LOW           ┆ Clerk#000000124 ┆ 0              ┆ sits. slyly regular     │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ warthogs c…             │
│ 5          ┆ 44485     ┆ F             ┆ 144659.2     ┆ … ┆ 5-LOW           ┆ Clerk#000000925 ┆ 0              ┆ quickly. bold deposits  │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ sleep s…                │
│ 6          ┆ 55624     ┆ F             ┆ 58749.59     ┆ … ┆ 4-NOT SPECIFIED ┆ Clerk#000000058 ┆ 0              ┆ ggle. special, final    │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ requests …              │
│ 7          ┆ 39136     ┆ O             ┆ 252004.18    ┆ … ┆ 2-HIGH          ┆ Clerk#000000470 ┆ 0              ┆ ly special requests     │
│ 32         ┆ 130057    ┆ O             ┆ 208660.75    ┆ … ┆ 2-HIGH          ┆ Clerk#000000616 ┆ 0              ┆ ise blithely bold,      │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ regular req…            │
│ 33         ┆ 66958     ┆ F             ┆ 163243.98    ┆ … ┆ 3-MEDIUM        ┆ Clerk#000000409 ┆ 0              ┆ uriously. furiously     │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ final requ…             │
│ 34         ┆ 61001     ┆ O             ┆ 58949.67     ┆ … ┆ 3-MEDIUM        ┆ Clerk#000000223 ┆ 0              ┆ ly final packages.      │
│            ┆           ┆               ┆              ┆   ┆                 ┆                 ┆                ┆ fluffily fi…            │
└────────────┴───────────┴───────────────┴──────────────┴───┴─────────────────┴─────────────────┴────────────────┴─────────────────────────┘
```

See this file at [https://huggingface.co/spaces/nameexhaustion/polars-docs/blob/main/orders.feather](https://huggingface.co/spaces/nameexhaustion/polars-docs/blob/main/orders.feather)

[Previous Google BigQuery](https://docs.pola.rs/user-guide/io/bigquery/)[Next Google Sheets (via Colab)](https://docs.pola.rs/user-guide/io/sheets_colab/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
