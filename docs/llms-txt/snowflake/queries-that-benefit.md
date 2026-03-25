# Source: https://docs.snowflake.com/en/user-guide/search-optimization/queries-that-benefit.md

# Identifying queries that can benefit from search optimization

Search optimization can improve the performance of many queries. This topic describes characteristics of the kinds of
queries that search optimization helps the most with, and conversely, the kinds of queries that do not benefit.

## General query characteristics

Search optimization works best to improve the performance of queries with the following characteristics:

* The query involves a column or columns other than the primary cluster key.
* The query typically runs for a few seconds or longer (before applying search optimization). In most cases, search optimization will
  not substantially improve the performance of a query that has a sub-second execution time.
* At least one of the columns accessed by the query filter operation has on the order of 100,000 distinct values or more.

  To determine the number of distinct values, you can use either of the following:

  * Use `APPROX_COUNT_DISTINCT` to get the approximate number of distinct values:

    ```sqlexample
    SELECT APPROX_COUNT_DISTINCT(column1) FROM table1;
    ```

  * Use `COUNT(DISTINCT <col_name>)` to get the actual number of distinct values:

    ```sqlexample
    SELECT COUNT(DISTINCT c1), COUNT(DISTINCT c2) FROM test_table;
    ```

  Because you need only an approximation of the number of distinct values, consider using `APPROX_COUNT_DISTINCT`, which
  is generally faster and cheaper than `COUNT(DISTINCT <col_name>)`.

## Supported data types

The search optimization service currently supports the following data types:

* [Data types for fixed-point numbers](../../sql-reference/data-types-numeric.md) (for example, INTEGER and NUMERIC)
* [String & binary data types](../../sql-reference/data-types-text.md) (for example, VARCHAR and BINARY)
* [Date & time data types](../../sql-reference/data-types-datetime.md) (for example, DATE, TIME, and TIMESTAMP)
* [Semi-structured data types](../../sql-reference/data-types-semistructured.md) (for example, VARIANT, OBJECT, and ARRAY)
* [Structured data types](../../sql-reference/data-types-structured.md) (for example, structured ARRAY, OBJECT, and MAP)
* [GEOGRAPHY data type](../../sql-reference/data-types-geospatial.md)

Queries that involve other values of other data types (for example, FLOAT, DECFLOAT, or GEOMETRY) don’t benefit.

## Supported table types

The search optimization service currently supports the following types of tables:

* Standard Snowflake tables
* [Interactive tables](../interactive.md)
* Iceberg tables
* [Dynamic tables](../dynamic-tables-about.md)
* [Transient tables](../tables-temp-transient.md)

The search optimization service currently *doesn’t* support the following types of tables:

* [External tables](../tables-external-intro.md)
* [Hybrid tables](../tables-hybrid.md)
* [Temporary tables](../tables-temp-transient.md)

## Supported predicate types

Search optimization can improve the performance of queries using these kinds of predicates:

* [Point lookup queries using equality and IN](point-lookup-queries.md).
* [Join queries](join-queries.md).
* [Queries using scalar subqueries](scalar-subqueries.md).
* [Queries using scalar functions](scalar-functions.md).
* [Character data (text) queries using the SEARCH and SEARCH_IP functions](text-queries.md).
* [Substring queries using wildcards and regular expressions](substring-queries.md).
* [Searches in semi-structured data](semi-structured-queries.md).
* [Searches in structured data](structured-queries.md).
* [Geospatial queries](geospatial-queries.md).
* [Queries using conjunctions (AND) and disjunctions (OR)](conjunctions-disjunctions.md).

## Support for collation

Search optimization can improve the performance of queries on columns defined with a [COLLATE clause](../../sql-reference/collation.md),
depending on the search method:

* When search optimization is [enabled](enabling.md) on a column using the
  `EQUALITY` search method, any collation specification is supported.
* When search optimization is enabled on a column using the `FULL_TEXT` or `SUBSTRING` search method,
  the `'utf8'` or `'bin'` collation specifications are supported.

For more information about search methods, see [ALTER TABLE … ADD SEARCH OPTIMIZATION](../../sql-reference/sql/alter-table.md).

Search optimization doesn’t support predicates that change the collation specification of a column using the
[COLLATE](../../sql-reference/functions/collate.md) function.

For example, create a table with columns that have collation specifications and insert a row:

