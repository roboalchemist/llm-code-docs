# Source: https://www.apollographql.com/docs/graphos/connectors/library/aws-lambda.md

# AWS Lambda Connector

AWS Lambda is a serverless compute service that lets you run code without provisioning or managing servers.
The [prebuilt AWS Lambda Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/aws-lambda) provides a GraphQL interface for AWS Lambda functions.

## Connector capabilities

This Connector lets you integrate Lambda functions into your graph.

## Prerequisites

To use the Connector, you need:

* AWS access credentials with permissions to invoke Lambda functions
* AWS Lambda functions deployed in your account

## Try out the Connector

Use the Apollo Sandbox below to test out the Connector.
This is the same interface you use locally to test your queries.

Starting with the `listFunctions` query is easiest since it doesn't require any parameters.
Available queries are listed on the left. Click one to add fields to your query and run to see the response.

## Getting started

1. If you haven't already, [create a new graph in GraphOS](https://www.apollographql.com/docs/quickstart#step-1-create-a-graph).

2. Copy the `supergraph.yaml` and `router.yaml` files from the [Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/aws-lambda) to replace the files created by running `rover init`.

3. Set your AWS credentials as environment variables in your terminal:

   ```terminal
   export AWS_ACCESS_KEY_ID=....
   export AWS_SECRET_ACCESS_KEY=....
   export AWS_REGION=us-east-1
   ```

4. Run `rover dev` to start the local development session:

   ```terminal
   APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
     APOLLO_GRAPH_REF=My-Graph-s1ff1u@main \
     rover dev --supergraph-config supergraph.yaml --router-config router.yaml
   ```

You're all set! Open [`http://localhost:4000`](http://localhost:4000/) to query your graph using [Apollo Sandbox](https://www.apollographql.com/docs/graphos/platform/sandbox).

### Adding to an existing graph in GraphOS

To add this Connector to an existing graph, publish the schema file to your graph ref using `rover subgraph publish`:

```terminal
APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
  rover subgraph publish My-Graph-s1ff1u@main --name lambda --schema lambda.graphql --routing-url http://lambda
```

## Setup VS Code task runner

Once you've set up the VS Code task runner, you can execute the `Tasks: Run Task` command in VS Code to run the `rover dev` task.
Edit your `.vscode/settings.json` to include the following AWS-specific keys:

```terminal
{
  "terminal.integrated.profiles.osx": {
    "graphos": {
      "path": "zsh",
      "args": ["-l"],
      "env": {
        "AWS_ACCESS_KEY_ID": "",
        "AWS_SECRET_ACCESS_KEY": "",
        "AWS_REGION": "us-east-1",
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

* Support for additional Lambda function invocation patterns
* Improved error handling and response formatting
* Schema updates to add new features

You can use the current implementation in the repository as an example to work with.
