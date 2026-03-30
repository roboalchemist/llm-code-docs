# Source: https://docs.snowflake.com/en/user-guide/search-optimization-service.md

# Search optimization service

The search optimization service can significantly improve the performance of certain types of lookup and analytical
queries. An extensive set of filtering predicates are supported (see [Identifying queries that can benefit from search optimization](search-optimization/queries-that-benefit.md)).

> **Note:**
>
> To start with a tutorial that compares execution time with and without search optimization, see
> [Getting Started with Search Optimization](https://quickstarts.snowflake.com/guide/getting_started_with_search_optimization/index.html).

The search optimization service aims to significantly improve the performance of certain types of queries on tables, including:

* Selective point lookup queries on tables. A point lookup query returns only one or a small number of distinct rows. Use case
  examples include:

  * Business users who need fast response times for critical dashboards with highly selective filters.
  * Data scientists who are exploring large data volumes and looking for specific subsets of data.
  * Data applications retrieving a small set of results based on an extensive set of filtering predicates.

  For more information, see [Speeding up point lookup queries with search optimization](search-optimization/point-lookup-queries.md).
* Character data (text) and IP address searches executed with the [SEARCH](../sql-reference/functions/search.md) and
  [SEARCH_IP](../sql-reference/functions/search_ip.md) functions. For more information, see [Speeding up text queries with search optimization](search-optimization/text-queries.md).
* Substring and regular expression searches (for example, [LIKE](../sql-reference/functions/like.md), [ILIKE](../sql-reference/functions/ilike.md),
  [RLIKE](../sql-reference/functions/rlike.md), and so on). For more information, see [Speeding up substring and regular expression queries with search optimization](search-optimization/substring-queries.md).
* Queries on elements in [VARIANT, OBJECT, and ARRAY](../sql-reference/data-types-semistructured.md) (semi-structured)
  columns that use the following types of predicates:

  * Equality predicates.
  * IN predicates.
  * Predicates that use [ARRAY_CONTAINS](../sql-reference/functions/array_contains.md).
  * Predicates that use [ARRAYS_OVERLAP](../sql-reference/functions/arrays_overlap.md).
  * Predicates that use full-text search with [SEARCH](../sql-reference/functions/search.md).
  * Substring and regular expression predicates.
  * Predicates that check for NULL values.

  For more information, see [Speeding up queries of semi-structured data with search optimization](search-optimization/semi-structured-queries.md).
* Queries on elements in [structured ARRAY, OBJECT, and MAP](../sql-reference/data-types-structured.md) (structured)
  columns that use the following types of predicates:

  * Equality predicates.
  * IN predicates.
  * Substring predicates (on STRING fields).

  For more information, see [Speeding up queries of structured data with search optimization](search-optimization/structured-queries.md).
* Queries that use selected geospatial functions with [GEOGRAPHY](../sql-reference/data-types-geospatial.md) values.
  For more information, see [Speeding up geospatial queries with search optimization](search-optimization/geospatial-queries.md).

Once you identify the queries that can benefit from the search optimization service, you can
[enable search optimization](search-optimization/enabling.md) for the columns and tables used in those queries.

The search optimization service is generally transparent to users. Queries work the same as they do without search
optimization; some are just faster. However, search optimization does have effects on certain other table operations. For
more information, see [Working with search-optimized tables](search-optimization/working-with-tables.md).

## How the search optimization service works

To improve performance of search queries, the search optimization service creates and maintains a persistent data
structure called a *search access path*. The search access path keeps track of which values of the table’s columns might
be found in each of its [micro-partitions](tables-clustering-micropartitions.md), allowing some micro-partitions to be
skipped when scanning the table.

A maintenance service is responsible for creating and maintaining the search access path:

* When you enable search optimization, the maintenance service creates and populates the search access path with the
  data needed to perform the lookups.

  Building the search access path can take significant time, depending on the size of the table. The maintenance service
  works in the background and does not block any operations on the table. Queries are not accelerated until the search
  access path has been fully built.
* When data in the table is updated (for example, by loading new data sets or through DML operations), the maintenance service
  automatically updates the search access path to reflect the changes to the data.

  If queries are run while the search access path is still being updated, queries might run more slowly, but will still
  return correct results.

The progress of each table’s maintenance service appears in the `search_optimization_progress` column in the
output of [SHOW TABLES](../sql-reference/sql/show-tables.md). Before you measure the performance improvement of search
optimization on a newly-optimized table, make sure this column shows that the table has been fully optimized.

Search access path maintenance is transparent. You don’t need to create a virtual warehouse for running the
maintenance service. However, there is a cost for the storage and compute resources of maintenance. For more details
on costs, see [Search optimization cost estimation and management](search-optimization/cost-estimation.md).

## Other options for optimizing query performance

The search optimization service is one of several ways to optimize query performance. The following list shows
other techniques:

* Query acceleration
* Creating one or more materialized views (clustered or unclustered)
* Clustering a table

For more information, see [Optimizing query performance](performance-query-options.md).

## Examples

Start by creating a table with data:

```sqlexample
CREATE OR REPLACE TABLE test_table (id INT, c1 INT, c2 STRING, c3 DATE) AS
  SELECT * FROM VALUES
    (1, 3, '4',  '1985-05-11'),
    (2, 4, '3',  '1996-12-20'),
    (3, 2, '1',  '1974-02-03'),
    (4, 1, '2',  '2004-03-09'),
    (5, NULL, NULL, NULL);
```

Add the SEARCH OPTIMIZATION property to the table using [ALTER TABLE](../sql-reference/sql/alter-table.md):

```sqlexample
ALTER TABLE test_table ADD SEARCH OPTIMIZATION;
```

The following queries can use the search optimization service:

```sqlexample
SELECT * FROM test_table WHERE id = 2;
```

```sqlexample
SELECT * FROM test_table WHERE c2 = '1';
```

```sqlexample
SELECT * FROM test_table WHERE c3 = '1985-05-11';
```

```sqlexample
SELECT * FROM test_table WHERE c1 IS NULL;
```

```sqlexample
SELECT * FROM test_table WHERE c1 = 4 AND c3 = '1996-12-20';
```

The following query can use the search optimization service because the implicit cast is on the constant, not the column:

```sqlexample
SELECT * FROM test_table WHERE c2 = 2;
```

The following can’t use the search optimization service because the cast is on the table’s column:

```sqlexample
SELECT * FROM test_table WHERE CAST(c2 AS NUMBER) = 2;
```

An [IN](../sql-reference/functions/in.md) clause is supported by the search optimization service:

```sqlexample
SELECT id, c1, c2, c3
  FROM test_table
  WHERE id IN (2, 3)
  ORDER BY id;
```

If predicates are individually supported by the search optimization service, then they can be joined by the conjunction
`AND` and still be supported by the search optimization service:

```sqlexample
SELECT id, c1, c2, c3
  FROM test_table
  WHERE c1 = 1
    AND c3 = TO_DATE('2004-03-09')
  ORDER BY id;
```

DELETE and UPDATE (and MERGE) can also use the search optimization service:

```sqlexample
DELETE FROM test_table WHERE id = 3;
```

```sqlexample
UPDATE test_table SET c1 = 99 WHERE id = 4;
```
