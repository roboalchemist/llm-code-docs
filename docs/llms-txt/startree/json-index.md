# Source: https://docs.startree.ai/recipes/json-index.md

# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/json-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Index

> The JSON index flattens and indexes JSON structures to allow fast, path-based filtering without the need for full document parsing.

## Overview and Purpose

A JSON index is a specialized data structure that accelerates filtering operations on JSON string columns. It enables efficient value lookups within JSON documents, without requiring the system to parse and analyze the entire JSON at query time.

JSON strings provide flexibility for representing complex data structures such as arrays, maps, and nested fields, without enforcing a rigid schema. However, without proper indexing, queries that filter on JSON content can be computationally expensive as they require scanning and reconstructing the entire JSON object for each record.

JSON indexes are particularly valuable for:

* Applications using JSON to store semi-structured or schema-flexible data
* Queries that filter on specific fields or paths within JSON documents
* Nested data structures where some fields are frequently used for filtering
* Use cases requiring fast lookups within arrays or nested objects

<Info>
  The JSON index optimizes query performance by pre-processing JSON documents during indexing, creating a flattened and searchable representation that dramatically reduces query-time computation.
</Info>

## How the Index Works

### Core Concepts

Traditional approaches to JSON filtering require the system to:

1. Scan every record in the table
2. Parse each JSON string into a structured object
3. Extract the required value based on the specified path
4. Apply the filter condition to determine matches

This process is computationally expensive, especially for large datasets or complex JSON structures.

The JSON index in StarTree Cloud optimizes this process, by:

1. **Flattening**: During indexing, the system "flattens" the JSON structure, extracting key-value pairs using paths that identify each value's location in the original structure.
2. **Path Indexing**: The flattened key-value pairs are indexed, allowing fast lookups based on specific JSON paths.
3. **Array Handling**: Arrays are processed by either:
   * Creating separate entries for each array element
   * Combining elements from multiple arrays using cross-array unnesting
4. **Query Optimization**: At query time, the system can directly access the indexed paths without parsing the entire JSON structure.

### Example Illustration

Consider a JSON document representing a person:

```json  theme={null}
{
  "name": "adam",
  "age": 30,
  "addresses": [
    {
      "number": 112,
      "street": "main st",
      "country": "us"
    },
    {
      "number": 2,
      "street": "second st",
      "country": "ca"
    }
  ]
}
```

Without a JSON index, to find all persons with addresses in "ca", the system would need to parse and analyze every JSON document.

With a JSON index, the document is flattened during indexing into entries like:

* `name`: "adam"
* `age`: 30
* `addresses[0].number`: 112
* `addresses[0].street`: "main st"
* `addresses[0].country`: "us"
* `addresses[1].number`: 2
* `addresses[1].street`: "second st"
* `addresses[1].country`: "ca"

At query time, the system can directly check the indexed values for `addresses[*].country` = "ca" without parsing the entire JSON structure.

## Configuration

### Enabling JSON Index

To enable a JSON index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "jsonColumn",
      "indexes": {
        "json": {
          "maxLevels": 5,
          "excludeArray": false,
          "disableCrossArrayUnnest": false,
          "includePaths": null,
          "excludePaths": null,
          "excludeFields": null,
          "indexPaths": null,
          "maxValueLength": 0,
          "skipInvalidJson": false
        }
      }
    }
  ]
}
```

For a simple configuration with default values, you can use:

```json  theme={null}
{
  "fieldConfigList": [
    {
      "name": "jsonColumn",
      "indexes": {
        "json": {}
      }
    }
  ]
}
```

### Configuration Parameters

1. **maxLevels**: Maximum levels to flatten in the JSON object (arrays count as one level)
   * Default: 5
   * Higher values allow indexing deeper nested structures
   * Lower values reduce index size but limit deep path accessibility
2. **excludeArray**: Whether to exclude arrays when flattening the object
   * Default: false
   * When true, array elements are not indexed
   * Useful to reduce index size when arrays aren't used in filters
3. **disableCrossArrayUnnest**: Controls array unnesting behavior
   * Default: false (calculate unique combinations of all elements)
   * When true, prevents cross-product expansion of multiple arrays
   * Recommended for documents with multiple large arrays to avoid combinatorial explosion
4. **includePaths**: Only include the specified JSON paths (mutually exclusive with excludePaths)
   * Example: \["$.name", "$.addresses\[\*].country"]
   * Paths under included paths are automatically included
   * Useful to precisely control which paths are indexed
5. **excludePaths**: Exclude the specified JSON paths (mutually exclusive with includePaths)
   * Example: \["$.age", "$.addresses\[\*].number"]
   * Paths under excluded paths are automatically excluded
   * Useful to omit rarely filtered paths
6. **excludeFields**: Exclude specific field names regardless of path
   * Example: \["street", "zip"]
   * Applies even if the field is under included paths
   * Useful for excluding specific fields across all objects
7. **indexPaths**: Control indexed paths using glob patterns
   * Example: \["*.*", "addresses.\*\*"]
   * More flexible than includePaths/excludePaths
   * Can be combined with other configuration options
8. **maxValueLength**: Maximum length for indexed values
   * Values longer than this are replaced with "$SKIPPED$"
   * Useful for limiting index size when some values are very large
9. **skipInvalidJson**: Handle invalid JSON documents gracefully
   * When true, replaces invalid JSON with empty key/path and "$SKIPPED$" value
   * When false (default), invalid JSON causes errors during indexing

### Alternative Configuration Methods

While the above method is recommended, you can also configure JSON indexes using legacy approaches:

```json  theme={null}
{
  "tableIndexConfig": {
    "jsonIndexConfigs": {
      "jsonColumn": {
        "maxLevels": 5,
        "excludeArray": false
      }
    }
  }
}
```

Or more simply:

```json  theme={null}
{
  "tableIndexConfig": {
    "jsonIndexColumns": [
      "jsonColumn"
    ]
  }
}
```

### Important Configuration Considerations

1. **Column Type**: JSON indexes can only be applied to columns with STRING or JSON data types that contain valid JSON strings.
2. **Dictionary Encoding**: To reduce storage overhead, consider [disabling the dictionary indexes](../indexes/dictionary-index#explicitly-disabling-dictionary-index) on  JSON-indexed columns.
3. **Array Handling**: For documents with multiple large arrays, setting disableCrossArrayUnnest to true can prevent the "Got too many combinations" error, which occurs when more than 100,000 flattened documents would be created.
4. **Index Size**: The index size grows with JSON complexity, depth, and the number of paths indexed. Use configuration parameters to control this.

Built with [Mintlify](https://mintlify.com).
