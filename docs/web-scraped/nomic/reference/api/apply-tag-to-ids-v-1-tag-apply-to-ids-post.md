# Tag By ID

Source: https://docs.nomic.ai/reference/api/apply-tag-to-ids-v-1-tag-apply-to-ids-post

# Tag By ID

```
POST /v1/query/update/tag/ids
```

## /v1/query/update/tag/ids

Applies or removes a tag to a specified list of data point IDs within a projection. If the tag does not exist, it will be created.

## Request​

- application/json
### Body

Body

required

The UUID of the projection (map).

The name of the tag to apply or remove.

The field containing the unique IDs. Defaults to the dataset's unique_id_field if not provided.

An array of data point IDs to tag or untag.

Possible values: [add, remove]

```
add
```

```
remove
```

Default value: add

```
add
```

The operation to perform.

## Responses​

- 200
- 422
Successful Response

- application/json
- Schema
- Example (from schema)
Schema

Indicates if the operation was successful.

The UUID of the tag involved in the operation.

The number of points successfully tagged or untagged.

```
{  "success": true,  "tag_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",  "points_tagged": 0}
```

Validation Error

- application/json
- Schema
- Example (from schema)
Schema

detail

object[]

- Array [
Array [

loc

object[]

required

- Array [
Array [

anyOf

- MOD1
- MOD2
string

integer

- ]
]

- ]
]

```
{  "detail": [    {      "loc": [        "string",        0      ],      "msg": "string",      "type": "string"    }  ]}
```

