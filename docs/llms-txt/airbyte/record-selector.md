# Source: https://docs.airbyte.com/platform/connector-development/config-based/understanding-the-yaml-file/record-selector.md

# Source: https://docs.airbyte.com/platform/2.0/connector-development/config-based/understanding-the-yaml-file/record-selector.md

# Source: https://docs.airbyte.com/platform/1.8/connector-development/config-based/understanding-the-yaml-file/record-selector.md

# Source: https://docs.airbyte.com/platform/1.7/connector-development/config-based/understanding-the-yaml-file/record-selector.md

# Source: https://docs.airbyte.com/platform/1.6/connector-development/config-based/understanding-the-yaml-file/record-selector.md

# Record selector

Copy Page

The record selector is responsible for translating an HTTP response into a list of Airbyte records by extracting records from the response and optionally filtering and shaping records based on a heuristic. Schema:

```
HttpSelector:
  type: object
  anyOf:
    - "$ref": "#/definitions/RecordSelector"
RecordSelector:
  type: object
  required:
    - extractor
  properties:
    "$parameters":
      "$ref": "#/definitions/$parameters"
    extractor:
      "$ref": "#/definitions/RecordExtractor"
    record_filter:
      "$ref": "#/definitions/RecordFilter"
```

The current record extraction implementation uses [dpath](https://pypi.org/project/dpath/) to select records from the json-decoded HTTP response. For nested structures `*` can be used to iterate over array elements. Schema:

```
DpathExtractor:
  type: object
  additionalProperties: true
  required:
    - field_path
  properties:
    "$parameters":
      "$ref": "#/definitions/$parameters"
    field_path:
      type: array
      items:
        type: string
```

## Common recipes:[​](#common-recipes "Direct link to Common recipes:")

Here are some common patterns:

### Selecting the whole response[​](#selecting-the-whole-response "Direct link to Selecting the whole response")

If the root of the response is an array containing the records, the records can be extracted using the following definition:

```
selector:
  extractor:
    field_path: []
```

If the root of the response is a json object representing a single record, the record can be extracted and wrapped in an array. For example, given a response body of the form

```
{
  "id": 1
}
```

and a selector

```
selector:
  extractor:
    field_path: []
```

The selected records will be

```
[
  {
    "id": 1
  }
]
```

### Selecting a field[​](#selecting-a-field "Direct link to Selecting a field")

Given a response body of the form

```
{
  "data": [{"id": 0}, {"id": 1}],
  "metadata": {"api-version": "1.0.0"}
}
```

and a selector

```
selector:
  extractor:
    field_path: ["data"]
```

The selected records will be

```
[
  {
    "id": 0
  },
  {
    "id": 1
  }
]
```

### Selecting an inner field[​](#selecting-an-inner-field "Direct link to Selecting an inner field")

Given a response body of the form

```
{
  "data": {
    "records": [
      {
        "id": 1
      },
      {
        "id": 2
      }
    ]
  }
}
```

and a selector

```
selector:
  extractor:
    field_path: ["data", "records"]
```

The selected records will be

```
[
  {
    "id": 1
  },
  {
    "id": 2
  }
]
```

### Selecting fields nested in arrays[​](#selecting-fields-nested-in-arrays "Direct link to Selecting fields nested in arrays")

Given a response body of the form

```
{
  "data": [
    {
      "record": {
        "id": "1"
      }
    },
    {
      "record": {
        "id": "2"
      }
    }
  ]
}
```

and a selector

```
selector:
  extractor:
    field_path: ["data", "*", "record"]
```

The selected records will be

```
[
  {
    "id": 1
  },
  {
    "id": 2
  }
]
```

## Filtering records[​](#filtering-records "Direct link to Filtering records")

Records can be filtered by adding a record\_filter to the selector. The expression in the filter will be evaluated to a boolean returning true if the record should be included.

In this example, all records with a `created_at` field greater than the stream slice's `start_time` will be filtered out:

```
selector:
  extractor:
    field_path: []
  record_filter:
    condition: "{{ record['created_at'] < stream_slice['start_time'] }}"
```

## Transformations[​](#transformations "Direct link to Transformations")

Fields can be added or removed from records by adding `Transformation`s to a stream's definition.

Schema:

```
RecordTransformation:
  type: object
  anyOf:
    - "$ref": "#/definitions/AddFields"
    - "$ref": "#/definitions/RemoveFields"
```

### Adding fields[​](#adding-fields "Direct link to Adding fields")

Fields can be added with the `AddFields` transformation. This example adds a top-level field "field1" with a value "static\_value"

Schema:

```
AddFields:
  type: object
  required:
    - fields
  additionalProperties: true
  properties:
    "$parameters":
      "$ref": "#/definitions/$parameters"
    fields:
      type: array
      items:
        "$ref": "#/definitions/AddedFieldDefinition"
AddedFieldDefinition:
  type: object
  required:
    - path
    - value
  additionalProperties: true
  properties:
    "$parameters":
      "$ref": "#/definitions/$parameters"
    path:
      "$ref": "#/definitions/FieldPointer"
    value:
      type: string
FieldPointer:
  type: array
  items:
    type: string
```

Example:

```
stream:
  <...>
  transformations:
      - type: AddFields
        fields:
          - path: [ "field1" ]
            value: "static_value"
```

This example adds a top-level field "start\_date", whose value is evaluated from the stream slice:

```
stream:
  <...>
  transformations:
      - type: AddFields
        fields:
          - path: [ "start_date" ]
            value: { { stream_slice[ 'start_date' ] } }
```

Fields can also be added in a nested object by writing the fields' path as a list.

Given a record of the following shape:

```
{
  "id": 0,
  "data":
  {
    "field0": "some_data"
  }
}
```

this definition will add a field in the "data" nested object:

```
stream:
  <...>
  transformations:
      - type: AddFields
        fields:
          - path: [ "data", "field1" ]
            value: "static_value"
```

resulting in the following record:

```
{
  "id": 0,
  "data":
  {
    "field0": "some_data",
    "field1": "static_value"
  }
}
```

### Removing fields[​](#removing-fields "Direct link to Removing fields")

Fields can be removed from records with the `RemoveFields` transformation.

Schema:

```
RemoveFields:
  type: object
  required:
    - field_pointers
  additionalProperties: true
  properties:
    "$parameters":
      "$ref": "#/definitions/$parameters"
    field_pointers:
      type: array
      items:
        "$ref": "#/definitions/FieldPointer"
```

Given a record of the following shape:

```
{
  "path":
  {
    "to":
    {
      "field1": "data_to_remove",
      "field2": "data_to_keep"
    }
  },
  "path2": "data_to_remove",
  "path3": "data_to_keep"
}
```

this definition will remove the 2 instances of "data\_to\_remove" which are found in "path2" and "path.to.field1":

```
the_stream:
  <...>
  transformations:
      - type: RemoveFields
        field_pointers:
          - [ "path", "to", "field1" ]
          - [ "path2" ]
```

resulting in the following record:

```
{
  "path":
  {
    "to":
    {
      "field2": "data_to_keep"
    }
  },
  "path3": "data_to_keep"
}
```
