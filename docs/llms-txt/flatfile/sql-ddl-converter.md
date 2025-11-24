# Source: https://flatfile.com/docs/plugins/sql-ddl-converter.md

# SQL DDL to Flatfile Blueprint Converter

> Automatically create Flatfile Blueprints from SQL Data Definition Language (DDL) files to streamline database schema imports.

The SQL DDL Converter plugin automates the creation of a Flatfile Blueprint from a SQL Data Definition Language (DDL) file. Its primary purpose is to streamline the setup of a Flatfile Space by translating existing database schemas directly into Flatfile Workbooks and Sheets.

The plugin reads a provided SQL file (e.g., from a `CREATE TABLE` script), parses it to identify table structures, and converts each table into a corresponding Sheet configuration with appropriate fields. This is ideal for use cases where a data import process needs to match an existing database schema, saving significant manual configuration time. It is designed to be used in a server-side listener, typically on the `space:configure` event.

## Installation

Install the plugin using npm:

```bash
npm install @flatfile/plugin-convert-sql-ddl
```

## Configuration & Parameters

The plugin is configured through the `setupFactory` object passed to the `configureSpaceWithSqlDDL` function.

### setupFactory: SqlSetupFactory (required)

The main configuration object containing:

#### workbooks: PartialWorkbookConfig\[] (required)

An array of workbook configurations to create in the Space.

Each `PartialWorkbookConfig` object contains:

* **name** (string): The display name of the Workbook
* **source** (string, required): The relative file path to the SQL DDL file (relative to project root)
* **sheets** (PartialSheetConfig\[], required): An array of sheet configurations

Each `PartialSheetConfig` object contains:

* **name** (string): The display name of the Sheet
* **slug** (string, required): The identifier for the sheet that MUST exactly match the table name from the SQL DDL file

#### space (object, optional)

An object containing additional configuration for the Space itself, such as metadata. Follows the structure of `Flatfile.spaces.SpaceConfig`.

### Default Behavior

The plugin has no default configuration and requires the `setupFactory` object to be fully defined. It will:

* Read the file specified in the `source` property
* Parse it as MySQL DDL
* Map each table to a sheet configuration where the table name matches the sheet's `slug`
* Log errors to console and skip sheets if the `slug` doesn't correspond to any table found in the SQL file
* Continue processing remaining valid sheets

## Usage Examples

### Basic Usage

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL } from "@flatfile/plugin-convert-sql-ddl";

  listener.use(
    configureSpaceWithSqlDDL({
      workbooks: [
        {
          name: "Database Import",
          source: "src/data/schema.sql",
          sheets: [
            {
              name: "Users",
              slug: "users", // Must match a table name in schema.sql
            },
            {
              name: "Products",
              slug: "products", // Must match a table name in schema.sql
            },
          ],
        },
      ],
    })
  );
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL, SqlSetupFactory } from "@flatfile/plugin-convert-sql-ddl";

  const setupFactory: SqlSetupFactory = {
    workbooks: [
      {
        name: "Database Import",
        source: "src/data/schema.sql",
        sheets: [
          {
            name: "Users",
            slug: "users", // Must match a table name in schema.sql
          },
          {
            name: "Products",
            slug: "products", // Must match a table name in schema.sql
          },
        ],
      },
    ],
  };

  listener.use(configureSpaceWithSqlDDL(setupFactory));
  ```
</CodeGroup>

### Advanced Configuration with Callback

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL } from "@flatfile/plugin-convert-sql-ddl";

  listener.use(
    configureSpaceWithSqlDDL(
      {
        workbooks: [
          {
            name: "Database Import",
            source: "src/data/schema.sql",
            sheets: [
              {
                name: "Users",
                slug: "users",
              },
            ],
          },
        ],
        space: {
          metadata: {
            sidebarTitle: "SQL Import Tool",
          },
        },
      },
      (event, workbookIds, tick) => {
        // This function runs after the space is configured
        console.log("Space configured successfully!");
        console.log("Created workbook IDs:", workbookIds);
        tick(100, "Configuration complete");
      }
    )
  );
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL, SqlSetupFactory } from "@flatfile/plugin-convert-sql-ddl";
  import { FlatfileEvent } from "@flatfile/listener";

  const setupFactory: SqlSetupFactory = {
    workbooks: [
      {
        name: "Database Import",
        source: "src/data/schema.sql",
        sheets: [
          {
            name: "Users",
            slug: "users",
          },
        ],
      },
    ],
    space: {
      metadata: {
        sidebarTitle: "SQL Import Tool",
      },
    },
  };

  listener.use(
    configureSpaceWithSqlDDL(
      setupFactory,
      (event: FlatfileEvent, workbookIds: string[], tick: any) => {
        // This function runs after the space is configured
        console.log("Space configured successfully!");
        console.log("Created workbook IDs:", workbookIds);
        tick(100, "Configuration complete");
      }
    )
  );
  ```
