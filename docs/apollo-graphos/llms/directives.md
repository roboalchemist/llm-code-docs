# Source: https://www.apollographql.com/docs/apollo-server/schema/directives.md

# Source: https://www.apollographql.com/docs/react/data/directives.md

# Source: https://www.apollographql.com/docs/graphos/connectors/reference/directives.md

# Source: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md

# Apollo Federation Directives

Apollo Federation defines a collection of directives that you use in your subgraph schemas to enable certain features.

## Importing directives

To use federated directives in a Federation 2 subgraph schema, apply the `@link` directive with the following format to the `schema` type:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3",
        import: ["@key", "@shareable"])
```

You can apply this directive to your existing `schema` declaration if you have one, or to a new `extend schema` declaration (as shown above).

Modify the `import` array to include whichever federated directives your subgraph schema uses. The example above imports the [`@key`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#key) and [`@shareable`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#shareable) directives (which are used most commonly).

Make sure to include the `@` in each directive name.

### Renaming directives

If an imported directive's default name matches one of your own custom directives, you can rename the imported directive with the following syntax:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3",
        import: [{ name: "@key", as: "@uniqueKey"}, "@shareable"])
```

This example subgraph schema uses `@uniqueKey` for the federated directive usually named [`@key`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#key).

### Namespaced directives

If you don't [import a particular directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#importing-directives) from a linked spec, you can still use that directive in your subgraph schema. However, that directive is namespaced with a prefix:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3",
        import: ["@key"])

type Book @federation__shareable {
  title: String!
}
```

In the example above, `@shareable` is not imported from the federation spec. Therefore, it is available as `@federation__shareable`.

The default namespace prefix for a `@link`ed directive is the name of its associated specification (indicated by the penultimate component of `url`), plus two underscores (`__`). For Apollo Federation directives, this prefix is `federation__`.

You can customize a particular specification's namespace prefix by providing the `as` argument to `@link`:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3",
        as: "fed")

type Book @fed__shareable {
  title: String!
}
```

As shown, custom namespace prefixes also end in two underscores.

## Managing schemas

### The `@link` directive

```graphql
directive @link(
  url: String!,
  as: String,
  for: link__Purpose,
  import: [link__Import]
) repeatable on SCHEMA
```

