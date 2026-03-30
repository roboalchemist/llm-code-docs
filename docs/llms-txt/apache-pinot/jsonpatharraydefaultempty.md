# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/jsonpatharraydefaultempty.md

# Source: https://docs.pinot.apache.org/functions-1/jsonpatharraydefaultempty.md

# JSONPATHARRAYDEFAULTEMPTY

Extracts an array from `jsonField` based on `'jsonPath'`, the result type is inferred based on JSON value. Returns empty array for null or parsing error. This function can only be used in an [ingestion transformation function](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations).

## Signature

> JSONPATHARRAYDEFAULTEMPTY(jsonField, 'jsonPath')

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

| Expression                                                                    | Value                  |
| ----------------------------------------------------------------------------- | ---------------------- |
| `JSONPATHARRAYDEFAULTEMPTY(myJsonRecord, '$.subjects[*].name')`               | `["maths", "english"]` |
| `JSONPATHARRAYDEFAULTEMPTY(myJsonRecord, '$.subjects[*].score')`              | `[90, 70]`             |
| `JSONPATHARRAYDEFAULTEMPTY(myJsonRecord, '$.subjects[*].homework_grades[1]')` | `[85, 65]`             |
| `JSONPATHARRAYDEFAULTEMPTY(myJsonRecord, '$.subjects[*].homework_grades[7]')` | `[]`                   |

This function can be used in the [table config](https://docs.pinot.apache.org/configuration-reference/table) to extract the `name`, `score`, and second value of `homework_grades` into their respective columns , as described below:

```json
{
   "tableConfig":{
      "ingestionConfig":{
         "transformConfigs":[
            {
               "columnName":"names",
               "transformFunction":"JSONPATHARRAYDEFAULTEMPTY(data, '$.subjects[*].name')"
            },
            {
               "columnName":"ages",
               "transformFunction":"JSONPATHARRAYDEFAULTEMPTY(data, '$.subjects[*].score')"
            },
            {
               "columnName":"homeworkGrades",
               "transformFunction":"JSONPATHARRAYDEFAULTEMPTY(data, '$.subjects[*].homework_grades[1]')"
            }
         ]
      }
   }
}
```
