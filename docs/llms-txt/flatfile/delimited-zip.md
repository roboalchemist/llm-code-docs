# Source: https://flatfile.com/docs/plugins/delimited-zip.md

# Delimited File Zip Exporter

> Export data from all sheets within a Flatfile Workbook into delimited text files and compress them into a single ZIP archive for download.

This plugin is designed to be used in a server-side Flatfile listener. Its primary purpose is to export data from all sheets within a Flatfile Workbook into delimited text files (such as CSV or TSV). After generating a file for each sheet, it compresses all of them into a single ZIP archive. This ZIP file is then uploaded back into the Flatfile space, making it available for download. This is useful for users who need to download all their processed data from a workbook in a portable, compressed format for use in other systems or for archival purposes. The plugin is triggered by a `job:ready` event.

## Installation

Install the plugin via npm:

```bash
npm install @flatfile/plugin-export-delimited-zip
```

## Configuration & Parameters

The plugin is configured by passing an options object to the `exportDelimitedZip` function.

| Parameter       | Type      | Default               | Description                                                                                                                     |
| --------------- | --------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `job`           | `string`  | `'downloadDelimited'` | The job name that will trigger the export process. The listener will be configured to listen for `workbook:${job}`.             |
| `delimiter`     | `string`  | `','`                 | The character to use as a delimiter to separate values in the output files. For example, use ',' for CSV or '\t' for TSV.       |
| `fileExtension` | `string`  | `'csv'`               | The file extension to use for the generated delimited files (e.g., 'csv', 'txt', 'tsv').                                        |
| `debug`         | `boolean` | `false`               | When set to true, the plugin will print detailed logs to the console during its execution, which is useful for troubleshooting. |

### Default Behavior

By default, the plugin listens for a job named `workbook:downloadDelimited`. When triggered, it will process all sheets in the workbook, convert them to CSV files (using a comma delimiter), zip them up, and upload the final archive. Debug logging is disabled.

## Usage Examples

<Tabs>
  <Tab title="JavaScript">
    ```javascript
    import { exportDelimitedZip } from '@flatfile/plugin-export-delimited-zip'

    export default function (listener) {
      // Using default options for a job named 'downloadDelimited'
      // that exports to .csv files
      listener.use(exportDelimitedZip({
          job: 'downloadDelimited',
          delimiter: ',',
          fileExtension: 'csv'
      }))
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    import type { FlatfileListener } from '@flatfile/listener'
    import { exportDelimitedZip } from '@flatfile/plugin-export-delimited-zip'

    export default function (listener: FlatfileListener) {
      // Using default options for a job named 'downloadDelimited'
      // that exports to .csv files
      listener.use(exportDelimitedZip({
          job: 'downloadDelimited',
          delimiter: ',',
          fileExtension: 'csv'
      }))
    }
    ```
  </Tab>
</Tabs>

### Custom Configuration

<Tabs>
  <Tab title="JavaScript">
    ```javascript
    import { exportDelimitedZip } from '@flatfile/plugin-export-delimited-zip'

    export default function (listener) {
      // Custom configuration to create tab-separated files (.tsv)
      // triggered by a job named 'export-workbook-tsv'
      // with debug logging enabled.
      listener.use(exportDelimitedZip({
          job: 'export-workbook-tsv',
          delimiter: '\t',
          fileExtension: 'tsv',
          debug: true
        }))
    }
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript
    import type { FlatfileListener } from '@flatfile/listener'
    import { exportDelimitedZip } from '@flatfile/plugin-export-delimited-zip'

    export default function (listener: FlatfileListener) {
      // Custom configuration to create tab-separated files (.tsv)
      // triggered by a job named 'export-workbook-tsv'
      // with debug logging enabled.
      listener.use(exportDelimitedZip({
          job: 'export-workbook-tsv',
          delimiter: '\t',
          fileExtension: 'tsv',
          debug: true
        }))
    }
    ```
  </Tab>
</Tabs>

## API Reference

### exportDelimitedZip(options)

This function registers a listener plugin that handles the process of exporting workbook data to a compressed ZIP file. It sets up a job handler for a `job:ready` event. When the specified job is executed, the plugin fetches all sheets in the workbook, streams their records, and writes them to local temporary files using the specified delimiter. These files are then added to a ZIP archive, which is uploaded to the Flatfile space. Finally, the temporary files and directory are cleaned up.

**Parameters:**

* `options` (PluginOptions) - An object containing configuration for the plugin
  * `job` (string) - The job name to listen for
  * `delimiter` (string) - The delimiter character for the output files
  * `fileExtension` (string) - The file extension for the output files
  * `debug` (boolean, optional) - An optional flag to enable verbose console logging

**Return Value:**
Returns a `FlatfileListener` plugin instance that can be passed to `listener.use()`. The job itself, when completed successfully, returns an `outcome` object to the Flatfile UI containing a message and a link to the generated ZIP file.

## Troubleshooting

The primary method for troubleshooting is to enable the `debug: true` configuration option. This will output detailed step-by-step logs to the console, including retrieved sheets, file paths, record counts, and any caught errors. This provides visibility into where the process might be failing.

### Error Handling

If any part of the process fails (e.g., reading sheets, writing temporary files, zipping, or uploading), the function will catch the error and fail the job with a generic message: "This job failed probably because it couldn't write to the \[EXTENSION] files, compress them into a ZIP file, or upload it.". To diagnose the specific cause of failure, set the `debug` option to `true` to see detailed error logs in the console where the listener is running.

The core logic is wrapped in a single `try...catch` block. If an error occurs at any stage, it is caught, and the job is marked as failed with a general error message. Specific warnings are logged to the console if the cleanup of temporary files fails, but these do not cause the job to fail.

## Notes

### Requirements and Limitations

* **Server-Side Execution**: This plugin must be deployed in a server-side listener environment (e.g., Node.js) as it requires access to the file system (`fs`) to create temporary files and directories.
* **Temporary Files**: The plugin writes temporary delimited files and a temporary ZIP file to the operating system's temporary directory (`os.tmpdir()`). It attempts to clean these files up after the upload is complete, but in case of an unhandled crash, temporary files might be left behind.
* **File Name Sanitization**: The plugin sanitizes both the workbook name and sheet names to create valid file names. It removes special characters (`[<>:"/\\|?*]`) and replaces spaces with underscores.
* **Sheet Name Length**: Sheet names are trimmed to a maximum of 31 characters after sanitization to avoid issues with file system or ZIP format limitations.
* **Dependencies**: The plugin relies on external libraries `adm-zip` for creating ZIP archives and `csv-stringify` for generating the delimited file content.
