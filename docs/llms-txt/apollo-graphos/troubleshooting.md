# Source: https://www.apollographql.com/docs/kotlin/caching/troubleshooting.md

# Source: https://www.apollographql.com/docs/graphos/connectors/troubleshooting.md

# Troubleshooting Connectors

Check out the [Connectors Mapping Playground](https://www.apollographql.com/docs/graphos/connectors/tooling/mapping-playground) to experiment with and troubleshoot mapping expressions.

## Debugging

If you haven't already, [set up IDE support](https://www.apollographql.com/docs/graphos/connectors/tooling/ide-extensions) for Apollo Connectors. These plugins enable syntax highlighting, validation, autocomplete, and more.

### Return debug information in GraphQL responses

To diagnose issues with your Connectors, you can return debugging information as part of each GraphQL response, including the details of each HTTP request and response from your Connectors.

Because this feature can leak sensitive information, enable it only for local
development environments.

First, run your router in development mode. This happens automatically when using `rover dev`. If you're running a router manually, you can pass it the `--dev` CLI argument.

[Your local Apollo Sandbox](https://www.apollographql.com/docs/apollo-sandbox) presents request, response, and mapping information in the right panel after you execute an operation.

GraphOS Studio Explorer, the version of Sandbox accessible from GraphOS Studio, doesn't return debugging information about Connectors.

### Adding debug information to telemetry

You can also add information about each Connector request and response to your [router telemetry](https://www.apollographql.com/docs/graphos/connectors/observability/telemetry). For example, the following router config will emit an event at the INFO level containing the details of each request and response. This event will contain the HTTP body and headers of each request and response, as well as the status code of each response:

```yaml
telemetry:
  instrumentation:
    events:
      connector:
        request: info
        response: info
```

Enabling Connector events may impact router performance.

Additionally, you can add information about any [mapping](https://www.apollographql.com/docs/graphos/connectors/mapping) problems to your router telemetry using selectors. For example, to emit an error event whenever there is one or more mapping problems, use the following router config:

```yaml
telemetry:
  instrumentation:
    events:
      connector:
        request.mapping.problems:
          message: "[Request Mapping Problems]"
          level: error
          on: request
          condition:
            gt:
              - connector_response_mapping_problems: count
              - 0
          attributes:
            request_mapping_problems:
              connector_request_mapping_problems: problems
        response.mapping.problems:
          message: "[Response Mapping Problems]"
          level: error
          on: response
          condition:
            gt:
              - connector_response_mapping_problems: count
              - 0
          attributes:
            response_mapping_problems:
              connector_response_mapping_problems: problems
```

The above events will be sent to the telemetry exporters you have configured in the router. For example, if you have the `stdout` logging exporter configured, you might see error events in the router logs:

```disableCopy=true
ERROR  response_mapping_problems=["{"message":"Property .missing not found in object","path":"@.missing","count":10}"] [Response Mapping Problems] kind=response.mapping.problems
```

## Common errors

The following are the most common composition errors you may encounter with Connectors.

### Satisfiability errors

A satisfiability error means that the GraphQL API composed of your REST APIs can't satisfy all possible requests.
This occurs because the [rules of federation composition](https://www.apollographql.com/docs/federation/federated-schemas/composition#rules-of-composition), including rules for unreachable fields, apply equally to Connectors and GraphQL subgraphs.

#### Example scenario

Consider a schema with two Connectors that hit different endpoints and get differing representations of the `Post` type. The goal is to merge the representations into a unified `Post` type so that clients can access all the fields without caring about the underlying data sources.

```graphql
type Query {
  posts: [Post]
    @connect(
      http: { GET: "https://api.example.com/v1/posts" }
      selection: "id title createdAt"
    )

  post(id: ID!): Post
    @connect(
      http: { GET: "https://api.example.com/v2/posts/{$args.id}" }
      selection: "id title body"
    )
}

type Post {
  id: ID!
  title: String
  body: String
  createdAt: String
}
```

These Connectors would raise the following satisfiability errors:

```text
SATISFIABILITY_ERROR: The following supergraph API query:
{
  posts {
    body
  }
}
cannot be satisfied by the subgraphs because:
- from subgraph "posts":
  - cannot find field "Post.body".
  - cannot move to subgraph "posts", which has field "Post.body", because type "Post" has no @key defined in subgraph "posts".

SATISFIABILITY_ERROR: The following supergraph API query:
{
  post(id: "<any id>") {
    createdAt
  }
}
cannot be satisfied by the subgraphs because:
- from subgraph "posts":
  - cannot find field "Post.createdAt".
  - cannot move to subgraph "posts", which has field "Post.createdAt", because type "Post" has no @key defined in subgraph "posts".
```

This error means we can't reach `body` from the `Query.posts` field, and we can't reach `createdAt` from the `Query.post(id:)` field.

The error messages for satisfiability suggest fixes that apply to GraphQL subgraphs, not Connectors. They suggest adding `@key` directive and an entity resolver for the type. Adding a Connector to a type is the equivalent of defining a `@key` and an entity resolver.

The first issue (`body`) is resolved with an entity Connector. By adding a Connector to the `Post` type, the query planner can make subsequent fetches to fetch that field.

```graphql
type Post
  @connect(
    http: { GET: "https://api.example.com/v2/posts/{$this.id}" }
    selection: "id title body"
  )
{
  id: ID!
  title: String
  body: String
  createdAt: String
}
```

The second issue (`createdAt`) doesn't have a straightforward solution. You need an endpoint that takes the ID of a `Post` and returns the `createdAt` field. A straightforward solution is to add a second Connector to the `Post` type:

```graphql
type Post
  @connect(
    http: { GET: "https://api.example.com/v2/posts/{$this.id}" }
    selection: "id title body"
  )
  @connect(
    http: { GET: "https://api.example.com/v1/posts/{$this.id}" }
    selection: "id createdAt"
  )
{
  id: ID!
  title: String
  body: String
  createdAt: String
}
```

Now there is always a way to resolve all fields, regardless of which Query root field the client uses.

### Circular references

If you get a composition error about circular references, you've run into a Connectors limitation. Direct circular references, such as `User.friends: [User]`, are not supported. Indirect circular references, such as `User.company: Business` and `Business.employees: [User]`, are supported using certain patterns.

#### Example scenario

When using a Connector, a `selection` of a type can't refer to itself. For example, a selection that results in `User.friends: [User]` is invalid:

```graphql
type Query {
  user(id: ID!): User
    @connect(
      http: { GET: "https://api.example.com/users/{$args.id}" }
      selection: """
      id
      name
      friends { # Circular reference to User
        id
      }
      """
    )
}

type User {
  id: ID!
  name: String
  friends: [User]
}
```

This occurs if *any* type within the selection can lead to a circular reference, not just the top-level type.
For example, this is *also* invalid:

```graphql
type Query {
  user(id: ID!): User
    @connect(
      http: { GET: "https://api.example.com/users/{$args.id}" }
      selection: """
      id
      name
      favoriteBooks { # First reference to Book
        id
        author {
          id
          books { # Circular reference to Book
            id
          }
        }
      }
      """
    )
}

type User {
  id: ID!
  name: String
  favoriteBooks: [Book]
}

type Book {
  id: ID!
  author: Author
}

type Author {
  id: ID!
  books: [Book]
}
```

To avoid circular references you can often use another Connector:

```graphql
type Query {
  user(id: ID!): User
    @connect(
      http: { GET: "https://api.example.com/users/{$args.id}" }
      selection: """
      id
      name
      favoriteBooks {
        id
        title
        author {
          id
          # No reference to books here
        }
      }
      """
    )
}

type User {
  id: ID!
  name: String
  favoriteBooks: [Book]
}

type Book {
  id: ID!
  title: String!
  author: Author
    @connect(
      http: { GET: "https://api.example.com/books/{$this.id}/author" }
      selection: """
      id
      name
      # No reference to books
      """
    )
}

type Author {
  id: ID!
  books: [Book]
    @connect(
      http: { GET: "https://api.example.com/authors/{$this.id}/books" }
      selection: """
      id
      title
      # No reference to author
      """
    )
}
```

### `null` response values

If a Connector's selection mapping and the corresponding type or field don't match,  a `null` value is returned to avoid breaking the client contract.

For example, the following Connector's `http` and `selection` arguments target a single product, but `Query.product` indicates an array of products should be returned:

```graphql
type Query {
  # TYPO: the response contains a single product, not an array
  product(id: ID!): [Product]
    @connect(
      http: { GET: "https://api/products/{$args.id}" }
      selection: "id name price"
    )
}
```

In the response, the `product` field will be `null`, though you won't see any mapping errors in the [debugger](https://www.apollographql.com/docs/graphos/connectors/troubleshooting.md#debugging).

```json
{
  "data": {
    "product": null
  }
}
```

To resolve issues like this, you can inspect the raw **Response body** in the debugger and then update the schema accordingly.
In this case, the fix is to change the return type from `[Product]` to `Product`.

### Composition errors about "valid `@key` directives"

Using the `$this` or `$batch` variables is an implicit way to create an "entity key" for a type. For example, a Connector with `GET: "/users/{$this.id}"` is the equivalent of defining a `@key(fields: "id")` directive on the `User` type.

Some expressions cannot be used to create a valid `@key` directive. For example, `$this.accounts->first.id` results in a composition error:

```text
Variables used in connector (`$this`) on type `User` cannot be used to create a valid `@key` directive.
```

To resolve this, use simpler expressions like `$this.accounts.id` or `$this.accounts { id }` without methods to create requests.
