# Source: https://www.apollographql.com/docs/graphos/connectors/reference/preview-features.md

# Apollo Connectors Preview Features

Want to try out the latest and greatest features of Apollo Connectors? You're in the right place!

Before you jump in, there are a couple important pieces of information:

* All of these features are subject to change. Use care when updating composition or GraphOS Router.
* [Tell us what you think](https://community.apollographql.com/c/connectors/29) before these features are stable.

## Enable Preview Features

1. Use GraphOS Router v2.11.0 or later. When running `rover dev` locally, set this environment variable:
   ```bash
   APOLLO_ROVER_DEV_ROUTER_VERSION=2.11.0
   ```

2. Configure the router to enable the preview version of Connectors (in whatever file you pass for `--router-config`, typically `router.yaml`):
   ```yaml
   connectors:
     preview_connect_v0_4: true
   ```

3. Use the appropriate composition version with `rover` and Apollo Federation.
   When running `rover` locally, configure this version in a YAML file specified with `--supergraph-config`:
   ```yaml
   federation_version: =2.13.0
   ```

4. Update your schemas to use the preview version of Connectors:
   ```graphql
   extend schema
    @link(
      url: "https://specs.apollo.dev/connect/v0.4",
      import: ["@source", "@connect"]
    )
   ```

The order of these steps is important. Older versions of the router don't accept the configuration setting, and routers without the configuration reject schemas composed with the latest composition version.

## Abstract type support

Connectors v0.4 introduces support for *abstract types* (`interface` and `union` types in GraphQL), enabling type polymorphism in your connector schemas.

### What's new

Previously, Connectors required concrete object types. With v0.4, you can:

* Define fields that return `interface` types.
* Define fields that return `union` types.
* Use `->match` with string literal `__typename` values to determine the concrete type at runtime.

### Interface example

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
        id
        title
        price
        ... type->match(
          ["book", { __typename: "Book", author: author }],
          ["movie", { __typename: "Movie", director: director }]
        )
      }
      """
    )
}
```

By the time connect/v0.4 is officially released, the mapping language
will have support for object shorthand notation, so you could write
`author` instead of `author: author` and `director` instead of
`director: director`, as in `{ __typename: "Book", author }`. However,
if you're using a preview version, you may need to use the `key: value`
syntax, as shown above.

### Union example

```graphql
extend schema
  @link(
    url: "https://specs.apollo.dev/connect/v0.4",
    import: ["@source", "@connect"]
  )

@source(name: "api", http: { baseURL: "https://api.example.com" })

union SearchResult = Book | Author | SearchError

type Book {
  id: ID!
  title: String!
}

type Author {
  id: ID!
  name: String!
}

type SearchError {
  message: String!
}

type Query {
  search(query: String!): [SearchResult!]!
    @connect(
      source: "api"
      http: { GET: "/search?q={$args.query}" }
      selection: """
      $.results {
        ... resultType->match(
          ["book", { __typename: "Book", id: id, title: title }],
          ["author", { __typename: "Author", id: id, name: name }],

          # Catch-all case if resultType does not match "book" or "author"
          [@, {
            __typename: "SearchError",
            message: ["bad search result type: ", resultType]->joinNotNull(" "),
          }],
        )
      }
      """
    )
}
```

This example shows how GraphQL `union` types can enable an errors-as-data pattern. The `@` variable is bound to the value of `resultType` here, so the `[@, ...]` case will always match.

### Abstract type resolution

The key to abstract type support is the `->match` method combined with the spread operator (`...`). The `->match` method lets you conditionally return different objects based on a discriminator field in the API response (like `type` or `resultType` in the preceding examples). Each match case includes:

* A `__typename` field set to a **string literal** (like `"Book"` or `"Author"`) that identifies the concrete GraphQL type.
* The fields specific to that type.

The spread operator (`...`) then merges the matched object's properties into the selection result.

The `__typename` value must be a string literal that exactly matches one of the concrete types implementing the interface or belonging to the union. Using a field reference (like `__typename: type`) doesn't work because the connector needs specific string literals for static type analysis.
