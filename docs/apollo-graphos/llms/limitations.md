# Source: https://www.apollographql.com/docs/apollo-mcp-server/limitations.md

# Source: https://www.apollographql.com/docs/graphos/connectors/reference/limitations.md

# Limitations of Apollo Connectors

Apollo Connectors have the following limitations.

## Some supergraphs are unsupported

A small fraction of supergraphs will not compose when adding a Connector. If you add a Connector and see a number of unrelated errors after composing (usually related to [`SATISFIABILITY`](https://www.apollographql.com/docs/graphos/connectors/troubleshooting#satisfiability-errors)), then you've likely encountered this limitation.

## Abstract schema types

Connectors v0.4 and later support abstract schema types (`interface` and `union`). See [Preview features](https://www.apollographql.com/docs/graphos/connectors/reference/preview-features#abstract-type-support) for details on enabling and using abstract types.

[Connectors v0.4 preview 3](https://www.apollographql.com/docs/graphos/connectors/reference/changelog#2024-12-09) adds support for [`@interfaceObject`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/interfaces).

Connectors v0.3 and earlier do not support abstract types. To work around this limitation for `union` types, create a new type that combines all properties from each possible return type. Mark any non-overlapping fields as nullable.

```graphql title=Unsupported schema with abstract type
type Query {
  products: [Product]
    @connect(
      http: { GET: "/products" }
      selection: """
      $.results {
        id
        title
        author { name }
        director { name }
      }
      """
    )
}

union Product = Book | Film

type Book {
  id: ID!
  title: String
  author: Person!
}

type Film {
  id: ID!
  title: String
  director: Person!
}

type Person {
  id: ID
  name: String
}
```

```graphql title=Workaround without abstract types
type Query {
  products: [Product]
    @connect(
      http: { GET: "https://api.example.com/products" }
      selection: """
      $.results {
        id
        title
        author { name }
        director { name }
      }
      """
    )
}

type Product {
  id: ID!
  title: String!
  author: Person # nullable
  director: Person # nullable
}

type Person {
  id: ID
  name: String
}
```

## Circular references are unsupported

Connectors don't yet support circular references in GraphQL schemas.
See [troubleshooting](https://www.apollographql.com/docs/graphos/schema-design/connectors/troubleshooting#circular-references) for details.

## Subscriptions are unsupported

Currently, you can use `@connect` on fields of the `Query` and `Mutation` types, but not on fields of the `Subscription` type.

## Unsupported federation directives

The following Apollo Federation directives are unsupported:

* `@context`
* `@fromContext`

## Partially supported federation directives

The `@override` directive is supported with some limitations.

`@override` is supported for fields transitioning from subgraphs that use resolvers to subgraphs that use Connectors.

```graphql title=subgraph-with-resolvers
type Query {
  products: [Product]
}
```

```graphql title=subgraph-with-connectors
type Query {
  products: [Product]
    @override(from: "subgraph-with-resolvers") # ✅
    @connect(...)
}
```

`@override` is not supported for fields transitioning from subgraphs that use Connectors to subgraphs that use resolvers.

```graphql title=subgraph-with-resolvers
type Query {
  products: [Product] @override(from: "subgraph-with-connectors") # ❌
}
```

```graphql title=subgraph-with-connectors
type Query {
  products: [Product] @connect(...)
}
```

## Interactions with GraphOS Router features

The following GraphOS Router features are not yet supported with Connectors:

* Entity caching
* Rhai scripting and coprocessors. The `router`, `supergraph`, and `execution` hooks work as expected, but Connectors don't have an equivalent to the `subgraph` hook.
