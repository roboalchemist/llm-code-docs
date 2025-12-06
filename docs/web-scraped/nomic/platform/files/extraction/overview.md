# Nomic Documentation

Source: https://docs.nomic.ai/platform/files/extraction/overview/

Extract turns unstructured documents (PDFs, scans, images, HTML) into predictable, structured JSON. You provide a JSON Schema describing the output you want, and the API extracts those fields from your document into that shape.

At a high level:

- You upload a file or pass a URL.
- You define a JSON Schema for the output.
- The API parses your document and extracts values according to your schema, returning structured JSON.
## How it works​

- Input: a document (URL or uploaded file).
- Schema: a JSON Schema describing the fields, types, and structure you expect in the output.
- Extraction: the service reads the parsed content of your document and fills the schema, returning structured JSON.
Extraction does not invent data. If a value does not exist in the document (or in the parsed content), it will be empty or omitted unless you have marked it as required.

## Design your schema​

Schemas follow standard JSON Schema. Tips for reliable extractions:

- Use clear field names and helpful description text that mirrors how the value appears in the document.
```
description
```

- Set type for every field (string, number, boolean, object, array).
```
type
```

```
string
```

```
number
```

```
boolean
```

```
object
```

```
array
```

- Use required for must-have fields so missing data is surfaced.
```
required
```

- Use enum to constrain values when there are limited options.
```
enum
```

- Keep nesting shallow (ideally ≤ 2–3 levels).
- Use array for long lists or line items.
```
array
```

Example schema with an array of accounts:

```
{  "type": "object",  "properties": {    "customerName": {      "type": "string",      "description": "Full name of the customer as shown on the statement."    },    "accounts": {      "type": "array",      "description": "List of the customer's financial accounts.",      "items": {        "type": "object",        "properties": {          "accountType": {            "type": "string",            "description": "Type of account.",            "enum": ["checking", "savings", "investment", "other"]          },          "accountNumber": {            "type": "string",            "description": "Account identifier as printed on the document."          },          "endingValue": {            "type": "number",            "description": "Closing balance or value of the account."          }        },        "required": ["accountType", "accountNumber", "endingValue"]      }    }  },  "required": ["customerName", "accounts"]}
```

## Quickstart​

Define your schema and run an extraction. Below is a minimal example similar to the current sample:

```
from nomic import NomicClientclient = NomicClient()# Define a schemaschema = {    "type": "object",    "properties": {        "title": {"type": "string", "description": "The title of the document"},        "university": {"type": "string", "description": "The university of the original document. Look for the name in references, URLs, etc."},        "translator": {"type": "string", "description": "The translator of the document"},        "old god": {"type": "string", "description": "The name of the famous Egyptian old god"}    },    "required": ["title"]}# Extract using a URLurl = "https://assets.nomicatlas.com/Phaedrus.pdf"result = client.extract(url, schema)# Or extract using an uploaded filefile = client.upload_file("sample.pdf")result = client.extract(file, schema)
```

To print the result:

```
import jsonimport sysprint("Extracted result:")json.dump(result["result"], sys.stdout, indent=4)
```

### Non-blocking usage​

As with parse, you can pass block=False to receive a task handle immediately instead of waiting for completion.

```
block=False
```

## Example result​

```
{  "data": {    "title": "Phaedrus",    "old god": "Theuth",    "translator": "Benjamin Jowett",    "university": "MIT"  },  "_metadata": {    "processing_status": "completed",    "fields_extracted": 4,    "schema_used": {      "type": "object",      "required": [        "title"      ],      "properties": {        "title": {          "type": "string",          "description": "The title of the document"        },        "old god": {          "type": "string",          "description": "The name of the famous Egyptian old god"        },        "translator": {          "type": "string",          "description": "The translator of the document"        },        "university": {          "type": "string",          "description": "The university of the original document"        }      }    }  }}
```

## Troubleshooting basics​

- Missing values: Confirm the value appears in the document. Strengthen field description text and keep schema shallow.
```
description
```

- Long lists: Use an array type at the appropriate level for tables or line items.
```
array
```

- Consistency: Use enum where fields have limited options; add required for must-have fields.
```
enum
```

```
required
```

## What’s next​

After extraction, you can:

- Feed results to downstream systems or databases
- Build search indexes
- Enrich with other pipelines as needed
- How it works
- Design your schema
- QuickstartNon-blocking usage
- Non-blocking usage
- Example result
- Troubleshooting basics
- What’s next
