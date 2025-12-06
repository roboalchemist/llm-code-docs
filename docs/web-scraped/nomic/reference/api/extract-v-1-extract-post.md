# Get specific data from your files using a template

Source: https://docs.nomic.ai/reference/api/extract-v-1-extract-post

# Get specific data from your files using a template

```
POST /v1/extract
```

## /v1/extract

Extract specific information from your files (like names, dates, amounts) by providing a template (JSON schema) of what you want to find.

## Request​

- application/json
### Body

Body

required

List of file URLs to process for extraction. Supports two URL types:

```
1. Public URLs - accessible from the internet    2. `nomic://` prefixed URLs - obtained from the `/upload` endpoint
```

extraction_schema

object

required

JSON schema defining the structure and data types for the extracted information.
This schema guides the AI model to extract specific fields and maintain consistent output format.

JSON schema defining the structure and data types for the extracted information.
This schema guides the AI model to extract specific fields and maintain consistent output format.

system_prompt

object

Custom system prompt to guide the AI extraction process across the entire file.
Use this to provide specific instructions, context, or constraints for how information
should be extracted and formatted according to your requirements.

anyOf

- MOD1
string

## Responses​

- 201
- 403
- 422
The task id of the extraction task.

- application/json
- Schema
- Example (from schema)
Schema

The id of the task.

```
{  "task_id": "string"}
```

The user is not authorized to perform this action.

- application/json
- Schema
- Example (from schema)
- Example
Schema

any

```
{  "status_code": 403,  "detail": "The user is not authorized to perform this action."}
```

```
{  "status_code": 403,  "detail": "The user is not authorized to perform this action."}
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

