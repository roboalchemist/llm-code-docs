# Source: https://docs.startree.ai/recipes/startree-index.md

# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/startree-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Star-tree Index

> The Star-tree index boosts aggregation and group-by query performance. It pre-aggregates data across multiple dimensions to reduce query latency and storage usage.

## Overview and Purpose

A star-tree index is an advanced multi-dimensional indexing structure that significantly accelerates aggregation and group-by queries by using pre-computed aggregation results. Unlike single-column indexes, star-tree indexes work across multiple dimensions to dramatically reduce the number of records that need to be processed at query time.

One of the biggest challenges in real-time analytics is maintaining low query latencies on large datasets while efficiently using storage resources. Traditional indexes improve query performance but are still limited by the number of records that must be processed. Pure pre-aggregation strategies guarantee fast query responses but can lead to storage explosion.

Star-tree indexes in StarTree Cloud provide an optimal balance between these approaches by selectively pre-aggregating data based on common query patterns, offering:

* Predictable, low query latencies for aggregation operations
* Efficient use of storage space compared to full pre-aggregation
* Significant performance improvements for multi-dimensional queries
* Configurable trade-offs between query speed and storage requirements

<Info>
  Star-tree indexes are particularly valuable for analytical workloads with high query volumes on large datasets where aggregation queries are common.
</Info>

## How the Index Works

### Core Concepts

The star-tree index creates a hierarchical tree structure that organizes data based on multiple dimensions. The key elements of this structure include:

1. **Dimension-based Organization**: Data is organized hierarchically based on an ordered list of dimensions, with each level in the tree representing a particular dimension.
2. **Pre-aggregation**: For each node in the tree, metrics are pre-aggregated, allowing the system to directly use these pre-computed results when possible.
3. **Star Nodes**: Special nodes that contain pre-aggregated results after removing a specific dimension, enabling efficient handling of queries that don't filter on certain dimensions.
4. **Configurable Depth**: The tree depth and node size can be configured to balance between storage requirements and query performance.

### Example Illustration

Consider a dataset with dimensions Country, Browser, and Locale, and a metric Impressions:

1. **Traditional Approach**: To find the sum of Impressions for USA, Chrome across all Locales, the system would need to scan all matching records and compute the sum at query time.
2. **Star-tree Approach**:
   * The data is organized hierarchically by Country, then Browser, then Locale
   * At the Country=USA, Browser=Chrome level, a star node pre-computes the sum across all Locales
   * The query directly uses this pre-computed result without scanning individual records

This approach significantly reduces query time by eliminating the need to process individual records when aggregate values can be used instead.

## Tree Structure and Components

### Node Types

1. **Root Node**: The single starting point of the tree from which all other nodes can be traversed.
2. **Leaf Node**: Contains at most T records (where T is configurable), representing the most granular level of data.
3. **Non-leaf Node**: Contains more than T records and is further split into child nodes based on the next dimension in the split order.
4. **Star Node**: A special child node that contains pre-aggregated records after removing the dimension on which data was split at that level.

### Node Properties

Each node in the star-tree contains:

* **Dimension**: The dimension the node is split on
* **Document ID Range**: The range of documents this node encompasses
* **Aggregated Document ID**: A single document containing the pre-aggregated results for all documents in this node

## Configuration

### Enabling Star-tree Index