This directive links definitions from an external specification to this schema. Every Federation 2 subgraph uses the `@link` directive to import the other federation-specific directives described in this article (see the syntax in [Importing directives](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#importing-directives)).

Subgraph schemas opt in to Federation v2 features by applying the `@link` directive to the `schema` type. You can optionally add an `import` list to this definition to include each federation-specific directive that the subgraph schema uses. In the example below, the schema uses the `@key` and `@shareable` directives:

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.0",
        import: ["@key", "@shareable"])
```

You can use `@link` to distinguish between Federation v1 (no `@link`) and Federation v2 (required `@link`) schemas.

For more information on `@link`, see the [official spec](https://specs.apollo.dev/link/v1.0/).

## Managing types

### `@key`

```graphql
directive @key(fields: FieldSet!, resolvable: Boolean = true) repeatable on OBJECT | INTERFACE
```

Designates an object type as an entity and specifies its key fields. Key fields are a set of fields that a subgraph can use to uniquely identify any instance of the entity.

```graphql
type Product @key(fields: "id") {
  id: ID!
  name: String!
  price: Int
}
```

To learn best practices and advanced use cases for `@key`, refer to the following guides:

* [Introduction to entities](https://www.apollographql.com/docs/graphos/get-started/guides/federate-schemas#entity-overview)
* [Define advanced keys](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys)

You can apply multiple `@key` directives to a single entity to specify multiple valid sets of key fields, if your subgraph library supports repeatable directives:

```graphql
type Product @key(fields: "upc") @key(fields: "sku") {
  upc: ID!
  sku: ID!
  name: String
}
```

To check whether your subgraph library supports repeatable directives, see the `repeatable @key` item in [Federation-compatible subgraph implementations](https://www.apollographql.com/docs/graphos/reference/federation/compatible-subgraphs).

In Apollo Federation 2.3 and later, you can also apply `@key` to `interface` definitions to create [entity interfaces](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/interfaces/). If you apply `@key` to an `interface` in earlier versions of Federation 2, a composition error occurs.

#### Arguments

Name /Type
Description

##### `fields`

`FieldSet!`

**Required.** A GraphQL selection set (provided as a string) of fields and subfields that contribute to the entity's unique key.

Examples:

* `"id"`
* `"username region"`
* `"name organization { id }"`

See also [Advanced `@key`s](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/define-keys).

##### `resolvable`

`Boolean`

If `false`, indicates to the router that this subgraph doesn't define a [reference resolver](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro/#2-define-a-reference-resolver) for this entity. This means that router query plans can't "jump to" this subgraph to resolve fields that aren't defined in another subgraph.

Most commonly, you set this to `false` when [referencing an entity without contributing fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#referencing-an-entity-without-contributing-fields).

The default value is `true`.

### `@interfaceObject`

```graphql
directive @interfaceObject on OBJECT
```

Indicates that an object definition serves as an abstraction of another subgraph's entity interface. This abstraction enables a subgraph to automatically contribute fields to all entities that implement a particular entity interface.

During composition, the fields of every `@interfaceObject` are added both to their corresponding `interface` definition and to all entity types that implement that interface.

[Learn more about entity interfaces.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/interfaces/)

### `@extends`

```graphql
directive @extends on OBJECT | INTERFACE
```

Indicates that an object or interface definition is an extension of another definition of that same type.

If your subgraph library supports GraphQL's built-in `extend` keyword, do not use this directive. Instead, use `extend`.

This directive is for use with GraphQL subgraph libraries that do not support the `extend` keyword. Most commonly, these are subgraph libraries that generate their schema programmatically instead of using a static `.graphql` file.

Federation 2 does not require any use of type extensions.

In Federation 1, every subgraph must extend the `Query` and `Mutation` types (if it defines them), and entities are extended in every subgraph that defines them except their originating subgraph.

## Managing shared fields

### `@shareable`

```graphql
directive @shareable repeatable on FIELD_DEFINITION | OBJECT
```

`@shareable` is only `repeatable` in [v2.2](https://www.apollographql.com/docs/graphos/reference/federation/versions#v22) and later.

Indicates that an object type's field is allowed to be resolved by multiple subgraphs (by default in Federation 2, object fields can be resolved by only one subgraph).

```graphql
type Position {
  x: Int! @shareable
  y: Int! @shareable
}
```

If applied to an object type definition, all of that type's fields are considered `@shareable`:

```graphql
type Position @shareable {
  x: Int!
  y: Int!
}
```

If a field is marked `@shareable` in any subgraph, it must be marked as either `@shareable` or [`@external`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#external) in every Federation 2 subgraph that defines it.

If a Federation 2 supergraph includes a Federation 1 subgraph, all value types in the Federation 1 subgraph are automatically considered `@shareable` by the Federation 2 composition algorithm.

If a field is included in an entity's [`@key` directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#key), that field is automatically considered `@shareable` and the directive is not required in the corresponding subgraph(s).

See also [Value types in Apollo Federation](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types/) and [Resolving another subgraph's field](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/resolve-another-subgraphs-fields).

The `@shareable` directive is about indicating when an object field can be resolved by multiple subgraphs. As interface fields are not directly resolved (their implementation is), `@shareable` is not meaningful on an interface field and is not allowed (at least since federation 2.2; earlier versions of federation 2 mistakenly ignored `@shareable` on interface fields).

### `@inaccessible`

```graphql
directive @inaccessible on FIELD_DEFINITION | INTERFACE | OBJECT | UNION | ARGUMENT_DEFINITION | SCALAR | ENUM | ENUM_VALUE | INPUT_OBJECT | INPUT_FIELD_DEFINITION
```

Indicates that a definition in the subgraph schema should be omitted from the router's [API schema](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/schema-types/#api-schema), even if that definition is also present in other subgraphs. This means that the field is not exposed to clients at all.

Common use cases for `@inaccessible` include:

* Avoiding composition errors while making staggered updates to a definition that's shared across multiple subgraphs (such as a [value type](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types/#adding-new-shared-fields))
* Using a private field as part of an entity's [`@key`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#key) without exposing that field to clients

Unlike with most directives, composition preserves uses of this directive in the generated supergraph schema. To preserve uses of other directives, see [`@composeDirective`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#composedirective).

Consequently, if you [rename this directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#renaming-directives), you must use the same name in every subgraph. Otherwise, a composition error occurs due to a naming mismatch.

```graphql title=Subgraph A
type Position @shareable {
  x: Int!
  y: Int!
  z: Int! @inaccessible
}
```

```graphql title=Subgraph B
type Position @shareable {
  x: Int!
  y: Int!
  # Subgraph is not yet updated
}
```

Often when you add a field to a value type in one subgraph, composition fails because that field isn't resolvable in other subgraphs. With `@inaccessible`, you can preserve composition while adding the field to your remaining subgraphs. When the rollout is complete, you can remove the directive and begin using the field.

An `@inaccessible` field or type is not omitted from the supergraph schema, so the router still knows it exists (but clients can't include it in operations). This is what enables the router to use an `@inaccessible` field as part of an entity's `@key` when combining entity fields from multiple subgraphs.

If a type is marked `@inaccessible`, all fields that return that type must also be marked `@inaccessible`. Otherwise, a composition error occurs.

For more information, see [Using `@inaccessible`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types/#using-inaccessible).

### `@override`

```graphql
directive @override(from: String!) on FIELD_DEFINITION
```

Indicates that an object field is now resolved by this subgraph instead of another subgraph where it's also defined. This enables you to migrate a field from one subgraph to another.

You can apply `@override` to [entity](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/) fields and fields of the root operation types (such as `Query` and `Mutation`).

```graphql title=Products subgraph
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean!
}
```

```graphql title=Inventory subgraph
type Product @key(fields: "id") {
  id: ID!
  inStock: Boolean! @override(from: "Products")
}
```

In the example above, we're migrating the `Product.inStock` field from the Products subgraph to the Inventory subgraph. The composed supergraph schema indicates that `Product.inStock` is resolved by the Inventory subgraph but not the Products subgraph, even though the Products subgraph also defines the field.

You can apply `@override` to a [`@shareable`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#shareable) field. If you do, only the subgraph you provide in the `from` argument no longer resolves that field. Other subgraphs can still resolve the field.

Only one subgraph can `@override` any given field. If multiple subgraphs attempt to `@override` the same field, a composition error occurs.

For more information, see [Migrating entity and root fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/migrate-fields).

#### Progressive `@override`

Rolling out any change to a production subgraph, including field migration, risks degrading the performance of your graph. Rerouting all traffic from one subgraph to another all at once could overload the overriding subgraph.

The *progressive `@override`* feature enables the gradual, progressive deployment of a subgraph with an `@override` field. As a subgraph developer, you can customize the percentage of traffic that the overriding and overridden subgraphs each resolve for a field. You apply a label to an `@override` field to set the percentage of traffic for the field that should be resolved by the overriding subgraph, with the remaining percentage resolved by the overridden subgraph. You can then monitor the performance of the subgraphs in Studio, resolve any issues, and iteratively and progressively increase the percentage until all traffic is resolved by the overriding subgraph.

To learn more, see the [Incremental migration with `@override`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/migrate-fields#incremental-migration-with-progressive-override) guide.

#### Arguments

Name /Type
Description

##### `from`

`String!`

**Required.** The name of the other subgraph that no longer resolves the field.

* If you're performing composition with managed federation, this must match the name of the subgraph registered to GraphOS.
* If you're performing composition with the Rover CLI, this must match the name of the subgraph in the YAML config file you provide to `rover supergraph compose`.

##### `label`

`String`

**Optional.** A string of arbitrary arguments. Supported in this release:

* `percent(<percent-value>)` - The percentage of traffic for the field that's resolved by this subgraph. The remaining percentage is resolved by the other ([from](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#from)) subgraph. To learn more, see [Incremental migration with `@override`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/migrate-fields#incremental-migration-with-progressive-override).

## Controlling access

### `@authenticated`

Rate limits apply on the Free plan.

Federation v2.9 and above doesn't allow `@authenticated` on interfaces. Applying `@authenticated` to an interface type, interface field or an interface object type results in a composition error.

```graphql
directive @authenticated on
    FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | SCALAR
  | ENUM
