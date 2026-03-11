# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/forward-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Forward Index

> The Forward index maps document IDs to column values, enabling efficient data retrieval for queries involving selection, aggregation, and sorting. There are three implementations: dictionary-encoded, sorted, and raw value, optimized for different data characteristics.

## Overview and Purpose

A forward index is the fundamental data structure that maps document IDs (row indices) to their actual column values in StarTree Cloud. It serves as the primary mechanism for retrieving column values when processing queries that select, aggregate, or sort data.

Unlike specialized indexes that accelerate specific query patterns, the forward index is the default storage mechanism that enables basic data access. It maintains a direct mapping from each row to its corresponding values, allowing the system to efficiently retrieve data for any query operation.

Forward indexes are particularly important for:

* SELECT clause operations that retrieve actual values
* Aggregation functions that compute over column values
* GROUP BY and ORDER BY operations that organize results
* Any query pattern that requires access to the raw data values

<Info>
  Forward indexes are enabled by default for all columns. They can be selectively disabled in specific scenarios to save storage space when other indexes sufficiently support your query patterns.
</Info>

## How the Index Works

### Core Concepts

At its core, a forward index implements a straightforward mapping:

```
Document ID (Row Number) → Column Value
```

StarTree Cloud offers multiple implementations of forward indexes, optimized for different data characteristics:

1. **Dictionary-Encoded Forward Index**: Maps row IDs to dictionary IDs rather than actual values, providing space efficiency for columns with low to medium cardinality.
2. **Sorted Forward Index**: Uses run-length encoding for sorted columns, storing only the start and end document IDs for each unique value, offering significant compression benefits.
3. **Raw Value Forward Index**: Stores actual values directly, eliminating dictionary lookup overhead and improving performance for high-cardinality columns.

The implementation choice affects both storage requirements and query performance, with each approach offering different trade-offs.

### Example Illustration

Consider a column storing product categories:

**Dictionary-Encoded Approach**:

1. Create a dictionary mapping unique values to IDs:

   ```
   "Electronics" → 1
   "Clothing" → 2
   "Home" → 3
   "Beauty" → 4
   ```

2. Store these IDs in the forward index instead of the actual values:

   ```
   Row 1 → 1 (representing "Electronics")
   Row 2 → 2 (representing "Clothing")
   Row 3 → 1 (representing "Electronics")
   Row 4 → 3 (representing "Home")
   ```

**Sorted Forward Index Approach** (if the column is sorted): Instead of storing an ID for each row, store ranges:

```
"Clothing" → Rows 1-2
"Electronics" → Rows 3-5
"Home" → Rows 6-8
```

**Raw Value Approach**: Store the actual values directly:

```
Row 1 → "Electronics"
Row 2 → "Clothing"
Row 3 → "Electronics"
Row 4 → "Home"
```

## Types of Forward Indexes

### Dictionary-Encoded Forward Index (Default)

The dictionary-encoded forward index uses bit compression to efficiently store dictionary IDs instead of actual values.

**When to Use:**

* For columns with low to medium cardinality (few unique values)
* When compression is important to reduce storage requirements
* For columns that may benefit from inverted indexes

**Benefits:**

* Significant space savings for columns with duplicate values
* Enables efficient inverted index creation
* Supports compression techniques for further space optimization

**Trade-offs:**

* Adds one level of indirection (dictionary lookup) when retrieving values
* Less efficient for columns with high cardinality
* For string columns, may add padding overhead in the dictionary

### Sorted Forward Index

When a column is physically sorted, StarTree Cloud can use a specialized sorted forward index that combines run-length encoding with dictionary encoding.

**When to Use:**

* For columns that are used as a sort key for the segment
* When the column has an enabled dictionary
* For columns frequently used in range filters and sorting operations

**Benefits:**

* Maximum compression efficiency
* Improved data locality (related values are stored together)
* Automatically serves as both a forward and inverted index
* Enables efficient binary search for range queries

**Requirements:**

