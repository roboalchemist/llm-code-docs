# Source: https://flatfile.com/docs/plugins/space-configure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flatfile Space Configuration Plugin

> Programmatically set up and configure a new Flatfile Space with workbooks, sheets, documents, and metadata from a single configuration object.

The `@flatfile/plugin-space-configure` plugin is designed to programmatically set up and configure a new Flatfile Space. It operates within a server-side listener, typically responding to the 'space:configure' event which is triggered when a new Space is created.

Its primary purpose is to define the entire structure of a Space from a single configuration object. This includes creating one or more Workbooks, defining their Sheets with specific fields and actions, setting Space-level properties like metadata and themes, and adding initial documents such as a welcome guide.

The plugin also includes a secondary utility, `dataChecklistPlugin`, which can automatically generate and maintain a "Data Checklist" document within the Space. This document provides a summary of all the fields and data types defined in the Space's workbooks, serving as a handy reference for users.

This plugin is essential for developers who want to create templatized, repeatable, or dynamically generated Space configurations for their users.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-space-configure
```

## Configuration & Parameters

The `configureSpace` function takes a `setup` object as its primary configuration. This can be a static object or a function that returns an object.

The `setup` object has the following properties:

### workbooks

* **Type:** `Partial<Flatfile.CreateWorkbookConfig>[]`
* **Required:** Yes
* **Description:** An array of workbook configuration objects. Each object defines a workbook to be created in the Space. You can specify its name, sheets, actions, labels, etc. This is the core of the Space's data structure.
* **Default:** There is no default; you must provide at least an empty array `[]`.

### space

* **Type:** `Partial<Flatfile.SpaceConfig>`
* **Required:** No
* **Description:** An object to configure the Space itself. You can set metadata (like themes), the primary workbook ID (though the plugin handles this automatically), and other space-level settings.
* **Default:** The plugin will automatically set the `primaryWorkbookId` to the ID of the first workbook created. Other properties are unset by default.

### documents

* **Type:** `Flatfile.DocumentConfig[]`
* **Required:** No
* **Description:** An array of document configuration objects. Each object creates a document in the Space's sidebar. This is useful for providing welcome text, instructions, or guides.
* **Default:** No documents are created by default.

### config

* **Type:** `object`
* **Required:** No
* **Description:** An object for plugin-specific configurations.
  * `maintainWorkbookOrder` (boolean): If set to `true`, the plugin will configure the Space's sidebar to display the workbooks in the same order they are defined in the `workbooks` array.
* **Default:** `{ maintainWorkbookOrder: false }`

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpace } from '@flatfile/plugin-space-configure'

  export default function (listener) {
    listener.use(
      configureSpace({
        workbooks: [],
        space: {
          metadata: {
            name: 'My Empty Space',
          },
        },
      })
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import type { FlatfileListener } from '@flatfile/listener'
  import { configureSpace } from '@flatfile/plugin-space-configure'

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpace({
        workbooks: [],
        space: {
          metadata: {
            name: 'My Empty Space',
          },
        },
      })
    )
  }
  ```
</CodeGroup>

### Configuration with Workbook and Sheets

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpace } from '@flatfile/plugin-space-configure'

  export default function (listener) {
    listener.use(
      configureSpace({
        workbooks: [
          {
            name: 'My First Workbook',
            sheets: [
              {
                name: 'Contacts',
                slug: 'contacts',
                fields: [
                  { key: 'firstName', type: 'string', label: 'First Name' },
                  { key: 'lastName', type: 'string', label: 'Last Name' },
                  { key: 'email', type: 'string', label: 'Email' },
                ],
              },
            ],
          },
        ],
        space: {
          metadata: {
            theme: {
              root: { primaryColor: 'blue' },
            },
          },
        },
      })
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import type { FlatfileListener } from '@flatfile/listener'
  import { configureSpace } from '@flatfile/plugin-space-configure'

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpace({
        workbooks: [
          {
            name: 'My First Workbook',
            sheets: [
              {
                name: 'Contacts',
                slug: 'contacts',
                fields: [
                  { key: 'firstName', type: 'string', label: 'First Name' },
                  { key: 'lastName', type: 'string', label: 'Last Name' },
                  { key: 'email', type: 'string', label: 'Email' },
                ],
              },
            ],
          },
        ],
        space: {
          metadata: {
            theme: {
              root: { primaryColor: 'blue' },
            },
          },
        },
      })
    )
  }
  ```
</CodeGroup>

### Advanced Usage with Callback

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpace } from '@flatfile/plugin-space-configure'
  import api from '@flatfile/api'

  export default function (listener) {
    listener.use(
      configureSpace(
        {
          workbooks: [
            {
              name: 'Onboarding Workbook',
              sheets: [{ name: 'Contacts', fields: [{ key: 'email', type: 'string' }] }],
            },
          ],
          documents: [
            {
              title: 'Welcome Guide',
              body: '<h1>Welcome!</h1><p>Follow the steps to get started.</p>',
            },
          ],
        },
        async (event, workbookIds, tick) => {
          // This code runs after the Space and Workbooks are created.
          const { spaceId } = event.context
          const workbookId = workbookIds[0]

          await tick(60, 'Callback started')
          console.log(`Space ${spaceId} and Workbook ${workbookId} are ready.`)

          // You can now perform additional API calls, like adding records.
          await api.records.insert(workbookId, [
            { email: { value: 'john.doe@example.com' } },
          ])

          await tick(100, 'Callback complete')
        }
      )
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import type { FlatfileListener } from '@flatfile/listener'
  import { configureSpace } from '@flatfile/plugin-space-configure'
  import api from '@flatfile/api'

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpace(
        {
          workbooks: [
            {
              name: 'Onboarding Workbook',
              sheets: [{ name: 'Contacts', fields: [{ key: 'email', type: 'string' }] }],
            },
          ],
          documents: [
            {
              title: 'Welcome Guide',
              body: '<h1>Welcome!</h1><p>Follow the steps to get started.</p>',
            },
          ],
        },
        async (event, workbookIds, tick) => {
          // This code runs after the Space and Workbooks are created.
          const { spaceId } = event.context
          const workbookId = workbookIds[0]

          await tick(60, 'Callback started')
          console.log(`Space ${spaceId} and Workbook ${workbookId} are ready.`)

          // You can now perform additional API calls, like adding records.
          await api.records.insert(workbookId, [
            { email: { value: 'john.doe@example.com' } },
          ])

          await tick(100, 'Callback complete')
        }
      )
    )
  }
  ```
