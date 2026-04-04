# Source: https://www.apollographql.com/docs/graphos/connectors/entities.md

# Working with Entities

Apollo Connectors are designed to simplify working with entities in federated graphs.
An entity is any object that can identified with one or more unique key fields, much like rows in a database table.
The different data fields are like columns in the table.
GraphQL federation uses entity types to represent object types that combine information from multiple data sources.

## Identifying entities

Most APIs associate entities with particular business domains.
When working with REST APIs, if there's a `GET` endpoint with a unique identifier (for example, `/products/:id`) it's likely you're dealing with an entity.

## Retrieve entity fields with Connectors

When retrieving an entity with a Connector, you use the `@connect` directive on the type instead of a field on `Query`.

```graphql
type Product
  @connect(
    source: "ecomm"
    http: { GET: "/products/{$this.id}" }
    selection: """
    id
    name
    description
    """
  )
{
  id: ID!
  name: String
  description: String
}
```

In this example, the query planner can fetch Product fields using this Connector as long as it has a value for the Product's `id` field, as indicated by `$this.id`.

Connectors that retrieve entity fields can also use batch endpoints to resolve the `N+1 problem.` Learn more about [batching requests](https://www.apollographql.com/docs/graphos/connectors/requests/batching).

## Where to use `@connect`

You can apply the `@connect` directive in two ways when working with entities:

* **On entity types** - Use this when you want to fetch entity fields without exposing a dedicated query to fetch entities directly
* **On `Query` fields** - Use this when you need both a way to fetch entities via a root field *and* to fetch entity fields from a query for another type

Connectors on `Query` fields are just as common as Connectors on types or fields of types. Choose the approach that best fits your specific use case and keeps your schema clean.

### `@connect` on entity types

When you only need to enhance an entity with additional fields without creating a root field to access it, apply `@connect` directly on the type. For example, if you only need to fetch products' prices in the context of fetching product information, but never fetch prices in isolation:

```graphql
type Product {
  id: ID!
  name: String
  price: Price
}

type Price @key(fields: "id")
  @connect(
    source: "ecomm"
    http: { GET: "/products/{$this.id}/price" }
    selection: """
      id
      active
      currency
      unitAmount
    }
    """
  ){
  id: ID!
  active: Boolean
  currency: String
  unitAmount: Float
}

type Query {
  products: [Product] 
    @connect(
      source: "ecomm"
      http: { GET: "/products"}
      selection: """
        $.products {
          id
          name
          price {
            id: default_price
          }
        }
      """
    )
}
```

This pattern is cleaner than the legacy approach of creating an `@inaccessible` field with `entity: true`.

Prior to v0.2 of the Connectors specification , you could only add `@connect` to fields and use `entity: true` to resolve entities:

```graphql
type Price @key(fields: "id") {
  id: ID!
  active: Boolean
  currency: String
  unitAmount: Float
}

type Query {
  price(id: ID!): Price 
    @connect(
      source: "ecomm"
      http: { GET: "/prices/{$args.id}"}
      selection: """
        id
        active
        currency
        unitAmount: unit_amount
      """
      entity: true #highlight-line
    )
    @inaccessible #highlight-line
}
```

In this example:

* `entity: true` indicates that this Connector should also be used to resolve `Price` references
* `@inaccessible` is used to hide this query field from clients while still allowing it to resolve entity references

This pattern has some limitations as described in [Rules for `entity: true`](https://www.apollographql.com/docs/graphos/connectors/reference/directives#rules-for-entity-true).

### `@connect` on Query

When you need both a way for clients to directly query for entities and to resolve entity references, place the `@connect` directive on a `Query` field with `entity: true`.

```graphql
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: """
      id
      name
      description
      """
      entity: true
    )
}

type Product {
  id: ID!
  name: String
  description: String
}
```

This approach avoids duplicating a Connector when you need both capabilities. This pattern has some limitations as described in [Rules for `entity: true`](https://www.apollographql.com/docs/graphos/connectors/reference/directives#rules-for-entity-true).

## Additional resources

For more foundational information about entities:

* See the [entity documentation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro) for additional information on using entities in GraphQL Federation.
* Check out the [Thinking in Entities](https://www.apollographql.com/blog/api-orchestration-with-connectors-thinking-in-entities) blog post for best practices for using entities with Connectors.

To learn more advanced entity resolution patterns:

* See [Entity Resolution Patterns](https://www.apollographql.com/docs/graphos/connectors/entities/patterns) to learn how to combine multiple endpoints and optimize data fetching
* See [Working with Entities Across Subgraphs](https://www.apollographql.com/docs/graphos/connectors/entities/cross-subgraph-entities) to learn how to work with entities in a federated architecture
* Learn about [batching requests](https://www.apollographql.com/docs/graphos/connectors/requests/batching) to optimize entity resolution and avoid the N+1 problem
