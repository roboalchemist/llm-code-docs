# Apollo Federation Changelog

This article describes notable changes and additions introduced in each minor version release of Apollo Federation. Most of these changes involve additions or modifications to [federation-specific directives](https://www.apollographql.com/docs/graphos/reference/federation/directives/).

For a comprehensive changelog for Apollo Federation and its associated libraries, see [GitHub](https://github.com/apollographql/federation/blob/main/CHANGELOG.md).

* To use a feature introduced in a particular federation version, make sure your subgraph schema's `@link` directive targets that version (or higher):

  ```graphql
  extend schema
    @link(url: "https://specs.apollo.dev/federation/v2.3", #highlight-line
          import: ["@key", "@shareable", "@interfaceObject"])
  ```

  The example above must target at least Federation v2.3, because the `@interfaceObject` directive was introduced in that version.

  Before you increment a subgraph's federation version, update your router and build pipeline. For details, see [Updating your graph safely](https://www.apollographql.com/docs/graphos/platform/graph-management/updates).

* If you maintain a [subgraph-compatible library](https://www.apollographql.com/docs/graphos/reference/federation/compatible-subgraphs), consult this article to stay current with recently added directives. All of these directive definitions are also listed in the [subgraph specification](https://www.apollographql.com/docs/graphos/reference/federation/subgraph-spec/#subgraph-schema-additions).

## v2.13

| First release    | Available in GraphOS? | Minimum router version |
| ---------------- | --------------------- | ---------------------- |
| **January 2026** | **Yes**               | **`2.11.0`**           |

Federation v2.13 is a prerequisite for the Connector specification version 0.4.
[Learn more.](https://www.apollographql.com/docs/graphos/connectors/reference/changelog)

## v2.12

| First release     | Available in GraphOS? | Minimum router version |
| ----------------- | --------------------- | ---------------------- |
| **November 2025** | **Yes**               | **`2.8.0`**            |

Federation v2.12 is a prerequisite for the Connector specification version 0.3.
[Learn more.](https://www.apollographql.com/docs/graphos/connectors/reference/changelog)

#### Directive changes

#### `@cacheTag`

Introduced. This directive allows you to set cache tags that can be associated with cached entries using [response caching](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/overview). Learn more about how to invalidate specific data in your schema [using `@cacheTag`](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/invalidation#by-cache-tag).

```graphql
directive @cacheTag(format: String!) repeatable on FIELD_DEFINITION | OBJECT
```

## v2.11

| First release | Available in GraphOS? | Minimum router version |
| ------------- | --------------------- | ---------------------- |
| **June 2025** | **Yes**               | **`2.3.0`**            |

Federation v2.11 is a prerequisite for the Connector specification version 0.2.
[Learn more.](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives)

## v2.10

| First release     | Available in GraphOS? | Minimum router version |
| ----------------- | --------------------- | ---------------------- |
| **February 2025** | **Yes**               | **`2.0.0`**            |

Federation v2.10 is a prerequisite for the Connector specification that introduces the `@connect` and `@source` directives.
[Learn more.](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives)

## v2.9

| First release   | Available in GraphOS? | Minimum router version |
| --------------- | --------------------- | ---------------------- |
| **August 2024** | **Yes**               | **`1.53.0`**           |

#### Directive changes

#### `@cost`

Introduced. [Learn more](https://www.apollographql.com/docs/federation/federated-schemas/federated-directives#cost).

```graphql
directive @cost(weight: Int!) on
  | ARGUMENT_DEFINITION
  | ENUM
  | FIELD_DEFINITION
  | INPUT_FIELD_DEFINITION
  | OBJECT
  | SCALAR;
```

#### `@listSize`

Introduced. [Learn more](https://www.apollographql.com/docs/federation/federated-schemas/federated-directives#listsize).

```graphql
directive @listSize(
  assumedSize: Int
  slicingArguments: [String!]
  sizedFields: [String!]
  requireOneSlicingArgument: Boolean = true
)
on FIELD_DEFINITION;
```

## v2.8

| First release | Available in GraphOS? | Minimum router version |
| ------------- | --------------------- | ---------------------- |
| **May 2024**  | **Yes**               | **`1.48.0`**           |

#### Directive changes

##### `@context`

Introduced. [Learn more](https://www.apollographql.com/docs/graphos/reference/federation/directives/#context).

```graphql
directive @context(name: String!) on OBJECT | INTERFACE | UNION;
```

##### `@fromContext`

Introduced. [Learn more](https://www.apollographql.com/docs/graphos/reference/federation/directives/#fromcontext).

```graphql
scalar ContextFieldValue;

directive @fromContext(field: ContextFieldValue) on ARGUMENT_DEFINITION;
```

## v2.7

| First release     | Available in GraphOS? | Minimum router version |
| ----------------- | --------------------- | ---------------------- |
| **February 2024** | **Yes**               | **`1.39.0`**           |

#### Directive changes

##### Progressive `@override`

Added progressive `@override`. [Learn more.](https://www.apollographql.com/docs/graphos/reference/federation/directives/#progressive-override)

```graphql
directive @override(from: String!, label: String) on FIELD_DEFINITION
```

## v2.6

| First release     | Available in GraphOS? | Minimum router version |
| ----------------- | --------------------- | ---------------------- |
| **November 2023** | **Yes**               | **`1.35.0`**           |

#### Directive changes

##### `@policy`

Introduced. [Learn more.](https://www.apollographql.com/docs/graphos/routing/security/authorization)

```graphql
directive @policy(policies: [[federation__Policy!]!]!) on
  | FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | SCALAR
  | ENUM
```

##### Subgraph changes

Topic
Description

Policy

* Custom scalar representing an authorization policy. Used by new `@policy` directive.

## v2.5

| First release | Available in GraphOS? | Minimum router version |
| ------------- | --------------------- | ---------------------- |
| **July 2023** | **Yes**               | **`1.29.1`**           |

#### Directive changes

##### `@authenticated`

Introduced. [Learn more.](https://www.apollographql.com/docs/graphos/routing/security/authorization)

```graphql
directive @authenticated on
    FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | SCALAR
  | ENUM
```

##### `@requiresScopes`

Introduced. [Learn more.](https://www.apollographql.com/docs/graphos/routing/security/authorization)

```graphql
directive @requiresScopes(scopes: [[federation__Scope!]!]!) on
    FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | SCALAR
  | ENUM
```

#### Subgraph changes

Topic
Description

Scope

* Custom scalar representing a JWT scope. Used by new `@requiresScopes` directive.

## v2.4

| First release  | Available in GraphOS? | Minimum router version |
| -------------- | --------------------- | ---------------------- |
| **March 2023** | **Yes**               | **`1.13.1`**           |

#### Subgraph changes

Topic
Description

Subscriptions

* Composition now supports defining the `Subscription` type in subgraph schemas.
* Use of GraphQL subscriptions with a federated graph requires a compatible version of the GraphOS Router. [See details.](https://www.apollographql.com/docs/graphos/routing/operations/subscriptions/#prerequisites)

## v2.3

| First release     | Available in GraphOS? | Minimum router version |
| ----------------- | --------------------- | ---------------------- |
| **February 2023** | **Yes**               | **`1.10.2`**           |

#### Directive changes

##### `@interfaceObject`

Introduced. [Learn more.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/interfaces)

```graphql
directive @interfaceObject on OBJECT
```

##### `@key`

Can now be applied to interface definitions to support [entity interfaces](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/interfaces/).

(Previous versions of composition threw an error if `@key` was applied to an interface definition.)

## v2.2

| First release     | Available in GraphOS? | Minimum router version |
| ----------------- | --------------------- | ---------------------- |
| **November 2022** | **No**                | **`1.6.0`**            |

#### Directive changes

##### `@shareable`

Added `repeatable` to the directive definition.

```graphql
directive @shareable repeatable on OBJECT | FIELD_DEFINITION
```

Additionally, composition now throws an error if `@shareable` is applied to fields of an `interface` definition.

## v2.1

| First release   | Available in GraphOS? | Minimum router version |
| --------------- | --------------------- | ---------------------- |
| **August 2022** | **Yes**               | **`1.0.0`**            |

#### Directive changes

##### `@composeDirective`

Introduced. [Learn more.](https://www.apollographql.com/docs/graphos/reference/federation/directives#composedirective)

```graphql
directive @composeDirective(name: String!) repeatable on SCHEMA
```

##### `@requires`

The `fields` argument can now include fields that themselves take arguments. [Learn more.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#using-requires-with-fields-that-take-arguments)

(Functionality added in v2.1.2)

```graphql
type Product @key(fields: "id") {
  id: ID!
  weight(units: String): Int! @external
  #highlight-start
  shippingEstimate: Int! @requires(fields: "weight(units: \"KILOGRAMS\")")
  #highlight-end
}
```

## v2.0

| First release  | Available in GraphOS? | Minimum router version |
| -------------- | --------------------- | ---------------------- |
| **April 2022** | **Yes**               | **`1.0.0`**            |

#### Directive changes

Subgraph schemas "opt in" to Federation 2 features by applying the `@link` directive to the `schema` type, like so:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.0",
        import: ["@key", "@shareable"])
```

The `import` list of this definition must include each federation-specific directive that the subgraph schema uses. In the example above, the schema uses `@key` and `@shareable`.

For details on these directives as defined in Federation 2, see [Federation-specific GraphQL directives](https://www.apollographql.com/docs/graphos/reference/federation/directives/).

##### `@key`

Added optional `resolvable` argument.

```graphql
directive @key(
  fields: FieldSet!,
  resolvable: Boolean = true # highlight-line
) repeatable on OBJECT | INTERFACE
```

##### `@shareable`

Introduced.

```graphql
directive @shareable on OBJECT | FIELD_DEFINITION
```

##### `@inaccessible`

Introduced.

```graphql
directive @inaccessible on
  | FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | UNION
  | ARGUMENT_DEFINITION
  | SCALAR
  | ENUM
  | ENUM_VALUE
  | INPUT_OBJECT
  | INPUT_FIELD_DEFINITION
```

##### `@override`

Introduced.

```graphql
directive @override(from: String!) on FIELD_DEFINITION
```

##### `@link`

Introduced.

```graphql
directive @link(
  url: String,
  as: String,
  for: link__Purpose,
  import: [link__Import]
) repeatable on SCHEMA
```

##### `@extends`, `@external`, `@provides`, `@requires`, `@tag`

No changes.

#### Subgraph changes

Topic
Description

Entities

* Entities no longer originate in a subgraph. Instead, any number of subgraphs can define the same entity and contribute fields to it.
* Multiple subgraphs can contribute the same field to an entity, if that field is marked as `@shareable` in every subgraph that defines it.
* Subgraphs no longer need to `extend` (or `@extends`) an entity whenever another subgraph already defines that entity.
* Each subgraph can apply any number of `@key` directives to an entity.
* Subgraphs must no longer apply the `@external` directive to their `@key` fields.

Value types

* To define a value type with shared fields across multiple subgraphs, those shared fields must be marked as `@shareable` in every subgraph that defines them.
* Value type fields can differ across subgraphs (in certain ways). For details, see [Differing shared fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types#differing-shared-fields).

`Query` and `Mutation`

* More than one subgraph can define the same field of the `Query` or `Mutation` type, if that field is marked as `@shareable` in every subgraph that defines it.
* Subgraphs no longer need to apply the `extend` keyword (or the `@extends` directive) to the `Query` and `Mutation` types.

## v1.1

Apollo Router Core and GraphOS Router v1.60 and later don't support Federation v1.x supergraphs.

#### Directive changes

##### `@tag`

Introduced.

```graphql
directive @tag(name: String!) repeatable on
  | FIELD_DEFINITION
  | INTERFACE
  | OBJECT
  | UNION
```

## v1.0

Apollo Router Core and GraphOS Router v1.60 and later don't support Federation v1.x supergraphs.

#### Directive changes

For details on these directives as defined in Federation 1, see the [Federation 1 subgraph spec](https://www.apollographql.com/docs/federation/v1/federation-spec).

##### `@key`

Introduced.

```graphql
directive @key(fields: _FieldSet!) repeatable on OBJECT | INTERFACE
```

##### `@external`

Introduced.

```graphql
directive @external on FIELD_DEFINITION
```

##### `@requires`

Introduced.

```graphql
directive @requires(fields: _FieldSet!) on FIELD_DEFINITION
```

##### `@provides`

Introduced.

```graphql
directive @provides(fields: _FieldSet!) on FIELD_DEFINITION
```

##### `@extends`

Introduced.

```graphql
directive @extends on OBJECT | INTERFACE
```

#### Subgraph changes

Topic
Description

Entities

* Each entity originates in exactly one subgraph and can be extended in other subgraphs.
* An entity's originating subgraph must apply at least one `@key` directive to the entity definition.
* An extending subgraph must use the `extend` keyword (or the `@extends` directive) when defining another subgraph's entity.
* An extending subgraph must apply exactly one `@key` directive to any entity it extends. The `fields` of that `@key` must match a `@key` that's defined by the entity's originating subgraph.
* An extending subgraph must apply the `@external` directive to all `@key` fields of an entity it extends.
* If an entity field is defined in more than one subgraph, it must be marked as `@external` in all but one subgraph.

Value types

* Each subgraph that defines a value type must define that value type identically.

`Query` and `Mutation`

* More than one subgraph cannot define the same field of the `Query` or `Mutation` type.
* Every subgraph must apply the `extend` keyword (or the `@extends` directive) to the `Query` and `Mutation` types.
