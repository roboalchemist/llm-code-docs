# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/inverted-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Inverted Index

> The Inverted index maps column values to row locations through bitmap or sorted structures, enabling rapid equality, range, and membership filtering.

## Overview and Purpose

An inverted index is a data structure that maps content (like words or values) to their locations in a database table. Think of it as a book's index that tells you exactly which pages contain specific words - but for your data.

The primary purpose of an inverted index is to dramatically speed up query performance when you're filtering data. Without an index, the system would need to scan every row to find matching values. With an inverted index, it can jump directly to the relevant rows.

Inverted indexes are especially valuable for:

* Equality filters (column = value)
* Membership checks (column IN \[value1, value2])
* Range queries (column > value)
* Any scenario where you frequently filter on specific columns

## How the Index Works

### Core Concepts

In traditional "forward" indexes, the system maps row IDs to their corresponding values:

```
Row 1 → Values (A, B, C)
Row 2 → Values (B, D, E)
Row 3 → Values (A, E, F)
```

An inverted index flips this relationship, mapping values to the rows containing them:

```
Value A → Rows [1, 3]
Value B → Rows [1, 2]
Value C → Rows [1]
Value D → Rows [2]
Value E → Rows [2, 3]
Value F → Rows [3]
```

StarTree Cloud (powered by Apache Pinot) supports two types of inverted indexes:

1. **Bitmap Inverted Index**: Creates a bitmap (a compact way to represent a set of rows) for each unique value in a column. This makes value lookups extremely fast with constant time complexity.
2. **Sorted Inverted Index**: Creates an index leveraging sorted column data structure for efficient binary search operations. This offers logarithmic lookup time and benefits of data locality.

Both types require dictionary encoding to be enabled for the column (which creates a mapping between actual values and encoded IDs).

### Example Illustration

For a `productCategory` column with values:

```
Row 1: "Electronics"
Row 2: "Clothing"
Row 3: "Electronics"
Row 4: "Home"
Row 5: "Clothing"
```

A bitmap inverted index would create:

```
"Electronics" → Bitmap [1,0,1,0,0]  (Rows 1 and 3)
"Clothing" → Bitmap [0,1,0,0,1]     (Rows 2 and 5)
"Home" → Bitmap [0,0,0,1,0]         (Row 4)
```

When filtering for "Electronics", the system immediately knows to retrieve rows 1 and 3 without scanning the entire dataset.

## Types of Inverted Indexes

### Bitmap Inverted Index

A bitmap inverted index maintains a mapping from each value to a bitmap of rows. This design makes value lookups extremely fast with constant time complexity.

**When to Use:**

* For columns with low to medium cardinality (number of unique values)
* When the column is frequently used in filter conditions
* When the column is not sorted

**Benefits:**

* Constant time lookup performance
* Works well with equality filters and IN clauses
* Can be created on multi-value columns

### Sorted Inverted Index

When a column is both sorted and has a dictionary enabled, StarTree Cloud automatically leverages the sorted structure to implement an efficient inverted index.

**When to Use:**

* For columns that are already sorted (like timestamps or sequential IDs)
* When the column is frequently used in filter conditions

**Benefits:**

* Logarithmic lookup time (log(n))
* Better data locality (related values are stored close together)
* Generally better performance than bitmap indexes
* No additional storage overhead (uses the same structure as the forward index)

## Configuration

### Configuring a Bitmap Inverted Index

To enable a bitmap inverted index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```
{
  "fieldConfigList": [
    {
      "name": "yourColumnName",
      "indexes": {
        "inverted": {}
      }
    }
  ]
}
```

### Alternative Configuration (Legacy Method)

You can also use the older configuration format, though it's not recommended for new deployments:

```
{
  "tableIndexConfig": {
    "invertedIndexColumns": [
      "yourColumnName"
    ]
  }
}
```

### Configuring a Sorted Inverted Index

To set up a sorted inverted index:

1. First, configure the column as a sorted column in your table configuration:

```
{
  "tableIndexConfig": {
    "sortedColumn": [
      "yourColumnName"
    ]
  }
}
```

1. Ensure dictionary encoding is enabled for this column (it is enabled by default)

The sorted inverted index will be automatically available without additional configuration when these conditions are met.

### Important Considerations

1. **When the Index is Created**: By default, bitmap inverted indexes are created when segments are loaded by Pinot, not during initial segment generation. If you want to create them during segment generation, set `indexingConfig.createInvertedIndexDuringSegmentGeneration` to `true` in your table configuration.
2. **Dictionary Requirement**: Both types of inverted indexes require dictionary encoding to be enabled for the column.
3. **Multi-Value Support**: You can create a bitmap inverted index on a multi-value column.

If your queries frequently filter on a specific column and performance is critical, consider using a sorted column with its implicit sorted inverted index for maximum efficiency.

Built with [Mintlify](https://mintlify.com).
