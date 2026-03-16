# Source: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys.md

# Define Advanced Keys

Depending on your entities' fields and usage, you may need to use more advanced `@key`s.
For example, you may need to define a [compound `@key`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys.md#compound-keys) if multiple fields are required to uniquely identify an entity.
If different subgraphs interact with different fields of an entity, you may need to define [multiple](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys.md#multiple-keys)—and sometimes [differing](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys.md#differing-keys-across-subgraphs)—`@key`s for the entity.

## Compound `@key`s

A single `@key` can consist of multiple fields, the combination of which uniquely identifies an entity. This is called a *compound* or *composite key*. In the following example, the combination of both `username` and `domain` fields is required to uniquely identify the `User` entity:

```graphql title=Users subgraph
type User @key(fields: "username domain") {
  username: String!
  domain: String!
}
```

### Nested fields in compound `@key`s

Nested fields are often used in compound keys.
In the following example, the `User` entity's `@key` consists of both a user's `id` and the `id` of that user's associated `Organization`:

```graphql title=Users subgraph
type User @key(fields: "id organization { id }") {
  id: ID!
  organization: Organization!
}

type Organization {
  id: ID!
}
```

Though nested fields are most commonly used in compound keys, you can also use a nested field as a single `@key` field.

## Multiple `@key`s

When different subgraphs interact with different fields of an entity, you may need to define multiple `@key`s for the entity. For example, a Reviews subgraph might refer to products by their ID, whereas an Inventory subgraph might use SKUs.

In the following example, the `Product` entity can be uniquely identified by either its `id` or its `sku`:

```graphql title=Products subgraph
type Product @key(fields: "id") @key(fields: "sku") {
  id: ID!
  sku: String!
  name: String!
  price: Int
}
```

If you include multiple sets of `@key` fields, the query planner uses the most efficient set for entity resolution. For example, suppose you allow a type to be identified by `@key(fields: "id")` or `@key(fields: "id sku")`:

```graphql
type Product @key(fields: "id") @key(fields: "id sku") {
  # ...
}
```

That means either `id` or (`id` and `sku`) is enough to uniquely identify the entity. Since `id` alone is enough, the query planner will use only that field to resolve the entity, and `@key(fields: "id sku")` is effectively ignored.

### Referencing entities with multiple keys

A subgraph that [references an entity without contributing any fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#referencing-an-entity-without-contributing-fields) can use any `@key` fields in its stub definition. For example, if the Products subgraph defines the `Product` entity like this:

```graphql title=Products subgraph
type Product @key(fields: "id") @key(fields: "sku") {
  id: ID!
  sku: String!
  name: String!
  price: Int
}
```

Then, a Reviews subgraph can use either `id` or `sku` in the stub definition:

```graphql title=Reviews subgraph
# Either:
type Product @key(fields: "id", resolvable: false) {
  id: ID!
}

# Or:
type Product @key(fields: "sku", resolvable: false) {
  sku: String!
}
```

When resolving a reference for an entity with multiple keys, you can determine how to resolve it based on which key is present. For example, if you're using [`@apollo/subgraph`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-subgraph/), it could look like this:

```js title=resolvers.js
// Products subgraph
const resolvers = {
  Product: {
    __resolveReference(productRepresentation) {
      if(productRepresentation.sku){
        return fetchProductBySku(productRepresentation.sku);
      } else {
        return fetchProductByID(productRepresentation.id);
      }
    }
  },
  // ...other resolvers...
}
```

## Differing `@key`s across subgraphs

Although an entity commonly uses the exact same `@key` field(s) across subgraphs, you can alternatively use different `@key`s with different fields. For example, you can define a `Product` entity shared between subgraphs, one with `sku` and `upc` as its `@key`s, and the other with only `upc` as the `@key` field:

```graphql title=Products subgraph
type Product @key(fields: "sku") @key(fields: "upc") {
  sku: ID!
  upc: String!
  name: String!
  price: Int
}
```

```graphql title=Inventory subgraph
type Product @key(fields: "upc") {
  upc: String!
  inStock: Boolean!
}
```

To merge entities between subgraphs, the entity must have at least one shared field between subgraphs. For example, operations can't merge the `Product` entity defined in the following subgraphs because they don't share any fields specified in the `@key` selection set:

❌

```graphql title=Products subgraph
type Product @key(fields: "sku") {
  sku: ID!
  name: String!
  price: Int
}
```

```graphql title=Inventory subgraph
type Product @key(fields: "upc") {
  upc: String!
  inStock: Boolean!
}
```

### Operations with differing `@key`s

Differing keys across subgraphs affect which of the entity's fields can be resolved from each subgraph. Requests can resolve fields if there is a traversable path from the root query to the fields.

Take these subgraph schemas as an example:

```graphql title=Products subgraph
type Product @key(fields: "sku") {
  sku: ID!
  upc: String!
  name: String!
  price: Int
}

type Query {
  product(sku: ID!): Product
  products: [Product!]!
}

```

```graphql title=Inventory subgraph
type Product @key(fields: "upc") {
  upc: String!
  inStock: Boolean!
}
```

The queries defined in the Products subgraph can always resolve all product fields because the product entity can be joined via the `upc` field present in both schemas.

On the other hand, queries added to the Inventory subgraph can't resolve fields from the Products subgraph:

```graphql title=Products subgraph
type Product @key(fields: "sku") {
  sku: ID!
  upc: String!
  name: String!
  price: Int
}
```

```graphql title=Inventory subgraph
type Product @key(fields: "upc") {
  upc: String!
  inStock: Boolean!
}

type Query {
  productsInStock: [Product!]!
}
```

The `productsInStock` query can't resolve fields from the Products subgraph since the Products subgraph's `Product` type definition doesn't include `upc` as a key field, and `sku` isn't present in the Inventory subgraph.

If the Products subgraph includes `@key(fields: "upc")`, all queries from the Inventory subgraph can resolve all product fields:

```graphql title=Products subgraph
type Product @key(fields: "sku") @key(fields: "upc") {
  sku: ID!
  upc: String!
  name: String!
  price: Int
}
```

```graphql title=Inventory subgraph
type Product @key(fields: "upc") {
  upc: String!
  inStock: Boolean!
}

type Query {
  productsInStock: [Product!]!
}
```

## Next steps

If you haven't already, learn how to [contribute entity fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields) to the supergraph and [reference them](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#referencing-an-entity-without-contributing-fields) from subgraphs that don't contribute any fields.
