# Source: https://flatfile.com/docs/plugins/markdown.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Markdown File Extractor

> Automatically parse Markdown files and extract tables into Flatfile Sheets

The Markdown Extractor plugin is designed to automatically parse Markdown files (`.md`) uploaded to Flatfile. Its primary purpose is to find and extract any tables present in the markdown content. For each table it discovers, the plugin creates a new Sheet within the Flatfile Space. The table's header row is used to define the fields (columns) of the Sheet, and the subsequent rows are converted into records. This is useful for importing data that is documented or stored in Markdown files, such as in project readmes, wikis, or technical documentation.

## Installation

Install the Markdown Extractor plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-markdown-extractor
```

## Configuration & Parameters

The plugin accepts the following configuration options:

### maxTables

* **Type:** `number`
* **Default:** `Infinity`
* **Description:** Sets the maximum number of tables to extract from a single Markdown file. By default, it will extract all tables it finds.

### errorHandling

* **Type:** `'strict' | 'lenient'`
* **Default:** `'lenient'`
* **Description:** Controls how parsing errors are handled:
  * `'strict'`: The plugin will throw an error and stop processing if it encounters a malformed table (e.g., a data row with a different number of columns than the header)
  * `'lenient'`: The plugin will log a warning to the console, skip the problematic table, and continue processing the rest of the file

### debug

* **Type:** `boolean`
* **Default:** `false`
* **Description:** When set to true, enables verbose logging to the console. This is useful for troubleshooting issues with file parsing, as it shows the content being parsed, tables found, and the final normalized data.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { listener } from '@flatfile/listener';
  import { MarkdownExtractor } from '@flatfile/plugin-markdown-extractor';

  export default function(listener) {
    listener.use(MarkdownExtractor());
  }
  ```

  ```typescript TypeScript theme={null}
  import { listener } from '@flatfile/listener';
  import { MarkdownExtractor } from '@flatfile/plugin-markdown-extractor';

  export default function(listener: any) {
    listener.use(MarkdownExtractor());
  }
  ```
</CodeGroup>

### Configuration Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { listener } from '@flatfile/listener';
  import { MarkdownExtractor } from '@flatfile/plugin-markdown-extractor';

  export default function(listener) {
    const options = {
      maxTables: 5,
      errorHandling: 'strict',
      debug: true
    };

    listener.use(MarkdownExtractor(options));
  }
  ```

  ```typescript TypeScript theme={null}
  import { listener } from '@flatfile/listener';
  import { MarkdownExtractor } from '@flatfile/plugin-markdown-extractor';

  export default function(listener: any) {
    const options = {
      maxTables: 5,
      errorHandling: 'strict' as const,
      debug: true
    };

    listener.use(MarkdownExtractor(options));
  }
  ```
</CodeGroup>

### Direct Parser Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import * as fs from 'fs';
  import { markdownParser } from '@flatfile/plugin-markdown-extractor';

  const markdownContent = '| ID | Name |\n|----|------|\n| 1  | Test |';
  const buffer = Buffer.from(markdownContent, 'utf-8');

  const workbookData = markdownParser(buffer, { errorHandling: 'lenient' });

  console.log(JSON.stringify(workbookData, null, 2));
  ```

  ```typescript TypeScript theme={null}
  import * as fs from 'fs';
  import { markdownParser } from '@flatfile/plugin-markdown-extractor';

  const markdownContent = '| ID | Name |\n|----|------|\n| 1  | Test |';
  const buffer = Buffer.from(markdownContent, 'utf-8');

  const workbookData = markdownParser(buffer, { errorHandling: 'lenient' });

  console.log(JSON.stringify(workbookData, null, 2));
  ```
</CodeGroup>

## API Reference

### MarkdownExtractor(options?)

The main factory function used to create and configure the markdown extractor plugin for use with a Flatfile listener.

**Parameters:**

* `options` (optional): Configuration settings object

**Returns:** An `Extractor` instance that can be passed to `listener.use()`

