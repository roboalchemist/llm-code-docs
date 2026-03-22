# Source: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition.md

# Schema Composition

In Apollo Federation, *composition* is the process of combining a set of subgraph schemas into a supergraph schema:

```mermaid
graph TB;
  serviceA[Subgraph<br/>schema<br/>A];
  serviceB[Subgraph<br/>schema<br/>B];
  serviceC[Subgraph<br/>schema<br/>C];
  composition[["🛠<br/>Composition "]];
  supergraph{{"Supergraph schema<br/>(A + B + C + routing machinery)"}};
  serviceA & serviceB & serviceC --> composition;
  composition -- "(Composition succeeds)" --> supergraph;
  class composition tertiary;
```

The supergraph schema includes all of the type and field definitions from your subgraph schemas. It also includes metadata that enables your router to intelligently route incoming GraphQL operations across all of your different subgraphs.

## Supported methods

You can perform schema composition with any of the following methods:

### Automatically with GraphOS

Apollo GraphOS performs composition automatically whenever you publish a subgraph schema.
This enables your running router to dynamically fetch an updated supergraph schema from Apollo as soon as it's available:

```mermaid
graph LR;
  subgraph "Your infrastructure"
  serviceA[Products<br/>subgraph];
  serviceB[Reviews<br/>subgraph];
  gateway([Router]);
  end
  subgraph "GraphOS"
    registry{{Schema Registry}};
    uplink{{Apollo<br/>Uplink}}
  end
  serviceA & serviceB -->|Publishes schema| registry;
  registry -->|Updates config| uplink;
  gateway -->|Polls for config changes| uplink;
  class registry secondary;
  class uplink secondary;
```

GraphOS also provides a [schema linter](https://www.apollographql.com/docs/graphos/platform/schema-management/linting) with [composition specific rules](https://www.apollographql.com/docs/graphos/platform/schema-management/linting/rules#composition-rules) to help you follow best practices. You can set up schema checks for your graph in GraphOS Studio or perform one-off linting with the Rover CLI. Check out the [schema linting](https://www.apollographql.com/docs/graphos/platform/schema-management/linting) docs to learn more.

### Manually with the Rover CLI

The [Rover CLI](https://www.apollographql.com/docs/rover/) supports a `supergraph compose` command that you can use to compose a supergraph schema from a collection of subgraph schemas:

```bash
rover supergraph compose --config ./supergraph-config.yaml
```

To learn how to install Rover and use this command, see the [Rover docs](https://www.apollographql.com/docs/rover/).

## Breaking composition

Sometimes, your subgraph schemas might conflict in a way that causes composition to fail. This is called *breaking composition*.

For example, take a look at these two subgraph schemas:

❌

```graphql title=Subgraph A
type Event @shareable {
  timestamp: String!
}
```

```graphql title=Subgraph B
type Event @shareable {
  timestamp: Int!
}
```

One subgraph defines `Event.timestamp` as a `String`, and the other defines it as an `Int`. Composition doesn't know which type to use, so it fails.

For examples of valid inconsistencies in field return types, see [Differing shared field return types](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types/#return-types).

Breaking composition is a helpful feature of federation! Whenever a team modifies their subgraph schema, those changes might conflict with another subgraph. But that conflict won't affect your router, because composition fails to generate a new supergraph schema. It's like a compiler error that prevents you from running invalid code. Refer to the [Composition Rules Reference](https://www.apollographql.com/docs/graphos/reference/federation/composition-rules) for details.

## Next steps

Ready to compose your first supergraph? [Get started with GraphOS!](https://www.apollographql.com/docs/graphos/get-started/guides/quickstart)
