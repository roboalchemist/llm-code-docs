# Source: https://flatfile.com/docs/plugins/job-handler.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Job Handler Plugin

> A Flatfile plugin that streamlines the handling of asynchronous Jobs by managing their lifecycle, progress reporting, and completion status.

The Job Handler plugin is designed to streamline the handling of Flatfile Jobs. A Job is a large unit of work performed asynchronously, such as processing a file or configuring a Space. This plugin listens for the `job:ready` event and executes a custom handler function when a matching job is triggered.

Its main purpose is to provide a structured way to manage the lifecycle of a job. It automatically acknowledges the job upon receipt, provides a `tick` function to report progress back to the user, and handles the final completion or failure status. This is useful for any long-running process initiated within Flatfile, allowing developers to focus on the business logic of the task while the plugin manages the communication with the Flatfile API.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-job-handler
```

## Configuration & Parameters

### job

* **Type:** `string | EventFilter`
* **Required:** Yes
* **Description:** A filter to specify which job the listener should handle. This is typically a string in the format "domain:operation", for example, "space:configure" or "workbook:submit".

### handler

* **Type:** `Function`
* **Required:** Yes
* **Description:** An async callback function that contains the logic to be executed for the job. It receives the `event` object and a `tick` function as arguments. Throwing an error within this function will cause the job to fail. If it completes successfully, it can optionally return a `JobCompleteDetails` object to customize the outcome message.

**Function signature:**

```typescript  theme={null}
(event: FlatfileEvent, tick: TickFunction) => Promise<void | Flatfile.JobCompleteDetails>
```

### opts.debug

* **Type:** `boolean`
* **Default:** `false`
* **Description:** An optional parameter to enable detailed logging for the plugin in the console, which is useful for troubleshooting.

### Default Behavior

By default, the plugin listens for the specified `job:ready` event. When triggered, it immediately acknowledges the job with the Flatfile API, setting its status to "Accepted" and progress to 0%. It then executes the user-provided `handler`. If the handler completes without returning a value, the plugin marks the job as complete with a default message "Job complete". If the handler throws an error, the plugin catches it and marks the job as failed, using the error message as the reason.

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';

  const listener = new FlatfileListener();

  listener.use(
    jobHandler('space:configure', async (event, tick) => {
      // Acknowledge the job has started
      await tick(10, 'Starting configuration...');

      // ... your custom logic to configure the space ...
      console.log('Configuring space:', event.context.spaceId);

      // Update progress
      await tick(50, 'Halfway there!');

      // ... more logic ...

      // Job is finished
      await tick(100, 'Configuration complete.');
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';
  import type { FlatfileEvent } from '@flatfile/listener';

  const listener = new FlatfileListener();

  listener.use(
    jobHandler('space:configure', async (event: FlatfileEvent, tick) => {
      // Acknowledge the job has started
      await tick(10, 'Starting configuration...');

      // ... your custom logic to configure the space ...
      console.log('Configuring space:', event.context.spaceId);

      // Update progress
      await tick(50, 'Halfway there!');

      // ... more logic ...

      // Job is finished
      await tick(100, 'Configuration complete.');
    })
  );
  ```
</CodeGroup>