* The segment must be sorted by the column
* Dictionary encoding must be enabled for the column

### Raw Value Forward Index

The raw value forward index stores actual values directly instead of dictionary IDs, eliminating dictionary lookup overhead.

**When to Use:**

* For columns with high cardinality (many unique values)
* When query performance is more important than storage efficiency
* For columns rarely used in equality filters

**Benefits:**

* Eliminates dictionary lookup overhead
* Better performance for sequential value scanning
* No padding overhead for variable-length data

**Trade-offs:**

* Typically requires more storage space
* Does not support inverted indexes
* Less efficient for random access patterns

## Configuration

### Dictionary-Encoded Forward Index Configuration

Dictionary-encoded forward indexes are the default. To explicitly configure one:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "productCategory",
      "encodingType": "DICTIONARY",
      "indexes": {
        "forward": {
          "compressionCodec": "LZ4"
        }
      }
    }
  ]
}
```

For multi-value columns with repeated entries, you can enable MV\_ENTRY\_DICT compression:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "productTags",
      "encodingType": "DICTIONARY",
      "indexes": {
        "forward": {
          "compressionCodec": "LZ4",
          "compressionType": "MV_ENTRY_DICT"
        }
      }
    }
  ]
}
```

### Sorted Forward Index Configuration

To enable a sorted forward index for real-time tables, specify the sorted column in the table configuration:

```json  theme={null}
{
  "tableIndexConfig": {
    "sortedColumn": [
      "timestamp"
    ]
  }
}
```

**Note:**

<Warning>
  * For offline tables, data must be pre-sorted before ingestion. The `sortedColumn` property is ignored for offline tables.
  * For online tables, only one column should be included. Using an array with more than one column will not result in segments being sorted by all the columns listed in the array.
</Warning>

### Raw Value Forward Index Configuration

To enable a raw value forward index, set the encoding type to RAW:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "userId",
      "encodingType": "RAW",
      "indexes": {
        "forward": {
          "compressionCodec": "PASS_THROUGH", 
          "deriveNumDocsPerChunk": false,
          "rawIndexWriterVersion": 4,
          "targetDocsPerChunk": 2048,
          "targetMaxChunkSize": 2097152
        }
      }
    }
  ]
}
```

### Compression Options

The following compression options are available:

* **PASS\_THROUGH**: No compression
* **SNAPPY**: Balanced compression ratio and speed
* **ZSTANDARD**: High compression ratio but slower
* **LZ4**: Fast compression with moderate ratio
* **GZIP**: High compression ratio but slower

### Raw Index Configuration Parameters

1. **compressionCodec**: Defines the compression algorithm to use.
2. **deriveNumDocsPerChunk**: For variable-length data, determines whether to derive chunk size dynamically (true) or use a fixed value (false).
3. **rawIndexWriterVersion**: Determines the algorithm version used to create the index (latest is 4).
4. **targetDocsPerChunk**: Sets the target number of documents per chunk.
5. **targetMaxChunkSize**: Sets the maximum size of a chunk in bytes.

### Disabling Forward Index

To disable a forward index for storage optimization:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "filterOnlyColumn",
      "indexes": {
        "forward": {
          "disabled": true
        }
      }
    }
  ]
}
```

## Important Considerations When Disabling Forward Index

Disabling a forward index has the following limitations:

1. **Supported only for offline segments**: Not applicable to real-time segments.
2. **Range index requirements**: If the column has a range index, it must be single-valued and use range index version 2.
3. **Dictionary and inverted index**: To support regeneration on reload, both dictionary and inverted index must be enabled.
4. **Multi-value columns**: Ordering and duplicate entries in multi-value columns will not be preserved if forward index is regenerated after being disabled.
5. **Query limitations**: Columns with disabled forward indexes cannot be used in:
   * SELECT clause
   * GROUP BY or ORDER BY clauses
   * Some aggregation functions (SUM, AVG, etc.)
   * DISTINCT queries
   * Range queries without a version 2 range index

Built with [Mintlify](https://mintlify.com).