```sqlexample
CREATE OR REPLACE TABLE search_optimization_collation_demo (
  en_ci_col VARCHAR COLLATE 'en-ci',
  utf_8_col VARCHAR COLLATE 'utf8');

INSERT INTO search_optimization_collation_demo VALUES (
  'test_collation_1',
  'test_collation_2');
```

Enable search optimization for equality predicates on both columns in the table:

```sqlexample
ALTER TABLE search_optimization_collation_demo
  ADD SEARCH OPTIMIZATION ON EQUALITY(en_ci_col, utf_8_col);
```

The following query can benefit from search optimization:

```sqlexample
SELECT *
  FROM search_optimization_collation_demo
  WHERE utf_8_col = 'test_collation_2';
```

The following query can’t benefit from search optimization because it changes the collation specification of the
`utf_8_col` column using the COLLATE function:

```sqlexample
SELECT *
  FROM search_optimization_collation_demo
  WHERE utf_8_col COLLATE 'de-ci' = 'test_collation_2';
```

The following query also can’t benefit from search optimization. Based on the
[collation rules of precedence](../../sql-reference/collation.md),
the query applies the `'de-ci'` collation specification to the `utf_8_col` column using the COLLATE
function.

```sqlexample
SELECT *
  FROM search_optimization_collation_demo
  WHERE utf_8_col = 'test_collation_2' COLLATE 'de-ci';
```

## Support for Apache Iceberg™ tables

Search optimization can improve the performance of queries on Apache Iceberg™ tables. For information
about configuring search optimization for Iceberg tables, see [ALTER ICEBERG TABLE](../../sql-reference/sql/alter-iceberg-table.md).

The following limitations apply to search optimization support for Iceberg tables:

* Search optimization can’t be added for columns with data types that Iceberg tables don’t support, which include
  [semi-structured](../../sql-reference/data-types-semistructured.md) and [geospatial](../../sql-reference/data-types-geospatial.md)
  data types. For more information, see [Data types for Apache Iceberg™ tables](../tables-iceberg-data-types.md).
* If Apache Parquet™ files are too large (for example, hundreds of megabytes compressed), then queries might not fully benefit from
  the search optimization service in some scenarios.

Other limitations that apply to search optimization for Snowflake tables also apply to Iceberg tables. For more information, see
Queries that do not benefit from search optimization.

## Potential improvements for views

The search optimization service can indirectly improve the performance of views (including secure views). If a base table for a
view has search optimization enabled, and the query uses a selective predicate for that table, the search optimization service
can improve performance when filtering rows. See Supported predicate types.

Not all tables in the view need to have search optimization enabled. Search optimization is performed on each table
independently.

## Queries that do not benefit from search optimization

Currently, the search optimization service doesn’t support floating point data types, GEOMETRY, or other data types not already discussed.
Snowflake might add support for more data types in the future.

Additionally, the search optimization service doesn’t support the following:

* Some table types.

  For more information, see Supported table types.
* Materialized views.
* Column concatenation.
* Analytical expressions.
* Casts on table columns (except for fixed-point numbers cast to strings).

  Although search optimization supports predicates with implicit and explicit casts on constant values, it doesn’t support
  predicates that cast values in the actual table column (except for casts from INTEGER and NUMBER to VARCHAR).

  For example, the following predicates are supported because they use implicit and explicit casts on constant values (not values
  in the table column):

  ```sqlexample
  -- Supported predicate
  -- (where the string '2020-01-01' is implicitly cast to a date)
  WHERE timestamp1 = '2020-01-01';

  -- Supported predicate
  -- (where the string '2020-01-01' is explicitly cast to a date)
  WHERE timestamp1 = '2020-01-01'::date;
  ```

  The following predicate is not supported because it uses a cast on values in the table column:

  ```sqlexample
  -- Unsupported predicate
  -- (where values in a VARCHAR column are cast to DATE)
  WHERE to_date(varchar_column) = '2020-01-01';
  ```

  The search optimization service considers the original column values, not the values after the cast. As a result,
  the search optimization service is not used for queries with these predicates.

As noted, the exception to this rule is casting NUMBER or INTEGER values to VARCHAR values in the table column. The
search optimization service does support this type of predicate:

> ```sqlexample
> -- Supported predicate
> -- (where values in a numeric column are cast to a string)
> WHERE cast(numeric_column as varchar) = '2'
> ```

Search optimization doesn’t improve performance of queries that use [Time Travel](../data-time-travel.md)
because search optimization works only on active data.
