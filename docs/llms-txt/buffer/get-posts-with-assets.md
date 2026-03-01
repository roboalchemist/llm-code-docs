# Source: https://developers.buffer.com/examples/get-posts-with-assets.md

Fetch a list of posts along with their associated assets (images, videos, etc.) for a specific set of Channel IDs.

```graphql
query GetPostsWithAssets {
  posts(
    input: {organizationId: "some_organization_id", filter: {status: [sent], channelIds: ["some_channel_id"]}}
  ) {
    edges {
      node {
        id
        text
        createdAt
        channelId
        assets {
          thumbnail
          mimeType
          source
          ... on ImageAsset {
            image {
              altText
              width
              height
            }
          }
        }
      }
    }
  }
}
```