# Source: https://flatfile.com/docs/plugins/rollout.md

# Rollout: Automatic Workbook Updates

> Automatically apply schema changes to existing, live workbooks when a new version of a Flatfile Agent is deployed

The Rollout plugin automates the process of applying schema changes to existing, live workbooks. When a new version of a Flatfile Agent is deployed (triggering `agent:created` or `agent:updated` events), this plugin identifies relevant workbooks and initiates an update process.

Its primary use case is to ensure that all workbooks associated with a particular configuration stay up-to-date with the latest schema definitions without manual intervention. It works by creating a job to apply the new schema via a user-defined `updater` function. After the schema is updated, it cleverly re-triggers all data hooks on all records in the updated sheets, ensuring data validity and transformations are re-evaluated against the new schema.

This plugin should be deployed in a server-side listener.

## Installation

```bash
npm install @flatfile/plugin-rollout
```

## Configuration & Parameters

The rollout plugin accepts a configuration object with the following parameters:

### `namespace` (required)

* **Type:** `string`
* **Description:** A string used to filter which spaces the plugin should operate on. The plugin will only consider spaces matching this namespace. The expected format is typically `workbook:your-namespace`.

### `dev` (required)

* **Type:** `boolean`
* **Description:** When set to `true`, the plugin will also trigger an update check when the agent starts up in a local development environment (i.e., not running on AWS Lambda). This is useful for testing changes locally without needing to deploy a new agent version.
* **Default:** Effectively `false` - updates in local development are suppressed unless this is explicitly set to `true`.

### `updater` (required)

* **Type:** `(space: Flatfile.Space, workbooks: Flatfile.Workbook[]) => Promise<undefined | Flatfile.Workbook[]>`
* **Description:** An asynchronous callback function you provide to perform the actual schema updates. It receives the `space` being processed and a list of its `workbooks`. You are responsible for using the Flatfile API within this function to apply your new schema to the workbooks. The function should return an array of the workbooks that were successfully updated.

## Usage Examples

<CodeGroup>
  ```javascript JavaScript - Basic Usage
  import { FlatfileListener } from '@flatfile/listener'
  import { rollout } from '@flatfile/plugin-rollout'
  import { FlatfileClient } from '@flatfile/api'

  const listener = new FlatfileListener()
  const api = new FlatfileClient()

  const rolloutPlugin = rollout({
    namespace: 'workbook:my-app',
    dev: process.env.NODE_ENV === 'development',
    updater: async (space, workbooks) => {
      // In a real scenario, you would update the workbook's sheets
      // with a new schema configuration here.
      console.log(`Updating workbooks in space ${space.id}`)
      // For example:
      // const newSchema = require('./schemas/my-new-schema')
      // await api.sheets.update(workbooks[0].sheets[0].id, { config: newSchema.config })
      
      // Return the workbooks you updated to re-trigger hooks.
      return workbooks
    },
  })

  // Register the job handler on a filtered listener
  listener.namespace(['workbook:my-app'], (filteredListener) => {
    filteredListener.use(rolloutPlugin)
  })

  // Register the root event handler on the main listener
  // This is required to catch the agent deployment events.
  listener.use(rolloutPlugin.root)
  ```

  ```typescript TypeScript - Basic Usage
  import { FlatfileListener } from '@flatfile/listener'
  import { rollout } from '@flatfile/plugin-rollout'
  import { FlatfileClient } from '@flatfile/api'
  import { Flatfile } from '@flatfile/api'

  const listener = new FlatfileListener()
  const api = new FlatfileClient()

  const rolloutPlugin = rollout({
    namespace: 'workbook:my-app',
    dev: process.env.NODE_ENV === 'development',
    updater: async (space: Flatfile.Space, workbooks: Flatfile.Workbook[]) => {
      // In a real scenario, you would update the workbook's sheets
      // with a new schema configuration here.
      console.log(`Updating workbooks in space ${space.id}`)
      // For example:
      // const newSchema = require('./schemas/my-new-schema')
      // await api.sheets.update(workbooks[0].sheets[0].id, { config: newSchema.config })
      
      // Return the workbooks you updated to re-trigger hooks.
      return workbooks
    },
  })

  // Register the job handler on a filtered listener
  listener.namespace(['workbook:my-app'], (filteredListener) => {
    filteredListener.use(rolloutPlugin)
  })

  // Register the root event handler on the main listener
  // This is required to catch the agent deployment events.
  listener.use(rolloutPlugin.root)
  ```
