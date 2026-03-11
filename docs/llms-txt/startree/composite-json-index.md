# Source: https://docs.startree.ai/corecapabilities/manage-data/indexes/composite-json-index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Composite JSON Index

> Use the Composite JSON index to accelerate complex JSON queries by enabling efficient filtering and retrieval of nested fields.

## Overview and Purpose

The Composite JSON Index is an enhanced version of the [JSON Index](/corecapabilities/manage-data/indexes/json-index).

<Info>
  The Composite JSON Index is available from Startree version 0.11.0.
</Info>

In addition to the features of the JSON index, this index supports:

* Indexing select path(s) with internal range, FST or text index.
* Controlling which paths are included in inverted index (to make the index smaller, speed up index build).
* Applying a filter to the number of matching flattened documents (per JSON document).
* Controlling how often to flush with the off-heap index creator and also limiting temporary memory usage.
* Disabling the indexing of array positions (to make the index smaller).

The composite JSON index heavily optimizes document ID mappings to reduce the index size and improve performance.

<Warning>
  Creating both the JSON Index and the Composite JSON Index on the same column is not recommended. When evaluating the JSON\_MATCH function, Pinot first checks for the regular JSON Index, ignoring the Composite JSON Index.
</Warning>

### Example Illustration

Benchmark testing shows a significant response time reduction for range expressions.

Consider the query:

```json  theme={null}
select count(*) 
from users 
where JSON_MATCH(json, '"$[*].TSTMP" between 1577836800000 AND 1735689599999')
```

The query takes 1200ms with a regular JSON index, but only 5ms with the composite JSON index.

## Configuration

### Enabling Composite JSON Index

To enable a composite JSON index on a column in your StarTree Cloud table, add the following configuration to your table definition:

```json  theme={null}
"compositeJson": {
   "flushThreshold": 10000,
   "enablePositionalIndexing": true,
   "invertedIndexConfigs": [{"path": "$.id"}]
   "rangeIndexConfigs": [{
         "path": "$[*].dateTime",
         "name" : "dateTime",
         "dataType": "LONG",
         "createDictionary":"true",
         "dictionaryType": "fixedLength",
         "defaultValue": "0"
    }]
   "textIndexConfigs": [{"path": "$[*].skills", "name" : "skills"}]
}
```

### Configuration Parameters

The composite JSON index configuration supports the JSON index options, as well as:

1. **flushThreshold**: Flush off-heap posting list every n documents to limit memory usage.
2. **enablePositionalIndexing**: Indicates whether to include array indexes or not.
   * Optional
   * Default: true
   * When set to false, then Pinot won't include array indexes in the inverted index.
3. **invertedIndexConfigs**: A list of paths to add to the inverted index.
   * Default: empty
   * Can be a single element with `"includeAllPaths":true`, to include everything
4. **rangeIndexConfigs**: A list of paths to include in internal range index(es), along with settings.\
   Supports the following parameters:
   * **path**: JSON path of field to index
     * Required
   * **name**: The name for the field.
     * Required and must be unique.
   * **dataType**: Data type of the JSON field.
     * Required
     * When `createDictionary=true`, this parameter accepts accepts INT, LONG, FLOAT, DOUBLE, STRING, BIG\_DECIMAL.
     * Otherwise this parameter accepts INT, LONG, FLOAT, DOUBLE.
   * **createDictionary**: Indicates whether to create the dictionary for the field.
     * Optional
     * Default: false
   * **dictionaryType**: Indicates the type, fixedLength or variableLength.
     * Optional
     * Default: variableLength
     * Due to dictionary limitations, Pinot currently supports only variableLength for BIG\_DECIMAL.
   * **defaultValue**: A value for flattened records that don't include the field, or that contain a badly formed value.
     * Optional
5. **textIndexConfigs**: A list of paths to include in the internal Lucene text index(es).
   * Accepts path and name parameters.
   * The name parameter must be unique.

### Example Queries

