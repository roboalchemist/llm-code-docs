# Source: https://www.apollographql.com/docs/apollo-operator/get-started/add-subgraphs.md

# Source: https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md

# Add a Subgraph

This guide helps you get started building a new subgraph that you can then add to your GraphOS supergraph.

* If you're building a new GraphQL API from scratch, we recommend [starting from a template](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md#starting-from-a-template).
* If you already have a GraphQL API to use as a subgraph, see [Starting with an existing API](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md#starting-with-an-existing-api).

Before you get started, you may want to check out the [Graphs and Variants](https://www.apollographql.com/docs/graphos/get-started/concepts/graphos) article for a conceptual overview.

## Starting from a template

The fastest way to create a new subgraph is to start with one of the templates provided by the [Rover CLI](https://www.apollographql.com/docs/rover/commands/template). The `rover template` command generates the skeleton of a new subgraph for you, so you can immediately begin defining your schema and implementing your resolvers.

If your installed version of Rover doesn't include the `template` command (or if you don't have Rover installed at all), [install the latest version.](https://www.apollographql.com/docs/rover/getting-started/)

You start by running `rover template use`, providing it the ID of your chosen template. For example, the following command creates a new directory called `my-subgraph` that contains the boilerplate code for a subgraph written in TypeScript using the Apollo Server library:

```bash
rover template use "my-subgraph" --template="subgraph-typescript-apollo-server"
```

To see the full list of available templates, see the [Rover template docs](https://www.apollographql.com/docs/rover/commands/template)

After generating the boilerplate code, you can start filling in your business logic. The generated code includes example resolvers for `Query` and `Mutation`, along with some [entity types](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro#entity-overview) to use as your starting point. All templates also come with example GitHub Actions workflows to help with [publishing your schema in CI/CD](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish/#publish-with-continuous-delivery).

When you're ready to add your new subgraph to your supergraph, [see below](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md#adding-to-your-supergraph).

## Starting with an existing API

If you have an existing GraphQL API that you want to use as a subgraph, confirm whether it uses a [subgraph-compatible library](https://www.apollographql.com/docs/graphos/federated-schemas/reference/compatible-subgraphs).

* If it does, consult the library's documentation to determine how to enable its support for Apollo Federation.
* If it doesn't, [open an issue to let us know](https://github.com/apollographql/apollo-federation-subgraph-compatibility/issues/new/choose) and we'll work with the library's maintainers to add support.

## Adding to your supergraph

You can add your new subgraph to your GraphOS supergraph in the following ways:

* [In GraphOS Studio](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md#adding-a-subgraph-in-graphos-studio) (cloud supergraphs only)
* [Via the Rover CLI](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md#adding-a-subgraph-via-the-rover-cli)

#### Adding a subgraph in GraphOS Studio

This method of adding a subgraph is available only to cloud supergraphs. For other graph types, see [Adding a subgraph via the Rover CLI](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs.md#adding-a-subgraph-via-the-rover-cli)

1. Go to your variant's **Subgraphs** page in Studio.

2. Click **Add a subgraph**.

3. In the dialog that appears, provide your subgraph's **Routing URL** (this is the URL that your supergraph's router will use to communicate with the subgraph), along with a **Subgraph Name**.

4. If Studio can't fetch your subgraph's schema automatically from the routing URL, click **Advanced options** to provide the schema another way (such as by pasting the schema directly or introspecting a locally running server).

5. Click **Add Subgraph**. When the action completes, your new subgraph is listed on the Subgraphs page.

#### Adding a subgraph via the Rover CLI

To add a subgraph to your supergraph with Rover, you publish the subgraph's schema! To do this, you use the exact same Rover command as [updating an existing subgraph](https://www.apollographql.com/docs/graphos/get-started/guides/graphql#step-3-publish-your-subgraphs). The only difference is that you provide the name of the new subgraph to the command.

[Learn about publishing subgraph schemas.](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/publish/#publish-subgraph-schemas)

## Next steps

Make sure you [configure your router](https://www.apollographql.com/docs/graphos/routing/configure-your-router) so that only GraphOS can query it.
