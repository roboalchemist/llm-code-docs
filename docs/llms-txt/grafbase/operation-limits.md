# Source: https://grafbase.com/docs/gateway/configuration/operation-limits.md

# Source: https://grafbase.com/docs/gateway/security/operation-limits.md

# Source: https://grafbase.com/docs/gateway/configuration/operation-limits.md

# Source: https://grafbase.com/docs/gateway/security/operation-limits.md

# Source: https://grafbase.com/docs/gateway/configuration/operation-limits.md

# Source: https://grafbase.com/docs/gateway/security/operation-limits.md

# Operation Limits

One of the most common attacks malicious actors do to GraphQL APIs is sending complex and deeply nested queries to overload the server. Operation Limits allow you to protect your GraphQL API from these types of attacks. [Read more on configuring the operation limits](https://grafbase.com/docs/gateway/configuration/operation-limits.md).

## Depth

Limits the deepest nesting of selection sets in an operation, including fields in fragments.

Here's how depth is calculated:

```graphql
query GetProduct {
  product(id: "123") {
    # depth 1
    title # depth 2
    brand {
      name # depth 3
    }
  }
}
```

To configure depth, add the following to your `grafbase.toml` file:

```toml
[operation_limits]
depth = 3
```

## Height

Limits the number of unique fields included in an operation, including fields of fragments. If a particular field is included multiple times via aliases, it's counted only once.

Here's how height is calculated:

```graphql
query GetProduct {
  product(id: "123") {
    # height 1
    id # height 2
    name # height 3
    title: name # aliases don't count
  }
}
```

To configure height, add the following to your `grafbase.toml` file:

```toml
[operation_limits]
height = 20
```

## Aliases

Limits the total number of aliased fields in an operation, including fields of fragments.

Here's how aliases are calculated:

```graphql
query GetProduct {
  product(id: "123") {
    title: name # alias 1
    something: name # alias 2
    else: name # alias 3
  }
}
```

To configure aliases, add the following to your `grafbase.toml` file:

```toml
[operation_limits]
aliases = 10
```

## Root Fields

Limits the number of root fields in an operation, including root fields in fragments. If a particular root field is included multiple times via aliases, each usage is counted.

Here's how root fields are calculated:

```graphql
query GetProducts {
  topBooks {
    # root field 1
    id
  }
  topMovies {
    # root field 2
    id
  }
  topGames {
    # root field 3
    id
  }
}
```

To configure root fields, add the following to your `grafbase.toml` file:

```toml
[operation_limits]
root_fields = 10
```

## Complexity

Complexity takes the number of fields as well as the depth and any pagination arguments into account. Every scalar field adds 1 point, every nested field adds 2 points, and every pagination argument multiplies the nested objects score by the number of records fetched.

Here's how root fields are calculated:

```graphql
query {
  # total: 18
  products(limit: 2) {
    # (Nested: 2 + 1 + 1 + 1 + (author: 2 + 1 + 1)) * limit: 2 = 18
    id # scalar: 1
    title # scalar: 1
    price # scalar: 1
    brand {
      # nested: 4 (2 + 1 + 1)
      id # scalar: 1
      name # scalar: 1
    }
  }
}
```

To configure complexity, add the following to your `grafbase.toml` file:

```toml
[operation_limits]
complexity = 100
```

## Size

Both the request body size and the document size, the `query` string, are limited by the gateway:

```toml
# default values
request_body_limit = "2MiB"
executable_document_limit = "32KiB"
```

Both values apply *after* request decompression if there is any.