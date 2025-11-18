# Source: https://flatfile.com/docs/plugins/delimiter-extractor.md

# Delimiter Extractor Plugin

> Parse text files with custom delimiters and automatically extract structured data for import into Flatfile

The Delimiter Extractor plugin is designed to parse text files that use non-standard delimiters to separate values. Its primary purpose is to automatically detect and extract structured data from these files when they are uploaded to Flatfile. It supports a variety of single-character delimiters such as `;`, `:`, `~`, `^`, and `#`.

This plugin is useful in scenarios where data is provided in custom formats that are not natively handled by the Flatfile platform's standard CSV, TSV, or PSV parsers. It operates within a server-side listener, triggering on the `file:created` event to process the file, identify headers, and structure the data into records for import.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-delimiter-extractor
```

## Configuration & Parameters

### Required Parameters

<ParamField path="fileExt" type="string" required>
  The file extension (e.g., ".txt", ".dat") that the plugin should listen for. This is the first argument to the `DelimiterExtractor` function.
</ParamField>

<ParamField path="options.delimiter" type="string" required>
  The character used to separate values in the file. Supported delimiters are `;`, `:`, `~`, `^`, `#`.
</ParamField>

### Optional Parameters

<ParamField path="options.dynamicTyping" type="boolean" default="false">
  If set to `true`, the plugin will attempt to convert numeric and boolean strings into their corresponding types. For example, "123" becomes `123` and "true" becomes `true`.
</ParamField>

<ParamField path="options.skipEmptyLines" type="boolean | 'greedy'" default="false">
  Controls how empty lines in the file are handled:

  * `true`: Skips lines that are completely empty
  * `'greedy'`: Skips lines that contain only whitespace characters
  * `false`: Includes all lines, even empty ones
</ParamField>

<ParamField path="options.transform" type="function" default="identity function">
  A function that is applied to each individual cell value during parsing. The return value of the function will replace the original value. This is applied before `dynamicTyping`.
</ParamField>

<ParamField path="options.chunkSize" type="number" default="10000">
  The number of records to process in each batch or chunk when inserting data into Flatfile.
</ParamField>

<ParamField path="options.parallel" type="number" default="1">
  The number of chunks to process concurrently.
</ParamField>

<ParamField path="options.headerDetectionOptions" type="object">
  An advanced configuration object to control the header detection strategy. Allows for specifying explicit headers, looking for headers in specific rows, or using different detection algorithms. Default uses the 'default' algorithm, which selects the row with the most non-empty cells within the first 10 rows as the header.
</ParamField>

<ParamField path="options.guessDelimiters" type="string[]" default="[',', '|', '\t', ';', ':', '~', '^', '#']">
  An array of delimiter characters to try if a specific `delimiter` is not provided. The parser will use the first one that successfully parses the data.
</ParamField>

<ParamField path="options.debug" type="boolean" default="false">
  Enables debug logging.
</ParamField>

## Usage Examples

### Basic Usage

Configure the listener to use the plugin for any `.txt` file, specifying that the data is separated by a colon:

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/platform";
  import { DelimiterExtractor } from "@flatfile/plugin-delimiter-extractor";

  listener.use(DelimiterExtractor(".txt", { delimiter: ":" }));
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/platform";
  import { DelimiterExtractor } from "@flatfile/plugin-delimiter-extractor";

  listener.use(DelimiterExtractor(".txt", { delimiter: ":" }));
  ```
</CodeGroup>

### Advanced Configuration

This example shows a more detailed configuration for `.data` files with type conversion, empty line handling, and value transformation:

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/platform";
  import { DelimiterExtractor } from "@flatfile/plugin-delimiter-extractor";

  const options = {
    delimiter: "#",
    dynamicTyping: true,
    skipEmptyLines: 'greedy',
    transform: (value) => {
      if (typeof value === 'string') {
        return value.toUpperCase();
      }
      return value;
    },
  };

  listener.use(DelimiterExtractor(".data", options));
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/platform";
  import { DelimiterExtractor } from "@flatfile/plugin-delimiter-extractor";

  const options = {
    delimiter: "#",
    dynamicTyping: true,
    skipEmptyLines: 'greedy' as const,
    transform: (value: any) => {
      if (typeof value === 'string') {
        return value.toUpperCase();
      }
      return value;
    },
  };

  listener.use(DelimiterExtractor(".data", options));
  ```