</CodeGroup>

<CodeGroup>
  ```javascript JavaScript - Advanced Configuration
  import { FlatfileListener } from '@flatfile/listener'
  import { rollout } from '@flatfile/plugin-rollout'
  import { FlatfileClient } from '@flatfile/api'
  import { myNewSheetConfig } from './new-sheet.config'

  const listener = new FlatfileListener()
  const api = new FlatfileClient()

  const rolloutPluginWithConfig = rollout({
    // Only act on spaces with this namespace
    namespace: 'workbook:customer-onboarding',
    
    // Enable local dev updates
    dev: true,
    
    // Provide the logic to update the workbook schemas
    updater: async (space, workbooks) => {
      const updatedWorkbooks = []
      for (const workbook of workbooks) {
        // Assuming we want to update the first sheet of each workbook
        if (workbook.sheets && workbook.sheets.length > 0) {
          const sheetId = workbook.sheets[0].id
          try {
            await api.sheets.update(sheetId, {
              config: myNewSheetConfig,
            })
            console.log(`Successfully updated schema for sheet ${sheetId}`)
            updatedWorkbooks.push(workbook)
          } catch (e) {
            console.error(`Failed to update sheet ${sheetId}:`, e)
          }
        }
      }
      // Return only the workbooks that were successfully updated
      return updatedWorkbooks
    },
  })

  // The plugin returns two parts that must both be registered.
  listener.namespace(['workbook:customer-onboarding'], (filteredListener) => {
    filteredListener.use(rolloutPluginWithConfig)
  })
  listener.use(rolloutPluginWithConfig.root)
  ```

  ```typescript TypeScript - Advanced Configuration
  import { FlatfileListener } from '@flatfile/listener'
  import { rollout } from '@flatfile/plugin-rollout'
  import { FlatfileClient } from '@flatfile/api'
  import { Flatfile } from '@flatfile/api'
  import { myNewSheetConfig } from './new-sheet.config'

  const listener = new FlatfileListener()
  const api = new FlatfileClient()

  const rolloutPluginWithConfig = rollout({
    // Only act on spaces with this namespace
    namespace: 'workbook:customer-onboarding',
    
    // Enable local dev updates
    dev: true,
    
    // Provide the logic to update the workbook schemas
    updater: async (space: Flatfile.Space, workbooks: Flatfile.Workbook[]) => {
      const updatedWorkbooks: Flatfile.Workbook[] = []
      for (const workbook of workbooks) {
        // Assuming we want to update the first sheet of each workbook
        if (workbook.sheets && workbook.sheets.length > 0) {
          const sheetId = workbook.sheets[0].id
          try {
            await api.sheets.update(sheetId, {
              config: myNewSheetConfig,
            })
            console.log(`Successfully updated schema for sheet ${sheetId}`)
            updatedWorkbooks.push(workbook)
          } catch (e) {
            console.error(`Failed to update sheet ${sheetId}:`, e)
          }
        }
      }
      // Return only the workbooks that were successfully updated
      return updatedWorkbooks
    },
  })

  // The plugin returns two parts that must both be registered.
  listener.namespace(['workbook:customer-onboarding'], (filteredListener) => {
    filteredListener.use(rolloutPluginWithConfig)
  })
  listener.use(rolloutPluginWithConfig.root)
  ```
</CodeGroup>

## API Reference

### `rollout(config)`

Initializes the rollout plugin. It sets up listeners for agent deployment events and a job handler to perform the updates. It relies on a user-provided `updater` function to apply the specific schema changes.

**Parameters:**

