# Source: https://grafbase.com/docs/federation/graphql-directives.md

# GraphQL Federation Directives

Composition works without intervention when independent subgraphs don't share types and fields. Composition does more than schema stitching: federation directives enable each subgraph to specify what it resolves and how it connects with other subgraphs in the federated graph. This lets the router expose a consistent whole that spans across subgraphs while requiring minimal coordination between teams.

## @authenticated

The Grafbase Gateway has deprecated embedded support for this directive. Please use the [Authenticated](/extensions/authenticated) extension instead.

```graphql
directive @authenticated on FIELD_DEFINITION | OBJECT | INTERFACE | SCALAR | ENUM
```

Restrict access to the annotated item to successfully authenticated users. For more granularity, use [@requiresScopes](#requiresscopes).

## @composeDirective

```graphql
directive @composeDirective(name: String!) repeatable on SCHEMA
```

By default, composition only passes some built-in (`@deprecated`) and federation directives (like `@inaccessible`) from subgraphs into the federated schema.

Use the `@composeDirective` directive to tell composition to keep instances of a specific directive in the final API schema of the Federated Graph.

## @external

```graphql
directive @external on FIELD_DEFINITION | OBJECT
```

When used on a field, `@external` indicates that the subgraph can't resolve the field even though it exists in the subgraph's schema. Use this directive only in combination with `@provides` and `@requires`.

When you apply `@external` to an object, it has the same effect as applying `@external` to each field in that object.

## @inaccessible

```graphql
directive @inaccessible on FIELD_DEFINITION | INTERFACE | OBJECT | UNION | ARGUMENT_DEFINITION | SCALAR | ENUM | ENUM_VALUE | INPUT_OBJECT | INPUT_FIELD_DEFINITION
```

The `@inaccessible` directive excludes marked schema elements from the composed API schema that the gateway exposes. When you mark an item as `@inaccessible` in any subgraph, the composition excludes it from the composed API, even when the same item appears without `@inaccessible` in other subgraphs.

### Example 1: Hiding Information

```graphql
type PersonalDetails @inaccessible {
  age: Int
  heightCm: Int
  birday: Date
}

type User @key(fields: "id") @key(fields: "socialSecurityNumber") {
  id: ID!
  # socialSecurityNumber is a key to enable fetching users by
  # social security number, but we do not want the field to be
  # queryable.
  socialSecurityNumber: String! @inaccessible

  # This field must be marked as inaccessible because the field
  # type is inaccessible.
  details: PersonalDetails @inaccessible
}
```

### Example 2: Adding Fields to a Shareable Type

Let's say you share an RGB color type across multiple subgraphs. Because the type uses `@shareable`, all subgraphs must return all fields. When you add a new field to the type, start by adding it to one subgraph and publishing.

This causes a composition error because only one subgraph contains the new field. You might choose to publish updates to all subgraphs quickly, though your federated graph won't compose during the interim.

While this works, it doesn't scale well with many subgraphs across different teams. Instead, use `@inaccessible` for a better solution. Publish your first subgraph with the new field like this:

```graphql
type Color @shareable {
  red: Int!
  green: Int!
  blue: Int!
  opacity: Int! @inaccessible
}
```

The inaccessible `opacity` field won't trigger composition errors when other subgraphs don't define it. Add the field to other subgraphs one at a time. After all subgraphs include the field, remove `@inaccessible`. All intermediate states will compose cleanly.

## @interfaceObject

```graphql
directive @interfaceObject on OBJECT
```

Federation supports entity interfaces, which follow the same model as regular entities but have different definition requirements and interface-specific behaviors.

An interface entity must include:

- An interface with a key in one subgraph.
- A regular object entity using the `@interfaceObject` directive in other subgraphs.

Objects that implement an entity interface automatically receive fields that other subgraphs contribute to that entity. This matches how objects normally implement regular interfaces.

## @key

```graphql
directive @key(
  fields: FieldSet!
  resolvable: Boolean = true
) repeatable on OBJECT | INTERFACE
```

The `@key` directive defines entities in your schema. An entity is a type that includes a key and appears in multiple subgraphs. It acts as the main mechanism to connect subgraphs in Federation, similar to a primary key.

When you create an entity type with the `@key` directive, your [Federation compatible GraphQL framework of choice](https://www.apollographql.com/docs/federation/building-supergraphs/supported-subgraphs) requires you to define an _entity resolver_ for that type. This resolver works with the Federation-specific `Query._entities` field to fetch

**Arguments**:

- `fields`: A string that contains the GraphQL selection set for key fields. You can nest the selection (for example, `@key(fields: "a { b } c d")`), but field arguments aren't valid (for example, don't use `@key(fields: "id(type: UUID) { bytes }")`).
- `resolvable`: Set this value to false to show that a subgraph references an entity (often by returning its key) but can't resolve it through `Query._entities`. This means the subgraph doesn't have an entity resolver for that entity. Use this when a subgraph includes an entity key (like `author_id` on a blog post) but doesn't contribute fields to the entity.

### Example

This example uses a fictitious e-commerce website to show how entities work. Define the `inventory` subgraph first:

```graphql
type Product @key(fields: "id") @key(fields: "sku") {
  id: ID!
  itemsInStock: Int!
  sku: String!
}
```

The second `@key` means the `inventory` subgraph resolves a `Product` by using its SKU.

Then a `reviews` subgraph for product reviews:

```graphql
type Product @key(fields: "id") {
  id: ID!
  reviews: [Review!]
}
```

The final `search` subgraph finds products based on a user's search query:

```graphql
type Query {
  findProducts(searchQuery: String!): [Product!]
}

type Product @key(fields: "id") {
  id: ID!
}
```

The federated graph's API looks like this after composition:

```graphql
type Query {
  findProducts(searchQuery: String!): [Product!]
}

type Product {
  id: ID!
  reviews: [Review!]
  itemsInStock: Int!
  sku: String!
}
```

API clients see one `Product` type. Subgraphs contribute fields without requiring coordination.

## @override

```graphql
directive @override(from: String!, label: String) on FIELD_DEFINITION
```

Use the `@override` directive to migrate a field from one subgraph to another. To migrate a field to a new subgraph, first define it in the new subgraph. The rules of composition don't allow defining the same field in two subgraphs. If you define the field as `@shareable`, all subgraphs must resolve it, not just the source and destination. Marking the new field as `@inaccessible` doesn't help because you still can't switch the field between subgraphs without coordination and downtime.

The `@override` directive solves this problem. When you add `@override(from: "other-subgraph")` to a field, the gateway routes requests for that field to the subgraph with the override and ignores the field in `other-subgraph`. Teams can deploy changes independently using this workflow (each bullet point represents a `publish`):

- Deploy the new field with `@override` in the overriding subgraph. If the field doesn't work correctly in the new subgraph, reverse the change and the gateway will resume resolving the field in the original subgraph.
- Remove the old field from the overridden subgraph.
- Remove the `@override` directive from the overriding subgraph.

**Arguments**:

- `from`: Specify the name of the subgraph that contains the field you want to override. Composition doesn't validate this name to support this workflow: 1. Define the overriding field with `@override`, 2. Deploy, 3. Remove the overridden field, 4. Remove the `@override` on the new field. This avoids breaking the migration at step 3 when subgraphs publish independently.
- `label`: Controls partial or progressive overriding. Set the `label` argument to a string formatted as "percent(n)" where n is an integer from 0-100. This percentage determines how much traffic the gateway routes to the overriding subgraph. For example, `@override(from: "inventory", label: "percent(0)")` routes no traffic to the new subgraph, while `@override(from: "inventory", label: "percent(100)")` behaves the same as `@override(from: "inventory")` without the `label` argument.

### Example

Split the comments handling from your blog engine monolith into a dedicated service with its own subgraph. The monolith defines the `Post` type like this:

```graphql
type Post @key(fields: "id") {
  id: ID!
  title: String
  comments: [Comment!]
  publishedAt: DateTime
  author: User
}
```

To migrate the `Post.comments` field to the new comments service, add the following to the comments subgraph's schema:

```graphql
type Post @key(fields: "id") {
  id: ID!
  comments: [Comment!] @override(from: "monolith")
}
```

After you deploy this addition, the gateway routes all traffic for `Post.comments` to the comments subgraph.

## @provides

```graphql
directive @provides(fields: FieldSet!) on FIELD_DEFINITION
```

The `@provides` directive on a field tells the gateway that when resolving this field, the same subgraph can also resolve a set of other fields on that object to optimize performance.

You must annotate these other fields with `@external`, since the subgraph can only resolve them when resolving the field with `@provides`. Think of this directive as a more restricted version of `@shareable`.

While shareable fields allow resolution at any time, fields marked with `@external` and provided with `@provides` only allow resolution when resolving their providing field.

### Example

The following shows a `Farm` subgraph:

```graphql {5}
type Farm @key(fields: "id") {
  id: ID!
  name: String!
  location: String
  vegetables: [Vegetable] @provides(fields: "name")
}

type Vegetable @key(fields: "id") {
  id: ID!
  name: String! @external
}

extend type Query {
  farm(id: ID!): Farm
  vegetablesInSeason(date: Date!): [Vegetable!]
}
```

Here's the `Vegetable` subgraph:

```graphql
type Vegetable @key(fields: "id") {
  id: ID!
  name: String!
  scientificName: String!
  nutritionInfo: NutritionInfo
  marketPriceEur: Int
}
```

Consider these two queries that demonstrate how `@provides` works.

```graphql
query {
  farm(id: "6058691a-2d0a-47f1-95b3-1632f9ad16f9") {
    id
    name
  }
}
```

The `Query.farm` field provides `name`, so the `Farm` subgraph can resolve the whole query without contacting other subgraphs. However, in this second query:

```graphql
query {
  vegetablesInSeason(date: "2023-10-03") {
    id
    name
  }
}
```

The gateway must fetch the vegetable name from the `Vegetables` subgraph. API consumers see one unified Vegetable type that includes all fields defined across all subgraphs.

## @requires

```graphql
directive @requires(fields: FieldSet!) on FIELD_DEFINITION
```

The `@requires` directive specifies when a field needs other fields from the parent type that other subgraphs can resolve. Here's an example: Consider a hotel booking subgraph that manages room service. This subgraph determines available room service based on a hotel's location and category, but doesn't store hotel information directly in its database.

### Example

The Hotels subgraph:

```graphql
type Hotel @key(fields: "id") {
  id: ID!
  category: Int
  countryCode: String
}
```

The RoomService subgraph:

```graphql
type Hotel @key(fields: "id") {
  id: ID!
  category: Int @external
  countryCode: String @external
  roomServiceOffering: [String!]! @requires(fields: "category countryCode")
}
```

In this last snippet, the RoomService subgraph resolves `Hotel.roomServiceOffering` but requires the `category` and `countryCode` fields from another subgraph. The `@requires` directive indicates dependencies on `category` and `countryCode` fields, while `@external` shows the subgraph can't resolve them directly. You must define the required fields on the type and annotate them with `@external`.

When resolving a query that selects `Hotel.roomServiceOffering`, the gateway queries the Hotels subgraph first before passing data to the RoomService subgraph to resolve `roomServiceOffering` for that hotel. The gateway passes the retrieved fields to the entity resolver (`Query._entities`) on the RoomService subgraph.

Other subgraphs can resolve fields marked with `@external`. Zero subgraphs make the field with `@requires` impossible to query, one subgraph works for regular entity fields, and multiple subgraphs work with `@shareable` fields.

Use `@requires` only on entity fields and always combine it with [`@external`](#external).

## @requiresScopes

The Grafbase Gateway has deprecated embedded support for this directive. Please use the [Requires Scopes](/extensions/requires-scopes) extension instead.

```graphql
directive @requiresScopes(
  scopes: [[String!]!]!
) on FIELD_DEFINITION | OBJECT | INTERFACE | SCALAR | ENUM
```

Users must have a matching `scope` claim in their JWT access token to access the annotated item. Format the `scope` claim as a space-separated string of scope names.

The directive's `scopes` argument contains an array of arrays that defines combinations of scopes. Each inner array specifies a set of required scopes (AND logic). The outer array lists alternative scope combinations that can grant access (OR logic). You can list scopes in any order.

### Example

Let's restrict blog post view count access to users with both `editor` and `analytics` scopes, or users with admin scope:

```graphql {5,5}
type BlogPost {
  id: ID!
  title: String!
  author: User
  viewCount: Int @requiresScopes(scopes: [["admin"], ["editor", "analytics"]])
  content: String
}
```

## @shareable

```graphql
directive @shareable on FIELD_DEFINITION | OBJECT
```

Use this directive to share a type or field between subgraphs. In contrast to entities that use `@key`, all subgraphs must resolve shareable types and fields. A Color type demonstrates this pattern:

```graphql
type Color @shareable {
  red: Int!
  green: Int!
  blue: Int!
}
```

Each subgraph that returns a `Color` must provide all fields. Think of shareable types as value types that provide complete data.

When you annotate a type like `Color` with `@shareable`, it affects all fields of that type as if you added `@shareable` to each field individually.