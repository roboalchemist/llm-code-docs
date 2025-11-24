# Source: https://flatfile.com/docs/plugins/xlsx-extractor.md

# Excel Extractor

> Parse various Excel file formats (.xls, .xlsx, .xlsm, .xlsb, .xltx, .xltm) and extract structured data with support for header detection, merged cells, and hierarchical spreadsheets.

The Excel Extractor plugin is designed to parse various Excel file formats (.xls, .xlsx, .xlsm, .xlsb, .xltx, .xltm) and extract structured data from them. When a user uploads a supported Excel file, this plugin automatically processes it, detects headers, and transforms the sheet data into a format that Flatfile can use. It offers extensive configuration for handling complex Excel files, including options for header detection, processing merged cells, and cascading data in hierarchical spreadsheets. This plugin is intended to be used in a server-side listener within the Flatfile platform.

## Installation

Install the Excel Extractor plugin using npm:

```bash
npm install @flatfile/plugin-xlsx-extractor
```

## Configuration & Parameters

The Excel Extractor accepts the following configuration options:

### Basic Options

| Parameter        | Type    | Default     | Description                                                   |
| ---------------- | ------- | ----------- | ------------------------------------------------------------- |
| `raw`            | boolean | `false`     | Extract raw, underlying cell values instead of formatted text |
| `rawNumbers`     | boolean | `false`     | Extract raw numeric values instead of formatted numbers       |
| `dateNF`         | string  | `undefined` | Specific date format string for interpreting dates            |
| `chunkSize`      | number  | `10000`     | Number of records to process in each batch                    |
| `parallel`       | number  | `1`         | Number of chunks to process concurrently                      |
| `skipEmptyLines` | boolean | `false`     | Skip rows that are entirely empty                             |
| `debug`          | boolean | `false`     | Enable verbose logging for troubleshooting                    |

### Advanced Options

| Parameter                | Type    | Default     | Description                                                   |
| ------------------------ | ------- | ----------- | ------------------------------------------------------------- |
| `cascadeRowValues`       | boolean | `false`     | Fill empty cells with values from the cell above              |
| `cascadeHeaderValues`    | boolean | `false`     | Fill empty header cells with values from the cell to the left |
| `headerDetectionOptions` | object  | See below   | Configure header row detection                                |
| `mergedCellOptions`      | object  | `undefined` | Define how to handle merged cells                             |

### Header Detection Options

Default configuration:

```javascript
{
  algorithm: 'default',
  rowsToSearch: 10
}
```

Available algorithms:

* `'default'` - Scans first 10 rows and selects the one with most non-empty cells
* `'explicitHeaders'` - Use when headers are explicitly defined
* `'specificRows'` - Define specific row numbers as headers
* `'dataRowAndSubHeaderDetection'` - Advanced detection for complex header structures

### Merged Cell Options

Configure treatment of merged cells with these options:

| Treatment        | Description                                      |
| ---------------- | ------------------------------------------------ |
| `applyToAll`     | Copy merged cell value to all cells in the range |
| `applyToTopLeft` | Keep value only in top-left cell                 |
| `coalesce`       | Keep first row/column and remove others          |
| `concatenate`    | Combine values with a separator                  |

## Usage Examples

<CodeGroup>
  ```javascript JavaScript - Basic Usage
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';

  export default function (listener) {
    listener.use(ExcelExtractor());
  }
  ```

  ```typescript TypeScript - Basic Usage
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';
  import type { FlatfileListener } from '@flatfile/listener';

  export default function (listener: FlatfileListener) {
    listener.use(ExcelExtractor());
  }
  ```
</CodeGroup>

### Configuration Example

<CodeGroup>
  ```javascript JavaScript - Configuration
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';

  export default function (listener) {
    listener.use(
      ExcelExtractor({
        rawNumbers: true,
        skipEmptyLines: true,
        chunkSize: 50000,
        debug: true,
      })
    );
  }
  ```

  ```typescript TypeScript - Configuration
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';
  import type { FlatfileListener } from '@flatfile/listener';

  export default function (listener: FlatfileListener) {
    listener.use(
      ExcelExtractor({
        rawNumbers: true,
        skipEmptyLines: true,
        chunkSize: 50000,
        debug: true,
      })
    );
  }
  ```
</CodeGroup>

### Advanced Header Detection

<CodeGroup>
  ```javascript JavaScript - Specific Rows
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';

  export default function (listener) {
    listener.use(
      ExcelExtractor({
        headerDetectionOptions: {
          algorithm: 'specificRows',
          rowNumbers: [2], // 0-based index for the third row
        },
      })
    );
  }
  ```

  ```typescript TypeScript - Specific Rows
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';
  import type { FlatfileListener } from '@flatfile/listener';

  export default function (listener: FlatfileListener) {
    listener.use(
      ExcelExtractor({
        headerDetectionOptions: {
          algorithm: 'specificRows',
          rowNumbers: [2], // 0-based index for the third row
        },
      })
    );
  }
  ```
</CodeGroup>

### Merged Cell Handling

