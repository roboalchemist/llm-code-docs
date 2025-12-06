# Parse files into structured information

Source: https://docs.nomic.ai/reference/api/parse-v-1-parse-post

# Parse files into structured information

```
POST /v1/parse
```

## /v1/parse

Parse a file into structured information.

Supports PDF files with configurable chunking strategies and optional embedding generation.

## Request​

- application/json
### Body

Body

required

File URL to process. Supports two URL types:

```
1. Public URLs - accessible from the internet    2. `nomic://` prefixed URLs - obtained from the `/upload` endpoint
```

options

object

Options to customize document parsing.

chunking

object

Options that control how the document is split into chunks.

Possible values: [page]

```
page
```

Default value: page

```
page
```

The method by which the document is split into chunks.

Possible values: [standard]

```
standard
```

Default value: standard

```
standard
```

The OCR method used to extract text from the document.

Possible values: [metadata, hybrid, ocr]

```
metadata
```

```
hybrid
```

```
ocr
```

Default value: hybrid

```
hybrid
```

The overall strategy for extracting content from the document.
metadata: Disable all OCR. Only use embedded document text.
hybrid: Use a VLM for tables, and run an OCR model on all bitmaps found in the document.
ocr: Use a VLM for tables. Run an OCR model on full pages.

table_summary

object

Options for generating table summaries.

Whether to generate a summary of table content.

figure_summary

object

Options for generating figure summaries.

Default value: true

```
true
```

Whether to generate a summary of figure content.

## Responses​

- 201
- 403
- 422
The task id of the parsing task.

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

