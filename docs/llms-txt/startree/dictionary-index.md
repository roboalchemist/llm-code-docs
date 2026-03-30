# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/dictionary-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Dictionary Index

> The Dictionary index enhances storage efficiency and query performance by encoding repetitive column values into compact dictionary IDs, making it ideal for columns with moderate cardinality and supporting other indexes like inverted and FST indexes.

## Overview and Purpose

A dictionary index is a fundamental indexing structure that improves storage efficiency and query performance by encoding repetitive data. It replaces actual column values with compact dictionary IDs, which is particularly beneficial for columns with a moderate number of unique values repeated across many rows.

In StarTree Cloud (powered by Apache Pinot), dictionary indexes serve as both an encoding mechanism and an indexing structure, enabling:

* Efficient storage of repetitive data through value deduplication
* Faster query processing through compact integer representations
* Reduced memory footprint for columns with moderate cardinality
* Optimized performance for string and other variable-length data types
* Support for other index types that rely on dictionary encoding

<Info>
  Dictionary indexes are enabled by default in StarTree Cloud for most columns, as they typically provide storage and performance benefits. However, they may be less efficient for columns with very high cardinality (where unique values approach the number of rows).
</Info>

## How the Index Works

### Core Concepts

When data contains repetitive values across many rows, storing each value individually wastes space and reduces query efficiency. Dictionary encoding addresses this challenge through value deduplication.

The dictionary index in StarTree Cloud:

1. Creates a **value mapping** table (dictionary) that assigns a unique integer ID to each unique value in the column.
2. Performs **ID substitution**, replacing actual values in the data with their corresponding dictionary IDs, which are typically much smaller.
3. Offers **bidirectional lookup** by maintaining structures for both:
   * Forward lookup: ID → Value (for retrieving original values)
   * Reverse lookup: Value → ID (for encoding and filtering)
4. Serves a **dual purpose**, by functioning as both a storage optimization technique and an indexing structure that enables efficient value lookups.

### Example Illustration

For a column storing countries with many repeated values:

1. **Original Data**:

   ```
   Row 1: "United States"
   Row 2: "Canada"
   Row 3: "United States"
   Row 4: "United Kingdom"
   Row 5: "Canada"
   ...
   ```

2. **Dictionary Approach**:
   * Create a dictionary mapping unique values to IDs:

     ```
     ID 0: "United States"
     ID 1: "Canada"
     ID 2: "United Kingdom"
     ...
     ```

   * Store the column using the more compact IDs:

     ```
     Row 1: 0
     Row 2: 1
     Row 3: 0
     Row 4: 2
     Row 5: 1
     ...
     ```

This approach significantly reduces storage requirements, especially for strings and other variable-length data types, while enabling efficient lookups and transformations.

## Relationship with Other Indexes

Dictionary indexes influence the behavior and implementation of many other index types:

| Index Type          | Relationship | Description                                                    |
| :------------------ | :----------- | :------------------------------------------------------------- |
| Forward Index       | Conditional  | Implementation depends on whether dictionary is enabled        |
| Range Index         | Conditional  | Implementation depends on whether dictionary is enabled        |
| Inverted Index      | Required     | Requires dictionary index to be enabled                        |
| JSON Index          | May disable  | When optimizeDictionary is enabled, dictionary may be disabled |
| Text Index          | May disable  | When optimizeDictionary is enabled, dictionary may be disabled |
| FST Index           | Required     | Requires dictionary index to be enabled                        |
| H3/Geospatial Index | Incompatible | Cannot use dictionary index                                    |

## Configuration

### Default Behavior

Dictionary indexes are enabled by default for all columns, based on the assumption that the number of unique values will be significantly lower than the number of rows.

### Explicitly Disabling Dictionary Index

To disable a dictionary for a column with high cardinality, use one of these approaches:

**Method 1**: Using the `dictionary` property in `indexes`:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "highCardinalityColumn",
      "indexes": {
        "dictionary": {
          "disabled": true
        }
      }
    }
  ]
}
```

**Method 2**: Setting `encodingType` to `RAW`:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "highCardinalityColumn",
      "encodingType": "RAW"
    }
  ]
}
```

**Method 3**: Using the `noDictionaryColumns` table configuration:

```
  "tableIndexConfig": {
    "noDictionaryColumns": ["column1", "column2"]
  },
```

### Heuristic Dictionary Configuration

For columns where the decision to use a dictionary isn't clear, you can enable heuristic-based dictionaries at the table level:

```json  theme={null}
{
  "tableIndexConfig": {
    "optimizeDictionary": true,
    "noDictionarySizeRatioThreshold": 0.85
  }
}
```

### Heuristic Parameters

1. **optimizeDictionary**: When set to true, enables heuristic dictionary creation for all eligible columns.
   * Default: false
2. **optimizeDictionaryForMetrics**: When set to true, enables heuristic dictionary creation only for metric columns.
   * Default: false
   * Note: optimizeDictionary takes precedence if both are specified
3. **noDictionarySizeRatioThreshold**: The ratio threshold used to determine if a dictionary should be created.
   * Default: 0.85
   * Meaning: If the ratio of (dictionary-encoded size)/(raw-encoded size) is lower than this threshold, the dictionary is created

### Advanced Configuration Parameters

You can use advanced configuration parameters for fine-tuning the dictionary behavior.

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "productName",
      "encodingType": "DICTIONARY",
      "indexes": {
        "dictionary": {
          "onHeap": false,
          "useVarLengthDictionary": false,
          "intern": {
            "capacity": 32000
          }
        }
      }
    }
  ]
}
```

1. **onHeap**: Determines whether the dictionary is stored in Java heap memory.
   * Default: false (off-heap)
   * When true: Dictionary is loaded into Java heap memory
   * When false: Dictionary is kept in off-heap memory (recommended)
   * Impact: May slightly improve performance, but increases heap usage and GC pressure
2. **useVarLengthDictionary**: Controls storage approach for variable-length data (strings, bytes, etc.).
   * Default: false
   * When false: All values are padded to the length of the longest value
   * When true: Values are stored with their actual length plus an offset
   * Recommended: Set to true when the length of values varies significantly
3. **intern**: Controls string interning for on-heap dictionaries.
   * Only applies to string and byte columns with onHeap=true
   * Purpose: Reduces memory usage when the same values appear across segments
4. **intern.capacity**: Maximum number of distinct values to intern.
   * Default: null (no interning)
   * Recommended: Set based on the estimated unique values across segments

## Performance Considerations

1. **Cardinality Trade-offs**:
   * Low cardinality (few unique values): Dictionary provides significant benefits
   * High cardinality (many unique values): Raw encoding may be more efficient
   * Rule of thumb: If the ratio of unique values is greater than 30% of total rows, consider disabling dictionary
2. **Variable Length Data**:
   * For string columns with widely varying lengths, set useVarLengthDictionary to true
   * For string columns with similar lengths, keep the default false for better performance
3. **Memory Management**:
   * Keep dictionaries off-heap (default) in most cases
   * Use on-heap dictionaries with caution, only for low-cardinality columns
   * When using on-heap dictionaries, consider enabling interning to reduce the memory footprint
4. **Segment Considerations**:
   * Dictionary scope is per segment
   * Very large tables may have many segments, each with its own dictionary
   * This can impact memory usage, especially with on-heap dictionaries

Built with [Mintlify](https://mintlify.com).
