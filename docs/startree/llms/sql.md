# Source: https://docs.startree.ai/corecapabilities/query_data/query_languages/sql.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# SQL

Apache Pinot provides a SQL interface for querying, which uses the **Calcite SQL** parser to parse queries and the **MYSQL\_ANSI** dialect. The multi-stage query engine in Pinot supports inner join, left-outer, semi-join, and nested queries out of the box.

Several different types of functions are supported, such as Aggeregation Functions, Transformation Functions, and query operators for querying JSON data.

For the complete list of supported functions and description of query syntax, see [Querying Pinot](https://docs.pinot.apache.org/users/user-guide-query/querying-pinot).

## Sample Queries

### Selection

```sql  theme={null}
//default to limit 10
SELECT * 
FROM myTable 

SELECT * 
FROM myTable 
LIMIT 100
```

```sql  theme={null}
SELECT "date", "timestamp"
FROM myTable 
```

### Aggregation

```sql  theme={null}
SELECT COUNT(*), MAX(foo), SUM(bar) 
FROM myTable
```

### Filtering

```sql  theme={null}
SELECT COUNT(*) 
FROM myTable
  WHERE foo = 'foo'
  AND bar BETWEEN 1 AND 20
  OR (baz < 42 AND quux IN ('hello', 'goodbye') AND quuux NOT IN (42, 69))
```

### Ordering on Selection

```sql  theme={null}
SELECT foo, bar 
FROM myTable
  WHERE baz > 20
  ORDER BY bar DESC
  LIMIT 100
```

StarTree Cloud supports a comprehensive set of functions for data manipulation and analysis. For a complete reference, see the [Apache Pinot Function Documentation](https://docs.pinot.apache.org/functions/supported-aggregations).

Built with [Mintlify](https://mintlify.com).
