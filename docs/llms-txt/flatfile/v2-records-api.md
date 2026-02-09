# Source: https://flatfile.com/docs/reference/v2-records-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# V2 Records API

> Using the V2 Records API with the Flatfile TypeScript API package

The V2 Records API provides an interface for reading and writing records from Flatfile sheets.
It is optimized for performance when working with large numbers of records.

<Note>Support for the V2 Records API was added to the `@flatfile/api` package in version 1.18.0.</Note>

## Overview

The V2 Records API is accessible through the `records.v2` property on the Flatfile client.

```typescript  theme={null}
import { FlatfileClient } from "@flatfile/api";
const client = new FlatfileClient({ token: "YOUR_TOKEN" });
await client.records.v2.get("us_sh_1234abcd")
```

The V2 API uses a specialized JSON Lines (JSONL) format that is optimized for performance and
usage with streaming requests.

## Reading Records

### getRaw()

Retrieve records from a sheet in raw JSONL format.

```typescript  theme={null}
getRaw(
  sheetId: Flatfile.SheetId,
  options?: GetRecordsRequestOptions,
  requestOptions?: RequestOptions
): Promise<JsonlRecord[]>
```

Returns an array of `JsonlRecord` objects containing the raw data structure from the API including special fields like `__k` (record ID), `__v` (version), etc.

**Example:**

```typescript  theme={null}
const rawRecords = await api.records.v2.getRaw('us_sh_123', {
  fields: ['firstName', 'lastName'],
  pageSize: 1000
});

rawRecords.forEach(record => {
  console.log(`Record ID: ${record.__k}`);
  console.log(`Field values:`, record);
});
```

### getRawStreaming()

Stream records from a sheet in raw JSONL format.

```typescript  theme={null}
getRawStreaming(
  sheetId: Flatfile.SheetId,
  options?: GetRecordsRequestOptions,
  requestOptions?: RequestOptions
): AsyncGenerator<JsonlRecord>
```

The most memory-efficient way to process large datasets as records are yielded individually.

**Example:**

```typescript  theme={null}
for await (const rawRecord of api.records.v2.getRawStreaming('us_sh_123', {
  includeTimestamps: true
})) {
  console.log(`Record ID: ${rawRecord.__k}`);
  console.log(`Updated at: ${rawRecord.__u}`);
  // Process each record as it streams in
}
```

## Writing Records

### writeRaw()

Write records to a sheet in raw JSONL format.

```typescript  theme={null}
writeRaw(
  records: JsonlRecord[],
  options?: WriteRecordsRequestOptions,
  requestOptions?: RequestOptions
): Promise<WriteRecordsResponse>
```

**Parameters:**

* `records` - Array of JsonlRecord objects to write
* `options` - Write configuration options
* `requestOptions` - Optional request configuration

**Example:**

```typescript  theme={null}
const records: JsonlRecord[] = [
  { firstName: 'John', lastName: 'Doe', __s: 'us_sh_123' },
  { __k: 'us_rc_456', firstName: 'Jane', lastName: 'Smith' }  // Update existing
];

const result = await api.records.v2.writeRaw(records, {
  sheetId: 'us_sh_123',
  truncate: false
});

console.log(`Created: ${result.created}, Updated: ${result.updated}`);
```

### writeRawStreaming()

Stream records to a sheet in raw JSONL format.

```typescript  theme={null}
writeRawStreaming(
  recordsStream: AsyncIterable<JsonlRecord>,
  options?: WriteStreamingOptions,
  requestOptions?: RequestOptions
): Promise<WriteRecordsResponse>
```

Efficiently write large datasets by streaming records to the server.

**Example:**

```typescript  theme={null}
async function* generateRecords() {
  for (let i = 0; i < 100000; i++) {
    yield {
      firstName: `User${i}`,
      email: `user${i}@example.com`,
      __s: 'us_sh_123'
    };
  }
}

const result = await api.records.v2.writeRawStreaming(generateRecords(), {
  sheetId: 'us_sh_123',
  chunkSize: 1000,
  useBodyStreaming: 'auto'
});
```