**Example:**

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { listener } from '@flatfile/listener';
  import { MarkdownExtractor } from '@flatfile/plugin-markdown-extractor';

  export default function(myListener) {
    // Use with default options
    myListener.use(MarkdownExtractor());

    // Use with custom options
    myListener.use(MarkdownExtractor({ maxTables: 1, errorHandling: 'strict' }));
  }
  ```

  ```typescript TypeScript theme={null}
  import { listener } from '@flatfile/listener';
  import { MarkdownExtractor } from '@flatfile/plugin-markdown-extractor';

  export default function(myListener: any) {
    // Use with default options
    myListener.use(MarkdownExtractor());

    // Use with custom options
    myListener.use(MarkdownExtractor({ maxTables: 1, errorHandling: 'strict' }));
  }
  ```
</CodeGroup>

### markdownParser(buffer, options)

A low-level function that directly parses a Buffer containing markdown content into a Flatfile `WorkbookCapture` object.

**Parameters:**

* `buffer`: A Node.js Buffer containing the UTF-8 encoded content of a markdown file
* `options`: Configuration settings object

**Returns:** A `WorkbookCapture` object, which is a map of sheet names to sheet data

**Example:**

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { markdownParser } from '@flatfile/plugin-markdown-extractor';

  const markdownContent = '| ID | Name |\n|----|------|\n| 1  | Test |';
  const buffer = Buffer.from(markdownContent, 'utf-8');

  const workbookData = markdownParser(buffer, { errorHandling: 'lenient' });
  console.log(JSON.stringify(workbookData, null, 2));
  ```

  ```typescript TypeScript theme={null}
  import { markdownParser } from '@flatfile/plugin-markdown-extractor';

  const markdownContent = '| ID | Name |\n|----|------|\n| 1  | Test |';
  const buffer = Buffer.from(markdownContent, 'utf-8');

  const workbookData = markdownParser(buffer, { errorHandling: 'lenient' });
  console.log(JSON.stringify(workbookData, null, 2));
  ```
</CodeGroup>

## Troubleshooting

### Error Handling Example

This example demonstrates how the `errorHandling` option affects behavior when parsing a malformed table:

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { markdownParser } from '@flatfile/plugin-markdown-extractor';

  // Table has a header with 2 columns but a data row with 3
  const malformedContent = '| A | B |\n|---|---|\n| 1 | 2 | 3 |';
  const buffer = Buffer.from(malformedContent, 'utf-8');

  // 'strict' mode will throw an error
  try {
    markdownParser(buffer, { errorHandling: 'strict' });
  } catch (e) {
    console.error('Caught error in strict mode:', e.message);
    //-> Caught error in strict mode: Data row length does not match header row length
  }

  // 'lenient' mode will not throw but will log a warning and skip the table
  const result = markdownParser(buffer, { errorHandling: 'lenient' });
  console.log('Result in lenient mode:', result);
  // (A warning is logged to the console)
  //-> Result in lenient mode: {}
  ```

  ```typescript TypeScript theme={null}
  import { markdownParser } from '@flatfile/plugin-markdown-extractor';

  // Table has a header with 2 columns but a data row with 3
  const malformedContent = '| A | B |\n|---|---|\n| 1 | 2 | 3 |';
  const buffer = Buffer.from(malformedContent, 'utf-8');

  // 'strict' mode will throw an error
  try {
    markdownParser(buffer, { errorHandling: 'strict' });
  } catch (e: any) {
    console.error('Caught error in strict mode:', e.message);
    //-> Caught error in strict mode: Data row length does not match header row length
  }

  // 'lenient' mode will not throw but will log a warning and skip the table
  const result = markdownParser(buffer, { errorHandling: 'lenient' });
  console.log('Result in lenient mode:', result);
  // (A warning is logged to the console)
  //-> Result in lenient mode: {}
  ```
</CodeGroup>

### Debug Mode

To diagnose parsing issues, enable debug mode:

<CodeGroup>
  ```javascript JavaScript theme={null}
  listener.use(MarkdownExtractor({ debug: true }));
  ```

  ```typescript TypeScript theme={null}
  listener.use(MarkdownExtractor({ debug: true }));
  ```
</CodeGroup>

## Notes

### Default Behavior

* The plugin extracts all tables found in a markdown file by default (`maxTables: Infinity`)
* Uses lenient error handling by default, skipping malformed tables and continuing processing
* Debug logging is disabled by default

### Special Considerations

* This plugin is intended for use in a server-side Flatfile listener
* It operates on files with the `.md` extension
* For each table found in a markdown file, a new Sheet is created with auto-generated names (`Table_1`, `Table_2`, etc.)
* The parser expects standard GitHub-flavored markdown table syntax
* Highly complex or non-standard tables may not be parsed correctly

### Error Handling Patterns

* **Lenient mode (default)**: Logs warnings for malformed tables and continues processing
* **Strict mode**: Throws errors immediately when encountering malformed tables, failing the entire file processing

### Troubleshooting Tips

* Set `debug: true` to enable detailed logging for diagnosing parsing issues
* Check console output for warnings about skipped tables in lenient mode
* Ensure markdown tables follow standard GitHub-flavored markdown syntax
* Verify that header and data rows have matching column counts
