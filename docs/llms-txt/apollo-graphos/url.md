# Source: https://www.apollographql.com/docs/graphos/connectors/requests/url.md

# Building Request URLs

Apollo Connectors let you dynamically build HTTP request URLs using GraphQL field arguments, sibling fields, and router configuration variables.
In this guide, you'll learn how to:

* Add dynamic path segments to your URLs
* Set query parameters, including repeated and optional parameters
* Share a base URL, path, or query parameters across multiple Connectors
* Implement common URL patterns like pagination and batching

If you haven't already, read the overview of [Making HTTP Requests](https://www.apollographql.com/docs/graphos/connectors/requests) to gain familiarity with basic Connectors first.

## Dynamic expressions

Dynamic expressions let you add parameters to the path or query string of the URL.
You can use dynamic expressions in URL templates with curly braces (`{}`).
For example, you can reference a GraphQL field argument using [`$args`](https://www.apollographql.com/docs/graphos/connectors/reference/mapping/variables#args):

```graphql title=products.graphql
type Query {
  product(id: ID!): Product # Notice "id" argument
    @connect(
      http: {
        GET: "https://ecommerce.demo-api.apollo.dev/products/{$args.id}"
      }
    )
}
```

In this example, when a client queries `product(id: "abc123")`, the Connector makes an HTTP request to `/products/abc123`.

Only certain variables are available for URL templates. Refer to the variable reference's [availability notes](https://www.apollographql.com/docs/graphos/connectors/mapping/variables#available-variables).

### Where to use expressions

Expressions can appear anywhere in the path or query string of the URL:

```graphql title=products.graphql
@connect(
  http: {
    GET: """
      https://ecommerce.demo-api.apollo.dev
      /products?{$args.paramName}={$args.paramValue}
    """
  }
)
```

They can't appear in earlier portions of the URL:

```graphql title=❌ This URL fails to build
@connect(
  http: { GET: "https://{$args.userControlledDomain}" }  
)
```

### Allowed expressions

Any [mapping expression](https://www.apollographql.com/docs/graphos/connectors/reference/mapping) can be used within the curly braces (`{}`) and is evaluated dynamically at runtime:

```graphql title=products.graphql
@connect(
  http: { GET: """
    https://ecommerce.demo-api.apollo.dev/products
    ?ids={$args.ids->joinNotNull(",")}
    """
  }
)
```

The result of every expression is percent-encoded. In the example above, if `$args.ids` is `[1, 2, 3]`, the resulting URL is `https://ecommerce.demo-api.apollo.dev/products?ids=1%2C2%2C3`.

Each expression must evaluate to a simple scalar value (string, number, boolean, etc.)—not an object or array:

```graphql title=❌ This URL fails to build
type Query {
  products(ids: [ID!]): [Product]
    @connect(
      http: { GET: """
        https://ecommerce.demo-api.apollo.dev/products
        ?ids={$args.ids} 
        """
      }
    )
}
```

This example fails to build because `$args.ids` is an array.

#### Null values

Parameter names still appear in the URL even when the parameter value is missing or `null`.

In this example, if `availability` in `{$args.availability}` is not provided or set to `null`, the URL will end with `?availability=`.

```graphql title=products.graphql
type Query {
   productsByAvailability(availability: String): [Product] # availability is nullable
    @connect(
      http: { GET: """
        https://ecommerce.demo-api.apollo.dev/products
        ?availability={$args.availability}
      """ }
    )
}
```

To omit parameter names for `null` values, see [omitting optional parameters](https://www.apollographql.com/docs/graphos/connectors/requests/url.md#omitting-optional-parameters).

## Reusing URL pieces

As described in the [request overview](https://www.apollographql.com/docs/graphos/connectors/requests#sharing-configuration-with-source), you can share some common pieces of a URL across multiple Connectors with a `@source` directive. For example, the two Connectors below build off the `ecomm` source's `baseURL`:

```graphql title=products.graphql
extend schema
@source(
  name: "ecomm"
  http: {baseURL: "https://ecommerce.demo-api.apollo.dev"}
)

type Query {
  allProducts: [Product]
    @connect(
      source: "ecomm"
      http: { GET: "/products"}
    )
  productsByAvailability(availability: String): [Product]
    @connect(
      source: "ecomm"
      http: { GET: "/products?availability={$args.availability}" }
    )
}
```

The `baseURL` can also contain common path segments:

```graphql title=products.graphql
extend schema
@source(
  name: "products"
  http: {baseURL: "https://ecommerce.demo-api.apollo.dev/products"}
)

type Query {
  allProducts: [Product]
    @connect(
      source: "products"
      http: { GET: "/"}
    )
    productsByAvailability(availability: String): [Product]
    @connect(
      source: "products"
      http: { GET: "?availability={$args.availability}" }
    )
}
```

Connectors handle deduplication of `/` and `?` and `&` automatically.

A `baseURL` **cannot** contain dynamic expressions (`{}`).

### Setting `baseURL` dynamically

You'll commonly want the `baseURL` within your schema to be the URL used for local development, and then override this with per-environment router config. You can change the `baseURL` of a source using router configuration, which can in turn load from additional sources like environment variables. See [Overriding Base URLs](https://www.apollographql.com/docs/graphos/connectors/deployment/overriding-base-urls) for an example.

## Advanced query parameters

For more advanced use cases, `http` has a `queryParams` attribute for dynamically setting parameters.
It takes a mapping expression that evaluates to an object.

```graphql title=products.graphql
type Query {
    productsByAvailability(availability: String, limit: Int): [Product]
    @connect(
      source: "ecomm"
      http: {
        GET: "/products"
        queryParams: "$args"
      }
    )
}
```

Because `queryParams` expects an object, you can use any [mapping expression](https://www.apollographql.com/docs/graphos/connectors/reference/mapping) that evaluates to an object, including a
short expression like `$args`. In this case, the query parameters `availability` and `limit` are both added to the URL,
resulting in something like `/products?availability=AVAILABLE&limit=10`.

### Omitting optional parameters

Any value that evaluates to `null` in `queryParams` will be entirely omitted from the URL.
In the above example, if `availability` is `null`, the resulting URL will be `/products?limit=10`.
If both values are `null`, the resulting URL will be `/products`.

### Repeated query parameters

Each value of the `queryParams` object can be a single value or an array of values. In the case of an array, the
parameter name will be repeated for each value.

```graphql title=products.graphql
type Query {
    productsByAvailability(ids: [ID!]): [Product]
    @connect(
      source: "ecomm"
      http: {
        GET: "/products"
        queryParams: "id: $args.ids"
      }
    )
}
```

In this example, if `$args.ids` evaluates to `[1, 2, 3]`, the resulting URL will be `/products?id=1&id=2&id=3`.

It's common to use a *singular* name when repeating query parameters.
The GraphQL parameter is named `ids` (plural), but the example above maps that to `id` (singular) in `id: $args.ids`.

### Query parameters in `@source`

You can add `queryParams` to `http` in both `@connect` and `@source`.
Connectors combine query parameters in the resulting URL in the following order:

1. Query parameters from `@source(http.baseURL:)`
2. Query parameters from `@source(http.queryParams:)`
3. Query parameters from `@connect(http.<METHOD>:)`
4. Query parameters from `@connect(http.queryParams:)`

#### Example query parameters in `@source` and `@connect`

With this schema:

```graphql title=products.graphql
extend schema
@source(
  name: "ecomm"
  http: {
    baseURL: "https://ecommerce.demo-api.apollo.dev/products?availability=AVAILABLE"
    queryParams: "limit: $(10)"
  }
)

type Query {
  allProducts: [Product]
    @connect(
      source: "ecomm"
      http: {
        GET: "/products?availability=UNAVAILABLE"
        queryParams: """availability: $("PREORDER")"""
      }
    )
}
```

The final URL is `https://ecommerce.demo-api.apollo.dev/products?availability=AVAILABLE&limit=10&availability=UNAVAILABLE&availability=PREORDER`.

Parameters are never deduplicated; they are only added in order.

The variables available in `@source` are different from those in `@connect`. Refer to the variable reference's [availability notes](https://www.apollographql.com/docs/graphos/connectors/mapping/variables#available-variables).

## Dynamic path segments

Both `@source` and `@connect` support the `path` field in their `http` configuration.
This field accepts a mapping expression that evaluates to an array of scalars.
Each entry in the array is added to the URL as a path segment.

```graphql title=products.graphql
extend schema
@source(
  name: "example"
  http: {
    baseURL: "https://example.com"
    path: "$config.basePath"
  }
)

type Query {
  dynamicPath(path: [String!]): [Product]
    @connect(
      source: "example"
      http: {
        GET: "/"
        path: "$args.path"
      }
    )
}
```

If `$config.basePath` is `["v1", "products"]` and `$args.path` is `["available", "reviews"]`, the resulting URL will be:

```text
https://example.com/v1/products/available/reviews
```

All path segments are added before all query parameters in this order:

1. Path segments from `@source(http.baseURL:)`
2. Path segments from `@source(http.path:)`
3. Path segments from `@connect(http.<METHOD>:)`
4. Path segments from `@connect(http.path:)`

## Common URL patterns

### Pagination

If your API supports pagination, for example, by supporting `limit` and `offset` query parameters, you can expose that functionality in your schema by defining field arguments and using them in your Connector URLs.

Connectors make it easy to expose these pagination controls in your GraphQL schema while also capturing pagination metadata like total counts.

Common pagination patterns you can implement include:

* **Offset-based pagination** with `limit` and `offset` parameters
* **Page-based pagination** with `page` and `size` parameters
* **Cursor-based pagination** with `after` or `before` tokens

Here's an example of implementing offset-based pagination:

```graphql title=products.graphql
type Query {
  paginatedProducts(limit: Int = 10, offset: Int = 0): ProductsResult!
    @connect(
      source: "ecomm"
      http: { GET: "/products?limit={$args.limit}&offset={$args.offset}" }
      selection: """
      # Map the array of products to a "results" field
      results: $.products {
        id
        name
        description
      }
      # Map the total count from the summary object
      totalCount: summary.total
      """
    )
}

# Define a wrapper type to hold both results and pagination metadata
type ProductsResult {
  results: [Product]
  totalCount: Int
}
```

This Connector enables GraphQL queries like this:

```graphql
query GetSecondPageOfProducts {
  paginatedProducts(limit: 10, offset: 10) {
    results {
      id
      name
    }
    totalCount  # Includes the total count of all products
  }
}
```

This query would retrieve products 11-20 (the second page) along with the total count of all available products, enabling clients to build pagination UI controls.

## Additional resources

To experiment with URLs you are building, use [Connector mode](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground#connector-mode) in the [Connectors Mapping Playground](https://www.apollographql.com/connectors-mapping-playground?embed=\&theme=light#N4IgbgpgTgzglgewHYgFwEYA0I4BM0gDGySEhALglCNuXOQDYQEDCJZl12DAhgJ4IAruQLEkpClRpF2k6qhAQAHuQhJcAAhiEAFhAC2PADpINGgAIwhUQhAAUJs2Z3lyAB1Qbgjp2YBGPDAQAKoASgAynkYgLu4wqAD0CTxwUAwIhADWALQMcDB0SADmMAB0uAYI2TxucKU1CAzp5RBg0T5mAL4+AJQmJuR8bhAaAIqC0HxePgBmcBAMuJ4AyuRQcMUdFmIS5A6mvhqxHtMHhxoA4gCiACpRIAkzEDzkglAQuLn5hSUA-HMMVRQAC8wAAJDwoCVSgCgd0QFszEEmBREEh7u0EWcnGDERpMe1sX0kJ1pIY3LVigRpBs3MICNFlgh9CMAFLLADyADkNLgXjwNDMoMyNAI3hoAIIABQAktFpGBIXAeH4mDACN4DtEIVCYNFPN4QLDoPr8SAeIq4LxVRBop1MD5tWI5kVTYbKJk1KboirCBUZnaHVqQGCCi9BHq0BoAEwABljQbM2veAEcJgU3VtonoeBVYG7ugd7Y6Q+8YG5kEFM9js8885GDYWuiZSZ0gA).
