# Source: https://developers.buffer.com/guides/data-model.md

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
