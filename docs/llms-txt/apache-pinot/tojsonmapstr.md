# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/tojsonmapstr.md

# Source: https://docs.pinot.apache.org/functions-1/tojsonmapstr.md

# TOJSONMAPSTR

Convert map to JSON String. This function can only be used in an [ingestion transformation function](https://docs.pinot.apache.org/developers/advanced/ingestion-level-transformations).

## Signature

> TOJSONMAPSTR(map)

## Usage Examples

The usage examples are based on extracting fields from the following JSON document:

```json
{"timestamp": "2019-10-09 21:25:25", "meta": {"age": 12}}
```

| Expression           | Value            |
| -------------------- | ---------------- |
| `TOJSONMAPSTR(meta)` | `"{\"age\":12}"` |

This function can be used in the [table config](https://docs.pinot.apache.org/configuration-reference/table) to extract the `meta` property into the `data` column, as described below:

```json
{
   "tableConfig":{
      "ingestionConfig":{
         "transformConfigs":[
            {
               "columnName":"data",
               "transformFunction":"TOJSONMAPSTR(meta)"
            }
         ]
      }
   }
}
```
