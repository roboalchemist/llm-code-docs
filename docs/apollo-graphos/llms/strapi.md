# Source: https://www.apollographql.com/docs/graphos/connectors/library/strapi.md

# Strapi Connector

Strapi is a headless CMS that provides a customizable API for content management.
The [prebuilt Strapi Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/strapi) provides a GraphQL interface for Strapi's REST API, allowing you to integrate your Strapi content into your federated graph.

## Connector capabilities

This Connector incorporates Strapi REST API [content-types](https://docs.strapi.io/cms/api/rest) into your graph.

## Prerequisites

To use the Connector, you need:

* A Strapi instance with REST API enabled
* API token for authentication (if required)

## Try out the Connector

Use the Apollo Sandbox below to test out the Connector.
This is the same interface you use locally to test your queries.

Starting with the `Products` query is easiest since it doesn't require any parameters.

## Getting started

1. If you haven't already, [create a new graph in GraphOS](https://www.apollographql.com/docs/quickstart#step-1-create-a-graph).

2. Copy the `supergraph.yaml` and `router.yaml` files from the [Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/strapi) to replace the files created by running `rover init`.

3. Set your Strapi endpoint and API token as environment variables in your terminal:

   ```terminal
   export STRAPI_API_URL=....
   export STRAPI_API_TOKEN=....
   ```

4. Run `rover dev` to start the local development session:

   ```terminal
   APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
     APOLLO_GRAPH_REF=My-Graph-s1ff1u@main \
     rover dev --supergraph-config supergraph.yaml --router-config router.yaml
   ```

You're all set! Open [`http://localhost:4000`](http://localhost:4000/) to query your graph using [Apollo Sandbox](https://www.apollographql.com/docs/graphos/platform/sandbox).

### Adding to an existing graph in GraphOS

To add this Connector to an existing graph, publish the schema ` strapi.graphql` file to your graph ref using `rover subgraph publish`:

```terminal
APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
  rover subgraph publish My-Graph-s1ff1u@main --name strapi --schema strapi.graphql --routing-url http://strapi
```

## Setup VS Code task runner

Once you've set up the VS Code task runner, you can execute the `Tasks: Run Task` command in VS Code to run the `rover dev` task.
Edit your `.vscode/settings.json` to include the following Strapi-specific keys:

```terminal
{
  "terminal.integrated.profiles.osx": {
    "graphos": {
      "path": "zsh",
      "args": ["-l"],
      "env": {
        "STRAPI_API_URL": "",
        "STRAPI_API_TOKEN": "",
        ...
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

* Support for complex relationships between content types
* Real-time data subscriptions
* Media library management
* User and permissions management

See the [Strapi REST API Documentation](https://docs.strapi.io/developer-docs/latest/developer-resources/database-apis-reference/rest-api.html) for other features to implement.
