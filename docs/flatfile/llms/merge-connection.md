# Source: https://flatfile.com/docs/plugins/merge-connection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Merge.dev Connection Plugin

> Connect Flatfile to the Merge.dev unified API platform to sync data from hundreds of third-party integrations including HRIS, ATS, CRM, and Accounting systems.

The Merge.dev Connection Plugin enables users to sync data from hundreds of third-party integrations directly into Flatfile through the Merge.dev unified API platform. When a user establishes a connection to a service via Merge within the Flatfile UI, the plugin automatically creates a new Flatfile Workbook with a schema that matches the data models for that integration. The plugin performs an initial data sync and allows users to manually trigger full data refreshes at any time.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-connect-via-merge
```

## Configuration & Parameters

This plugin is configured through Flatfile Secrets rather than code-based options.

### Required Secret

<ParamField path="MERGE_ACCESS_KEY" type="Secret (String)" required>
  Your API key from your Merge.dev account. This secret must be created in your Flatfile Space and is used to authenticate with the Merge API for token exchange, schema fetching, and data synchronization.

  **Default Behavior:** If the `MERGE_ACCESS_KEY` secret is not present or invalid, the plugin will fail during workbook creation or data sync, resulting in a failed Flatfile Job with an error message indicating the missing key.
</ParamField>

### Function Signature

The plugin exports a single function:

```typescript  theme={null}
mergePlugin(): (listener: FlatfileListener) => void
```

**Parameters:** None

**Returns:** A function that registers job handlers with the Flatfile listener for:

* `space:createConnectedWorkbook`: Creates workbooks based on Merge schemas
* `workbook:syncConnectedWorkbook`: Syncs data from connected services

## Usage Examples

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { mergePlugin } from "@flatfile/plugin-connect-via-merge";

  export default function (listener) {
    // Add the Merge.dev plugin to the listener
    listener.use(mergePlugin());
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { mergePlugin } from "@flatfile/plugin-connect-via-merge";

  export default function (listener: FlatfileListener) {
    // Add the Merge.dev plugin to the listener
    listener.use(mergePlugin());
  }
  ```
</CodeGroup>

### Complete Setup Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { mergePlugin } from "@flatfile/plugin-connect-via-merge";

  export default function (listener) {
    // Register the Merge.dev plugin handlers
    listener.use(mergePlugin());

    // Add other listeners as needed
    listener.on('**', (event) => {
      console.log(`Event received: ${event.topic}`);
    });
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { mergePlugin } from "@flatfile/plugin-connect-via-merge";

  export default function (listener: FlatfileListener) {
    // Register the Merge.dev plugin handlers
    listener.use(mergePlugin());

    // Add other listeners as needed
    listener.on('**', (event) => {
      console.log(`Event received: ${event.topic}`);
    });
  }
  ```
</CodeGroup>

### Configuration Setup

1. **Create the Secret:** In your Flatfile Space settings, create a new Secret with the name `MERGE_ACCESS_KEY` and your Merge.dev API key as the value.

2. **Use the Plugin:** The plugin automatically looks for the `MERGE_ACCESS_KEY` secret in the Space where it's running.

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { mergePlugin } from "@flatfile/plugin-connect-via-merge";

  export default function (listener) {
    // The plugin automatically uses the 'MERGE_ACCESS_KEY' secret
    listener.use(mergePlugin());
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from "@flatfile/listener";
  import { mergePlugin } from "@flatfile/plugin-connect-via-merge";

  export default function (listener: FlatfileListener) {
    // The plugin automatically uses the 'MERGE_ACCESS_KEY' secret
    listener.use(mergePlugin());
  }
  ```
</CodeGroup>

## Troubleshooting

### Missing API Key Error

If you encounter errors related to missing Merge API keys, ensure that:

1. The `MERGE_ACCESS_KEY` secret is properly set in your Flatfile Space
2. The API key value is correct and active in your Merge.dev account

### Sync Timeout Issues

If sync operations timeout, the plugin polls Merge.dev for up to 5 minutes (30 attempts at 10-second intervals). If Merge doesn't complete its sync within this window, the job will fail with a timeout error.

### Job Failures

Check the Flatfile Job logs in your dashboard for specific error messages. The plugin provides descriptive error messages for common issues like missing credentials or API failures.

## Notes

### Prerequisites

* The `connections` feature flag must be enabled for your Flatfile account (contact [support@flatfile.com](mailto:support@flatfile.com))
* Active Merge.dev account required
* `MERGE_ACCESS_KEY` secret must be configured in your Flatfile Space

### Alpha Release Warning

This plugin is an alpha release. Functionality and APIs may change in future versions.

### Data Sync Behavior

* Each sync performs a **full refresh** of data
* All existing records are deleted before inserting current data
* Manual changes made in Flatfile will be overwritten on next sync
* This ensures data consistency with the source system

### Automatic Secret Management

The plugin automatically creates workbook-specific secrets named `<workbookId>:MERGE_X_ACCOUNT_TOKEN` to store account tokens for each connection. These are managed internally by the plugin.

### Error Handling Pattern

The plugin uses centralized error handling that:

* Logs original errors to the console for debugging
* Throws user-friendly error messages displayed in the Flatfile UI
* Causes failed jobs to show descriptive error messages in the dashboard

### Manual Sync Actions

After initial setup, the plugin automatically adds a "Sync" action to connected workbooks. Users can trigger this action from the Flatfile UI to refresh data without additional code.
