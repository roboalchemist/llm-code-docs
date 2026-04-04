# Source: https://docs.startree.ai/corecapabilities/ingestdata/dataportal/data-modeling/concepts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Examples

> Derive new columns or modify existing columns during ingestion by applying expressions, functions, or logic.

Derived columns are useful when:

* You want to compute columns (examples: dayOfWeek, hour, lat\_lon\_hash).
* You need to format or clean up incoming data (trimming strings, parsing timestamps).
* You want to simplify querying by precomputing fields.

Transformations are applied before data is persisted, meaning the transformed fields are stored as part of the segment.

### How it Works

Pinot supports transformations through a section in the table config called `ingestionConfig`. The key part of this is the `transformConfigs`, where each transform is defined as a mapping between a column name and an expression.

Here’s a basic structure:

```json  theme={null}
"ingestionConfig": {
  "transformConfigs": [
    {
      "columnName": "eventDate",
      "transformFunction": "DATETIMECONVERT(event_timestamp, '1:MILLISECONDS:EPOCH', '1:DAYS:SIMPLE_DATE_FORMAT:yyyy-MM-dd')"
    },
    {
      "columnName": "isLargeTransaction",
      "transformFunction": "amount > 1000"
    }
  ]
}
```

#### Components

* `columnName`: The name of the column to be created.
* `transformFunction`: The expression or function that generates the column’s value.

Transformation functions in JSON have the following 3 components:

* transforms
* timeTransforms
* filter

```json  theme={null}
{
  "timeTransforms": [],
  "transforms": [],
  "filter": null
}
```

## Column operations

### Add new columns

You can add new Dimension, Metric or Datetime columns.

Introducing new columns to your Pinot table schema is a seamless process. Whether it's adding dimensions or metrics, mandatory mapping functions can be assigned to these newly created columns. Moreover, DateTime columns can be generated from an existing column, simplifying the management of date formats or varying levels of granularity within your datasets. This feature empowers you to enhance the richness of their data by incorporating new elements efficiently.

#### Dimension column

```json  theme={null}
{
    "name": "student_name",
    "fieldType": "dimension",
    "dataType": "string"
}
```

#### Metric column

```json  theme={null}
{
    "name": "studentID",
    "fieldType": "metric",
    "dataType": "long"
}
```

### Customize columns

When organizing your data in Pinot tables, consider the column data type, for example, as a Dimension, Metric, or DateTime, you can adjust these attributes to suit the nature of the data fetched. Additionally, if your data is structured in arrays, it enables you to configure columns capable of handling multiple values. Moreover, you can set default values for columns in instances where the value is absent. This customization lets you align your data more effectively with your analytical needs.

#### Single value dimension column

```json  theme={null}
{
    "name": "gender",
    "fieldType": "dimension",
    "dataType": "string"
}
```

#### Multi-value dimension column

For columns with multiple values (like `courses`), set the type as `dimension` with `mv(string)` for handling arrays.

```json  theme={null}
{
    "name": "courses",
    "fieldType": "dimension",
    "dataType": "mv(string)"
}
```

#### Set values

To set values for default, customize the max length for string columns, and set the column as mandatory.

```json  theme={null}
{
      "name": "description",
      "maxLength": "5122",
      "notNull": false,
      "dataType": "STRING",
      "defaultNullValue": "null",
      "singleValueField": true,
      "fieldType": "DIMENSION",
}
```

### Delete columns

Keeping your Pinot table schema concise and relevant is crucial for efficient data management. Pinot lets you remove unnecessary columns by using the delete function in the schema interface. Retain only pertinent data columns in your dataset structures.

## Transform data with functions

Apache Pinot offers a flexible and powerful mechanism for transforming data at ingestion time using transform functions. This allows users to shape and enrich data before it is indexed, which can simplify queries and improve performance. Modify columns through a variety of transformation functions to manipulate and refine your data. Test transformations to ensure they meet your expectations before applying changes.

### Unnesting Columns

With JSON unnesting, you can flatten nested structures—including arrays and objects—directly during ingestion. This allows each nested element to be transformed into individual rows or columns, making the data significantly easier to query and analyze.

Key Capabilities:

1. Flatten Arrays: Unnest array elements into separate rows, enabling row-level access to each item.
2. Extract Nested Fields: Promote nested JSON fields to top-level columns for direct querying.

For more information, see [JSON Unnesting](unnesting-json).

### Datetime-related examples

#### Timestamp column with epoch format

Create timestamp columns like `created_ts` with the format `EPOCH` and granularity `SECONDS`.

```json  theme={null}
{
    "name": "created_ts",
    "fieldType": "datetime",
    "dataType": "long",
    "format": "EPOCH|SECONDS|1",
    "granularity": "SECONDS|1"
}
```

#### Transforming epoch seconds to epoch milliseconds

Easily convert timestamps from seconds to milliseconds using transformation functions.

```json  theme={null}
{
  "timeTransforms": [
      {
        "inputFieldName": "timestamp",
        "inputFormat": "EPOCH",
        "inputGranularity": "SECONDS",
        "outputFieldName": "created_ts",
        "outputFormat": "EPOCH",
        "outputGranularity": "MILLISECONDS"
      }
}
```

### String transformation example

#### Creating a new string column by concatenation

Combine columns (like `firstName` and `lastName`) into a new column called `name`.

```json  theme={null}
{
  "transforms": [
    {
      "outputFieldName": "name",
      "transformFunction": "concat("firstName", "lastName")"
    }
}
```

## Supported Functions

Pinot supports a rich set of built-in functions for transformations, including:

* Math: ADD(), SUB(), MULT(), DIV()
* String: LOWER(), UPPER(), CONCAT(), REGEXP\_EXTRACT()
* Date/Time: DATETIMECONVERT(), DATE\_TRUNC(), EPOCH()
* Logical: IF(), CASE WHEN, AND, OR, NOT
* Geospatial: ST\_DISTANCE(), GEO\_TO\_H3()

### Further Reading

For a complete and up-to-date guide to Pinot’s transformation functions and configuration please read the official documentation on [Apache Pinot Transform Functions](https://docs.pinot.apache.org/users/user-guide-query/query-syntax/supported-transformations)

Built with [Mintlify](https://mintlify.com).
