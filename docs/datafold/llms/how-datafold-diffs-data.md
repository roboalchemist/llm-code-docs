# Source: https://docs.datafold.com/data-diff/how-datafold-diffs-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How Datafold Diffs Data

> Data diffs allow you to perform value-level comparisons between any two datasets within the same database, across different databases, or even between files.

The basic inputs required to run a diff are the data connections, names/paths of the datasets to be compared, and the primary key (one or more columns that uniquely identify rows in the datasets).

## What types of data can data diffs compare?

Diffs can compare data in tables, views, SQL queries (in relational databases and data lakes), and even files (e.g. CSV, Excel, Parquet, etc.).

Datafold facilitates data diffing by supporting a wide range of basic data types across major database systems like Snowflake, Databricks, BigQuery, Redshift, PostgreSQL, and many more.

## Creating data diffs

Diffs can be created in several ways:

* Interactively through the Datafold app
* Programmatically via our [REST API](/api-reference/data-diffs/create-a-data-diff)
* As part of a Continuous Integration (CI) workflow for [Deployment Testing](/deployment-testing/how-it-works)

## How in-database diffing works

When diffing data within the same physical database or data lake namespace, diffs compare data by executing various SQL queries in the target database. It uses several `JOIN`-type queries and various aggregate queries to provide detailed insights into differences at the row, value, and column levels, and to calculate differences in metrics and distributions.

## How cross-database diffing works

Datasets from both data connections are co-located in a centralized database to execute comparisons and identify specific rows, columns, and values with differences. To perform diffs at massive scale and increased speed, users can apply sampling, filtering, and column selection.
