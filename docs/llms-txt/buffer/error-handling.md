# Source: https://developers.buffer.com/guides/error-handling.md

# Error Handling

The Buffer API uses two categories of errors. Here's how they work and how to handle them in your code.

## Two types of errors

| Type | Where | When | HTTP Status |
|:-----|:------|:-----|:------------|
| **Typed mutation errors** | In the response `data` | User-fixable problems (validation, limits) | 200 |
| **Non-recoverable errors** | In the `errors` array | System problems (auth, not found, server) | 200 |

GraphQL always returns HTTP 200. Check the response body to determine success or failure.

## Typed mutation errors

Mutations return a **union type** that includes both the success case and possible error cases. This lets you handle each error type differently in your code.

### Basic pattern

Always include `... on MutationError` in every mutation:

```graphql
mutation {
  createPost(input: {
    text: "Hello world",
    channelId: "your_channel_id",
    schedulingType: automatic,
    mode: addToQueue
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

If the mutation succeeds, you get `PostActionSuccess`. If it fails, you get a `MutationError` with a human-readable `message`.

### Handling specific error types

Some mutations return specific error types with additional data. You can match on these for more precise handling:

```graphql
mutation {
  createPost(input: { ... }) {
    ... on PostActionSuccess {
      post { id }
    }
    ... on LimitReachedError {
      message
    }
    ... on InvalidInputError {
      message
    }
    ... on MutationError {
      message
    }
  }
}
```

The `... on MutationError` at the end acts as a catch-all. Because all error types implement the `MutationError` interface, any error type you don't explicitly handle will still return a `message`.

### InvalidInputError

When input validation fails, you get an error message:

```json
{
  "data": {
    "createPost": {
      "message": "Text is required"
    }
  }
}
```

### Future-proofing with VoidMutationError

Some mutations include a `VoidMutationError` in their union. The API never explicitly returns this type, but it ensures that if new error types are added later, your `... on MutationError` catch-all will still receive the `message` - no code changes needed.

**This is why you should always include `... on MutationError` in every mutation.**

## Non-recoverable errors

System-level errors appear in the GraphQL `errors` array. These indicate problems you typically can't fix by changing your input.

### Error codes

| Code | Meaning | What to do |
|------|---------|------------|
| `UNAUTHORIZED` | Missing or invalid API key | Check your `Authorization` header and API key |
| `FORBIDDEN` | Valid key, but no permission | Verify you're accessing resources in your own account |
| `NOT_FOUND` | Resource doesn't exist | Check the ID you're using is correct |
| `UNEXPECTED` | Server error | Retry after a short delay; contact support if persistent |
| `RATE_LIMIT_EXCEEDED` | Too many requests | Wait and retry; see [Rate Limits](api-limits.html) |

### Example error response

```json
{
  "data": null,
  "errors": [
    {
      "message": "Not authorized",
      "extensions": {
        "code": "UNAUTHORIZED"
      }
    }
  ]
}
```

## Error handling snippet

Here's a reusable pattern for handling both error types:

```javascript
async function bufferRequest(query, variables = {}) {
  const response = await fetch('https://api.buffer.com', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.BUFFER_API_KEY}`,
    },
    body: JSON.stringify({ query, variables }),
  });

  const result = await response.json();

  // Check for non-recoverable errors
  if (result.errors) {
    const error = result.errors[0];
    const code = error.extensions?.code;

    if (code === 'RATE_LIMIT_EXCEEDED') {
      // Wait and retry
      throw new Error('Rate limited, try again later');
    }
    throw new Error(`API error (${code}): ${error.message}`);
  }

  return result.data;
}
```

For mutations, check the response type:

```javascript
const data = await bufferRequest(`
  mutation CreatePost($input: CreatePostInput!) {
    createPost(input: $input) {
      ... on PostActionSuccess { post { id } }
      ... on MutationError { message }
    }
  }
`, { input: postInput });

if (data.createPost.post) {
  // Success
  console.log('Created post:', data.createPost.post.id);
} else if (data.createPost.message) {
  // Typed error
  console.error('Mutation error:', data.createPost.message);
}
```

## Best practices

- **Always include `... on MutationError { message }` in every mutation.** This catches current and future error types.
- **Check the `errors` array on every response.** Even successful mutations can include warnings.
- **Don't display raw error messages to end users.** Use the error type to decide what to show.
- **Log the full error response for debugging.** Include the query, variables, and complete response.
- **Handle `RATE_LIMIT_EXCEEDED` with exponential backoff.** See [Rate Limits](api-limits.html) for details on limits and retry headers.

## Next steps

- [API Standards](api-standards.html): full details on the API's error design philosophy
- [Rate Limits](api-limits.html): understand request limits and throttling
- [Your First Post](your-first-post.html): see error handling in action
