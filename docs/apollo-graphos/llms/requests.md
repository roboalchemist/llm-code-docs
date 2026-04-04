# Source: https://www.apollographql.com/docs/apollo-server/workflow/requests.md

# Source: https://www.apollographql.com/docs/graphos/connectors/requests.md

# Making HTTP Requests

Apollo Connectors provide a declarative way to integrate REST API calls into your graph using the `@connect` and `@source` directives in your schemas.
In this guide, you'll learn the basics of making HTTP requests with Apollo Connectors.

## Overview

Every Connector needs three things to make an HTTP request:

1. The HTTP method (`GET`, `POST`, etc.)
2. The URL to send the request to
3. A selection mapping that describes how to handle the response

You define 1 and 2 with the `http` argument of the `@connect` directive and 3 with the `selection` argument.

The most basic Connector looks something like this:

```graphql title=Basic Connector
type Query {
  products: [Product]
    @connect(
      http: { GET: "https://ecommerce.demo-api.apollo.dev/products" }
      selection: "id"
    )
}
```

This Connector makes a `GET` request to `https://ecommerce.demo-api.apollo.dev/products` and makes the `id` field available in GraphQL queries.

### Basic example Connectors

#### Example GET request

```graphql title=Example Connector for GET HTTP method
type Query {
  products: [Product]
    @connect(
      http: { GET: "https://myapi.dev/products" }
      selection: "id"
    )
}
```

#### Example POST request with body

Requests can also include bodies when using a `POST`, `PUT`, or `PATCH` method.

```graphql title=Example Connector for POST HTTP method
type Mutation {
  createProduct(name: String!): Product
    @connect(
      http: {
        POST: "https://myapi.dev/products"
        body: "name: $args.name"
      }
      selection: "id"
    )
}
```

Learn more about [creating request bodies with Connectors](https://www.apollographql.com/docs/graphos/connectors/requests/body).

#### Example PUT request with path parameter

URLs can contain dynamic expressions for setting path or query parameters.

```graphql title=Example Connector for PUT HTTP method
type Mutation {
  setProduct(id: ID!, name: String!): Product
    @connect(
      http: {
        PUT: "https://myapi.dev/products/{$args.id}"
        body: """
        {
          name: $args.name,
          description: $args.description,
          price: $args.price,
          inventory: $args.inventory
        }
        """
      }
      selection: "id"
    )
}
```

Learn more about [using dynamic expressions with Connectors](https://www.apollographql.com/docs/graphos/connectors/requests/url#dynamic-expressions).

#### Example PATCH request with query parameter

```graphql title=Example Connector for PATCH HTTP method
type Mutation {
  updateProduct(id: ID!, name: String!): Product
    @connect(
      http: {
        PATCH: "https://myapi.dev/products/{$args.id}?name={$args.name}"
      }
      selection: "id"
    )
}
```

Learn more about [setting query parameters with Connectors](https://www.apollographql.com/docs/docs/graphos/connectors/requests/url).

#### Example DELETE request

```graphql title=Example Connector for DELETE HTTP method
type Mutation {
  deleteProduct(id: ID!): Product
    @connect(
      http: {
        DELETE: "https://myapi.dev/products/{$args.id}"
      }
      selection: "id"
    )
}
```

## Sharing configuration with `@source`

You can use the `@source` directive to share a partial URL and headers with multiple Connectors.

### Source definition

To define a `@source`:

```graphql title=Example @source creation
extend schema
  @link(
    url: "https://specs.apollo.dev/connect/v0.1",
    import: ["@connect", "@source"]
  )
  @source(
    name: "myapi"
    http: {
      baseURL: "https://myapi.example.com/v1?client=router"
      headers: [{ name: "X-API-Key", value: "{$config.api_key}" }]
    }
  )
```

1. Import the `@source` directive from the Connectors `@link`. (line 4 above)
2. Apply the `@source` directive to the `schema`. (lines 6-12 above)
   * Define a `baseURL`.
   * Optionally define `headers`, which can't contain `$this` or `$args`.

### Source usage

To use a `@source`:

```graphql title=Example Connector with a related @source

type Query {
  products(first: Int = 10): [Product]
    @connect(
      source: "myapi"
      http: {
        GET: "/products?first={$args.first}",
        headers: [{ name: "X-Product-Type", from: "Product-Type" }]
      }
      selection: "id"
    )
}
```

1. Set the `source` field in each `@connect` directive that should use the shared configuration. Use the `name` defined in source definition.
2. Use a partial URL in the `@connect` directive containing *only* the path and query parameters (no scheme, host, etc.).
3. Define headers in `@connect` to override headers from the `@source` with the same `name`.

The Connector request above resolves to `https://myapi.example.com/v1/products?client=router&first=10`.
It includes the `X-API-Key` header from the `@source` configuration and the `X-Product-Type` header from the `@connect` configuration.

## Additional resources

For crafting more complex requests, refer to in-depth pages on each part of the HTTP request:

* [URL](https://www.apollographql.com/docs/graphos/connectors/requests/url), including query parameters and path segments
* [Headers](https://www.apollographql.com/docs/graphos/connectors/requests/headers)
* [Body](https://www.apollographql.com/docs/graphos/connectors/requests/body)
