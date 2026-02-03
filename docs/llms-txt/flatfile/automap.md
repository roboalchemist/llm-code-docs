# Source: https://flatfile.com/docs/plugins/automap.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Automap Plugin

> Automatically map columns for headless data import workflows in Flatfile with configurable confidence levels

The Automap plugin is designed for headless data import workflows in Flatfile. Its primary purpose is to automate the column mapping process. The plugin listens for successfully extracted files, and when a matching file is found, it automatically creates and executes a mapping job to a specified destination Sheet.

This is ideal for scenarios where files with consistent schemas are uploaded programmatically, bypassing the need for a user to manually map columns in the UI. The plugin determines whether to proceed with the mapping based on a configurable confidence level, ensuring that only high-quality matches are automated. If the mapping confidence is too low, it can trigger a failure callback for custom notifications or alternative handling.

## Installation

<CodeGroup>
  ```bash npm theme={null}
  npm install @flatfile/plugin-automap
  ```

  ```bash yarn theme={null}
  yarn add @flatfile/plugin-automap
  ```
</CodeGroup>

## Configuration & Parameters

The `automap` function accepts an `AutomapOptions` configuration object with the following parameters:

### Required Parameters

<ParamField path="accuracy" type="'confident' | 'exact'" required>
  Controls the minimum confidence level required for the plugin to automatically execute the mapping job.

  * `'confident'`: All mapped fields must have a confidence level of 'strong' (> 90%) or 'absolute' (100%)
  * `'exact'`: All mapped fields must have a confidence level of 'absolute' (100%)
</ParamField>

### Optional Parameters

<ParamField path="debug" type="boolean" default="false">
  Toggles verbose logging for development and troubleshooting. When true, the plugin will output detailed information about its progress, decisions, and any errors it encounters to the console.
</ParamField>

<ParamField path="defaultTargetSheet" type="string | function">
  Specifies the destination sheet for the imported data.

  * If a string is provided, it must be the exact slug of the target sheet
  * If a function is provided, it receives the uploaded file's name and the event payload, and must return the target sheet slug (or a Promise that resolves to it)
  * **Default behavior**: If not provided, the plugin will not be able to map a single-sheet file automatically unless more advanced logic is implemented by the user
</ParamField>

<ParamField path="matchFilename" type="RegExp">
  A regular expression used to filter which files the plugin should process.

  * **Default behavior**: If not provided, the plugin will attempt to automap every file that is uploaded
  * The plugin will only act on files whose names pass a `test()` against this regex
</ParamField>

<ParamField path="onFailure" type="function">
  A callback function that is executed if the automapping process is aborted due to low mapping confidence.

  * **Default behavior**: Nothing happens on failure, though a warning may be logged if `debug` is true
  * This can be used to trigger notifications (e.g., email, SMS, webhook) to alert a user that manual intervention is required
</ParamField>

<ParamField path="targetWorkbook" type="string">
  Specifies the destination Workbook by its ID or name.

  * **Default behavior**: If not provided, the plugin searches for a suitable workbook in the space. It filters out workbooks associated with raw files (those with a 'file' label). If only one workbook remains, it is chosen. If multiple remain, it will select the one with the 'primary' label.
</ParamField>

<ParamField path="disableFileNameUpdate" type="boolean" default="false">
  Prevents the plugin from updating the name of the processed file in the Flatfile UI.

  * By default, the plugin prepends "⚡️" to the file name on processing and appends the destination sheet name on success to provide visual feedback
  * Setting this to `true` disables this behavior
</ParamField>

## Usage Examples

### Basic Usage

This example shows the simplest way to use the automap plugin, targeting a specific sheet for all uploaded CSV files.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'confident',
        defaultTargetSheet: 'Contacts',
        matchFilename: /\.csv$/,
      })
    );
  });
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'confident',
        defaultTargetSheet: 'Contacts',
        matchFilename: /\.csv$/,
      })
    );
  });
  ```
</CodeGroup>

### Configuration with Failure Handling

This example demonstrates a more complete configuration, including a failure callback and targeting a specific workbook.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'confident',
        defaultTargetSheet: 'Contacts',
        targetWorkbook: 'MyPrimaryWorkbook',
        matchFilename: /^(contacts|people|users)\.csv$/i,
        debug: true,
        onFailure: (event) => {
          console.error(
            `Automap failed for file in space ${event.context.spaceId}. Please map manually.`
          );
          // Add custom logic here, like sending an email or Slack message.
        },
      })
    );
  });
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';
  import type { FlatfileEvent } from '@flatfile/listener';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'confident',
        defaultTargetSheet: 'Contacts',
        targetWorkbook: 'MyPrimaryWorkbook',
        matchFilename: /^(contacts|people|users)\.csv$/i,
        debug: true,
        onFailure: (event: FlatfileEvent) => {
          console.error(
            `Automap failed for file in space ${event.context.spaceId}. Please map manually.`
          );
          // Add custom logic here, like sending an email or Slack message.
        },
      })
    );
  });
  ```