</CodeGroup>

### Custom Header Detection

This example demonstrates how to use advanced header detection options to explicitly define headers:

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/platform";
  import { DelimiterExtractor } from "@flatfile/plugin-delimiter-extractor";

  const advancedOptions = {
    delimiter: "~",
    headerDetectionOptions: {
      algorithm: 'explicitHeaders',
      headers: ['product_id', 'product_name', 'quantity', 'price'],
      skip: 1 // Skip the first row in the file
    }
  };

  listener.use(DelimiterExtractor(".inv", advancedOptions));
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/platform";
  import { DelimiterExtractor } from "@flatfile/plugin-delimiter-extractor";

  const advancedOptions = {
    delimiter: "~",
    headerDetectionOptions: {
      algorithm: 'explicitHeaders' as const,
      headers: ['product_id', 'product_name', 'quantity', 'price'],
      skip: 1 // Skip the first row in the file
    }
  };

  listener.use(DelimiterExtractor(".inv", advancedOptions));
  ```
</CodeGroup>

### Direct Buffer Parsing

For advanced use cases where you need to parse a buffer directly:

<CodeGroup>
  ```javascript JavaScript
  import * as fs from 'fs';
  import { delimiterParser } from "@flatfile/plugin-delimiter-extractor";

  async function parseLocalFile() {
    const fileBuffer = fs.readFileSync('my-data.txt');
    const options = { delimiter: '|', dynamicTyping: true };

    const workbookData = await delimiterParser(fileBuffer, options);
    console.log(workbookData.Sheet1.headers);
    console.log(workbookData.Sheet1.data[0]);
  }

  parseLocalFile();
  ```

  ```typescript TypeScript
  import * as fs from 'fs';
  import { delimiterParser } from "@flatfile/plugin-delimiter-extractor";

  async function parseLocalFile(): Promise<void> {
    const fileBuffer = fs.readFileSync('my-data.txt');
    const options = { delimiter: '|', dynamicTyping: true };

    const workbookData = await delimiterParser(fileBuffer, options);
    console.log(workbookData.Sheet1.headers);
    console.log(workbookData.Sheet1.data[0]);
  }

  parseLocalFile();
  ```
</CodeGroup>

## Troubleshooting

### No Data Appears After Upload

If a file is uploaded but no data appears, check the following:

1. **File Extension**: Ensure the file extension matches the one configured in `DelimiterExtractor(fileExt, ...)`
2. **Delimiter**: Verify that the `delimiter` option matches the actual delimiter used in the file
3. **Empty Files**: If the file is empty or contains no parsable data, the plugin will log "No data found in the file" to the console and produce no records

### Unsupported File Types Error

<CodeGroup>
  ```javascript JavaScript
  try {
    // This will throw an error
    const csvExtractor = DelimiterExtractor(".csv", { delimiter: "," });
  } catch (e) {
    console.error(e.message); 
    // -> ".csv is a native file type and not supported by the delimiter extractor."
  }
  ```

  ```typescript TypeScript
  try {
    // This will throw an error
    const csvExtractor = DelimiterExtractor(".csv", { delimiter: "," });
  } catch (e: any) {
    console.error(e.message); 
    // -> ".csv is a native file type and not supported by the delimiter extractor."
  }
  ```
</CodeGroup>

## Notes

### Limitations

* The plugin explicitly does not support file types that are natively handled by Flatfile: `.csv` (comma-separated), `.tsv` (tab-separated), and `.psv` (pipe-separated)
* The list of supported delimiters is fixed to: `;`, `:`, `~`, `^`, `#`
* This plugin is intended to be run in a server-side listener environment within the Flatfile Platform

### Error Handling

* The main `DelimiterExtractor` function includes a guard clause that throws an `Error` if an unsupported native file type is provided
* The internal parsing function uses try-catch blocks to handle parsing errors, which are logged to the console and re-thrown, causing the associated Flatfile job to fail

### Default Behavior

* By default, the plugin does not perform type conversion (`dynamicTyping: false`)
* Empty lines are included in the output unless explicitly configured otherwise (`skipEmptyLines: false`)
* The plugin processes 10,000 records per chunk with no parallel processing (`chunkSize: 10000`, `parallel: 1`)
* Header detection uses the 'default' algorithm, selecting the row with the most non-empty cells within the first 10 rows
