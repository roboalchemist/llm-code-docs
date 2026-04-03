# Source: https://developers.buffer.com/examples/get-paginated-posts.md

Fetch a list of posts with support for pagination.

```graphql
query GetPosts {
  posts(
    after: "id_to_start_after",
    first: 20,
    input: {organizationId: "some_organization_id", filter: {status: [sent], channelIds: ["some_channel_id"]}}
  ) {
    pageInfo {
      startCursor
      endCursor
      hasNextPage
    }
    edges {
      node {
        id
        text
        createdAt
        channelId
      }
    }
  }
}
```