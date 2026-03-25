# Source: https://docs.pola.rs/user-guide/lazy/multiplexing/

Title: Multiplexing queries - Polars user guide

URL Source: https://docs.pola.rs/user-guide/lazy/multiplexing/

Markdown Content:
Multiplexing queries - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/lazy/multiplexing/#multiplexing-queries)

[![Image 4: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Multiplexing queries 

 Initializing search 

[pola-rs/polars](https://github.com/pola-rs/polars "Go to repository")

*   [Polars](https://docs.pola.rs/)
*   [Polars Cloud](https://docs.pola.rs/polars-cloud/)
*   [Polars on-premises](https://docs.pola.rs/polars-on-premises/)

[![Image 5: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide") Polars user guide  

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
            *   - [x]  Multiplexing queries  [Multiplexing queries](https://docs.pola.rs/user-guide/lazy/multiplexing/) Table of contents  
                *   [Eager](https://docs.pola.rs/user-guide/lazy/multiplexing/#eager)
                *   [Lazy](https://docs.pola.rs/user-guide/lazy/multiplexing/#lazy)
                *   [Combine the query plans](https://docs.pola.rs/user-guide/lazy/multiplexing/#combine-the-query-plans)

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
*   [Eager](https://docs.pola.rs/user-guide/lazy/multiplexing/#eager)
*   [Lazy](https://docs.pola.rs/user-guide/lazy/multiplexing/#lazy)
*   [Combine the query plans](https://docs.pola.rs/user-guide/lazy/multiplexing/#combine-the-query-plans)

Multiplexing queries
====================

In the [Sources and Sinks](https://docs.pola.rs/user-guide/lazy/sources_sinks/) page, we already discussed multiplexing as a way to split a query into multiple sinks. This page will go a bit deeper in this concept, as it is important to understand when combining `LazyFrame`s with procedural programming constructs.

When dealing with eager dataframes, it is very common to keep state in a temporary variable. Let's look at the following example. Below we create a `DataFrame` with 10 unique elements in a random order (so that Polars doesn't hit any fast paths for sorted keys).

 Python 

```
np.random.seed(0)
a = np.arange(0, 10)
np.random.shuffle(a)
df = pl.DataFrame({"n": a})
print(df)
```

```
shape: (10, 1)
┌─────┐
│ n   │
│ --- │
│ i64 │
╞═════╡
│ 2   │
│ 8   │
│ 4   │
│ 9   │
│ 1   │
│ 6   │
│ 7   │
│ 3   │
│ 0   │
│ 5   │
└─────┘
```

Eager
-----

If you deal with the Polars eager API, making a variable and iterating over that temporary `DataFrame` gives the result you expect, as the result of the group-by is stored in `df1`. Even though the output order is unstable, it doesn't matter as it is eagerly evaluated. The follow snippet therefore doesn't raise and the assert passes.

 Python 

```
# A group-by doesn't guarantee order
df1 = df.group_by("n").len()

# Take the lower half and the upper half in a list
out = [df1.slice(offset=i * 5, length=5) for i in range(2)]

# Assert df1 is equal to the sum of both halves
pl.testing.assert_frame_equal(df1, pl.concat(out))
```

Lazy
----

Now if we tried this naively with `LazyFrame`s, this would fail.

 Python 

```
lf1 = df.lazy().group_by("n").len()

out = [lf1.slice(offset=i * 5, length=5).collect() for i in range(2)]

pl.testing.assert_frame_equal(lf1.collect(), pl.concat(out))
```

```
AssertionError: DataFrames are different (value mismatch for column 'n')
[left]:  [9, 2, 0, 5, 3, 1, 7, 8, 6, 4]
[right]: [0, 9, 6, 8, 2, 5, 4, 3, 1, 7]
```

The reason this fails is that `lf1` doesn't contain the materialized result of `df.lazy().group_by("n").len()`, it instead holds the query plan in that variable.

![Image 6](blob:http://localhost/92d256a9ddfda4bd9030a12f4898797a)

This means that every time we branch of this `LazyFrame` and call `collect` we re-evaluate the group-by. Besides being expensive, this also leads to unexpected results if you assume that the output is stable (which isn't the case here).

In the example above you are actually evaluating 2 query plans:

**Plan 1**

![Image 7](blob:http://localhost/b22134eba41bc51118615d6031b3d50b)

**Plan 2**

![Image 8](blob:http://localhost/561a1601f2d8581df33e9f4d62824f96)

Combine the query plans
-----------------------

To circumvent this, we must give Polars the opportunity to look at all the query plans in a single optimization and execution pass. This can be done by passing the diverging `LazyFrame`'s to the `collect_all` function.

 Python 

```
lf1 = df.lazy().group_by("n").len()

out = [lf1.slice(offset=i * 5, length=5) for i in range(2)]
results = pl.collect_all([lf1] + out)

pl.testing.assert_frame_equal(results[0], pl.concat(results[1:]))
```

If we explain the combined queries with `pl.explain_all`, we can also observe that they are shared under a single "SINK_MULTIPLE" evaluation and that the optimizer has recognized that parts of the query come from the same subplan, indicated by the inserted "CACHE" nodes.

```
SINK_MULTIPLE
  PLAN 0:
    CACHE[id: 8c7b6d16-b60e-4e72-a8c7-9eaee90d852e]
      AGGREGATE[maintain_order: false]
        [len()] BY [col("n")]
        FROM
        DF ["n"]; PROJECT */1 COLUMNS
  PLAN 1:
    SLICE[offset: 0, len: 5]
      CACHE[id: 8c7b6d16-b60e-4e72-a8c7-9eaee90d852e]
        AGGREGATE[maintain_order: false]
          [len()] BY [col("n")]
          FROM
          DF ["n"]; PROJECT */1 COLUMNS
  PLAN 2:
    SLICE[offset: 5, len: 5]
      CACHE[id: 8c7b6d16-b60e-4e72-a8c7-9eaee90d852e]
        AGGREGATE[maintain_order: false]
          [len()] BY [col("n")]
          FROM
          DF ["n"]; PROJECT */1 COLUMNS
END SINK_MULTIPLE
```

Combining related subplans in a single execution unit with `pl.collect_all` can thus lead to large performance increases and allows diverging query plans, storing temporary tables, and a more procedural programming style.

[Previous Sources and sinks](https://docs.pola.rs/user-guide/lazy/sources_sinks/)[Next GPU Support](https://docs.pola.rs/user-guide/lazy/gpu/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
