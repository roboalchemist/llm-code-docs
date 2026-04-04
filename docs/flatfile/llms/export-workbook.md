# Source: https://flatfile.com/docs/plugins/export-workbook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Export Workbook Plugin

> A server-side utility for Flatfile that allows users to export data from an entire Flatfile Workbook into a single, downloadable Microsoft Excel (.xlsx) file.

The Export Workbook Plugin is a server-side utility for Flatfile that allows users to export data from an entire Flatfile Workbook into a single, downloadable Microsoft Excel (`.xlsx`) file.

Its primary purpose is to provide a simple way to get data out of Flatfile in a widely-used format. The plugin is triggered by a user action, typically a "Download" button configured on the workbook. It then iterates through all the sheets in the workbook (unless some are excluded), fetches the records, and compiles them into a corresponding sheet in the generated Excel file.

Use cases include:

* Allowing end-users to download a copy of their cleaned and validated data after an import
* Creating backups or snapshots of data within a Flatfile Space
* Exporting data for use in other systems that accept Excel files
* Providing a final report of all imported data, including any validation messages as comments in the Excel cells

## Installation

<CodeGroup>
  ```bash npm theme={null}
  npm install @flatfile/plugin-export-workbook
  ```
</CodeGroup>

## Configuration & Parameters

The plugin is configured by passing an options object to the `exportWorkbookPlugin` function.

| Parameter               | Type                                                | Default                       | Description                                                                                                                                                                                                |
| ----------------------- | --------------------------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `jobName`               | `string`                                            | `'workbook:downloadWorkbook'` | The name of the job operation that the plugin will listen for. This must match the `operation` name of an action configured on the workbook.                                                               |
| `excludedSheets`        | `string[]`                                          | `undefined`                   | An array of sheet slugs to be excluded from the export.                                                                                                                                                    |
| `excludeFields`         | `string[]`                                          | `undefined`                   | An array of field keys (column names) to be excluded from the export across all sheets.                                                                                                                    |
| `excludeMessages`       | `boolean`                                           | `false`                       | If set to `true`, validation messages on records will not be included as comments in the cells of the exported Excel file.                                                                                 |
| `recordFilter`          | `'valid' \| 'error' \| 'all'`                       | `undefined`                   | Filters the records to be exported. Can be set to 'valid' to export only records without errors, or 'error' to export only records with errors.                                                            |
| `includeRecordIds`      | `boolean`                                           | `false`                       | If set to `true`, a 'recordId' column containing the Flatfile internal record ID will be added as the first column in each sheet.                                                                          |
| `autoDownload`          | `boolean`                                           | `false`                       | If set to `true`, the exported file will be downloaded automatically in the user's browser upon job completion. If `false`, the user is directed to the "Files" page in the Flatfile Space to download it. |
| `filename`              | `string`                                            | `undefined`                   | A custom filename for the exported file (without the `.xlsx` extension). If not provided, a filename is generated using the workbook name and a timestamp.                                                 |
| `debug`                 | `boolean`                                           | `false`                       | If set to `true`, the plugin will output verbose logging to the console, which is useful for development and troubleshooting.                                                                              |
| `sheetOptions`          | `Record<string, ExportSheetOptions>`                | `undefined`                   | An object that maps a sheet slug to sheet-specific export options.                                                                                                                                         |
| `columnNameTransformer` | `(columnName: string, sheetSlug: string) => string` | `undefined`                   | A callback function to dynamically transform column names before they are written to the Excel file.                                                                                                       |

### Sheet Options

The `sheetOptions` parameter allows you to configure specific sheets with the following options:

| Option              | Type                                      | Description                                                                                                                                 |
| ------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `skipColumnHeaders` | `boolean`                                 | If `true`, the header row with column names is omitted for that sheet.                                                                      |
| `origin`            | `number \| {row: number, column: number}` | Sets the starting cell for the data in the sheet. A number sets the starting row, while an object can set both the starting row and column. |

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

  export default function (listener) {
    // Use the plugin with default settings
    listener.use(exportWorkbookPlugin());
  }

  /*
  // In your workbook.config.json, you need an action to trigger the plugin:
  "actions": [
    {
      "operation": "downloadWorkbook",
      "mode": "foreground",
      "label": "Download Excel Workbook",
      "description": "Downloads all data in an Excel file.",
      "primary": true
    }
  ]
  */
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

  export default function (listener: FlatfileListener) {
    // Use the plugin with default settings
    listener.use(exportWorkbookPlugin());
  }

  /*
  // In your workbook.config.json, you need an action to trigger the plugin:
  "actions": [
    {
      "operation": "downloadWorkbook",
      "mode": "foreground",
      "label": "Download Excel Workbook",
      "description": "Downloads all data in an Excel file.",
      "primary": true
    }
  ]
  */
  ```
</CodeGroup>

### Configuration Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

  export default function (listener) {
    listener.use(
      exportWorkbookPlugin({
        // Only export records that have passed validation
        recordFilter: 'valid',
        // Exclude the 'internal_notes' field from all sheets
        excludeFields: ['internal_notes'],
        // Exclude the 'raw_data' sheet entirely
        excludedSheets: ['raw_data'],
        // Automatically start the download for the user
        autoDownload: true,
        // Enable verbose logging for troubleshooting
        debug: true,
        // Add custom options for the 'contacts' sheet
        sheetOptions: {
          contacts: {
            // Omit the header row for the 'contacts' sheet
            skipColumnHeaders: true,
          },
        },
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

  export default function (listener: FlatfileListener) {
    listener.use(
      exportWorkbookPlugin({
        // Only export records that have passed validation
        recordFilter: 'valid',
        // Exclude the 'internal_notes' field from all sheets
        excludeFields: ['internal_notes'],
        // Exclude the 'raw_data' sheet entirely
        excludedSheets: ['raw_data'],
        // Automatically start the download for the user
        autoDownload: true,
        // Enable verbose logging for troubleshooting
        debug: true,
        // Add custom options for the 'contacts' sheet
        sheetOptions: {
          contacts: {
            // Omit the header row for the 'contacts' sheet
            skipColumnHeaders: true,
          },
        },
      })
    );
  }
  ```
