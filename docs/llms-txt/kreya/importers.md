# Source: https://kreya.app/docs/importers.md

# Importers

Importers are used to fetch information about the available operations and request/response types. You can add, edit and delete importers via Project → Importers.

info

Because fetching and parsing API definitions may take some time, Kreya caches the imported data. If you changed your API definitions, you may need to manually run the importers again (by clicking the  icon in the main window).

## Generating operations automatically[​](#generating-operations-automatically "Direct link to Generating operations automatically")

For each importer, there is an option to create missing operations, which is enabled by default. When an importer runs, Kreya checks if any of the imported methods are missing in the project. This is useful if you want to keep your operations in sync with your API. If you add a method to your API, Kreya will automatically add an operation for it on the next importer run.

Removed operations are also detected. They are highlighted and Kreya presents an option to remove them.

## Custom Headers [Pro / Enterprise](/pricing.md)[​](#custom-headers- "Direct link to custom-headers-")

If you require custom headers for your gRPC server reflection, GraphQL introspection or REST OpenAPI URL importers, open the advanced options and set the headers.

![Setting custom header on REST OpenAPI URL importer](/assets/ideal-img/importer-custom-headers.b8af57b.400.png)
