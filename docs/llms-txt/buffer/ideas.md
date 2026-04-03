# Source: https://developers.buffer.com/guides/ideas.md

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
