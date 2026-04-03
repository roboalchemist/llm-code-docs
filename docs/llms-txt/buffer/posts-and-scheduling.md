# Source: https://developers.buffer.com/guides/posts-and-scheduling.md

# Posts & Scheduling

Posts are the core content type in Buffer. Here's how they work, from creation through delivery.

## What is a post?

A post is a piece of content scheduled or published through Buffer. Every post belongs to a specific [channel](data-model.html#channel) (a connected social media profile) and goes through a lifecycle from creation to delivery.

Key fields on a post:

- **`id`** - unique identifier
- **`text`** - the post content
- **`channelId`** - which channel this post belongs to
- **`dueAt`** - when the post is scheduled to publish
- **`status`** - current lifecycle state (scheduled, sent, etc.)
- **`assets`** - attached images or media

## Scheduling types

When creating a post, you choose how it should be scheduled:

### `addToQueue`

We'll add the post to the next available time slot from your posting schedule. This is the simplest option.

```graphql
mutation {
  createPost(input: {
    text: "Automatically scheduled post",
    channelId: "your_channel_id",
    schedulingType: automatic,
    mode: addToQueue
  }) {
    ... on PostActionSuccess { post { id dueAt } }
    ... on MutationError { message }
  }
}
```

### `customScheduled`

You specify an exact date and time using the `dueAt` field in ISO 8601 format (UTC):

```graphql
mutation {
  createPost(input: {
    text: "Scheduled for a specific time",
    channelId: "your_channel_id",
    schedulingType: automatic,
    mode: customScheduled,
    dueAt: "2026-03-10T15:00:00.000Z"
  }) {
    ... on PostActionSuccess { post { id dueAt } }
    ... on MutationError { message }
  }
}
```

## Post status lifecycle

A post moves through the following states:

- **Scheduled** the post is in the queue, waiting for its `dueAt` time
- **Sent** the post was successfully published to the social platform
- **Error** the post could not be published (e.g., the channel was disconnected)

## Creating posts

Use the `createPost` mutation. Required fields:

- **`text`** - the post content
- **`channelId`** - the target channel
- **`schedulingType`** - how to schedule (`automatic`)

Always include both `PostActionSuccess` and `MutationError` in your response:

```graphql
mutation {
  createPost(input: {
    text: "Hello from the API",
    channelId: "your_channel_id",
    schedulingType: automatic,
    mode: addToQueue
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        dueAt
        assets { id mimeType }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

See [Create a Text Post](../examples/create-text-post.html) and [Create an Image Post](../examples/create-image-post.html) for complete examples.

## Retrieving posts

Query posts for a specific organization, filtered by channel and status:

```graphql
query {
  posts(
    first: 20,
    input: {
      organizationId: "your_org_id",
      filter: {
        status: [sent],
        channelIds: ["your_channel_id"]
      }
    }
  ) {
    edges {
      node {
        id
        text
        dueAt
        channelId
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

Posts are returned using [cursor-based pagination](pagination.html). Use `first` and `after` to page through results.

See [Get Posts for Channels](../examples/get-posts-for-channels.html) and [Get Paginated Posts](../examples/get-paginated-posts.html) for more examples.

## Supported platforms

The API can create posts for the following platforms:

- Instagram
- Threads
- LinkedIn
- X (Twitter)
- Facebook
- Google Business Profiles
- Mastodon
- YouTube
- Pinterest
- Bluesky

The `service` field on a [Channel](data-model.html#channel) tells you which platform it's connected to.

## Next steps

- [Create a Text Post](../examples/create-text-post.html): basic post creation example
- [Create an Image Post](../examples/create-image-post.html): attach images to posts
- [Ideas](ideas.html): save content for later
- [Pagination](pagination.html): iterate through all your posts
