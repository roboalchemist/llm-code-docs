# Source: https://grafbase.com/docs/federation/overview.md

# Federation

The purpose of Federation is to create a single, unified graph from many subgraphs. Some form of this idea has been around for a long time under the name "schema stitching", but Federation goes further by letting the federated GraphQL APIs — called "subgraphs" — declaratively extend each other and share parts of their API surface, in a way that is seamless and transparent for consumers of the Federated graph.

## Composition

Composition is the process of combining the schemas of all the subgraphs in a federated graphs into a single federated schema. The subgraphs can evolve independently most of the time, but composition has rules on what is valid or not.

Composition happens in the schema registry whenever you [publish a subgraph](https://grafbase.com/docs/platform/schema-registry.md) or run a [schema check](https://grafbase.com/docs/platform/schema-checks.md).

Without [subgraph directives](https://grafbase.com/docs/federation/graphql-directives.md), the following basic rules apply:

**Object types** can be defined in any number of subgraphs, but each of their fields can only be defined in a single subgraph (the same field cannot be defined in two subgraphs). That each field belongs to a single subgraph that is responsible for resolving it.

The same rule applies to **interfaces**.

When the same **input type** is present in multiple subgraphs, composition will reduce it to the fields that are defined in all subgraphs, and exclude any field that is defined in some subgraphs but not others. If any nonnullable field is excluded, that triggers a composition errors. The same rule applies to field arguments.

**Enums** are composed based on how they are used:

- For enums that are used only in input types and field arguments, composition will only preserve the values of the enum that are common between all subgraphs
- For enums that are used only as output field types, composition will preserve all values from all subgraphs
- Enums that are used both in input and output position must match exactly between subgraphs, else that will be a composition error.

Composition will accumulate and merge all members for each **union** across all subgraphs.

**Directives** are not preserved in the composed schema except for built-ins like `@deprecated`.

This set of rules is of course very limiting in how much subgraphs can evolve together and integrate into a coherent, unified API. Read the following section entities and the [subgraph directives](https://grafbase.com/docs/federation/graphql-directives.md) page to understand how subgraphs can be better integrated.

## Runtime

At runtime, a federated setup is made up of three components:

- The subgraphs. They are regular GraphQL APIs that can use federation directives to interact with composition
- The [schema registry](https://grafbase.com/docs/platform/schema-registry.md), responsible for storing and composing published subgraph schemas
- The gateway, that serves the Federated Graph based on the schema composed by the schema registry

In the context of Grafbase, the subgraphs will be your standalone graphs or regular GraphQL APIs hosted on Grafbase or somewhere else. The schema registry is part of the platform; you interact with it through the web dashboard and the Grafbase CLI. The [Grafbase Gateway](https://grafbase.com/docs/gateway/installation.md) is a GraphQL router and gateway you run in your own premises. The gateway either always fetches the composed schema from the schema registry or can be configured to load it from a local file.

## Entities

The most important mechanism for subgraphs to combine with each other.

An entity is defined as an object annotated with the [`@key` directive](https://grafbase.com/docs/federation/graphql-directives.md):

```graphql
type Product @key(fields: "id") {
  id: String!
  name: String!
  createdAt: DateTime!
}
```

The fields in `@key` uniquely identify the object across subgraphs, similar to the primary key in a database. When you use a GraphQL library compatible with federation to define a subgraph, each object annotated with `@key` will require that you write an entity resolver that can retrieve the object based on that key. For example in Apollo Server:

```js
const resolvers = {
  User: {
    __resolveReference(object) {
      return fetchUserById(object.id) // fetchUserById is a hypothetical function that retrieves a User by their ID
    },
  },
}
```

The gateway knows which subgraphs can resolve which fields on each entity, so for example, if you have a comments subgraph for a blog API with the following API:

```graphql
type BlogPost @key(fields: "id") {
  id: ID!
  comments: [Comment!]
}
```

and a search subgraph with the following:

```graphql
type BlogPost @key(fields: "id") {
  id: ID!
}

type Query {
  findBlogPosts(filters: Filters): [BlogPost!]
}
```

you can query the gateway with queries that bridge the subgraphs transparently:

```graphql
query {
  findBlogPosts(filters: [...]) {
    id
    comments {
      id
      title
      author { name }
      text
    }
  }
}
```