```

Indicates to composition that the target element is accessible only to the authenticated supergraph users. For more granular access control, see the [`@requiresScopes`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#requiresScopes) directive below. Refer to the [router article](https://www.apollographql.com/docs/graphos/routing/security/authorization#authenticated) for additional details.

### `@requiresScopes`

Rate limits apply on the Free plan.

Federation v2.9 and above doesn't allow `@requiresScopes` on interfaces. Applying `@requiresScopes` to an interface type, interface field or an interface object type results in a composition error.

```graphql
directive @requiresScopes(scopes: [[federation__Scope!]!]!) on
    FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | SCALAR
  | ENUM
```

Indicates to composition that the target element is accessible only to the authenticated supergraph users with the appropriate JWT scopes. Refer to the [router article](https://www.apollographql.com/docs/graphos/routing/security/authorization#requiresscopes) for additional details.

#### Arguments

Name /Type
Description

##### `scopes`

`[federation__Scope!]!`

**Required.** List of JWT scopes that must be granted to the user in order to access the underlying element data.

### `@policy`

Rate limits apply on the Free plan.

Federation v2.9 and above doesn't allow `@policy` on interfaces. Applying `@policy` to an interface type, interface field or an interface object type results in a composition error.

```graphql
directive @policy(policies: [[federation__Policy!]!]!) on
  | FIELD_DEFINITION
  | OBJECT
  | INTERFACE
  | SCALAR
  | ENUM
