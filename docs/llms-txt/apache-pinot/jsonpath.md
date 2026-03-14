# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/jsonpath.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/jsonpath.md

# Source: https://docs.pinot.apache.org/functions-1/jsonpath.md

# JSONPATH

Extracts the object value from jsonField based on 'jsonPath', the result type is inferred based on JSON value. This function can only be used in an [ingestion transformation function](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations).

## Signature

> JSONPATH(jsonField, 'jsonPath')

| Arguments    | Description                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| `jsonField`  | An **Identifier**/**Expression** contains JSON documents.                                              |
| `'jsonPath'` | Follows [JsonPath Syntax](https://goessner.net/articles/JsonPath/) to read values from JSON documents. |

{% hint style="warning" %}
**`'jsonPath'`**\` is a literal. Pinot uses single quotes to distinguish them from **identifiers.**\
\
You can use the [JsonPath tester tool](https://jsoning.com/jsonpath/) to test JSON expressions before you import any data.
{% endhint %}

## Usage Examples

The usage examples are based on extracting fields from the following JSON document:

```json
{
  "data": {
    "name": "Pete",
    "age": 24,
    "subjects": [
      {
        "name": "maths",
        "homework_grades": [80, 85, 90, 95, 100],
        "grade": "A",
        "score": 90
      },
      {
        "name": "english",
        "homework_grades": [60, 65, 70, 85, 90],
        "grade": "B",
        "score": 70
      }
    ]
  }
}
```

| Expression                 | Value    |
| -------------------------- | -------- |
| `JSONPATH(data, '$.name')` | `"Pete"` |
| `JSONPATH(data, '$.age')`  | `24`     |

This function can be used in the [table config](https://docs.pinot.apache.org/configuration-reference/table) to extract the `name` property into the `name` column and `age` property into the `age` column, as described below:

```json
{
   "tableConfig":{
      "ingestionConfig":{
         "transformConfigs":[
            {
               "columnName":"name",
               "transformFunction":"JSONPATHSTRING(data, '$.name')"
            },
            {
               "columnName":"age",
               "transformFunction":"JSONPATHSTRING(data, '$.age')"
            }
         ]
      }
   }
}
```
