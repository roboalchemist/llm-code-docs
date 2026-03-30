# Source: https://www.apollographql.com/docs/ide-support.md

# IDE Support for Graph Development

Many IDEs provide features to streamline federated GraphQL development, such as federation-aware syntax highlighting, inline performance information, and autocomplete for fields, types, and federation directives. Learn how to enable federation-specific features in tools like VS Code, JetBrains IDEs, and Vim/NeoVim.

## Visual Studio Code

Apollo's [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo) provides an all-in-one tooling experience for developing apps with Apollo. See the [dedicated documentation page](https://www.apollographql.com/docs/graphos/schema-design/ide-support/vs-code) for configuration details.

## JetBrains

Apollo's [JetBrains Plugin](https://plugins.jetbrains.com/plugin/20645-apollo-graphql) provides federation-specific development features, such as autocomplete for federation directives. This plugin supports all IntelliJ-based IDEs, including:

* IntelliJ IDEA
* PyCharm
* PhpStorm
* WebStorm
* CLion
* RubyMine
* Rider
* GoLand

You must enable the Rover integration after installing the plugin. Otherwise, your IDE might display unexpected errors while you're working with a subgraph schema. See the [dedicated documentation page](https://www.apollographql.com/docs/graphos/schema-design/ide-support/jetbrains) for configuration details.

## Vim/NeoVim

You can configure Vim/NeoVim to use the same Apollo Language Server that powers the VS Code and JetBrains plugins. See the [dedicated documentation page](https://www.apollographql.com/docs/graphos/schema-design/ide-support/vim) for configuration details.

## Additional resources

If your graph uses the Apollo Router Core or GraphOS Router, make sure to enable [router configuration awareness](https://www.apollographql.com/docs/graphos/reference/router/configuration#configuration-awareness-in-your-text-editor) in your editor.
