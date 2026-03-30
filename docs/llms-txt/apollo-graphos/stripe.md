# Source: https://www.apollographql.com/docs/graphos/connectors/library/stripe.md

# Stripe Connector

Stripe is a payments platform that provides a REST API to support multiple checkout flows.
The [prebuilt Stripe Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/stripe) provides a GraphQL interface for Stripe's services.

## Connector capabilities

This Connector can incorporate the following [Stripe REST API](https://docs.stripe.com/api) endpoints into your graph:

* [Checkout](https://docs.stripe.com/api/checkout/sessions)
* Core resources, like [Customers](https://docs.stripe.com/api/customers?api-version=2025-05-28.basil) and [Payment Intents](https://docs.stripe.com/api/payment_intents?api-version=2025-05-28.basil)
* [Payment methods](https://docs.stripe.com/api/payment_methods?api-version=2025-05-28.basil)
* [Products](https://docs.stripe.com/api/products?api-version=2025-05-28.basil)

## Prerequisites

To use the Connector, you need a [Stripe API key](https://docs.stripe.com/keys).

## Try out the Connector

Use the Apollo Sandbox below to test out the Connector.
This is the same interface you use locally to test your queries.

Starting with the `Products` query is easiest since it doesn't require any parameters.
Other available queries are listed on the left. Click one to add fields to your query and run to see the response.

## Getting started

1. If you haven't already, [create a new graph in GraphOS](https://www.apollographql.com/docs/quickstart#step-1-create-a-graph).

2. Copy the `supergraph.yaml` and `router.yaml` files from the [Connector](https://github.com/apollographql/connectors-community/tree/main/connectors/stripe) to replace the files created by running `rover init`.

3. Set your Stripe API key as an environment variable in your terminal:

   ```terminal
   export STRIPE_API_KEY=....
   ```

4. Run `rover dev` to start the local development session:

   ```terminal
   APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
     APOLLO_GRAPH_REF=My-Graph-s1ff1u@main \
     rover dev --supergraph-config supergraph.yaml --router-config router.yaml
   ```

You're all set! Open [`http://localhost:4000`](http://localhost:4000/) to query your graph using [Apollo Sandbox](https://www.apollographql.com/docs/graphos/platform/sandbox).

### Adding to an existing graph in GraphOS

To add these Connectors to an existing graph, publish the schema ` products.graphql` file to your graph ref using `rover subgraph publish`:

```terminal
APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
  rover subgraph publish My-Graph-s1ff1u@main --name products --schema products.graphql --routing-url http://products

APOLLO_KEY=service:My-Graph-s1ff1u:•••••••••••••••••••••• \
  rover subgraph publish My-Graph-s1ff1u@main --name checkout --schema checkout.graphql --routing-url http://checkout
```

## Setup VS Code task runner

Once you've set up the VS Code task runner, you can execute the `Tasks: Run Task` command in VS Code to run the `rover dev` task.
Edit your `.vscode/settings.json` to include the following Stripe-specific key:

```terminal
{
  "terminal.integrated.profiles.osx": {
    "graphos": {
      "path": "zsh",
      "args": ["-l"],
      "env": {
        "STRIPE_API_KEY": "",
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

The following schema modules can be added to this Connector:

* [Payment Link](https://docs.stripe.com/api/payment-link)
* [Billing](https://docs.stripe.com/api/billing)
* Additional modules listed in the left column of the [Stripe API documentation](https://docs.stripe.com/api)

To contribute a new module:

1. Add a schema designed for the module as a new `.graphql` file
2. Update the `router.yaml` and `supergraph.yaml` files accordingly

You can use the current modules in this folder as examples to start from.
