# Source: https://developers.buffer.com/guides/introduction.md

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
