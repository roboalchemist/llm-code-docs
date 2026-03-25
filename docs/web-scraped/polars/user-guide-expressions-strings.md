# Source: https://docs.pola.rs/user-guide/expressions/strings/

Title: Strings - Polars user guide

URL Source: https://docs.pola.rs/user-guide/expressions/strings/

Published Time: Thu, 12 Mar 2026 14:44:20 GMT

Markdown Content:
Strings - Polars user guide
===============
- [x] - [x] 

[Skip to content](https://docs.pola.rs/user-guide/expressions/strings/#strings)

[![Image 1: logo](https://docs.pola.rs/_build/assets/logo.png)](https://docs.pola.rs/ "Polars user guide")

 Polars user guide 

 Strings 

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
            *   - [x]  Strings  [Strings](https://docs.pola.rs/user-guide/expressions/strings/) Table of contents  
                *   [The string namespace](https://docs.pola.rs/user-guide/expressions/strings/#the-string-namespace)
                *   [Parsing strings](https://docs.pola.rs/user-guide/expressions/strings/#parsing-strings)
                    *   [Check for the existence of a pattern](https://docs.pola.rs/user-guide/expressions/strings/#check-for-the-existence-of-a-pattern)
                    *   [Regex specification](https://docs.pola.rs/user-guide/expressions/strings/#regex-specification)
                    *   [Extract a pattern](https://docs.pola.rs/user-guide/expressions/strings/#extract-a-pattern)
                    *   [Replace a pattern](https://docs.pola.rs/user-guide/expressions/strings/#replace-a-pattern)

                *   [Modifying strings](https://docs.pola.rs/user-guide/expressions/strings/#modifying-strings)
                    *   [Case conversion](https://docs.pola.rs/user-guide/expressions/strings/#case-conversion)
                    *   [Stripping characters from the ends](https://docs.pola.rs/user-guide/expressions/strings/#stripping-characters-from-the-ends)
                    *   [Slicing](https://docs.pola.rs/user-guide/expressions/strings/#slicing)

                *   [API documentation](https://docs.pola.rs/user-guide/expressions/strings/#api-documentation)

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
*   [The string namespace](https://docs.pola.rs/user-guide/expressions/strings/#the-string-namespace)
*   [Parsing strings](https://docs.pola.rs/user-guide/expressions/strings/#parsing-strings)
    *   [Check for the existence of a pattern](https://docs.pola.rs/user-guide/expressions/strings/#check-for-the-existence-of-a-pattern)
    *   [Regex specification](https://docs.pola.rs/user-guide/expressions/strings/#regex-specification)
    *   [Extract a pattern](https://docs.pola.rs/user-guide/expressions/strings/#extract-a-pattern)
    *   [Replace a pattern](https://docs.pola.rs/user-guide/expressions/strings/#replace-a-pattern)

*   [Modifying strings](https://docs.pola.rs/user-guide/expressions/strings/#modifying-strings)
    *   [Case conversion](https://docs.pola.rs/user-guide/expressions/strings/#case-conversion)
    *   [Stripping characters from the ends](https://docs.pola.rs/user-guide/expressions/strings/#stripping-characters-from-the-ends)
    *   [Slicing](https://docs.pola.rs/user-guide/expressions/strings/#slicing)

*   [API documentation](https://docs.pola.rs/user-guide/expressions/strings/#api-documentation)

Strings
=======

The following section discusses operations performed on string data, which is a frequently used data type when working with dataframes. String processing functions are available in the namespace `str`.

Working with strings in other dataframe libraries can be highly inefficient due to the fact that strings have unpredictable lengths. Polars mitigates these inefficiencies by [following the Arrow Columnar Format specification](https://docs.pola.rs/user-guide/concepts/data-types-and-structures/#data-types-internals), so you can write performant data queries on string data too.

The string namespace
--------------------

When working with string data you will likely need to access the namespace `str`, which aggregates 40+ functions that let you work with strings. As an example of how to access functions from within that namespace, the snippet below shows how to compute the length of the strings in a column in terms of the number of bytes and the number of characters:

 Python  Rust 

[`str.len_bytes`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.len_bytes.html) ·[`str.len_chars`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.len_chars.html)

```
import polars as pl

df = pl.DataFrame(
    {
        "language": ["English", "Dutch", "Portuguese", "Finish"],
        "fruit": ["pear", "peer", "pêra", "päärynä"],
    }
)

result = df.with_columns(
    pl.col("fruit").str.len_bytes().alias("byte_count"),
    pl.col("fruit").str.len_chars().alias("letter_count"),
)
print(result)
```

[`str.len_bytes`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.len_bytes) ·[`str.len_chars`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.len_chars)

```
use polars::prelude::*;

let df = df! (
    "language" => ["English", "Dutch", "Portuguese", "Finish"],
    "fruit" => ["pear", "peer", "pêra", "päärynä"],
)?;

let result = df
    .clone()
    .lazy()
    .with_columns([
        col("fruit").str().len_bytes().alias("byte_count"),
        col("fruit").str().len_chars().alias("letter_count"),
    ])
    .collect()?;

println!("{result}");
```

```
shape: (4, 4)
┌────────────┬─────────┬────────────┬──────────────┐
│ language   ┆ fruit   ┆ byte_count ┆ letter_count │
│ ---        ┆ ---     ┆ ---        ┆ ---          │
│ str        ┆ str     ┆ u32        ┆ u32          │
╞════════════╪═════════╪════════════╪══════════════╡
│ English    ┆ pear    ┆ 4          ┆ 4            │
│ Dutch      ┆ peer    ┆ 4          ┆ 4            │
│ Portuguese ┆ pêra    ┆ 5          ┆ 4            │
│ Finish     ┆ päärynä ┆ 10         ┆ 7            │
└────────────┴─────────┴────────────┴──────────────┘
```

Note

If you are working exclusively with ASCII text, then the results of the two computations will be the same and using `len_bytes` is recommended since it is faster.

Parsing strings
---------------

Polars offers multiple methods for checking and parsing elements of a string column, namely checking for the existence of given substrings or patterns, and counting, extracting, or replacing, them. We will demonstrate some of these operations in the upcoming examples.

### Check for the existence of a pattern

We can use the function `contains` to check for the presence of a pattern within a string. By default, the argument to the function `contains` is interpreted as a regular expression. If you want to specify a literal substring, set the parameter `literal` to `True`.

For the special cases where you want to check if the strings start or end with a fixed substring, you can use the functions `starts_with` or `ends_with`, respectively.

 Python  Rust 

[`str.contains`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.contains.html) ·[`str.starts_with`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.starts_with.html) ·[`str.ends_with`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.ends_with.html)

```
result = df.select(
    pl.col("fruit"),
    pl.col("fruit").str.starts_with("p").alias("starts_with_p"),
    pl.col("fruit").str.contains("p..r").alias("p..r"),
    pl.col("fruit").str.contains("e+").alias("e+"),
    pl.col("fruit").str.ends_with("r").alias("ends_with_r"),
)
print(result)
```

[`str.contains`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.contains) ·[`str.starts_with`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.starts_with) ·[`str.ends_with`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.ends_with) ·[Available on feature regex](https://docs.pola.rs/user-guide/installation/#feature-flags "To use this functionality enable the feature flag regex")

```
let result = df
    .lazy()
    .select([
        col("fruit"),
        col("fruit")
            .str()
            .starts_with(lit("p"))
            .alias("starts_with_p"),
        col("fruit").str().contains(lit("p..r"), true).alias("p..r"),
        col("fruit").str().contains(lit("e+"), true).alias("e+"),
        col("fruit").str().ends_with(lit("r")).alias("ends_with_r"),
    ])
    .collect()?;

println!("{result}");
```

```
shape: (4, 5)
┌─────────┬───────────────┬───────┬───────┬─────────────┐
│ fruit   ┆ starts_with_p ┆ p..r  ┆ e+    ┆ ends_with_r │
│ ---     ┆ ---           ┆ ---   ┆ ---   ┆ ---         │
│ str     ┆ bool          ┆ bool  ┆ bool  ┆ bool        │
╞═════════╪═══════════════╪═══════╪═══════╪═════════════╡
│ pear    ┆ true          ┆ true  ┆ true  ┆ true        │
│ peer    ┆ true          ┆ true  ┆ true  ┆ true        │
│ pêra    ┆ true          ┆ false ┆ false ┆ false       │
│ päärynä ┆ true          ┆ true  ┆ false ┆ false       │
└─────────┴───────────────┴───────┴───────┴─────────────┘
```

### Regex specification

Polars relies on the Rust crate `regex` to work with regular expressions, so you may need to [refer to the syntax documentation](https://docs.rs/regex/latest/regex/#syntax) to see what features and flags are supported. In particular, note that the flavor of regex supported by Polars is different from Python's module `re`.

### Extract a pattern

The function `extract` allows us to extract patterns from the string values in a column. The function `extract` accepts a regex pattern with one or more capture groups and extracts the capture group specified as the second argument.

 Python  Rust 

[`str.extract`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.extract.html)

```
df = pl.DataFrame(
    {
        "urls": [
            "http://vote.com/ballon_dor?candidate=messi&ref=polars",
            "http://vote.com/ballon_dor?candidat=jorginho&ref=polars",
            "http://vote.com/ballon_dor?candidate=ronaldo&ref=polars",
        ]
    }
)
result = df.select(
    pl.col("urls").str.extract(r"candidate=(\w+)", group_index=1),
)
print(result)
```

[`str.extract`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.extract)

```
let df = df! (
    "urls" => [
        "http://vote.com/ballon_dor?candidate=messi&ref=polars",
        "http://vote.com/ballon_dor?candidat=jorginho&ref=polars",
        "http://vote.com/ballon_dor?candidate=ronaldo&ref=polars",
    ]
)?;

let result = df
    .lazy()
    .select([col("urls").str().extract(lit(r"candidate=(\w+)"), 1)])
    .collect()?;

println!("{result}");
```

```
shape: (3, 1)
┌─────────┐
│ urls    │
│ ---     │
│ str     │
╞═════════╡
│ messi   │
│ null    │
│ ronaldo │
└─────────┘
```

To extract all occurrences of a pattern within a string, we can use the function `extract_all`. In the example below, we extract all numbers from a string using the regex pattern `(\d+)`, which matches one or more digits. The resulting output of the function `extract_all` is a list containing all instances of the matched pattern within the string.

 Python  Rust 

[`str.extract_all`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.extract_all.html)

```
df = pl.DataFrame({"text": ["123 bla 45 asd", "xyz 678 910t"]})
result = df.select(
    pl.col("text").str.extract_all(r"(\d+)").alias("extracted_nrs"),
)
print(result)
```

[`str.extract_all`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.extract_all)

```
let df = df! (
    "text" => ["123 bla 45 asd", "xyz 678 910t"]
)?;

let result = df
    .lazy()
    .select([col("text")
        .str()
        .extract_all(lit(r"(\d+)"))
        .alias("extracted_nrs")])
    .collect()?;

println!("{result}");
```

```
shape: (2, 1)
┌────────────────┐
│ extracted_nrs  │
│ ---            │
│ list[str]      │
╞════════════════╡
│ ["123", "45"]  │
│ ["678", "910"] │
└────────────────┘
```

### Replace a pattern

Akin to the functions `extract` and `extract_all`, Polars provides the functions `replace` and `replace_all`. These accept a regex pattern or a literal substring (if the parameter `literal` is set to `True`) and perform the replacements specified. The function `replace` will make at most one replacement whereas the function `replace_all` will make all the non-overlapping replacements it finds.

 Python  Rust 

[`str.replace`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.replace.html) ·[`str.replace_all`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.replace_all.html)

```
df = pl.DataFrame({"text": ["123abc", "abc456"]})
result = df.with_columns(
    pl.col("text").str.replace(r"\d", "-"),
    pl.col("text").str.replace_all(r"\d", "-").alias("text_replace_all"),
)
print(result)
```

[`str.replace`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.replace) ·[`str.replace_all`](https://docs.pola.rs/api/rust/dev/polars_lazy/dsl/string/struct.StringNameSpace.html#method.replace_all) ·[Available on feature regex](https://docs.pola.rs/user-guide/installation/#feature-flags "To use this functionality enable the feature flag regex")

```
let df = df! (
    "text" => ["123abc", "abc456"]
)?;

let result = df
    .lazy()
    .with_columns([
        col("text").str().replace(lit(r"\d"), lit("-"), false),
        col("text")
            .str()
            .replace_all(lit(r"\d"), lit("-"), false)
            .alias("text_replace_all"),
    ])
    .collect()?;

println!("{result}");
```

```
shape: (2, 2)
┌────────┬──────────────────┐
│ text   ┆ text_replace_all │
│ ---    ┆ ---              │
│ str    ┆ str              │
╞════════╪══════════════════╡
│ -23abc ┆ ---abc           │
│ abc-56 ┆ abc---           │
└────────┴──────────────────┘
```

Modifying strings
-----------------

### Case conversion

Converting the casing of a string is a common operation and Polars supports it out of the box with the functions `to_lowercase`, `to_titlecase`, and `to_uppercase`:

 Python  Rust 

[`str.to_lowercase`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_lowercase.html) ·[`str.to_titlecase`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_titlecase.html) ·[`str.to_uppercase`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.to_uppercase.html)

```
addresses = pl.DataFrame(
    {
        "addresses": [
            "128 PERF st",
            "Rust blVD, 158",
            "PoLaRs Av, 12",
            "1042 Query sq",
        ]
    }
)

addresses = addresses.select(
    pl.col("addresses").alias("originals"),
    pl.col("addresses").str.to_titlecase(),
    pl.col("addresses").str.to_lowercase().alias("lower"),
    pl.col("addresses").str.to_uppercase().alias("upper"),
)
print(addresses)
```

[`str.to_lowercase`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.to_lowercase) ·[`str.to_titlecase`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.to_titlecase) ·[`str.to_uppercase`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.to_uppercase) ·[Available on feature nightly](https://docs.pola.rs/user-guide/installation/#feature-flags "To use this functionality enable the feature flag nightly")

```
let addresses = df! (
    "addresses" => [
        "128 PERF st",
        "Rust blVD, 158",
        "PoLaRs Av, 12",
        "1042 Query sq",
    ]
)?;

let addresses = addresses
    .lazy()
    .select([
        col("addresses").alias("originals"),
        col("addresses").str().to_titlecase(),
        col("addresses").str().to_lowercase().alias("lower"),
        col("addresses").str().to_uppercase().alias("upper"),
    ])
    .collect()?;

println!("{addresses}");
```

```
shape: (4, 4)
┌────────────────┬────────────────┬────────────────┬────────────────┐
│ originals      ┆ addresses      ┆ lower          ┆ upper          │
│ ---            ┆ ---            ┆ ---            ┆ ---            │
│ str            ┆ str            ┆ str            ┆ str            │
╞════════════════╪════════════════╪════════════════╪════════════════╡
│ 128 PERF st    ┆ 128 Perf St    ┆ 128 perf st    ┆ 128 PERF ST    │
│ Rust blVD, 158 ┆ Rust Blvd, 158 ┆ rust blvd, 158 ┆ RUST BLVD, 158 │
│ PoLaRs Av, 12  ┆ Polars Av, 12  ┆ polars av, 12  ┆ POLARS AV, 12  │
│ 1042 Query sq  ┆ 1042 Query Sq  ┆ 1042 query sq  ┆ 1042 QUERY SQ  │
└────────────────┴────────────────┴────────────────┴────────────────┘
```

### Stripping characters from the ends

Polars provides five functions in the namespace `str` that let you strip characters from the ends of the string:

| Function | Behaviour |
| --- | --- |
| `strip_chars` | Removes leading and trailing occurrences of the characters specified. |
| `strip_chars_end` | Removes trailing occurrences of the characters specified. |
| `strip_chars_start` | Removes leading occurrences of the characters specified. |
| `strip_prefix` | Removes an exact substring prefix if present. |
| `strip_suffix` | Removes an exact substring suffix if present. |

Similarity to Python string methods
`strip_chars` is similar to Python's string method `strip` and `strip_prefix`/`strip_suffix` are similar to Python's string methods `removeprefix` and `removesuffix`, respectively.

It is important to understand that the first three functions interpret their string argument as a set of characters whereas the functions `strip_prefix` and `strip_suffix` do interpret their string argument as a literal string.

 Python  Rust 

[`str.strip_chars`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.strip_chars.html) ·[`str.strip_chars_end`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.strip_chars_end.html) ·[`str.strip_chars_start`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.strip_chars_start.html) ·[`str.strip_prefix`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.strip_prefix.html) ·[`str.strip_suffix`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.strip_suffix.html)

```
addr = pl.col("addresses")
chars = ", 0123456789"
result = addresses.select(
    addr.str.strip_chars(chars).alias("strip"),
    addr.str.strip_chars_end(chars).alias("end"),
    addr.str.strip_chars_start(chars).alias("start"),
    addr.str.strip_prefix("128 ").alias("prefix"),
    addr.str.strip_suffix(", 158").alias("suffix"),
)
print(result)
```

[`str.strip_chars`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.strip_chars) ·[`str.strip_chars_end`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.strip_chars_end) ·[`str.strip_chars_start`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.strip_chars_start) ·[`str.strip_prefix`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.strip_prefix) ·[`str.strip_suffix`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.strip_suffix)

```
let addr = col("addresses");
let chars = lit(", 0123456789");
let result = addresses
    .lazy()
    .select([
        addr.clone().str().strip_chars(chars.clone()).alias("strip"),
        addr.clone()
            .str()
            .strip_chars_end(chars.clone())
            .alias("end"),
        addr.clone().str().strip_chars_start(chars).alias("start"),
        addr.clone().str().strip_prefix(lit("128 ")).alias("prefix"),
        addr.str().strip_suffix(lit(", 158")).alias("suffix"),
    ])
    .collect()?;

println!("{result}");
```

```
shape: (4, 5)
┌───────────┬───────────────┬────────────────┬────────────────┬───────────────┐
│ strip     ┆ end           ┆ start          ┆ prefix         ┆ suffix        │
│ ---       ┆ ---           ┆ ---            ┆ ---            ┆ ---           │
│ str       ┆ str           ┆ str            ┆ str            ┆ str           │
╞═══════════╪═══════════════╪════════════════╪════════════════╪═══════════════╡
│ Perf St   ┆ 128 Perf St   ┆ Perf St        ┆ Perf St        ┆ 128 Perf St   │
│ Rust Blvd ┆ Rust Blvd     ┆ Rust Blvd, 158 ┆ Rust Blvd, 158 ┆ Rust Blvd     │
│ Polars Av ┆ Polars Av     ┆ Polars Av, 12  ┆ Polars Av, 12  ┆ Polars Av, 12 │
│ Query Sq  ┆ 1042 Query Sq ┆ Query Sq       ┆ 1042 Query Sq  ┆ 1042 Query Sq │
└───────────┴───────────────┴────────────────┴────────────────┴───────────────┘
```

If no argument is provided, the three functions `strip_chars`, `strip_chars_end`, and `strip_chars_start`, remove whitespace by default.

### Slicing

Besides [extracting substrings as specified by patterns](https://docs.pola.rs/user-guide/expressions/strings/#extract-a-pattern), you can also slice strings at specified offsets to produce substrings. The general-purpose function for slicing is `slice` and it takes the starting offset and the optional _length_ of the slice. If the length of the slice is not specified or if it's past the end of the string, Polars slices the string all the way to the end.

The functions `head` and `tail` are specialised versions used for slicing the beginning and end of a string, respectively.

 Python  Rust 

[`str.slice`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.slice.html) ·[`str.head`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.head.html) ·[`str.tail`](https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.str.tail.html)

```
df = pl.DataFrame(
    {
        "fruits": ["pear", "mango", "dragonfruit", "passionfruit"],
        "n": [1, -1, 4, -4],
    }
)

result = df.with_columns(
    pl.col("fruits").str.slice(pl.col("n")).alias("slice"),
    pl.col("fruits").str.head(pl.col("n")).alias("head"),
    pl.col("fruits").str.tail(pl.col("n")).alias("tail"),
)
print(result)
```

[`str.str_slice`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.str_slice) ·[`str.str_head`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.str_head) ·[`str.str_tail`](https://docs.rs/polars/latest/polars/prelude/trait.StringNameSpaceImpl.html#method.str_tail)

```
let df = df! (
    "fruits" => ["pear", "mango", "dragonfruit", "passionfruit"],
    "n" => [1, -1, 4, -4],
)?;

let result = df
    .lazy()
    .with_columns([
        col("fruits")
            .str()
            .slice(col("n"), lit(NULL))
            .alias("slice"),
        col("fruits").str().head(col("n")).alias("head"),
        col("fruits").str().tail(col("n")).alias("tail"),
    ])
    .collect()?;

println!("{result}");
```

```
shape: (4, 5)
┌──────────────┬─────┬─────────┬──────────┬──────────┐
│ fruits       ┆ n   ┆ slice   ┆ head     ┆ tail     │
│ ---          ┆ --- ┆ ---     ┆ ---      ┆ ---      │
│ str          ┆ i64 ┆ str     ┆ str      ┆ str      │
╞══════════════╪═════╪═════════╪══════════╪══════════╡
│ pear         ┆ 1   ┆ ear     ┆ p        ┆ r        │
│ mango        ┆ -1  ┆ o       ┆ mang     ┆ ango     │
│ dragonfruit  ┆ 4   ┆ onfruit ┆ drag     ┆ ruit     │
│ passionfruit ┆ -4  ┆ ruit    ┆ passionf ┆ ionfruit │
└──────────────┴─────┴─────────┴──────────┴──────────┘
```

API documentation
-----------------

In addition to the examples covered above, Polars offers various other string manipulation functions. To explore these additional methods, you can go to the API documentation of your chosen programming language for Polars.

[Previous Casting](https://docs.pola.rs/user-guide/expressions/casting/)[Next Lists and arrays](https://docs.pola.rs/user-guide/expressions/lists-and-arrays/)

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
