# Source: https://www.apollographql.com/docs/ios/project-configuration/intro.md

# Source: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro.md

# Introduction to Entities

Before getting started with entities, you may want to check out the [Introduction to Apollo Federation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/federation) for a conceptual overview.

## Entity overview

In Apollo Federation, federated data objects are represented as *entities*. Entities are objects that can be fetched with one or more unique key fields. Like a row in a database table, an entity contains fields of various types, and it can be uniquely identified by a key field or set of fields.

Entities are defined in subgraph schemas. Each subgraph can contribute different fields to an entity it defines and is responsible for *resolving* it—returning only the fields that it contributes. This enables subgraphs to adhere to the separation of concerns principle.

An *entity type* is an object type that has been [defined as an entity](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro.md#defining-an-entity). Because an entity is keyed, an entity type's definition must have a `@key` directive. For example, this `Product` entity's fields are defined and resolved across two subgraphs:

```graphql title=Products subgraph
type Product @key(fields: "upc") {
  upc: ID!
  name: String!
  price: Int
}
```

```graphql title=Reviews subgraph
type Product @key(fields: "productUpc") {
  productUpc: ID!
  rating: Int!
}
```

Only object types can be entities.

The rest of this guide goes over how to define entities in your subgraph schemas and code.

## Defining an entity

To define an entity within a particular subgraph, you do the following:

1. Apply the [`@key` directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro.md#1-define-a-key) to an object type.
2. Define the object type's [reference resolver](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro.md#2-define-a-reference-resolver).

With Apollo Connectors, you add [connector directives](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives) instead of writing reference resolver code.

You can [set `entity: true`](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives#rules-for-entity-true) for the `@connect` directive to provide an entity resolver for its fields.

### 1. Define a `@key`

In a subgraph schema, you can designate any object type as an entity by adding the `@key` directive to its definition, like so:

```graphql title=Products subgraph
type Product @key(fields: "upc") {
  upc: ID!
  name: String!
  price: Int
}
```

The `@key` directive defines an entity's *unique key*, which consists of one or more of the type's `fields`.
In the previous example, the `Product` entity's unique key is its `upc` field.
Every instance of an entity must be uniquely identifiable by its `@key` field(s).
Key fields' uniqueness enable your router to associate fields from different subgraphs with the same entity instance.

In most cases, the `@key` field(s) for the same entity will be the same across subgraphs.
For example, if one subgraph uses `upc` as the `@key` field for the `Product` entity, other subgraphs should likely do the same.
However, this [isn't strictly required](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys/#differing-keys-across-subgraphs).

If coming from a database context, it can be helpful to think of a `@key` as an entity's [primary key](https://en.wikipedia.org/wiki/Primary_key).
This term isn't completely accurate for entities since a single entity can have [multiple `@key`s](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys/#multiple-keys). The field(s) you select for an entity's `@key` must, however, uniquely identify the entity.
In that way, `@key`s are similar to [candidate keys](https://en.wikipedia.org/wiki/Candidate_key).

```graphql title=Products subgraph
type Product @key(fields: "upc") {
  upc: ID!
  name: String!
  price: Int
}
```

```graphql title=Reviews subgraph
type Product @key(fields: "productUpc") {
  productUpc: ID!
  rating: Int!
}
```

For more information on advanced key options, like defining [multiple keys](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys/#multiple-keys) or [compound keys](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys/#compound-keys), see the guide on [Defining keys](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys).

#### Key field limitations

An entity's `@key` cannot include:

* Fields that return a union or interface
* Fields that take arguments

Though not strictly required, it's best to use non-nullable fields for keys. If you use fields that return `null` values, GraphOS may encounter issues resolving the entity.

### 2. Define a reference resolver

The `@key` directive effectively tells the router, "This subgraph can resolve an instance of this entity if you provide its unique key." For this to be true, the subgraph must have a *reference resolver* for the entity.

This section describes how to create reference resolvers in Apollo Server.

* If you're using Apollo Connectors, the [connectors directives](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives) declare which REST endpoints to use to  resolve entity fields, so you don't write any reference resolvers.

* If you're using another [subgraph-compatible library](https://www.apollographql.com/docs/graphos/reference/federation/compatible-subgraphs), see its documentation for creating reference resolvers or the equivalent functionality.

For the `Product` entity defined [above](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro.md#1-define-a-key), the reference resolver might look like this:

```js title=resolvers.js
// Products subgraph
const resolvers = {
  Product: {
    __resolveReference(productRepresentation) {
      return fetchProductByID(productRepresentation.upc);
    }
  },
  // ...other resolvers...
}
```

Let's break this example down:

* You declare an entity's reference resolver in your resolver map, as a member of the entity's corresponding object.
* A reference resolver's name is always `__resolveReference`.
* A reference resolver's first parameter is a representation of the entity being resolved.
  * An entity representation is an object that contains the entity's `@key` fields, plus its `__typename` field. These values are automatically provided to your subgraph by your router.
* A reference resolver is responsible for returning all of the entity fields that this subgraph defines.
  * In this example, the hypothetical `fetchProductByID` function fetches a particular `Product`'s field data based on its `upc`.

A particular reference resolver might be called many times to resolve a single query. It's crucial that reference resolvers account for "N+1" issues (typically via [data loaders](https://github.com/graphql/dataloader)). For details, see [Handling the N+1 problem](https://www.apollographql.com/docs/graphos/schema-design/guides/handling-n-plus-one).

Every subgraph that contributes at least one unique field to an entity must define a reference resolver for that entity.

To learn more about `__resolveReference` in Apollo Server, see the [API docs](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-subgraph/#__resolvereference).

## Next steps

Once you [add your subgraphs](https://www.apollographql.com/docs/graphos/platform/graph-management/add-subgraphs) to your supergraph, GraphOS composes them into a supergraph schema.
Clients querying your supergraph can interact with entity fields without needing to know the details of which subgraphs contribute which fields.

To learn about more advanced ways of using entities, check out these guides:

* [Define Advanced Keys](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys), including compound and nested key fields
* [Contribute and Reference Entity Fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields), including computed fields
