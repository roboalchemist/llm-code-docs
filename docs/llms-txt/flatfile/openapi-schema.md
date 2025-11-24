# Source: https://flatfile.com/docs/plugins/openapi-schema.md

# OpenAPI Schema to Flatfile Blueprint Converter

> Automatically converts OpenAPI v3.0.3 schemas into Flatfile Blueprints to streamline Space setup using existing API data structures

This plugin automatically converts an OpenAPI v3.0.3 schema into a Flatfile Blueprint. Its primary purpose is to streamline the setup of a Flatfile Space by using an existing OpenAPI specification as the single source of truth for data models. When a new Space is configured, the plugin fetches the specified OpenAPI schema, parses its components, and generates corresponding Workbooks and Sheets with correctly typed fields, constraints, and relationships. This is ideal for developers who want to quickly create a data import experience that matches their existing API data structures without manually defining each field in Flatfile.

## Installation

```bash
npm install @flatfile/plugin-convert-openapi-schema
```

## Configuration & Parameters

The plugin is configured via a single `setupFactory` object passed to the `configureSpaceWithOpenAPI` function.

### setupFactory

The main configuration object containing the following properties:

* **workbooks** (required): `Array<PartialWorkbookConfig>` - An array of workbook configurations to create from OpenAPI schemas
  * **source** (required): `string` - The URL pointing to the raw OpenAPI schema JSON file
  * **sheets** (required): `Array<PartialSheetConfig>` - An array of sheet configurations, mapping models from the schema to Flatfile Sheets
    * **model** (required): `string` - The name of the model in the OpenAPI `components.schemas` section to use for this sheet
    * **name** (optional): `string` - A custom display name for the Sheet. Defaults to the `model` name
    * **slug** (optional): `string` - A custom slug for the Sheet. Defaults to the `model` name
    * **actions** (optional): `Flatfile.Action[]` - An array of actions to add to the sheet
  * **name** (optional): `string` - A custom name for the Workbook. Defaults to the `info.title` property from the OpenAPI schema
  * **actions** (optional): `Flatfile.Action[]` - An array of actions to add to the workbook
* **space** (optional): `object` - A partial `Flatfile.spaces.SpaceConfig` object to apply custom configurations to the Space
* **debug** (optional): `boolean` - A flag for enabling debug mode

### callback (optional)

An optional function that executes after the Space and Workbooks have been successfully configured:

* **event**: `FlatfileEvent` - The event that triggered the configuration
* **workbookIds**: `string[]` - An array of IDs for the newly created workbooks
* **tick**: `TickFunction` - A function to report progress on the configuration job

## Usage Examples

### Basic Usage

This example sets up a listener that configures a Space with a single Workbook and Sheet based on a remote OpenAPI schema.

<CodeGroup>
  ```javascript
  import { configureSpaceWithOpenAPI } from "@flatfile/plugin-convert-openapi-schema";

  export default function (listener) {
    listener.on(
      "space:configure",
      configureSpaceWithOpenAPI({
        workbooks: [
          {
            source:
              "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.1/webhook-example.json",
            sheets: [{ model: "Pet" }],
          },
        ],
      })
    );
  }
  ```

  ```typescript
  import { configureSpaceWithOpenAPI } from "@flatfile/plugin-convert-openapi-schema";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.on(
      "space:configure",
      configureSpaceWithOpenAPI({
        workbooks: [
          {
            source:
              "https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v3.1/webhook-example.json",
            sheets: [{ model: "Pet" }],
          },
        ],
      })
    );
  }
  ```
</CodeGroup>

### Custom Configuration

This example shows how to customize the names of the Workbook and Sheet, and how to define multiple Sheets from the same source schema.

<CodeGroup>
  ```javascript
  import { configureSpaceWithOpenAPI } from "@flatfile/plugin-convert-openapi-schema";

  export default function (listener) {
    listener.on(
      "space:configure",
      configureSpaceWithOpenAPI({
        workbooks: [
          {
            name: "My Custom Workbook",
            source: "https://api.merge.dev/api/accounting/v1/schema",
            sheets: [
              { model: "Account" },
              { model: "Address", name: "Mailing Addresses", slug: "addresses" },
              { model: "Invoice" },
            ],
          },
        ],
      })
    );
  }
  ```

  ```typescript
  import { configureSpaceWithOpenAPI } from "@flatfile/plugin-convert-openapi-schema";
  import { FlatfileListener } from "@flatfile/listener";

  export default function (listener: FlatfileListener) {
    listener.on(
      "space:configure",
      configureSpaceWithOpenAPI({
        workbooks: [
          {
            name: "My Custom Workbook",
            source: "https://api.merge.dev/api/accounting/v1/schema",
            sheets: [
              { model: "Account" },
              { model: "Address", name: "Mailing Addresses", slug: "addresses" },
              { model: "Invoice" },
            ],
          },
        ],
      })
    );
  }
  ```
