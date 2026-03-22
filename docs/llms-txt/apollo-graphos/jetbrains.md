# Source: https://www.apollographql.com/docs/ide-support/jetbrains.md

# Graph Development in JetBrains IDEs

The JetBrains [Apollo GraphQL plugin](https://plugins.jetbrains.com/plugin/20645-apollo-graphql) can give you fast feedback on your GraphQL schemas in IntelliJ, WebStorm, and other JetBrains IDEs.
Through it, you can get the same validations that composition provides, with errors and hints highlighted in your schema file on each save.

## Prerequisites

These composition-based diagnostics are powered by Rover, starting with version 0.27.0. You need this version or later [installed](https://www.apollographql.com/docs/rover/getting-started) to use composition-based diagnostics.

## Configuration

1. Install the [plugin](https://plugins.jetbrains.com/plugin/20645-apollo-graphql).

2. Enable the Rover integration by going to **Setting** > **Languages & Frameworks** > **GraphQL** > **Rover** and checking **Enabled**.

3. Ensure a `supergraph.yaml` file is in the root of your project. This [configuration file](https://www.apollographql.com/docs/rover/commands/supergraphs#yaml-configuration-file) is used for Rover commands like `rover dev`, `rover supergraph compose`, and this plugin.

   You can set a different location for your `supergraph.yaml` in the  **LSP Arguments** > **Supergraph config file** field in the Rover integration settings.

4. In your `supergraph.yaml` do the following:

* Ensure every schema file you want feedback on is included in the `subgraphs` section.
* If you're developing with Apollo Connectors, set the composition version to 2.11.0.

## Troubleshooting

### Restart the language server

If you aren't seeing diagnostics, try restarting the language server by clicking the Apollo icon in the status bar.

### Confirm your Rover version

You can see the currently installed Rover version in the plugin's settings, or by running `rover --version` in a terminal.
Ensure you have version 0.27.0 or later.

### Debug logging

If the extension isn't working as expected, you can enable debug logging by going to **Help** > **Diagnostic Tools** > **Debug Log Settings...** and
adding `Apollo` and `#com.intellij.platform.lsp` to the list.
This settings adds detailed logs to IDE's log file, which can aid in debugging.
