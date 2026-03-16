# Source: https://www.apollographql.com/docs/graphos/connectors/requests/headers.md

# Setting HTTP Request Headers

Apollo Connectors support adding headers to HTTP requests with the `http.headers` argument.
Like [with URLs](https://www.apollographql.com/docs/graphos/connectors/requests/url#dynamic-expressions), you can define header values using a combination of fixed values and dynamic [mapping expressions](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping) in curly braces (`{}`).

## Headers with static and dynamic values

This example uses a static value for the `x-api-version` header and a dynamic value with the [`$config` variable](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#config) for the `Authorization` header:

```graphql title=Example Connector with headers
type Query {
  products: [Product]
    @connect(
      http: {
        GET: "https://myapi.dev/products"
        headers: [
          { name: "x-api-version", value: "2024-01-01" }
          { name: "Authorization", value: "Bearer {$config.token}" }
        ]
      }
      selection: "id"
    )
}
```

## Header propagation

You can propagate headers from an incoming client request using the `from` argument.
This example forwards the `Authorization` header value from a client request to the connected HTTP endpoint.

```graphql title=Example Connector with client header propagation
type Query {
  products: [Product]
    @connect(
      http: { GET: "https://myapi.dev/products",
      headers: [{ name: "Authorization", from: "Authorization" }] }
      selection: "id"
    )
}
```

If [header rules in your router configuration](https://www.apollographql.com/docs/router/configuration/header-propagation) conflict with headers set in `@connect` or `@source`, the router configuration takes precedence.

## Shared headers with `@source`

You can use a source to share a set of headers with multiple Connectors:

```graphql title=Example: Connector with shared headers
extend schema
@source(
  name: "ecomm"
  http: {
    baseURL: "https://myapi.dev"
    headers: [
      { name: "x-api-version", value: "2024-01-01" }
      { name: "Authorization", value: "{$config.token}" }
    ]
  }
)

type Query {
  products: [Product]
    @connect(
      source: "ecomm"
      http: { GET: "/products" }
      selection: "id"
    )
}
```

### Overriding headers

Headers in `@connect` override headers in `@source`; they are not combined.

In this example, because `@connect` includes an `Authorization` header, the `Authorization` header from `@source` is never set on requests to the `/products` endpoint:

```graphql title=Example: Overriding source headers
extend schema
@source(
  name: "ecomm"
  http: {
    baseURL: "https://myapi.dev"
    headers: [
      { name: "x-api-version", value: "2024-01-01" }
      { name: "Authorization", value: "{$config.token}" }
    ]
  }
)

type Query {
  products: [Product]
    @connect(
      source: "ecomm"
      http: {
        GET: "/products"
        headers: [
          { name: "Authorization", from: "Authorization" }
        ]
      }
      selection: "id"
    )
}
```

The `@source` header setting is overridden even if the incoming client request doesn't include an `Authorization` header to propagate.

## Additional resources

To test header configurations, use [Connector mode](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground#connector-mode) in the [Connectors Mapping Playground](https://www.apollographql.com/connectors-mapping-playground?embed=\&theme=light#N4IgbgpgTgzglgewHYgFwEYA0I4BM0gDGySEhALglCNuXOQDYQEDCJZl12DAhgJ4IAruQLEkpClRpF2k6qhAQAHuQhJcAAhiEAFhAC2PADpINGgAIwhUQhAAUJs2Z3lyAB1Qbgjp2YBGPDAQAKoASgAynkYgLu4wqAD0CTxwUAwIhADWALQMcDB0SADmMAB0uAYI2TxucKU1CAzp5RBg0T6+ejwVsJ4A2h1OwBpIPPoQUSBK1bXZkLCISNGYGmA8DIITGtEATAAMOwAs2XvoJ+jRGgC+g2bDo+OTAILCOlRwAF48dMjLq+ubSbAAAkYgAZnAiqVKJk1DcQNdBgBdQY3UwaACUJhM5D4bggGgAipsoHwvD4IRAGLhPABlchQODFQbmMQScgOdGdVweclc3waADiAFEACqTBJgiDfQRQCC4XL5QolAD8EIYqigAF4QTwoCVSurNfDbk4uj14hoBvyBV4HhNoi9yG9GV8fksaP8NltogAhaVyqBeUHICFQmFw6Jo21mFE2xHxoJMCiLSbtECm4Gm9PtflYpBXaSGNy1YoEaRMtzCAjRWkIcYaABStIA8gA5DS4b48DRgqD1jQCWUaJ4ABQAktFpGtGTw-EwYARvOjosC9SVop5vCAjdBN9sQDw1nBePOIFHMD5V+DIfvtxGPZM54QKmCL1eQMCCjKYPv9ntLxXT85QAR02Ao70GaJzWgX80C8aNrkAsxVzlGA3GQIJIP5aDpQtO9ELRQsriAA).
