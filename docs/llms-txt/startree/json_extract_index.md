# Source: https://docs.startree.ai/corecapabilities/query_data/functions/json_extract_index.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Extract Index

`json_extract_index` is a high-performance JSON extraction function in Apache Pinot and StarTree Cloud. Unlike `json_extract_scalar`,
which parses raw JSON strings at query time, this function reads values directly from the **JSON index**.
By leveraging the prebuilt index, it reduces parsing overhead and improves query latency for large or deeply nested JSON documents.

<Callout type="info">
  For smaller JSON payloads or highly selective queries, the standard <code>json\_extract\_scalar</code> function may still perform better.
</Callout>

### Syntax

```sql  theme={null}
json_extract_index(jsonFieldName, 'jsonPath', 'resultType', ['defaultValue'])
```

#### Parameters

| Parameter                       | Description                                                                                                      |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **`jsonFieldName`**             | The name of the JSON column. The column must have a JSON index configured.                                       |
| **`jsonPath`**                  | The JSONPath expression that identifies which field to extract.                                                  |
| **`resultType`**                | The expected output type: `INT`, `LONG`, `FLOAT`, `DOUBLE`, `BIG_DECIMAL`, `STRING`, or their `_ARRAY` variants. |
| **`defaultValue`** *(optional)* | The value to return when the path does not exist. If omitted, Pinot throws an error.                             |

#### Examples

```sql  theme={null}
select ... group by json_extract_index(col, '$.keyA, 'STRING', 'null')
```

```sql  theme={null}
select ... regexp_like(json_extract_index(json_data, '$.keyA, 'STRING', 'null'), 'val')
```

### How It Works

When a query uses json\_extract\_index, Pinot accesses the JSON index to fetch the requested value directly, instead of deserializing the entire JSON document. This lookup uses internal index mappings between JSON paths, values, and document IDs, allowing for faster query execution on large datasets.
This function supports both single-value and multi-value results, depending on the structure of the field being extracted.

### When to Use

Use json\_extract\_index when:
• Your dataset contains large JSON blobs or deeply nested objects.
• You need to repeatedly extract the same fields across many records.
• The column has a JSON index(on String or MAP Column) configured in the table schema.
• Ideal for leaf-stage query execution where direct access to the index is available.

### Error Handling

If the specified JSON path doesn’t exist and no default value is defined, the query will throw an error. To make your ingestion resilient, always include a defaultValue when paths may be missing.

Built with [Mintlify](https://mintlify.com).
