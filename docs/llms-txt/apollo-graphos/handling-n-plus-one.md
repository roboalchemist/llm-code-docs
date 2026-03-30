# Source: https://www.apollographql.com/docs/graphos/schema-design/guides/handling-n-plus-one.md

# Handling the N+1 Problem

Want to learn how to handle the N+1 problem with Apollo Connectors? See our [Batch Requests](https://www.apollographql.com/docs/graphos/connectors/requests/batching/) guide.

GraphQL developers often encounter the "N+1 query problem" with operations that return a list.
Consider this `TopReviews` query:

```graphql
query TopReviews {
  topReviews(first: 10) {
    id
    rating
    product {
      name
      imageUrl
    }
  }
}
```

In a monolithic GraphQL server, the execution engine takes these steps:

1. Resolve the `Query.topReviews` field, which returns a list of `Review`s.
2. For each `Review`, resolve the `Review.product` field.

If `Query.topReviews` returns ten reviews, then the executor resolves `Review.product` field ten times.
If the `Reviews.product` field makes a database or REST query for a single `Product`, then there are ten unique calls to the data source.
This is suboptimal for the following reasons:

* Fetching all products in a single query is more efficient—for example, `SELECT * FROM products WHERE id IN (<product ids>)`.
* If any reviews refer to the same product, then resources are wasted fetching data that was already retrieved.

## The N+1 problem in a federated graph

Understand the basics of [Apollo Federation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/federation) and federated graphs.

Consider the same `TopReviews` operation with the `Product` type as an entity defined in Reviews and Products subgraphs.

```graphql title=Reviews subgraph
type Query {
  topReviews(first: Int): [Review]
}

type Review {
  id: ID
  rating: Int
  product: Product
}

type Product @key(fields: "id") {
  id: ID
}
```

```graphql title=Products subgraph
type Product @key(fields: "id") {
  id: ID!
  name: String
  imageUrl: String
}
```

Most subgraph implementations use *reference resolvers* to return the entity object corresponding to a key.
Although this pattern is straightforward, it can diminish performance when a client operation requests fields from many entities.
Recall the `topReviews` query, now in the context of a federated graph:

```graphql
query TopReviews {
  topReviews(first: 10) { # Defined in Reviews subgraph
    id
    rating
    product { # ⚠️ NOT defined in Reviews subgraph
      name
      imageUrl
    }
  }
}
```

The router executes two queries:

1. Fetch all fields except `Product.name` and `Product.imageURL` from the Reviews subgraph.
2. Fetch each product's `name` and `imageURL` from the Products subgraph.

In the Products subgraph, the reference resolver for `Product` doesn't take a list of keys but rather a single key.
Therefore, the subgraph library calls the reference resolver once for each key:

```js title=resolvers.js
// Products subgraph
const resolvers = {
  Product: {
    __resolveReference(productRepresentation) {
      return fetchProductByID(productRepresentation.id);
    }
  },
  // ...other resolvers...
}
```

A basic `fetchProductByID` function might make a database call each time it's called.
If you need to resolve `Product.name` for `N` different products, this results in `N` database calls.
These calls are made in addition to the call made by the Reviews subgraph to fetch the initial list of reviews and the `id` of each product.
This problem can cause performance problems or even enable denial-of-service attacks.

### Query planning to handle N+1 queries

By default, the router's query planner handles N+1 queries for entities like the `Product` type.
The query plan for the `TopReviews` operation works like this:

1. First, the router fetches the list of `Review`s from the Reviews subgraph using the root field `Query.topReviews`. The router also asks for the `id` of each associated product.
2. Next, the router extracts the `Product` entity references and fetches them in a batch to the Products subgraph's `Query._entities` root field.
3. After the router gets back the `Product` entities, it merges them into the list of `Review`s, indicated by the `Flatten` step.

```mermaid
graph TB
    A("Fetch (reviews)") --> B("Fetch (products)")
    B --> C("Flatten (topReviews,[],products)")
```

```text
QueryPlan {
  Sequence {
    Fetch(service: "reviews") {
      {
        topReviews(first: 10) {
          id
          rating
          product {
            __typename
            id
          }
        }
      }
    },
    Flatten(path: "reviews.@") {
      Fetch(service: "products") {
        {
          ... on Product {
            __typename
            id
          }
        } =>
        {
          ... on Product {
            name
            imageUrl
          }
        }
      },
    },
  },
}
```

Most subgraph implementations (including [`@apollo/subgraph`](https://www.apollographql.com/docs/apollo-server/using-federation/api/apollo-subgraph/)) don't write the [`Query._entities` resolver](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/subgraph-specific-fields/#query_entities) directly.
Instead, they use the [reference resolver API](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro/#2-define-a-reference-resolver) for resolving an individual entity reference:

```js
const resolvers = {
  Product: {
    __resolveReference(productRepresentation) {
      return fetchProductByID(productRepresentation.id);
    },
  },
};
```

The motivation for this API relates to a subtle, critical aspect of the [subgraph specification](https://www.apollographql.com/docs/federation/subgraph-spec):
the order of resolved entities must match the order of the given entity references.
If the entities are returned in the wrong order, those fields are merged with the wrong entities, leading to incorrect results.
To avoid this issue, most subgraph libraries handle entity order for you.

Because order matters, it reintroduces the N+1 query problem: in the example above, `fetchProductByID` gets called once for each entity reference.

## The DataLoader pattern solution

The solution for the N+1 problem—whether for federated or monolithic graphs—is the [DataLoader](https://github.com/graphql/dataloader) pattern.
For example, in an Apollo Server implementation, using DataLoaders could look like this:

```js
const resolvers = {
  Product: {
    __resolveReference(product, context) {
      return context.dataloaders.products(product.id);
    },
  },
};
```

With DataLoaders, when the query planner calls the Products subgraph with a batch of `Product` entities, the router makes a single batched request to the Products data source.

Nearly every GraphQL server library provides a DataLoader implementation, and Apollo recommends using it in every resolver, even those that aren't for entities or don't return a list.

## Comparing Connectors batching with DataLoaders

Connectors batching with `$batch` provides functionality similar to DataLoaders in a declarative API. Both approaches have three responsibilities:

1. **Deduplication**: Connectors and DataLoaders ensure that the same request is not sent multiple times. For example, if all the reviews are for the same product, we only want to make a single `/products/42` request. This is actually the default behavior of the query planner and works for non-batching Connectors that use `$this`.

2. **Creating the request**: Both approaches create a single request for all the items in the batch. In a DataLoader, you provide a callback function that takes the accumulated keys and executes a request. With Connectors, you define your request in terms of the values in the `$batch` variable.

3. **Associating response items with keys**: This is the most critical and overlooked aspect of batching solutions. Batch endpoints often return the list of items in an arbitrary order, irrespective of the order of keys in the request. If we incorrectly match items in the list with the keys in the batch, we end up serious data inconsistencies.

   Both Connectors and DataLoaders use a map internally to ensure items are correctly associated with their keys. The reason [you must select the key fields in the `selection:` mapping](https://www.apollographql.com/docs/graphos/connectors/requests/batching#rules-for-batch-connectors) is to give Connectors the information it needs to build the map.