```

Indicates to composition that the target element is restricted based on authorization policies that are evaluated in a Rhai script or coprocessor. Refer to the [router article](https://www.apollographql.com/docs/graphos/routing/security/authorization#policy) for additional details.

#### Arguments

Name /Type
Description

##### `policies`

`[federation__Policy!]!`

**Required.** List of authorization policies to evaluate.

## Referencing external fields

### `@external`

```graphql
directive @external on FIELD_DEFINITION | OBJECT
```

Indicates that this subgraph usually can't resolve a particular object field, but it still needs to define that field for other purposes.

This directive is always used in combination with another directive that references object fields, such as [`@provides`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#provides) or [`@requires`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#requires).

```graphql title=Inventory subgraph
type Product @key(fields: "id") {
  id: ID!
  name: String! @external
  inStock: Boolean!
}

type Query {
  outOfStockProducts: [Product!]! @provides(fields: "name")
  discontinuedProducts: [Product!]!
}
```

This example subgraph usually can't resolve the `Product.name` field, but it can at the `Query.outOfStockProducts` query path (indicated by the [`@provides` directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#provides)).

If applied to an object type definition, all of that type's fields are considered `@external`:

```graphql
type Position @external {
  x: Int!
  y: Int!
}
```

### `@provides`

```graphql
directive @provides(fields: FieldSet!) on FIELD_DEFINITION
```

Specifies a set of entity fields that a subgraph can resolve, but only at a particular schema path (at other paths, the subgraph can't resolve those fields).

If a subgraph can always resolve a particular entity field, do not apply this directive.

Using this directive is always an optional optimization. It can reduce the total number of subgraphs that your router needs to communicate with to resolve certain operations, which can improve performance.

```graphql title=Inventory subgraph
type Product @key(fields: "id") {
  id: ID!
  name: String! @external
  inStock: Boolean!
}

