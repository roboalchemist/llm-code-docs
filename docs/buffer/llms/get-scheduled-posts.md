# Source: https://developers.buffer.com/examples/get-scheduled-posts.md

Fetch a list of posts that are scheduled for future publishing.

```graphql
query GetScheduledPosts {
  posts(
    input: {organizationId: "some_organization_id", sort: [{ field: dueAt, direction: asc  }, { field: createdAt, direction: desc  }] filter: {status: [scheduled]}}
  ) {
    edges {
      node {
        id
        text
        createdAt
      }
    }
  }
}
```