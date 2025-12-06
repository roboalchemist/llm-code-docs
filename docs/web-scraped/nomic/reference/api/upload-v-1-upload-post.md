# Get URLs to upload files

Source: https://docs.nomic.ai/reference/api/upload-v-1-upload-post

# Get URLs to upload files

```
POST /v1/upload
```

## /v1/upload

Get URLs to upload files and use in different tasks (parsing, extraction, etc.).

## Request​

- application/json
### Body

Body

required

files

object[]

required

List of files to prepare for upload.
Each file must have a unique ID, size in bytes, and content type.

- Array [
Array [

Unique identifier for the file in your request.
Use this to match the response with your original file.

Possible values: >= 1

```
>= 1
```

File size in bytes. Must be at least 1 byte.

MIME type of the file (e.g., "application/pdf")

- ]
]

## Responses​

- 201
- 403
- 422
The URLs to upload the files to.

- application/json
- Schema
- Example (from schema)
Schema

files

object[]

required

List of upload information for each file in your request.
Each file gets its own upload URL and task (parsing, extraction, etc.) id.

- Array [
Array [

The ID you provided in your request.
Use this to match the response with your original file.

URL for uploading your file.
Use this URL with a PUT request to upload your file content.

Use this URL to reference the file when making calls to parsing or extraction services.

- ]
]

```
{  "files": [    {      "request_id": "string",      "upload_url": "string",      "nomic_url": "string"    }  ]}
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

