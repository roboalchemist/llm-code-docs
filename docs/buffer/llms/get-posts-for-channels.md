# Source: https://developers.buffer.com/examples/get-posts-for-channels.md

Fetch a list of posts for a specific set of Channel IDs.

```graphql
query GetPostsForChannels {
  posts(
    input: {organizationId: "some_organization_id", sort: [{ field: dueAt, direction: desc  }, { field: createdAt, direction: desc  }] , filter: {status: sent, channelIds: ["some_channel_id"]}}
  ) {
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