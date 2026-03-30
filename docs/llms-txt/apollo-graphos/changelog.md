# Source: https://www.apollographql.com/docs/apollo-operator/changelog.md

# Source: https://www.apollographql.com/docs/graphos/resources/changelog.md

# Source: https://www.apollographql.com/docs/graphos/routing/changelog.md

# Source: https://www.apollographql.com/docs/graphos/connectors/reference/changelog.md

# Apollo Connectors Changelog

## Connectors 0.4 (experimental)

### Upgrade instructions

1. Upgrade local development environments for testing:
   * Set `federation_version` to `=2.13.0` or later in `supergraph.yaml`.
   * Update Rover to the latest version.
2. Update your deployed routers to v2.11.0 or later.
3. Enable the preview feature in your router configuration:
   ```yaml
   connectors:
     preview_connect_v0_4: true
   ```
4. Update your schemas to use Connectors v0.4:
   ```graphql
   extend schema
     @link(
       url: "https://specs.apollo.dev/connect/v0.4",
       import: ["@source", "@connect"]
     )
   ```

Learn more about [Connectors version requirements](https://www.apollographql.com/docs/graphos/connectors/getting-started/version-requirements).

### New features

#### Abstract type support

Connectors v0.4 introduces support for abstract types (`interface` and `union` types in GraphQL). This enables type polymorphism in your connector schemas, so you can:

* Define fields that return interface types.
* Define fields that return union types.
* Use `->match` with string literal `__typename` values to determine the concrete type at runtime.

Example with interfaces:

```graphql
extend schema
  @link(
    url: "https://specs.apollo.dev/connect/v0.4",
    import: ["@source", "@connect"]
  )

@source(name: "api", http: { baseURL: "https://api.example.com" })

interface Product {
  id: ID!
  title: String!
  price: Float!
}

type Book implements Product {
  id: ID!
  title: String!
  price: Float!
  author: String!
}

type Movie implements Product {
  id: ID!
  title: String!
  price: Float!
  director: String!
}

type Query {
  products: [Product!]!
    @connect(
      source: "api"
      http: { GET: "/products" }
      selection: """
      $.results {
        ... type->match(
          ["book", { __typename: "Book", id, title, price, author }],
          ["movie", { __typename: "Movie", id, title, price, director }]
        )
      }
      """
    )
}
```

For more details and examples, see [Abstract type support](https://www.apollographql.com/docs/graphos/connectors/reference/preview-features#abstract-type-support).

## Connectors 0.3 & Federation 2.12.0

### Upgrade instructions

1. Upgrade local development environments for testing:
   * `supergraph.yaml` files should have `federation_version` set to `=2.12.0` or later.
   * Rover should be v0.36.0 or later.
2. Update your deployed routers to support Connectors 0.3.
3. Update the **Build pipeline** in [GraphOS Studio](https://studio.apollographql.com/signup?type=enterprise-trial\&referrer=docs-content) to v2.12.
   * Go to your graph's **Settings** page and click **Update version** to update your **Federation version** to 2.12.
4. Update your schemas to use Connectors v0.3:
   ```graphql
   extend schema
     @link(
       url: "https://specs.apollo.dev/connect/v0.3",
       import: ["@source", "@connect"]
     )
   ```

Learn more about [Connectors version requirements](https://www.apollographql.com/docs/graphos/connectors/getting-started/version-requirements).

### New features

#### Environment variable access with `$env`

Access environment variables in your Connectors using the new `$env` variable. This is useful for API keys or other configuration values that you don't want to hard-code into your schema.

#### New array methods

Added new array manipulation methods:

* `find` - Returns the first item in an array that matches the specified criteria
* `filter` - Returns a new array containing all items that match the specified criteria
* `get` - Returns the character at a specified index (for strings), item at a specified index (for arrays), or property with a specified name (for objects)

#### New logical operators

Added logical operators for conditional expressions:

* `ne` - Not equal to
* `in` - Value is in the list of arguments
* `contains` - Array contains the argument value
* `lte` - Less than or equal to
* `gt` - Greater than
* `lt` - Less than
* `gte` - Greater than or equal to
* `or` - Logical OR
* `not` - Inverts boolean value
* `eq` - Equal to
* `and` - Logical AND

#### New math methods

Added mathematical operations:

* `mod` - Modulo operation (remainder after division)
* `sub` - Subtraction
* `add` - Addition
* `div` - Division
* `mul` - Multiplication

#### Type coercion methods

Added methods for type conversion:

* `parseInt` - Converts a value to an `Int`
* `toString` - Converts a value to a `String`

#### Nullish coalescing operators

The new `??` and `?!` operators enable providing default values when expressions evaluate to `null` or `None`:

* `??` - Coalesces on `null` or `None`
* `?!` - Coalesces only on `None`

```connectors
people: $(people ?? [])
bOrDefault: $(b ?? "default")
nullAllowed: $(null ?! "default")
safeSlice: array->slice($args.sliceStart ?? 0, $args.sliceEnd ?? 10)
```

#### Custom success handling with `isSuccess`

The new `isSuccess` argument for `@source` and `@connect` directives enables customizing how HTTP status codes are handled. By default, `20X` responses map to `data` and other status codes map to `errors`. With `isSuccess`, you can customize this behavior using expressions that evaluate to a boolean.

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
```

## Router 2.3.0 & Composition 2.11.0

### Upgrade instructions

1. Upgrade local development environments for testing:
   * `supergraph.yaml` files should have `federation_version` set to `=2.11.0` or later.
   * Rover should be v0.30.0 or later.
2. Update your deployed routers to v2.3.0.
3. Update the **Build pipeline** in [GraphOS Studio](https://studio.apollographql.com/signup?type=enterprise-trial\&referrer=docs-content) to v2.11.
   * Go to your graph's **Settings** page and click **Update version** to update your **Federation version** to 2.11.

Learn more about [Connectors version requirements](https://www.apollographql.com/docs/graphos/connectors/getting-started/version-requirements).

### New features

#### Resolve entities using Connectors on types

You can now add `@connect` directly on types instead of adding a `Query` or `Mutation` field.

```graphql title=Before
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
    @inaccessible
}
```

```graphql title=After
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
```

This eliminates the need to include `entity: true` when resolving entities. See [Where to use `@connect`](https://www.apollographql.com/docs/graphos/connectors/entities#where-to-use-connect) for details on when to use `@connect` on types and fields.

#### Batch requests with `$batch`

The new `$batch` variable allows you to address the N+1 problem by batching requests to REST batch endpoints. This helps optimize your API calls by reducing the number of network requests. Learn more in the [batch request documentation](https://www.apollographql.com/docs/graphos/connectors/requests/batching).

#### `joinNotNull` method

The new `->joinNotNull` method allows you to join a list of strings with a comma or other separators. It ignores any null values in the list.

```graphql
type Query {
  products(filterName: String, filterValue: [String]): [Product]
    @connect(
      source: "myApi"
      http: {
        GET: "/products?{$args.filterName}={$args.filterValue->joinNotNull(',')}"
      }
      selection: "id name reviews { id }"
    )
}
```

This is particularly useful for passing lists of IDs to a REST endpoint for batch requests.

```graphql
type Review
  @connect(
    source: "myApi"
    http: { GET: "/reviews?ids={$batch.id->joinNotNull(',')}" }
    selection: "id text rating"
  ) {
  id: ID!
  text: String!
  rating: Int!
}
```

#### Advanced request URL building

Building URLs is now more flexible with two new options:

* The `http.queryParams` argument supports [repeating and nullable query parameters](https://www.apollographql.com/docs/graphos/connectors/requests/url#advanced-query-parameters)
* The `http.path` argument enables building dynamic URL path segments with arrays of values as described in the [dynamic path segments documentation](https://www.apollographql.com/docs/graphos/connectors/requests/url#dynamic-path-segments).

#### Request and response header access

New variables `$request.headers` and `$response.headers` are now available to access request and response headers when building request URLs, bodies, and in selection mapping. This enables more sophisticated data transformation based on header values. See the [variables reference](https://www.apollographql.com/docs/graphos/connectors/mapping/variables) for usage details.

#### Non-JSON response support

Connectors now supports mapping against endpoints that return non-JSON content types, opening up text-based responses, empty responses, and more. See the [response handling documentation](https://www.apollographql.com/docs/graphos/connectors/responses#mapping-non-json-content-types) for details.

#### Customized error handling

Customize the `message` and `extensions` of the GraphQL response when an HTTP endpoint returns a non-200 status. This gives you greater control over error presentation to clients. Learn more in the [error handling documentation](https://www.apollographql.com/docs/graphos/connectors/responses/error-handling).

## Router 2.2.0

### New features

#### YAML-based header propagation

Connectors now support the router's [header propagation features](https://www.apollographql.com/docs/graphos/routing/header-propagation).
See the [Connectors traffic shaping documentation](https://www.apollographql.com/docs/graphos/connectors/deployment/overriding-headers#header-propagation) for configuration examples.

## Router 2.1.2 & Composition 2.10.2

### Bug fixes

* Fixed a bug that dropped [`@context`/`@fromContext`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/versions#context) directives from the supergraph schema when any subgraph schema uses Connectors. The [context pattern](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/use-contexts) is still available only for subgraph schemas that don't use Connectors.
* Fixed a bug relating to how [Connectors methods](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#methods) work. The fix standardizes `->method` behavior to apply to the full value of an expression, not each item, when the preceding expression returns an array. For example, prior to this change, the expression `$.id->jsonStringify` resulted in `["1","2","3"]`, with each item individually stringified. After the fix, the result is `'["1","2","3"]'`, with the entire array stringified.

## Router 2.1.0

### New features

#### Traffic shaping support

Connectors now support the router's [traffic shaping features](https://www.apollographql.com/docs/graphos/routing/performance/traffic-shaping).
See the [Connectors traffic shaping documentation](https://www.apollographql.com/docs/graphos/connectors/performance/traffic-shaping) for configuration examples.

#### TLS support

Connectors now support the router's [TLS features](https://www.apollographql.com/docs/graphos/routing/security/tls) to authenticate and encrypt communications.
See the [Connectors traffic shaping documentation](https://www.apollographql.com/docs/graphos/connectors/security/tls) for configuration examples.

## 2025-02-18

**Router 2.0.0 & Composition 2.10.0**

### New features

#### General availability of Apollo Connectors

Apollo Connectors is now [generally available](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages#general-availability).

#### Migrating from Apollo Connectors preview releases

You must migrate your router Connectors configuration to the GA format once you update your router to v2.0.0. When you update to v2.0.0, configurations from preview releases no longer work.

The key changes between preview and GA versions:

* The top-level `preview-connectors` configuration has been renamed to `connectors`.
* Configuration that was previously under `subgraphs` has now moved to `sources`.
* Each Connector source is now configured under an entry combining the subgraph name and source name, separated by a `.`—for example, `subgraph_name.source_name`.
* Any `$config` variables should now be placed under their corresponding source configuration.

For example, given the following preview configuration:

```yaml title=router.yaml
preview_connectors:
   # This applies globally to all Connectors
  max_requests_per_operation_per_source: 100
  subgraphs:
    example: # The name of the subgraph
      $config:
        my.config.value: true # Applies to all sources in this subgraph
      sources:
        v1: # Refers to @source(name: "v1")
          # These configurations apply to Connectors with the "endpoint1" source in the "subgraph1" subgraph
          override_url: 'https://localhost:5000'
          max_requests_per_operation: 50
        v2: # Refers to @source(name: "v2")
          #  These configurations apply to Connectors with the "endpoint2" source in the "subgraph1" subgraph
          max_requests_per_operation: 100
```

The GA configuration would look like this:

```yaml title=router.yaml
connectors:
   # This applies globally to all Connectors
  max_requests_per_operation_per_source: 100
  sources:
    subgraph1.endpoint1: # subgraph.source
      # These configurations apply to Connectors with the "endpoint1" source in the "subgraph1" subgraph
      override_url: 'https://localhost:5000'
      max_requests_per_operation: 50
      $config:
        my.config.value: true # Applies to the "v1" source
    subgraph1.endpoint2: # subgraph.source
      # These configurations apply to Connectors with the "endpoint2" source in the "subgraph1" subgraph
      max_requests_per_operation: 25
      another.config.value: true # Applies to the "v2" source
```

## Deprecated preview releases

The following changelog entries are for deprecated preview release versions.
Use the [generally available router and federation versions](https://www.apollographql.com/docs/graphos/connectors/reference/changelog.md#general-availability-of-apollo-connectors) for a fully supported and feature-complete experience.

### 2025-02-06

**Router 2.0.0-preview\.6 & Composition 2.10.0-preview\.6**

#### Fixes

* Improve composition performance
* Provide a clearer error when the version of Connectors is incorrect in a `@link` directive

### 2025-01-31

**Router 2.0.0-preview\.5 & Composition 2.10.0-preview\.5**

#### Breaking changes

* When the `->map` method is applied to a non-list value, the result is now a list. For example `$(1)->map(@)` results in `[1]`.

#### New features

* The [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) is officially available. Use it to experiment and troubleshoot mapping expressions.

#### New validations

* Validations on the `http.body` now catch more types of errors. For example,  validations now flag selections that don't come from a variable (`myField` instead of `$this.myField`).

#### Fixes

* The router no longer tries to parse an empty API response. If your API responds with nothing, you can use literal values like `success: $(true)` to map to your schema.
* The `@cost` and `@listSize` directives are preserved to support [Demand Control](https://www.apollographql.com/docs/graphos/routing/security/demand-control).
* Types marked with `@external` are handled correctly.

### 2025-01-15

**Router 2.0.0-preview\.4 & Composition 2.10.0-preview\.4**

#### Breaking changes

* Adding a `@key` directive to a type signals to the query planner that this subgraph implements an entity resolver for that type. When using Connectors, you can accomplish this by adding an `entity: true` argument to the Connector.

  * If you see an error like `Entity resolution for @key(fields: "id") on Product is not implemented by a connector`, it means you need to either add an `entity: true` Connector or add `resolvable: false` to the`@key` directive.
  * See the [Rules for `entity: true`](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives#rules-for-entity-true) for more details.

* Header expressions now match the behavior of URI templates, so arrays and objects are no longer allowed. You can restore the old behavior using `->jsonStringify` or explore other [methods](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#value-transformations).

#### New features

* Includes all changes from router [v1.59.1](https://github.com/apollographql/router/releases/tag/v1.59.1).
* Better type inference and validations for selection mappings.
* The `jsonStringify` [value transformation](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#methods) is available to JSON stringify any value.
* Expressions within URIs and headers now support the full power of [mapping expressions](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping).
  * Within the dynamic `{ }` pieces of a URI or header, you can apply the same transformations allowed within `selection` and `body`.
  * The expression's result must be a simple scalar value.
  * Arrays and objects can't be serialized into URI or header values.

### 2024-12-09

**Router 2.0.0-preview\.3 & Composition 2.10.0-preview\.3**

#### Breaking changes to URI templates

* Arrays and objects can no longer be used in URI templates. If you need to convert complex types into URI parameters, contact Apollo to request new functionality and how you'd like them to be serialized.
* `null` values will now render in URIs as empty strings (`""`) instead of `"null"`.
* If an expression within the key or value of a query parameter is missing, it will now be rendered as an empty string instead of omitting the query parameter entirely.
* Missing values in path parameters will now render as empty strings instead of returning errors.

#### New validations

* Certain headers are already restricted by the router. Composition will now emit an error if one of these is set in `@source` or `@connect`.
* Variables used within headers are now validated at composition time.

#### New features

* Includes all changes from router [v1.58.1](https://github.com/apollographql/router/releases/tag/v1.58.1).
* `$args` and `$this` variables can be used in HTTP headers for Connectors.
* The `$context` variable is available in selection mapping, as well as URLs, headers, and body mappings.
* The `$status` variable, representing the HTTP Status Code (200, 404, etc.) is available in selection mapping.

#### Bug fixes

* Fixed a couple of edge cases where composition would fail. A small fraction of supergraph still [do not compose](https://www.apollographql.com/docs/graphos/connectors/limitations#some-supergraphs-are-unsupported).
* Connectors debugging information is now included for multipart responses, like when `@defer` is used.
* Composition will no longer emit "unused field" errors if another error (such as a selection parse error) happens first. This makes it easier to spot the most important errors.
* [Escape sequences](https://spec.graphql.org/October2021/#sec-String-Value) in selection and body strings are handled correctly.

### 2024-11-08

**Router 2.0.0-preview\.1 & Composition 2.10.0-preview\.2**

#### New features

* Includes all changes from Router [1.57.0](https://github.com/apollographql/router/releases/tag/v1.57.0).
* [Router telemetry](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry) can now be configured for Connectors.
* Connectors can now [invoke AWS HTTP APIs using SigV4](https://www.apollographql.com/docs/graphos/connectors/security/service-to-service-auth).
* The `content-length` header is automatically set on `POST`, `PATCH`, and `PUT` requests.
* Error messages for parsing errors in `@connect(selection:)` and `@connect(http: { body: })` are more informative.
* Using coprocessors to fetch authentication tokens is now easier. See [authentication with coprocessors](https://www.apollographql.com/docs/graphos/connectors/reference/router#authentication-with-coprocessors).

#### Bug fixes

* Fixed a bug where `$this.siblingField.nestedField` failed to compose.
* A non-JSON response no longer causes all responses to fail.

### 2024-10-01

**Router 2.0.0-preview\.0 & Composition 2.10.0-preview\.0**

#### Selection mapping enhancements

* To distinguish a path consisting of a single key from a field name,
  you should now use `$.key` instead of `.key`. The `.key` syntax is now
  forbidden since it can accidentally parse as a continuation of a previous
  selection, whereas `$.key` is unambiguous.

* Multiple deeply nested properties can now be flattened into the same output
  object alongside shallower properties:

  ```graphql
  id
  model
  choices->first.message { role content }
  ```

  This selection produces an object with `id`, `model`, `role`, and `content`
  properties, all at the same level.

  Previously, to achieve the same output, it was necessary to repeat the
  `choices->first.message` path multiple times:

  ```graphql
  id
  model
  role: choices->first.message.role
  content: choices->first.message.content
  ```

#### Improvements

* Includes all changes from router release [1.56](https://github.com/apollographql/router/releases/tag/v1.56.0).

### 2024-09-23

**Router 2.0.0-alpha.7 & Composition 2.10.0-alpha.4**

#### Selection mapping enhancements

* Support for [value transforms](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#methods) in selection mapping.
* Support for [literal values](https://www.apollographql.com/docs/graphos/schema-design/connectors/mapping#literal-values) in selection mapping.

#### New validations

* URL template arguments are now validated and must correspond to existing fields (`$this`) or arguments (`$args`).
* `entity: true` Connectors have several new validations, including enforcing that arguments match entity fields.

### 2024-09-11

**Router 2.0.0-alpha.6 & Composition 2.10.0-alpha.3**

#### New validations

* Require that all fields are resolvable through a Connector.

#### New features

* Connectors now obey the `include_subgraph_errors` configuration.

#### Improvements

* Includes all changes from router release [1.54](https://github.com/apollographql/router/releases/tag/v1.54.0).
* When running the router in development mode, the local Sandbox will have the Connectors debug panel enabled by default.

### 2024-09-06

**Router 2.0.0-alpha.5 & Composition 2.10.0-alpha.2**

#### New validations

* Require that every field of an object is included in at least one `selection`.
* When using Connectors, require that fields with arguments use a `@connect` directive.

#### New features

* [URL-encoded forms](https://www.apollographql.com/docs/graphos/connectors/requests/#form-url-encoding) are now supported in `body` parameters.

#### Improvements

* Includes all changes from router release [1.52.1](https://github.com/apollographql/router/releases/tag/v1.52.1).
* Includes all changes from router release [1.53.0](https://github.com/apollographql/router/releases/tag/v1.53.0).
* Includes all changes from federation composition release [2.9.0](https://github.com/apollographql/federation/releases/tag/%40apollo%2Fcomposition%402.9.0).
* Better detect circular references in Connector selections.

### 2024-08-20

**Router 2.0.0-alpha.3 & Composition 2.10.0-alpha.0**

#### New validations

New errors will be caught during composition, which may cause previously successful compositions to fail:

* Referring to a field name within `selection` which doesn't exist.

#### Improvements

* Fully support `$this` and `$args` in `http.body`.
* Allow subgraph names which are not GraphQL identifiers, for example, `my-subgraph`.
* Allow [`$config` values in headers](https://www.apollographql.com/docs/graphos/connectors/deployment/configuration#accessing-router-configuration-in-connectors).
* Ability to set [request limits](https://www.apollographql.com/docs/graphos/connectors/security/request-limits) for Connectors.
