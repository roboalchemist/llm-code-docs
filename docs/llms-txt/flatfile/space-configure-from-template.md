# Source: https://flatfile.com/docs/plugins/space-configure-from-template.md

# Space Configure from Template

> Automatically configure new Flatfile Spaces by cloning an existing Space Template, including workbooks, documents, and settings.

This plugin automates the setup of a new Flatfile Space by cloning an existing Space Template. It listens for the `space:configure` event, which is triggered when a new Space is created. Upon activation, the plugin finds the oldest Space Template associated with the current Flatfile App, and then copies its workbooks, documents, and settings (including metadata, actions, labels, etc.) into the new Space.

This is particularly useful for scenarios where you need to consistently provision new Spaces with a predefined structure and configuration, ensuring a uniform starting point for all users. It should be deployed in a server-side listener.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-space-configure-from-template
```

## Configuration & Parameters

The plugin is configured through a single optional parameter passed to the `configureSpaceFromTemplate` function.

### Parameters

| Parameter  | Type                  | Description                                                                                                                                                                                                                       | Default                      |
| ---------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `callback` | `Function` (optional) | An asynchronous function executed after the Space and its Workbooks have been successfully created from the template. Receives the original `event`, an array of the new `workbookIds`, and a `tick` function to report progress. | No additional logic executed |

#### Callback Function Signature

```typescript
(event: FlatfileEvent, workbookIds: string[], tick: TickFunction) => any | Promise<any>
```

* `event`: The FlatfileEvent object that triggered the job
* `workbookIds`: An array of strings, where each string is the ID of a workbook created in the new Space
* `tick`: A function to update the job's progress with signature `(progress: number, message?: string) => Promise<void>`

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { configureSpaceFromTemplate } from "@flatfile/plugin-space-configure-from-template";

  export default function (listener) {
    listener.use(configureSpaceFromTemplate());
  }
  ```

  ```typescript TypeScript
  import { configureSpaceFromTemplate } from "@flatfile/plugin-space-configure-from-template";
  import type { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.use(configureSpaceFromTemplate());
  }
  ```
</CodeGroup>

### Usage with Callback

<CodeGroup>
  ```javascript JavaScript
  import { configureSpaceFromTemplate } from "@flatfile/plugin-space-configure-from-template";

  export default function (listener) {
    listener.use(
      configureSpaceFromTemplate(
        async (event, workbookIds, tick) => {
          const { spaceId } = event.context;
          
          // Report progress
          await tick(60, "Callback started.");

          // Example: Log the IDs of the newly created workbooks
          console.log(`Space ${spaceId} configured with workbooks: ${workbookIds.join(', ')}`);

          // Perform other custom actions here...

          await tick(99, "Callback complete!");
        }
      )
    );
  }
  ```

  ```typescript TypeScript
  import type { FlatfileListener } from "@flatfile/listener";
  import { configureSpaceFromTemplate } from "@flatfile/plugin-space-configure-from-template";

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpaceFromTemplate(
        async (event, workbookIds, tick) => {
          const { spaceId } = event.context;
          
          // Report progress
          await tick(60, "Callback started.");

          // Example: Log the IDs of the newly created workbooks
          console.log(`Space ${spaceId} configured with workbooks: ${workbookIds.join(', ')}`);

          // Perform other custom actions here...

          await tick(99, "Callback complete!");
        }
      )
    );
  }
  ```
</CodeGroup>

## Troubleshooting

### Common Errors

**"Space configuration failed"**

* Check the logs of your listener for a more detailed error message
* This could be due to missing API permissions, network issues, or the absence of a Space Template in your App

**"No space template found"**

* This error occurs if the plugin cannot find any Space Templates associated with the `appId` from the event context
* Ensure you have at least one Space configured as a template for the App you are using

## Notes

### Default Behavior

If no callback is provided, the plugin will configure the Space from the template and mark the job as complete. No additional custom logic is executed. When a callback is provided, it is invoked after the space configuration is complete, with the job's progress at 50%.

### Important Considerations

* **Deployment Environment**: This plugin must be deployed in a server-side listener environment, as it makes direct calls to the Flatfile API
* **Template Selection Logic**: The plugin automatically selects the oldest Space Template associated with the App (sorted by `createdAt` date). It is not possible to specify which template to use if multiple exist. The first one created will always be chosen
* **Permissions**: The agent or token used by the listener must have sufficient permissions to perform the following API actions: `spaces:list`, `spaces:update`, `workbooks:list`, `workbooks:create`, `documents:list`, and `documents:create`
* **Idempotency**: The plugin operates on the `space:configure` event, which typically runs only once for a given Space. Re-running the job may lead to duplicate workbooks or unexpected behavior

### Error Handling

Errors are caught within the `jobHandler`. A generic error is thrown to fail the job, and the specific error is logged to the server console for debugging. There is no built-in mechanism for custom error handling; failures are managed by the Flatfile Job system.
