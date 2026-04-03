# Source: https://developers.buffer.com/examples/get-channel.md

Fetch a single channel by its ID.

```graphql
query GetChannel {
  channel(input: {
    id: "some_channel_id"
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