type Query {
  outOfStockProducts: [Product!]! @provides(fields: "name")
  discontinuedProducts: [Product!]!
}
```

This example subgraph can resolve `Product.name` for products returned by `Query.outOfStockProducts` but not `Query.discontinuedProducts`.

If a subgraph `@provides` an entity field:

* The subgraph must define that field and mark it as [`@external`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#external), as shown above with `Product.name`.
* The entity field must be marked as either [`@shareable`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#shareable) or [`@external`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#external) in every subgraph that defines it.
* The entity field must be marked as [`@shareable`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#shareable) in at least one other subgraph (i.e., there's at least one subgraph that can always resolve the field).

Otherwise, a composition error occurs.

For more information, see [Using `@provides`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/resolve-another-subgraphs-fields#using-provides).

#### Arguments

Name /Type
Description

##### `fields`

`FieldSet!`

**Required.** A GraphQL selection set (provided as a string) of object fields and subfields that the subgraph can resolve only at this query path.

Examples:

* `"name"`
* `"name address"`
* `"... on Person { name address }"` (valid for fields that return a union or interface)

### `@requires`

```graphql
directive @requires(fields: FieldSet!) on FIELD_DEFINITION
```

Indicates that the resolver for a particular entity field depends on the values of other entity fields that are resolved by other subgraphs. This tells the router that it needs to fetch the values of those externally defined fields first, even if the original client query didn't request them.

```graphql title=Shipping subgraph
type Product @key(fields: "id") {
  id: ID!
  size: Int @external
  weight: Int @external
  shippingEstimate: String @requires(fields: "size weight")
}
```

The example subgraph above resolves a `Product` object's `shippingEstimate` field, but it requires the product's `size` and `weight` to do so. Because these two fields are resolved by a different subgraph, they're marked as [`@external`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#external).

If a subgraph `@requires` an entity field, the subgraph must define that field and mark it as [`@external`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#external), as shown above with `Product.size` and `Product.weight`. Otherwise, a composition error occurs.

See also [Contributing computed entity fields](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/contribute-fields#contributing-computed-entity-fields).

#### Arguments

Name /Type
Description

##### `fields`

`FieldSet!`

**Required.** A GraphQL selection set (provided as a string) of `@external` object fields and subfields that this field requires.

Examples:

* `"name"`
* `"name address"`
* `"name organization { id }"`

## Applying metadata

### `@tag`

```graphql
directive @tag(name: String!) repeatable on FIELD_DEFINITION | INTERFACE | OBJECT | UNION | ARGUMENT_DEFINITION | SCALAR | ENUM | ENUM_VALUE | INPUT_OBJECT | INPUT_FIELD_DEFINITION | SCHEMA
```

Applies arbitrary string metadata to a schema location. Custom tooling can use this metadata during any step of the schema delivery flow, including composition, static analysis, and documentation. The GraphOS Enterprise [contracts feature](https://www.apollographql.com/docs/graphos/platform/schema-management/delivery/contracts/overview) uses `@tag` with its inclusion and exclusion filters.

Unlike with most directives, composition preserves uses of this directive in the generated supergraph schema. To preserve uses of other directives, see [`@composeDirective`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#composedirective).

Consequently, if you [rename this directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/reference/directives.md#renaming-directives), you must use the same name in every subgraph that uses it. Otherwise, a composition error occurs due to a naming mismatch.

```graphql
extend schema
    @link(url: "https://specs.apollo.dev/federation/v2.3", import: ["@tag"])

type Query {
  customer(id: String!): Customer @tag(name: "team-customers")
  employee(id: String!): Employee @tag(name: "team-admin")
}

interface User @tag(name: "team-accounts") {
  id: String!
  name: String!
}

type Customer implements User @tag(name: "team-customers") {
  id: String!
  name: String!
}

type Employee implements User @tag(name: "team-admin") {
  id: String!
  name: String!
  ssn: String!
}
```

#### Arguments

Name /Type
Description

##### `name`

`String!`

**Required.** The tag name to apply.

## Managing custom directives

### `@composeDirective`

```graphql
directive @composeDirective(name: String!) repeatable on SCHEMA
```

Indicates to composition that all uses of a particular custom [type system directive](https://www.apollographql.com/docs/graphos/reference/federation/composition-rules/#type-system-directives) in the subgraph schema should be preserved in the supergraph schema (by default, composition omits most directives from the supergraph schema).

Do not use this directive with an [executable directive](https://www.apollographql.com/docs/graphos/reference/federation/composition-rules/#executable-directives). Executable directives have different rules for composition.

```graphql
extend schema
    @link(url: "https://specs.apollo.dev/link/v1.0")
    @link(url: "https://specs.apollo.dev/federation/v2.3", import: ["@composeDirective"])
    @link(url: "https://myspecs.dev/myDirective/v1.0", import: ["@myDirective", { name: "@anotherDirective", as: "@hello" }])
    # highlight-start
    @composeDirective(name: "@myDirective")
    @composeDirective(name: "@hello")

directive @myDirective(a: String!) on FIELD_DEFINITION
directive @hello on FIELD_DEFINITION
    # highlight-end
