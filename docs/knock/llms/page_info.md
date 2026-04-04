# Source: https://docs.knock.app/mapi-reference/$shared/schemas/page_info.md

# Source: https://docs.knock.app/api-reference/$shared/schemas/page_info.md

### PageInfo

Pagination information for a list of resources.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **after** (string) - The cursor to fetch entries after.
- **before** (string) - The cursor to fetch entries before.
- **page_size** (integer) *required* - The number of items per page (defaults to 50).

#### Example

```json
{
  "__typename": "PageInfo",
  "after": null,
  "before": null,
  "page_size": 25
}
```

