# Source: https://firebase.google.com/docs/data-connect/configuration-reference.md.txt

The Firebase CLI lets you manage your Firebase projects in a local,
version-controllable project directory. This includes Data Connect
services in your projects, connectors for those services, and resources like
schema, query and mutation sources for each connector. The CLI also lets you
install and operate the Firebase Data Connect emulator. The CLI is an
efficient alternative to working in the Firebase console.

For instructions on installing the Firebase CLI experiment for
Private Preview program, and Data Connect-related CLI commands, see the
[CLI reference](https://firebase.google.com/docs/data-connect/cli-reference).

> [!NOTE]
> **Note:** Project configuration changes you make in the Firebase console are not automatically synchronized with configurations stored in a local project directory.

This reference guide documents:

- Data Connect-specific entries in your `firebase.json` project configuration file.
- Data Connect configurations in `dataconnect.yaml` and `connector.yaml`.

## Firebase project configuration files

### firebase.json configuration reference

Use the `dataconnect` keys to configure one or more Data Connect
services in your project.

    dataconnect: {
       source: string // Path to the directory containing the dataconnect.yaml service file.
    }

### dataconnect.yaml configuration reference

The `dataconnect.yaml` file stores configuration information about the locations
of application schema sources, connector sources, and data source connection
information. The file also serves as a project directory signifier for the
Firebase CLI.

The `schemaValidation` key controls the level of schema validation performed
when schemas are migrated during deployment. With no value set, the behavior of
the `dataconect:sql:migrate` command is to apply compatible changes and prompt
you before executing any strict changes. When set, the behavior is as follows:

- `STRICT` mode. The database schema must exactly match the application schema before the application schema can be deployed. Any tables or columns that are not used in your Data Connect schema will be deleted from the database.
- `COMPATIBLE` mode. The database schema must be compatible with the application schema before the application schema can be deployed; any additional changes are considered optional. Compatible means that schema migrations are based on the application schema you write. Elements in your database that are not used by your application schema are left unmodified. Therefore, after deployment, your backend may contain unused schemas, tables, and columns.

Values for other keys in this file are explained in the comments below.

    # The top-level Firebase Data Connect YAML file.

    # The Firebase Data Connect API version to target.
    # Optional. Defaults to the latest version.
    specVersion: string

    # The ID of the Firebase Data Connect service resource.
    # Required.
    serviceId: string

    # The location of the Firebase Data Connect service.
    # Required.
    location: string

    # Required.
    schema:
      # Relative path to directory for schema definitions.
      # Recursively loads all .gql files in this directory.
      # Optional. If not present, defaults to ./schema.
      source: string
      # Datasource connection information.
      # Required.
      datasource:
        # Required.
        postgresql:
          # The name of the PostgreSQL database.
          # Required.
          database: string
          cloudSql:
            # The ID of the CloudSQL instance resource.
            # Required.
            instanceId: string
            # Schema validation mode for schema migrations.
            # Defaults to unspecified/commented out, meaning you are prompted to
            # review all changes during migration.
            # If desired, uncomment and indicate one of "STRICT" or "COMPATIBLE".
            schemaValidation: string

    # Required.
    # Relative paths to directories for connector definitions.
    # Recursively loads all .gql files in the listed directories.
    # All directories specified MUST contain a connector.yaml file.
    connectorDirs: [string]

The YAML file assumes a default (but configurable) directory structure of:

    ./(project root)
       /dataconnect
          dataconnect.yaml
          /schema
            *.gql
          /example
            connector.yaml
            *.gql

### connector.yaml configuration reference

Use `connector.yaml` to configure default authentication mode and SDK generation
options.

    # The connector-level YAML file.

    # Required. The connector name of the Firebase Data Connect connector resource.
    connectorId: string

    # Optional. If not specified, no generated libraries (i.e. type-safe SDKs) will
    # be generated.
    generate:
        # Optional.
        javascriptSdk:
            # Path to the directory that will be updated with the latest generated
            # web TypeScript SDK.
            # Required.
            outputDir: string
            # Name of the Javascript package to be created.
            # Required. Example: @dataconnect/generated
            package: string
            # Path to your package.json directory. If specified, the new generated
            # SDK will be installed in this path.
            # Optional. If not provided, the package will not be auto-installed for
            # you.
            packageJsonDir: string
            # Enable React framework bindings.
            # Optional. Default to false.
            react: Boolean
            # Enable Angular framework bindings.
            # Optional. Default to false.
            angular: Boolean
        # Optional.
        dartSdk:
            # Path to the directory that will be updated with the latest generated
            # Flutter Dart SDK.
            # Required.
            outputDir: string
            # Name of the Dart package to be created.
            # Required. Example: "dataconnect_generated"
            package: string
        # Optional.
        kotlinSdk:
            # Path to the directory that will be updated with the latest generated
            # Android SDK.
            # Required.
            outputDir: string
            # Name of the package to be created.
            # Required. Example: com.google.firebase.dataconnect.generated
            package: string
        # Optional.
        adminNodeSdk:
            # Path to the directory that will be updated with the latest generated
            # Node Admin SDK.
            # Required.
            outputDir: string
            # Path to your package.json directory. If specified, the new generated
            # SDK will be installed in this path.
            # Optional. If not provided, the package will not be auto-installed for
            # you.
            packageJsonDir: string
            # Name of the package to be created (for example: @dataconnect/admin-generated).
            # Required.
            package: string
        # Optional.
        swiftSdk:
            # Path to the directory that will be updated with the latest generated
            # iOS Swift SDK.
            # Required.
            outputDir: string
            # Name of the Swift package to be created.
            # Required. Example: "FirebaseDataConnectGenerated"
            package: string