# Source: https://flatfile.com/docs/plugins/html-table.md

# HTML Table Extractor

> Parse HTML files and extract data from tables within them, converting structured data into Flatfile-compatible format

This plugin for Flatfile is designed to parse HTML files and extract data from tables within them. Its main purpose is to automatically convert structured data found in HTML `<table>` elements into a format that Flatfile can process.

The plugin can handle multiple tables within a single HTML file, creating a separate sheet for each one. It is capable of interpreting complex table layouts that use `colspan` and `rowspan` attributes to merge cells, ensuring the data is correctly aligned. Use cases include importing data from legacy systems that export reports as HTML pages, scraping data from web pages, or processing any structured data provided in an HTML table format.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-extract-html-table
```

## Configuration & Parameters

The plugin accepts the following configuration options:

| Parameter       | Type    | Default | Description                                                                                                                                         |
| --------------- | ------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `handleColspan` | boolean | `true`  | When true, the plugin will correctly handle cells with a `colspan` attribute by duplicating the cell's value across the specified number of columns |
| `handleRowspan` | boolean | `true`  | When true, the plugin will attempt to handle cells with a `rowspan` attribute by carrying the cell's value down into the subsequent rows            |
| `maxDepth`      | number  | `3`     | Defines the maximum depth for parsing nested tables (Note: not currently implemented)                                                               |
| `debug`         | boolean | `false` | When set to true, the plugin will output detailed logs to the console during the parsing process                                                    |

### Default Behavior

By default, the plugin processes HTML files with `handleColspan` and `handleRowspan` enabled, meaning it will attempt to correctly structure data from cells that span multiple columns or rows. Debug logging is disabled, and the nesting depth for tables is notionally set to 3.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript
  import { FlatfileListener } from '@flatfile/listener';
  import { HTMLTableExtractor } from '@flatfile/plugin-extract-html-table';

  const listener = new FlatfileListener();

  // Use the extractor with default options
  listener.use(HTMLTableExtractor());
  ```

  ```typescript
  import { FlatfileListener } from '@flatfile/listener';
  import { HTMLTableExtractor } from '@flatfile/plugin-extract-html-table';

  const listener = new FlatfileListener();

  // Use the extractor with default options
  listener.use(HTMLTableExtractor());
  ```
</CodeGroup>

### Configuration Example

<CodeGroup>
  ```javascript
  import { FlatfileListener } from '@flatfile/listener';
  import { HTMLTableExtractor } from '@flatfile/plugin-extract-html-table';

  const listener = new FlatfileListener();

  // Use the extractor with custom options
  listener.use(
    HTMLTableExtractor({
      handleColspan: true,
      handleRowspan: false, // Disable rowspan handling
      debug: true // Enable verbose logging for troubleshooting
    })
  );
  ```

  ```typescript
  import { FlatfileListener } from '@flatfile/listener';
  import { HTMLTableExtractor } from '@flatfile/plugin-extract-html-table';

  const listener = new FlatfileListener();

  // Use the extractor with custom options
  listener.use(
    HTMLTableExtractor({
      handleColspan: true,
      handleRowspan: false, // Disable rowspan handling
      debug: true // Enable verbose logging for troubleshooting
    })
  );
  ```
</CodeGroup>

### Direct Parser Usage

This example shows how to use the parser function directly, outside of a Flatfile listener, to process an HTML file:

