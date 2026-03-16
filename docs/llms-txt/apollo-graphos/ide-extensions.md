# Source: https://www.apollographql.com/docs/graphos/connectors/tooling/ide-extensions.md

# IDE Support for Connectors Development

Apollo provides IDE extensions to streamline graph development, such as syntax highlighting, inline performance information, and autocomplete for fields, types, and federation directives.

Once you've [installed the relevant extension](https://www.apollographql.com/docs/ide-support), use this guide to enable Connectors-specific features in tools like VS Code, JetBrains IDEs, and Vim/NeoVim.

## Visual Studio Code

Starting with v2.3.3, the [Apollo GraphQL VS Code extension](https://www.apollographql.com/docs/ide-support/vs-code) can give you fast feedback on your Apollo Connectors in VS Code.
Through it, you can get the *same* validations that composition provides, with errors and hints highlighted in your schema file on each save.

### Prerequisites

These composition-based diagnostics are powered by Rover. You'll need Rover v0.27.0 or later [installed](https://www.apollographql.com/docs/rover/getting-started) to use composition-based diagnostics.

### Connector configuration

By default, you need two files in the root of your project to enable Connectors validations in VS Code:

1. An `apollo.config.yaml` file containing `rover: {}`
2. A `supergraph.yaml` file that's the
   [configuration file](https://www.apollographql.com/docs/rover/commands/supergraphs#yaml-configuration-file)
   used for `rover dev`, `rover supergraph compose`, and this VS Code extension.
   1. Make sure to set the composition version to 2.11.0.
   2. Make sure every file you want feedback on is included in the `subgraphs` section.

You can use a different location for your `supergraph.yaml` by setting the `rover.supergraphConfig` option in
`apollo.config.yaml`, like this:

```yaml title=apollo.config.yaml
rover:
  supergraphConfig: path/to/supergraph.yaml
```

### Troubleshooting

Refer to the dedicated VS Code extension documentation for [troubleshooting tips](http://localhost:3000/docs/ide-support/vs-code#troubleshooting).

## JetBrains IDEs

Installing and configuring the [Apollo GraphQL plugin](https://plugins.jetbrains.com/plugin/20645-apollo-graphql) in JetBrains IDEs for Connectors development is no different than for [regular GraphQL development](https://www.apollographql.com/docs/ide-support/jetbrains).

## Vim/NeoVim

Setting up the Apollo Language Server in Vim/NeoVim for Connectors development is no different than for [regular GraphQL development](https://www.apollographql.com/docs/ide-support/vim).