```

This directive has the following requirements:

* Ensure your [subgraph library](https://www.apollographql.com/docs/graphos/reference/federation/compatible-subgraphs) supports `@composeDirective` or try manually adding the `@composeDirective` definition to your subgraph schema.
* The directive to preserve must be defined and imported from a core specification via the `@link` directive.
* The specified directive `name` must match the name used for the directive in this subgraph.
  * If you use the `as` argument in your `@link` definition to modify the directive's name from its spec's default, provide the modified name, not the default name.
* If multiple subgraphs import and use the directive:
  * The name used for the directive must be identical in all of those subgraphs.
  * All of those subgraphs should use the same major version of the spec that defines the directive.

If any of these requirements is not met, composition fails.

If different subgraphs use different versions of a directive's corresponding spec, the supergraph schema uses whichever version number is highest among all subgraphs. Composition does not verify whether this version of the directive is compatible with subgraphs that use an earlier version.

#### Arguments

Name /Type
Description

##### `name`

`String!`

**Required.** The name (including the leading `@`) of the directive to preserve during composition.

## Saving and referencing data with contexts

### `@context`

The `@context` directive defines a named context from which a field of the annotated type can be passed to a receiver of the context. The receiver must be a field annotated with the `@fromContext` directive.

```graphql
directive @context(name: String!) on OBJECT | INTERFACE | UNION;
```

A `@context` directive must be applied to an object, interface, or union type. A type can be annotated with one or more `@context` directives.

Each `@context` must be defined with a name, and each `@context` name can be applied to multiple places within a subgraph. For example:

```graphql
type A @key(fields: "id") @context(name: "userContext") {
  id: ID!
  prop: String!
}

type B @key(fields: "id") @context(name: "userContext") {
  id: ID!
  prop: String!
}

type U @key(fields: "id") {
  id: ID!
  field (arg: String @fromContext(field: "$userContext { prop }")): String!
}
```

### `@fromContext`

The `@fromContext` directive sets the context from which to receive the value of the annotated field. The context must have been defined with the `@context` directive.

```graphql
scalar ContextFieldValue;

directive @fromContext(field: ContextFieldValue) on ARGUMENT_DEFINITION;
```

A `@fromContext` directive must be used as an argument on a field. Its field value—the `ContextFieldValue` scalar—must contain the name of a defined context and a selection of a field from the context's type.

The selection syntax for `@fromContext` used in its `ContextFieldValue` is similar to GraphQL field selection syntax, with some additional rules:

* The first element must be the name of a context defined by `@context` and prefixed with `$` (for example, `$myContext`). This is the only context that can be referenced by the annotated field.
* The `@skip` and `@include` directives must not be used.
* The second element must be a selection set that resolves to a single field.
* Top-level type conditions must not overlap with one another, so that the field can be resolved to a single value.
* All fields referenced in the `ContextFieldValue` must be expressed within the current subgraph. If the fields are referenced across multiple subgraphs, they must be annotated with [`@external`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/use-contexts#referencing-fields-across-subgraphs) .
* The argument must be nullable. Because validation is done at the subgraph level, the referenced field may become nullable when merging subgraphs, such as when the field is nullable in one subgraph but not in another.

When the same contextual value is set in multiple places, the `ContextFieldValue` must resolve all types from each place into a single value that matches the parameter type.

For examples using `@context` and `@fromContext`, see [Using contexts to share data along type hierarchies](https://www.apollographql.com/docs/federation/entities/use-contexts).

## Customizing demand controls

### `@cost`

Rate limits apply on the Free plan.

```graphql
directive @cost(weight: Int!) on ARGUMENT_DEFINITION | ENUM | FIELD_DEFINITION | INPUT_FIELD_DEFINITION | OBJECT | SCALAR
```

The `@cost` directive defines a custom weight for a schema location. For GraphOS Router, it customizes the operation cost calculation of the [demand control feature](https://www.apollographql.com/docs/router/executing-operations/demand-control/).

If `@cost` is not specified for a field, a default value is used:

* Scalars and enums have default cost of 0
* Composite input and output types have default cost of 1

Regardless of whether `@cost` is specified on a field, the field cost for that field also accounts for its arguments and selections.

#### Arguments

Name /Type
Description

##### `weight`

`Int!`

**Required.** Assigns a custom weight for scoring the current field.

### `@listSize`

Rate limits apply on the Free plan.

```graphql
directive @listSize(assumedSize: Int, slicingArguments: [String!], sizedFields: [String!], requireOneSlicingArgument: Boolean = true) on FIELD_DEFINITION
```

The `@listSize` directive is used to customize the cost calculation of the [demand control feature](https://www.apollographql.com/docs/router/executing-operations/demand-control/) of GraphOS Router.

In the static analysis phase, the cost calculator does not know how many entities will be returned by each list field in a given query. By providing an estimated list size for a field with `@listSize`, the cost calculator can produce a more accurate estimate of the cost during static analysis.

#### Configuring static list sizes

The simplest way to define a list size for a field is to use the `assumedSize` argument. This defines a static assumed maximum length for a given list field in the schema.

```graphql
type Query {
  items: [Item!] @listSize(assumedSize: 10)
}

