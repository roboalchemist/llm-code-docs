# Source: https://flatfile.com/docs/plugins/zip-extractor.md

# Zip Extractor

> Automatically decompress .zip files uploaded to a Flatfile Space and extract their contents as individual files

The Zip Extractor plugin for Flatfile is designed to automatically decompress `.zip` files uploaded to a Flatfile Space. When a user uploads a zip archive, this plugin intercepts the file, extracts its contents, and uploads each individual file back into the same Space.

This is particularly useful for workflows where users need to bulk-upload multiple files (like CSVs, Excel files, or JSON files) at once. After this plugin runs, other extractor plugins (e.g., `@flatfile/plugin-xlsx-extractor`, `@flatfile/plugin-csv-extractor`) can then process the individual extracted files. The plugin intelligently ignores common system files and directories found in zip archives, such as those starting with a dot (`.`) or `__MACOSX`. It should be deployed in a server-side listener.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-zip-extractor
```

## Configuration & Parameters

The ZipExtractor plugin accepts an optional configuration object with the following parameter:

| Parameter | Type      | Default | Description                                                                                                                                           |
| --------- | --------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `debug`   | `boolean` | `false` | Enables verbose logging for troubleshooting. When set to `true`, it prints helpful information such as file paths of extracted files being processed. |

### Default Behavior

By default, the plugin runs silently without printing extra diagnostic messages to the console. The plugin automatically filters out system files and directories, including files whose names start with a `.` (e.g., `.DS_Store`) and files within the `__MACOSX` directory.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { ZipExtractor } from '@flatfile/plugin-zip-extractor';

  const listener = new FlatfileListener();

  // Register the Zip Extractor with default options
  listener.use(ZipExtractor());

  // When a .zip file is uploaded to Flatfile, the plugin will automatically
  // extract its contents and upload them back to the Space.
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { ZipExtractor } from '@flatfile/plugin-zip-extractor';

  const listener = new FlatfileListener();

  // Register the Zip Extractor with default options
  listener.use(ZipExtractor());

  // When a .zip file is uploaded to Flatfile, the plugin will automatically
  // extract its contents and upload them back to the Space.
  ```
</CodeGroup>

### With Debug Enabled

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { ZipExtractor } from '@flatfile/plugin-zip-extractor';

  const listener = new FlatfileListener();

  // Register the Zip Extractor with debugging enabled
  listener.use(ZipExtractor({ debug: true }));
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { ZipExtractor } from '@flatfile/plugin-zip-extractor';

  const listener = new FlatfileListener();

  // Register the Zip Extractor with debugging enabled
  listener.use(ZipExtractor({ debug: true }));
  ```
</CodeGroup>

### Combined with Other Extractors

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { ZipExtractor } from '@flatfile/plugin-zip-extractor';
  import { XlsxExtractor } from '@flatfile/plugin-xlsx-extractor';

  const listener = new FlatfileListener();

  // First, use the Zip Extractor to decompress any uploaded .zip files.
  listener.use(ZipExtractor());

  // Then, use the XLSX Extractor to process any .xlsx files,
  // including those that were just extracted from a zip archive.
  listener.use(XlsxExtractor());
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { ZipExtractor } from '@flatfile/plugin-zip-extractor';
  import { XlsxExtractor } from '@flatfile/plugin-xlsx-extractor';

  const listener = new FlatfileListener();

  // First, use the Zip Extractor to decompress any uploaded .zip files.
  listener.use(ZipExtractor());

  // Then, use the XLSX Extractor to process any .xlsx files,
  // including those that were just extracted from a zip archive.
  listener.use(XlsxExtractor());
  ```
</CodeGroup>

## Troubleshooting

The primary tool for troubleshooting is the `debug` option. Setting `debug: true` during initialization will cause the plugin to output detailed logs, including the paths of files it is extracting and uploading, which can help diagnose issues with the extraction process.

If an error occurs during the unzipping or file upload process, the plugin will catch the exception, log it, and fail the associated Flatfile Job with the message "Extraction failed" followed by the original error message. This provides clear feedback in the Flatfile UI.

## Notes

### Server-Side Operation

This plugin is intended to be run in a server-side listener environment, not in the browser.

### Event Handling

The plugin operates on the `file:created` event in Flatfile and specifically targets files with a `.zip` extension, ignoring all other file types.

### File Filtering

The plugin automatically filters out certain files from the archive to avoid clutter:

* Files whose names start with a `.` (e.g., `.DS_Store`)
* Files within the `__MACOSX` directory (common in archives created on macOS)

### Job Tracking

The plugin utilizes `@flatfile/plugin-job-handler` to provide feedback on the extraction progress within the Flatfile UI.

### Deprecated Export

The `zipExtractorPlugin` export is deprecated and kept for backward compatibility. Use `ZipExtractor` in all new implementations.
