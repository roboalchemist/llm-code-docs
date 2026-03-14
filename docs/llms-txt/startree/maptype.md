# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/data-modeling/maptype.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Map type

Use the **MAP** data type to efficiently store and query semi-structured data where the number of keys is large or unpredictable (e.g., Metric labels, cloud tags, or application metadata).

## **Overview and Purpose**

The MAP data type  bridges the gap between flexible JSON blobs and rigid dedicated columns. It is designed for observability use cases where data is semi-structured and sparse.

Unlike a standard JSON string column, the MAP type uses a specialized **Forward Index** that intelligently adapts to your data:

* **Dense Keys:** Frequently occurring keys (e.g., host, region) are automatically detected and stored as efficient, column-like structures (Dense Storage) for fast **O(1)** retrieval.
* **Sparse Keys:** Rare keys (e.g., error\_id) are stored in a compact Key-Value format (Sparse Storage) to save disk space.

This hybrid approach allows you to maintain schema flexibility without sacrificing query performance or storage efficiency.

## **Configuration**

To use the MAP data type, you must update both your **Schema** and **Table Configuration**.

### **1. Schema Definition**

Define the column using complexFieldSpecs. You must specify the dataType as MAP and provide childFieldSpecs for both the key and the value.

* **Key:** Must be of type STRING.
* **Value:** Can be strongly typed (e.g., INT, STRING, LONG, FLOAT, DOUBLE).

[<u>https://docs.pinot.apache.org/configuration-reference/schema#complexfieldspec</u>](https://docs.pinot.apache.org/configuration-reference/schema#complexfieldspec)

**Example Schema:**

```
{
  "schemaName": "appLogs",
  "complexFieldSpecs": [
    {
      "name": "attributes",
      "dataType": "MAP",
      "fieldType": "COMPLEX",
      "childFieldSpecs": {
        "key": {
          "name": "key",
          "dataType": "STRING",
          "fieldType": "DIMENSION"
        },
        "value": {
          "name": "value",
          "dataType": "STRING",
          "fieldType": "DIMENSION"
        }
      }
    }
  ]
}
```

### **2. Table Configuration**

In the table configuration, you can tune the behavior of the Forward Index (to control Dense vs. Sparse behavior) and enable the JSON Index (for fast filtering).

Configure the forward index properties under the indexes section.

| **Parameter**              | **Default** | **Description**                                                                                                |
| :------------------------- | :---------- | :------------------------------------------------------------------------------------------------------------- |
| maxDenseKeys               | 32          | The maximum number of keys to promote to "Dense" (columnar) storage.                                           |
| denseKeyThresholdPct       | 70.0        | The frequency threshold (0-100). A key must appear in this percentage of rows to be promoted to Dense storage. |
| dynamicallyCreateDenseKeys | true        | If true, the engine automatically identifies dense keys during segment creation.                               |

## Index Support on MAP type columns

<u>Currently Json and Composite Json Index are supported for MAP type columns.</u>

Enable the json index to support high-performance filtering (Inverted, Range, and Text indexing) on your Map keys.

[<u>https://docs.startree.ai/corecapabilities/manage-data/indexes/composite-json-index</u>](https://docs.startree.ai/corecapabilities/manage-data/indexes/composite-json-index)

[<u>https://docs.startree.ai/corecapabilities/manage-data/indexes/json-index#json-index</u>](https://docs.startree.ai/corecapabilities/manage-data/indexes/json-index#json-index)

**Example Table Config:**

```
{
  "tableIndexConfig": {
    "indexes": {
      "forward": {
        "configs": {
          "maxDenseKeys": 50,
          "denseKeyThresholdPct": 50.0,
          "dynamicallyCreateDenseKeys": true
        }
      },
      "json": {
        "enabled": true,
        "maxLevels": 2,
        "excludeArray": false
      }
    }
  }
}
```

## Queries

Querying MAP columns uses standard SQL syntax with the \*\*bracket \['key'] \*\*notation.

### **Selection**

Select specific keys directly. If a key does not exist for a row, it returns null.

```
SELECT attributes['host'] AS host, attributes['region'] AS region
FROM appLogs
LIMIT 10
```

### **Filtering**

Filter records based on map values. If the JSON index is enabled, these lookups use the inverted index for sub-second latency.

```
-- Equality Check
SELECT count(\*) FROM appLogs 
WHERE attributes['status'] = 'failed'

-- Set Membership
SELECT \* FROM appLogs 
WHERE attributes['tier'] IN ('gold', 'platinum')
```

### **Aggregation and Grouping**

You can aggregate or group by specific map keys just like regular columns.

```
-- Group by a map key
SELECT attributes['team'], COUNT(\*) 
FROM appLogs 
GROUP BY attributes['team']

-- Aggregate a map value (e.g., if Map value type is INT/DOUBLE)
SELECT MAX(metricsMap['latency_ms']) 
FROM appLogs
```

## **Limitations**

* **Nesting:** Currently, only one level of nesting is supported (Key -> Value). You cannot store a Map inside a Map.
* **Multi-Value:** Multi-value Map columns are not supported.
* **Key Type:** The Map key must always be a STRING.

Built with [Mintlify](https://mintlify.com).
