# Source: https://developers.buffer.com/guides/pagination.md

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
