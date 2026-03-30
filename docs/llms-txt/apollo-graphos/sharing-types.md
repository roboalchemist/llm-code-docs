# Source: https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types.md

# Value Types in Apollo Federation

In a federated graph, it's common to want to reuse a GraphQL type across multiple subgraphs.

For example, suppose you want to define and reuse a generic `Position` type in different subgraphs:

```graphql
type Position {
  x: Int!
  y: Int!
}
```

Types like this are called *value types*. This article describes how to share value types and their fields in federated graph, enabling multiple subgraphs to define and resolve them.

## Sharing object types

By default, in Federation 2 subgraphs, a single object field can't be defined or resolved by more than one subgraph schema.

Consider the following `Position` example:

❌

```graphql title=Subgraph A
type Position {
  x: Int!
  y: Int!
}
```

```graphql title=Subgraph B
type Position {
  x: Int!
  y: Int!
}
```

Attempting to compose these two subgraph schemas together will [break composition](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition/#breaking-composition). The router doesn't know which subgraph is responsible for resolving `Position.x` and `Position.y`. To enable multiple subgraphs to resolve these fields, you must first mark that field as [`@shareable`](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types.md#using-shareable).

As an alternative, if you want Subgraphs A and B to resolve different fields of `Position`, you can designate the `Position` type as an [entity](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro).

### Using `@shareable`

The `@shareable` directive enables multiple subgraphs to resolve a particular object field (or set of object fields).

To use `@shareable` in a subgraph schema, you first need to add the following snippet to that schema to [opt in to Federation 2](https://www.apollographql.com/docs/graphos/reference/migration/to-federation-version-2/#opt-in-to-federation-2):

```graphql
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3",
        import: ["@key", "@shareable"])
```

Then you can apply the `@shareable` directive to an object type, or to individual fields of that type:

✅

```graphql title=Subgraph A
type Position @shareable {
  x: Int!
  y: Int!
}
```

```graphql title=Subgraph B
type Position {
  x: Int! @shareable
  y: Int! @shareable
}
```

Marking a type as `@shareable` is equivalent to marking all of its fields as `@shareable`, so the two subgraph definitions above are equivalent.

Both subgraphs A and B can now resolve the `x` and `y` fields for the `Position` type, and our subgraph schemas will successfully compose into a supergraph schema.

#### ⚠️ Important considerations for `@shareable`

* If a type or field is marked `@shareable` in any subgraph, it must be marked either `@shareable` or [`@external`](https://www.apollographql.com/docs/graphos/reference/federation/directives/#external) in every subgraph that defines it. Otherwise, composition fails.
* If multiple subgraphs can resolve a field, make sure each subgraph's resolver for that field behaves identically. Otherwise, queries might return inconsistent results depending on which subgraph resolves the field.

#### Using `@shareable` with `extend`

If you apply `@shareable` to an object type declaration, it only applies to the fields within that exact declaration. It does not apply to other declarations for that same type:

```graphql title=Subgraph A
type Position @shareable {
  x: Int! # shareable
  y: Int! # shareable
}

extend type Position {
  # highlight-start
  z: Int! # ⚠️ NOT shareable!
  # highlight-end
}
```

Using the `extend` keyword, the schema above includes two different declarations for `Position`. Because only the first declaration is marked `@shareable`, `Position.z` is not considered shareable.

To make `Position.z` shareable, you can do one of the following:

* Mark the individual field `z` with `@shareable`.

  ```graphql
  extend type Position {
    # highlight-start
    z: Int! @shareable
    # highlight-end
  }
  ```

* Mark the entire `extend` declaration with `@shareable`.

  * This strategy requires targeting v2.2 or later of the Apollo Federation specification in your subgraph schema. Earlier versions do not support applying `@shareable` to the same object type multiple times.

  ```graphql
  extend schema
    @link(url: "https://specs.apollo.dev/federation/v2.3", import: ["@shareable"]) #highlight-line

  extend type Position @shareable { #highlight-line
    z: Int!
  }
  ```

## Differing shared fields

Shared fields can only differ in their [return types](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types.md#return-types) and [arguments](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types.md#arguments) in specific ways.
If fields you want to share between subgraphs differ more than is permitted, use  [entities](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/intro) instead of shareable value types.

### Return types

Let's say two subgraphs both define an `Event` object type with a `timestamp` field:

❌

```graphql title=Subgraph A
type Event @shareable {
  timestamp: Int!
}
```

```graphql title=Subgraph B
type Event @shareable {
  timestamp: String!
}
```

Subgraph A's `timestamp` returns an `Int`, and Subgraph B's returns a `String`. This is invalid. When composition attempts to generate an `Event` type for the supergraph schema, it fails due to an unresolvable conflict between the two `timestamp` field definitions.

Next, look at these varying definitions for the `Position` object type:

✅

```graphql title=Subgraph A
type Position @shareable {
  x: Int!
  y: Int!
}
```

```graphql title=Subgraph B
type Position @shareable {
  x: Int
  y: Int
}
```

The `x` and `y` fields are non-nullable in Subgraph A, but they're nullable in Subgraph B. This is valid. Composition recognizes that it can use the following definition for `Position` in the supergraph schema:

```graphql title=Supergraph schema
type Position {
  x: Int
  y: Int
}
```

This definition works for querying Subgraph A, because Subgraph A's definition is more restrictive than this (a non-nullable value is always valid for a nullable field). In this case, composition coerces Subgraph A's `Position` fields to satisfy the reduced restrictiveness of Subgraph B.

Subgraph A's actual subgraph schema is not modified. Within Subgraph A, `x` and `y` remain non-nullable.

### Arguments

Arguments for a shared field can differ between subgraphs in certain ways:

* If an argument is required in at least one subgraph, it can be optional in other subgraphs. It cannot be omitted.
* If an argument is optional in every subgraph where it's defined, it is technically valid to omit it in other subgraphs. However:
  * ⚠️ If a field argument is omitted from any subgraph, that argument is omitted from the supergraph schema entirely. This means that clients can't provide the argument for that field.

✅

```graphql title=Subgraph A
type Building @shareable {
  # Argument is required
  height(units: String!): Int!
}
```

```graphql title=Subgraph B
type Building @shareable {
  # Argument can be optional
  height(units: String): Int!
}
```

❌

```graphql title=Subgraph A
type Building @shareable {
  # Argument is required
  height(units: String!): Int!
}
```

```graphql title=Subgraph B
type Building @shareable {
  # ⚠️ Argument can't be omitted! ⚠️
  height: Int!
}
```

⚠️

```graphql title=Subgraph A
type Building @shareable {
  # Argument is optional
  height(units: String): Int!
}
```

```graphql title=Subgraph B
type Building @shareable {
  # Argument can be omitted, BUT
  # it doesn't appear in the
  # supergraph schema!
  height: Int!
}
```

For more information, see [Input types and field arguments](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition#input-types-and-field-arguments).

### Omitting fields

Look at these two definitions of a `Position` object type:

⚠️

```graphql title=Subgraph A
type Position @shareable {
  x: Int!
  y: Int!
}
```

```graphql title=Subgraph B
type Position @shareable {
  x: Int!
  y: Int!
  z: Int!
}
```

Subgraph B defines a `z` field, but Subgraph A doesn't. In this case, when composition generates the `Position` type for the supergraph schema, it includes all three fields:

```graphql title=Supergraph schema
type Position {
  x: Int!
  y: Int!
  z: Int!
}
```

This definition works for Subgraph B, but it presents a problem for Subgraph A. Let's say Subgraph A defines the following `Query` type:

```graphql title=Subgraph A
type Query {
  currentPosition: Position!
}
```

According to the hypothetical supergraph schema, the following query is valid against the supergraph:

❌

```graphql
query GetCurrentPosition {
  currentPosition {
    x
    y
    z # ⚠️ Unresolvable! ⚠️
  }
}
```

And here's the problem: if Subgraph B doesn't define `Query.currentPosition`, this query must be executed on Subgraph A. But Subgraph A is missing the `Position.z` field, so that field is unresolvable!

Composition recognizes this potential problem, and it fails with an error. To learn how to fix it, check out [Solutions for unresolvable fields](https://www.apollographql.com/docs/graphos/reference/federation/composition-rules#solutions-for-unresolvable-fields).

## Adding new shared fields

Adding a new field to a value type can cause composition issues, because it's challenging to add the field to all defining subgraphs at the same time.

Let's say we're adding a `z` field to our `Position` value type, and we start with Subgraph A:

⚠️

```graphql title=Subgraph A
type Position @shareable {
  x: Int!
  y: Int!
  z: Int!
}
```

```graphql title=Subgraph B
type Position @shareable {
  x: Int!
  y: Int!
}
```

It's likely that when we attempt to compose these two schemas, composition will fail, because Subgraph B can't resolve `Position.z`.

To incrementally add the field to all of our subgraphs without breaking composition, we can use the [`@inaccessible` directive](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types.md#using-inaccessible).

### Using `@inaccessible`

If you apply the `@inaccessible` directive to a field, composition omits that field from your router's API schema. This helps you incrementally add a field to multiple subgraphs without breaking composition.

To use `@inaccessible` in a subgraph, first make sure you include it in the `import` array of your Federation 2 opt-in declaration:

```graphql title=Subgraph A
extend schema
  @link(url: "https://specs.apollo.dev/federation/v2.3",
        import: ["@key", "@shareable", "@inaccessible"])
```

Then, whenever you add a new field to a value type, apply `@inaccessible` to that field if it isn't yet present in every subgraph that defines the value type:

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
}
```

Even if `Position.z` is defined in multiple subgraphs, you only need to apply `@inaccessible` in one subgraph to omit it. In fact, you might want to apply it in only one subgraph to simplify removing it later.

With the syntax above, composition omits `Position.z` from the generated API schema, and the resulting `Position` type includes only `x` and `y` fields.

Notice that `Position.z` does appear in the supergraph schema, but the API schema enforces which fields clients can include in operations. [Learn more about federated schemas.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/schema-types)

Whenever you're ready, you can now add `Position.z` to Subgraph B:

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
  z: Int!
}
```

At this point, `Position.z` is still `@inaccessible`, so composition continues to ignore it.

Finally, when you've added `Position.z` to every subgraph that defines `Position`, you can remove `@inaccessible` from Subgraph A:

```graphql title=Subgraph A
type Position @shareable {
  x: Int!
  y: Int!
  z: Int!
}
```

```graphql title=Subgraph B
type Position @shareable {
  x: Int!
  y: Int!
  z: Int!
}
```

Composition now successfully includes `Position.z` in the supergraph schema!

## Unions and interfaces

In Federation 2, `union` and `interface` type definitions can be shared between subgraphs by default, and those definitions can differ:

```graphql title=Subgraph A
union Media = Book | Movie

interface User {
  name: String!
}
```

```graphql title=Subgraph B
union Media = Book | Podcast

interface User {
  name: String!
  age: Int!
}
```

[Compositional logic](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition#merging-types-from-multiple-subgraphs) merges these definitions in your supergraph schema:

```graphql title=Supergraph schema
union Media = Book | Movie | Podcast

# The object types that implement this interface are
# responsible for resolving these fields.
interface User {
  name: String!
  age: Int!
}
```

This can be useful when different subgraphs are responsible for different subsets of a particular set of related types or values.

You can also use the `enum` type across multiple subgraphs. For details, see [Merging types from multiple subgraphs](https://www.apollographql.com/docs/graphos/reference/federation/composition-rules#merging-types-from-multiple-subgraphs).

### Challenges with shared interfaces

Sharing an interface type across subgraphs introduces maintenance challenges whenever that interface changes. Consider these subgraphs:

```graphql title=Subgraph A
interface Media {
  id: ID!
  title: String!
}

type Book implements Media {
  id: ID!
  title: String!
}
```

```graphql title=Subgraph B
interface Media {
  id: ID!
  title: String!
}

type Podcast implements Media {
  id: ID!
  title: String!
}
```

Now, let's say Subgraph B adds a `creator` field to the `Media` interface:

❌

```graphql title=Subgraph A
interface Media {
  id: ID!
  title: String!
}

type Book implements Media {
  id: ID!
  title: String!
  # ❌ Doesn't define creator!
}
```

```graphql title=Subgraph B
interface Media {
  id: ID!
  title: String!
  creator: String! #highlight-line
}

type Podcast implements Media {
  id: ID!
  title: String!
  creator: String! #highlight-line
}
```

This breaks composition, because `Book` also implements `Media` but doesn't define the new `creator` field.

To prevent this error, all implementing types across all subgraphs need to be updated to include all fields of `Media`. This becomes more and more challenging to do as your number of subgraphs and teams grows. Fortunately, there's a [solution](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/sharing-types.md#solution-entity-interfaces).

#### Solution: Entity interfaces

Apollo Federation 2.3 introduces a powerful abstraction mechanism for interfaces, enabling you to add interface fields across subgraphs without needing to update every single implementing type.

[Learn more about entity interfaces.](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/entities/interfaces/)

## Input types

Subgraphs can share `input` type definitions, but composition merges their fields using an intersection strategy. When `input` types are composed across multiple subgraphs, only mutual fields are preserved in the supergraph schema:

```graphql title=Subgraph A
input UserInput {
  name: String!
  age: Int # Not in Subgraph B
}
```

```graphql title=Subgraph B
input UserInput {
  name: String!
  email: String # Not in Subgraph A
}
```

Compositional logic merges only the fields that all `input` types have in common. To learn more, see [Merging input types and field arguments](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition#input-types-and-field-arguments).

```graphql title=Supergraph schema
input UserInput {
  name: String!
}
```

To learn more about how composition merges different schema types under the hood, see [Merging types during composition](https://www.apollographql.com/docs/graphos/schema-design/federated-schemas/composition#merging-types-from-multiple-subgraphs).
