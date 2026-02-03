# Source: https://flatfile.com/docs/plugins/graphql-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GraphQL Schema to Flatfile Blueprint Converter

> Automatically generate Flatfile Space configurations by converting GraphQL schemas into Workbooks and Sheets, streamlining data import setup for GraphQL APIs.

This plugin automates the creation of a Flatfile Space configuration by converting a GraphQL schema into a Flatfile Blueprint. It introspects a given GraphQL source—which can be a live endpoint URL, a static Schema Definition Language (SDL) string, or a GraphQL.js schema object—and generates corresponding Workbooks and Sheets.

The primary purpose is to significantly speed up the setup process for developers who need to import data that conforms to an existing GraphQL API. It maps GraphQL object types to Flatfile Sheets and their fields to Flatfile Fields, automatically handling scalar types, object relationships (as reference fields), and non-null constraints.

**Use cases include:**

* Rapidly scaffolding a data importer for a headless CMS or backend service that exposes a GraphQL API
* Creating a consistent data onboarding experience based on a single source of truth (the GraphQL schema)
* Migrating data from other systems into an application with a GraphQL-based data model

## Installation

Install the plugin using npm:

```bash  theme={null}
npm install @flatfile/plugin-graphql-schema
```

## Configuration & Parameters

The plugin is configured via a `setupFactory` object passed to the `configureSpaceGraphQL` function.

### Main Configuration

| Parameter   | Type                      | Required | Description                                                                  |
| ----------- | ------------------------- | -------- | ---------------------------------------------------------------------------- |
| `workbooks` | `PartialWorkbookConfig[]` | Yes      | Array of workbook configuration objects. Each object generates one workbook. |
| `space`     | `object`                  | No       | Configuration for the Space itself (e.g., metadata, themes).                 |
| `documents` | `object[]`                | No       | Array of document configurations to add to the Space.                        |

### PartialWorkbookConfig

| Parameter | Type                                  | Default              | Description                                                                                                   |
| --------- | ------------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------- |
| `source`  | `string \| GraphQLSchema \| function` | Required             | GraphQL schema source - can be a URL, SDL string, GraphQLSchema object, or function returning a GraphQLSchema |
| `sheets`  | `PartialSheetConfig[]`                | `undefined`          | Optional array to filter and customize generated sheets                                                       |
| `name`    | `string`                              | `'GraphQL Workbook'` | User-friendly name for the workbook                                                                           |

### PartialSheetConfig

| Parameter | Type     | Default                              | Description                                           |
| --------- | -------- | ------------------------------------ | ----------------------------------------------------- |
| `slug`    | `string` | Required                             | Sheet slug that must match a GraphQL object type name |
| `name`    | `string` | `capitalCase` of GraphQL object name | User-friendly name for the sheet                      |

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'

  const listener = FlatfileListener.create((listener) => {
    listener.on('**', (event) => {
      console.log(`Event: ${event.topic}`)
    })

    listener.use(
      configureSpaceGraphQL({
        workbooks: [
          {
            name: 'SpaceX Launches',
            source: 'https://spacex-production.up.railway.app/',
          },
        ],
      })
    )
  })
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'

  const listener = FlatfileListener.create((listener) => {
    listener.on('**', (event) => {
      console.log(`Event: ${event.topic}`)
    })

    listener.use(
      configureSpaceGraphQL({
        workbooks: [
          {
            name: 'SpaceX Launches',
            source: 'https://spacex-production.up.railway.app/',
          },
        ],
      })
    )
  })
  ```
</CodeGroup>

### Filtering Sheets

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      configureSpaceGraphQL({
        workbooks: [
          {
            name: 'SpaceX Capsules',
            source: 'https://spacex-production.up.railway.app/',
            // Only generate a sheet for the 'Capsule' GraphQL object type
            sheets: [{ slug: 'Capsule' }],
          },
        ],
      })
    )
  })
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      configureSpaceGraphQL({
        workbooks: [
          {
            name: 'SpaceX Capsules',
            source: 'https://spacex-production.up.railway.app/',
            // Only generate a sheet for the 'Capsule' GraphQL object type
            sheets: [{ slug: 'Capsule' }],
          },
        ],
      })
    )
  })
  ```
</CodeGroup>

