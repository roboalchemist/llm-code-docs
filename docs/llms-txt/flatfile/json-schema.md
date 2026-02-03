# Source: https://flatfile.com/docs/plugins/json-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://flatfile.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# JSON Schema Converter

> Automatically transform JSON Schema into Flatfile Blueprint for streamlined data model setup

The JSON Schema Converter plugin for Flatfile automatically transforms a JSON Schema into a Flatfile Blueprint. A Blueprint is Flatfile's Data Definition Language (DDL) used for defining data models, validations, and transformations.

The primary purpose of this plugin is to streamline the setup of a Flatfile Space. Instead of manually defining each field for your Sheets, you can provide a JSON Schema, and the plugin will generate the corresponding Workbooks and Sheets configuration. This is particularly useful for projects that already use JSON Schema for data validation or API definitions, allowing for a single source of truth for data structures.

The plugin is designed to be used in a server-side Flatfile listener, typically on the `space:configure` event. It can fetch schemas from a URL, use a direct JSON object, or execute a function to retrieve the schema dynamically.

## Installation

```bash  theme={null}
npm install @flatfile/plugin-convert-json-schema
```

## Configuration & Parameters

The plugin is configured via a single object passed to the `configureSpaceWithJsonSchema` function. This object is of type `JsonSetupFactory`.

### JsonSetupFactory

| Parameter   | Type                                   | Required | Description                                                         |
| ----------- | -------------------------------------- | -------- | ------------------------------------------------------------------- |
| `workbooks` | `PartialWorkbookConfig[]`              | Yes      | An array of workbook configurations to be created in the Space      |
| `space`     | `Partial<Flatfile.spaces.SpaceConfig>` | No       | Configuration details for the Space itself, like metadata or themes |

### PartialWorkbookConfig

| Parameter | Type                   | Required | Description                                          |
| --------- | ---------------------- | -------- | ---------------------------------------------------- |
| `name`    | `string`               | Yes      | The name of the Workbook                             |
| `sheets`  | `PartialSheetConfig[]` | Yes      | An array of sheet configurations within the Workbook |
| `actions` | `Flatfile.Action[]`    | No       | Actions available at the Workbook level              |

### PartialSheetConfig

| Parameter | Type                                                    | Required | Description                                                                                                                                                  |
| --------- | ------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `source`  | `object \| string \| (() => object \| Promise<object>)` | Yes      | The JSON Schema for the sheet. Can be a direct JSON Schema object, a string URL pointing to a schema file, or an async function that returns a schema object |
| `name`    | `string`                                                | No       | The name of the Sheet. Defaults to the `title` property from the root of the JSON Schema if not provided                                                     |
| `slug`    | `string`                                                | No       | A unique identifier for the sheet                                                                                                                            |
| `actions` | `Flatfile.Action[]`                                     | No       | Actions available at the Sheet level                                                                                                                         |

### Default Behavior

By default, the plugin will create Workbooks and Sheets as defined in the `workbooks` array. For each sheet, it parses the `source` JSON schema, converting its `properties` into Flatfile fields. Nested objects in the schema are flattened into fields with names like `parentKey_childKey`. The sheet's name defaults to the schema's `title` if not explicitly provided.

## Usage Examples

