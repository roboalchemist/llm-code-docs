# Source: https://docs.pola.rs/user-guide/migration/spark/

Title: Coming from Apache Spark - Polars user guide

URL Source: https://docs.pola.rs/user-guide/migration/spark/

Markdown Content:
Coming from Apache Spark - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/migration/spark/#coming-from-apache-spark)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Coming from Apache Spark 

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
            *   [IO Plugins](https://docs.pola.rs/user-guide/plugins/io_plugins/)

        *   - [x]  SQL   SQL  
            *   [Introduction](https://docs.pola.rs/user-guide/sql/intro/)
            *   [SHOW TABLES](https://docs.pola.rs/user-guide/sql/show/)
            *   [SELECT](https://docs.pola.rs/user-guide/sql/select/)
            *   [CREATE](https://docs.pola.rs/user-guide/sql/create/)
            *   [Common Table Expressions](https://docs.pola.rs/user-guide/sql/cte/)

        *   - [x]  Migrating   Migrating  
            *   [Coming from Pandas](https://docs.pola.rs/user-guide/migration/pandas/)
            *   - [x]  Coming from Apache Spark  [Coming from Apache Spark](https://docs.pola.rs/user-guide/migration/spark/) Table of contents  
                *   [Column-based API vs. Row-based API](https://docs.pola.rs/user-guide/migration/spark/#column-based-api-vs-row-based-api)
                    *   [Example 1: Combining head and sum](https://docs.pola.rs/user-guide/migration/spark/#example-1-combining-head-and-sum)
                    *   [Example 2: Combining Two heads](https://docs.pola.rs/user-guide/migration/spark/#example-2-combining-two-heads)
                    *   [Example 3: Composing expressions](https://docs.pola.rs/user-guide/migration/spark/#example-3-composing-expressions)

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
*   [Column-based API vs. Row-based API](https://docs.pola.rs/user-guide/migration/spark/#column-based-api-vs-row-based-api)
    *   [Example 1: Combining head and sum](https://docs.pola.rs/user-guide/migration/spark/#example-1-combining-head-and-sum)
    *   [Example 2: Combining Two heads](https://docs.pola.rs/user-guide/migration/spark/#example-2-combining-two-heads)
    *   [Example 3: Composing expressions](https://docs.pola.rs/user-guide/migration/spark/#example-3-composing-expressions)

Coming from Apache Spark
========================

Column-based API vs. Row-based API
----------------------------------

Whereas the `Spark``DataFrame` is analogous to a collection of rows, a Polars `DataFrame` is closer to a collection of columns. This means that you can combine columns in Polars in ways that are not possible in `Spark`, because `Spark` preserves the relationship of the data in each row.

Consider this sample dataset:

```
import polars as pl

df = pl.DataFrame({
    "foo": ["a", "b", "c", "d", "d"],
    "bar": [1, 2, 3, 4, 5],
})

dfs = spark.createDataFrame(
    [
        ("a", 1),
        ("b", 2),
        ("c", 3),
        ("d", 4),
        ("d", 5),
    ],
    schema=["foo", "bar"],
)
```

### Example 1: Combining `head` and `sum`

In Polars you can write something like this:

```
df.select(
    pl.col("foo").sort().head(2),
    pl.col("bar").filter(pl.col("foo") == "d").sum()
)
```

Output:

```
shape: (2, 2)
┌─────┬─────┐
│ foo ┆ bar │
│ --- ┆ --- │
│ str ┆ i64 │
╞═════╪═════╡
│ a   ┆ 9   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ b   ┆ 9   │
└─────┴─────┘
```

The expressions on columns `foo` and `bar` are completely independent. Since the expression on `bar` returns a single value, that value is repeated for each value output by the expression on `foo`. But `a` and `b` have no relation to the data that produced the sum of `9`.

To do something similar in `Spark`, you'd need to compute the sum separately and provide it as a literal:

```
from pyspark.sql.functions import col, sum, lit

bar_sum = (
    dfs
    .where(col("foo") == "d")
    .groupBy()
    .agg(sum(col("bar")))
    .take(1)[0][0]
)

(
    dfs
    .orderBy("foo")
    .limit(2)
    .withColumn("bar", lit(bar_sum))
    .show()
)
```

Output:

```
+---+---+
|foo|bar|
+---+---+
|  a|  9|
|  b|  9|
+---+---+
```

### Example 2: Combining Two `head`s

In Polars you can combine two different `head` expressions on the same DataFrame, provided that they return the same number of values.

```
df.select(
    pl.col("foo").sort().head(2),
    pl.col("bar").sort(descending=True).head(2),
)
```

Output:

```
shape: (3, 2)
┌─────┬─────┐
│ foo ┆ bar │
│ --- ┆ --- │
│ str ┆ i64 │
╞═════╪═════╡
│ a   ┆ 5   │
├╌╌╌╌╌┼╌╌╌╌╌┤
│ b   ┆ 4   │
└─────┴─────┘
```

Again, the two `head` expressions here are completely independent, and the pairing of `a` to `5` and `b` to `4` results purely from the juxtaposition of the two columns output by the expressions.

To accomplish something similar in `Spark`, you would need to generate an artificial key that enables you to join the values in this way.

```
from pyspark.sql import Window
from pyspark.sql.functions import row_number

foo_dfs = (
    dfs
    .withColumn(
        "rownum",
        row_number().over(Window.orderBy("foo"))
    )
)

bar_dfs = (
    dfs
    .withColumn(
        "rownum",
        row_number().over(Window.orderBy(col("bar").desc()))
    )
)

(
    foo_dfs.alias("foo")
    .join(bar_dfs.alias("bar"), on="rownum")
    .select("foo.foo", "bar.bar")
    .limit(2)
    .show()
)
```

Output:

```
+---+---+
|foo|bar|
+---+---+
|  a|  5|
|  b|  4|
+---+---+
```

### Example 3: Composing expressions

Polars allows you compose expressions quite liberally. For example, if you want to find the rolling mean of a lagged variable, you can compose `shift` and `rolling_mean` and evaluate them in a single `over` expression:

```
df.with_columns(
    feature=pl.col('price').shift(7).rolling_mean(7).over('store', order_by='date')
)
```

In PySpark however this is not allowed. They allow composing expressions such as `F.mean(F.abs("price")).over(window)` because `F.abs` is an elementwise function, but not `F.mean(F.lag("price", 1)).over(window)` because `F.lag` is a window function. To produce the same result, both `F.lag` and `F.mean` need their own window.

```
from pyspark.sql import Window
from pyspark.sql import functions as F

window = Window().partitionBy("store").orderBy("date")
rolling_window = window.rowsBetween(-6, 0)
(
    df.withColumn("lagged_price", F.lag("price", 7).over(window)).withColumn(
        "feature",
        F.when(
            F.count("lagged_price").over(rolling_window) >= 7,
            F.mean("lagged_price").over(rolling_window),
        ),
    )
)
```

[Previous Coming from Pandas](https://docs.pola.rs/user-guide/migration/pandas/)[Next Ecosystem](https://docs.pola.rs/user-guide/ecosystem/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
