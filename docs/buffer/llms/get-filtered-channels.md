# Source: https://developers.buffer.com/examples/get-filtered-channels.md

Fetch all channels for the provided Organization ID.

```graphql
query GetChannels {
  channels(input: {
    organizationId: "some_organization_id",
    filter:{
      isLocked: false
    }
  }) {
    id
    name
    displayName
    service
    avatar
    isQueuePaused
  }
}
```