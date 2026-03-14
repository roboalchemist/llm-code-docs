# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/sparse-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Sparse Index

> The Sparse index improves equality-based query performance on high-cardinality columns. It is a hybrid between inverted indexes and Bloom filters, particularly beneficial for tiered storage environments.

## Overview and Purpose

A sparse index is a specialized data structure that accelerates equality-based filter operations on columns with extremely high cardinality. It represents a hybrid approach between inverted indexes and Bloom filters, designed specifically for scenarios where traditional indexes become inefficient due to the sheer number of unique values.

Sparse indexes are particularly valuable for:

* Columns storing hundreds of thousands of unique values
* Random identifiers like UUIDs or session IDs
* High-cardinality fields such as public IP addresses
* Any query pattern involving equality filters (`column = value` or `column IN (...)`) on high-cardinality columns
* Deployments using tiered storage with data in cloud object stores

<Info>
  Sparse index is a StarTree extension that shows particular performance benefits when used with tiered storage, as they can significantly reduce the amount of data transferred from cloud storage during query execution.
</Info>

## How the Index Works

### Core Concepts

Traditional inverted indexes create a direct mapping between each unique value and the rows containing that value. While effective for low- to medium-cardinality columns, this approach becomes inefficient as cardinality increases, leading to large index sizes and degraded performance.

The sparse index in StarTree Cloud takes a different approach:

1. **Chunking**: Rows are grouped into contiguous chunks of a predefined size.
2. **Partitioning**: Column values are classified into a fixed number of partitions using one or more hash functions (mappers).
3. **Pseudo-Inverted Index**: Instead of mapping values directly to rows, the index maps partitions to chunks that contain values from that partition.

### Example Illustration

For a column storing device IDs with millions of unique values:

1. **Traditional Approach**: An inverted index would map each unique device ID to its corresponding rows, potentially creating an enormous index.
2. **Sparse Index Approach**:
   * Rows are grouped into chunks of 8,192 rows
   * Device IDs are hashed into 1,000 partitions using 10 different hash functions
   * The index maps each partition to the chunks that contain values from that partition

When processing a query like `WHERE deviceId = 'abc123'`:

1. The system determines which partition contains 'abc123'
2. It identifies the chunks associated with that partition
3. Only those chunks are scanned, dramatically reducing I/O operations

This approach is particularly beneficial with tiered storage, as it minimizes the amount of data downloaded from cloud storage.

## Configuration

### Enabling Sparse Index at Server Level

To use sparse indexes, you must first enable them at the server level:

```
pinot.server.instance.index.sparse.enabled=true
```

This can be set via the Swagger UI using the `/cluster/configs` API, or through your server configuration files.

**Note:** After adding this configuration, restart the servers for the changes to take effect.

### Configuring Sparse Index for a Column

To enable a sparse index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "deviceId",
      "indexes": {
        "sparse": {
          "chunkSize": 8192,
          "partitions": 1000,
          "hashFunctionCount": 10
        }
      }
    }
  ]
}
```

### Configuration Parameters

1. **chunkSize**: The number of documents per chunk.
   * Must be a power of 2
   * Default: 8192
   * Recommended range: 1 to 16384
   * Impact: Smaller chunks reduce query latency but may slightly increase index size
   * Affects index size inversely but sub-linearly
2. **partitions**: The number of partitions used for classifying values.
   * Default: 1000
   * Recommended: Depends on the number of unique values in the column
   * Impact: Higher values improve selectivity but increase index size
   * Affects index size linearly
3. **hashFunctionCount**: The number of partition mapping functions used.
   * Default: 10
   * Recommended range: 1 to 20
   * Impact: Higher values increase selectivity but also increase index size
   * Affects index size linearly

### Advanced Configuration Parameters

These parameters are rarely needed and should only be used in specific scenarios:

1. **seedGenerator**: An integer seed for generating hash functions.
   * Only necessary if hash collisions are unusually frequent
2. **mapperId**: Specifies the hash function type.
   * Currently, only "murmur" is supported

## Performance Considerations

1. **Tiered Storage Benefits**: Sparse indexes provide the greatest performance improvements when using tiered storage, as they minimize data transfer from cloud storage.
2. **Cardinality Trade-offs**: For low-cardinality columns (fewer than 1,000 unique values), traditional inverted indexes are typically more efficient.
3. **Parameter Tuning**:
   * For columns with extremely high cardinality, consider increasing the `partitions` value
   * If query latency is a priority, consider decreasing `chunkSize`
   * Balance `hashFunctionCount` based on selectivity needs and storage constraints
4. **Storage Impact**: Increasing `partitions` or `hashFunctionCount` will linearly increase the index size. Double either value, and the index size approximately doubles.

Built with [Mintlify](https://mintlify.com).
