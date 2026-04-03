# Buffer Documentation

Source: https://developers.buffer.com/llms-full.txt

---

# Buffer GraphQL API

> Complete API reference documentation

API Endpoint: https://api.buffer.com
Authentication: Bearer token via Authorization header

## Guides

### Introduction

# Introduction

## What is the Buffer API?

The Buffer API gives you programmatic access to your Buffer account. Create and schedule posts, manage content ideas, pull data on your connected channels, and build custom integrations, all through our GraphQL API.

## What can the API do?

- **Create posts:** Schedule text and image posts to any connected channel
- **Delete posts:** Remove scheduled or sent posts
- **Create ideas:** Save content ideas for later
- **Retrieve channels:** List and filter your connected social media profiles
- **Retrieve posts:** Fetch scheduled, sent, and draft posts
- **Retrieve organizations:** Access organization and account data

## How is the API built?

We use [GraphQL](https://graphql.org/), which lets you request exactly the data you need in a single request. The main difference from REST is that instead of hitting different URLs for different resources, you send queries to a single endpoint:

```
https://api.buffer.com
```

## Next steps

- [Quick Start](getting-started.html): Make your first API request in 5 minutes
- [Data Model](data-model.html): Understand how organizations, channels, and posts relate to each other
- [Examples](../examples/): See working code for common tasks

### Quick Start

Buffer's API is built with GraphQL. If you're new to GraphQL, we'd recommend the [official GraphQL documentation](https://graphql.org/learn/) to get familiar with the basics before diving in.

## Register for API Access

To get started with the Buffer API, you'll need a Buffer account and an API key. If you don't have an account yet, you can [sign up here](https://buffer.com/signup).

Once you have an account, head to [API settings](https://publish.buffer.com/settings/api) to create your API key.

## What the API supports

Your API key lets you perform actions against **your own Buffer account**. We currently support the following operations:

- Post Creation
- Post Deletion
- Post Retrieval
- Idea Creation
- Account Retrieval
- Organization Retrieval
- Channel Retrieval

## Endpoint

The Buffer GraphQL API is available at:

```
https://api.buffer.com
```

If you'd like to use a tool like Postman or another HTTP client, point your requests to the endpoint above and follow [Postman's GraphQL guide](https://learning.postman.com/docs/sending-requests/graphql/graphql-overview/) for setup.

## Authorization

Every request must include an `Authorization` header with your API key using the `Bearer` format.

<!-- AUTH_CODE_EXAMPLES -->

## Making your first request

Here's a quick query to fetch your account and organization:

<!-- FIRST_REQUEST_CODE_EXAMPLES -->

Once you have your organization ID, you can use it to fetch channels, posts, and other data for that organization.

### Authentication

# Authentication

Every request to the Buffer API needs an API key. Here's how to get one and start using it.

## Getting your API key

1. Log in to your [Buffer](https://buffer.com) account
2. Go to [Settings → API](https://publish.buffer.com/settings/api)
3. Create a new API key
4. Copy the key

## Using your API key

Include your key in the `Authorization` header of every request:

<!-- AUTH_CODE_EXAMPLES -->

Every request to `https://api.buffer.com` must include this header. Requests without a valid key will return a `401 Unauthorized` error.

## Key permissions and scope

- Your API key acts on behalf of **your account only**
- It can access all organizations and channels in your account
- There is no per-organization scoping at this time
- The key is account-based, not organization-based

If you belong to multiple organizations, your key gives you access to all of them. Use the organization ID in your queries to target a specific one.

## Security best practices

- **Never commit your API key to version control.** Add it to `.gitignore` or use a secrets manager.
- **Don't expose it in client-side code.** API calls should be made from your server, not from a browser or mobile app.
- **Use environment variables.** Store the key in an environment variable like `BUFFER_API_KEY` and reference it in your code.
- **Rotate your key if compromised.** Generate a new one in [Settings → API](https://publish.buffer.com/settings/api) and update your applications.

```javascript
// Good: read from environment variable
const apiKey = process.env.BUFFER_API_KEY;

// Not advised: hardcoded in source code
const apiKey = "buf_abc123...";
```

## OAuth (coming soon)

We're working on OAuth support for third-party apps. Check the [Roadmap](../roadmap.html) for updates. This will let you build apps that access other people's Buffer accounts with their permission.

For now, the API is designed for first-party use: automating your own account or building internal tools for your team.

## Next steps

- [Quick Start](getting-started.html): Make your first API request
- [Your First Post](your-first-post.html): Go from authenticated to a scheduled post

### Your First Post

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

### GraphQL for REST Devs

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

### REST API Migration

# Migrating from the REST API

If you've been using our REST API (`api.bufferapp.com/1/`), this guide will help you move over to the GraphQL API. It's faster to work with, returns only the data you need, and supports the core functionality of the legacy API offering.

## What's changing

| | REST API | GraphQL API |
|---|---|---|
| **Base URL** | `https://api.bufferapp.com/1/` | `https://api.buffer.com` |
| **HTTP method** | GET, POST per endpoint | Always POST |
| **Endpoints** | One per resource (`/profiles.json`, `/updates/:id.json`) | Single endpoint for everything |
| **Auth** | OAuth 2.0 access token | API key via `Authorization: Bearer` header |
| **Response shape** | Fixed - server decides what fields to return | You choose exactly which fields you need |
| **Pagination** | Offset-based (`page=1&count=10`) | Cursor-based (`first`, `after`) |
| **Errors** | HTTP status codes (401, 404, etc.) | Typed error unions in the response body |

## Authentication

The REST API used OAuth 2.0 with a client ID/secret flow. For automating your own workflows, our GraphQL API uses a simpler API key approach. OAuth support for third-party apps is coming soon.

**REST (before):**
```
GET https://api.bufferapp.com/1/user.json?access_token=YOUR_TOKEN
```

**GraphQL (now):**
```
Authorization: Bearer YOUR_API_KEY
```

Get your API key from [Settings > API](https://publish.buffer.com/settings/api). Every request to `https://api.buffer.com` must include:

- **`Authorization: Bearer YOUR_API_KEY`**

The body is always a JSON object with a `query` field. See the [Authentication guide](authentication.html) for more details.

## Endpoint mapping

### User / Account

**REST:** `GET /user.json`
**GraphQL:**

<!-- TABBED_CODE -->
```graphql
query {
  account {
    id
    email
    name
    organizations {
      id
      name
    }
  }
}
```

The REST API returned `plan` and `activity_at`. With GraphQL, you get richer account data including all your organizations in a single request - no separate calls needed.

### Profiles -> Channels

Profiles are now called **channels**. The concept is the same, a connected social media account.

**REST:** `GET /profiles.json`
**GraphQL:**

<!-- TABBED_CODE -->
```graphql
query {
  channels(input: { organizationId: "your_org_id" }) {
    id
    name
    service
    avatar
    isQueuePaused
  }
}
```

**REST:** `GET /profiles/:id.json`
**GraphQL:**

<!-- TABBED_CODE -->
```graphql
query {
  channel(input: { id: "your_channel_id" }) {
    id
    name
    service
    displayName
    avatar
  }
}
```

> **Key difference:** You now need an `organizationId` to list channels. Query your account first to get it.

### Updates -> Posts

Updates are now called **posts**.

#### List queued posts

**REST:** `GET /profiles/:id/updates/pending.json?count=10&page=1`
**GraphQL:**

<!-- TABBED_CODE -->
```graphql
query {
  posts(
    first: 10
    input: {
      organizationId: "your_org_id"
      filter: {
        status: [scheduled]
        channelIds: ["your_channel_id"]
      }
      sort: [{ field: dueAt, direction: asc }]
    }
  ) {
    edges {
      node {
        id
        text
        status
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

#### List sent posts

**REST:** `GET /profiles/:id/updates/sent.json?count=10`
**GraphQL:**

<!-- TABBED_CODE -->
```graphql
query {
  posts(
    first: 10
    input: {
      organizationId: "your_org_id"
      filter: {
        status: [sent]
        channelIds: ["your_channel_id"]
      }
      sort: [{ field: createdAt, direction: desc }]
    }
  ) {
    edges {
      node {
        id
        text
        sentAt
        externalLink
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

#### Create a post

**REST:** `POST /updates/create.json` with `profile_ids[]`, `text`, `scheduled_at`, `media[photo]`, etc.
**GraphQL:**

<!-- TABBED_CODE -->
```graphql
mutation {
  createPost(input: {
    text: "Hello from the new API!"
    channelId: "your_channel_id"
    schedulingType: automatic
    mode: addToQueue
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        status
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

> **Key differences:**
> - Posts are created for a single `channelId` instead of an array of `profile_ids`. To post to multiple channels, send one mutation per channel.
> - Use `mode: addToQueue` to add to the queue, or set `dueAt` for a specific time.
> - Errors are returned as typed unions in the response, not as HTTP status codes.

### Scheduling

**REST:** `GET /profiles/:id/schedules.json` and `POST /profiles/:id/schedules/update.json`

The GraphQL API handles scheduling differently. Instead of managing recurring time slots, you control scheduling per post:

- **Add to queue:** Set `mode: addToQueue`
- **Custom time:** Set `dueAt` to an ISO 8601 timestamp
- **Post now:** Set `mode: now`

### Links

**REST:** `GET /links/shares.json?url=https://example.com`

This endpoint has no direct equivalent in the GraphQL API. If you were using it for analytics, Buffer's analytics features are available in the dashboard.

### Configuration

**REST:** `GET /info/configuration.json`

Platform configuration (character limits, supported media types, etc.) is no longer exposed as a standalone endpoint. These constraints are enforced server-side - if you exceed a limit, you'll get an `InvalidInputError` with a clear message.

## Pagination

The REST API used offset-based pagination (`page=1&count=10`). Our GraphQL API uses cursor-based pagination, which is more reliable when data changes between requests.

**REST (before):**
```
GET /profiles/:id/updates/sent.json?page=2&count=20
```

**GraphQL (now):**

<!-- TABBED_CODE -->
```graphql
query {
  posts(
    first: 20
    after: "cursor_from_previous_page"
    input: { organizationId: "your_org_id" }
  ) {
    edges {
      node { id, text }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

To paginate, pass the `endCursor` from the previous response as the `after` argument in your next query. See the [Pagination guide](pagination.html) for more details.

## Error handling

The REST API used HTTP status codes (401, 404, 429, etc.) and numeric error codes in the body. Our GraphQL API always returns HTTP 200 and uses typed error unions instead.

**REST (before):**
```json
HTTP 403
{
  "code": 1023,
  "error": "Profile update quota exceeded."
}
```

**GraphQL (now):**
```json
{
  "data": {
    "createPost": {
      "message": "Queue limit reached",
      "limit": 100
    }
  }
}
```

Always include `... on MutationError { message }` as a catch-all in your mutations. See [Error Handling](error-handling.html) for the full guide.

## Concepts that don't carry over

A few REST API features work differently or aren't yet available in our GraphQL API:

- **`/updates/:id/share.json`** (post immediately) - Use `mode: now` on `createPost` instead
- **`/updates/:id/move_to_top.json`** and **reorder/shuffle** - Queue management is handled through scheduling
- **`/user/deauthorize.json`** - API keys can be revoked from your account settings
- **`/links/shares.json`** - Share counts are not available via the API
- **`/info/configuration.json`** - Platform limits are enforced server-side with clear validation errors

### Data Model

# Data Model

Buffer's API is organized around a few core objects. Here's how they fit together.

## Overview

```
Account
  └── Organizations (one or more)
        ├── Channels (one or more per org)
        │     └── Posts (belong to a channel)
        └── Ideas (belong to an organization)
```

Your **account** contains one or more **organizations**. Each organization has **channels** (connected social media profiles) and **ideas** (draft content). **Posts** are created on specific channels.

## Account

Your account represents your Buffer login. When you authenticate with the API, you're acting as your account. Each account can belong to one or more organizations.

```graphql
query {
  account {
    id
    organizations {
      id
      name
    }
  }
}
```

## Organization

An organization is a workspace in Buffer. Most people have one, but if you're managing multiple brands you might have several. Each organization contains channels and ideas.

You'll need an organization ID for most operations. Retrieve it first:

```graphql
query {
  account {
    organizations {
      id
      name
    }
  }
}
```

## Channel

A channel is a connected social media profile, like your company's X account or your personal Instagram. Channels belong to an organization.

```graphql
query {
  channels(input: { organizationId: "your_org_id" }) {
    id
    name
    service
  }
}
```

The `service` field tells you which platform the channel is on (e.g., twitter, instagram, facebook, linkedin).

## Post

A post is a piece of content scheduled or published through Buffer. Every post belongs to a channel. When creating a post, you specify the channel ID and the scheduling behavior.

```graphql
mutation {
  createPost(input: {
    text: "Hello world"
    channelId: "your_channel_id"
    schedulingType: automatic
    mode: addToQueue
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
      }
    }
  }
}
```

## Idea

An idea is a piece of draft content saved for later. Ideas belong to an organization (not a channel) because they haven't been assigned to a specific platform yet.

```graphql
mutation {
  createIdea(input: {
    organizationId: "your_org_id"
    content: {
      text: "Blog post concept: ..."
    }
  }) {
    ... on Idea {
      id
      content {
        text
      }
    }
  }
}
```

## Common patterns

### The typical API flow

1. **Authenticate** with your API key
2. **Query your account** to get organization IDs
3. **Query channels** for your target organization
4. **Create posts** on specific channels, or **create ideas** on the organization

## Next steps

- [Your First Post](your-first-post.html): Walk through the full flow from authentication to a published post
- [Posts & Scheduling](posts-and-scheduling.html): Deep dive into scheduling options and post types

### Posts & Scheduling

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

### Ideas

# Ideas

Ideas let you capture content thoughts and plan ahead before scheduling to a specific channel.

## Ideas vs. posts

The key difference:

- **Posts** belong to a **channel**. They're assigned to a specific social media profile and have a scheduled time.
- **Ideas** belong to an **organization**. They're not tied to any channel or schedule yet.

Think of ideas as your content backlog. When you're ready to publish, you create a post from an idea by assigning it to a channel.

## Creating an idea

Use the `createIdea` mutation with your organization ID:

```graphql
mutation {
  createIdea(input: {
    organizationId: "your_org_id",
    content: {
      title: "Blog post announcement",
      text: "We just published our guide to social media automation. Share it across all channels this week."
    }
  }) {
    ... on Idea {
      id
      content {
        title
        text
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

The `content` object supports:

- **`title`** - a short heading for the idea (optional)
- **`text`** - the body content of the idea

See [Create an Idea](../examples/create-idea.html) for a complete example.

## Why ideas belong to organizations

Ideas are organization-level because they haven't been assigned to a platform yet. A single idea might eventually become:

- A tweet on X
- A carousel on Instagram
- A post on LinkedIn

Since you haven't decided which channel (or channels) to use, the idea lives at the organization level where all your channels are.

When you're ready to publish, create a [Post](posts-and-scheduling.html) on the appropriate channel using the idea's content.

## Next steps

- [Create an Idea](../examples/create-idea.html): working example
- [Posts & Scheduling](posts-and-scheduling.html): publish content to channels
- [Data Model](data-model.html): understand how ideas, posts, channels, and organizations relate

### API Standards

# API Standards

We've designed the Buffer API around a set of principles that keep things stable and predictable as we evolve the schema.

## Always Add, Never Modify or Remove

We only add to the schema. We won't modify or remove existing fields and types. Your queries and mutations will keep working as we ship updates. New fields and types are added alongside existing ones, so you don't need to worry about breaking changes.

When we plan to retire a field, we mark it with the `@deprecated` annotation. Deprecated fields include a `reason` that describes the replacement and when the field will be removed.

```jsx
type ExampleType {
  oldField: String @deprecated(reason: "Use `newField`. This will be removed on the 12/10/2021")
  newField: String
}
```

You'll always have advance notice before a field is removed. Keep an eye on the `@deprecated` annotations in the schema, our [Changelog](../changelog.html), and migrate to the recommended replacements before the removal date.

## Using Input Objects for Operation Arguments

We use input objects rather than inline arguments. This keeps things flexible as the API evolves. For example, instead of passing individual scalars:

```jsx
type Mutation {
  createPost(text: String): ...
}
```

The API uses a dedicated input type:

```jsx
input PostInput {
  orgId: String
  text: String
}

type Mutation {
  createPost(input: PostInput!): ...
}
```

This means new fields can be added to the input type without affecting existing operations.

## Returning Typed Responses

Our operations return typed response objects rather than scalar values. This lets responses evolve over time. For example, adding new fields, without breaking the contract. It also enables union types for error handling.

```jsx
type Mutation {
  createPost(...): Post
}
```

Instead, we use typed responses that can include additional data and error states:

```jsx
type PostActionSuccess {
  post: Post!
}

type LimitReachedError {
  message: String!
}

union PostActionPayload = PostActionSuccess | LimitReachedError

type Mutation {
  createPost(...): PostActionPayload
}
```

## Being Specific with Nullability

We use nullability to communicate exactly what you can expect from each field. A non-null field (marked with `!`) guarantees a value will always be present. A nullable field may return `null`, and your client should handle that case.

Here's an example:

```jsx
type Post {
  type: PostStatus!
  sentAt: DateTime
}
```

For this type, there are two states:

- **Non-null** - a value will always be provided. You don't need to handle a null state. For example, a post always has a `PostStatus`:

```jsx
type: PostStatus!
```

- **Nullable** - a null value may be returned, and your client should handle it. For example, a post only has a `sentAt` for when a post has been published:

```jsx
sentAt: DateTime
```

### Nullability in Arrays

Nullability applies to both the array itself and the type contained within it.

**In short**: if an array will never contain null entries, the entry type is marked as non-null. If the array itself can never be null, it's also marked as non-null.

```jsx
posts: [Post]
```

Both the array and its entries can be null. You could receive `null`, or an array containing null values such as `[ATTACHMENT, null, ATTACHMENT]`.

```jsx
posts: [Post]!
```

The array will never be null (it will always be returned, even if empty), but individual entries may be null. For example, `[null, TAG, null]` or `[]`, but never `null`.

```jsx
posts: [Post!]
```

The array may be null, but when present, its entries will never be null. For example, `[]`, `null`, or `[MEDIA, MEDIA]`.

When both the array and entries are non-null:

```jsx
posts: [Post!]!
```

You are guaranteed a non-null array with non-null entries.

### Boolean Values

Boolean fields are always non-null. You will always receive either `true` or `false`, so there is no need to handle a null state for boolean values.

## Returning Contextual Responses to Clients

Our mutation responses return meaningful data related to the action performed, rather than generic status flags. For example, instead of:

```kotlin
type PostActionSuccess  {
    success: Boolean!
}
```

The response returns the resource that was affected:

```kotlin
type PostActionSuccess {
    post: Post!
}
```

This gives you immediately useful data and avoids redundant checks. If you're using Apollo Client, the local cache will automatically update when it receives a response matching the `id` and `__typename` of an already-cached object.

## Maintaining Input Type Ordering

We always append new fields to the end of input types. This matters because some code-generated clients send arguments positionally. If a new field were inserted in the middle, existing positional arguments would shift and map to the wrong fields.

Here's an example. Given this input type:

```kotlin
input IdeaCreationInput {
  organizationId: String!
  content: IdeaContentInput!
  source: String
}
```

A code-generated client (e.g. Apollo on Android) produces:

```kotlin
public data class IdeaCreationInput(
  public val organizationId: String,
  public val content: IdeaContentInput,
  public val cta: Optional<String?> = Optional.Absent,
)
```

And the client sends arguments positionally:

```kotlin
IdeaCreateMutation(
    IdeaCreationInput(
        idea.organizationId!!,
        idea.toInput(),
        Optional.presentIfNotNull(source)
    )
)
```

If a new field `groupId` were added in the middle:

```kotlin
input IdeaCreationInput {
  organizationId: String!
  content: IdeaContentInput!
  groupId: ID
  source: String
}
```

The generated class would shift:

```kotlin
public data class IdeaCreationInput(
  public val organizationId: String,
  public val content: IdeaContentInput,
  public val groupId: Optional<String?> = Optional.Absent,
  public val cta: Optional<String?> = Optional.Absent,
)
```

Clients that have not updated would now send the `source` value as `groupId`, causing incorrect behavior.

```kotlin
IdeaCreateMutation(
    IdeaCreationInput(
        idea.organizationId!!,
        idea.toInput(),
        Optional.presentIfNotNull(source)
    )
)
```

To avoid this, always use **named arguments** rather than positional arguments when constructing input types in your client code.

## Pagination

Paginated responses use cursor-based pagination with the following structure:

- `edges`: a list of connections to the response items
- `pageInfo`: pagination metadata (see `PaginationPageInfo` below)
- `totalCount`: optional, but when present, always non-null. The total count of all results matching the query filters.

### Request Fields

**input**

The input filter. The top level includes static, required fields (typically the organization ID), plus an optional `filter` object for narrowing results.

- `organizationId`: The organization ID for the request.
- `filter`: Filtering criteria applied to results and counts.
  - Filter values are typically lists of string IDs.
  - Fields are nullable - omitting a filter field means no filtering is applied for that criterion.
  - Filtering logic uses an **AND** operation between all defined items.

**first**

The maximum number of items to return (synonymous with "limit").

**after**

The cursor to start fetching from. Cursors are opaque strings. Do not parse or construct them yourself.

### Response Fields

**totalCount**

The total number of results matching the query filters, consistent with [GraphQL pagination best practices](https://graphql.org/learn/pagination/) and [GitHub's implementation](https://docs.github.com/en/graphql/reference/objects#branchprotectionruleconflictconnection).

**pageInfo**

- `startCursor`: The first cursor in the list. Use it to fetch the previous page.
- `endCursor`: The last cursor in the list. Use it to fetch the next page.
- `hasPreviousPage`: `true` if a previous page is available. Currently always `false` as only forward pagination is supported.
- `hasNextPage`: `true` if a next page is available.

## Error Handling

We use two categories of errors:

- **Non-recoverable errors** appear in the standard GraphQL `errors` array. These represent issues outside your control - authentication failures, missing resources, or server errors. They include an error `code` in the `extensions` object (e.g. `NOT_FOUND`, `FORBIDDEN`, `UNAUTHORIZED`, `UNEXPECTED`).

- **Recoverable errors** (user errors) are returned as typed data in the response payload. These are situations you can act on, like input validation failures or account limits being reached.

### Mutations

#### Modelling Errors

Every mutation returns a payload union that includes both the success state and any user-facing errors. The payload follows the naming convention `{MutationName}Payload`.

```graphql
union PostActionPayload = PostActionSuccess | ...
```

You can query for the specific error types you need to handle. New error types may be added to a payload over time.

```graphql
union PostActionPayload = PostActionSuccess | LimitReachedError | InvalidInputError
```

Every typed error implements the `MutationError` interface:

```graphql
interface MutationError {
    message: String!
}
```

Each error type includes the `message` field from the interface:

```graphql
type LimitReachedError implements MutationError {
    message: String!
}

type InvalidInputError implements MutationError {
    message: String!
}
```

The `message` field contains a human-readable string suitable for display. In most cases you'll use the error type itself to determine what to show, but the `message` provides a sensible default (see **Future Proofing Error Responses** below).

#### Consuming Errors

To consume typed errors, use the `... on` pattern to match specific error types in the response. This lets you handle each error differently - for example, showing a specific recovery path to the user.

You only need to match the error types you care about. For everything else, use `... on MutationError` as a catch-all:

```graphql
mutation CreatePost {
  createPost {
    ... on PostActionSuccess {
      // handle fields
    }
    ... on LimitReachedError {
      message
    }
    ... on MutationError {
      message
    }
  }
}
```

If you don't need to handle specific error types, you can rely entirely on the `MutationError` interface:

```graphql
mutation CreatePost {
  createPost {
    ... on PostActionSuccess {
      // handle fields
    }
    ... on MutationError {
      message
    }
  }
}
```

#### Future Proofing Error Responses

Some mutations may not have specific typed errors defined yet. To make sure your client handles any errors we add in the future, every mutation payload includes a `VoidMutationError` type:

```graphql
type VoidMutationError implements MutationError {
  message: String!
}

union PostActionPayload = PostActionSuccess | VoidMutationError
```

We'll never explicitly return a `VoidMutationError`, but its presence in the union means that if you include `... on MutationError` in your query, your client will automatically receive the `message` for any new error types we add later - no code changes needed.

```graphql
... on MutationError {
  message
}
```

For this reason, **always include `... on MutationError`** in your mutation queries.

#### Non-Recoverable Errors

Non-recoverable errors are returned in the standard GraphQL `errors` array. These include an error `code` in the `extensions` object for additional context. Common error codes include:

- `NOT_FOUND` - the requested resource doesn't exist
- `FORBIDDEN` - you don't have permission for this action
- `UNAUTHORIZED` - authentication is required or invalid
- `UNEXPECTED` - an unexpected server error occurred

If you need to show error details to users, use typed errors (as described above) instead of the `errors` array.

### Queries

In most cases, queries return either the requested data or a non-recoverable error in the `errors` array:

```graphql
type Query {
  channels(input: ChannelsInput!): [Channel!]!
}
```

A successful result returns the list of `Channel` types. If an error occurs, it appears in the `errors` array.

In rare cases, a query may need to return a recoverable error. When this applies, we use a union payload, the same pattern as mutations. For example, if fetching a post requires reconnecting a channel, the response includes a typed error:

```graphql
type PostSuccess {
  post: Post!
}

type ChannelReconnectRequired implements MutationError {
  message: String!
  channelId: String!
}

union PostPayload = PostSuccess | ChannelReconnectRequired

type Query {
  post(input: PostInput!): PostPayload
}
```

This pattern is uncommon for queries but provides a way to surface recoverable errors when needed.

### Error Handling

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

### Rate Limits

We apply rate limits using a dual-layer approach to keep things fair for everyone.

### Rate Limits by Client Type

- **Third-party Clients**: 100 requests per 15 minutes
- **Unknown/Unauthenticated**: 50 requests per 15 minutes
- **Account Overall** (all clients combined): 2000 requests per 15 minutes

### How It Works

Rate limits are applied in two layers:

1. **Client + Account**: Limits requests per client and account combination. This prevents a single client from overwhelming the API for a specific account.
2. **Account Overall**: Limits total requests per account across all clients. This prevents bypassing limits by using multiple clients simultaneously.

### Response Headers

Rate limit information is included in the response headers:

```http
RateLimit-Limit: 1000
RateLimit-Remaining: 850
RateLimit-Reset: 2024-01-01T12:00:00.000Z
```

### Error Response

When a rate limit is exceeded, you will receive an HTTP `429 Too Many Requests` response:

```json
{
  "errors": [
    {
      "message": "Too many requests from this client. Please try again later.",
      "extensions": {
        "code": "RATE_LIMIT_EXCEEDED",
        "limitType": "CLIENT_ACCOUNT",
        "retryAfter": 900
      }
    }
  ]
}
```

Use the `retryAfter` value (in seconds) to determine when you can make requests again.

## Query Limits

In addition to rate limits, we enforce query-level limits to protect against overly complex or expensive GraphQL queries.

### Query Complexity

Each query is assigned a cost based on the fields it requests:

- **Scalar fields** (e.g., `id`, `name`): 1 point each
- **Object fields** (e.g., `organization`, `channel`): 2 points each
- **Nesting multiplier**: Nested fields are multiplied by a factor of 1.5x per level of depth

The maximum allowed query cost is **175,000 points**. If your query exceeds this, you will receive an error asking you to simplify it.

### Query Depth

Queries are limited to a maximum depth of **25 levels**. Deeply nested queries can cause exponential resource consumption, so keep your queries as flat as possible.

### Aliases

A maximum of **30 aliases** are allowed per query. Aliases let you rename fields in a response, but excessive use can be used to amplify query cost.

### Directives

Queries are limited to a maximum of **50 directives**.

### Tokens

Queries are limited to a maximum of **15,000 tokens**. This is a parser-level limit on the overall size of the query document.

### Query Limit Error Responses

When a query limit is exceeded, you will receive a GraphQL error response:

```json
{
  "errors": [
    {
      "message": "Query exceeds maximum allowed complexity. Please simplify your query."
    }
  ]
}
```

The error message will indicate which limit was exceeded (complexity, depth, aliases, directives, or tokens).

These limits may change as we evolve the API, so keep an eye on your usage.

### Pagination

# Pagination

The Buffer API uses **cursor-based pagination** for queries that return lists of items. Here's how to page through results.

## How it works

Rather than using page numbers, the Buffer API uses cursor strings to track your position in a result set. You request a batch of items, receive a cursor pointing to the last item, then pass that cursor to fetch the next batch.

This means you won't skip or duplicate results if new items are added between requests.

## Basic query structure

Paginated queries use three key arguments:

- **`first`** - how many items to return (the page size)
- **`after`** - the cursor to start from (omit for the first page)
- **`input`** - filters for the query

And the response includes:

- **`edges`** - the list of items, each wrapped in a `node`
- **`pageInfo`** - pagination metadata

```graphql
query {
  posts(
    first: 20,
    input: {
      organizationId: "your_org_id",
      filter: { status: [sent] }
    }
  ) {
    edges {
      node {
        id
        text
        dueAt
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Reading the response

The `pageInfo` object tells you about pagination state:

- **`hasNextPage`** - `true` if there are more items after this batch
- **`endCursor`** - the cursor of the last item, used to fetch the next page
- **`startCursor`** - the cursor of the first item
- **`hasPreviousPage`** - currently always `false` (only forward pagination is supported)

## Fetching the next page

To get the next page, pass the `endCursor` from the previous response as the `after` argument:

```graphql
query {
  posts(
    first: 20,
    after: "cursor_from_previous_response",
    input: {
      organizationId: "your_org_id",
      filter: { status: [sent] }
    }
  ) {
    edges {
      node {
        id
        text
      }
    }
    pageInfo {
      hasNextPage
      endCursor
    }
  }
}
```

## Tips

- **Choose an appropriate page size.** A `first` value of 20–50 works well for most use cases. Larger pages mean fewer requests but larger responses.
- **Don't parse cursors.** Cursors are opaque strings. Store them and pass them back as-is.
- **Respect rate limits.** When fetching many pages, be mindful of the [rate limits](api-limits.html). Consider adding a small delay between requests if needed.


## Filtering

Most paginated queries support filtering via the `input.filter` object. Filters are combined with **AND** logic - all conditions must match.

```graphql
query {
  posts(
    first: 20,
    input: {
      organizationId: "your_org_id",
      filter: {
        status: [scheduled],
        channelIds: ["your_channel_id", "your_other_channel_id"]
      }
    }
  ) {
    edges { node { id text channelId } }
    pageInfo { hasNextPage endCursor }
  }
}
```

This returns only scheduled posts from the specified channels.

## Next steps

- [Get Paginated Posts](../examples/get-paginated-posts.html): working pagination example
- [API Limits](api-limits.html): rate limiting and query constraints
- [Posts & Scheduling](posts-and-scheduling.html): more about working with posts

### Integrations

Connect Buffer with your favorite tools and AI assistants. Browse our integrations below to automate your social media workflow.

<div class="integrations-grid">

  <a href="integrations/zapier.html" class="integration-card">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="https://static.buffer.com/publish/zapier-B5YW4nQ2.png" alt="Zapier" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">Zapier</div>
      <div class="integration-card-desc">Automate workflows by connecting Buffer with thousands of apps.</div>
    </div>
  </a>

  <a href="integrations/claude.html" class="integration-card">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="https://static.buffer.com/publish/claude-Cy2cH_fJ.png" alt="Claude" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">Claude</div>
      <div class="integration-card-desc">Draft, refine, and schedule social content with Anthropic's AI assistant.</div>
    </div>
  </a>

  <a href="integrations/mcp.html" class="integration-card">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="https://static.buffer.com/publish/mcp-TA3XSNhs.png" alt="MCP" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">MCP</div>
      <div class="integration-card-desc">Give AI assistants direct access to Buffer via Model Context Protocol.</div>
    </div>
  </a>

  <a href="integrations/cursor.html" class="integration-card">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="data:image/avif;base64,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" alt="Cursor" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">Cursor</div>
      <div class="integration-card-desc">Manage Buffer content directly from your AI-powered code editor.</div>
    </div>
  </a>

  <a href="integrations/n8n.html" class="integration-card">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="data:image/avif;base64,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" alt="n8n" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">n8n</div>
      <div class="integration-card-desc">Build visual automation workflows with Buffer and hundreds of services.</div>
    </div>
  </a>

  <a href="integrations/raycast.html" class="integration-card">
    <div class="integration-card-icon" style="background-color: #1a1a1a;">
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">Raycast</div>
      <div class="integration-card-desc">Schedule posts and manage your queue with a quick keyboard shortcut.</div>
    </div>
  </a>

  <a href="https://buffersurvey.typeform.com/to/ff0kQonB" class="integration-card integration-card--coming-soon" target="_blank" rel="noopener noreferrer">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="https://static.buffer.com/publish/chatgpt-BkqmL2Ui.png" alt="ChatGPT" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">
        ChatGPT
        <span class="integration-badge">Coming soon</span>
      </div>
      <div class="integration-card-desc">Create and manage social content through natural conversation.</div>
      <span class="integration-cta">Get early access &rarr;</span>
    </div>
  </a>

  <a href="https://buffersurvey.typeform.com/to/wFc1U7v2" class="integration-card integration-card--coming-soon" target="_blank" rel="noopener noreferrer">
    <div class="integration-card-icon" style="background-color: transparent; overflow: hidden;">
      <img src="https://static.buffer.com/publish/perplexity-6Nmqf2ts.png" alt="Perplexity" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
    </div>
    <div class="integration-card-body">
      <div class="integration-card-name">
        Perplexity
        <span class="integration-badge">Coming soon</span>
      </div>
      <div class="integration-card-desc">Research trending topics and create data-backed social posts.</div>
      <span class="integration-cta">Get early access &rarr;</span>
    </div>
  </a>

</div>

### Zapier

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/zapier-B5YW4nQ2.png" alt="Zapier" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Zapier</div>
    <div class="integration-page-subtitle">Automate workflows with Zapier</div>
  </div>
</div>

Zapier connects Buffer with thousands of apps so you can automate your workflow without writing code. For example, you could auto-post to Discord when you publish, send engagement stats to a spreadsheet, or turn Trello card updates into scheduled Buffer drafts.

## Setup

<div class="setup-steps">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Zapier.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Navigate to Zapier Connections</h3>
      <p>Click "Add connection" to connect Buffer. <a href="https://actions.zapier.com/credentials/" target="_blank" rel="noopener noreferrer">Zapier Connections</a></p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Search for MCP Client</h3>
      <p>Search for "MCP Client by Zapier" and select it, then click "Add connection".</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Configure the connection</h3>
      <p>Fill in the form with the following settings:</p>
      <ul class="setup-settings-list">
        <li>
          <span>Server URL:</span>
          <code>https://mcp.buffer.com/mcp</code>
          <button class="inline-copy-btn" data-copy="https://mcp.buffer.com/mcp" title="Copy URL">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li><span>Transport:</span> Streamable HTTP</li>
        <li><span>OAuth:</span> No</li>
        <li>
          <span>Bearer Token:</span>
          <code>YOUR_API_KEY</code>
          <button class="inline-copy-btn" data-copy="YOUR_API_KEY" title="Copy bearer token">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Complete the setup</h3>
      <p>Click "Yes, Continue to MCP Client by Zapier" to finish.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Zapier:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>When a new blog post is published in WordPress, create a draft post in Buffer with the post title and link</span>
    <button class="inline-copy-btn" data-copy="When a new blog post is published in WordPress, create a draft post in Buffer with the post title and link" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>When a new row is added to my Google Sheet, add a post to my Buffer queue with that content</span>
    <button class="inline-copy-btn" data-copy="When a new row is added to my Google Sheet, add a post to my Buffer queue with that content" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Every Monday at 8am, check my Buffer queue and notify me in Slack if any channel has no posts scheduled</span>
    <button class="inline-copy-btn" data-copy="Every Monday at 8am, check my Buffer queue and notify me in Slack if any channel has no posts scheduled" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>

### Claude

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/claude-Cy2cH_fJ.png" alt="Claude" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Claude</div>
    <div class="integration-page-subtitle">Manage your content from Claude</div>
  </div>
</div>

Claude lets you manage your Buffer content using natural language.

You can create posts, schedule content, and manage your social media presence directly from Claude using the Buffer MCP server.

<div class="setup-tabs-container">
  <div class="setup-tabs">
    <button class="setup-tab active" data-tab="claude-desktop">Claude Desktop</button>
    <button class="setup-tab" data-tab="claude-code">Claude Code</button>
  </div>

  <div class="setup-tab-content active" data-tab-content="claude-desktop">

<div class="setup-steps" style="--step-color: #D97757;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Claude.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Install Node.js (one-time setup)</h3>
      <p>This integration requires Node.js 18 or higher. <a href="https://nodejs.org" target="_blank" rel="noopener noreferrer">Download Node.js</a></p>
      <p class="setup-note"><strong>Note:</strong> If you have multiple Node.js versions installed, verify that Claude Desktop is picking up version 18 or higher.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Open Claude Settings</h3>
      <p>Open Claude desktop and go to "Settings..."</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Navigate to Developer Tab</h3>
      <p>Click on the "Developer" tab.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Edit Configuration</h3>
      <p>Click "Edit config" to open the configuration file.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">6</div>
    <div class="setup-step-content">
      <h3>Add Buffer MCP Server</h3>
      <p>Open claude_desktop_config.json and add the following configuration:</p>
      <div class="setup-code-block">
        <button class="inline-copy-btn" data-copy='{
  "mcpServers": {
    "Buffer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.buffer.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}' title="Copy configuration">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        </button>
<pre><code>{
  "mcpServers": {
    "Buffer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.buffer.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}</code></pre>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">7</div>
    <div class="setup-step-content">
      <h3>Save and Restart</h3>
      <p>Save the configuration file and restart Claude desktop to apply the changes.</p>
    </div>
  </div>
</div>

  </div>

  <div class="setup-tab-content" data-tab-content="claude-code">

<div class="setup-steps" style="--step-color: #D97757;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Claude Code.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Install Node.js (one-time setup)</h3>
      <p>This integration requires Node.js 18 or higher. <a href="https://nodejs.org" target="_blank" rel="noopener noreferrer">Download Node.js</a></p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Add Buffer MCP Server</h3>
      <p>Run the following command to add the Buffer MCP server to Claude Code:</p>
      <div class="setup-code-block">
        <button class="inline-copy-btn" data-copy="claude mcp add buffer -- npx -y mcp-remote https://mcp.buffer.com/mcp --header &quot;Authorization: Bearer YOUR_API_KEY&quot;" title="Copy command">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        </button>
<pre><code>claude mcp add buffer -- npx -y mcp-remote \
  https://mcp.buffer.com/mcp \
  --header "Authorization: Bearer YOUR_API_KEY"</code></pre>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Start Using Buffer</h3>
      <p>Launch Claude Code and start managing your Buffer content with natural language.</p>
    </div>
  </div>
</div>

  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Claude:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>Show me all my scheduled Buffer posts for this week</span>
    <button class="inline-copy-btn" data-copy="Show me all my scheduled Buffer posts for this week" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Create a draft post in Buffer that says 'We just launched our redesigned dashboard!' for my Twitter channel</span>
    <button class="inline-copy-btn" data-copy="Create a draft post in Buffer that says 'We just launched our redesigned dashboard!' for my Twitter channel" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>List my Buffer channels and show me which ones have posts scheduled for tomorrow</span>
    <button class="inline-copy-btn" data-copy="List my Buffer channels and show me which ones have posts scheduled for tomorrow" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>

### MCP

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/mcp-TA3XSNhs.png" alt="MCP" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">MCP</div>
    <div class="integration-page-subtitle">Connect any tool to the Buffer MCP server</div>
  </div>
</div>

Use our open MCP server to connect any MCP-compatible AI tool to Buffer. If your AI tool supports MCP but doesn't have a Buffer integration guide, follow the setup instructions.

## Setup

<div class="setup-steps" style="--step-color: #6366F1;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with MCP.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Configure Your MCP Client</h3>
      <p>LLM clients that support MCP and headers can connect to Buffer by adding an HTTP MCP server with the following settings:</p>
      <ul class="setup-settings-list">
        <li>
          <span>Server URL:</span>
          <code>https://mcp.buffer.com/mcp</code>
          <button class="inline-copy-btn" data-copy="https://mcp.buffer.com/mcp" title="Copy URL">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li>
          <span>Authorization Header:</span>
          <code>Authorization: Bearer YOUR_API_KEY</code>
          <button class="inline-copy-btn" data-copy="Authorization: Bearer YOUR_API_KEY" title="Copy authorization header">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with MCP:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>List all my connected Buffer channels</span>
    <button class="inline-copy-btn" data-copy="List all my connected Buffer channels" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Add a post to my Buffer queue that says 'Excited to share our latest update!' for next Monday</span>
    <button class="inline-copy-btn" data-copy="Add a post to my Buffer queue that says 'Excited to share our latest update!' for next Monday" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Show me all my draft posts in Buffer so I can review what's pending</span>
    <button class="inline-copy-btn" data-copy="Show me all my draft posts in Buffer so I can review what's pending" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>

### Cursor

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="data:image/avif;base64,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" alt="Cursor" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Cursor</div>
    <div class="integration-page-subtitle">Manage Buffer from your code editor</div>
  </div>
</div>

Use the Buffer MCP server within Cursor to manage social media content directly from your AI-powered code editor. Schedule posts, check your queue, and draft content - all without leaving your IDE.

## Setup

<div class="setup-steps" style="--step-color: #2563EB;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Cursor.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Install Node.js (one-time setup)</h3>
      <p>This integration requires Node.js 18 or higher. <a href="https://nodejs.org" target="_blank" rel="noopener noreferrer">Download Node.js</a></p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Open Cursor Settings</h3>
      <p>Open Cursor and go to Settings. You can use the keyboard shortcut <code>Cmd+Shift+J</code> (Mac) or <code>Ctrl+Shift+J</code> (Windows/Linux).</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Navigate to MCP</h3>
      <p>Click on the "MCP" tab in the settings sidebar.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Add Buffer MCP Server</h3>
      <p>Click "Add new global MCP server" and add the following configuration:</p>
      <div class="setup-code-block">
        <button class="inline-copy-btn" data-copy='{
  "mcpServers": {
    "Buffer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.buffer.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}' title="Copy configuration">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
        </button>
<pre><code>{
  "mcpServers": {
    "Buffer": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.buffer.com/mcp",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}</code></pre>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">6</div>
    <div class="setup-step-content">
      <h3>Verify Connection</h3>
      <p>After saving, you should see a green indicator next to "Buffer" in the MCP settings confirming the server is connected.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Cursor:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>List all my connected Buffer channels</span>
    <button class="inline-copy-btn" data-copy="List all my connected Buffer channels" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Draft a Buffer post announcing the new feature I just committed and schedule it for tomorrow morning</span>
    <button class="inline-copy-btn" data-copy="Draft a Buffer post announcing the new feature I just committed and schedule it for tomorrow morning" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Show me all my draft posts in Buffer so I can review what's pending</span>
    <button class="inline-copy-btn" data-copy="Show me all my draft posts in Buffer so I can review what's pending" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>

### n8n

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="data:image/avif;base64,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" alt="n8n" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">n8n</div>
    <div class="integration-page-subtitle">Workflow automation with n8n</div>
  </div>
</div>

n8n is a workflow automation tool that connects Buffer with hundreds of apps.

Create complex automation workflows, trigger posts based on events, and integrate Buffer into your existing automation pipelines.

## Setup

<div class="setup-steps" style="--step-color: #EA4B71;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with n8n.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Add MCP Client to Workflow</h3>
      <p>Inside of a workflow, add an "MCP Client" node.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Configure the MCP Client</h3>
      <p>Fill in the form with the following details:</p>
      <ul class="setup-settings-list">
        <li><span>Server Transport:</span> HTTP Streamable</li>
        <li>
          <span>MCP Endpoint URL:</span>
          <code>https://mcp.buffer.com/mcp</code>
          <button class="inline-copy-btn" data-copy="https://mcp.buffer.com/mcp" title="Copy URL">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li><span>Authentication:</span> Bearer Auth</li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Add Your Credentials</h3>
      <p>Click on "Credential for Bearer Auth" and configure:</p>
      <ul class="setup-settings-list">
        <li>Select "Create new credential"</li>
        <li>
          Add your API key: <code>YOUR_API_KEY</code>
          <button class="inline-copy-btn" data-copy="YOUR_API_KEY" title="Copy API key">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li>Click "Save"</li>
        <li>Close the modal</li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Select Buffer MCP Tools</h3>
      <p>Select the MCP tool you want the workflow to use from the available Buffer MCP tools, then configure it as needed.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with n8n:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>When a new RSS feed item appears, automatically create a draft post in Buffer with the article title and link</span>
    <button class="inline-copy-btn" data-copy="When a new RSS feed item appears, automatically create a draft post in Buffer with the article title and link" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Every Friday, pull my scheduled posts in Buffer for the next week and send a summary to Slack</span>
    <button class="inline-copy-btn" data-copy="Every Friday, pull my scheduled posts in Buffer for the next week and send a summary to Slack" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>When a form submission comes in, create a draft post in Buffer using the submitted content</span>
    <button class="inline-copy-btn" data-copy="When a form submission comes in, create a draft post in Buffer using the submitted content" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>

### Raycast

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: #1a1a1a;">
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Raycast</div>
    <div class="integration-page-subtitle">Quick actions from your menu bar</div>
  </div>
</div>

Raycast lets you quickly access Buffer from your menu bar on macOS.

Create posts, view your queue, and manage your social media with keyboard shortcuts and quick actions.

## Setup

<div class="setup-steps" style="--step-color: #FF6363;">
  <div class="setup-step">
    <div class="setup-step-number">1</div>
    <div class="setup-step-content">
      <h3>Get Your API Key</h3>
      <p>You need an API key to integrate Buffer with Raycast.</p>
      <div class="setup-callout">
        <div class="setup-callout-header">
          <span>API Key</span>
          <a href="https://publish.buffer.com/settings/api" class="setup-callout-action" target="_blank" rel="noopener noreferrer">Get API Key &rarr;</a>
        </div>
        <div class="setup-callout-body">
          <div class="setup-key-input-group">
            <input type="text" class="setup-key-input" placeholder="Paste your API key here" autocomplete="off" spellcheck="false" />
            <button class="setup-key-clear-btn" title="Clear API key">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
          <p class="setup-key-hint">Your key is shared with the API Explorer and will prefill the configuration steps below.</p>
        </div>
      </div>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">2</div>
    <div class="setup-step-content">
      <h3>Open Install Server</h3>
      <p>In Raycast, search for "Install Server" and press Enter.</p>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">3</div>
    <div class="setup-step-content">
      <h3>Configure the Server</h3>
      <p>Fill in the form with the following details:</p>
      <ul class="setup-settings-list">
        <li><span>Name:</span> Buffer</li>
        <li><span>Transport:</span> HTTP</li>
        <li>
          <span>URL:</span>
          <code>https://mcp.buffer.com/mcp</code>
          <button class="inline-copy-btn" data-copy="https://mcp.buffer.com/mcp" title="Copy URL">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">4</div>
    <div class="setup-step-content">
      <h3>Add Authorization Header</h3>
      <p>In HTTP Headers, click on "Add Item" and enter:</p>
      <ul class="setup-settings-list">
        <li>
          <span>Key:</span>
          <code>Authorization</code>
          <button class="inline-copy-btn" data-copy="Authorization" title="Copy key">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
        <li>
          <span>Value:</span>
          <code>Bearer YOUR_API_KEY</code>
          <button class="inline-copy-btn" data-copy="Bearer YOUR_API_KEY" title="Copy value">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          </button>
        </li>
      </ul>
    </div>
  </div>
  <div class="setup-step">
    <div class="setup-step-number">5</div>
    <div class="setup-step-content">
      <h3>Install the Server</h3>
      <p>Click on "Install" (or press Cmd+Enter) to complete the setup.</p>
    </div>
  </div>
</div>

## Try It Out

Copy any of these example prompts to get started with Raycast:

<div class="prompt-cards">
  <div class="prompt-card">
    <span>Add a post saying 'Just shipped a new feature! Stay tuned for details.' to my Buffer queue</span>
    <button class="inline-copy-btn" data-copy="Add a post saying 'Just shipped a new feature! Stay tuned for details.' to my Buffer queue" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Show me my upcoming scheduled Buffer posts for this week</span>
    <button class="inline-copy-btn" data-copy="Show me my upcoming scheduled Buffer posts for this week" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
  <div class="prompt-card">
    <span>Create a draft post in Buffer for each of my connected channels with the text 'Happy Monday! What are you working on this week?'</span>
    <button class="inline-copy-btn" data-copy="Create a draft post in Buffer for each of my connected channels with the text 'Happy Monday! What are you working on this week?'" title="Copy prompt">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
    </button>
  </div>
</div>

### ChatGPT

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/chatgpt-BkqmL2Ui.png" alt="ChatGPT" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">ChatGPT</div>
    <div class="integration-page-subtitle">Create and manage social content through conversation</div>
  </div>
</div>

Use ChatGPT to create and manage your Buffer content with natural language. This integration is currently in development.

## Coming Soon

We're building a native ChatGPT integration that will let you:

- Draft and schedule posts through conversation
- Get AI-powered content suggestions tailored to your audience
- Manage your Buffer queue directly from ChatGPT

<a href="https://buffersurvey.typeform.com/to/ff0kQonB" class="integration-cta-btn" target="_blank" rel="noopener noreferrer">Get early access &rarr;</a>

### Perplexity

<a href="../integrations.html" class="integration-back-link"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"/></svg>Integrations</a>
<div class="integration-page-header">
  <div class="integration-page-icon" style="background-color: transparent; overflow: hidden;">
    <img src="https://static.buffer.com/publish/perplexity-6Nmqf2ts.png" alt="Perplexity" style="width: 100%; height: 100%; object-fit: cover; border-radius: var(--radius-sm);" />
  </div>
  <div class="integration-page-info">
    <div class="integration-page-title">Perplexity</div>
    <div class="integration-page-subtitle">Research-driven social content</div>
  </div>
</div>

Use Perplexity AI to research trending topics and create timely Buffer posts backed by real-time data. This integration is currently in development.

## Coming Soon

We're building a Perplexity integration that will let you:

- Research trending topics and turn insights into social posts
- Generate data-backed content with cited sources
- Schedule research-driven content directly to Buffer

<a href="https://buffersurvey.typeform.com/to/wFc1U7v2" class="integration-cta-btn" target="_blank" rel="noopener noreferrer">Get early access &rarr;</a>

## Examples

### Create Idea

Create an idea post for a specified Organization, using the provided content.

```graphql
mutation CreateIdea {
  createIdea(input: {
    organizationId: "some_organization_id",
    content: {
      title: "New Idea from GraphQL API"
      text: "This is the text of the new idea created via the GraphQL API."
    }
  }) {
    ... on Idea {
      id
      content {
        title
        text
      }
    }
  }
}
```

### Create Image Post

Creating a post with an image works in the same way as creating a text post, with the addition of the imageUrl argument. This argument is used to specify the URL of the image that you want to include in the post.
```graphql
mutation CreatePost {
  createPost(input: {
    text: "Hello there, this is another one!",
    channelId: "some_channel_id",
    schedulingType: automatic,
    mode: addToQueue
    assets: {
      images:[
        {
          url:"https://images.unsplash.com/photo-1742850541164-8eb59ecb3282?q=80&w=3388&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        }
      ]
    }
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          id
          mimeType
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

### Create Scheduled Post

Scheduled posts can be created using the createPost mutation with the `customScheduled` mode and a `dueAt` timestamp. When creating a scheduled post, there are several required arguments:

- The channel ID that the post is being created for

- The scheduling type to be used for the post (automatic or notification)

- The sharing mode set to `customScheduled` to schedule the post for a specific time

- The `dueAt` timestamp for when the post should be published

- The text to be used when creating the Post

When performing the mutation, the PostActionSuccess type can be used to retrieve the information for the Post that was created. Similarly, the MutationError will provide you with information on the error that was triggered when trying to create the post.

```graphql
mutation CreatePost {
  createPost(input: {
    text: "Hello there, this is another one!",
    channelId: "some_channel_id",
    schedulingType: automatic,
    mode: customScheduled,
    dueAt: "2026-03-26T10:28:47.545Z"
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          id
          mimeType
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

### Create Text Post

Text posts can be created using the createPost mutation. When creating a post, there are several required arguments:

- The channel ID that the post is being created for

- The scheduling type to be used for the post (automatic or notification)

- The sharing mode to be used for the post (add the post to the queue, share it now or share it next)

- The text to be used when creating the Post

When performing the mutation, the PostActionSuccess type can be used to retrieve the information for the Post that was created. Similarly, the MutationError will provide you with information on the error that was triggered when trying to create the post.

```graphql
mutation CreatePost {
  createPost(input: {
    text: "Hello there, this is another one!",
    channelId: "some_channel_id",
    schedulingType: automatic,
    mode: addToQueue
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          id
          mimeType
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```

### Get Channel

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

### Get Channels

Fetch all channels for the provided Organization ID.

```graphql
query GetChannels {
  channels(input: {
    organizationId: "some_organization_id"
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

### Get Filtered Channels

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

### Get Organizations

Fetch all of the organizations that belong to the authenticated account.

```graphql
query GetOrganizations {
  account {
    organizations {
      id
      name
      ownerEmail
    }
  }
}
```

### Get Paginated Posts

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

### Get Posts For Channels

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

### Get Posts With Assets

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

### Get Scheduled Posts

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

## API Reference

### Queries

#### account

Retrieves the authenticated user's account information

**Returns:** `Account!`

#### channel

Fetches a single channel using the provided ID

**Returns:** `Channel!`

**Arguments:**
- `input`: `ChannelInput!` - Query's input.

#### channels

Fetch all channels for the organization taking into account the current's user permissions

**Returns:** `[Channel!]!`

**Arguments:**
- `input`: `ChannelsInput!` - Query's input.

#### dailyPostingLimits

Returns daily posting limit status for the given channels on the specified date.

**Returns:** `[DailyPostingLimitStatus!]!`

**Arguments:**
- `input`: `DailyPostingLimitsInput!` - Query's input.

#### post

Fetches a post by PostID for the given organization: first and last can be set for forward pagination using Relay convention

**Returns:** `Post!`

**Arguments:**
- `input`: `PostInput!` - Query's input.

#### posts

Fetches posts for the given organization: first and last can be set for forward pagination using Relay convention

**Returns:** `PostsResults!`

**Arguments:**
- `input`: `PostsInput!` - Query's input.
- `first`: `Int` - The number of posts to return
- `after`: `String` - The cursor of the post to start fetching from

### Mutations

#### createIdea

Create a new idea with the given content and metadata

**Returns:** `CreateIdeaPayload!`

**Arguments:**
- `input`: `CreateIdeaInput!` - Input to create an idea

#### createPost

Create post for channel

**Returns:** `PostActionPayload!`

**Arguments:**
- `input`: `CreatePostInput!` - The mutation's input

#### deletePost

Delete a post by id.

**Returns:** `DeletePostPayload!`

**Arguments:**
- `input`: `DeletePostInput!`

### Object Types

#### Account

Account is a representation of a Buffer user.

**Fields:**
- `id`: `ID!` - Unique identifier for the account
- `email`: `String!` - Primary email address for the account
- `backupEmail`: `String` - Backup email address for account recovery
- `avatar`: `String!` - URL to the account's avatar image
- `createdAt`: `DateTime` - Date the account was created in the Core DB. For older customers, it's possible a Publish account existed in the Publish DB for this customer before this date
- `organizations`: `[Organization!]!`
  - Arg `filter`: `OrganizationFilterInput`
- `timezone`: `String` - The account-level timezone - this is used as a default input for streaks, posting plans, and new channel channel connections.
- `name`: `String` - The account name, different from the organization name
- `preferences`: `Preferences` - The accounts preferences
- `connectedApps`: `[ConnectedApp!]` - The connected apps for the account

#### Annotation

Annotation representing all the entities in the text

**Fields:**
- `type`: `AnnotationType!` - The type of the annotation
- `indices`: `[Int!]!` - The indices of the annotation in the text
- `content`: `String!` - The content of the annotation. Annotations can sometimes be different from the actual text content.
E.g., Mastodon mentions have 'text: @buffer', but includes the server name in the content, 'content: @buffer@threads.net'
- `text`: `String!` - The text representation of the annotation, eg '@buffer'
- `url`: `String!` - The URL the annotation points to

#### Author

Represent the author of a post or note.

**Fields:**
- `id`: `AccountId!` - The unique identifier of the author.
- `email`: `String!` - The email address of the author.
- `avatar`: `String!` - The avatar URL of the author.
- `isDeleted`: `Boolean!` - Indicates whether the author is a deleted.
- `name`: `String` - The name of the author. Null if the user has not yet set a name.

#### BlueskyMetadata

Bluesky metadata

**Fields:**
- `serverUrl`: `String!` - The instance of bluesky of the channel

#### BlueskyPostMetadata

Bluesky post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts
- `linkAttachment`: `LinkAttachment` - Link attachment

#### Channel

Channel entity

**Fields:**
- `id`: `ChannelId!` - The ID of the channel
Source: mapper from channel collection - channel._id
Defined in: both proposals
- `allowedActions`: `[ChannelAction!]!` - The allowed actions for the current user
Source: field resolver
Defined in: new proposal
- `scopes`: `[String]!` - Scopes requested for a given channel - empty array if we don't have them tracked
Source: mapper from channel collection - channel.credentials.scopes
Defined in: current implementation
- `avatar`: `String!` - The avatar URL of the channel
Source: mapper from channel collection - channel.avatar
Defined in: both proposals
- `createdAt`: `DateTime!` - The creation date of the channel
Source: mapper from channel collection - channel.createdAt
Defined in: both proposals
- `descriptor`: `String!` - Formatted name of the channel service and type: e.g. 'Twitter Profile' or 'Facebook Page'
Source: mapper from channel collection - channel.service and channel.type
Defined in: current implementation
- `displayName`: `String` - The display name of the channel - nullable (reason?)
Source: mapper from channel collection - channel.displayName
Defined in: current implementation
- `isDisconnected`: `Boolean!` - Indicates if the channel is properly connected to Buffer
Source: mapper from channel collection - channel.credentials.invalid
Defined in: both proposals
- `isLocked`: `Boolean!` - Indicates if the channel is locked - Locked channels can't be used for posting.
A channel can be locked when the organization downgrades and reduces the channel quantity of their plan.
Source: mapper from channel collection - channel.isLocked
Defined in: both proposals
- `isNew`: `Boolean!` - Indicates if the channel was recently created (in less than 10 seconds). This is used to determine the redirect modal after channel authorization
Source: mapper from channel collection - channel.createdAt comparison with current time
Defined in: current implementation
- `postingSchedule`: `[ScheduleV2!]!` - Provides the posting slots for each day of the week
Source: field resolver based on profiles collection - getPostingSchedule
- `isQueuePaused`: `Boolean!` - Indicates is the queue is paused for the channel. A paused queue means schedules posts won't be published.
Source: Field resolver - From profiles collection - profile.paused
Defined in: new proposal
- `showTrendingTopicSuggestions`: `Boolean!` - Indicates if trending topic suggestions should be shown in the composer.
When false, users can still access trends via the trending icon button.
Defaults to true for backward compatibility.
Source: Field resolver - From profiles collection - profile.show_trending_topic_suggestions
- `metadata`: `ChannelMetadata` - Metadata or settings depending on the service type - such as the server URL for Mastodon or Location data for Facebook/GPB
Source: Field resolver - From channel collection: channel.locationData + channel.serverURL | profile collection: profile.default_to_reminder
Defined in: new proposal
- `name`: `String!` - The name of the channel - the handle name, username, etc.
Source: mapper from channel collection - channel.name
Defined in: both proposals
- `organizationId`: `OrganizationId!` - The organization ID of the channel
Source: mapper from channel collection - channel.organizationId
Defined in: both proposals
- `products`: `[Product!]` - Products that support a given channel
- `service`: `Service!` - Represents the social network
Source: mapper from channel collection - channel.serviceType
Defined in: both proposals
- `serviceId`: `String!` - Represents the external ID of the channel on social network API
Source: mapper from channel collection - channel.serviceId
Defined in: both proposals
- `timezone`: `String!` - The timezone of the channel - Default if not set is Europe/London
Source: field resolver based on profiles collection - timezone
Defined in: both proposals
- `type`: `ChannelType!` - The type of the channel - Page, Profile, Business, Group, Account, etc.
Source: mapper from channel collection - channel.type
Defined in: both proposals
- `updatedAt`: `DateTime!` - The last time the channel was updated
Source: mapper from channel collection - channel.updatedAt
Defined in: both proposals
- `hasActiveMemberDevice`: `Boolean!` - Whether at least one member of the orginization who have access to this channel
also has a user device registered for push notifications
- `postingGoal`: `PostingGoal` - The posting goal for the channel
- `externalLink`: `String` - The channel's URL on the social network (e.g. instagram.com/username or facebook.com/page)
Source: field resolver
Returns null if the channel is not supported
- `linkShortening`: `ChannelLinkShortening!` - Link Shortening settings for the channel
- `weeklyPostingLimit`: `WeeklyPostingLimit` - Weekly posting limit for the channel *(Deprecated: This field is not used anymore)*

#### ChannelLinkShortening

Settings for link shortening

**Fields:**
- `config`: `LinkShorteningConfig` - Configuration of link shortening integration. Null if disabled.
- `isEnabled`: `Boolean!` - If link shortening is enabled for the channel

#### ConnectedApp

Connected App

**Fields:**
- `clientId`: `ID!` - The id of the connectedApp.
- `userId`: `ID!` - The id of the user that has granted access to the app.
- `name`: `String!` - The name of the connected app.
- `description`: `String!` - A brief description of the connected app.
- `website`: `String!` - The website URL of the connected app.
- `createdAt`: `DateTime!` - The date and time when the connected app was created.

#### DailyPostingLimitStatus

Status of daily posting limits for a channel on a given day.

**Fields:**
- `channelId`: `ChannelId!` - The channel ID this status refers to.
- `sent`: `Int!` - Number of posts already sent on this day.
- `scheduled`: `Int!` - Number of posts scheduled for this day.
- `limit`: `Int` - The network daily posting limit. Null means unlimited.
- `isAtLimit`: `Boolean!` - Whether the channel has reached its daily posting limit.

#### DeletePostSuccess

deletePost success response returns the post id that was deleted.

**Fields:**
- `id`: `PostId!` - Post id that was delete.

#### DocumentAsset

Document asset

**Implements:** Asset

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset
- `document`: `DocumentMetadata!` - Document specific metadata

#### DocumentMetadata

Document metadata

**Fields:**
- `filesize`: `Int` - Document fileSize in bytes
- `numPages`: `Int!` - Number of pages in the document
- `thumbnails`: `[String!]!` - URLs to the static thumbnails of the document pages

#### FacebookMetadata

Facebook metadata

**Fields:**
- `locationData`: `LocationData` - Metadata about the location of the business associated with the channel. Only available for Facebook and GPB

#### FacebookPostMetadata

Facebook post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `linkAttachment`: `LinkAttachment` - Link attachment
- `title`: `String` - Title of Facebook reel
- `firstComment`: `String` - Facebook post's first comment

#### GoogleBusinessEventMetaData

Metadata for a GBP post that is an event

**Fields:**
- `title`: `String!` - Title of the event
- `startDate`: `DateTime!` - Start date of the event
- `endDate`: `DateTime!` - End date of the event
- `startTime`: `String` - Start time of the event *(Deprecated: get time from the startDate)*
- `endTime`: `String` - End time of the event *(Deprecated: get time from the endDate)*
- `isFullDayEvent`: `Boolean!` - Indicate whether the event has a start or end time.
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### GoogleBusinessMetadata

Google Business metadata

**Fields:**
- `locationData`: `LocationData` - Metadata about the location of the business associated with the channel. Only available for Facebook and GPB

#### GoogleBusinessOfferMetaData

Metadata for a GBP post that is an offer

**Fields:**
- `title`: `String!` - Title of the offer
- `startDate`: `DateTime!` - Start date of the offer
- `endDate`: `DateTime!` - End date of the offer
- `code`: `String` - Coupon code for the offer
- `link`: `String` - Link to the offer
- `terms`: `String` - Terms and Conditions

#### GoogleBusinessPostMetadata

Google Business Profile post metadata
@deprecated: pending proposal for specific GBP post types: update, offer and event metadata types

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `title`: `String` - Title if available in the given GBP post type: event and offer
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `details`: `GoogleBusinessPostDetails` - Details of the metadata

#### GoogleBusinessWhatsNewMetaData

Metadata for a GBP post of type Whats new

**Fields:**
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### Idea

Ideas are the main entity in the create space

**Fields:**
- `id`: `ID!` - Unique identifier for the idea
- `organizationId`: `ID!` - ID of the organization that owns this idea
- `content`: `IdeaContent!` - The actual content and metadata of the idea
- `groupId`: `ID` - ID of the group this idea belongs to (if any)
- `position`: `Float` - Numerical position for ordering within a group
- `createdAt`: `Int!` - Unix timestamp of when the idea was created
- `updatedAt`: `Int!` - Unix timestamp of when the idea was last modified

#### IdeaContent

Content of an idea

**Fields:**
- `title`: `String` - Title or headline of the idea
- `text`: `String` - Main body text or description of the idea
- `media`: `[IdeaMedia!]` - List of media items attached to the idea
- `tags`: `[PublishingTag!]!` - Tags used to categorize and organize the idea
- `aiAssisted`: `Boolean!` - Indicates whether AI tools were used in creating this idea
- `services`: `[Service!]!` - Services tagged by the user - this is typically used to annotate ideas with their target services
- `date`: `DateTime` - DateTime set by user associated with the idea - this often reflects a target publish date.

#### IdeaMedia

Media attached to an idea

**Fields:**
- `id`: `ID!` - Unique identifier for the media in Buffer's upload system
- `url`: `String!` - Direct URL to access the media file
- `alt`: `String` - Alternative text description for accessibility
- `thumbnailUrl`: `String` - URL to a smaller version of the media for preview purposes
- `type`: `MediaType!` - Type of media (e.g., image, video, gif)
- `size`: `Int` - File size in bytes
- `source`: `IdeaMediaSource` - Source platform information for the media

#### IdeaMediaSource

Media source for the idea, e.g. Unsplash, Gifphy, etc.

**Fields:**
- `name`: `String!` - Name of the media source platform (e.g., 'Unsplash', 'Giphy')
- `id`: `String` - Unique identifier from the source platform
- `author`: `String` - Name of the content creator/author
- `authorUrl`: `String` - URL to the author's profile on the source platform

#### IdeaResponse

createIdea response type

**Fields:**
- `idea`: `Idea` - The affected idea
- `refreshIdeas`: `Boolean!` - If true, the client should refresh the ideas list because other ideas might have been moved

#### ImageAsset

Image asset

**Implements:** Asset

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset
- `image`: `ImageMetadata!` - Image specific metadata

#### ImageMetadata

Image metadata

**Fields:**
- `altText`: `String!` - Alternative text for accessibility
- `width`: `Int!` - Image width in pixels
- `height`: `Int!` - Image height in pixels
- `isAnimated`: `Boolean!` - Is the image animated?
- `animatedThumbnail`: `String` - Animated thumbnail URL
- `userTags`: `[UserTag!]` - User tags in the image

#### InstagramGeolocation

Instagram Geolocation

**Fields:**
- `id`: `String` - The id of this location
- `text`: `String` - The name of this location

#### InstagramMetadata

Instagram metadata

**Fields:**
- `defaultToReminders`: `Boolean!` - Indicates if we should default to reminder for Instagram
Source: field resolver: profile.default_to_reminders

#### InstagramPostMetadata

Instagram post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `firstComment`: `String` - Instagram post's first comment
- `link`: `String` - Shop Grid link for the post
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `geolocation`: `InstagramGeolocation` - Geolocation of the post
- `shouldShareToFeed`: `Boolean!` - Indicates whether post should be shared to feed
- `stickerFields`: `InstagramStickerFields` - Sticker fields for reminder-based publishing

#### InstagramStickerFields

Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user
is prompted to copy and paste these fields into the Instagram app to complete the post.

**Fields:**
- `text`: `String` - Text for the Story or Reel
- `music`: `String` - Placeholder text for the post's music
- `products`: `String` - Placeholder text for the post's linked products
- `topics`: `String` - Placeholder text for the post's topics (Reels only)
- `other`: `String` - Additional field for any other post content

#### InvalidInputError

Error returned when the input is invalid

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### LimitReachedError

Error returned when the limit is reached

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### LinkAttachment

Link attachment

**Implements:** ScrapedLink

**Fields:**
- `url`: `String!` - URL that the link asset has been built from
- `expandedUrl`: `String` - Full URL that the link asset has been built from
- `text`: `String!` - Description for the scraped link
- `thumbnails`: `[String!]!` - Thumbnails of media available in the link
- `thumbnail`: `String` - Selected thumbnail for this link preview
- `title`: `String!` - Title for the link attachment

#### LinkedInMetadata

LinkedIn metadata

**Fields:**
- `shouldShowLinkedinAnalyticsRefreshBanner`: `Boolean!` - Property parsed from scopes indicating whether the client should show the LinkedIn analytics refresh banner

#### LinkedInPostMetadata

LinkedIn post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `firstComment`: `String` - LinkedIn post's first comment
- `linkAttachment`: `LinkAttachment` - Link attachment

#### LinkShorteningConfig

Link Shortening Configuration

**Fields:**
- `domain`: `String!` - Domain of the link shortener - eg buff.ly, dub.co,
or the user's custom domain.
- `name`: `String!` - Human readable string to describe the link shortening
service.

#### LocationData

Location data about the channel

**Fields:**
- `location`: `String` - Location of the business associated with the channel
- `mapsLink`: `String` - Link to the map
- `googleAccountId`: `String` - Google Account Id of the business

#### MastodonMetadata

Mastodon metadata

**Fields:**
- `serverUrl`: `String!` - The instance of mastodon of the channel

#### MastodonPostMetadata

Mastodon post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts
- `spoilerText`: `String` - Spoiler text hiding the root text of this post

#### MemberConnection

Represents the members connection edge. Later, we can add the list of members with the page info to follow our connection edge pattern.

**Fields:**
- `totalCount`: `Int!` - The total count of team members counting the org owner and team members from the Publish DB.

#### Note

Note entity

**Fields:**
- `id`: `NoteId!` - The unique identifier of the note.
- `text`: `String!` - The content of the note.
- `type`: `NoteType!` - The type of the note.
- `author`: `Author!` - The author of the note - null if the user is deleted or left the organization.
- `createdAt`: `DateTime!` - The date and time when the note was created.
- `updatedAt`: `DateTime` - The date and time when the note was last edited.
- `allowedActions`: `[NoteAction!]!` - The allowed actions a user can perform on the note.

#### NotFoundError

Error returned when the resource is not found

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### Organization

Organization is a representation of a Buffer Organization.

**Fields:**
- `id`: `OrganizationId!` - The ID of the organization.
- `channelCount`: `Int!` - The total number of channels connected to the organization.
- `limits`: `OrganizationLimits!` - The limits of the organization. Can be used to check if the organization has reached the limit of channels, members, etc.
- `members`: `MemberConnection!` - The members of the organization. Can be used to check the total number of members in the organization. In the future, it might contain more information about the members.
- `name`: `String!` - The name of the organization.
- `ownerEmail`: `String!` - The owner email of the organization.

#### OrganizationLimits

Resource limits for an organization including channels, members, and content limits

**Fields:**
- `channels`: `Int!`
- `members`: `Int!`
- `scheduledPosts`: `Int!`
- `scheduledThreadsPerChannel`: `Int!`
- `scheduledStoriesPerChannel`: `Int!`
- `generateContent`: `Int!`
- `tags`: `Int!`
- `ideas`: `Int!`
- `ideaGroups`: `Int!`
- `savedReplies`: `Int!`

#### PaginationPageInfo

Information to aid in pagination.

**Fields:**
- `startCursor`: `String` - The first cursor in the list. It can be used to fetch the previous page.
- `endCursor`: `String` - The last cursor in the list. It can be used to fetch the next page.
- `hasPreviousPage`: `Boolean!` - When set to true, it means there is a previous page available. Will always return false for now as we only support forward pagination.
- `hasNextPage`: `Boolean!` - When set to true, it means there is a next page available.

#### PinterestBoard

A Pinterest board

**Fields:**
- `id`: `String!` - The ID of the board
- `serviceId`: `String!` - The ID of the service
- `name`: `String!` - The board name
- `url`: `String!` - The board URL
- `description`: `String` - The board description
- `avatar`: `String` - The board avatar

#### PinterestMetadata

Pinterest metadata

**Fields:**
- `boards`: `[PinterestBoard!]!` - The list of boards the user has on Pinterest

#### PinterestPostMetadata

Pinterest post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `title`: `String` - The title of the Pin
- `url`: `String` - The Pin destination link
- `board`: `PinterestBoard` - The board the Pin is saved to
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text

#### Post

Post entity

**Fields:**
- `id`: `PostId!` - ObjectId of the post
- `ideaId`: `IdeaId` - Is set when the Post is generated from an Idea
- `status`: `PostStatus!` - status
- `via`: `PostVia!` - Indicates if the post is created from Buffer or the API
- `schedulingType`: `SchedulingType` - Scheduling type can be null if the post was created natively on the social network without using notification publishing or automatic publishing
- `author`: `Author` - Represents the user who created the post
- `isCustomScheduled`: `Boolean!` - Indicates whether time to publish was manually selected by the user
- `createdAt`: `DateTime!` - Date when the post was created
- `updatedAt`: `DateTime!` - Date when the post was updated
- `dueAt`: `DateTime` - Date when the post is scheduled to be published
- `sentAt`: `DateTime` - Date when the post is published
- `text`: `String!` - Text content of the Post
- `externalLink`: `String` - The external URL of the post at the destination service
- `metadata`: `PostMetadata` - Metadata of the post which differs based on the social network/service
@see post.metadata.graphql
- `channelId`: `ChannelId!` - channel ID (faster than resolving the channnel.id)
- `channelService`: `Service!` - channel service (faster than resolving the channnel.service)
- `channel`: `Channel!` - channel
- `tags`: `[Tag!]!` - tags - sorted by name in ascending order
- `notes`: `[Note!]!` - notes
- `notificationStatus`: `NotificationStatus` - notificationStatus: notified or markedAsPublished
- `error`: `PostPublishingError` - error
- `assets`: `[Asset!]!` - assets
- `allowedActions`: `[PostAction!]!` - Indicates what actions the current account can perform on the post
- `sharedNow`: `Boolean!` - Indicates whether the post was shared via publish now action
- `shareMode`: `ShareMode!` - Indicates the share mode of the post (e.g., addToQueue, shareNext, shareNow, customScheduled)

#### PostActionSuccess

Success response returns the full up-to-date post from after the action was performed.

**Fields:**
- `post`: `Post!` - Post on which the action was successfully performed.

#### PostingGoal

Represents a posting goal for a channel, including target, progress, and status information.

**Fields:**
- `goal`: `Int!` - The target number of posts for this goal.
- `sentCount`: `Int!` - The number of posts that have been sent (published or ingested) for this goal.
- `scheduledCount`: `Int!` - The number of posts that are scheduled to be sent for this goal.
- `status`: `PostingGoalStatus!` - The current status of the posting goal.
- `periodStart`: `DateTime!` - The start date of the period for this posting goal.
- `periodEnd`: `DateTime!` - The end date of the period for this posting goal.

#### PostPublishingError

Post publishing error

**Fields:**
- `message`: `String!` - Error message to display
- `supportUrl`: `String` - Link to a help center article to help resolve the error
- `rawError`: `String` - The original error from the publishing service (internal use only)

#### PostsEdge

Represent a node in the pagination result using the Connect Relay convention.

**Fields:**
- `node`: `Post!` - Represents the current post in the list.
- `cursor`: `String!` - Opaque cursor to be used in pagination to fetch from current node.

#### PostsResults

Results for the posts query.

**Fields:**
- `edges`: `[PostsEdge!]` - The list of posts that match the query.
- `pageInfo`: `PaginationPageInfo!` - Information to aid in pagination.

#### Preferences

Account preferences

**Fields:**
- `timeFormat`: `String`
- `startOfWeek`: `String`
- `defaultScheduleOption`: `ScheduleOption!`

#### PublishingTag

Tag associated with a post

**Fields:**
- `id`: `ID!`
- `color`: `String!` - Hex color for tag e.g #F523F1
- `name`: `String!`

#### RestProxyError

Error proxied from the REST API response

**Implements:** MutationError

**Fields:**
- `message`: `String!` - An error message from the REST API response that we proxied here
- `link`: `String` - Link to our Help center from the REST API response
- `code`: `Int` - Error code from the REST API response - https://buffer.com/developers/api/errors

#### RetweetMetadata

Information about the initial Tweet that was retweeted

**Implements:** ScrapedLink

**Fields:**
- `id`: `String!` - Retweet ID
- `url`: `String!` - Link to original tweet
- `text`: `String!` - Text of the original tweet
- `createdAt`: `DateTime!` - Date when the original tweet was created
- `user`: `RetweetUserMetadata!` - User who created the original tweet
- `thumbnails`: `[String!]!` - Thumbnails to media available in the link

#### RetweetUserMetadata

Information about the initial author of the Tweet that was retweeted

**Fields:**
- `name`: `String!` - Name of the user who created the original Tweet
- `username`: `String!` - Username of the user who created the original Tweet
- `avatar`: `String!` - Avatar of the user who created the original Tweet

#### ScheduleV2

Posting schedule for a specific day of the week

**Fields:**
- `day`: `DayOfWeek!` - The day of the week: mon, tue, wed, thu, fri, sat, sun
- `times`: `[String!]!` - The times the channel is scheduled to post on the day: HH:MM
- `paused`: `Boolean!` - Indicates if this day is paused in the posting schedule.

#### StartPagePostMetadata

Start Page post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `link`: `String` - Optional link in post

#### Tag

Tag entity

**Fields:**
- `id`: `TagId!` - ObjectId of the tag
- `color`: `String!` - Hex color for tag e.g '#F523F1'
- `name`: `String!` - Name of the tag e.g 'Summer sales'
- `isLocked`: `Boolean!` - Locked tag cannot be assigned to new items in the UI.
A Tag is locked after a customer downgrades and has more tags than the free plan limit allows

#### ThreadedPost

A post authored by the user which is posted to a thread.
This is commonly used for long-format twitter and meta threads posts to
allow authored content to span multiple threads.
Threads are represented as a list of replies, each replying to the previous one.

**Fields:**
- `text`: `String!` - The text body content of the threaded post
- `assets`: `[Asset!]!` - Media assets of the threaded post
- `linkAttachment`: `LinkAttachment` - Link attachment for the threaded post

#### ThreadsPostMetadata

Threads post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts
- `linkAttachment`: `LinkAttachment` - Link attachment
- `topic`: `String` - Topic associated with the post
- `locationId`: `String` - LocationId associated with the post
- `locationName`: `String` - Location name associated with the post

#### TiktokMetadata

Tiktok metadata

**Fields:**
- `defaultToReminders`: `Boolean!` - Indicates if we should default to reminder for Tiktok
Source: field resolver: profile.default_to_reminders

#### TiktokPostMetadata

Tiktok post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `title`: `String` - The title of the TikTok post (for photo posts)

#### TwitterMetadata

Twitter metadata

**Fields:**
- `subscriptionType`: `String` - Indicates the type of subscription the user has on Twitter

#### TwitterPostMetadata

Twitter post metadata

**Implements:** CommonPostMetadata, ThreadedPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `retweet`: `RetweetMetadata` - The details of the tweet being retweeted
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts

#### UnauthorizedError

Error returned when the user is not authorized to perform the action

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### UnexpectedError

Error returned when unexpected error occurs

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### UserTag

User tag in the image

**Fields:**
- `handle`: `String!` - The handle of the user
- `x`: `Float!` - The x coordinate of the user tag
- `y`: `Float!` - The y coordinate of the user tag

#### VideoAsset

Video asset

**Implements:** Asset

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset
- `video`: `VideoMetadata!` - Video specific metadata

#### VideoMetadata

Video metadata

**Fields:**
- `durationMs`: `Int!` - Video duration in seconds
- `containerFormat`: `String` - Video container format
- `videoCodec`: `String` - Video codec
- `frameRate`: `Int` - Video framerate
- `videoBitRate`: `Int` - Video bitrate in kbps
- `audioCodec`: `String` - Audio codec
- `rotationDegree`: `Int` - Rotation degree
- `isTranscodingRequired`: `Boolean!` - Whether the video needs to be transcoded before it can be broadcasted
- `isVideoProcessing`: `Boolean!` - Whether the video is currently being processed (transcoding in progress)
- `width`: `Int!` - Video width in pixels
- `height`: `Int!` - Video height in pixels
- `fileSize`: `Int` - Video fileSize in bytes

#### VoidMutationError

Error implementation that allows clients to resolve the MutationError on mutations that do not currently have typed errors.
This allows clients to automatically handle errors that may be added to a mutation in future.

Do not directly throw this error, use a custom typed error instead

**Implements:** MutationError

**Fields:**
- `message`: `String!` - Error message

#### WeeklyPostingLimit

Weekly posting limit for a channel

**Fields:**
- `sent`: `Int!` - The number of posts the channel has sent this week
- `scheduled`: `Int!` - The number of posts the channel has scheduled for this week
- `limit`: `Int!` - The weekly posting limit for the channel

#### YoutubeCategory

**Fields:**
- `categoryId`: `String!`
- `title`: `String!`

#### YoutubeMetadata

Youtube metadata

**Fields:**
- `defaultToReminders`: `Boolean!` - Indicates if we should default to reminder for Youtube
Source: field resolver: profile.default_to_reminders

#### YoutubePostMetadata

Youtube post metadata

**Implements:** CommonPostMetadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Youtube
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text
- `title`: `String` - Title of the Youtube post
- `privacy`: `YoutubePrivacy` - Privacy setting for post
- `category`: `YoutubeCategory` - Post category
- `license`: `YoutubeLicense` - Video license
- `notifySubscribers`: `Boolean!` - Indicates whether to notify subscribers on publish video
- `embeddable`: `Boolean!` - Indicates whether the video allows embedding
- `madeForKids`: `Boolean!` - Indicates whether the video is suitable for kids

### Input Types

#### AnnotationInputFacebook

Annotation representing all the entities in the text

**Fields:**
- `content`: `String!` - The content of the annotation, e.g. '107509875938399'
- `indices`: `[Int!]!` - The indices of the annotation in the text, e.g. [6, 9] (from 6 to 9 characters in the text)
- `text`: `String!` - The text representation of the annotation, eg 'Buffer'
- `url`: `String!` - The URL the annotation points to, e.g. https://www.facebook.com/107509875938399

#### AnnotationInputLinkedIn

Annotation representing all the entities in the text

**Fields:**
- `id`: `String!` - The id of the annotation, e.g. 1521226
- `link`: `String!` - The link of the annotation, e.g. https://www.linkedin.com/company/bufferapp
- `entity`: `String!` - The entity of the annotation, e.g. urn:li:organization:1521226
- `vanityName`: `String!` - The vanity name of the annotation, e.g. bufferapp
- `localizedName`: `String!` - The localized name of the annotation, e.g. Buffer
- `start`: `Int!` - The start of the annotation, e.g. 5
- `length`: `Int!` - The length of the annotation, e.g. 6

#### AssetsInput

Asset interface with common fields

**Fields:**
- `images`: `[ImageAssetInput!]` - Images to be attached to the post
- `videos`: `[VideoAssetInput!]` - Videos to be attached to the post
- `documents`: `[DocumentAssetInput!]` - Documents to be attached to the post
- `link`: `LinkAssetInput` - Link to be attached to the post

#### BlueskyPostMetadataInput

Bluesky post metadata

**Fields:**
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)
- `linkAttachment`: `LinkAttachmentInput` - Link attachment

#### ChannelInput

Input for the channel query

**Fields:**
- `id`: `ChannelId!` - The ID of the channel to be retrieved

#### ChannelsFiltersInput

Filter to pass when fetching channels.

**Fields:**
- `isLocked`: `Boolean` - If not defined, it returns all channels
Else,
  if true, it only returns locked channels
  if false, it only returns not locked channels
- `product`: `Product` - If not passed, it return all channels
Else, it filters the channels based on what the product supports.

#### ChannelsInput

Input to pass when fetching channels.

**Fields:**
- `organizationId`: `OrganizationId!` - The Organization id to fetch channels for
- `filter`: `ChannelsFiltersInput` - A list of option filters - passing null means we don't want to filter

#### CreateIdeaInput

createIdea input type

**Fields:**
- `organizationId`: `ID!` - Organization ID that will own the idea
- `content`: `IdeaContentInput!` - Content and metadata for the new idea
- `cta`: `String` - Call-to-action identifier for analytics tracking
- `group`: `IdeaGroupInput` - Group placement (null for unassigned group)
- `templateId`: `String` - Template ID used to create the idea

#### CreatePostInput

Create post's request input.

**Fields:**
- `ideaId`: `IdeaId` - Is set when the Post is generated from an Idea
- `draftId`: `DraftId` - Is set when the Post is generated from a Draft
- `schedulingType`: `SchedulingType!` - Scheduling type to indicate notification publishing or automatic publishing
- `dueAt`: `DateTime` - Date when the post is scheduled to be published
- `text`: `String` - Text content of the Post
- `metadata`: `PostInputMetaData` - Metadata of the post which differs based on the social network/service
- `channelId`: `ChannelId!` - Channel's Id for which we want to create the post
- `tagIds`: `[TagId!]` - List of tag IDs
- `assets`: `AssetsInput` - assets
- `mode`: `ShareMode!` - How the post is being scheduled.
- `source`: `String` - source where the composer was initiated from, used for tracking.
- `aiAssisted`: `Boolean` - If this post was created with the help of AI
- `saveToDraft`: `Boolean` - If true, saves the post as a draft instead of scheduling it.
When saving as draft:
- Post status will be 'draft' instead of 'buffer'
- Posting limits are not checked
- The post will not be published until explicitly scheduled

#### DailyPostingLimitsInput

Input for the dailyPostingLimits query.

**Fields:**
- `channelIds`: `[ChannelId!]!` - List of channel IDs to check limits for. All channels must belong to the same organization.
- `date`: `DateTime` - The date to check limits for. Defaults to today if not provided.

#### DateTimeComparator

Comparator for filtering by date

**Fields:**
- `start`: `DateTime` - Include results with dates equal to or after
the specified date
- `end`: `DateTime` - Include results with dates equal to or before
the specified date

#### DeletePostInput

deletePost mutation deletes a post by id.

**Fields:**
- `id`: `PostId!` - Post id to delete.

#### DocumentAssetInput

Document asset

**Fields:**
- `url`: `String!` - Document URL
- `title`: `String!` - Document title
- `thumbnailUrl`: `String!` - Document thumbnail URL

#### FacebookPostMetadataInput

Facebook post metadata

**Fields:**
- `type`: `PostTypeFacebook!` - The channel-specific type of the post, eg, post, story, reel for Facebook
- `annotations`: `[AnnotationInputFacebook!]` - Annotations representing entities in the text
- `linkAttachment`: `LinkAttachmentInput` - Link attachment
- `firstComment`: `String` - Facebook post's first comment

#### GoogleBusinessEventMetaDataInput

Metadata for a GBP post that is an event

**Fields:**
- `title`: `String!` - Title of the event
- `startDate`: `DateTime!` - Start date of the event
- `endDate`: `DateTime!` - End date of the event
- `isFullDayEvent`: `Boolean!` - Indicate whether the event has a start or end time.
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### GoogleBusinessOfferMetaDataInput

Metadata for a GBP post that is an offer

**Fields:**
- `title`: `String!` - Title of the offer
- `startDate`: `DateTime!` - Start date of the offer
- `endDate`: `DateTime!` - End date of the offer
- `code`: `String` - Coupon code for the offer
- `link`: `String` - Link to the offer
- `terms`: `String` - Terms and Conditions

#### GoogleBusinessPostMetadataInput

Google Business Profile post metadata
@deprecated: pending proposal for specific GBP post types: update, offer and event metadata types

**Fields:**
- `type`: `PostTypeGoogleBusiness!` - The channel-specific type of the post, eg, post, offer, event for Google Business Profile
- `title`: `String` - Title if available in the given GBP post type: event and offer
- `detailsOffer`: `GoogleBusinessOfferMetaDataInput` - Details of the Offer metadata
- `detailsEvent`: `GoogleBusinessEventMetaDataInput` - Details of the Event metadata
- `detailsWhatsNew`: `GoogleBusinessWhatsNewMetaDataInput` - Details of the Whats new metadata

#### GoogleBusinessWhatsNewMetaDataInput

Metadata for a GBP post of type Whats new

**Fields:**
- `button`: `GoogleBusinessPostActionType!` - Action button
- `link`: `String` - Link to the action

#### IdeaContentInput

content input for creating/updating an idea

**Fields:**
- `title`: `String` - Title or headline of the idea
- `text`: `String` - Main body text or description
- `media`: `[IdeaMediaInput!]` - List of media items to attach
- `tags`: `[TagInput!]` - Tags to categorize the idea
- `aiAssisted`: `Boolean` - Whether AI tools were used in creation
- `services`: `[Service!]` - Services associated with the idea for targeting specific platforms
- `date`: `DateTime` - Target date for the idea, often used for planning publish schedules

#### IdeaGroupInput

idea group input for create/update

**Fields:**
- `groupId`: `ID` - Target group ID (null for unassigned group)
- `placeAfterId`: `ID` - ID of idea to place after (null for top position)

#### IdeaMediaInput

**Fields:**
- `url`: `String!` - The URL of the media
- `alt`: `String` - Alternative text for the media
- `thumbnailUrl`: `String` - Thumbnail URL for the media
- `type`: `MediaType!` - The type of media (image, gif, video, link, document, unsupported). Note: 'video' is not supported via public API
- `size`: `Int` - The size of the media in bytes
- `source`: `IdeaMediaSourceInput` - Source information for the media

#### IdeaMediaSourceInput

Input type for the source information of media attached to an idea

**Fields:**
- `name`: `String!`
- `id`: `String`
- `trigger`: `String`
- `author`: `String` - for unsplash only
- `authorUrl`: `String`

#### ImageAssetInput

Image asset

**Fields:**
- `url`: `String!` - URL to the file source
- `thumbnailUrl`: `String` - URL to the static thumbnail of the asset
- `metadata`: `ImageMetadataInput` - Image specific metadata

#### ImageDimensionsInput

Image dimensions

**Fields:**
- `width`: `Int!` - Image width in pixels
- `height`: `Int!` - Image height in pixels

#### ImageMetadataInput

Image metadata

**Fields:**
- `altText`: `String!` - Alternative text for accessibility
- `animatedThumbnail`: `String` - Animated thumbnail URL
- `userTags`: `[UserTagInput!]` - User tags in the image
- `dimensions`: `ImageDimensionsInput` - Image dimensions

#### InstagramGeolocationInput

Instagram Geolocation

**Fields:**
- `id`: `String` - The id of this location
- `text`: `String` - The name of this location

#### InstagramPostMetadataInput

Instagram post metadata

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `firstComment`: `String` - Instagram post's first comment
- `link`: `String` - Shop Grid link for the post
- `geolocation`: `InstagramGeolocationInput` - Geolocation of the post
- `shouldShareToFeed`: `Boolean!` - Indicates whether post should be shared to feed
- `stickerFields`: `InstagramStickerFieldsInput` - Sticker fields for reminder-based publishing

#### InstagramStickerFieldsInput

Instagram fields for reminder-based publishing. Upon the reminder for publishing, the user
is prompted to copy and paste these fields into the Instagram app to complete the post.

**Fields:**
- `text`: `String` - Text for the Story or Reel
- `music`: `String` - Placeholder text for the post's music
- `products`: `String` - Placeholder text for the post's linked products
- `topics`: `String` - Placeholder text for the post's topics (Reels only)
- `other`: `String` - Additional field for any other post content

#### LinkAssetInput

Link attached to the post

**Fields:**
- `url`: `String!` - URL to the link
- `title`: `String` - Title of the link
- `description`: `String` - Description of the link
- `thumbnailUrl`: `String` - Thumbnail URL of the link

#### LinkAttachmentInput

Link attachment

**Fields:**
- `url`: `String!` - URL that the link asset has been built from

#### LinkedInPostMetadataInput

LinkedIn post metadata

**Fields:**
- `annotations`: `[AnnotationInputLinkedIn!]` - Annotations representing entities in the text
- `firstComment`: `String` - LinkedIn post's first comment
- `linkAttachment`: `LinkAttachmentInput` - Link attachment

#### MastodonPostMetadataInput

Mastodon post metadata

**Fields:**
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)
- `spoilerText`: `String` - Spoiler text hiding the root text of this post

#### OrganizationFilterInput

Allow retrieving a specific Organization

**Fields:**
- `organizationId`: `String!`

#### PinterestPostMetadataInput

Pinterest post metadata

**Fields:**
- `title`: `String` - The title of the Pin
- `url`: `String` - The Pin destination link
- `boardServiceId`: `String!` - The board ID of the Pin, can be obtained when fetching the channel details with the following query:
```
query GetChannelWithSubprofiles {
  channel(input: { id: "[CHANNEL_ID_HERE]" }) {
    metadata {
      ... on PinterestMetadata {
        boards {
          serviceId
        }
      }
    }
  }
}
```

#### PostInput

Input for the post query

**Fields:**
- `id`: `PostId!` - The ID of the post to be retrieved

#### PostInputMetaData

Metadata of the post which differs based on the social network/service

**Fields:**
- `instagram`: `InstagramPostMetadataInput` - Metadata for Instagram post
- `facebook`: `FacebookPostMetadataInput` - Metadata for Facebook post
- `linkedin`: `LinkedInPostMetadataInput` - Metadata for LinkedIn post
- `twitter`: `TwitterPostMetadataInput` - Metadata for Twitter post
- `pinterest`: `PinterestPostMetadataInput` - Metadata for Pinterest post
- `google`: `GoogleBusinessPostMetadataInput` - Metadata for Google Business Profile post
- `youtube`: `YoutubePostMetadataInput` - Metadata for Youtube post
- `mastodon`: `MastodonPostMetadataInput` - Metadata for Mastodon post
- `startPage`: `StartPagePostMetadataInput` - Metadata for Start Page post
- `threads`: `ThreadsPostMetadataInput` - Metadata for Threads post
- `bluesky`: `BlueskyPostMetadataInput` - Metadata for Bluesky post
- `tiktok`: `TikTokPostMetadataInput` - Metadata for TikTok post

#### PostsFiltersInput

Filter to apply to the posts query

**Fields:**
- `channelIds`: `[ChannelId!]` - When set, it will filter posts by channel
- `startDate`: `DateTime` - When set, it will return posts with createdAt or dueAt date after startDate
- `endDate`: `DateTime` - When set, it will return posts with createdAt or dueAt date before endDate
- `status`: `[PostStatus!]` - When set, it will filter posts by status
- `tags`: `TagComparator` - Filter posts by tags. Supports specific tags, untagged posts, or union of both.
- `tagIds`: `[TagId!]` - When set, it will filter posts by tag
- `dueAt`: `DateTimeComparator` - When set, it will filter posts by their scheduled posting date
- `createdAt`: `DateTimeComparator` - When set, it will filter posts by the date they were created

#### PostsInput

Input for the posts query

**Fields:**
- `organizationId`: `OrganizationId!` - The Organization id to fetch posts for
- `filter`: `PostsFiltersInput` - The filters to apply to the posts query
- `sort`: `[PostSortInput!]` - The sort to apply to the posts results

#### PostSortInput

Sort order of post results. List multiple to create tie-breaking order.

**Fields:**
- `field`: `PostSortableKey!` - The field to sort by.
- `direction`: `SortDirection!` - The direction to sort by.

#### RetweetMetadataInput

Information about the initial Tweet that was retweeted

**Fields:**
- `id`: `String!` - Retweet ID

#### StartPagePostMetadataInput

Start Page post metadata

**Fields:**
- `link`: `String` - Optional link in post

#### TagComparator

Comparator for filtering by tags

**Fields:**
- `in`: `[TagId!]!` - Include results that have any of the specified tags (union/OR).
- `isEmpty`: `Boolean!` (default: false) - When true, include results that have no tags assigned.
Can be combined with 'in' for union filtering.
Defaults to false if not specified.

#### TagInput

Input type for tag information used in idea creation

**Fields:**
- `id`: `ID!`
- `name`: `String!`
- `color`: `String!`

#### ThreadedPostInput

A post authored by the user which is posted to a thread.
This is commonly used for long-format twitter and meta threads posts to
allow authored content to span multiple threads.
Threads are represented as a list of replies, each replying to the previous one.

**Fields:**
- `text`: `String` - The text body content of the threaded post
- `assets`: `AssetsInput` - Media assets of the threaded post

#### ThreadsPostMetadataInput

Threads post metadata

**Fields:**
- `type`: `PostType` - The type of the post
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)
- `linkAttachment`: `LinkAttachmentInput` - Link attachment
- `topic`: `String` - Topic associated with the post
- `locationId`: `String` - LocationId associated with the post
- `locationName`: `String` - Location name associated with the post

#### TikTokPostMetadataInput

TikTok post metadata

**Fields:**
- `title`: `String` - The title of the TikTok post (for photo posts)

#### TwitterPostMetadataInput

Twitter post metadata

**Fields:**
- `retweet`: `RetweetMetadataInput` - The details of the tweet being retweeted
- `thread`: `[ThreadedPostInput!]` - The list of threaded posts (not paginated)

#### UserTagInput

User tag in the image

**Fields:**
- `handle`: `String!` - The handle of the user
- `x`: `Float!` - The x coordinate of the user tag
- `y`: `Float!` - The y coordinate of the user tag

#### VideoAssetInput

Video asset

**Fields:**
- `url`: `String!` - URL to the file source
- `thumbnailUrl`: `String` - URL to the thumbnail of the video
- `metadata`: `VideoMetadataInput` - Video specific metadata

#### VideoMetadataInput

Video metadata

**Fields:**
- `thumbnailOffset`: `Int` - Offset of the thumbnail chosen for the video, in ms
- `title`: `String` - Video title

#### YoutubePostMetadataInput

Youtube post metadata

**Fields:**
- `title`: `String!` - Title of the Youtube post
- `privacy`: `YoutubePrivacy` - Privacy setting for post (default: public)
- `categoryId`: `String!` - Youtube Category ID, one ID of this list:
ID: 1 -> Film & Animation
ID: 2 -> Autos & Vehicles
ID: 10 -> Music
ID: 15 -> Pets & Animals
ID: 17 -> Sports
ID: 19 -> Travel & Events
ID: 20 -> Gaming
ID: 22 -> People & Blogs
ID: 23 -> Comedy
ID: 24 -> Entertainment
ID: 25 -> News & Politics
ID: 26 -> Howto & Style
ID: 27 -> Education
ID: 28 -> Science & Technology
ID: 29 -> Nonprofits & Activism
- `license`: `YoutubeLicense` - Video license (default: youtube)
- `notifySubscribers`: `Boolean` - Indicates whether to notify subscribers on publish video (default: true)
- `embeddable`: `Boolean` - Indicates whether the video allows embedding (default: true)
- `madeForKids`: `Boolean` - Indicates whether the video is suitable for kids (default: false)

### Interfaces

#### Asset

Asset interface with common fields

**Fields:**
- `id`: `ID` - The ID of the asset in the database
- `type`: `AssetType!` - The type of the asset
- `mimeType`: `String!` - The MIME type of the asset
- `source`: `String!` - URL to the file source
- `thumbnail`: `String!` - URL to the static thumbnail of the asset

#### CommonPostMetadata

Common properties for all post metadata types

**Fields:**
- `type`: `PostType!` - The channel-specific type of the post, eg, post, story, reel for Instagram
- `annotations`: `[Annotation!]!` - Annotations representing entities in the text

#### MutationError

Base Mutation Error type

**Fields:**
- `message`: `String!` - Error message

#### ScrapedLink

Link data for link preview

**Fields:**
- `url`: `String!` - URL that the link asset has been built from
- `text`: `String!` - Description for the scraped link
- `thumbnails`: `[String!]!` - Thumbnails of media available in the link

#### ThreadedPostMetadata

Common properties for all posts that support threaded replies.
See ThreadedPost for more details.

**Fields:**
- `thread`: `[ThreadedPost!]!` - The list of threaded posts (not paginated)
- `threadCount`: `Int!` - The number of threaded posts

### Unions

#### ChannelMetadata

Metadata or settings about the channel depending on the service type

**Possible types:** InstagramMetadata | TiktokMetadata | YoutubeMetadata | PinterestMetadata | MastodonMetadata | BlueskyMetadata | GoogleBusinessMetadata | FacebookMetadata | TwitterMetadata | LinkedInMetadata

#### CreateIdeaPayload

createIdea response (including errors)

**Possible types:** Idea | IdeaResponse | InvalidInputError | UnauthorizedError | UnexpectedError | LimitReachedError

#### DeletePostPayload

All possible response types for the deletePost mutation.

**Possible types:** DeletePostSuccess | VoidMutationError

#### GoogleBusinessPostDetails

GoogleBusiness Metadata details

**Possible types:** GoogleBusinessWhatsNewMetaData | GoogleBusinessOfferMetaData | GoogleBusinessEventMetaData

#### PostActionPayload

Create post's request response payload.

**Possible types:** PostActionSuccess | NotFoundError | UnauthorizedError | UnexpectedError | RestProxyError | LimitReachedError | InvalidInputError

#### PostMetadata

Post metadata union type. Contains all possible types of post metadata.

**Possible types:** InstagramPostMetadata | FacebookPostMetadata | LinkedInPostMetadata | TwitterPostMetadata | PinterestPostMetadata | GoogleBusinessPostMetadata | YoutubePostMetadata | MastodonPostMetadata | StartPagePostMetadata | TiktokPostMetadata | ThreadsPostMetadata | BlueskyPostMetadata

### Enums

#### AnnotationType

List of possible types for an annotation

**Values:**
- `hashtag`
- `mention`
- `url`
- `annotation`
- `cashtag`

#### AssetType

Asset types

**Values:**
- `image`
- `video`
- `document`

#### ChannelAction

List of possible actions that can be performed on a Channel

**Values:**
- `publishStartPage`

#### ChannelType

Channel is a representation of a social media account or page that can be connected to Buffer.

**Values:**
- `page`
- `profile`
- `business`
- `group`
- `account`
- `channel`

#### DayOfWeek

**Values:**
- `mon`
- `tue`
- `wed`
- `thu`
- `fri`
- `sat`
- `sun`

#### GoogleBusinessPostActionType

List of possible types for GBP cta

**Values:**
- `none`
- `book`
- `order`
- `shop`
- `learn_more`
- `signup`
- `call`

#### MediaType

The type of media attached to a post

**Values:**
- `image`
- `gif`
- `video`
- `link`
- `document`
- `unsupported`

#### NoteAction

List of possible actions that can be performed on a note

**Values:**
- `updateNote` - The user can update the note.
- `deleteNote` - The user can delete the note.

#### NoteType

The type of a note.

**Values:**
- `userGenerated` - A note that was manually written by a user.
- `bufferGenerated` - A note that was generated by our internal system. Can be used for approval flows notifications or other automated processes.
- `aiGenerated` - A note that was generated by our AI system.

#### NotificationStatus

List of possible statuses for a notification

**Values:**
- `notified`
- `markedAsPublished`

#### OrganizationAction

List of possible actions that can be performed on a Organization

**Values:**
- `view`
- `edit`
- `manageBilling`
- `manageTeamMembers`
- `publishStartPages`
- `manageAllNotes`
- `manageChannels`
- `transferOwnership`
- `receiveOrganizationOwnership`

#### PostAction

List of possible actions that can be performed on a Post

**Values:**
- `updatePost`
- `deletePost`
- `viewPost`
- `sharePostLink`
- `copyPostLink`
- `movePostToDraft`
- `publishPostNow`
- `publishPostNext`
- `addPostToQueue`
- `updatePostSchedule`
- `removePostScheduledTime`
- `requestPostApproval`
- `revertPostApprovalRequest`
- `approvePost`
- `rejectPost`
- `duplicatePost`
- `updatePostTags`
- `addPostNote`
- `updateShopGridLink`
- `createPostRecurrence`
- `editPostRecurrence`
- `cancelPostRecurrence`

#### PostingGoalStatus

PostingGoalStatus is used to track the status of a posting goal.

**Values:**
- `OnTrack`
- `AtRisk`
- `Hit`

#### PostSortableKey

Key of collection to use for sorting

**Values:**
- `dueAt` - Sort by the post's dueAt field.
Due at is the date when the post is scheduled to be published.
- `createdAt` - Sort by the post's createdAt field.
Created at is the date when the post was created.

#### PostStatus

List of possible statuses for a Post

**Values:**
- `draft`
- `needs_approval`
- `scheduled`
- `sending`
- `sent`
- `error`

#### PostType

List of possible types for a Post. Some services may have different types (e.g., Instagram has story, reel, post but Twitter has only post)

**Values:**
- `post`
- `reel`
- `story`
- `short`
- `whats_new`
- `offer`
- `event`
- `carousel`
- `ghost_post`
- `thread`

#### PostTypeFacebook

List of specific post types available for Facebook

**Values:**
- `post`
- `story`
- `reel`

#### PostTypeGoogleBusiness

List of specific post types available for Google Business profiles

**Values:**
- `event`
- `whats_new`
- `offer`

#### PostVia

List of possible ways to create a Post

**Values:**
- `buffer`
- `network`
- `api`

#### Product

Buffer products, buffer is used as all products

**Values:**
- `analyze`
- `engage`
- `publish`
- `buffer`
- `startPage`
- `comments`

#### ScheduleOption

**Values:**
- `Queue`
- `Prioritize`
- `FixedTime`
- `Now`

#### SchedulingType

Indicates whether the post was scheduled for notification publishing or automatic publishing

**Values:**
- `notification` - The post was created natively on the social network using notification publishing
- `automatic` - The post was created natively on the social network using automatic publishing

#### Service

The list of services that can be authorized.

**Values:**
- `instagram`
- `facebook`
- `twitter`
- `linkedin`
- `pinterest`
- `tiktok`
- `googlebusiness`
- `startPage`
- `mastodon`
- `youtube`
- `threads`
- `bluesky`

#### ShareMode

How the post is being scheduled.

**Values:**
- `addToQueue`
- `shareNow`
- `shareNext`
- `customScheduled`
- `recommendedTime`

#### SortDirection

Direction to sort the results by.

**Values:**
- `asc` - Sort records in ascending order.
- `desc` - Sort records in descending order.

#### YoutubeLicense

List of license types

**Values:**
- `youtube`
- `creativeCommon`

#### YoutubePrivacy

List of privacy types

**Values:**
- `public`
- `unlisted`
- `private`

### Scalars

#### AccountId

The `AccountId` scalar represents the MongoDB ObjectId of a Buffer Account

#### ChannelId

The `ChannelId` scalar represents the MongoDB ObjectId of a Buffer Channel

#### DateTime

The `DateTime` scalar represents a date and time following the ISO 8601 standard.

#### DraftId

The `DraftId` scalar represents the MongoDB ObjectId of a Buffer Draft

#### IdeaId

The `IdeaId` scalar represents the MongoDB ObjectId of a Buffer Idea

#### NoteId

The `NoteId` scalar represents the MongoDB ObjectId of a Buffer Note

#### OrganizationId

The `OrganizationId` scalar represents the MongoDB ObjectId of a Buffer Organization

#### PostId

The `PostId` scalar represents the MongoDB ObjectId of a Buffer Post

#### TagId

The `TagId` scalar represents the MongoDB ObjectId of a Buffer Tag
