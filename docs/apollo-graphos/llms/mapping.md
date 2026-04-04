# Source: https://www.apollographql.com/docs/graphos/connectors/mapping.md

# Mapping Language Overview

This overview describes the Apollo Connectors *mapping language*.
You use the mapping language anywhere data needs to be transformed from one form to another.
This includes building URIs and headers when making requests, constructing request bodies, and mapping response data to GraphQL schema.

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.
If you learn best with videos and exercises, this [interactive course](https://www.apollographql.com/tutorials/connectors-mapping-and-transforms) teaches the syntax and methods of the Connectors mapping language.

## The basics

The mapping language uses a declarative approach to transforming data from one shape to another.
Unlike traditional programming languages, it doesn't have state or loops.
Since the mapping language borrows heavily from the GraphQL query language, some concepts like the alias syntax and array handling might look familiar.

## Fields and paths

The most basic mapping expression selects a value from a path.
For example, a URI path might include the expression `$args.id`.
This expression means, "Use the `id` field of the `$args` variable."
For example:

```graphql title=Example of $args.id in a URI path
type Query {
  product(id: ID!): Product
    @connect(
      source: "ecomm"
      http: { GET: "/products/{$args.id}" }
      selection: "id name description"
    )
}
```

When applied to an array, the result of a path is also an array.
For example, if `$args.filters` is an array of objects, `$args.filters.value` is an array of the `value` property of each object.

```json title=$args
{
  "filters": [
    { "value": 1 },
    { "value": 2 },
    { "value": 3 }
  ]
}
```

```json title=Result of $args.filters.value
[1, 2, 3]
```

## Creating objects

For this section, assume that `$args` contains this JSON object:

```json title=$args
{ "handle": "alice", "email": "alice@example.com" }
```

When you give a value a name, you create an object *containing* that value:

```connectors title=Expression
username: $args.handle
```

```json title=Result
{ "username": "alice" }
```

You can combine multiple fields to create an object with multiple properties:

```connectors title=Expression
username: $args.handle
email: $args.email

```

```json title=Result
{
  "username": "alice",
  "email": "alice@example.com"
}
```

### Nested objects

You can create a new object as the property of another object using curly braces (`{}`):

```connectors title=Expression
user: {
  username: $args.handle
  email: $args.email
}
```

```json title=Result
{
  "user": {
    "username": "alice",
    "email": "alice@example.com"
  }
}
```

### Subselections

If multiple properties from an object come from another object, you can use a *subselection* to avoid repeating the object name. The `$` variable in the curly braces refers to the selected object—whatever comes directly before the `{`. In the following example, that's `$args`.

```connectors title=Expression
$args {
  username: $.handle
  email: $.email
}
```

```json title=Result
{
  "username": "alice",
  "email": "alice@example.com"
}
```

As shorthand, you can omit `$.` and refer to the fields only by their names:

```connectors title=Expression
$args {
  username: $.handle
  email: $.email
}
```

```connectors title=Equivalent expression
$args {
  username: handle
  email: email
}
```

When the name of the new field matches the name of the source, you can also omit the left-hand side:

```connectors title=Expression
$args {
  username: handle
  email: email
}
```

```connectors title=Equivalent expression
$args {
  username: handle
  email
}
```

You can combine this with the ability to create nested objects by adding back in the `user:` field name:

```connectors title=Expression
user: $args {
  username: handle
  email
}
```

```json title=Result
{
  "user": {
    "username": "alice",
    "email": "alice@example.com"
  }
}
```

### Multiple levels

For more complex inputs, you can use multiple subselections to achieve the desired result without repetition. Suppose `$args` looks like this:

```json title=$args
{
  "user": {
    "handle": "alice",
    "email": "alice@example.com"
  },
  "company": {
    "name": "Acme",
    "address": "123 Main St"
  }
}
```

You can select all the data like this:

```connectors title=Expression
$args {
  user {
    username: handle
    email
  }
  organization: company {
    name
    address
  }
}
```

```json title=Result
{
  "user": {
    "username": "alice",
    "email": "alice@example.com"
  },
  "organization": {
    "name": "Acme",
    "address": "123 Main St"
  }
}
```

Because the `user` property being creating comes from the parent's property of the same name, you can use the shorthand
syntax when creating the object.

### Special case for selection

For the `@connect` directive's `selection` argument only, a top-level `$` refers to the root of the response body from the source API.
This means you can select basic GraphQL fields succinctly.

For example, given this JSON response:

```json title=JSON Response
{
  "id": "1",
  "username": "alice",
  "email": "alice@example.com"
}
```

You can use this basic `selection` to select all of a user's fields.

```graphql title=Example selection
type Query {
  user(id: ID!): User
    @connect(
      http: { GET: "https://api.example.com/users/{$args.id}" }
      selection: "id username email"
    )
}

type User {
  id: ID!
  username: String!
  email: String!
}
```

Since the REST endpoint returns `username` and `email` in its
response, you can map them directly to fields of the same name in the GraphQL schema using the [shorthand that omits the `$`](https://www.apollographql.com/docs/graphos/connectors/mapping.md#subselections).

## Additional resources

* See additional pages for [variables](https://www.apollographql.com/docs/graphos/connectors/variables), [methods](https://www.apollographql.com/docs/graphos/connectors/methods), and common mapping patterns like [arrays](https://www.apollographql.com/docs/graphos/connectors/mapping/arrays), [enums](https://www.apollographql.com/docs/graphos/connectors/mapping/enums), and [literal values](https://www.apollographql.com/docs/graphos/connectors/mapping/literals).
* Refer to the guide on [Mapping Response Fields](https://www.apollographql.com/docs/graphos/connectors/responses/fields) for examples of common selection mappings.