<CodeGroup>
  ```javascript
  import * as fs from 'fs';
  import { htmlTableParser } from '@flatfile/plugin-extract-html-table';

  // Read an HTML file into a buffer
  const fileBuffer = fs.readFileSync('path/to/your/table.html');

  // Define parser options
  const options = {
    handleColspan: true,
    handleRowspan: true,
    debug: false
  };

  // Parse the buffer to get structured data
  try {
    const workbookData = htmlTableParser(fileBuffer, options);
    console.log('Extracted Workbook:', JSON.stringify(workbookData, null, 2));
  } catch (error) {
    console.error('An error occurred during parsing:', error);
  }
  ```

  ```typescript
  import * as fs from 'fs';
  import { htmlTableParser } from '@flatfile/plugin-extract-html-table';

  // Read an HTML file into a buffer
  const fileBuffer = fs.readFileSync('path/to/your/table.html');

  // Define parser options
  const options = {
    handleColspan: true,
    handleRowspan: true,
    debug: false
  };

  // Parse the buffer to get structured data
  try {
    const workbookData = htmlTableParser(fileBuffer, options);
    console.log('Extracted Workbook:', JSON.stringify(workbookData, null, 2));
  } catch (error) {
    console.error('An error occurred during parsing:', error);
  }
  ```
</CodeGroup>

### Example with HTML Content

<CodeGroup>
  ```javascript
  import { htmlTableParser } from '@flatfile/plugin-extract-html-table';

  const htmlContent = '<table><thead><tr><th>Name</th><th>Age</th></tr></thead><tbody><tr><td>John</td><td>30</td></tr></tbody></table>';
  const buffer = Buffer.from(htmlContent, 'utf-8');
  const workbook = htmlTableParser(buffer, {});

  // workbook will be:
  // {
  //   "Table_1": {
  //     "headers": ["Name", "Age"],
  //     "data": [{ "Name": { "value": "John" }, "Age": { "value": "30" } }]
  //   }
  // }
  ```

  ```typescript
  import { htmlTableParser } from '@flatfile/plugin-extract-html-table';

  const htmlContent = '<table><thead><tr><th>Name</th><th>Age</th></tr></thead><tbody><tr><td>John</td><td>30</td></tr></tbody></table>';
  const buffer = Buffer.from(htmlContent, 'utf-8');
  const workbook = htmlTableParser(buffer, {});

  // workbook will be:
  // {
  //   "Table_1": {
  //     "headers": ["Name", "Age"],
  //     "data": [{ "Name": { "value": "John" }, "Age": { "value": "30" } }]
  //   }
  // }
  ```
</CodeGroup>

## Troubleshooting

If data is missing or incorrect, enable `debug: true` in the configuration to see a step-by-step log of the parsing process:

<CodeGroup>
  ```javascript
  listener.use(
    HTMLTableExtractor({
      debug: true
    })
  );
  ```

  ```typescript
  listener.use(
    HTMLTableExtractor({
      debug: true
    })
  );
  ```
</CodeGroup>

Ensure the source HTML file contains well-structured `<table>` elements with `<th>` tags for headers and `<td>` tags for data cells. The plugin's effectiveness is highly dependent on the quality of the input HTML.

## Notes

### Important Considerations

* **Supported File Type**: The plugin is hardcoded to only process files with the `.html` extension
* **Event Listener**: It operates on the `listener.on('file:created')` event
* **Multiple Tables**: Each `<table>` element found in the HTML document will be extracted into its own separate sheet within the Flatfile workbook. Sheets are named sequentially: `Table_1`, `Table_2`, and so on
* **Header Extraction**: Headers are extracted from `<th>` elements. If a table has no `<th>` elements, the `headers` array for that sheet will be empty, and data rows will likely not be mapped correctly

### Limitations

* **`maxDepth` Limitation**: The `maxDepth` configuration option is defined in the options type but is not currently implemented in the parsing logic. Nested tables are processed, but their depth is not limited by this setting
* **`rowspan` Implementation**: The current implementation for `handleRowspan` may not function as expected because it attempts to re-parse trimmed text content of a cell to find an attribute, which is not possible. This feature should be considered unreliable

### Error Handling

* The primary method for diagnosing issues is to set the `debug` option to `true`. This will print detailed logs of the extraction process, including tables found, headers extracted, and cell data
* If a data row contains more cells than there are headers, a warning is logged (in debug mode) and the extra cell data is ignored to prevent data misalignment
* The underlying HTML parser is generally resilient to malformed HTML, but if the table structure (`<table>`, `<tr>`, `<th>`, `<td>`) is invalid, the function may return an empty object or partially extracted data