### Configuration with Debug

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';

  const listener = new FlatfileListener();

  // Using the 'opts' parameter to enable debug logging
  listener.use(
    jobHandler(
      'workbook:submit',
      async (event) => {
        console.log('Processing submitted workbook...');
        // ... processing logic ...
      },
      { debug: true }
    )
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';
  import type { FlatfileEvent } from '@flatfile/listener';

  const listener = new FlatfileListener();

  // Using the 'opts' parameter to enable debug logging
  listener.use(
    jobHandler(
      'workbook:submit',
      async (event: FlatfileEvent) => {
        console.log('Processing submitted workbook...');
        // ... processing logic ...
      },
      { debug: true }
    )
  );
  ```
</CodeGroup>

### Advanced Usage with Custom Outcomes

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';

  const listener = new FlatfileListener();

  listener.use(
    jobHandler('file:process', async (event, tick) => {
      try {
        await tick(25, 'Processing file...');
        // ... your processing logic ...

        // Return a custom outcome on success
        return {
          outcome: {
            message: 'File processed successfully. 10 new records created.',
            acknowledge: true,
          },
        };
      } catch (error) {
        console.error('An error occurred:', error);
        // Throwing the error will automatically fail the job
        throw new Error('Failed to process the file.');
      }
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';
  import type { FlatfileEvent } from '@flatfile/listener';
  import type { Flatfile } from '@flatfile/api';

  const listener = new FlatfileListener();

  listener.use(
    jobHandler('file:process', async (event: FlatfileEvent, tick): Promise<Flatfile.JobCompleteDetails> => {
      try {
        await tick(25, 'Processing file...');
        // ... your processing logic ...

        // Return a custom outcome on success
        return {
          outcome: {
            message: 'File processed successfully. 10 new records created.',
            acknowledge: true,
          },
        };
      } catch (error) {
        console.error('An error occurred:', error);
        // Throwing the error will automatically fail the job
        throw new Error('Failed to process the file.');
      }
    })
  );
  ```
</CodeGroup>

### Error Handling Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';

  const listener = new FlatfileListener();

  listener.use(
    jobHandler('data:validate', async (event, tick) => {
      await tick(1, 'Starting validation...');
      const records = await getRecords(event); // Fictional function

      if (records.length === 0) {
        // This will be caught by the plugin and fail the job
        throw new Error('Validation failed: No records found to validate.');
      }

      // ... continue validation ...
    })
  );
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener';
  import { jobHandler } from '@flatfile/plugin-job-handler';
  import type { FlatfileEvent } from '@flatfile/listener';

  const listener = new FlatfileListener();

  listener.use(
    jobHandler('data:validate', async (event: FlatfileEvent, tick) => {
      await tick(1, 'Starting validation...');
      const records = await getRecords(event); // Fictional function

      if (records.length === 0) {
        // This will be caught by the plugin and fail the job
        throw new Error('Validation failed: No records found to validate.');
      }

      // ... continue validation ...
    })
  );
  ```
</CodeGroup>

## Troubleshooting

The main tool for troubleshooting is the `debug` option. Setting `opts.debug = true` when calling `jobHandler` will enable verbose logging from the plugin, showing when a job is received and when it is completed. Fatal errors are logged using `console.error`, which can be monitored in your server logs.

## Notes

### Requirements and Considerations

This plugin is designed to be used within a Flatfile listener environment, such as a Node.js server running the `@flatfile/listener` package. It relies on the Flatfile API to update job statuses, so proper API keys and permissions are required for the environment where the listener is running.

### Error Handling Patterns

The primary error handling pattern is to wrap the logic inside the `handler` function in a `try...catch` block if you need to perform cleanup actions, or to simply `throw` an error to immediately fail the job. The plugin automatically handles the API call to `api.jobs.fail()` when an unhandled exception is thrown from the `handler`.

### Function Signatures

```typescript  theme={null}
function jobHandler(
  job: string | { job: string },
  handler: (event: FlatfileEvent, tick: TickFunction) => Promise<void | Flatfile.JobCompleteDetails>,
  opts?: { debug?: boolean }
): (listener: FlatfileListener) => void

type TickFunction = (progress: number, info?: string) => Promise<Flatfile.JobResponse>
```

### Return Values

* The `jobHandler` function returns a plugin function to be passed to `listener.use()`
* The `handler` function can return either `void` or a `Flatfile.JobCompleteDetails` object
* If `void` is returned, the job is completed with a default success message
* If a `JobCompleteDetails` object is returned, it is used to set a custom outcome for the completed job
* The `tick` function returns a `Promise<Flatfile.JobResponse>` which can be awaited but is not required
