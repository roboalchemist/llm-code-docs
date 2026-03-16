# Source: https://www.apollographql.com/docs/ios/fetching/error-handling.md

# Source: https://www.apollographql.com/docs/react/data/error-handling.md

# Source: https://www.apollographql.com/docs/graphos/connectors/responses/error-handling.md

# Error Handling with Connectors

Learn how Connectors handle errors by default and how you can customize error handling.

## Default behavior

When an HTTP endpoint returns a non-200 status, GraphOS Router includes errors in the GraphQL `errors` array of the response. It uses the following default error structure:

```json
{
  "data": null,
  "errors": [
    {
      "message": "Request failed",
      "path": ["products"],
      "extensions": {
        "http": {
          "status": 500
        },
        "connector": {
          "coordinate": "ecomm:Query.products@connect[0]"
        },
        "code": "CONNECTOR_FETCH",
        "service": "ecomm"
      }
    }
  ]
}
```

Fields that return non-200 HTTP responses are set to `null` in the response's `data` attribute, following the [GraphQL specification](https://spec.graphql.org/draft/#sec-Response).

To include all the fields in the example error response, ensure you configure [subgraph error inclusion](https://www.apollographql.com/docs/graphos/routing/observability/subgraph-error-inclusion) in the router.

## Error handling customization

You can customize errors in the response using the `errors` property on `@source` or `@connect` directives.
The `errors` property lets you customize the `message` and `extensions` fields in `errors` objects in the GraphQL response using information from the HTTP response and literal values.

```json
{
  "data": null,
  "errors": [
    {
      "message": "Custom message", #highlight-line
      "path": ["products"],
      "extensions": { #highlight-line
        "http": { #highlight-line
          "customField": "Custom value" #highlight-line
        }, #highlight-line
      /// ...
      }
    }
  ]
}
```

The `errors.message` and `errors.extensions` fields take mapping expressions, which are applied on the response body, just like selection mapping.
You can access all of the mapping language's variables and methods in these fields.

### Customizing `errors.message`

You can set a custom error message using the `errors.message` property on `@connect` and `@source` directives.
For example, this schema:

```graphql
type Query {
  users: [User]
    @connect(
      http: { GET: "http://my-api.com/users" }
      selection: "id name"
      errors: {
        message: "error.message"
      }
    )
}
```

results in a GraphQL response with a customized `errors.message`:

```json
{
  "data": null,
  "errors": [
    {
      "message": "There was a critical failure!", #highlight-line
      "path": ["users"],
      /// ...
    }
  ]
}
```

The `errors.message` property expects a mapping expression that results in a string.

#### Valid `error.message` mapping expressions

The following are examples of valid mapping expressions for `errors.message`:

* Using a static [literal value](https://www.apollographql.com/docs/graphos/connectors/mapping/literals):

  ```graphql
  @connect(
    # --snip --
    errors: {
      message: "$('This is a hard-coded literal message')"
    }
  )
  ```

* Using a response field (in particular, `error.message`)\`:

  ```graphql
  @connect(
    # --snip --
    errors: {
      message: "error.message"
    }
  )
  ```

* Using a header value from the response with the [`$response.headers` variable](https://www.apollographql.com/docs/graphos/connectors/mapping/variables#responseheaders):

  ```graphql
  @connect(
    # --snip --
    errors: {
      message: "$response.headers.errorheader->first"
    }
  )
  ```

* Using the [`$` root element](https://www.apollographql.com/docs/graphos/connectors/mapping/variables) to access top-level response properties directly when the response is a simple key-value structure like `{ "error": "error message" }`:

  ```graphql
  @connect(
    # --snip --
    errors: {
      message: "$.error"
    }
  )
  ```

#### Invalid `error.message` mapping expressions

The following are examples of invalid mapping expressions for `errors.message`:

* Using a value that doesn't result in a string, for example, using the [`$status` variable](https://www.apollographql.com/docs/graphos/connectors/responses#status-variable), which returns a number:

  ```graphql title=❌ Invalid example
  @connect(
    # --snip --
    errors: {
      message: "$status"
    }
  )
  ```

* Using an object format:

  ```graphql title=❌ Invalid example
  @connect(
    # --snip --
    errors: {
      message: "myProperty: error.message"
    }
  )
  ```

#### `error.message` precedence rules

If both `@source` and `@connect` set `errors.message`, the `@connect`'s value takes precedence.

### Customizing `errors.extensions`

You can set custom error extensions using the `errors.extensions` property on `@connect` and `@source` directives.

```graphql
type Query {
  users: [User]
    @connect(
      http: { GET: "http://my-api.com/users" }
      selection: "id name"
      errors: {
        extensions: """
          code: error.code
          status: $status
        """
      }
    )
}
```

This customization sets additional properties in the GraphQL `errors.extensions` object:

```json
{
  "data": null,
  "errors": [
    {
      "message": "Request failed",
      "path": ["users"],
      "extensions": {
        "code": "INTERNAL_SERVER_ERROR", #highlight-line
        "status": 500, #highlight-line
        "http": {
          "status": 500
        },
        "connector": {
          "coordinate": "connector-graph:Query.users@connect[0]"
        }
      }
    }
  ]
}
```

The `errors.extensions` property expects a mapping expression that results in an object.

#### Valid `errors.extensions` mapping expressions

The following are examples of valid mapping expressions for `errors.extensions`:

* Using properties from the response:

  ```graphql
  @connect(
    # --snip --
    errors: {
      extensions: """
        code: error.code
      """
    }
  )
  ```

* Using the [`$status` variable](https://www.apollographql.com/docs/graphos/connectors/responses#status-variable):

  ```graphql
  @connect(
    # --snip --
    errors: {
      extensions: """
        status: $status
      """
    }
  )
  ```

* Using [literal values](https://www.apollographql.com/docs/graphos/connectors/mapping/literals) in a nested structure:

  ```graphql
  @connect(
    # --snip --
    errors: {
      extensions: """
        http: {
          myField: $("literal Value")
        }
      """
    }
  )
  ```

* Combining multiple properties from different sources:

  ```graphql
  @connect(
    # --snip --
    errors: {
      extensions: """
        code: error.code
        statusCode: $status
        errorDetails: {
          message: error.message
          timestamp: $response.headers."x-error-timestamp"->first
          source: $("backend-service")
        }
      """
    }
  )
  ```

#### Invalid `errors.extensions` mapping expressions

The following example is invalid because it uses a value that doesn't result in an object:

```graphql title=❌ Invalid example
@connect(
  # --snip --
  errors: {
    extensions: "$status"
  }
)
```

#### `errors.extensions` precedence rules

If both `@source` and the `@connect` set `errors.extensions` properties, the response contains both. The `extensions` object also retains its default properties. When properties are found in more than one of the three:

* Properties set in `@source` overwrite default properties
* Properties set in `@connect` overwrite `@source` properties

## Customize success conditions with `isSuccess`

By default, Apollo Connectors map successful `20X` HTTP responses to the `data` property of the GraphQL response, and map other status codes to the `errors` property. The `isSuccess` argument for both `@source` and `@connect` directives enables you to customize this behavior.

The `isSuccess` expression uses the [Connectors mapping language](https://www.apollographql.com/docs/graphos/connectors/mapping) and must evaluate to a boolean. If the result is true, the router applies the `selection` mapping to the response and merges the result to the `data` property. If it's false, the router applies the `errors.message` and `errors.extensions` mappings and appends the result to the `errors` property.

You can use expressions like `isSuccess: "$status->match([200, true], [400, true], [@, false])"` to map the response to data for specific status codes.

### Example: Treating all responses as successful

Here is an example that will never result in a GraphQL error by setting `isSuccess` to `true`:

```graphql
type Mutation {
  createProduct: CreateProductResponse!
    @connect(
      http: { GET: "https://api.dev/endpoint-that-can-fail" }
      isSuccess: "$(true)"
      selection: """
      product { id }
      errors { message }
      """
    )
}

type CreateProductResponse {
  product: Product
  errors: [Error]
}
```

In this example, even if the HTTP endpoint returns a non-200 status, the router will still map the response to the `data` property, allowing you to handle errors in your GraphQL schema structure instead of in the GraphQL errors array.

### Example: Treating specific status codes as successful

You can also specify which status codes should be considered successful:

```graphql
type Query {
  product(id: ID!): Product
    @connect(
      http: { GET: "https://api.dev/products/{$args.id}" }
      isSuccess: "$status->match([200, true], [404, true], [@, false])"
      selection: "id name"
    )
}
```

In this example, both 200 and 404 responses are treated as successful, allowing you to handle "not found" cases in your resolver logic rather than as GraphQL errors.

## Additional resources

* Refer the [mapping language documentation](https://www.apollographql.com/docs/graphos/connectors/mapping) for more information on writing mapping expressions.
* See the [common errors section](https://www.apollographql.com/docs/graphos/connectors/troubleshooting#common-errors) on the troubleshooting page for information on composition errors.