To enable a star-tree index in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
{
  "tableIndexConfig": {
    "starTreeIndexConfigs": [
      {
        "dimensionsSplitOrder": [
          "country",
          "browser",
          "locale"
        ],
        "skipStarNodeCreationForDimensions": [],
        "functionColumnPairs": [
          "SUM__impressions",
          "COUNT__*"
        ],
        "maxLeafRecords": 10000
      }
    ]
  }
}
```

### Alternative Configuration Using Aggregation Configs

You can also use the more detailed `aggregationConfigs` approach with compression settings:

```json  theme={null}
{
  "tableIndexConfig": {
    "starTreeIndexConfigs": [
      {
        "dimensionsSplitOrder": [
          "country",
          "browser",
          "locale"
        ],
        "skipStarNodeCreationForDimensions": [],
        "aggregationConfigs": [
          {
            "columnName": "impressions",
            "aggregationFunction": "SUM",
            "compressionCodec": "LZ4"
          },
          {
            "columnName": "*",
            "aggregationFunction": "COUNT"
          }
        ],
        "maxLeafRecords": 10000
      }
    ]
  }
}
```

### Default Star-tree Index

For a simpler approach, you can enable the default star-tree index:

```json  theme={null}
{
  "tableIndexConfig": {
    "enableDefaultStarTree": true
  }
}
```

The default configuration:

* Includes all single-value dictionary-encoded dimensions with cardinality ≤ 10,000
* Sorts dimensions by cardinality in descending order
* Appends time columns at the end of the dimension split order
* Includes COUNT(\*) and SUM for all numeric metrics
* Uses a default maxLeafRecords value of 10,000

### Configuration Parameters

1. **dimensionsSplitOrder**: An ordered list of dimension names that determines the split order in the tree.
   * Only these dimensions are included in the star-tree index
   * The order is important as it determines the hierarchy of the tree
   * All columns in the filter and group-by clauses should be included for the index to be used
2. **skipStarNodeCreationForDimensions**: (Optional) Dimensions for which star nodes should not be created.
3. **functionColumnPairs** / **aggregationConfigs**: The metrics and aggregation functions to pre-compute.
   * Format for functionColumnPairs: FUNCTION\_\_COLUMN (e.g., SUM\_\_impressions)
   * All aggregations in a query must be included here for the star-tree to be used
4. **maxLeafRecords**: (Optional, default 10,000) The threshold for splitting nodes further.
5. **compressionCodec**: (Optional, via aggregationConfigs) The compression type for aggregated values.

### Supported Aggregation Functions

The star-tree index supports aggregation functions that have bounded-sized intermediate results:

* **SUM**, **MIN**, **MAX**, **COUNT**
* **AVG** (implemented as SUM/COUNT)
* **DISTINCTCOUNT** variants with bounded intermediate size:
  * DISTINCTCOUNT\_HLL
  * DISTINCTCOUNT\_THETA\_SKETCH
  * DISTINCTCOUNT\_CPC\_SKETCH
  * DISTINCTCOUNT\_TUPLE\_SKETCH
* **PERCENTILE** implementations with bounded size:
  * PERCENTILE\_TDIGEST

Unsupported functions include:

* Basic DISTINCTCOUNT (unbounded Set)
* PERCENTILE (unbounded List)

## Query Behavior and Optimization

### When Star-tree Index Is Used

The star-tree index is automatically used when:

1. All predicates in the query are supported by the star-tree index
2. All group-by columns are included in the dimensionsSplitOrder
3. All aggregation functions are included in the index configuration

### How Queries Are Optimized

When a query is executed with a star-tree index:

1. The system first checks if the query can be answered using the star-tree
2. It traverses the tree to identify nodes that satisfy the query predicates
3. For each level in the tree:
   * If no predicate or group-by exists on the split dimension, the star node is selected if available
   * If predicates exist on the split dimension, only matching child nodes are selected
   * If no predicate but a group-by exists on the split dimension, all child nodes except the star node are selected
4. The system collects documents from selected nodes:
   * If all predicates and group-bys are satisfied, it uses the single pre-aggregated document from each node
   * Otherwise, it processes all documents in the range

### Supported Predicates

* **Equality**: column = value
* **Range**: >, >=, \<, \<=, BETWEEN
* **NOT**: Applied to simple predicates (added in 1.2.0)
* **OR**: Only for predicates on the same dimension

### Unsupported Predicates

* **REGEXP\_LIKE**: Not supported as it requires scanning the entire dictionary
* **IS NULL/IS NOT NULL**: Limited support (use column = default or column != default as workaround)
* **OR across dimensions**: Cannot be used due to double-counting risks
* **Complex NOT**: NOT on top of AND/OR is not supported

Built with [Mintlify](https://mintlify.com).
