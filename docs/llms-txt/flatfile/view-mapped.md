# Source: https://flatfile.com/docs/plugins/view-mapped.md

# View Mapped Data Plugin

> Automatically hides unmapped columns after the mapping stage to provide a cleaner data review experience

The View Mapped Data Plugin enhances the user experience during the data import process by automatically modifying the data grid view after users complete the column matching step. It hides all columns in the destination sheet that were not mapped by the user, providing a cleaner and more focused view for data validation.

The primary use case is to simplify the "Review" stage of an import by showing only columns that contain mapped data. This reduces visual clutter and helps users concentrate on the data that will actually be imported. The plugin also includes an option to retain required fields in the view, even if they were not mapped.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-view-mapped
```

## Configuration & Parameters

The plugin accepts an optional configuration object with the following parameter:

### `keepRequiredFields`

* **Type:** `boolean`
* **Default:** `false`
* **Description:** Controls whether fields marked as "required" in the sheet's configuration are kept visible after mapping, even if the user did not map any source data to them.

### Default Behavior

By default, the plugin will hide all unmapped fields, including those that are required. Only fields that the user explicitly mapped will remain visible in the data review step.

## Usage Examples

<CodeGroup>
  ```javascript Basic Usage
  import { FlatfileListener } from '@flatfile/listener'
  import { viewMappedPlugin } from '@flatfile/plugin-view-mapped'

  export default function(listener) {
    listener.use(viewMappedPlugin())
  }
  ```

  ```typescript Basic Usage
  import { FlatfileListener } from '@flatfile/listener'
  import { viewMappedPlugin } from '@flatfile/plugin-view-mapped'

  export default function(listener: FlatfileListener) {
    listener.use(viewMappedPlugin())
  }
  ```
</CodeGroup>

<CodeGroup>
  ```javascript With Configuration
  import { FlatfileListener } from '@flatfile/listener'
  import { viewMappedPlugin } from '@flatfile/plugin-view-mapped'

  export default function(listener) {
    listener.use(viewMappedPlugin({
      keepRequiredFields: true
    }))
  }
  ```

  ```typescript With Configuration
  import { FlatfileListener } from '@flatfile/listener'
  import { viewMappedPlugin } from '@flatfile/plugin-view-mapped'

  export default function(listener: FlatfileListener) {
    listener.use(viewMappedPlugin({
      keepRequiredFields: true
    }))
  }
  ```
</CodeGroup>

<CodeGroup>
  ```javascript Complete Example
  import { FlatfileListener } from '@flatfile/listener'
  import { viewMappedPlugin } from '@flatfile/plugin-view-mapped'

  export default function(listener) {
    // Add the plugin to the listener
    listener.use(viewMappedPlugin({ keepRequiredFields: true }))

    // Define other listeners
    listener.on('**', (event) => {
      // Your other event handlers
    })
  }
  ```

  ```typescript Complete Example
  import { FlatfileListener } from '@flatfile/listener'
  import { viewMappedPlugin } from '@flatfile/plugin-view-mapped'

  export default function(listener: FlatfileListener) {
    // Add the plugin to the listener
    listener.use(viewMappedPlugin({ keepRequiredFields: true }))

    // Define other listeners
    listener.on('**', (event) => {
      // Your other event handlers
    })
  }
  ```
</CodeGroup>

## Troubleshooting

### Error Handling

The plugin includes built-in error handling. If an issue occurs while updating the sheet view, the job will fail and log the error to the console:

```javascript
try {
  // The plugin's internal job handler logic runs here
} catch (error) {
  // If an error occurs, it is logged and a generic error is thrown to the UI
  logError('@flatfile/plugin-view-mapped', JSON.stringify(error, null, 2))
  throw new Error('plugins.viewMapped.error')
}
```

## Notes

### Requirements

* **`trackChanges` Required:** The workbook being processed must have the `trackChanges` setting enabled. The plugin checks for this setting and will abort its operation if it is not enabled. This prevents race conditions between different data processing hooks and the workbook update.

### Behavior Details

* **Foreground Job:** The plugin creates a `foreground` job to update the sheet view. This means the user interface will be blocked with a progress indicator while columns are being hidden, preventing user interaction with a stale view of the data.

* **Commit Synchronization:** The plugin includes logic to wait for all pending sheet commits to complete before attempting to update the workbook's field configuration. This prevents race conditions and ensures data integrity.

### API Reference

#### `viewMappedPlugin(options?: ViewMappedOptions)`

Initializes the View Mapped Data plugin and returns a configured listener that should be passed to `listener.use()`. The plugin listens for the completion of a `workbook:map` job and then creates a new job to update the destination sheet's configuration, hiding any unmapped columns.

**Parameters:**

* `options` (optional): Configuration object with `keepRequiredFields` boolean property

**Returns:** A listener function of type `(listener: FlatfileListener) => void`
