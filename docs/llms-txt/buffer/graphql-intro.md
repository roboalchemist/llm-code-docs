# Source: https://developers.buffer.com/guides/graphql-intro.md

# GraphQL for REST Developers

If you've worked with REST APIs before, GraphQL will feel a bit different. Here's a quick rundown of the key differences.

## One endpoint, many queries

With REST, you use different URLs for different resources:

```
GET /posts
GET /channels
GET /organizations
```

With GraphQL, everything goes to one endpoint:

```
POST https://api.buffer.com
```

Instead of choosing a URL, you write a **query** that describes what you want. The endpoint is always the same.

## You choose what comes back

With REST, the server decides what's in the response. You might get 30 fields back when you only need 2. With GraphQL, you pick exactly which fields you want:

```graphql
query {
  channels(input: { organizationId: "your_org_id" }) {
    id
    name
  }
}
```

This returns only `id` and `name`, nothing extra.

## Queries read, mutations write

REST uses HTTP verbs to indicate intent: `GET` to read, `POST` to create, `PUT` to update, `DELETE` to remove.

GraphQL uses **operation types**:

- **`query`** - read data (like GET)
- **`mutation`** - create or change data (like POST/PUT/DELETE)

Both are sent as POST requests to the same endpoint. The operation type inside the request body tells the server what you're doing.

```graphql
# Reading data
query {
  account { id }
}

# Writing data
mutation {
  createPost(input: { text: "Hello!", channelId: "your_channel_id", schedulingType: automatic, mode: addToQueue }) {
    ... on PostActionSuccess { post { id } }
  }
}
```

## Errors work differently

REST uses HTTP status codes: 404 for not found, 401 for unauthorized, 500 for server error.

GraphQL always returns HTTP 200. Errors are in the response body, in two places:

**1. The `errors` array** - for non-recoverable problems (bad auth, server error):

```json
{
  "errors": [
    {
      "message": "Not authorized",
      "extensions": { "code": "UNAUTHORIZED" }
    }
  ]
}
```

**2. Typed errors in the data** for recoverable problems (validation, limits):

```graphql
mutation {
  createPost(input: { ... }) {
    ... on PostActionSuccess { post { id } }
    ... on MutationError { message }
  }
}
```

Buffer uses typed union errors so you can handle specific error cases in your code. See [Error Handling](error-handling.html) for details.

## Tools for exploring

- **[Buffer API Explorer](../explorer.html)**: try queries right in your browser
- **[API Reference](../reference.html)**: browse all available queries, mutations, and types
- **Any GraphQL client**: tools like Postman or Insomnia work great too

## Further reading

- [Quick Start](getting-started.html): make your first Buffer API request
- [Official GraphQL docs](https://graphql.org/learn/): learn GraphQL fundamentals
