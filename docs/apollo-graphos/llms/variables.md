# Source: https://www.apollographql.com/docs/graphos/connectors/mapping/variables.md

# Mapping Variable Reference

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

Variables are the building blocks for transforming data in GraphOS Connectors. They provide access to the various data sources that can be used in your mapping expressions, allowing you to dynamically connect your GraphQL schema to your REST APIs.

Variables can refer to:

* GraphQL arguments
* sibling fields from parent objects
* request and response data
* information from the router

## Available variables

The available variables depend on the context of the expression.

Variable
Definition
Availability Notes

#### `$`

At the top level, `$` refers to the root of the API response body.

Within a `{...}` sub-selection, `$` refers to the value of the parent. [See an example.](https://www.apollographql.com/docs/graphos/connectors/mapping/variables.md#-2)

* Only available in `@connect`'s [`selection`](https://www.apollographql.com/docs/graphos/connectors/responses/fields) and [`errors`](https://www.apollographql.com/docs/graphos/connectors/responses/error-handling) fields.

* Not available in `@source`.

#### `$args`

The arguments passed to the field in the GraphQL query.
For a field defined like `product(id: ID!): Product`, `$args.id` refers to the `id` argument passed to the `product` field.

* Available in any expression in a `@connect` directive if arguments are defined for the field.

* Not available in `@source`.

#### `$batch`

Provides a list of entity references so that multiple requests can be batched into a single request. [Learn about batching](https://www.apollographql.com/docs/graphos/connectors/requests/batching).

* Only available in `@connect` on types, not on fields.

* Not available in `@source`.

* Follow these [`$batch` rules to ensure data integrity](https://www.apollographql.com/docs/graphos/connectors/requests/batching#rules-for-batch-connectors).

#### `$config`

Variables set [in the GraphOS Router configuration](https://www.apollographql.com/docs/graphos/connectors/deployment/configuration#accessing-router-configuration-in-connectors).
Always available.

#### `$context`

Context set by router customizations like [coprocessors](https://www.apollographql.com/docs/graphos/routing/customization/coprocessor).

Only available if router customizations exist where context has been set.

#### `$env`

Environment variables available in the router process. This is useful for API keys or other configuration values that you don't want to hardcode into your schema or config file.

Always available.

#### `$request.headers`

Headers of the incoming request to the router.

Because an HTTP header can contain multiple values, `$request.headers.x` is always an array.
Use `->first` to grab the first item:

```connectors
$request.headers.authorization->first
$request.headers.'x-my-header'->first
```

Always available.

#### `$response.headers`

Headers of the response from the connected HTTP endpoint.

Because an HTTP header can contain multiple values, `$request.headers.x` is always an array.
Use `->first` to grab the first item:

```connectors
$request.headers.authorization->first
$request.headers.'x-my-header'->first
```

Available in [`selection`](https://www.apollographql.com/docs/graphos/connectors/responses/fields) and [`errors`](https://www.apollographql.com/docs/graphos/connectors/responses/error-handling).

#### `$status`

The numeric HTTP status code (`200`, `404`, etc.) from the response of the connected HTTP endpoint.

* Only available in `@connect`'s [`selection`](https://www.apollographql.com/docs/graphos/connectors/responses/fields) and [`errors`](https://www.apollographql.com/docs/graphos/connectors/responses/error-handling) fields.

* Not available in `@source`.

#### `$this`

The parent object of the current field. Can be used to access sibling fields. [Learn about dependencies `$this` can create.](https://www.apollographql.com/docs/graphos/connectors/mapping/variables.md#this-1)

* Only available on non-root types, that is, not within `Query` or `Mutation` Connectors.

* Not available in `@source`.

#### `@`

The value being transformed with a [method](https://www.apollographql.com/docs/graphos/connectors/mapping/variables.md#methods). Behaves differently depending on the context. [Learn more.](https://www.apollographql.com/docs/graphos/connectors/mapping/variables.md#-3)
Depends on the specific transformation method or mapping being applied.

## Additional variable notes

### `$`

When used at the top-level of an expression, `$` is only valid within the [`selection`](https://www.apollographql.com/docs/graphos/connectors/responses/fields) and [`errors`](https://www.apollographql.com/docs/graphos/connectors/responses/error-handling) fields of a Connector, and refers
to the root of the response body from the API. When used within a `{...}` sub-selection, `$` refers to the value of the parent.

```connectors
$.results {  # Here `$` refers to the response body
  id: $.id  # `$` refers to the `results` field
}
```

### `$this`

Using `$this` creates a dependency between the Connector and fields on the parent object. This implies that another Connector or another subgraph can provide this field.

```graphql
type Product {
  id: ID!
  reviews: [Review]
    # Some other Connector or subgraph provides the `id` value.
    @connect(http: { GET: "/products/{$this.id}/reviews" }, selection: "id rating comment")
}
```

This feature of `$this` is equivalent to the [`@requires` directive in Apollo Federation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#contributing-computed-entity-fields).

For example, the following Connectors usage is equivalent to the following `@requires` usage in a subgraph schema.

```graphql
type Product {
  id: ID!
  weight: Int
  shippingCost: Int @connect(http: { GET: "/shipping?weight={$this.weight}" }, selection: "$")
}
```

```graphql
type Product @key(fields: "id") {
  id: ID!
  weight: Int @external
  shippingCost: Int @requires(fields: "weight")
}
```

In fact, you can [combine Connectors with `@requires`](https://www.apollographql.com/docs/graphos/schema-design/connectors/federation#add-a-computed-field-using-requires) to create computed fields using REST APIs.

### `@`

Refers to the value being transformed with a [method](https://www.apollographql.com/docs/graphos/connectors/mapping/methods), which is sometimes the same as `$`, but not always.

For example, in the `value->echo({ wrapped: @ })` example in the [methods section](https://www.apollographql.com/docs/graphos/connectors/mapping/methods), `@` refers to the value of `value`, while `$`
refers to the object containing `value`.

Additionally, in the `colors->map({ name: @ })` example, the method binds `@` to each element in the `$.colors` list, while `$` remains unchanged.
