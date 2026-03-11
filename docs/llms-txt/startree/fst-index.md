# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/fst-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# FST Index

> The FST (Finite State Transducer) index accelerates regex and prefix text queries by compactly encoding dictionary-encoded columns.

## Overview and Purpose

A Finite State Transducer (FST) index is a specialized data structure that accelerates regular expression queries on text columns while dramatically reducing the on-disk index size. It provides efficient pattern matching capabilities while consuming 4-6 times less storage space compared to traditional indexing approaches.

In StarTree Cloud (powered by Apache Pinot), FST indexes are particularly valuable for:

* Supporting regular expression (regex) queries on text columns
* Optimizing prefix match operations (`LIKE 'prefix%'`)
* Reducing index storage requirements for text search functionality
* Pattern matching across large text datasets with storage efficiency
* Applications requiring wildcard searches with storage constraints

<Info>
  FST indexes are optimized for regex operations and prefix queries. They complement text indexes by providing a more storage-efficient option for specific text search patterns.
</Info>

## How the Index Works

### Core Concepts

Traditional text indexing approaches can require significant storage space to enable pattern matching across text data. The FST index takes a different approach, using finite state transducers - a specialized data structure from computational linguistics - to represent patterns efficiently.

The FST index in StarTree Cloud:

1. **Compact Representation**: Represents all possible text patterns in the column as a directed graph structure that recognizes valid strings.
2. **Prefix Optimization**: Particularly efficient for prefix searches, as the FST can quickly traverse the initial states of the automaton.
3. **Storage Efficiency**: Achieves 4-6x reduction in on-disk index size compared to other text indexing approaches.
4. **Dictionary Integration**: Leverages dictionary encoding to further optimize performance and storage.

### Example Illustration

For a column storing product names:

1. **Traditional Text Index**: Stores tokenized terms and their positions, consuming significant storage space.
2. **FST Index Approach**:
   * Builds a finite state automaton representing all product names
   * Enables regex queries like `product LIKE 'Smart%'` to quickly find all products starting with "Smart"
   * Consumes 4-6x less storage space compared to text index

When processing a query like `WHERE product LIKE 'Phone%'`, FST can efficiently traverse the initial states of the automaton that correspond to the prefix "Phone", then identify all possible completions that exist in the data.

## Configuration

### Enabling FST Index

To enable an FST index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```
{
  "fieldConfigList": [
    {
      "name": "productName",
      "encodingType": "DICTIONARY",
      "indexes": {
        "fst": {}
      }
    }
  ]
}
```

### Alternative Configuration (Legacy Method)

You can also use the older configuration format:

```
{
  "fieldConfigList": [
    {
      "name": "productName",
      "encodingType": "DICTIONARY",
      "indexTypes": ["FST"]
    }
  ]
}
```

### Important Configuration Requirements

1. **Dictionary Encoding**: The column must be dictionary-encoded (not RAW encoded).
   * Set `encodingType` to `DICTIONARY` (this is the default if left unspecified)
2. **Segment Types**: FST indexes are only supported on:
   * Completed segments (offline mode)
   * Committed segments (real-time mode)
   * Not supported on consuming segments (real-time in-progress segments)
3. **Complementary Indexing**: FST indexes work well alongside inverted indexes:
   * If an inverted index is also enabled on the same column, the FST index can leverage it for additional performance improvements

## Performance Considerations

1. **Prefix Query Efficiency**: FST indexes perform best with prefix queries (patterns starting with a fixed string followed by wildcards) rather than patterns with leading wildcards.
2. **Storage Benefits**: The primary advantage is the 4-6x reduction in on-disk index size compared to other text index types.
3. **Case Sensitivity**: Remember that the index is case-sensitive, which might require adjustments to query patterns.
4. **Dictionary Requirement**: The requirement for dictionary encoding means FST indexes are best suited for columns with manageable cardinality.
5. **Complementary Use**: Consider using FST indexes alongside other index types:
   * FST for regex and prefix queries
   * Text index for more complex text search needs
   * Inverted index for exact match operations

Built with [Mintlify](https://mintlify.com).
