# Source: https://developers.buffer.com/guides/rest-migration.md

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
