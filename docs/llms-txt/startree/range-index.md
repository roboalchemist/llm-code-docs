# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/range-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Range Index

> Use the Range index to optimize range-based queries. The index enhances performance for inequality filters and BETWEEN operations on high-cardinality numeric or timestamp columns by mapping value ranges to corresponding rows.

## Overview and Purpose

A range index is a specialized data structure that accelerates queries involving range-based filtering operations. While traditional inverted indexes excel at equality-based filters (column = value), range indexes are optimized for comparison operations like greater than, less than, or between.

Range indexes transform range-based filtering from full table scans to targeted lookups, significantly improving query performance when filtering data across numeric ranges or time intervals.

Range indexes are particularly valuable for:

* Queries with inequality filters (`>`, `<`, `>=`, `<=`)
* Between operations (`column BETWEEN x AND y`)
* Numeric or timestamp columns with high cardinality
* Analytical workloads that frequently filter metric values by ranges

<Info>
  Range indexes are especially beneficial for high-cardinality columns (columns with many unique values) where traditional inverted indexes would be inefficient due to their large size.
</Info>

## How the Index Works

### Core Concepts

Traditional inverted indexes create mappings from individual values to the rows containing them. This approach works well for equality checks but becomes inefficient for range operations, especially with high-cardinality columns.

A range index in StarTree Cloud complements inverted indexes by utilizing:

1. **Range-Based Mapping**: Instead of mapping individual values to rows, a range index maps ranges of values to rows that contain values within those ranges.
2. **Efficient Range Evaluation**: When a query includes a range predicate (e.g., `column > 100`), the index can quickly identify the exact set of rows that meet this condition without scanning the entire dataset.

### Example Illustration

For a column storing sales amounts with values ranging from \$0 to \$1,000:

A traditional approach would need to scan every row and check each value against the filter condition.

With a range index, the system:

1. Divides the value range into segments (e.g., \$0-\$100, \$100-\$200, etc.)
2. Maps each segment to the rows containing values in that range
3. For a query like `sales_amount > 500`, quickly identifies only the relevant segments and returns the corresponding rows

This dramatically reduces the number of rows that need to be examined, resulting in faster query performance.

## Configuration

### Enabling Range Index

To enable a range index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "sales_amount",
      "indexes": {
        "range": {}
      }
    }
  ]
}
```

### Alternative Configuration (Legacy Method)

You can also use the older configuration format, though it's not recommended for new deployments:

```json  theme={null}
{
  "tableIndexConfig": {
    "rangeIndexColumns": [
      "sales_amount"
    ]
  }
}
```

### Important Configuration Considerations

1. **Column Requirements**: Range indexes can be created on:
   * Dictionary-encoded columns of any data type
   * Raw-encoded columns of numeric types (INT, LONG, FLOAT, DOUBLE)
   * Dictionary-encoded time columns using STRING type (if the datetime format maintains lexicographical order)
2. **Cardinality Recommendation**: Range indexes are best suited for columns with high cardinality (many unique values), where inverted indexes would be inefficient.
3. **Storage and Memory**: Range indexes are more compact than inverted indexes for high-cardinality columns, resulting in better storage efficiency and memory usage.
4. **Query Pattern**: Use range indexes on columns that are frequently filtered with range predicates (`>`, `<`, `>=`, `<=`, `BETWEEN`).

Built with [Mintlify](https://mintlify.com).