</CodeGroup>

### Custom Event Handler Usage

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL } from "@flatfile/plugin-convert-sql-ddl";

  listener.on("space:configure", async (event) => {
    const { spaceId } = event.context;
    
    const configure = configureSpaceWithSqlDDL({
      workbooks: [
        {
          name: "Customer Data",
          source: "data/my_schema.sql",
          sheets: [
            { name: "Customers", slug: "customers" },
            { name: "Orders", slug: "orders" },
          ],
        },
      ],
      space: {
        metadata: {
          theme: {
            root: {
              primaryColor: "blue"
            }
          }
        }
      }
    });
    
    await configure(listener);
  });
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL, SqlSetupFactory } from "@flatfile/plugin-convert-sql-ddl";
  import { FlatfileEvent } from "@flatfile/listener";

  listener.on("space:configure", async (event: FlatfileEvent) => {
    const { spaceId } = event.context;
    
    const setupFactory: SqlSetupFactory = {
      workbooks: [
        {
          name: "Customer Data",
          source: "data/my_schema.sql",
          sheets: [
            { name: "Customers", slug: "customers" },
            { name: "Orders", slug: "orders" },
          ],
        },
      ],
      space: {
        metadata: {
          theme: {
            root: {
              primaryColor: "blue"
            }
          }
        }
      }
    };
    
    const configure = configureSpaceWithSqlDDL(setupFactory);
    await configure(listener);
  });
  ```
</CodeGroup>

## Troubleshooting

### Schema Not Found Error

If a sheet's `slug` doesn't match any table in the SQL file, you'll see a console error:

Schema not found for table name accounts
**Solution**: Ensure the `slug` property exactly matches the table name in your SQL DDL file.

### File Not Found Error

If the SQL file specified in the `source` property cannot be read, a hard error will be thrown.

**Solution**:

* Verify the file path is correct and relative to your project root
* Ensure the file exists and the process has read permissions
* Check that the file contains valid MySQL DDL syntax

### Example Error Handling

<CodeGroup>
  ```javascript JavaScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL } from "@flatfile/plugin-convert-sql-ddl";

  // Example: schema.sql contains 'users' table but not 'accounts'
  listener.use(
    configureSpaceWithSqlDDL({
      workbooks: [
        {
          name: "App Data",
          source: "data/schema.sql",
          sheets: [
            {
              name: "Users",
              slug: "users", // This will succeed
            },
            {
              name: "Accounts", 
              slug: "accounts", // This will fail and be skipped
            },
          ],
        },
      ],
    })
  );
  ```

  ```typescript TypeScript
  import { listener } from "@flatfile/listener";
  import { configureSpaceWithSqlDDL, SqlSetupFactory } from "@flatfile/plugin-convert-sql-ddl";

  // Example: schema.sql contains 'users' table but not 'accounts'
  const setupFactory: SqlSetupFactory = {
    workbooks: [
      {
        name: "App Data",
        source: "data/schema.sql",
        sheets: [
          {
            name: "Users",
            slug: "users", // This will succeed
          },
          {
            name: "Accounts",
            slug: "accounts", // This will fail and be skipped
          },
        ],
      },
    ],
  };

  listener.use(configureSpaceWithSqlDDL(setupFactory));
  ```
</CodeGroup>

## Notes

### Important Considerations

* **Server-Side Only**: This plugin must be deployed in a server-side listener environment as it requires file system access to read SQL files
* **File Path**: The `source` property must be a file path relative to the project's root directory
* **SQL Dialect**: Currently only supports MySQL-compatible DDL syntax due to the hardcoded parser configuration
* **Exact Matching**: The `slug` property must exactly match table names in your SQL DDL file for proper field generation
* **Automatic Constraints**: The plugin automatically identifies `NOT NULL` columns and other constraints from DDL and translates them into Flatfile field constraints
* **Bundled Dependencies**: Uses `sql-ddl-to-json-schema` and `@flatfile/plugin-convert-json-schema` internally (no separate installation required)

### Default Behavior

* Reads and parses SQL files as MySQL DDL
* Maps tables to sheets based on exact slug matching
* Logs errors for unmatched slugs but continues processing valid sheets
* Automatically applies field constraints based on SQL column definitions
* Requires fully defined configuration with no built-in defaults