</CodeGroup>

### Dynamic Sheet Targeting

This example uses a function for `defaultTargetSheet` to dynamically route data to different sheets based on the filename.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'exact',
        defaultTargetSheet: (fileName) => {
          if (fileName.includes('invoice')) {
            return 'Invoices';
          } else if (fileName.includes('contact')) {
            return 'Contacts';
          }
          // Return a default or handle cases where no match is found
          return 'DefaultSheet';
        },
        onFailure: (event) => {
          console.log('Automap failed, manual mapping required.');
        },
      })
    );
  });
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';
  import type { FlatfileEvent } from '@flatfile/listener';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'exact',
        defaultTargetSheet: (fileName?: string): string => {
          if (fileName?.includes('invoice')) {
            return 'Invoices';
          } else if (fileName?.includes('contact')) {
            return 'Contacts';
          }
          // Return a default or handle cases where no match is found
          return 'DefaultSheet';
        },
        onFailure: (event: FlatfileEvent) => {
          console.log('Automap failed, manual mapping required.');
        },
      })
    );
  });
  ```
</CodeGroup>

## Troubleshooting

The most effective way to troubleshoot the plugin is to set the `debug: true` option in the configuration. This will provide a step-by-step log of the plugin's execution, including:

* Which files are matched
* What workbooks and sheets are targeted
* The contents of the mapping plan
* The reason for any failures

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'exact',
        defaultTargetSheet: 'Contacts',
        debug: true, // Enable verbose logging
        onFailure: (event) => {
          const { spaceId, fileId } = event.context;
          console.error(
            `Could not automap file ${fileId} with 'exact' accuracy. ` +
            `Please visit space ${spaceId} to map it manually.`
          );
        },
      })
    );
  });
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { automap } from '@flatfile/plugin-automap';
  import type { FlatfileEvent } from '@flatfile/listener';

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      automap({
        accuracy: 'exact',
        defaultTargetSheet: 'Contacts',
        debug: true, // Enable verbose logging
        onFailure: (event: FlatfileEvent) => {
          const { spaceId, fileId } = event.context;
          console.error(
            `Could not automap file ${fileId} with 'exact' accuracy. ` +
            `Please visit space ${spaceId} to map it manually.`
          );
        },
      })
    );
  });
  ```
</CodeGroup>

## Notes

### Default Behavior

* **File processing**: If no `matchFilename` is provided, the plugin will attempt to automap every uploaded file
* **Target sheet**: It is highly recommended to set `defaultTargetSheet` for basic workflows, as the plugin cannot map single-sheet files automatically without it
* **Workbook selection**: When `targetWorkbook` is not specified, the plugin filters out file-associated workbooks and selects the remaining one, or the one with the 'primary' label if multiple exist
* **File naming**: By default, the plugin updates file names with status indicators ("⚡️" during processing, destination sheet name on success)

### Special Considerations

* This plugin is intended for use in a server-side listener, not in the browser
* The plugin relies on two key events: `job:completed:file:extract` to start the process, and `job:updated:workbook:map` to check the mapping plan
* The logic for selecting a `targetWorkbook` works best when there's a clear primary workbook in the space

### Limitations

* The `accuracy` check is all-or-nothing. If even one column mapping does not meet the required confidence level, the entire automatic mapping job is aborted
* The plugin's default behavior works best with single-sheet source files. For multi-sheet source files, you must provide more complex logic
* For internal errors (e.g., API call failures, inability to find a file or workbook), the plugin uses `try/catch` blocks and logs errors to the console, which are more verbose when `debug` is set to `true`

### Error Handling Patterns

The primary pattern for user-defined error handling is the `onFailure` callback, which is triggered when mapping confidence is too low. This allows you to implement custom notification systems or alternative workflows when automatic mapping cannot proceed.
