# Source: https://flatfile.com/docs/plugins/json-extractor.md

# JSON Extractor

> Parse JSON and JSON Lines files uploaded to Flatfile and extract data into Sheets within a Workbook

The JSON Extractor plugin is designed to parse JSON (`.json`) and JSON Lines (`.jsonl`, `.jsonlines`) files uploaded to Flatfile. It automatically detects the file type and extracts the data into one or more Sheets within a Flatfile Workbook.

The primary use case is to allow users to upload structured JSON data and have it seamlessly transformed into a tabular format for review and import. The plugin can handle two main JSON structures:

1. A JSON object where each top-level key is a sheet name and its value is an array of objects (records). This creates a multi-sheet Workbook.
2. A single JSON array of objects. This creates a single-sheet Workbook with the default sheet name "Sheet1".

The plugin also intelligently handles nested JSON objects by flattening them into a single-level structure, using dot notation for headers (e.g., an object `{ "address": { "city": "..." } }` becomes a column named `Address.City`). This plugin is intended to be used in a server-side listener.

## Installation

Install the JSON Extractor plugin using npm:

```bash
npm install @flatfile/plugin-json-extractor
```

## Configuration & Parameters

The `JSONExtractor` function accepts an optional options object with the following properties:

| Parameter   | Type      | Default | Description                                                                                                                                        |
| ----------- | --------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `chunkSize` | `number`  | `10000` | Controls the number of records to process in each batch or "chunk" when inserting data into Flatfile                                               |
| `parallel`  | `number`  | `1`     | Controls how many chunks are processed concurrently. Increasing this can speed up the import of very large files but may use more server resources |
| `debug`     | `boolean` | `false` | If set to true, enables more verbose logging for debugging purposes                                                                                |

### Default Behavior

If no options are provided, the plugin processes files by inserting data in chunks of 10,000 records, with only one chunk being processed at a time. Debug logging is disabled.

## Usage Examples

### Basic Usage

This example shows how to add the JSON extractor to a Flatfile listener with its default settings.

<CodeGroup>
  ```javascript JavaScript
  import { listener } from '@flatfile/listener';
  import { JSONExtractor } from '@flatfile/plugin-json-extractor';

  listener.use(JSONExtractor());
  ```

  ```typescript TypeScript
  import { listener } from '@flatfile/listener';
  import { JSONExtractor } from '@flatfile/plugin-json-extractor';

  listener.use(JSONExtractor());
  ```
</CodeGroup>

### Configuration Example

This example configures the extractor to use a smaller chunk size and process two chunks in parallel.

<CodeGroup>
  ```javascript JavaScript
  import { listener } from '@flatfile/listener';
  import { JSONExtractor } from '@flatfile/plugin-json-extractor';

  listener.use(
    JSONExtractor({
      chunkSize: 5000,
      parallel: 2,
    })
  );
  ```

  ```typescript TypeScript
  import { listener } from '@flatfile/listener';
  import { JSONExtractor } from '@flatfile/plugin-json-extractor';

  listener.use(
    JSONExtractor({
      chunkSize: 5000,
      parallel: 2,
    })
  );
  ```
</CodeGroup>

### Advanced Usage (Standalone Parser)

This example shows how to use the exported `jsonParser` function directly to parse a JSON file buffer outside of the Flatfile listener context.

<CodeGroup>
  ```javascript JavaScript
  import * as fs from 'fs';
  import { jsonParser } from '@flatfile/plugin-json-extractor';

  const fileBuffer = fs.readFileSync('path/to/my-data.json');
  const workbookData = jsonParser(fileBuffer);

  console.log(workbookData);
  // Output: { Sheet1: { headers: [...], data: [...] } }
  ```

  ```typescript TypeScript
  import * as fs from 'fs';
  import { jsonParser } from '@flatfile/plugin-json-extractor';

  const fileBuffer = fs.readFileSync('path/to/my-data.json');
  const workbookData = jsonParser(fileBuffer);

  console.log(workbookData);
  // Output: { Sheet1: { headers: [...], data: [...] } }
  ```
</CodeGroup>

## API Reference

### JSONExtractor

This is the main factory function for the plugin. It returns a configured extractor instance that can be registered with a Flatfile listener. The extractor listens for `.json`, `.jsonl`, and `.jsonlines` file uploads, parses them, and creates the corresponding Sheets and Records in Flatfile.

**Parameters:**

* `options` (optional): `PluginOptions`
  * `chunkSize` (number): Records per chunk. Default: 10000
  * `parallel` (number): Number of chunks to process in parallel. Default: 1
  * `debug` (boolean): Enable verbose logging. Default: false

**Return Value:**
Returns a Flatfile `Extractor` instance, which is a type of listener middleware.

**Usage Example:**