### Basic Usage with URL Schema

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpaceWithJsonSchema } from "@flatfile/plugin-convert-json-schema";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener) {
    listener.use(
      configureSpaceWithJsonSchema({
        workbooks: [
          {
            name: "JSON Schema Workbook",
            sheets: [
              {
                name: "Person Sheet",
                source: "https://example.com/schemas/person.json",
              },
            ],
          },
        ],
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { configureSpaceWithJsonSchema } from "@flatfile/plugin-convert-json-schema";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpaceWithJsonSchema({
        workbooks: [
          {
            name: "JSON Schema Workbook",
            sheets: [
              {
                name: "Person Sheet",
                source: "https://example.com/schemas/person.json",
              },
            ],
          },
        ],
      })
    );
  }
  ```
</CodeGroup>

### Local Schema with Callback

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpaceWithJsonSchema } from "@flatfile/plugin-convert-json-schema";
  import { FlatfileListener } from "@flatfile/listener";
  import api from "@flatfile/api";

  export default function (listener) {
    const personSchema = {
      title: "Person",
      type: "object",
      properties: {
        firstName: { type: "string" },
        lastName: { type: "string" },
        age: { type: "integer", minimum: 0 },
      },
    };

    const callback = async (event, workbookIds, tick) => {
      const { spaceId } = event.context;
      await api.documents.create(spaceId, {
        title: "Welcome",
        body: "<h1>Welcome to your new Space!</h1>",
      });
      await tick(100, "Space setup complete");
    };

    listener.use(
      configureSpaceWithJsonSchema(
        {
          workbooks: [
            {
              name: "My Workbook",
              sheets: [{ source: personSchema }],
            },
          ],
        },
        callback
      )
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { configureSpaceWithJsonSchema } from "@flatfile/plugin-convert-json-schema";
  import { FlatfileListener, FlatfileEvent } from "@flatfile/listener";
  import { TickFunction } from "@flatfile/plugin-job-handler";
  import api from "@flatfile/api";

  export default function (listener: FlatfileListener) {
    const personSchema = {
      title: "Person",
      type: "object",
      properties: {
        firstName: { type: "string" },
        lastName: { type: "string" },
        age: { type: "integer", minimum: 0 },
      },
    };

    const callback = async (event: FlatfileEvent, workbookIds: string[], tick: TickFunction) => {
      const { spaceId } = event.context;
      await api.documents.create(spaceId, {
        title: "Welcome",
        body: "<h1>Welcome to your new Space!</h1>",
      });
      await tick(100, "Space setup complete");
    };

    listener.use(
      configureSpaceWithJsonSchema(
        {
          workbooks: [
            {
              name: "My Workbook",
              sheets: [{ source: personSchema }],
            },
          ],
        },
        callback
      )
    );
  }
  ```
</CodeGroup>

### Dynamic Schema from Function

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { configureSpaceWithJsonSchema, fetchExternalReference } from "@flatfile/plugin-convert-json-schema";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener) {
    listener.use(
      configureSpaceWithJsonSchema({
        workbooks: [
          {
            name: "Dynamic Workbook",
            sheets: [
              {
                name: "Product Sheet",
                source: async () => {
                  // Imagine custom logic here, e.g., adding auth headers
                  const schemaUrl = "https://api.my-service.com/schemas/product.json";
                  return await fetchExternalReference(schemaUrl);
                },
              },
            ],
          },
        ],
      })
    );
  }
  ```

  ```typescript TypeScript theme={null}
  import { configureSpaceWithJsonSchema, fetchExternalReference } from "@flatfile/plugin-convert-json-schema";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.use(
      configureSpaceWithJsonSchema({
        workbooks: [
          {
            name: "Dynamic Workbook",
            sheets: [
              {
                name: "Product Sheet",
                source: async () => {
                  // Imagine custom logic here, e.g., adding auth headers
                  const schemaUrl = "https://api.my-service.com/schemas/product.json";
                  return await fetchExternalReference(schemaUrl);
                },
              },
            ],
          },
        ],
      })
    );
  }
  ```
</CodeGroup>

### Using fetchExternalReference with Error Handling

<CodeGroup>
  ```javascript JavaScript theme={null}
  import { fetchExternalReference } from "@flatfile/plugin-convert-json-schema";

  try {
    const schema = await fetchExternalReference("https://example.com/schemas/product.json");
    // Use schema
  } catch (error) {
    console.error("Failed to fetch schema:", error.message);
    // Handle the error, perhaps by falling back to a default schema
  }
  ```

  ```typescript TypeScript theme={null}
  import { fetchExternalReference } from "@flatfile/plugin-convert-json-schema";

  try {
    const schema = await fetchExternalReference("https://example.com/schemas/product.json");
    // Use schema
  } catch (error) {
    console.error("Failed to fetch schema:", error.message);
    // Handle the error, perhaps by falling back to a default schema
  }
  ```
</CodeGroup>

## Troubleshooting

### Job Fails on `space:configure`

Check the Job status in the Flatfile Dashboard for error messages. Common causes include:

* An invalid URL was provided for a schema `source`
* The schema at the URL is not valid JSON
* A `$ref` in the schema points to a location that cannot be resolved

### Fields Not Appearing as Expected

* Ensure the JSON schema has a `properties` object at the level you expect fields to be generated from
* Nested objects are flattened with an underscore (`_`) separator. For example, an `address` object with a `street` property becomes a field with the key `address_street`
* Check the data types in your schema. Supported types include `string`, `number`, `integer`, `boolean`, and `array` (which becomes `string-list`). `enum` is also supported. Unrecognized types will be ignored

## Notes

### Special Considerations

* This plugin is intended for use in server-side listeners, specifically for the `space:configure` event
* The plugin handles JSON schema references (`$ref`). It can resolve local references within the same schema (e.g., `#/definitions/address`) and external references to other files (e.g., `common.json#/definitions/name`). External references are resolved relative to the `$id` property of the schema they are in
* The plugin makes API calls on behalf of the user, including `api.spaces.update` and `api.workbooks.create`

### Error Handling

Errors during schema fetching (`fetchExternalReference`) or reference resolution will bubble up. When used within a Flatfile listener, these unhandled exceptions will cause the associated Job to fail, which is the standard error handling pattern in the Flatfile ecosystem. The Job's execution history will contain details about the error.

It is the user's responsibility to ensure that the provided JSON schemas are valid and that any URLs are accessible from the server environment where the listener is running.
