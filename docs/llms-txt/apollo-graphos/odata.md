# Source: https://www.apollographql.com/docs/graphos/connectors/library/odata.md

# OData Connector

OData (Open Data Protocol) is a standard protocol for building and consuming RESTful APIs.
The [prebuilt OData Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/odata) provides a GraphQL interface for OData services, allowing you to integrate OData endpoints into your federated graph.

## Connector capabilities

This Connector represents an example service created with OData. For information on how to create your own services, check the [OData documentation](https://www.odata.org/getting-started/basic-tutorial/).

## Prerequisites

To use the Connector, you need:

* Access to an OData service endpoint
* Authentication credentials if required by the service

## Try out the Connector

Use the Apollo Sandbox below to test out the Connector.
This is the same interface you use locally to test your queries.

Starting with the `People` query is easiest since it doesn't require any parameters.

## Getting started

1. If you haven't already, [create a new graph in GraphOS](https://www.apollographql.com/docs/quickstart#step-1-create-a-graph).

2. Copy the `supergraph.yaml` and `router.yaml` files from the [Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/odata) to replace the files created by running `rover init`.

3. Set your OData service URL as an environment variable in your terminal:

   ```terminal
   export ODATA_SERVICE_URL=....
   ```

4. Run `rover dev` to start the local development session:

   ```terminal
   APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
     APOLLO_GRAPH_REF=My-Graph-s1ff1u@main \
     rover dev --supergraph-config supergraph.yaml --router-config router.yaml
   ```

You're all set! Open [`http://localhost:4000`](http://localhost:4000/) to query your graph using [Apollo Sandbox](https://www.apollographql.com/docs/graphos/platform/sandbox).

### Adding to an existing graph in GraphOS

To add this Connector to an existing graph, publish the schema ` odata.graphql` file to your graph ref using `rover subgraph publish`:

```terminal
APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
  rover subgraph publish My-Graph-s1ff1u@main --name odata --schema odata.graphql --routing-url http://odata
```

## Setup VS Code task runner

Once you've set up the VS Code task runner, you can execute the `Tasks: Run Task` command in VS Code to run the `rover dev` task.
Edit your `.vscode/settings.json` to include the following OData-specific key:

```terminal
{
  "terminal.integrated.profiles.osx": {
    "graphos": {
      "path": "zsh",
      "args": ["-l"],
      "env": {
        "ODATA_SERVICE_URL": "",
        "ODATA_USERNAME": "",
        "ODATA_PASSWORD": "",
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

* Support for OData v4.0 features
* Query and filter operations
* Comprehensive entity relationship mapping
* Advanced metadata handling

See the [OData Documentation](https://www.odata.org/documentation/) for other features to implement.