### Advanced Configuration

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      configureSpaceGraphQL(
        {
          workbooks: [
            {
              name: 'Custom SpaceX Workbook',
              source: 'https://spacex-production.up.railway.app/',
              sheets: [
                {
                  name: 'Capsules', // Custom sheet name
                  slug: 'Capsule',
                  actions: [
                    {
                      operation: 'dedupe',
                      mode: 'background',
                      label: 'Deduplicate Records',
                    },
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
        },
        async (event, workbookIds, tick) => {
          const { spaceId } = event.context
          console.log('Space configured successfully!', { spaceId, workbookIds })
          await tick(100, 'Configuration complete')
        }
      )
    )
  })
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'
  import type { FlatfileEvent } from '@flatfile/listener'

  const listener = FlatfileListener.create((listener) => {
    listener.use(
      configureSpaceGraphQL(
        {
          workbooks: [
            {
              name: 'Custom SpaceX Workbook',
              source: 'https://spacex-production.up.railway.app/',
              sheets: [
                {
                  name: 'Capsules', // Custom sheet name
                  slug: 'Capsule',
                  actions: [
                    {
                      operation: 'dedupe',
                      mode: 'background',
                      label: 'Deduplicate Records',
                    },
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
        },
        async (event: FlatfileEvent, workbookIds: string[], tick) => {
          const { spaceId } = event.context
          console.log('Space configured successfully!', { spaceId, workbookIds })
          await tick(100, 'Configuration complete')
        }
      )
    )
  })
  ```
</CodeGroup>

### Using Local Schema File

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'
  import fs from 'fs'
  import path from 'path'

  const listener = FlatfileListener.create((listener) => {
    // Read a GraphQL schema from a local file
    const schemaSDL = fs.readFileSync(
      path.join(__dirname, 'schema.graphql'),
      'utf8'
    )

    listener.use(
      configureSpaceGraphQL({
        workbooks: [
          {
            name: 'My Local Schema Workbook',
            source: schemaSDL,
          },
        ],
      })
    )
  })
  ```

  ```typescript TypeScript theme={null}
  import { FlatfileListener } from '@flatfile/listener'
  import { configureSpaceGraphQL } from '@flatfile/plugin-graphql-schema'
  import fs from 'fs'
  import path from 'path'

  const listener = FlatfileListener.create((listener) => {
    // Read a GraphQL schema from a local file
    const schemaSDL = fs.readFileSync(
      path.join(__dirname, 'schema.graphql'),
      'utf8'
    )

    listener.use(
      configureSpaceGraphQL({
        workbooks: [
          {
            name: 'My Local Schema Workbook',
            source: schemaSDL,
          },
        ],
      })
    )
  })
  ```
</CodeGroup>

## Troubleshooting

### Missing Sheets or Fields

Check the console logs for messages about "unsupported" field types or missing reference tables. The plugin logs warnings for non-critical issues.

### Invalid GraphQL Source

Ensure that any URL provided in the `source` option points to a valid, publicly accessible GraphQL endpoint that responds to introspection queries.

### Sheet Filtering Issues

When using the `sheets` filter, verify that the `slug` for each sheet configuration exactly matches the name of the corresponding GraphQL object type.

### Reference Field Problems

If reference fields are not working, confirm that the sheet being referenced is also being generated (i.e., it's included in your `sheets` filter or the filter is omitted entirely).

## Notes

### Default Behavior

By default, the plugin introspects the entire GraphQL schema from the provided `source`. It creates one sheet for each GraphQL `OBJECT` type, excluding standard types like `Query`, `Mutation`, `Subscription`, and internal types (those starting with `__`).

**Field Type Mapping:**

* GraphQL scalar types are mapped to Flatfile field types (`Int` → `number`, `String` → `string`)
* GraphQL object types are mapped to Flatfile reference fields
* If a GraphQL field is `NON_NULL`, a `required` constraint is added

### Supported Field Types

The plugin currently supports GraphQL `SCALAR`, `OBJECT`, and `NON_NULL` types. Other GraphQL types like `LIST`, `UNION`, `INTERFACE`, and `ENUM` are not explicitly supported and will be skipped during sheet generation.

### Reference Field Generation

For a reference field to be created correctly, the corresponding GraphQL object type must also be generated as a sheet in the same workbook. The plugin automatically selects the first non-reference field from the referenced sheet to use as the relationship key.

### Error Handling

The plugin uses console logging to provide feedback. Critical errors, such as failure to fetch or parse the GraphQL schema, will throw an exception, causing the `configureSpace` job to fail.
