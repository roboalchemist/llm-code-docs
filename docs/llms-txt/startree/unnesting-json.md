# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/data-modeling/unnesting-json.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Unnesting

> JSON unnesting makes it easy to work with deeply nested and semi-structured data. Extract nested fields from JSON objects and arrays into flat, queryable formats during ingestion.

### Why JSON Unnesting?

* **Simplifies Queries**: Flatten nested data for easier filtering, aggregations, and joins.
* **Improves Performance**: Avoids expensive JSON path evaluations at query time.
* **Streamlines Data Modeling**: Convert complex structures into relational form at ingestion.

Whether you’re dealing with clickstream data, telemetry logs, or API responses, unnesting simplifies data modeling and enhances query performance.

### Enabling JSON Unnesting in StarTree

JSON unnesting can be configured via:

* The **StarTree Data Portal UI**, or
* The **ingestion config JSON** using `transformConfigs` and `unnestConfig`.

## Examples

Let's go through a few examples to unnest a JSON Object,

### Example 1: Unnesting a JSON Object

**Input JSON:**

```json  theme={null}
{
  "user": {
    "id": 123,
    "name": "Alice"
  },
  "event": "click"
}
```

**Unnesting Config:**

```json  theme={null}
"ingestionConfig": {
    "transformConfigs": [
      {
        "columnName": "user_id",
        "transformFunction": "JSONPATHLONG(user, '$.id')"
      },
      {
        "columnName": "user_name",
        "transformFunction": "JSONPATHSTRING(user, '$.name')"
      }
    ]
}
```

**Resulting Schema:**

| user\_id | user\_name | event |
| -------- | ---------- | ----- |
| 123      | Alice      | click |

### Example 2: Unnesting an Array into Multiple Rows

**Input JSON:**

```json  theme={null}
{
  "orderId": "A001",
  "items": [
    { "sku": "X1", "qty": 2 },
    { "sku": "X2", "qty": 1 }
  ]
}
```

**Unnesting Config:**

```json  theme={null}
{
 "ingestionConfig": {
   "complexTypeConfig": {
     "delimiter": "_",
      "fieldsToUnnest": ["items"],
      "collectionNotUnnestedToJson": "NON_PRIMITIVE"
   }
 }
}
```

**Resulting Schema:**

| orderId | items\_sku | items\_qty |
| ------- | ---------- | ---------- |
| A001    | X1         | 2          |
| A001    | X2         | 1          |

Built with [Mintlify](https://mintlify.com).