type Item @key(fields: "id") {
  id: ID
}
```

In this case, all queries for `items` are expected to receive at most ten items in the list.

#### Configuring dynamic list sizes

When using paging parameters, the length of a list field can be determined by an input value. You can use the `slicingArguments` argument to tell the router to expect as many elements as the query requests.

```graphql
type Query {
  items(first: Int, last: Int): [Item!] @listSize(slicingArguments: ["first", "last"], requireOneSlicingArgument: false)
}
```

In this example, the `items` field can be requested with paging parameters. If the client sends a query with multiple slicing arguments, the scoring algorithm will use the maximum value of all specified slicing arguments. The following query is assumed to return ten items in the scoring algorithm.

```graphql
query MultipleSlicingArgumentsQuery {
  items(first: 5, last: 10)
}
```

In some cases, you may want to enforce that only one slicing argument is used. For example, you may want to ensure that clients request either the first *n* items or the last *n* items, but not both. You can do this by setting `requireOneSlicingArgument` to `true`.

```graphql
type Query {
  items(first: Int, last: Int): [Item!] @listSize(slicingArguments: ["first", "last"], requireOneSlicingArgument: true)
}
```

With this updated schema, sending the the above `MultipleSlicingArgumentsQuery` with its two slicing arguments to a graph would result in an error, as would sending a query with no slicing arguments.

#### Cursor support

Some pagination patterns include extra information along with the requested entities. For example, we may have some schema with a cursor type.

```graphql
type Query {
  items(first: Int): Cursor! @listSize(slicingArguments: ["first"], sizedFields: ["page"])
}

type Cursor {
  page: [Item!]
  nextPageToken: String
}

type Item @key(fields: "id") {
  id: ID
}
```

This application of `@listSize` indicates that the length of the `page` field inside `Cursor` is determined by the `first` argument.

#### Arguments

Name /Type
Description

##### `assumedSize`

`Int`

Indicates that the annotated list field will return at most this many items.

##### `slicingArguments`

`[String!]`

Indicates that the annotated list field returns as many items as are requested by a paging argument. If multiple arguments are passed, the maximum value of the arguments is used.

If both this and `assumedSize` are specified, the value from `slicingArguments` will take precedence.

##### `sizedFields`

`[String!]`

Supports cursor objects by indicating that the expected list size should be applied to fields within the returned object.

##### `requireOneSlicingArgument`

`Boolean`

If `true`, indicates that queries must supply exactly one argument from `slicingArguments`.

If `slicingArguments` are not specified, this value is ignored.

The default value is `true`.

## Managing cache invalidation

### `@cacheTag`

```graphql
directive @cacheTag(format: String!) repeatable on FIELD_DEFINITION | OBJECT
```

Assigns cache tags to cached data in the Apollo Router for [active cache invalidation](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/invalidation#active-invalidation). Use cache tags to remove specific cached entries on demand when data changes, instead of waiting for time-to-live (TTL) expiration.

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.12",
        import: ["@key", "@cacheTag"])

type Query {
  users: [User!]! @cacheTag(format: "users-list")
  user(id: ID!): User @cacheTag(format: "user-{$args.id}")
}

type User @key(fields: "id") @cacheTag(format: "user-{$key.id}") {
  id: ID!
  name: String!
}
```

#### Arguments

Name /Type
Description

##### `format`

`String!`

**Required.** A string template that defines the cache tag. Can include interpolated variables:

* For root fields: `{$args.fieldName}` to interpolate field arguments
* For entities: `{$key.fieldName}` to interpolate entity key fields

Interpolated variables must be either a scalar or enum type.

For details on applying cache invalidation with cache tags, see [Response cache invalidation](https://www.apollographql.com/docs/graphos/routing/performance/caching/response-caching/invalidation#by-cache-tag).

## Connectors

Directives for Connectors like `@connect` and `@source` are documented in [Connector Directives Reference](https://www.apollographql.com/docs/graphos/schema-design/connectors/directives).
