# Source: https://docs.pola.rs/releases/upgrade/0.19/

Title: Version 0.19 - Polars user guide

URL Source: https://docs.pola.rs/releases/upgrade/0.19/

Markdown Content:
Version 0.19 - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/releases/upgrade/0.19/#version-019)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Version 0.19 

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
            *   - [x]  Version 0.19  [Version 0.19](https://docs.pola.rs/releases/upgrade/0.19/) Table of contents  
                *   [Breaking changes](https://docs.pola.rs/releases/upgrade/0.19/#breaking-changes)
                    *   [Aggregation functions no longer support horizontal computation](https://docs.pola.rs/releases/upgrade/0.19/#aggregation-functions-no-longer-support-horizontal-computation)
                    *   [Update to all / any](https://docs.pola.rs/releases/upgrade/0.19/#update-to-all-any)
                    *   [Improved error types for many methods](https://docs.pola.rs/releases/upgrade/0.19/#improved-error-types-for-many-methods)
                    *   [Updates to expression input parsing](https://docs.pola.rs/releases/upgrade/0.19/#updates-to-expression-input-parsing)
                    *   [shuffle / sample now use an internal Polars seed](https://docs.pola.rs/releases/upgrade/0.19/#shuffle-sample-now-use-an-internal-polars-seed)

                *   [Deprecations](https://docs.pola.rs/releases/upgrade/0.19/#deprecations)
                    *   [groupby renamed to group_by](https://docs.pola.rs/releases/upgrade/0.19/#groupby-renamed-to-group_by)
                    *   [apply renamed to map_*](https://docs.pola.rs/releases/upgrade/0.19/#apply-renamed-to-map_)

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
*   [Breaking changes](https://docs.pola.rs/releases/upgrade/0.19/#breaking-changes)
    *   [Aggregation functions no longer support horizontal computation](https://docs.pola.rs/releases/upgrade/0.19/#aggregation-functions-no-longer-support-horizontal-computation)
    *   [Update to all / any](https://docs.pola.rs/releases/upgrade/0.19/#update-to-all-any)
    *   [Improved error types for many methods](https://docs.pola.rs/releases/upgrade/0.19/#improved-error-types-for-many-methods)
    *   [Updates to expression input parsing](https://docs.pola.rs/releases/upgrade/0.19/#updates-to-expression-input-parsing)
    *   [shuffle / sample now use an internal Polars seed](https://docs.pola.rs/releases/upgrade/0.19/#shuffle-sample-now-use-an-internal-polars-seed)

*   [Deprecations](https://docs.pola.rs/releases/upgrade/0.19/#deprecations)
    *   [groupby renamed to group_by](https://docs.pola.rs/releases/upgrade/0.19/#groupby-renamed-to-group_by)
    *   [apply renamed to map_*](https://docs.pola.rs/releases/upgrade/0.19/#apply-renamed-to-map_)

Version 0.19
============

Breaking changes
----------------

### Aggregation functions no longer support horizontal computation

This impacts aggregation functions like `sum`, `min`, and `max`. These functions were overloaded to support both vertical and horizontal computation. Recently, new dedicated functionality for horizontal computation was released, and horizontal computation was deprecated.

Restore the old behavior by using the horizontal variant, e.g. `sum_horizontal`.

**Example**

Before:

```
>>> df = pl.DataFrame({'a': [1, 2], 'b': [11, 12]})
>>> df.select(pl.sum('a', 'b'))  # horizontal computation
shape: (2, 1)
┌─────┐
│ sum │
│ --- │
│ i64 │
╞═════╡
│ 12  │
│ 14  │
└─────┘
```

After:

```
>>> df = pl.DataFrame({'a': [1, 2], 'b': [11, 12]})
>>> df.select(pl.sum('a', 'b'))  # vertical computation
shape: (1, 2)
┌─────┬─────┐
│ a   ┆ b   │
│ --- ┆ --- │
│ i64 ┆ i64 │
╞═════╪═════╡
│ 3   ┆ 23  │
└─────┴─────┘
```

### Update to `all` / `any`

`all` will now ignore null values by default, rather than treat them as `False`.

For both `any` and `all`, the `drop_nulls` parameter has been renamed to `ignore_nulls` and is now keyword-only. Also fixed an issue when setting this parameter to `False` would erroneously result in `None` output in some cases.

To restore the old behavior, set `ignore_nulls` to `False` and check for `None` output.

**Example**

Before:

```
>>> pl.Series([True, None]).all()
False
```

After:

```
>>> pl.Series([True, None]).all()
True
```

### Improved error types for many methods

Improving our error messages is an ongoing effort. We did a sweep of our Python code base and made many improvements to error messages and error types. Most notably, many `ValueError`s were changed to `TypeError`s.

If your code relies on handling Polars exceptions, you may have to make some adjustments.

**Example**

Before:

```
>>> pl.Series(values=15)
...
ValueError: Series constructor called with unsupported type; got 'int'
```

After:

```
>>> pl.Series(values=15)
...
TypeError: Series constructor called with unsupported type 'int' for the `values` parameter
```

### Updates to expression input parsing

Methods like `select` and `with_columns` accept one or more expressions. But they also accept strings, integers, lists, and other inputs that we try to interpret as expressions. We updated our internal logic to parse inputs more consistently.

**Example**

Before:

```
>>> pl.DataFrame({'a': [1, 2]}).with_columns(None)
shape: (2, 1)
┌─────┐
│ a   │
│ --- │
│ i64 │
╞═════╡
│ 1   │
│ 2   │
└─────┘
```

After:

```
>>> pl.DataFrame({'a': [1, 2]}).with_columns(None)
shape: (2, 2)
┌─────┬─────────┐
│ a   ┆ literal │
│ --- ┆ ---     │
│ i64 ┆ null    │
╞═════╪═════════╡
│ 1   ┆ null    │
│ 2   ┆ null    │
└─────┴─────────┘
```

### `shuffle` / `sample` now use an internal Polars seed

If you used the built-in Python `random.seed` function to control the randomness of Polars expressions, this will no longer work. Instead, use the new `set_random_seed` function.

**Example**

Before:

```
import random

random.seed(1)
```

After:

```
import polars as pl

pl.set_random_seed(1)
```

Deprecations
------------

Creating a consistent and intuitive API is hard; finding the right name for each function, method, and parameter might be the hardest part. The new version comes with several naming changes, and you will most likely run into deprecation warnings when upgrading to `0.19`.

If you want to upgrade without worrying about deprecation warnings right now, you can add the following snippet to your code:

```
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
```

### `groupby` renamed to `group_by`

This is not a change we make lightly, as it will impact almost all our users. But "group by" is really two different words, and our naming strategy dictates that these should be separated by an underscore.

Most likely, a simple search and replace will be enough to take care of this update:

*   Search: `.groupby(`
*   Replace: `.group_by(`

### `apply` renamed to `map_*`

`apply` is probably the most misused part of our API. Many Polars users come from pandas, where `apply` has a completely different meaning.

We now consolidate all our functionality for user-defined functions under the name `map`. This results in the following renaming:

| Before | After |
| --- | --- |
| `Series/Expr.apply` | `map_elements` |
| `Series/Expr.rolling_apply` | `rolling_map` |
| `DataFrame.apply` | `map_rows` |
| `GroupBy.apply` | `map_groups` |
| `apply` | `map_groups` |
| `map` | `map_batches` |

[Previous Version 0.20](https://docs.pola.rs/releases/upgrade/0.20/)[Next Changelog](https://docs.pola.rs/releases/changelog/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
