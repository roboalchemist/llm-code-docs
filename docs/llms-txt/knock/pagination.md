# Source: https://docs.knock.app/api-reference/overview/pagination.md

# Pagination

All top-level API resources expose support for bulk fetches via a `list` method. For instance, you can [list users](#list-users), [list objects](#list-objects) in a collection, and [list subscriptions](#list-subscriptions).

Resources that return multiple entities support the same cursor-based pagination to interact with the resources, using `after`, `before`, and `page_size` parameters as well as returning a common format for the metadata associated with the page.

### Query parameters

- **after** (string): The pagination cursor to fetch items after. Usually derived from the after cursor in `PageInfo`.
- **before** (string): The pagination cursor to fetch items before. Usually derived from the before cursor in `PageInfo`.
- **page_size** (number (optional)): A number between 1 and 50 that represents the number of items to return in the response. Defaults to 50.

### Response format

- **entries** (object[]): A list of items contained in this response.
- **page_info** (PageInfo): Metadata about the page of data returned.

### PageInfo response details

- **after** (string): The cursor to use to fetch items after the last item in the list. May be null when there are no other items to retrieve.
- **before** (string): The cursor to use to fetch items before the first item in the list. May be null when there are no other items to retrieve.
- **page_size** (number): The maximum number of items requested in the page.
- **total_count** (number): The total number of items in this resource (up-to 10,000).

```json title="Response"
{
  "entries": [
    {
      "__typename": "User",
      "id": "user_1",
      "name": "User name",
      "email": "user-1@example.com",
      "created_at": null,
      "updated_at": "2021-03-05T12:00:00Z"
    },
    {
      "__typename": "User",
      "id": "user_2",
      "name": "User name",
      "email": "user-2@example.com",
      "created_at": null,
      "updated_at": "2021-03-05T12:00:00Z"
    }
  ],
  "page_info": {
    "__typename": "PageInfo",
    "page_size": 50,
    "total_count": 2,
    "after": null,
    "before": null
  }
}
```