**Range-index-based range query against a JSON field**

```json  theme={null}
SELECT count(*) 
FROM users 
WHERE JSON_MATCH(json, '""$[*].timestamp" between 1577836800000 AND 1735689599999')
```

**Text-index-based TEXT\_MATCH against JSON field**

```json  theme={null}
SELECT count(*) 
FROM users 
WHERE JSON_MATCH(json, 'TEXT_MATCH("$[*].DX", ''/E99.*/'' ')
```

See the [Pinot documentation](https://docs.pinot.apache.org/basics/indexing/text-search-support) for more information.

**Select only documents with at least 5 matching flattened documents**

```json  theme={null}
SELECT count(*) 
FROM users 
WHERE JSON_MATCH(json, '"$[*].id"=10', '"cnt" >= 5')
```

### Range Index Default Values

The range index contains value for each flattened row. If value is missing or unparseable then either user-set or fixed - '0' - default is used. That default might cause unexpected results to appear when range-querying without upper or lower bound. For example, with no `defaultValue` set, the following query will include documents without a `value` field:

```json  theme={null}
SELECT count(*) FROM users WHERE JSON_MATCH(json, '""$.value" < 3')
```

### Array Position Indexing

A query that specifies an array index in the JSON path will require the `enablePositionalIndexing=true` parameter configuration, even when path is range-indexed. Otherwise, the query will return an empty result. For example, the following query:

```json  theme={null}
SELECT count(*) 

FROM users 

WHERE JSON_MATCH(json, '""$.grades[1].value" between 1 AND 10')
```

That is because array index values are stored as separate bitmaps in the inverted index.

### Range Queries against Mutable Segments

A range index is used for immutable/commited segments, while mutable segments rely on the inverted index. When indexing hybrid or real-time tables, you must include paths used for range queries in the inverted index. Otherwise queries will return empty results for the mutable segments.

Consider the following example configuration:

```json  theme={null}
  "invertedIndexConfigs": [{}]
   "rangeIndexConfigs": [{
         "path": "$[*].dateTime",
         "name" : "dateTime",
         "dataType": "LONG",
         "createDictionary":"true",
         "dictionaryType": "fixedLength",
         "defaultValue": "0"
    }]
```

The inverted index configuration is empty. In such a case, the following query will return correct results only for for the immutable segments:

```json  theme={null}
SELECT count(*) 
FROM users 
WHERE JSON_MATCH(json, '""$.grades[*].value" between 1 AND 10')
```

The mutable/realtime segments will produce no rows because they can’t use the range index and the inverted index is empty.

### Text Index Configuration

Apart from the path and name, the textIndexConfig can contain fields allowed in regular text index configuration:

"rawValue", "queryCache", "useANDForMultiTermQueries", "stopWordsInclude", "stopWordsExclude",\
"luceneUseCompoundFile", "luceneMaxBufferSizeMB", "luceneAnalyzerClass", "luceneAnalyzerClassArgs",\
"luceneAnalyzerClassArgTypes", "luceneQueryParserClass", "enablePrefixSuffixMatchingInPhraseQueries",\
"reuseMutableIndex", "luceneNRTCachingDirectoryMaxBufferSizeMB"

For more information on the text index and configuration, see the [Pinot documentation](https://docs.startree.ai/corecapabilities/manage-data/indexes/text-index).

### FST Index Configuration

We can use FST index to accelerate regex and prefix text search queries as part of the composite JSON index.

<Info>
  FST index within composite JSON was added in Startree 0.12 release
</Info>

Example configuration:

```json  theme={null}
"compositeJson": {
   "flushThreshold": 10000,
   "enablePositionalIndexing": true,
   "invertedIndexConfigs": [{"path": "$.email"}],
   "fstIndexConfigs": [
     {
       "name": "propsText",
       "path": "$.email"
     }
   ]
}
```

Note: FST index requires inverted index(dictionary) for the path to be enabled

Built with [Mintlify](https://mintlify.com).
