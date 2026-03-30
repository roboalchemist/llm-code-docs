# Source: https://www.apollographql.com/docs/graphos/connectors/library/anthropic.md

# Anthropic Connector

Anthropic provides AI models for text understanding, reasoning, and safe conversations.
The [prebuilt Anthropic Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/anthropic) provides a GraphQL interface for Anthropic's AI models and services, allowing you to integrate Anthropic's capabilities into your graph.

## Connector capabilities

This Connector provides your graph access to the Anthropic API's [Messages endpoints](https://docs.anthropic.com/en/api/messages).

## Prerequisites

To use the Connector, you need an [Anthropic API key](https://docs.anthropic.com/claude/reference/getting-started-with-the-api).

## Try out the Connector

Use the Apollo Sandbox below to test out the Connector.
This is the same interface you use locally to test your queries.

To use this sandbox you either need to add your Anthropic key as a header or copy and paste placeholder values.

1. In the sandbox, below the **Operations** panel, open the **Headers** tab then click **Add a new header**.
2. Add a new header with the name `x-api-key` and your Anthropic API key as the value.
3. Select and run a query from the **Documentation** tab to test.

1) Copy and paste the following into the **Operations** panel in Sandbox:

   ```graphql
   mutation GenerateStory($about: [MessageInput]!) {
     createMessage(messages: $about) {
       id
       model
       role
       usage {
         inputTokens
         outputTokens
       }
       content {
         type
         text
       }
     }
   }
   ```

2) Copy and paste the following into the **Variables** panel below **Operations**:

   ```JSON
   {
     "about": [
       {
         "role": "USER",
         "content": "The story about Apollo"
       }
     ]
   }
   ```

3) Run the operation.

## Getting started

1. If you haven't already, [create a new graph in GraphOS](https://www.apollographql.com/docs/quickstart#step-1-create-a-graph).

2. Copy the `supergraph.yaml` and `router.yaml` files from the [Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/anthropic) to replace the files created by running `rover init`.

3. Set your Anthropic API key as an environment variable in your terminal:

   ```terminal
   export ANTHROPIC_API_KEY=....
   ```

4. Run `rover dev` to start the local development session:

   ```terminal
   APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
     APOLLO_GRAPH_REF=My-Graph-s1ff1u@main \
     rover dev --supergraph-config supergraph.yaml --router-config router.yaml
   ```

You're all set! Open [`http://localhost:4000`](http://localhost:4000/) to query your graph using [Apollo Sandbox](https://www.apollographql.com/docs/graphos/platform/sandbox).

### Adding to an existing graph in GraphOS

To add this Connector to an existing graph, publish the schema ` anthropic.graphql` file to your graph ref using `rover subgraph publish`:

```terminal
APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
  rover subgraph publish My-Graph-s1ff1u@main --name anthropic --schema anthropic.graphql --routing-url http://anthropic
```

## Setup VS Code task runner

Once you've set up the VS Code task runner, you can execute the `Tasks: Run Task` command in VS Code to run the `rover dev` task.
Edit your `.vscode/settings.json` to include the following Anthropic-specific key:

```terminal
{
  "terminal.integrated.profiles.osx": {
    "graphos": {
      "path": "zsh",
      "args": ["-l"],
      "env": {
        "ANTHROPIC_API_KEY": "",
        "APOLLO_KEY": ""
      }
    }
  },
  "terminal.integrated.defaultProfile.osx": "graphos"
}
```

Alternatively, you can open a new terminal window in VS Code with the `graphos` profile, then run `rover dev --supergraph-config supergraph.yaml --router-config router.yaml`.

## Contributing

The Connectors Community welcomes contributions to this Connector or to expand the library. For instructions on how to contribute, see the [contributing guide](https://github.com/apollographql/connectors-community?tab=readme-ov-file#contributing-a-connector-to-the-community).

### Modules to contribute

The following features can be added to this Connector:

* Support for newer Claude models
* Stream response handling
* Additional Anthropic API endpoints

See the [Anthropic API Documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api) for other features to implement.
