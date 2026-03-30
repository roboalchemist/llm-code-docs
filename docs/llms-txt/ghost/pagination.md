# Source: https://docs.ghost.org/themes/helpers/utility/pagination.md

# Source: https://docs.ghost.org/content-api/pagination.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Pagination

All browse endpoints are paginated, returning 15 records by default. You can use the [page](/content-api/parameters#page) and [limit](/content-api/parameters#limit) parameters to move through the pages of records. The response object contains a `meta.pagination` key with information on the current location within the records:

```json  theme={"dark"}
"meta":{
    "pagination":{
      "page":1,
      "limit":2,
      "pages":1,
      "total":1,
      "next":null,
      "prev":null
    }
  }
```


Built with [Mintlify](https://mintlify.com).