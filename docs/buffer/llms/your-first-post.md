# Source: https://developers.buffer.com/guides/your-first-post.md

# Your First Post

Let's walk through creating your first post with the Buffer API. By the end, you'll have a post scheduled in your queue.

**Prerequisites:** A Buffer account with at least one connected channel, and an API key. See [Authentication](authentication.html) if you don't have a key yet.

**Time:** ~5 minutes

## Step 1: Get your organization ID

First, query your account to find your organization ID:

<!-- TABBED_CODE -->
```graphql
query GetOrganizations {
  account {
    organizations {
      id
      name
    }
  }
}
```

You'll get a response like this:

```json
{
  "data": {
    "account": {
      "organizations": [
        { "id": "your_org_id", "name": "My Company" }
      ]
    }
  }
}
```

Copy the `id` from the response. You'll need it in the next step.

## Step 2: Get your channel ID

Now query your channels using the organization ID from Step 1:

<!-- TABBED_CODE -->
```graphql
query GetChannels {
  channels(input: { organizationId: "your_org_id" }) {
    id
    name
    service
  }
}
```

This returns all your connected social profiles:

```json
{
  "data": {
    "channels": [
      { "id": "your_channel_id", "name": "My Twitter", "service": "twitter" },
      { "id": "your_other_channel_id", "name": "My Instagram", "service": "instagram" }
    ]
  }
}
```

Pick the channel you want to post to and copy its `id`.

## Step 3: Create your post

Now create a post using the channel ID from Step 2:

<!-- TABBED_CODE -->
```graphql
mutation CreateFirstPost {
  createPost(input: {
    text: "Hello from the Buffer API!",
    channelId: "your_channel_id",
    schedulingType: automatic,
    mode: addToQueue
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        dueAt
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

A successful response looks like this:

```json
{
  "data": {
    "createPost": {
      "post": {
        "id": "your_post_id",
        "text": "Hello from the Buffer API!",
        "dueAt": "2026-03-05T14:30:00.000Z"
      }
    }
  }
}
```

## Step 4: Verify in Buffer

Open your [Buffer dashboard](https://publish.buffer.com). You should see your new post in the queue for the channel you selected. With `mode: addToQueue`, we've assigned it to the next available time slot.

## Scheduling options

The example above used `mode: addToQueue`, which adds the post to the next available time slot. You can also schedule a post for a specific time:

<!-- TABBED_CODE -->
```graphql
mutation CreateScheduledPost {
  createPost(input: {
    text: "Scheduled for a specific time",
    channelId: "your_channel_id",
    schedulingType: automatic,
    mode: customScheduled,
    dueAt: "2026-03-10T15:00:00.000Z"
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        dueAt
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

The `dueAt` field accepts an ISO 8601 datetime string in UTC.

## Handling errors

If something goes wrong, the response includes a `MutationError` with a `message` field instead of `PostActionSuccess`:

```json
{
  "data": {
    "createPost": {
      "message": "Channel not found"
    }
  }
}
```

Common issues:

- **Invalid `channelId`** - double-check you copied the right ID from Step 2
- **Missing required fields** - `text` and `channelId` are always required
- **Queue limit reached**: your channel's queue is full

Always include `... on MutationError { message }` in your mutations to catch errors. See [Error Handling](error-handling.html) for more details.

## Next steps

- [Create posts with images](../examples/create-image-post.html): add images to your posts
- [Posts & Scheduling](posts-and-scheduling.html): learn about scheduling types and post lifecycle
- [Data Model](data-model.html): understand the full object hierarchy
