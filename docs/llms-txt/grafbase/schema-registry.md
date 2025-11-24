# Source: https://grafbase.com/docs/platform/schema-registry.md

# Schema Registry

The Schema Registry tracks published schemas and helps you evolve your APIs with [Schema Checks](https://grafbase.com/docs/platform/schema-checks.md). Use the CLI and Grafbase dashboard to interact with the registry.

## Managing a Federated Graph

In a federated graph, the schema registry tracks published subgraphs. The schema registry uses this tracking to:

- Compose subgraph schemas into a federated graph schema
- Help you evolve schemas individually and as a group (see [Schema checks](https://grafbase.com/docs/platform/schema-checks.md))

Each branch of a federated graph contains its own set of subgraphs. Each subgraph represents a live, deployed GraphQL endpoint that you can manage on Grafbase or deploy anywhere else.

The schema registry views each subgraph as a record with these properties:

- `name`: The identifier for a subgraph within a branch. It corresponds to the `--name` argument in the CLI publish and check commands. The schema and subgraph URL can change, but the name remains the same.
- `url`: The endpoint where the subgraph runs. It corresponds to the `--url` argument of the CLI publish command.
- `schema`: The GraphQL schema of the subgraph. It corresponds to the `--schema` argument of the CLI command.

The schema registry tracks published subgraphs, their names, URLs and schemas. After each change, it attempts to _compose_ the subgraphs into a federated graph.

## Publishing a Subgraph

The schema registry composes the federated graph's schema from subgraph schemas. To update the federated graph's schema, publish your subgraphs.

Read more on publishing from the [reference documentation](https://grafbase.com/docs/cli/commands/publish.md).

### Publish Workflow

We recommend publishing a subgraph schema each time you deploy a new version of the subgraph. You can publish an unchanged schema multiple times safely without side effects.

As described in [composition](#schema-composition), publishing an updated subgraph schema can have these effects:

- If composition fails, your federated graph's schema doesn't update until you fix the composition errors.
- If composition succeeds, the federated graph's schema updates but your changes might break existing clients (for example, when you remove a field or change its type).

Use [Schema Checks](https://grafbase.com/docs/platform/schema-checks.md) to verify that publishing your new or updated schema is safe.

### Schema Composition

When you [publish](#publishing-a-subgraph) a subgraph, the registry attempts to compose it with all other subgraphs published in the branch.

When composition succeeds, it creates a new federated graph schema. The router uses that schema as the new public facing API for the federated graph.

When composition fails, the federated graph continues running with the previous working federated schema. The branch enters a state where the subgraphs don't compose. You'll see composition errors and hints about how to fix them on each new publish and check, until the subgraph schemas compose without error.

<CardWidget>

Publishing succeeds even when it creates composition errors and puts a branch in a failing state, because valid migration workflows require this behavior.

For example, when you move a type from subgraph A to subgraph B, you can use this zero downtime, non-breaking migration path that temporarily prevents the subgraphs from composing:

1. Add the type to subgraph B.
2. Publish and deploy subgraph B.
3. Delete the type from subgraph A.
4. Publish and deploy subgraph A.

Between steps 2 and 4, the branch won't compose because multiple subgraphs own the type, but subgraph A continues to serve queries for the type.

</CardWidget>

## Listing Subgraphs

Use the `grafbase subgraphs` command to list published subgraphs in a branch.

Example:

```bash
grafbase subgraphs tomhoule/schema-check-action-federated-graph-example@main

Subgraphs:

-  manufacturing
-  retail
```

## Inspecting Schemas

Use the `grafbase schema` command to inspect subgraph and federated graph schemas.

To view a specific subgraph's GraphQL schema, use the `--name` argument:

```bash
grafbase schema tomhoule/schema-check-action-federated-graph-example@main --name retail
# < prints the whole GraphQL schema >
```

The CLI prints the composed schema of the federated graph when you omit the `--name` argument.

## Changelog

View changes to schemas and public API in your graph from the Changelog tab in the dashboard. The Changelog shows an overview of GraphQL API schema changes for each deployment.

![Changelog tab in the dashboard](/images/docs/schema-registry/changelog.png)