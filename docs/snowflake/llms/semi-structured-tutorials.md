# Source: https://docs.snowflake.com/en/user-guide/semi-structured-tutorials.md

# Tutorials: Work with semi-structured data

The following tutorials provide examples and step-by-step instructions you can follow as you learn to
work with semi-structured data in Snowflake:

> **Note:**
>
> These tutorials show you how to load data into a table by using the
> [COPY INTO <table>](../sql-reference/sql/copy-into-table.md) command. For information about other options
> for loading data, see [Overview of data loading](data-load-overview.md).

[Learn the basics of using JSON with Snowflake](tutorials/json-basics-tutorial.md)
:   Describes the basics of using [JSON](semistructured-data-formats.md) with Snowflake.

[Load JSON data into a relational table](tutorials/script-data-load-transform-json.md)
:   Uses a [COPY INTO <table>](../sql-reference/sql/copy-into-table.md) command with a SELECT statement to load individual
    elements in a staged JSON file into a table.

[Load and unload Parquet data](tutorials/script-data-load-transform-parquet.md)
:   Describes how you can upload [Parquet](semistructured-data-formats.md) data by transforming elements of
    a staged Parquet file directly into table columns using the [COPY INTO <table>](../sql-reference/sql/copy-into-table.md) command. The
    tutorial also describes how you can use the [COPY INTO <location>](../sql-reference/sql/copy-into-location.md) command to unload table data
    into a Parquet file.
