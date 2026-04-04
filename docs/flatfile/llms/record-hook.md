# Source: https://flatfile.com/docs/plugins/record-hook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Record Hook Plugin

> Execute custom logic on individual data records within a Flatfile Sheet with support for validation, transformation, enrichment, and cleaning.

The Record Hook plugin provides a way to execute custom logic on individual data records within a Flatfile Sheet. It works by attaching a listener to the `commit:created` event, which fires when new data is added or existing data is updated.

This plugin is ideal for a variety of use cases, including:

* **Data Validation:** Implementing complex validation rules that go beyond Flatfile's built-in validators, such as checking for valid email formats or ensuring conditional field requirements.
* **Data Transformation:** Modifying data on the fly, like capitalizing names, standardizing formats, or setting default values.
* **Data Enrichment:** Augmenting records with additional information from external sources.
* **Data Cleaning:** Removing whitespace, correcting common typos, or normalizing values.

The plugin offers two main functions: `recordHook` for processing records one-by-one, and `bulkRecordHook` for processing records in batches, which is more efficient for large datasets.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-record-hook
```

## Configuration & Parameters

### recordHook

Processes individual records one at a time. The provided callback function is executed for each record in the commit.

**Parameters:**

* `sheetSlug` (string, required): The slug of the Sheet you want the hook to apply to
* `callback` (function, required): A function that contains your custom logic. It receives the record and the event object as arguments
* `options` (object, optional): Configuration options
  * `concurrency` (number, default: 10): Controls how many individual record handlers can run in parallel
  * `debug` (boolean, default: false): When set to `true`, enables verbose logging to the console

### bulkRecordHook

Processes records in batches (chunks). The provided callback function is executed for each chunk of records.

**Parameters:**

* `sheetSlug` (string, required): The slug of the Sheet you want the hook to apply to
* `callback` (function, required): A function that contains your custom logic. It receives an array of records and the event object as arguments
* `options` (object, optional): Configuration options
  * `chunkSize` (number, default: 10000): Specifies the number of records to process in each batch. Maximum recommended value is 5000
  * `parallel` (number, default: 1): Specifies how many chunks of records to process in parallel
  * `debug` (boolean, default: false): When set to `true`, enables verbose logging to the console

**Default Behavior:**
By default, the plugin processes records for the specified `sheetSlug` after a commit is created. `bulkRecordHook` processes all records in a single chunk sequentially (`parallel: 1`). `recordHook` processes up to 10 records concurrently. Debug logging is disabled.

## Usage Examples

### Basic Single Record Processing

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { recordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener) {
    listener.use(
      recordHook("contacts", (record) => {
        const firstName = record.get("firstName");
        if (firstName) {
          record.set("firstName", firstName.charAt(0).toUpperCase() + firstName.slice(1));
        }
        return record;
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { recordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.use(
      recordHook("contacts", (record) => {
        const firstName = record.get("firstName") as string;
        if (firstName) {
          record.set("firstName", firstName.charAt(0).toUpperCase() + firstName.slice(1));
        }
        return record;
      })
    );
  }
  ```
</CodeGroup>

### Basic Bulk Record Processing

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { bulkRecordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener) {
    listener.use(
      bulkRecordHook("contacts", (records) => {
        records.forEach((record) => {
          const firstName = record.get("firstName");
          if (firstName) {
            record.set("firstName", firstName.charAt(0).toUpperCase() + firstName.slice(1));
          }
        });
        return records;
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { bulkRecordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";
  import { FlatfileRecord } from "@flatfile/hooks";

  export default function (listener: FlatfileListener) {
    listener.use(
      bulkRecordHook("contacts", (records: FlatfileRecord[]) => {
        records.forEach((record) => {
          const firstName = record.get("firstName") as string;
          if (firstName) {
            record.set("firstName", firstName.charAt(0).toUpperCase() + firstName.slice(1));
          }
        });
        return records;
      })
    );
  }
  ```
</CodeGroup>

### Configuration Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { bulkRecordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener) {
    listener.use(
      bulkRecordHook(
        "contacts",
        (records) => {
          // Your processing logic here
          return records;
        },
        { chunkSize: 1000, parallel: 5, debug: true }
      )
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { bulkRecordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";
  import { FlatfileRecord } from "@flatfile/hooks";

  export default function (listener: FlatfileListener) {
    listener.use(
      bulkRecordHook(
        "contacts",
        (records: FlatfileRecord[]) => {
          // Your processing logic here
          return records;
        },
        { chunkSize: 1000, parallel: 5, debug: true }
      )
    );
  }
  ```
</CodeGroup>

### Advanced Usage - Email Validation

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { recordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener) {
    listener.use(
      recordHook("contacts", (record) => {
        const email = record.get("email");
        if (!email) {
          record.addError("email", "Email address is required.");
          return record;
        }

        const validEmailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!validEmailRegex.test(email)) {
          record.addError("email", "Please enter a valid email address.");
        }
        return record;
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { recordHook } from "@flatfile/plugin-record-hook";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.use(
      recordHook("contacts", (record) => {
        const email = record.get("email") as string;
        if (!email) {
          record.addError("email", "Email address is required.");
          return record;
        }

        const validEmailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!validEmailRegex.test(email)) {
          record.addError("email", "Please enter a valid email address.");
        }
        return record;
      })
    );
  }
  ```
</CodeGroup>

## Troubleshooting

The most effective way to troubleshoot issues is to set the `debug: true` option in the plugin configuration. This will print detailed logs to the console, showing the timing and status of each major step: fetching data, running the handler, filtering modified records, and updating records. This can help identify performance bottlenecks or see why records are not being updated as expected.

## Notes

### Special Considerations

* The plugin operates on the `commit:created` event. This means it runs after Flatfile's initial parsing and validation but before the data is finalized.
* To save changes, your callback function **must** return the modified record (for `recordHook`) or the array of modified records (for `bulkRecordHook`). If you return `null`, `undefined`, or nothing, your changes will not be persisted.
* The plugin intelligently detects which records have actually been modified and only sends those records back to the Flatfile API for an update, optimizing performance.

### Limitations

* The `chunkSize` for `bulkRecordHook` has a recommended maximum of 5000 records to ensure stability and performance.

### Error Handling

* The plugin is designed to be robust. It wraps the execution of the user-provided callback in a `try...catch` block.
* If an error is thrown inside your callback, the plugin will log the error message to the console with a `[FATAL]` prefix.
* Crucially, it will then ensure the commit is marked as complete with the Flatfile API, preventing the import process from stalling due to an error in custom code.