<CodeGroup>
  ```javascript JavaScript
  import { listener } from '@flatfile/listener';
  import { JSONExtractor } from '@flatfile/plugin-json-extractor';

  // Register the plugin with default options
  listener.use(JSONExtractor());

  // Or with custom options
  listener.use(JSONExtractor({ chunkSize: 1000, parallel: 5 }));
  ```

  ```typescript TypeScript
  import { listener } from '@flatfile/listener';
  import { JSONExtractor } from '@flatfile/plugin-json-extractor';

  // Register the plugin with default options
  listener.use(JSONExtractor());

  // Or with custom options
  listener.use(JSONExtractor({ chunkSize: 1000, parallel: 5 }));
  ```
</CodeGroup>

**Error Handling:**
The extractor is built on the `@flatfile/util-extractor` utility, which automatically handles job lifecycle events. If the parser throws an error (e.g., due to malformed JSON), the utility will catch it and fail the corresponding job in Flatfile, providing feedback to the user in the UI.

### jsonParser

A standalone function that performs the core logic of parsing a file buffer into a `WorkbookCapture` object. This is useful for testing or for use cases where parsing is needed without the full listener integration. It handles both standard JSON and JSONL formats.

**Parameters:**

* `buffer`: `Buffer` - A Node.js Buffer containing the raw file content
* `options` (optional): `{ readonly fileExt?: string }`
  * `fileExt` (string): Can be set to 'jsonl' to explicitly trigger JSON Lines parsing logic, even if the file name is not available

**Return Value:**
Returns a `WorkbookCapture` object, which has sheet names as keys and `SheetCapture` objects as values.
Example: `{ "MySheet": { headers: ["id", "name"], data: [{ id: {value: 1}, name: {value: "Test"} }] } }`

**Usage Example:**

<CodeGroup>
  ```javascript JavaScript
  import * as fs from 'fs';
  import { jsonParser } from '@flatfile/plugin-json-extractor';

  // For a standard JSON array file
  const jsonBuffer = Buffer.from('[{"id": 1, "name": "Alice"}]');
  const workbook = jsonParser(jsonBuffer);
  // workbook -> { Sheet1: { headers: ['id', 'name'], data: [...] } }

  // For a JSONL file
  const jsonlBuffer = Buffer.from('{"id": 1}\n{"id": 2}');
  const workbookL = jsonParser(jsonlBuffer, { fileExt: 'jsonl' });
  // workbookL -> { Sheet1: { headers: ['id'], data: [...] } }
  ```

  ```typescript TypeScript
  import * as fs from 'fs';
  import { jsonParser } from '@flatfile/plugin-json-extractor';

  // For a standard JSON array file
  const jsonBuffer = Buffer.from('[{"id": 1, "name": "Alice"}]');
  const workbook = jsonParser(jsonBuffer);
  // workbook -> { Sheet1: { headers: ['id', 'name'], data: [...] } }

  // For a JSONL file
  const jsonlBuffer = Buffer.from('{"id": 1}\n{"id": 2}');
  const workbookL = jsonParser(jsonlBuffer, { fileExt: 'jsonl' });
  // workbookL -> { Sheet1: { headers: ['id'], data: [...] } }
  ```
</CodeGroup>

**Error Handling:**

* If the buffer contains fundamentally invalid JSON, the function will throw a `SyntaxError`
* For JSONL files, it will skip any individual lines that are not valid JSON, log an error to the console for each invalid line, and continue processing the rest of the file
* If the input data is not an object or array (e.g., a simple string or number), it will log an error and return an empty object

## Troubleshooting

* **File not being processed**: Ensure it has a `.json` or `.jsonl` extension and that the listener is correctly configured with `listener.use(JSONExtractor())`
* **Data appears in wrong sheet or not at all**: Check the root structure of your JSON file. It must be either an array of objects or an object of arrays
* **Some rows from JSONL file are missing**: Check the server logs for "Invalid JSON line" errors to identify and correct malformed lines in the source file

## Notes

### Special Considerations

* **Deployment**: This plugin is designed to run in a server-side environment as part of a Flatfile listener
* **Supported File Types**: The plugin automatically triggers for files with extensions `.json`, `.jsonl`, and `.jsonlines`
* **Data Structure for Multi-Sheet Extraction**: To create multiple sheets from a single file, the root of the JSON must be an object where each key is a string (the sheet name) and each value is an array of uniform objects
* **Data Structure for Single-Sheet Extraction**: If the root of the JSON is an array of objects, the plugin will create a single sheet named "Sheet1"
* **Nested Objects**: Nested objects are flattened into columns using dot notation. For example, `{ "user": { "name": "John" } }` will result in a column named `user.name`

### Error Handling Patterns

* The core `parseBuffer` function is wrapped in a try/catch block. On a fatal parsing error (like malformed JSON), it re-throws the error, which is then handled by the extractor utility to fail the job
* For JSONL files, the parser processes the file line-by-line. If a line contains invalid JSON, it is skipped, an error is logged to the console, and processing continues with the next valid line. This makes it resilient to partially corrupted JSONL files
