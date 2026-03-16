# Source: https://www.apollographql.com/docs/graphos/connectors/entities/across-subgraphs.md

# Working with Entities Across Subgraphs

Entities in GraphQL Federation allow you to combine data from across multiple services called *subgraphs*. This guide shows how to use Apollo Connectors with entities in a federated architecture.

## Overview

Connectors work seamlessly to combine data across multiple subgraphs into a unified GraphQL API, or *supergraph*.
You can use Connectors to contribute to and reference entities from other subgraphs, whether those are different REST or GraphQL APIs.

```mermaid
flowchart LR;
  clients(Clients);

  subgraph supergraph["Supergraph"]
    router([Router]);
    router --- |@connect| a[REST API];
    router --- |@connect| b[REST API];
    router --- c[GraphQL API];
    router --- d[GraphQL API];
  end

  clients -.- router;
```

## Working across subgraphs with keys

As your schema grows, it's common to maintain each subgraph schema in its own schema file, for example, `products.graphql`, `reviews.graphql`, etc. Modularizing schemas likes this improves collaboration by allowing independent development and deployment across teams.

To identify an entity across different subgraphs, GraphQL schemas rely on the `@key` directive. The `@key` directive defines which key field(s) to cross-identify a particular entity type.

For example, a `Product` type may be uniquely identifiable by a SKU or ID.

```graphql title=products.graphql
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Int
}
```

## Contributing entity fields across Connectors

Any number of different subgraphs can contribute fields to an entity.
For example, you may have both a products subgraph and a reviews subgraph contributing fields to a Product entity.

The products subgraph may provide product data via a Connector that orchestrates `/products/` and `/products/:id` endpoints.

```graphql title=products.graphql
type Query {
  products: [Product]
    @connect(
      source: "ecomm"
      http: { GET: "/products" }
      selection: """
      $. products {
        id
        name
      }
      """
    )
}

type Product
  @connect(
    source: "ecomm"
    http: { GET: "/products/{$this.id}" }
    selection: """
    id
    description
    """
  )
{
  id: ID!
  title: String
  description: String
}
```

See [Combining endpoints to complete an entity](https://www.apollographql.com/docs/graphos/connectors/entities/patterns#combining-endpoints-to-complete-an-entity) to learn more about how this works.

Product review data may come from a separate review subgraph that connects a `/reviews?product_id=:productId` endpoint to your graph.

```graphql title=reviews.graphql
type Product @key(fields: "id") {
  id: ID!
  reviews: [Review]
    @connect(
      source: "example"
      http: { GET: "/reviews?product_id={$this.id}" }
      selection: """
      $.reviews {
        id
        title
        body
        rating
      }
      """
    )
}

type Review {
  id: ID!
  title: String
  body: String
  rating: Int
}
```

The `@connect` directive defines the `reviews` fields to request from the `/reviews` endpoint.
The `id` used as a parameter in the endpoint URL comes from the product's `id` field, which comes from the products subgraph.

## Using entities across Connectors

Imagine all your reviews include a `productId` field to reference the product they're about. When displaying a review in detail, you might need to fetch some of the related product's fields.

It can be tempting to structure your Connectors like this:

```graphql title=❌ Unnecessary foreign keys
type Query {
  review(id: ID!): Review
    @connect(
      source: "ecomm"
      http: { GET: "/reviews/{$args.id}" }
      selection: """
      id
      rating
      comment
      productId
      """
    )
}

type Product {
  id: ID!
  name: String
  description: String
}

type Review {
  id: ID!
  rating: Float!
  comment: String
  productId: ID!
  product: Product!
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$this.productId}" }
      selection: """
      id
      name
      description
      """
    )
}
```

Instead of carrying the `productId` field around ourselves, you can model the `Review.product` relationship using entity types directly. Then you can use a Connector on `Product` to fetch the product details.

```graphql title=✅ Efficient entity usage
type Query {
  review(id: ID!): Review
    @connect(
    source: "ecomm"
    http: { GET: "/reviews/{$args.id}" }
    selection: """
    id
    name
    comment
    product: { id: productId }
    """
  )
}

type Product
  @connect(
    source: "ecomm"
    http: { GET: "/products/{this.id}" }
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

type Review {
  id: ID!
  rating: Float!
  comment: String
  product: Product!
}
```

In this context, `product: { id: productId }` tells Connectors: *"This review references a product that you can fetch with this ID."*
Because `Product` is an entity, Connectors automatically use the existing `Product` Connector to fetch the full product object.

**Key takeaway**:
When working with entities across your schema, you'll often encounter fields like `entityId` or `entity_id` in API responses. These are opportunities to use entity references instead of duplicating Connector mapping selections. Rather than exposing the raw ID directly, you can structure it as a nested object:

```graphql
product: {
  id: productId
}
```

This tells the router to resolve product as an entity, using the existing connector logic defined elsewhere in your schema. It makes your schema cleaner, avoids duplication, and lets you reuse the entity's fields wherever they're needed.

## Referencing entities across Connectors

If your REST API provides foreign key references, you can use them to reference entities and fetch corresponding fields from a different subgraph.

For example, if your REST API lets you fetch a user's favorite products and provides those products' IDs, you can use the `@connect` directive to reference the `Product` entity:

```graphql title=users.graphql
type User @key(fields: "id") {
  id: ID!
  favoriteProducts: [Product]
    @connect(
      source: "example"
      http: { GET: "/users/{$this.id}/favorites" }
      selection: """
      $.products {
        id: productId
      }
      """
    )
}

type Product @key(fields: "id", resolvable: false) {
  id: ID!
}
```

The mapping language maps the `productId` to the `Product` entity's `id` field.
The `resolvable: false` argument denotes that while this subgraph includes a definition for the `Product` entity, it doesn't provide a way to fetch or *resolve* all of it's fields. [Learn more.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#referencing-an-entity-without-contributing-fields)

## Adding a computed field using `@requires`

You might need to compute a field's value based on data from other subgraphs that contribute to an entity type.
The` @requires` directive allows a subgraph to declare that it depends on specific fields from the same entity before resolving a field. The `@external` directive declares that a field is resolved from a different subgraph.

```graphql
type Product @key(fields: "id") {
  id: ID!
  weight: Int @external
  shippingCost(zipCode: String): Int
    @requires(fields: "weight")
    @connect(
      source: "example"
      http: {
        GET: "/shipping?zip={$args.zipCode}&weight={$this.weight}"
      }
      selection: "$.result"
    )
}
```

In this example, `shippingCost` depends on the `weight` field.
Because `weight` is marked as `@external` (coming from another subgraph), the `@requires` directive ensures its inclusion in the query plan before resolving `shippingCost`.

## Compatibility with other federation features

Connectors work seamlessly with many other federation features. You can use directives like `@tag`, `@inaccessible`, `@provides`, and [more](https://www.apollographql.com/docs/graphos/reference/federation/directives) alongside `@connect`.

See the [limitations reference](https://www.apollographql.com/docs/graphos/schema-design/connectors/limitations#unsupported-federation-directives) for a list of unsupported federation directives.

## Additional resources

* See the [entity documentation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro) for more information on using entities in GraphQL Federation.

* Check out the [Thinking in Entities](https://www.apollographql.com/blog/api-orchestration-with-connectors-thinking-in-entities) blog post for best practices for using entities with Connectors.
