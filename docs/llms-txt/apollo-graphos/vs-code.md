# Source: https://www.apollographql.com/docs/ide-support/vs-code.md

# Graph Development in VS Code

The Apollo [VS Code extension](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo) provides an all-in-one tooling experience for developing apps with Apollo. The extension provides:

* [Syntax highlighting](https://www.apollographql.com/docs/ide-support/vs-code.md#syntax-highlighting) for GraphQL files and `gql` templates in JavaScript
* Real-time feedback, including [intelligent autocomplete](https://www.apollographql.com/docs/ide-support/vs-code.md#intelligent-autocomplete) for fields, arguments, types, and variables as you write queries
* Client-side and remote schema management, including [client-only](https://www.apollographql.com/docs/ide-support/vs-code.md#client-only-schemas) schemas
* Inline [performance information](https://www.apollographql.com/docs/ide-support/vs-code.md#performance-insights) and [supergraph editing](https://www.apollographql.com/docs/ide-support/vs-code.md#supergraph-editing) tool
* [Streamlined project navigation](https://www.apollographql.com/docs/ide-support/vs-code.md#navigating-projects) with jump-to and peek-at definitions
* [Switch graph variants](https://www.apollographql.com/docs/ide-support/vs-code.md#graph-variant-switching) to work with schemas running on different environments
* (Experimental) [Apollo Client DevTools](https://www.apollographql.com/docs/ide-support/vs-code.md#experimental-apollo-client-devtools-in-your-ide) in your IDE

Starting with version 2.3.3, the extension also works with Apollo Connectors. [Learn more.](https://www.apollographql.com/docs/ide-support/vs-code.md#developing-connectors)

## Getting started

The VS Code extension must be linked to a published or local schema via a configuration file.

### Configuration

The VS Code extension requires a `apollo.config.json` configuration file at the root of the project.
Alternatively, you can create a `yaml`, `cjs`, `mjs`, or `ts` file with the same configuration.

Select one of the options below to define the contents of this configuration file.

#### Configure extension for client development with schemas published to Apollo GraphOS

To get all the benefits of the VS Code experience, it's best to link the schema being developed before installing the extension. The best way to do that is by [publishing a schema](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish) to the [GraphOS schema registry](https://www.apollographql.com/docs/graphos/get-started/concepts/graphos#graph-registry).

After that's done, edit the `apollo.config.json` file to look like this:

```json
{
  "client": {
    "service": "graphos-graph-name"
  }
}
```

The `service` name is the name of the graph you've created in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content).

See [additional configuration options](https://www.apollographql.com/docs/ide-support/vs-code.md#additional-apollo-config-options).

To authenticate with GraphOS Studio to pull down your schema, create an `.env` file in the same directory as the `apollo.config.json` file. The `.env` file should be untracked—that is, don't commit it to Git.

Then, go to your [User Settings page](https://studio.apollographql.com/user-settings/api-keys?referrer=docs-content) in GraphOS Studio to create a new personal API key.

It's best practice to create a new API key for each team member. API keys should also be named so they're easy to find and revoke if needed.

After you've created your API key, add the following line to the `.env` file:

```bash
APOLLO_KEY=<enter copied key here>
```

Afterward, reload VS Code. The Apollo integration will connect to GraphOS Studio to provide autocomplete, validation, and more.

#### Configure extension for supergraph schema development

The extension can integrate with the [Rover CLI](https://www.apollographql.com/docs/rover/) to help you design supergraph schemas with additional support for Apollo Federation.

To get all the benefits of the extension, ensure you've [installed](https://www.apollographql.com/docs/rover/getting-started) and [configured](https://www.apollographql.com/docs/rover/configuring) the latest preview Rover release (`v0.27.0`). For now, we recommend installing this preview release to your project's root directory rather than directly to your `PATH`. If you choose to do so, you need to configure the `rover.bin` key accordingly in your `apollo.config.js` file as shown below.

Next edit your `apollo.config.json` to look like this:

```json
{
  "rover": {
    // optional, if your rover binary is in PATH it will automatically be detected
    "bin": "/path/to/rover",
    // optional, defaults to `supergraph.yaml` in the folder of the configuration file
    "supergraphConfig": "/path/to/supergraph.yaml",
    // optional, defaults to the Rover default profile
    "profile": ""
  }
}
```

Since all these options are optional, you can specify only the `rover` key to indicate you're using Rover for schema development rather than client development:

```json
{
  "rover": {}
}
```

Afterward, reload VS Code. The Apollo extension will start using Rover to help you build your supergraph.

#### Configure extension for client development with introspection from a locally running service

To experiment with designs under active development, you can link the editor to a locally running version of a schema. Link the `apollo.config.json` file to a local service definition like so:

```json
{
  "client": {
    "service": {
      "name": "my-graphql-app",
      "url": "http://localhost:4000/graphql"
    }
  }
}
```

Linking to local schemas won't provide all extension features, such as switching graph variants and performance metrics.

#### Configure extension for client development with local schema files

You might not always have a running server to link to, so the extension also supports linking to a local schema file.
This is useful for working on a schema in isolation or for testing out new features.
To link to a local schema file, add the following to the `apollo.config.json` file:

```json
{
  "client": {
    "service": {
      // can be a string pointing to a single file or an array of strings
      "localSchemaFile": "./path/to/schema.graphql"
    }
  }
}
```

#### Bonus: Adding client-only schemas

One of the best features of the VS Code extension is the automatic merging of remote and local schemas when using integrated state management with Apollo Client. This happens automatically whenever schema definitions are found within a client project. By default, the VS Code extension will look for all JavaScript, TypeScript, and GraphQL files under `./src` to find both the operations and schema definitions for building a complete schema for the application.

Client-side schema definitions can be spread throughout the client app project and will be merged to create one single schema. You can set the default behavior by adding specifications to the `apollo.config.json`:

```json
{
  "client": {
    // "service": <your service configuration>,
    // array of glob patterns
    "includes": ["./src/**/*.js"],
    // array of glob patterns
    "excludes": ["**/__tests__/**"]
  }
}
```

### Get the extension

Once you have a config set up and a schema published, [install the Apollo GraphQL extension](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo), then try opening a file containing a GraphQL operation.

After opening a file, click the status bar icon to open the output window and see stats about the project associated with that file. This is helpful for confirming that the project is set up properly.

## Features

Apollo for VS Code offers a range of useful features for working on GraphQL projects.

### Intelligent autocomplete

Once configured, VS Code has full knowledge of the schema clients are running operations against, including client-only schemas (for things like local state mutations). Because of this, it have the ability to autocomplete fields and arguments as you type.

### Inline errors and warnings

VS Code can use local or published schemas to validate operations before running them. **Syntax errors**, **invalid fields or arguments**, and even **deprecated fields** instantly appear as errors or warnings in your editor, ensuring your entire team is working with the most up-to-date production schemas.

### Inline field type information

Because of GraphQL's strongly typed schema, VS Code knows not only which fields and arguments are valid, but also what types are expected. Hover over any type in a valid GraphQL operation to see what type that field returns and whether or not it can be null.

### Performance insights

GraphQL's flexibility can make it difficult to predict the cost of an operation. Without insight into how expensive an operation is, developers can accidentally write queries that place strain on their graph API's underlying backends. Thanks to the Apollo platform's integration with VS Code and our trace warehouse, teams can avoid these performance issues by instantly seeing the cost of a query in their editor.

The VS Code extension will show inline performance diagnostics when connected to a service with reported metrics in GraphOS Studio. As operations are typed, any fields that take longer than 1 ms to respond will be annotated to the right of the field inline. This shows team members how long the operation will take as more and more fields are added to operations or fragments.

### Syntax highlighting

Apollo's editor extension provides syntax highlighting for all things GraphQL, including schema definitions in `.graphql` files, complex queries in TypeScript, and even client-only schema extensions. Syntax highlighting for GraphQL works out-of-the-box in GraphQL, JavaScript, TypeScript, Python, Lua, Ruby, Dart, Elixir, and ReasonML files.

### Supergraph editing

The extension provides features for supergraph editing, such as support for Federation directives, subgraph-spanning go-to-definition, and reporting composition errors directly to the **Problems** panel.

### Navigating projects

Navigating large codebases can be difficult, but the Apollo GraphQL extension makes this easier. Right-clicking on any field in operations or schemas allows you to jump to (or peek at) definitions and find any other references to that field in your project.

### Schema tag switching

Apollo supports publishing multiple versions ([variants](https://www.apollographql.com/docs/graphos/graphs/#variants)) of a schema. This is useful for developing on a future development schema and preparing your clients to conform to that schema. To switch between graph variants, open the Command Palette (`cmd + shift + p` on mac), search "Apollo" and choose the "Apollo: Select Schema Tag" option.

### Developing Connectors

Starting with version 2.3.3, the Apollo GraphQL VS Code extension can give you fast feedback on your Apollo Connectors in VS Code.
Through it, you can get the *same* validations that composition provides, with errors and hints highlighted in your schema file on each save.

#### Prerequisites

These composition-based diagnostics are powered by Rover. You'll need Rover version 0.27.0 or later [installed](https://www.apollographql.com/docs/rover/getting-started) to use composition-based diagnostics.

#### Connector configuration

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

### (Experimental) Apollo Client DevTools in your IDE

The Apollo VS Code extension ships with an instance of the [Apollo Client Devtools](https://chromewebstore.google.com/detail/apollo-client-devtools/jdkknkkbebbapilgoeccciglkfbmbnfm).
You can use it to remotely debug your client, making it easier to debug React Native and Node.js applications.

To configure it, follow these steps:

1. In the VS code settings dialog, set **Apollographql > Dev Tools: Show Panel** to `detect` or `always`.

2. In your code base, install the `@apollo/client-devtools-vscode` package:

   ```sh
   npm install @apollo/client-devtools-vscode
   ```

3. After initializing your `ApolloClient` instance, call `connectApolloClientToVSCodeDevTools` with your client instance.

   ```js
   import { connectApolloClientToVSCodeDevTools } from "@apollo/client-devtools-vscode";

   const client = new ApolloClient({ /* ... */ });

   // We recommend wrapping this statement in a check for e.g. process.env.NODE_ENV === "development"
   const devtoolsRegistration = connectApolloClientToVSCodeDevTools(
     client,
     // the default port of the VSCode DevTools is 7095
     "ws://localhost:7095",
   );
   ```

4. Open the **Apollo Client DevTools** panel in VS Code.

5. Start your application. It should automatically connect to the DevTools.

## Troubleshooting

The most common errors are configuration errors, like a missing `.env` file or incorrect service information in the `apollo.config.json` file.

An old version of a published schema may cause other errors. To reload a schema, open the **Command Palette** (`cmd + shift + p` on Mac), search for "Apollo." Choose the **Apollo: Reload Schema** option.

Sometimes, errors will appear as a notification at the bottom of your editor. Other, less critical, messages may be shown in the output pane of the editor. To open the output pane and get diagnostic information about the extension and the current service loaded (if working with a client project), click the Apollo GraphQL icon in the status bar at the bottom.

If problems persist or the error messages are unhelpful, open an [issue](https://github.com/apollographql/vscode-graphql/issues)
in the `vscode-graphql` repository.

### Reloading the extension

If you aren't seeing diagnostics, try reloading the extension by running the `Apollo: Reload schema` command from the command palette.

### Turn on autosave

Most diagnostics will only appear when you save your schema file.
If you enable autosave in VS Code, you'll see feedback each time you finish typing.

### Double-check your Rover version

If you aren't seeing diagnostics for Apollo Connectors, run `rover --version` in a terminal to ensure you have version 0.27.0 or later.
You can also specify a path to a specific Rover binary in your `apollo.config.yaml` file:

```yaml title=apollo.config.yaml
rover:
  bin: /path/to/rover
```

### Debug logging

If the extension isn't working as expected, you can set the `apollographql.trace.server` setting to `verbose` in your VS Code settings.
This settings adds detailed logs to the output panel of the extension, which can aid in debugging.

## Additional Apollo config options

You can add these configurations to your [Apollo config file](https://www.apollographql.com/docs/ide-support/vs-code.md#setting-up-an-apollo-config).

### `client.tagName`

*Optional* - custom tagged template literal.

When using GraphQL with JavaScript or TypeScript projects, it is common to use the `gql` tagged template literal to write out operations. Apollo tools look through your files for the `gql` tag to extract your queries, so if you use a different template literal, you can configure it like so:

```json
{
  "client": {
    "tagName": "graphql",
    "service": //...
  }
}
```