</CodeGroup>

### Advanced Usage with Callback

This example demonstrates adding custom actions to Workbooks and Sheets, and using the optional callback function to perform additional setup tasks after the Space is configured.

<CodeGroup>
  ```javascript
  import api from "@flatfile/api";
  import { configureSpaceWithOpenAPI } from "@flatfile/plugin-convert-openapi-schema";

  export default function (listener) {
    const callback = async (event, workbookIds, tick) => {
      const { spaceId } = event.context;
      // Create a getting started document
      await api.documents.create(spaceId, {
        title: "Getting Started",
        body: "<h1>Welcome!</h1><p>Follow the steps to import your data.</p>",
      });
      await tick(100, "Space setup complete");
    };

    listener.use(
      configureSpaceWithOpenAPI(
        {
          workbooks: [
            {
              source: "https://api.merge.dev/api/accounting/v1/schema",
              actions: [
                {
                  operation: "submitActionFg",
                  mode: "foreground",
                  label: "Submit",
                  primary: true,
                },
              ],
              sheets: [{ model: "Account" }, { model: "Invoice" }],
            },
          ],
        },
        callback
      )
    );
  }
  ```

  ```typescript
  import api from "@flatfile/api";
  import type { FlatfileListener } from "@flatfile/listener";
  import { configureSpaceWithOpenAPI } from "@flatfile/plugin-convert-openapi-schema";

  export default function (listener: FlatfileListener) {
    const callback = async (event, workbookIds, tick) => {
      const { spaceId } = event.context;
      // Create a getting started document
      await api.documents.create(spaceId, {
        title: "Getting Started",
        body: "<h1>Welcome!</h1><p>Follow the steps to import your data.</p>",
      });
      await tick(100, "Space setup complete");
    };

    listener.use(
      configureSpaceWithOpenAPI(
        {
          workbooks: [
            {
              source: "https://api.merge.dev/api/accounting/v1/schema",
              actions: [
                {
                  operation: "submitActionFg",
                  mode: "foreground",
                  label: "Submit",
                  primary: true,
                },
              ],
              sheets: [{ model: "Account" }, { model: "Invoice" }],
            },
          ],
        },
        callback
      )
    );
  }
  ```
</CodeGroup>

## Troubleshooting

If a sheet fails to generate, check the server logs for the message: `Schema not found for table name [sheet slug]`. This indicates that the `model` name provided in your configuration does not match any model name found in the `components.schemas` section of your OpenAPI file. Ensure the `model` name is spelled correctly and exists in the schema.

Common error scenarios:

* **Network errors**: If the `source` URL cannot be reached or returns a non-200 status code, an error like `Error fetching or processing schema: API returned status 404: Not Found` will be thrown
* **Missing models**: If a model specified in the `sheets` configuration is not found in the schema, an error is logged to the console and that sheet is skipped
* **Invalid schema**: Malformed OpenAPI schemas will cause the configuration job to fail

## Notes

### Default Behavior

* The plugin creates one Workbook for each entry in the `workbooks` array
* Workbook names default to the `info.title` field from the OpenAPI schema
* Sheet names and slugs default to the `model` name
* Fields are generated based on the model's properties, with OpenAPI types (`string`, `number`, `integer`, `boolean`) mapped to corresponding Flatfile field types
* Properties marked as `required` in the schema will have a `required` constraint in Flatfile

### Limitations and Considerations

* This plugin is designed for server-side execution within a Flatfile listener
* Officially supports OpenAPI version 3.0.3 (compatibility with other versions is not guaranteed)
* Depends on `@flatfile/plugin-space-configure` to apply the generated configuration
* OpenAPI `array` types are mapped to Flatfile's `string-list` type by default
* Complex arrays (arrays of objects) are not explicitly handled and may not convert as expected
* Schema references (`$ref`) are resolved only within the same document (e.g., `#/components/schemas/ModelName`)
* External file references are not supported
* Errors are logged to the console and re-thrown, which can aid in debugging within the listener's execution environment