</CodeGroup>

### Advanced Usage with Column Transformer

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

  export default function (listener) {
    listener.use(
      exportWorkbookPlugin({
        // Use a custom job name
        jobName: 'export:customExcel',
        // Transform column names to be more user-friendly
        columnNameTransformer: (columnName, sheetSlug) => {
          // Example: transform 'firstName' to 'First Name'
          const friendlyName = columnName.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
          
          // Add a prefix for a specific sheet
          if (sheetSlug === 'users') {
            return `User - ${friendlyName}`;
          }
          
          return friendlyName;
        },
      })
    );
  }

  /*
  // In your workbook.config.json, the action must match the custom jobName:
  "actions": [
    {
      "operation": "export:customExcel",
      "mode": "foreground",
      "label": "Download Custom Excel Report",
      "primary": true
    }
  ]
  */
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { exportWorkbookPlugin } from "@flatfile/plugin-export-workbook";

  export default function (listener: FlatfileListener) {
    listener.use(
      exportWorkbookPlugin({
        // Use a custom job name
        jobName: 'export:customExcel',
        // Transform column names to be more user-friendly
        columnNameTransformer: (columnName: string, sheetSlug: string) => {
          // Example: transform 'firstName' to 'First Name'
          const friendlyName = columnName.replace(/([A-Z])/g, ' $1').replace(/^./, (str) => str.toUpperCase());
          
          // Add a prefix for a specific sheet
          if (sheetSlug === 'users') {
            return `User - ${friendlyName}`;
          }
          
          return friendlyName;
        },
      })
    );
  }

  /*
  // In your workbook.config.json, the action must match the custom jobName:
  "actions": [
    {
      "operation": "export:customExcel",
      "mode": "foreground",
      "label": "Download Custom Excel Report",
      "primary": true
    }
  ]
  */
  ```
</CodeGroup>

## Troubleshooting

### Enable Debug Mode

The most important troubleshooting tool is the `debug: true` option. When enabled, the plugin prints detailed logs to the console, including which sheets are being processed, which are skipped, and the status of file writing and uploading.

### Check Action Operation

If the plugin does not trigger when the action button is clicked, ensure the `operation` value in your `workbook.config.json` action exactly matches the `jobName` used to configure the plugin.

### No Data Exported

If the exported file is empty or missing sheets, check if a `recordFilter` is unintentionally filtering out all records or if `excludedSheets` is misconfigured. The `debug` logs will show if sheets are being skipped. If all sheets are empty, the plugin will throw an error: `No data to write to Excel file.`

## Notes

### Server-Side Execution

This plugin must be deployed in a server-side listener environment, not in the browser.

### Action Configuration

For the plugin to be triggered, a corresponding `action` must be configured on the `Workbook` in your `workbook.config.json`. The `operation` of this action must match the `jobName` option of the plugin (which defaults to `workbook:downloadWorkbook`).

### File System Access

The plugin temporarily writes the `.xlsx` file to the `/tmp` directory of the execution environment, which is standard for serverless functions.

### Sheet Name Sanitization

Excel sheet names have limitations (e.g., max 31 characters, no invalid characters like `\ / ? * [ ]`). The plugin automatically sanitizes sheet names from your workbook to comply with these rules. If a name becomes empty after sanitization, it will be replaced with a default like `Sheet1`, `Sheet2`, etc.

### Default Behavior

* By default, all records from all sheets are exported
* Validation messages are included as comments in the Excel cells
* The exported file is made available in the "Files" page rather than auto-downloading
* Column headers are included in the export
* A filename is auto-generated using the workbook name and timestamp if not specified

### Error Handling

The plugin wraps its entire logic in a `try...catch` block. If any critical step fails (fetching records, writing the file to disk, uploading the file to Flatfile), it logs the error and throws a new `Error`. This causes the associated job in Flatfile to fail and display the error message to the user, providing feedback on what went wrong.
