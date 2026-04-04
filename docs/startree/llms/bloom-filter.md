# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/bloom-filter.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Bloom Filter Index

> The Bloom Filter index enables fast filtering of high-cardinality columns by reducing unnecessary data scans.

## Overview and Purpose

A Bloom filter index is a space-efficient probabilistic data structure that enables fast segment pruning for equality-based queries. When applied to a column, it allows the system to quickly determine if a segment does not contain any records matching an equality (=) or IN predicate, thereby skipping unnecessary segment processing.

In StarTree Cloud (powered by Apache Pinot), Bloom filter indexes are particularly valuable for:

* Accelerating point queries that filter on high-cardinality columns
* Improving performance of queries with equality conditions
* Reducing processing overhead for IN clause queries (with up to 10 values)
* Optimizing segment pruning in distributed query execution
* Any query pattern where quickly eliminating irrelevant segments is beneficial

<Info>
  Bloom filters are designed to provide a definitive "no" but only a probable "yes" when checking for value existence. They never produce false negatives (missing values that exist) but may produce false positives (indicating values might exist when they don't).
</Info>

## How the Index Works

### Core Concepts

Traditional query processing must examine every segment that might contain matching records, even if many segments ultimately contain no matches. This approach leads to unnecessary I/O and computation.

The Bloom Filter index provides:

1. **Probabilistic Hash Structure**: During indexing, each unique value in the column is hashed and added to a bit array.
2. **Segment-Level Filtering**: One Bloom filter is created per segment for each configured column.
3. **Fast Negative Answers**: When executing a query, the system checks the Bloom filter first to determine if a segment cannot possibly contain the requested value.
4. **Mathematical Trade-offs**: The filter's size, false positive rate, and the column's cardinality are mathematically related, allowing for tunable accuracy versus memory trade-offs.

### Example Illustration

For a query filtering on `playerId = 12345`:

1. **Without Bloom Filter Index**: The system must scan every segment, reading and checking values to find matches.
2. **With Bloom Filter Index**: Before scanning each segment:
   * The system checks the segment for `playerId` value 12345
   * If the filter returns "definitely not present," the entire segment is skipped
   * If the filter returns "possibly present," the segment is scanned normally
   * This eliminates unnecessary work for segments that don't contain the value

For a table with 100 segments where only 5 segments contain records with `playerId = 12345`, the Bloom filter could potentially eliminate processing for 95 segments, dramatically reducing query time.

## Configuration

### Enabling Bloom Filter Index

To enable a Bloom filter index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "playerId",
      "indexes": {
        "bloom": {}
      }
    }
  ]
}
```

This enables a Bloom filter index with default settings.

### Customizing Bloom Filter Index Parameters

To customize the Bloom filter index configuration:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "playerId",
      "indexes": {
        "bloom": {
          "fpp": 0.01,
          "maxSizeInBytes": 1000000,
          "loadOnHeap": true
        }
      }
    }
  ]
}
```

### Alternative Configuration (Legacy Method)

You can also use the older configuration format with default settings:

```json  theme={null}
{
  "tableIndexConfig": {
    "bloomFilterColumns": [
      "playerId"
    ]
  }
}
```

Or with customized parameters:

```json  theme={null}
{
  "tableIndexConfig": {
    "bloomFilterConfigs": {
      "playerId": {
        "fpp": 0.01,
        "maxSizeInBytes": 1000000,
        "loadOnHeap": true
      }
    }
  }
}
```

### Configuration Parameters

1. **fpp**: False positive probability of the Bloom filter
   * Default: 0.05 (5%)
   * Range: 0 to 1
   * Impact: Lower values increase accuracy but also increase memory usage
   * Recommended values: 0.01 to 0.1 depending on accuracy requirements
2. **maxSizeInBytes**: Maximum size of the Bloom filter
   * Default: 0 (unlimited)
   * Impact: Limits memory usage by potentially increasing false positive rate
   * Takes precedence over fpp if both are specified
3. **loadOnHeap**: Memory allocation type
   * Default: false (use off-heap memory)
   * When true: Use Java heap memory
   * When false: Use off-heap memory
   * Impact: Affects memory management and garbage collection
4. **disabled**: Explicitly disable the Bloom filter
   * Default: false
   * When true: Disables the Bloom filter even if other parameters are specified

## Performance Considerations

1. **False Positive Rate vs Memory Usage**: Lower fpp values increase accuracy but require more memory. Choose a value that balances your accuracy needs with memory constraints.
2. **Column Characteristics**: Bloom filters are most effective for columns with:
   * High cardinality (many unique values)
   * Selective equality predicates (filtering for specific values)
   * Values distributed across segments (not all values in all segments)
3. **Query Patterns**: Bloom filters accelerate queries with:
   * Equality conditions (`column = value`)
   * IN predicates with up to 10 values (`column IN (value1, value2, ...)`)
   * They do not help with range queries, LIKE, or other non-equality filters
4. **Segment Distribution**: The benefit increases with the number of segments that can be pruned. If all segments contain all values, the benefit will be minimal.
5. **Memory Management**: Use loadOnHeap=true with caution, as it impacts Java garbage collection. For most cases, the default off-heap setting is recommended.

Built with [Mintlify](https://mintlify.com).
