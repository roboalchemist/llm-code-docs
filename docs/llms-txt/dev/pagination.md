# Source: https://dev.writer.com/components/pagination.md

# Source: https://dev.writer.com/api-reference/pagination.md

# Paginate API results

The Writer API supports pagination for list endpoints. By default, the API returns 50 results per page. See below for more information about how to paginate your API requests.

## Pagination parameters

The following parameters are available for pagination in the API:

| Parameter | Type      | Description                                                                                                                                                |
| --------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `limit`   | `integer` | The number of items to return per page. The default is 50. The maximum is 100.                                                                             |
| `order`   | `string`  | The order in which to return the items, based on the `created_at` field for the resource. The default is `desc`. The possible values are `asc` and `desc`. |
| `before`  | `string`  | The ID of first object in the previous page. This parameter instructs the API to return the previous page of results.                                      |
| `after`   | `string`  | The ID of the last object in the next page. This parameter instructs the API to return the next page of results.                                           |

## Pagination response

The API returns the following pagination information in the response body:

| Parameter  | Type      | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| `has_more` | `boolean` | Indicates whether there are more pages of results. |
| `first_id` | `string`  | The ID of the first object in the collection.      |
| `last_id`  | `string`  | The ID of the last object in the collection.       |

## Pagination example: Retrieving files

### Retrieve two most recently created files

The following cURL command retrieves the two most recently created files.

```bash  theme={null}
curl -X GET "https://api.writer.com/v1/files?limit=2" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json"
```

The response body contains the two most recently created files, along with the pagination information:

* The `has_more` parameter is `true`, indicating that there are more files to retrieve
* The `first_id` parameter is the ID of the first file in the collection
* The `last_id` parameter is the ID of the last file in the collection

```json  theme={null}
{
  "data": [
    {
      "id": "c6006e1f",
      "created_at": "2025-06-04T18:19:12.495984Z",
      "name": "paper.pdf",
      "graph_ids": [],
      "status": "completed"
    },
    {
      "id": "57c3754c",
      "created_at": "2025-06-04T18:19:09.973779Z",
      "name": "meeting_notes.pdf",
      "graph_ids": [],
      "status": "completed"
    }
  ],
  "has_more": true,
  "first_id": "c6006e1f",
  "last_id": "57c3754c"
}
```

### Retrieve the next page of results

To retrieve the next page of results, you can use the `after` parameter to specify the ID of the last object in the previous page.

```bash  theme={null}
curl -X GET "https://api.writer.com/v1/files?limit=2&after=57c3754c" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json"
```

## SDK support

The Python and JavaScript SDKs provide iterators that automatically handle pagination for you. See more information about pagination in the [Python SDK](https://github.com/writer/writer-python/blob/main/README.md#pagination) and [JavaScript SDK](https://github.com/writer/writer-node/blob/main/README.md#pagination) documentation.