* `config` (object): Configuration object with the following properties:
  * `namespace` (string, required): The namespace to filter spaces for updates
  * `dev` (boolean, required): Set to `true` to enable updates on local agent reloads
  * `updater` (function, required): Async function that performs the schema update

**Return Value:**
A listener callback function with a `.root` property (also a listener callback). The main callback handles the `space:auto-update` job, while the `.root` callback handles `agent:created` and `agent:updated` events.

<CodeGroup>
  ```javascript JavaScript - Error Handling
  const rolloutWithErrorHandling = rollout({
    namespace: 'workbook:my-app',
    dev: true,
    updater: async (space, workbooks) => {
      const updated = []
      for (const wb of workbooks) {
        try {
          // Attempt to update a sheet
          const sheetId = wb.sheets[0].id
          // ... your api call to update the sheet ...
          console.log(`Updated sheet ${sheetId}`)
          updated.push(wb)
        } catch (error) {
          console.error(`Could not update workbook ${wb.id}. Reason:`, error)
          // Continue to the next workbook without stopping the whole process
        }
      }
      return updated
    },
  })
  ```

  ```typescript TypeScript - Error Handling
  const rolloutWithErrorHandling = rollout({
    namespace: 'workbook:my-app',
    dev: true,
    updater: async (space: Flatfile.Space, workbooks: Flatfile.Workbook[]) => {
      const updated: Flatfile.Workbook[] = []
      for (const wb of workbooks) {
        try {
          // Attempt to update a sheet
          const sheetId = wb.sheets[0].id
          // ... your api call to update the sheet ...
          console.log(`Updated sheet ${sheetId}`)
          updated.push(wb)
        } catch (error) {
          console.error(`Could not update workbook ${wb.id}. Reason:`, error)
          // Continue to the next workbook without stopping the whole process
        }
      }
      return updated
    },
  })
  ```
</CodeGroup>

## Troubleshooting

### Updates not triggering

* Ensure the `agent:created` or `agent:updated` events are firing upon deployment
* Check that the target space has the correct namespace and the required secret (`FF_AUTO_UPDATE` or `FF_AUTO_UPDATE_DEV`) is set to `'true'`

### Local updates not working

* Make sure you have set `dev: true` in the plugin configuration

### Hooks not re-running

* Verify that your `updater` function is returning an array containing the workbooks that you successfully updated
* If an empty or `undefined` value is returned, the hook re-triggering step will be skipped

## Notes

### Default Behavior

By default, the plugin will only trigger updates for production spaces that have a secret named `FF_AUTO_UPDATE` with a value of `'true'`. If the `dev: true` option is used, it will trigger updates for development spaces that have a secret named `FF_AUTO_UPDATE_DEV` with a value of `'true'`. This secret-based mechanism acts as an explicit opt-in for each space, preventing accidental updates.

### Special Considerations

* **Dual Listener Registration:** The plugin returns a function with a `.root` property. You MUST register both. The main function handles the job execution and should be on a namespaced listener. The `.root` function handles the global events that trigger the job and must be on the root listener.
* **Server-Side Only:** This plugin is designed to run in a server-side listener environment, not in the browser.
* **Opt-In via Secrets:** The plugin will not update a space unless it contains a specific secret. For production environments, a secret named `FF_AUTO_UPDATE` must exist with the value `'true'`. For local development (with `dev: true`), the secret must be `FF_AUTO_UPDATE_DEV` with the value `'true'`.
* **Hook Re-triggering:** To re-run data hooks after a schema change, the plugin updates the metadata of every record in the updated sheets by adding a `_autoUpdateKey` with a random UUID. This modification forces Flatfile to re-evaluate each record.

### API Permissions

The agent using this plugin requires API permissions for the following actions:

* `space:read` (for `spaces.list`, `spaces.get`)
* `secret:read` (for `secrets.list`)
* `workbook:read` (for `workbooks.list`)
* `job:write` (for `jobs.create`)
* Your `updater` function will likely require additional permissions, such as `sheet:write` to update sheet configurations.
