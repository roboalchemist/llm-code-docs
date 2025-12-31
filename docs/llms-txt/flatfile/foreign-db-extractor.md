# Source: https://flatfile.com/docs/plugins/foreign-db-extractor.md

# Foreign Database Extractor for Microsoft SQL Server

> Automatically extract data from Microsoft SQL Server backup files (.bak) into Flatfile Workbooks for easy data review and processing.

This plugin automates the process of extracting data from a Microsoft SQL Server (MSSQL) database backup file (`.bak`). When a user uploads a `.bak` file to a Flatfile Space, this plugin triggers a multi-step process. First, it uploads the backup file to a secure storage location. Then, it restores the backup to a Flatfile-hosted MSSQL database instance. After the database is restored and available, the plugin inspects its schema to identify all tables. Finally, it creates a read-only Flatfile Workbook where each database table is represented as a separate Sheet. This allows users to view and interact with data from large MSSQL databases directly within the Flatfile UI without needing to manually export data to CSV or Excel first. It is ideal for scenarios where the source of truth is an MSSQL database and users need to bring that data into the Flatfile ecosystem for review or processing.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-foreign-db-extractor
```

## Configuration & Parameters

This plugin does not have any user-configurable options that are passed during initialization. The plugin operates with a default, built-in configuration that automatically listens for `file:created` events. If the uploaded file has a `.bak` extension and is not for export, it initiates a job named 'extract-foreign-mssql-db'. This job handles the entire workflow: creating a workbook, uploading the file to S3, restoring the database, polling for status, generating sheets from the database tables, and linking everything together. The process is entirely self-contained.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { foreignDBExtractor } from '@flatfile/plugin-foreign-db-extractor';

  export default function (listener) {
    // Simply use the plugin
    listener.use(foreignDBExtractor());

    // Add other listeners as needed
  }
  ```

  ```typescript TypeScript
  import type { FlatfileListener } from '@flatfile/listener';
  import { foreignDBExtractor } from '@flatfile/plugin-foreign-db-extractor';

  export default function (listener: FlatfileListener) {
    // Simply use the plugin
    listener.use(foreignDBExtractor());

    // Add other listeners as needed
  }
  ```
</CodeGroup>

### Complete Setup Example

<CodeGroup>
  ```javascript JavaScript
  import { FlatfileListener } from '@flatfile/listener';
  import { foreignDBExtractor } from '@flatfile/plugin-foreign-db-extractor';

  const listener = new FlatfileListener();

  // Register the plugin with the listener instance
  listener.use(foreignDBExtractor());

  // The listener is now configured to handle .bak file extractions
  export default listener;
  ```

  ```typescript TypeScript
  import { FlatfileListener } from '@flatfile/listener';
  import { foreignDBExtractor } from '@flatfile/plugin-foreign-db-extractor';

  const listener = new FlatfileListener();

  // Register the plugin with the listener instance
  listener.use(foreignDBExtractor());

  // The listener is now configured to handle .bak file extractions
  export default listener;
  ```
</CodeGroup>

## API Reference

### foreignDBExtractor()

A factory function that returns a pre-configured plugin for a Flatfile Listener. The returned plugin contains all the necessary logic to listen for `.bak` file uploads and manage the extraction process. This includes creating a corresponding job, restoring the database on a Flatfile-managed service, polling for its availability, generating Sheets from the database tables, and updating the Flatfile Workbook and File entities with the results.

**Parameters:**

* None

**Return Value:**

* `(listener: FlatfileListener) => void` - A function that accepts a FlatfileListener instance and registers the necessary event handlers

**Error Handling:**

The plugin has built-in error handling. If any step in the extraction job fails (e.g., database restore fails, polling times out), the `try...catch` block within the `job:ready` listener will catch the exception. It then updates the associated File status to 'failed' and fails the Job with a descriptive error message, making the failure visible in the Flatfile UI.

<CodeGroup>
  ```javascript JavaScript
  // Error handling is automatic - failures will be visible in the Flatfile UI
  try {
    listener.use(foreignDBExtractor());
  } catch (error) {
    console.error('Plugin registration failed:', error);
  }
  ```

  ```typescript TypeScript
  // Error handling is automatic - failures will be visible in the Flatfile UI
  try {
    listener.use(foreignDBExtractor());
  } catch (error) {
    console.error('Plugin registration failed:', error);
  }
  ```
</CodeGroup>

## Troubleshooting

To troubleshoot issues, check the status and outcome message of the 'extract-foreign-mssql-db' job in the Flatfile dashboard. The error message from the failed step (e.g., "Database restore failed", "Failed to retrieve user credentials", or an error from the API) will be available in the job's `info` field. Common causes of failure could be a corrupted `.bak` file or the database restore process exceeding the built-in timeout.

## Notes

### Requirements

* The `@flatfile/plugin-foreign-db-extractor` and `@flatfile/listener` packages must be installed
* This feature must be enabled for your Flatfile account. Please contact Flatfile support to get access
* The environment where the listener runs must have `AGENT_INTERNAL_URL` and `FLATFILE_BEARER_TOKEN` environment variables set, which are typically provided by the Flatfile platform

### Limitations

* The plugin only activates for files with a `.bak` extension. Other file types are ignored
* The created Workbook and Sheets are read-only representations of the restored database
* The database restore process has a polling timeout of 3 minutes. If the restore takes longer, the job will fail
* The process to retrieve database user credentials has a polling timeout of 50 seconds (10 attempts with a 5-second delay)

### Error Handling Patterns

The primary error handling is centralized in the `job:ready` listener. It uses a `try...catch` block to wrap the entire extraction workflow. Upon catching an error, it uses the Flatfile API to update the status of the associated file and job to reflect the failure:

* `api.files.update(fileId, { status: 'failed' })`
* `api.jobs.fail(jobId, { info: e.message })`

This ensures that failures are clearly communicated to the user through the Flatfile UI. Internal helper functions throw standard `Error` objects with specific messages that are propagated up to this central handler.
