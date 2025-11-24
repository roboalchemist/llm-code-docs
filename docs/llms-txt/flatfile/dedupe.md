# Source: https://flatfile.com/docs/plugins/dedupe.md

# Deduplicate Sheet Records

> A Flatfile plugin that provides functionality to find and remove duplicate records from a sheet based on specified field values or custom logic.

The Dedupe plugin provides functionality to find and remove duplicate records from a sheet within Flatfile. It is designed to be used as a server-side listener that is triggered by a custom action configured on a specific sheet.

The primary use case is data cleaning. For example, when importing a list of contacts, you can use this plugin to automatically remove entries that have the same email address. The plugin is flexible, allowing you to specify which field to check for duplicates (e.g., 'email', 'orderId'). You can configure it to keep either the first or the last occurrence of a duplicate record. For more complex deduplication logic, you can provide your own custom function.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-dedupe
```

## Configuration & Parameters

The `dedupePlugin` function takes two parameters:

### Parameters

* **jobOperation** (string, required): The operation name that you define in a Sheet-level action. The plugin will only run when an action with this exact operation name is triggered.
* **opts** (PluginOptions, required): An object containing the configuration options for the plugin.

### Configuration Options

| Option   | Type              | Default   | Description                                                                                                                                                     |
| -------- | ----------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `on`     | string            | undefined | The field key (e.g., 'email') to check for duplicate values. Required when using the `keep` option.                                                             |
| `keep`   | 'first' \| 'last' | undefined | Determines which record to keep when a duplicate is found. 'first' keeps the first record encountered, 'last' keeps the last record encountered.                |
| `custom` | function          | undefined | A custom function that receives a batch of records and a set of unique values. Should return an array of record IDs to be deleted. Overrides the `keep` option. |
| `debug`  | boolean           | false     | When set to `true`, the plugin may output additional logging for development and debugging purposes.                                                            |

### Default Behavior

By default, without any configuration in the `opts` object, the plugin will not perform any deduplication. You must provide either the `keep` and `on` options or a `custom` function for the plugin to work. If the `keep` option is used, the `on` option becomes mandatory.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "./listener-instance"; // Your listener instance
  import { dedupePlugin } from "@flatfile/plugin-dedupe";

  listener.use(
    dedupePlugin("dedupe-email", {
      on: "email",
      keep: "last",
    })
  );

  // You also need to configure the action on your Sheet
  /*
  const contactsSheet = {
    name: 'Contacts',
    // ... other fields
    actions: [
      {
        operation: "dedupe-email",
        mode: "background",
        label: "Dedupe emails",
        description: "Remove duplicate emails"
      }
    ]
  }
  */
  ```

  ```typescript TypeScript
  import { listener } from "./listener-instance"; // Your listener instance
  import { dedupePlugin } from "@flatfile/plugin-dedupe";
  import { Flatfile } from "@flatfile/api";

  listener.use(
    dedupePlugin("dedupe-email", {
      on: "email",
      keep: "last",
    })
  );

  // You also need to configure the action on your Sheet
  /*
  const contactsSheet: Flatfile.SheetConfig = {
    name: 'Contacts',
    // ... other fields
    actions: [
      {
        operation: "dedupe-email",
        mode: "background",
        label: "Dedupe emails",
        description: "Remove duplicate emails"
      }
    ]
  }
  */
  ```
</CodeGroup>

This example configures the plugin to trigger when a sheet action with the operation "dedupe-email" is clicked. It will find duplicates in the 'email' field and keep the last record found, deleting any previous ones.

### Custom Deduplication Logic

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "./listener-instance"; // Your listener instance
  import { dedupePlugin } from "@flatfile/plugin-dedupe";

  listener.use(
    dedupePlugin("dedupe-email", {
      custom: (records) => {
        const uniques = new Set();
        const toDelete = [];

        records.forEach(record => {
          const emailValue = record.values["email"]?.value;
          if (emailValue) {
            if (uniques.has(emailValue)) {
              toDelete.push(record.id);
            } else {
              uniques.add(emailValue);
            }
          }
        });

        return toDelete;
      },
    })
  );
  ```

  ```typescript TypeScript
  import { listener } from "./listener-instance"; // Your listener instance
  import { dedupePlugin } from "@flatfile/plugin-dedupe";
  import { Flatfile } from "@flatfile/api";

  listener.use(
    dedupePlugin("dedupe-email", {
      custom: (records: Flatfile.RecordsWithLinks) => {
        const uniques = new Set();
        const toDelete: string[] = [];

        records.forEach(record => {
          const emailValue = record.values["email"]?.value;
          if (emailValue) {
            if (uniques.has(emailValue)) {
              toDelete.push(record.id);
            } else {
              uniques.add(emailValue);
            }
          }
        });

        return toDelete;
      },
    })
  );
  ```
</CodeGroup>

This example shows how to use a custom function for more complex deduplication logic. The custom function identifies records to delete based on the 'email' field and returns their IDs.

### Keep First Record

<CodeGroup>
  ```javascript JavaScript
  import { dedupePlugin } from "@flatfile/plugin-dedupe";

  listener.use(
    dedupePlugin("dedupe:contacts-email", {
      on: "email",
      keep: "first",
    })
  );
  ```

  ```typescript TypeScript
  import { dedupePlugin } from "@flatfile/plugin-dedupe";

  listener.use(
    dedupePlugin("dedupe:contacts-email", {
      on: "email",
      keep: "first",
    })
  );
  ```
</CodeGroup>

This example keeps the first record encountered for each unique email value and deletes subsequent duplicates.

## Troubleshooting

### Common Issues

**Plugin Not Triggering**

* Check for a mismatch between the `jobOperation` string in your listener code and the `operation` value in your Sheet configuration's action. They must be identical.

**Incorrect Field Error**

* Ensure the field key passed to the `on` option exists in your Sheet configuration and is spelled correctly.

**No Duplicates Removed**

* Verify your data to ensure duplicates actually exist for the specified `on` field.
* If using a `custom` function, add logging to debug its logic.

### Error Scenarios

The plugin will throw descriptive errors for common misconfigurations:

* **Missing `on` option**: `Error: \`on\` is required when \`keep\` is first\`
* **Field not found**: `Error: Field "non_existent_field" not found`
* **Invalid context**: `Error: Dedupe must be called from a sheet-level action`

## Notes

### Requirements and Limitations

* **Server-Side Requirement**: This plugin must be deployed in a server-side listener. It is not intended for client-side use.
* **Sheet Action Requirement**: The plugin is triggered by a job. To trigger this job, you must configure a Sheet-level action in your Sheet configuration. The `operation` property of this action must exactly match the `jobOperation` string passed to the `dedupePlugin` function.
* **Large Dataset Limitation**: The `keep: 'last'` option may not function as expected on very large datasets where duplicate records are spread across different pages of data. The `keep: 'first'` option is generally more reliable for large datasets as it correctly tracks unique values across all pages. For a reliable "keep last" implementation on large datasets, a `custom` function should be used.

### Error Handling

The plugin is wrapped in the `jobHandler` utility, which provides standardized job management. Any error thrown during the dedupe function's execution will be caught, and the job will be marked as 'failed' with the corresponding error message. The plugin also performs its own configuration checks and will throw descriptive errors for common misconfigurations.
