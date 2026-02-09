# Source: https://flatfile.com/docs/plugins/yaml-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# YAML Schema to Flatfile Blueprint Converter

> Automates the creation of a Flatfile Blueprint (Workbook and Sheets) from one or more YAML schema definitions, streamlining the setup of a Flatfile Space by converting existing data models into a Flatfile-compatible format.

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-convert-yaml-schema
```

## Configuration & Parameters

### ModelToSheetConfig

Configuration object for each Sheet to be created from a YAML schema:

| Parameter             | Type   | Required | Description                                                                                      |
| --------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------ |
| `sourceUrl`           | string | Yes      | The URL where the YAML schema file is hosted                                                     |
| `name`                | string | No       | A custom name for the generated Sheet. If not provided, the `title` from the YAML schema is used |
| Additional properties | -      | No       | Other `Flatfile.SheetConfig` properties (e.g., `actions`) can be included to customize the Sheet |

### Options

Optional configuration object for the Workbook and plugin behavior:

| Parameter        | Type                  | Default | Description                                                                            |
| ---------------- | --------------------- | ------- | -------------------------------------------------------------------------------------- |
| `workbookConfig` | PartialWorkbookConfig | -       | Configuration for the generated Workbook (name, actions, etc.)                         |
| `debug`          | boolean               | `false` | When set to `true`, prints the generated Blueprint configuration object to the console |

### PartialWorkbookConfig

Configuration for the parent Workbook:

| Parameter             | Type   | Description                                                                      |
| --------------------- | ------ | -------------------------------------------------------------------------------- |
| `name`                | string | Custom name for the Workbook. Defaults to "YAML Schema Workbook" if not provided |
| `actions`             | array  | Custom actions for the Workbook                                                  |
| Additional properties | -      | Other properties from `Flatfile.CreateWorkbookConfig`                            |

### Callback Function

Optional function executed after Space and Workbook configuration:

```typescript  theme={null}
(event: FlatfileEvent, workbookIds: string[], tick: TickFunction) => any | Promise<any>
```

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceWithYamlSchema } from '@flatfile/plugin-convert-yaml-schema'

  export default function (listener) {
    listener.use(
      configureSpaceWithYamlSchema([
        { sourceUrl: 'http://example.com/schemas/my-schema.yml' },
      ])
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceWithYamlSchema } from '@flatfile/plugin-convert-yaml-schema'

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpaceWithYamlSchema([
        { sourceUrl: 'http://example.com/schemas/my-schema.yml' },
      ])
    )
  }
  ```
</CodeGroup>

### Advanced Configuration

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceWithYamlSchema } from '@flatfile/plugin-convert-yaml-schema'

  export default function (listener) {
    listener.use(
      configureSpaceWithYamlSchema(
        [
          {
            sourceUrl: 'https://example.com/schemas/person.yml',
            name: 'Custom Person Sheet',
          },
          {
            sourceUrl: 'https://example.com/schemas/product.yml',
          },
        ],
        {
          workbookConfig: {
            name: 'My Custom Workbook',
            actions: [
              {
                operation: 'submitActionFg',
                mode: 'foreground',
                label: 'Submit all data',
                primary: true,
              },
            ],
          },
          debug: true,
        }
      )
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import {
    configureSpaceWithYamlSchema,
    ModelToSheetConfig,
    PartialWorkbookConfig,
  } from '@flatfile/plugin-convert-yaml-schema'

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpaceWithYamlSchema(
        [
          {
            sourceUrl: 'https://example.com/schemas/person.yml',
            name: 'Custom Person Sheet',
          },
          {
            sourceUrl: 'https://example.com/schemas/product.yml',
          },
        ] as ModelToSheetConfig[],
        {
          workbookConfig: {
            name: 'My Custom Workbook',
            actions: [
              {
                operation: 'submitActionFg',
                mode: 'foreground',
                label: 'Submit all data',
                primary: true,
              },
            ],
          } as PartialWorkbookConfig,
          debug: true,
        }
      )
    )
  }
  ```
</CodeGroup>

### Using Callback Function

<CodeGroup>
  ```javascript JavaScript theme={null}
  import api from '@flatfile/api'
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceWithYamlSchema } from '@flatfile/plugin-convert-yaml-schema'

  export default function (listener) {
    const callback = async (event, workbookIds, tick) => {
      const { spaceId } = event.context
      await tick(50, 'Workbook configured, creating welcome document...')
      await api.documents.create(spaceId, {
        title: 'Getting Started',
        body: '<h1>Welcome!</h1><p>Your data templates are ready.</p>',
      })
      await tick(100, 'Document created')
    }

    listener.use(
      configureSpaceWithYamlSchema(
        [{ sourceUrl: 'https://example.com/schemas/person.yml' }],
        { debug: true },
        callback
      )
    )
  }
  ```

  ```typescript TypeScript theme={null}
  import api from '@flatfile/api'
  import { FlatfileEvent, FlatfileListener } from '@flatfile/listener'
  import { TickFunction } from '@flatfile/plugin-job-handler'
  import { configureSpaceWithYamlSchema } from '@flatfile/plugin-convert-yaml-schema'

  export default function (listener: FlatfileListener) {
    const callback = async (
      event: FlatfileEvent,
      workbookIds: string[],
      tick: TickFunction
    ) => {
      const { spaceId } = event.context
      await tick(50, 'Workbook configured, creating welcome document...')
      await api.documents.create(spaceId, {
        title: 'Getting Started',
        body: '<h1>Welcome!</h1><p>Your data templates are ready.</p>',
      })
      await tick(100, 'Document created')
    }

    listener.use(
      configureSpaceWithYamlSchema(
        [{ sourceUrl: 'https://example.com/schemas/person.yml' }],
        { debug: true },
        callback
      )
    )
  }
  ```
</CodeGroup>

## Troubleshooting

### Debug Mode

The most effective troubleshooting tool is the `debug: true` option. When enabled, the complete generated Blueprint object is printed to the console where the listener is running. This allows you to inspect the exact Workbook, Sheet, and Field configuration that the plugin produced.

```javascript  theme={null}
listener.use(
  configureSpaceWithYamlSchema(
    [{ sourceUrl: 'https://example.com/schemas/person.yml' }],
    { debug: true }
  )
)
```

### Common Error Scenarios

**Network/URL Issues**: If the plugin fails to fetch a schema from a `sourceUrl` (e.g., due to a network error, 404 Not Found, or invalid URL), it will throw an error with a message like:

Error: Error fetching external reference: API returned status 404: Not Found

**YAML Parsing Errors**: Errors during YAML parsing will bubble up and cause the configuration to fail. Ensure your YAML schema files are valid and properly formatted.

## Notes

### Requirements and Limitations

* This plugin must be used in a server-side listener environment
* It is designed to run on the `space:configure` event
* The YAML schema must be publicly accessible via the provided `sourceUrl`
* The plugin internally converts YAML to JSON and uses `@flatfile/plugin-convert-json-schema`, so supported YAML schema features are limited to what the underlying JSON Schema converter supports

### Default Behavior

* If no `name` is provided for a Sheet, the `title` from the YAML schema is used
* If no `name` is provided for the Workbook, it defaults to "YAML Schema Workbook"
* The `debug` option defaults to `false`

### Error Handling

The plugin's external fetching logic includes error handling for network failures and HTTP errors. When errors occur, they are caught by the Flatfile listener runner and reported in the corresponding Job's execution history.
