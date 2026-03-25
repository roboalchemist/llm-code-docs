# Source: https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md

# The Codegen CLI

The Codegen CLI provides a command line tool that streamlines the process of running code generation. The CLI can be ran manually from Terminal (or any other shell program) or can be called into from bash scripts.

The Codegen CLI has three primary commands:

* [**Initialize**](https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md#initialize): Initializes an `apollo-codegen-configuration.json` file that can be used to [configure how the CLI generates code](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration).
* [**Fetch Schema**](https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md#fetch-schema): Fetches your GraphQL schema and writes it to a file. The schema is required in order to run code generation.
  * To learn how to configure schema fetching, see [Downloading a schema](https://www.apollographql.com/docs/ios/code-generation/downloading-schema).
* [**Generate**](https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md#generate): Runs the code generation engine using the configuration in your `apollo-codegen-configuration.json` file.
* [**Generate Operation Manifest**](https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md#generate-operation-manifest): Generates the operation manifest for persisted queries using the configuration in your `apollo-codegen-configuration.json` file.

> For detailed usage documentation of these commands, see the [Usage](https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md#usage) section.

## Installation

When Apollo iOS is included as a dependency through Swift Package Manager (SPM), the CLI is built and packaged with the dependency automatically. This ensures you always have a valid version of the CLI for the version of Apollo iOS you are using and you never have to worry about installation or updates.

To learn how to run the Codegen CLI with your chosen package manager, open the appropriate section:

The Apollo iOS SPM package includes the Codegen CLI as an executable target. This ensures you always have a valid CLI version for your Apollo iOS version.

To simplify accessing the Codegen CLI, you can run the included `apollo-cli-install` SPM plugin. This plugin builds the CLI and creates a symbolic link to the executable in your project root.

If using a `Package.swift` file, you can install the CLI by running:

```bash
swift package --allow-writing-to-package-directory apollo-cli-install
```

After the plugin installs, it creates a symbolic link to the Codegen CLI (named `apollo-ios-cli`) in your project root folder. You can now run the CLI from the command line using `./apollo-ios-cli`.

> **Note:** Because the `apollo-ios-cli` in your project root is only a symbolic link, it only works if the compiled CLI executable exists. This is generally located in your Xcode Derived Data or the `.build` folder. If these are cleared, you can rerun the Install CLI plugin to rebuild the CLI executable.

The Apollo iOS SPM package includes the Codegen CLI as an executable target. This ensures you always have a valid CLI version for your Apollo iOS version.

To simplify accessing the Codegen CLI, you can run the included `InstallCLI` SPM plugin.

This plugin downloads the matching version of the CLI for the library version you are using.

If you use Swift packages through Xcode, right-click your project in the Xcode file explorer and select the **Install CLI** plugin command. A dialog prompts you to grant the plugin write access to your project directory and network access to download the CLI tool.

After the plugin downloads, it's unpacked to your project root. You can now run the CLI from the command line with `./apollo-ios-cli`.

Each [release](https://github.com/apollographql/apollo-ios/releases) of Apollo iOS in GitHub has a pre-built CLI binary attached. This binary can be downloaded and moved to any local directory that is convenient for you.

After downloading the binary, you can run the Codegen CLI from the directory where it is located:

```bash
./apollo-ios-cli ${Command Name} -${Command Arguments}
```

If you are not using SPM and do not want to use the pre-built CLI binary, you can compile the CLI manually. Once you've cloned the Apollo iOS git repo, use Terminal to go into that cloned directory and run the following command:

```bash
make build-cli
```

This will compile the Codegen CLI which you will find at `.build/release/apollo-ios-cli`. You can run the CLI from this directory, move it to another location, or add it to your shell's `$PATH`.

```bash
./.build/release/apollo-ios-cli ${Command Name} -${Command Arguments}
```

## Usage

The Apollo iOS Codegen CLI is a command like utility for Apollo iOS code generation.

#### `apollo-ios-cli <subcommand>`

#### Options:

| Option       | Description                  |
| ------------ | ---------------------------- |
| `--version`  | Show the version of the CLI. |
| `-h, --help` | Show help information.       |

#### Subcommands:

| Command        | Description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| `init`         | Initialize a new configuration with defaults.                                |
| `generate`     | Generate Swift source code based on a code generation configuration.         |
| `fetch-schema` | Download a GraphQL schema from the Apollo Registry or GraphQL introspection. |

See `apollo-ios-cli help <subcommand>` for detailed help.

### Initialize

Creates an `apollo-codegen-configuration.json` file with default values. The Codegen CLI reads this file to [configure how the CLI generates code](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration).

The default configuration will:

* Find all GraphQL schema files ending with the file extension `.graphqls` within your project directory.
* Find all GraphQL operation and fragment definition files ending with the file extension `.graphql` within your project directory.
* Create a Swift Package for your generated schema with the `schema-name` provided.
* Generate operation and fragment models relative to the `.graphql` files that define them.

> For more information on configuring code generation, see the [configuration documentation](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration).

#### Command:

`apollo-ios-cli init --schema-namespace <namespace> --module-type <type> [--target-name <target name>]`

#### Options:

| Option               | Description                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--schema-namespace` | **\[Required]** The name you would like to be used as the namespace for your generated schema files.                                                                                         |
| `--module-type`      | **\[Required]** How to package the schema types for dependency management. Possible types are `embeddedInTarget`, `swiftPackageManager`, `other`.                                            |
| `--target-name`      | Name of the target in which the schema types files will be manually embedded.*Note: This is required for the "embeddedInTarget" module type and will be ignored for all other module types.* |
| `-p, --path <path>`  | Write the configuration to a file at the path. (default: `./apollo-codegen-config.json`)                                                                                                     |
| `-w, --overwrite`    | Overwrite any file at `--path`. If init is called without `--overwrite` and a config file already exists at `--path`, the command will fail.                                                 |
| `-s, --print`        | Print the configuration to stdout.                                                                                                                                                           |
| `--version`          | Show the version of the CLI.                                                                                                                                                                 |
| `-h, --help`         | Show help information.                                                                                                                                                                       |

### Fetch Schema

Downloads a GraphQL schema from the Apollo Registry or GraphQL introspection and writes it to a file. The schema is required in order to run code generation.

> For more information on schema fetching, see [Downloading a schema](https://www.apollographql.com/docs/ios/code-generation/downloading-schema).

> For more information on configuring schema fetching, see the [configuration documentation](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#schema-download-configuration).

#### Command:

`apollo-ios-cli fetch-schema [--path <path>] [--string <string>]`

#### Options:

| Option                  | Description                                                                                                                                                                                                                                                                                                                       |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-p, --path <path>`     | Read the configuration from a file at the path. Requires that the [`schemaDownload`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#schema-download-configuration) property is configured in the file. `--string` overrides this option if used together. (default: `./apollo-codegen-config.json`) |
| `-s, --string <string>` | Provide the configuration string in JSON format. This option overrides `--path`.                                                                                                                                                                                                                                                  |
| `-v, --verbose `        | Increase verbosity to include debug output.                                                                                                                                                                                                                                                                                       |
| `--version`             | Show the version of the CLI.                                                                                                                                                                                                                                                                                                      |
| `-h, --help`            | Show help information.                                                                                                                                                                                                                                                                                                            |

### Generate

Runs the code generation engine to generate Swift source code using the configuration in your `apollo-codegen-configuration.json` file.

> For more information on configuring code generation, see the [configuration documentation](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration).

#### Command:

`apollo-ios-cli generate [--path <path>] [--string <string>]`

#### Options:

| Option                      | Description                                                                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-p, --path <path>`         | Read the configuration from a file at the path. `--string` overrides this option if used together. (default: `./apollo-codegen-config.json`)                                       |
| `-s, --string <string>`     | Provide the configuration string in JSON format. This option overrides `--path`.                                                                                                   |
| `-v, --verbose `            | Increase verbosity to include debug output.                                                                                                                                        |
| `-f, --fetch-schema`        | Fetch the GraphQL schema before Swift code generation. This runs the [`fetch-schema`](https://www.apollographql.com/docs/ios/code-generation/codegen-cli.md#fetch-schema) command. |
| `--ignore-version-mismatch` | Ignores version mismatches between the `apollo-ios-cli` and the version of the Apollo sdk being used.                                                                              |
| `--version`                 | Show the version of the CLI.                                                                                                                                                       |
| `-h, --help`                | Show help information.                                                                                                                                                             |

### Generate Operation Manifest

Generates the operation manifest for persisted queries using the configuration in your `apollo-codegen-configuration.json` file.

> For more information on configuring code generation, see the [configuration documentation](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration).

#### Command:

`apollo-ios-cli generate-operation-manifest [--path <path>] [--string <string>]`

#### Options:

| Option                      | Description                                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `-p, --path <path>`         | Read the configuration from a file at the path. `--string` overrides this option if used together. (default: `./apollo-codegen-config.json`) |
| `-s, --string <string>`     | Provide the configuration string in JSON format. This option overrides `--path`.                                                             |
| `-v, --verbose `            | Increase verbosity to include debug output.                                                                                                  |
| `--ignore-version-mismatch` | Ignores version mismatches between the `apollo-ios-cli` and the version of the Apollo sdk being used.                                        |
| `--version`                 | Show the version of the CLI.                                                                                                                 |
| `-h, --help`                | Show help information.                                                                                                                       |