</CodeGroup>

### Using Data Checklist Plugin

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpace, dataChecklistPlugin } from '@flatfile/plugin-space-configure'

  export default function (listener) {
    // Use configureSpace to set up the initial structure
    listener.use(
      configureSpace({
        workbooks: [{ name: 'Contacts', sheets: [/* ... */] }],
      })
    )

    // Use dataChecklistPlugin to generate a summary document
    // This will run after the workbook is created by configureSpace
    listener.use(dataChecklistPlugin())
  }
  ```

  ```typescript TypeScript theme={null}
  import type { FlatfileListener } from '@flatfile/listener'
  import { configureSpace, dataChecklistPlugin } from '@flatfile/plugin-space-configure'

  export default function (listener: FlatfileListener) {
    // Use configureSpace to set up the initial structure
    listener.use(
      configureSpace({
        workbooks: [{ name: 'Contacts', sheets: [/* ... */] }],
      })
    )

    // Use dataChecklistPlugin to generate a summary document
    // This will run after the workbook is created by configureSpace
    listener.use(dataChecklistPlugin())
  }
  ```
</CodeGroup>

### Error Handling Example

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpace } from '@flatfile/plugin-space-configure'

  export default function (listener) {
    listener.use(
      configureSpace(
        { workbooks: [{ name: 'My Workbook' }] },
        async (event, workbookIds, tick) => {
          try {
            await tick(75, 'Running custom logic');
            // Simulate a failing operation
            throw new Error('Custom API call failed!');
          } catch (e) {
            console.error('Error in callback:', e.message);
            // Rethrow the error to fail the job
            throw e;
          }
        }
      )
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import type { FlatfileListener } from '@flatfile/listener'
  import { configureSpace } from '@flatfile/plugin-space-configure'

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpace(
        { workbooks: [{ name: 'My Workbook' }] },
        async (event, workbookIds, tick) => {
          try {
            await tick(75, 'Running custom logic');
            // Simulate a failing operation
            throw new Error('Custom API call failed!');
          } catch (e) {
            console.error('Error in callback:', e.message);
            // Rethrow the error to fail the job
            throw e;
          }
        }
      )
    )
  }
  ```
</CodeGroup>

## API Reference

### configureSpace(setupFactory, callback)

Creates a Flatfile listener plugin that listens for the `job:ready` event with the topic `space:configure`. When triggered, it configures the Space according to the provided setup. It handles creating workbooks, updating the space with a primary workbook, and creating documents.

**Parameters:**

1. `setupFactory`: `Setup | (event: FlatfileEvent) => Setup | Promise<Setup>`
   * The configuration for the space. This can be a static object or an async function that receives the event context and returns a configuration object.

2. `callback`: `(event: FlatfileEvent, workbookIds: string[], tick: TickFunction) => any | Promise<any>` (Optional)
   * An optional async function that is executed after the space and workbooks have been successfully configured. The job progress will be at 50% when the callback is invoked.
   * `event`: The original FlatfileEvent that triggered the job.
   * `workbookIds`: An array of strings containing the IDs of the workbooks that were created.
   * `tick`: A function to update the job's progress percentage and message.

**Returns:** `(listener: FlatfileListener) => void`

### dataChecklistPlugin()

A utility plugin that creates and maintains a "Data Checklist" document in a Space. It listens for `workbook:created` and `workbook:updated` events, then inspects all workbooks and sheets to generate an HTML document summarizing the data model.

**Parameters:** None

**Returns:** `(listener: FlatfileListener) => void`

## Troubleshooting

If a Space fails to configure, check the "Jobs" log in the Flatfile Dashboard for the specific Space. The `space:configure` job will show an error message detailing what went wrong.

Common issues include:

* Malformed configuration objects (e.g., incorrect field types in a sheet definition)
* API permission errors - ensure your agent has the necessary permissions to create workbooks, documents, and update spaces

## Notes

### Special Considerations

* This plugin is designed to be used in a server-side listener environment
* The `configureSpace` plugin is specifically tied to the `space:configure` job topic. It will not run on other events
* The `dataChecklistPlugin` listens for `workbook:created` and `workbook:updated` events. It will automatically update its document if you add or change workbooks in the Space after the initial configuration

### Error Handling Patterns

* The plugin is built on top of `@flatfile/plugin-job-handler`, which provides robust job management. If any of the API calls made by the plugin fail, the job handler will catch the error, mark the job as 'failed', and provide the error message in the Flatfile UI
* For custom logic inside the optional `callback` function, you are responsible for your own error handling. It is best practice to use `try/catch` blocks. If you rethrow an error from the callback, the job will be marked as 'failed'

### Default Behavior

* The plugin will automatically set the `primaryWorkbookId` to the ID of the first workbook created
* Workbooks are displayed in the sidebar in the order they are created unless `maintainWorkbookOrder` is set to `true`
* No documents are created by default unless specified in the configuration
