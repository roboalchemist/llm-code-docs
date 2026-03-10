# Source: https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue.md.txt

An array value.

| JSON representation |
|---|
| ``` { "values": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) } ] } ``` |

| Fields ||
|---|---|
| `values[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`)`` Values in the array. |

## Value

A message that can hold any of the supported value types.

| JSON representation |
|---|
| ``` { // Union field `value_type` can be only one of the following: "nullValue": null, "booleanValue": boolean, "integerValue": string, "doubleValue": number, "timestampValue": string, "stringValue": string, "bytesValue": string, "referenceValue": string, "geoPointValue": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/LatLng`) }, "arrayValue": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue`) }, "mapValue": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#MapValue`) }, "fieldReferenceValue": string, "variableReferenceValue": string, "functionValue": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Function`) }, "pipelineValue": { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Pipeline`) } // End of list of possible types for union field `value_type`. } ``` |

| Fields ||
|---|---|
| Union field `value_type`. Must have a value set. `value_type` can be only one of the following: ||
| `nullValue` | `null` A null value. |
| `booleanValue` | `boolean` A boolean value. |
| `integerValue` | `string (https://developers.google.com/discovery/v1/type-format format)` An integer value. |
| `doubleValue` | `number` A double value. |
| `timestampValue` | ``string (`https://protobuf.dev/reference/protobuf/google.protobuf#timestamp` format)`` A timestamp value. Precise only to microseconds. When stored, any additional precision is rounded down. Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. |
| `stringValue` | `string` A string value. The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries. |
| `bytesValue` | `string (https://developers.google.com/discovery/v1/type-format format)` A bytes value. Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries. A base64-encoded string. |
| `referenceValue` | `string` A reference to a document. For example: `projects/{projectId}/databases/{databaseId}/documents/{document_path}`. |
| `geoPointValue` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/LatLng`)`` A geo point value representing a point on the surface of Earth. |
| `arrayValue` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue`)`` An array value. Cannot directly contain another array value, though can contain a map which contains another array. |
| `mapValue` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#MapValue`)`` A map value. |
| `fieldReferenceValue` | `string` Value which references a field. This is considered relative (vs absolute) since it only refers to a field and not a field within a particular document. **Requires:** - Must follow \[field reference\]\[FieldReference.field_path\] limitations. - Not allowed to be used when writing documents. |
| `variableReferenceValue` | `string` Pointer to a variable defined elsewhere in a pipeline. Unlike `fieldReferenceValue` which references a field within a document, this refers to a variable, defined in a separate namespace than the fields of a document. |
| `functionValue` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Function`)`` A value that represents an unevaluated expression. **Requires:** - Not allowed to be used when writing documents. |
| `pipelineValue` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Pipeline`)`` A value that represents an unevaluated pipeline. **Requires:** - Not allowed to be used when writing documents. |

## MapValue

A map value.

| JSON representation |
|---|
| ``` { "fields": { string: { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) }, ... } } ``` |

| Fields ||
|---|---|
| `fields` | ``map (key: string, value: object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`))`` The map's fields. The map keys represent field names. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |

## Function

Represents an unevaluated scalar expression.

For example, the expression `like(user_name, "%alice%")` is represented as:

    name: "like"
    args { fieldReference: "user_name" }
    args { stringValue: "%alice%" }

| JSON representation |
|---|
| ``` { "name": string, "args": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) } ], "options": { string: { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) }, ... } } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The name of the function to evaluate. **Requires:** - must be in snake case (lower case with underscore separator). |
| `args[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`)`` Optional. Ordered list of arguments the given function expects. |
| `options` | ``map (key: string, value: object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`))`` Optional. Optional named arguments that certain functions may support. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |

## Pipeline

A Firestore query represented as an ordered list of operations / stages.

| JSON representation |
|---|
| ``` { "stages": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Stage`) } ] } ``` |

| Fields ||
|---|---|
| `stages[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Stage`)`` Required. Ordered list of stages to evaluate. |

## Stage

A single operation within a pipeline.

A stage is made up of a unique name, and a list of arguments. The exact number of arguments \& types is dependent on the stage type.

To give an example, the stage `filter(state = "MD")` would be encoded as:

    name: "filter"
    args {
      functionValue {
        name: "eq"
        args { fieldReferenceValue: "state" }
        args { stringValue: "MD" }
      }
    }

See public documentation for the full list.

| JSON representation |
|---|
| ``` { "name": string, "args": [ { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) } ], "options": { string: { object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`) }, ... } } ``` |

| Fields ||
|---|---|
| `name` | `string` Required. The name of the stage to evaluate. **Requires:** - must be in snake case (lower case with underscore separator). |
| `args[]` | ``object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`)`` Optional. Ordered list of arguments the given stage expects. |
| `options` | ``map (key: string, value: object (`https://firebase.google.com/docs/firestore/reference/rest/Shared.Types/ArrayValue#Value`))`` Optional. Optional named arguments that certain functions may support. An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`. |