<CodeGroup>
  ```javascript JavaScript - Merged Cells
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';

  export default function (listener) {
    listener.use(
      ExcelExtractor({
        mergedCellOptions: {
          acrossColumns: {
            treatment: 'concatenate',
            separator: ' ',
          },
          acrossRows: {
            treatment: 'applyToAll',
          },
        },
      })
    );
  }
  ```

  ```typescript TypeScript - Merged Cells
  import { listener } from '@flatfile/listener';
  import { ExcelExtractor } from '@flatfile/plugin-xlsx-extractor';
  import type { FlatfileListener } from '@flatfile/listener';

  export default function (listener: FlatfileListener) {
    listener.use(
      ExcelExtractor({
        mergedCellOptions: {
          acrossColumns: {
            treatment: 'concatenate',
            separator: ' ',
          },
          acrossRows: {
            treatment: 'applyToAll',
          },
        },
      })
    );
  }
  ```
</CodeGroup>

### Direct Parser Usage

<CodeGroup>
  ```javascript JavaScript - Direct Parser
  import * as fs from 'fs';
  import { excelParser } from '@flatfile/plugin-xlsx-extractor';

  async function parseMyFile(filePath) {
    try {
      const fileBuffer = fs.readFileSync(filePath);
      const workbookData = await excelParser(fileBuffer, {
        skipEmptyLines: true,
      });
      console.log(workbookData['Sheet1'].data);
    } catch (error) {
      console.error('Failed to parse file:', error);
    }
  }
  ```

  ```typescript TypeScript - Direct Parser
  import * as fs from 'fs';
  import { excelParser } from '@flatfile/plugin-xlsx-extractor';
  import type { WorkbookCapture } from '@flatfile/plugin-xlsx-extractor';

  async function parseMyFile(filePath: string): Promise<WorkbookCapture | null> {
    try {
      const fileBuffer = fs.readFileSync(filePath);
      const workbookData = await excelParser(fileBuffer, {
        skipEmptyLines: true,
      });
      console.log(workbookData['Sheet1'].data);
      return workbookData;
    } catch (error) {
      console.error('Failed to parse file:', error);
      return null;
    }
  }
  ```
</CodeGroup>

## Troubleshooting

### Large File Handling

<CodeGroup>
  ```javascript JavaScript - Error Handling
  import { excelParser } from '@flatfile/plugin-xlsx-extractor';

  async function parseLargeFile(buffer) {
    try {
      const workbookData = await excelParser(buffer);
      return workbookData;
    } catch (error) {
      if (error.message === 'plugins.extraction.fileTooLarge') {
        console.error('The file is too large to be processed. Please convert it to CSV first.');
      } else {
        console.error('An unexpected error occurred:', error);
      }
    }
  }
  ```

  ```typescript TypeScript - Error Handling
  import { excelParser } from '@flatfile/plugin-xlsx-extractor';
  import type { WorkbookCapture } from '@flatfile/plugin-xlsx-extractor';

  async function parseLargeFile(buffer: Buffer): Promise<WorkbookCapture | null> {
    try {
      const workbookData = await excelParser(buffer);
      return workbookData;
    } catch (error: any) {
      if (error.message === 'plugins.extraction.fileTooLarge') {
        console.error('The file is too large to be processed. Please convert it to CSV first.');
      } else {
        console.error('An unexpected error occurred:', error);
      }
      return null;
    }
  }
  ```
</CodeGroup>

### Debug Mode

Enable debug mode for detailed logging:

```javascript
ExcelExtractor({
  debug: true
})
```

This provides detailed logs about the extraction process, including detected headers, rows processed, and configuration options being applied.

## Notes

### Default Behavior

* **Header Detection**: By default, the plugin scans the first 10 rows and selects the one with the most non-empty cells as the header row
* **Empty Rows**: Empty rows are included as empty records unless `skipEmptyLines` is set to `true`
* **Merged Cells**: Handled by the underlying library's default behavior unless custom options are provided
* **Chunk Processing**: Data is processed in batches of 10,000 records by default

### Important Considerations

* **Server-Side Only**: This plugin is designed to run in a server-side environment and should be used within a Flatfile listener
* **Duplicate Headers**: If a sheet contains duplicate column headers, the plugin automatically makes them unique by appending a suffix (e.g., 'Name', 'Name\_1', 'Name\_2')
* **Empty Headers**: Empty header cells are renamed to 'empty' (e.g., 'empty', 'empty\_1')
* **Trailing Empty Rows**: The parser automatically trims any fully empty rows from the end of a sheet before processing
* **Memory Limitations**: The plugin has built-in handling for extremely large files that can cause memory issues, throwing a user-friendly error when files are too large

### Cascading Behavior

* **Row Cascading**: When `cascadeRowValues` is enabled, empty cells are filled with values from the cell above. The cascade resets on a completely blank row or a new value in the column
* **Header Cascading**: When `cascadeHeaderValues` is enabled, empty header cells are filled with values from the cell to the left. The cascade resets on a blank column or a new value