## JSONL Record Format Reference

The V2 Records API uses JSONL (JSON Lines) format for raw record operations. JSONL is a text format where each line is a valid JSON object representing a single record.

### Special Fields

Flatfile uses special fields prefixed with `__` (double underscore) to store metadata and system information:

| Field  | Description                   | Example                                                       |
| ------ | ----------------------------- | ------------------------------------------------------------- |
| `__k`  | Record ID (unique identifier) | `"us_rc_123456"`                                              |
| `__nk` | New record ID (for creation)  | `"temp_123"`                                                  |
| `__v`  | Record version ID             | `"v_789"`                                                     |
| `__s`  | Sheet ID                      | `"us_sh_123"`                                                 |
| `__n`  | Sheet slug                    | `"contacts"`                                                  |
| `__c`  | Record configuration          | `{"locked": true}`                                            |
| `__m`  | Record metadata               | `{"source": "import"}`                                        |
| `__i`  | Validation messages           | `{"email": [{"type": "error", "message": "Invalid format"}]}` |
| `__d`  | Deleted flag                  | `true`                                                        |
| `__e`  | Valid flag                    | `false`                                                       |
| `__l`  | Linked records                | `[{...}]`                                                     |
| `__u`  | Updated timestamp             | `"2023-11-20T16:59:40.286Z"`                                  |

Note that many special fields will not be included unless the corresponding query parameter is included,
such as `includeMessages` to include the `__i` field with validation messages.

### Field Values

Regular field values are stored directly as properties on the JSONL record:

```json  theme={null}
{
  "__k": "us_rc_123456",
  "__s": "us_sh_123",
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "age": 30,
  "isActive": true
}
```

### Validation Messages

If included, the `__i` field contains validation messages for fields that have errors or warnings.
The messages are structured as an array of objects. Each validation message object will be structured
as `{"x": <field key of message>, "m": <validation message>}`.

```json  theme={null}
{
  "__k": "us_rc_123456",
  "__s": "us_sh_123",
  "email": "invalid-email",
  "__i": [
    {"x": "firstName", "m": "First name is required"},
    {"x": "email", "m": "Not a valid email address"}
  ]
}
```

### Complete Example

A complete JSONL record with all common fields:

```json  theme={null}
{
  "__k": "us_rc_123456",
  "__v": "v_789",
  "__s": "us_sh_123",
  "__n": "contacts",
  "__c": {
    "locked": false,
    "priority": "high"
  },
  "__m": {
    "source": "api_import",
    "batch_id": "batch_001"
  },
  "__i": [
    {"x": "firstName", "m": "First name is required"},
    {"x": "email", "m": "Not a valid email address"}
  ],
  "__e": true,
  "__u": "2023-11-20T16:59:40.286Z",
  "firstName": "John",
  "lastName": "Doe",
  "email": "john.doe@example.com",
  "company": "Acme Corp",
  "phone": "+1-555-123-4567"
}
```

### Record Operations

The V2 write records endpoint can be used to create, update, or delete records into a sheet
all in a single request. The operation performed depends on which special keys are provided.

#### Create New Record

To create a new record, the record can simply be passed with a sheet ID in `__s` and no record ID.

```json  theme={null}
{
  "__s": "us_sh_123",
  "firstName": "New",
  "lastName": "User"
}
```

#### Update Existing Record

To update an existing record, provide the record ID in the `__k` field.

```json  theme={null}
{
  "__k": "us_rc_123456",
  "__s": "us_sh_123",
  "firstName": "Updated",
  "lastName": "Name"
}
```

#### Delete Record

To delete a record, provide the record ID in the `__k` field and pass the delete flag
in the `__d` field.

```json  theme={null}
{
  "__k": "us_rc_123456",
  "__s": "us_sh_123",
  "__d": true
}
```
