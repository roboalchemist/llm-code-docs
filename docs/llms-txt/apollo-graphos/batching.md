# Source: https://www.apollographql.com/docs/graphos/connectors/requests/batching.md

# Batch Requests

The "N+1 problem" is a common challenge in GraphQL APIs that can lead to performance issues. You start with an initial request (1), that returns a list of objects. The size of the list determines how many follow-up requests (N) are necessary. The exact number of follow-up requests is not known until the first request is executed.

Consider a simple e-commerce API that provides a list of reviews, each with a rating and a reference to a product. The product is an entity that can be fetched separately.

```graphql
type Query {
  reviews: [Review] # A list!
    @connect(
      source: "ecom"
      http: { GET: "/reviews" }
      selection: "id rating product: { id: productId }"
    )
}

type Review {
  id: ID!
  rating: Int!
  product: Product
}

type Product
  @connect(
    source: "ecom"
    http: { GET: "/product/{$this.id}" }
    selection: "id name"
  ) @key(fields: "id") {
  id: ID!
  name: String
}
```

In the [Connectors Debugger](https://www.apollographql.com/docs/graphos/connectors/troubleshooting#return-debug-information-in-graphql-responses), you can see that fetching the list of reviews results in a separate request for each product associated with the review.

To solve the N+1 problem, you can use Connectors batching. With batching, a single request is made for all N items in the list.

```graphql
type Product
  @connect(
    source: "ecom"
    # Use the $batch variable to make a batch request for products
    http: { GET: "/product", queryParams: "id: $batch.id" }
    selection: "id name"
  ) {
  id: ID!
  name: String
}
```

This reduces the total number of requests to two: one for the list of reviews and one for the list of products.

Learn more about the similarities between Connectors batching and DataLoaders in the [N+1 handling guide](https://www.apollographql.com/docs/graphos/schema-design/guides/handling-n-plus-one#comparing-connectors-batching-with-dataloaders).

## Fetching entities in batches

Using Connectors batching requires an HTTP endpoint that accepts a list of keys and returns a list of items. This is often referred to as a *batch endpoint*.
There are a few common patterns for batch endpoints and how to use the Connectors `$batch` variable to make batch requests:

### Repeated query parameters

Using repeated query parameters, each ID is sent as a separate query parameter in the HTTP request, for example, `?id=1&id=2`.

Use the `http.queryParams` mapping to specify the query parameter name and the value from `$batch.id`. The `$batch.id` variable is a list of IDs that will be sent in the request.

```graphql
http: { GET: "/" queryParams: "id: $batch.id" }
```

### Comma-separated list

Using a comma-separated list, all IDs are passed in a single query parameter, for example, `?ids=1,2`. Commas will be percent-encoded: `?ids=1%2C2`.

Use the `joinNotNull` mapping method to join the IDs into a single string, ignoring any `null` values. Interpolate the `$batch.id` variable in the `http.GET` mapping to create the query parameter.

```graphql
http: { GET: "?ids={$batch.id->joinNotNull(',')}" }
```

The [`->joinNotNull` mapping method](https://www.apollographql.com/docs/graphos/connectors/mapping/methods#array-methods) creates a string from a list of scalar values by joining them with a separator. It ignores null values, which is important when dealing with entity references from the query planner. Read more about the [implications of null entity references](https://www.apollographql.com/docs/graphos/schema-design/guides/nullability#weigh-the-implications-of-non-null-entity-references).

### JSON request body

Using a JSON request body, all IDs are passed in as a filter criteria in the JSON payload, for example, `{ "ids": [1, 2] }`.

Use the `http.body` mapping to specify the request body. The `$batch.id` variable is used to access the list of IDs.

```graphql
http: { POST: "/products" body: "ids: $batch.id" }
```

### Composite keys

In this example, the `Product` type has a composite key that includes the `id` and the `store.id`. The request body needs to include both fields to uniquely identify each product.

```json title=Example request body
{
  "items": [
    { "id": 1, "store_id": 10 },
    { "id": 2, "store_id": 20 },
    { "id": 3, "store_id": 10 }
  ]
}
```

```graphql
type Product
  @connect(
    source: "ecom"
    http: {
      POST: "/products"
      body: """
      items: $batch { 
        id 
        store_id: store.id 
      }
      """
    }
    selection: """
    id
    name
    store { id name }
    """
  ) {
  id: ID!
  name: String
  store: Store
}

type Store {
  id: ID!
  name: String
}
```

## Rules for batch Connectors

* The mappings from the `$batch` variable must be scalar fields of the entity type.

  ```graphql
  type Product
    @connect(
      source: "ecom"
      http: {
        GET: "/products"
        queryParams: "id: $batch.id"
      }
      selection: """
      id
      name
      """
    ) {
    id: ID! # scalar field
    name: String
  }
  ```

  ```graphql
  type Product
    @connect(
      source: "ecom"
      http: {
        GET: "/products"
        body: "id: $batch.variation"
      }
      selection: """
      id
      name
      """
    ) {
    id: ID!
    name: String
    variation: Variation
  }

  type Variation {
    id: ID!
    color: String
  }
  ```

* The selection mapping for a batch request must evaluate to a list of objects.

  ```graphql
  type Product
    @connect(
      source: "ecom"
      http: {
        GET: "/products"
        queryParams: "id: $batch.id"
      }
      selection: """
      # unwrap the { "results": [...] } wrapper
      $.results {
        id
        name
      }
      """
    ) {
    id: ID!
    name: String
  }
  ```

  ```graphql
  type Product
    @connect(
      source: "ecom"
      http: {
        GET: "/products"
        queryParams: "id: $batch.id"
      }
      selection: """
      # evaluates to { "results": [{ "id": 1, "name": "Hat" }] }
      results {
        id
        name
      }
      """
    ) {
    id: ID!
    name: String
  }
  ```

* The selection mapping for a batch request must contain the same fields as the `$batch` variable.

  ```graphql
  type Product
    @connect(
      source: "ecom"
      http: {
        GET: "/products"
        queryParams: "id: $batch.id"
      }
      selection: """
      $.results {
        # maps the product_id field to the id field referenced from $batch
        id: product_id
        name
      }
      """
    ) {
    id: ID!
    name: String
  }
  ```

  Not selecting the id field means we can't associate the response items to the keys in the batch.

  ```graphql
  type Product
    @connect(
      source: "ecom"
      http: {
        GET: "/products"
        queryParams: "id: $batch.id"
      }
      selection: """
      $.results {
        name
      }
      """
    )
  {
    id: ID!
    name: String
  }
  ```

## Batch options

### `maxSize`

You may want to limit the number of items included in each batch request. This is useful when the API has a limit on the number of items that can be fetched in a single request.

Use the `batch.maxSize` option to specify the maximum number of items included in each batch request. This results in `(N / maxSize) + 1` requests to your API.

```graphql
type Product
  @connect(
    source: "ecom"
    http: { GET: "/products", queryParams: "id: $batch.id" }
    selection: "id name"
    batch: { maxSize: 10 }
  ) {
  id: ID!
  name: String
}
```

## A complex batching example

The [Fast Healthcare Interoperability Resources (FHIR)](https://www.hl7.org/fhir/) standard defines a RESTful API for exchanging healthcare data. It has an unusual pattern for batch requests that takes a little more effort to implement with Connectors.

Batch requests in FHIR are made by sending a JSON payload with a list of requests. Each request has a method, URL, and optional resource.

```json
{
  "resourceType": "Bundle",
  "type": "batch",
  "entry": [
    {
      "request": {
        "method": "GET",
        "url": "Patient/123"
      }
    },
    {
      "request": {
        "method": "GET",
        "url": "Patient/456"
      }
    },
    {
      "request": {
        "method": "GET",
        "url": "Patient/789"
      }
    }
  ]
}
```

You can accomplish this with Connectors by using the `http.body` mapping to create the JSON payload. The `$batch` variable is used to access the list of IDs and construct the requests.

```graphql
@connect(
  http: {
    POST: "https://fhir.example.com/"
    body: """
    resourceType: $("Bundle")
    type: $("batch")
    entry: $batch.id { # Iterate over the batch ids
      request: {
        method: $("GET")
        url: $(["Patient", $])->joinNotNull("/")
      }
    }
    """
  }
)
```

Lastly, you can map over resources in the response to return a list that the query planner can use to resolve the entities in the batch.

```graphql
@connect(
  selection: """
  $.entry.resource {
    id
    name {
      family
      given
    }
  }
  """
)
```

## Limitations of "has-many" relationships

With a relationship like `Product.reviews`, it's usually not possible to batch requests. These relationships often involve pagination and providing the parameters in a batch request isn't possible.

In this example, fetching the reviews for a list of products will always result in a separate request for each product.

```graphql
type Product {
  id: ID!
  name: String
  reviews(first: Int, after: String): [Review]
    @connect(
      source: "ecom"
      http: {
        GET: """
        /products/{$this.id}/reviews
        ?first={$args.first}
        &after={$args.after}
        """
      }
      selection: "id rating"
    )
}
```
