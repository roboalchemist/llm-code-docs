# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/jsonpathdouble.md

# Source: https://docs.pinot.apache.org/functions-1/jsonpathdouble.md

# JSONPATHDOUBLE

Extracts the **Double** value from `jsonField` based on `'jsonPath'`, use optional `defaultValue`for null or parsing error. This function can only be used in an [ingestion transformation function](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations).

## Signature

> JSONPATHDOUBLE(jsonField, 'jsonPath', \[defaultValue])

| Arguments    | Description                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------ |
| `jsonField`  | An **Identifier**/**Expression** contains JSON documents.                                              |
| `'jsonPath'` | Follows [JsonPath Syntax](https://goessner.net/articles/JsonPath/) to read values from JSON documents. |

{% hint style="warning" %}
**`'jsonPath'`**\` is a literal. Pinot uses single quotes to distinguish them from **identifiers**.\
\
You can use the [Jayway JsonPath Evaluator Tool](https://jsonpath.herokuapp.com/) to test JSON expressions before you import any data.
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

| Expression                      | Value  |
| ------------------------------- | ------ |
| `JSONPATHDOUBLE(data, '$.age')` | `24.0` |

This function can be used in the [table config](https://docs.pinot.apache.org/configuration-reference/table) to extract the `age` property into the `age` column, as described below:

```json
{
   "tableConfig":{
      "ingestionConfig":{
         "transformConfigs":[
            {
               "columnName":"age",
               "transformFunction":"JSONPATHDOUBLE(data, '$.age')"
            }
         ]
      }
   }
}
```
