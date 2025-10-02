# List file uploads

GET https://api.notion.com/v1/file_uploads

Use this API to retrieve [file uploads](https://developers.notion.com/reference/file-upload) for the current bot integration, sorted by most recent first.

## Query Params

**status** (string, enum)
Filter file uploads by specifying the status. Supported values are `pending`, `uploaded`, `expired`, `failed`.

Allowed values:
- `pending`
- `uploaded`
- `expired`
- `failed`

**start_cursor** (string)
If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.

**page_size** (int32)
Defaults to 100
The number of items from the full list desired in the response. Maximum: 100

## Headers

**Notion-Version** (string, required)
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.

## Responses

### 200
200 - Response body: object

### 400
400 - Response body: object

---

## Example Request

```shell
curl --request GET \
--url 'https://api.notion.com/v1/file_uploads?page_size=100' \
--header 'accept: application/json'
```

## Example Response (200)

```json
{}
```

---

Updated 5 months ago

**Previous:** [Retrieve a file upload](/reference/retrieve-a-file-upload)
**Next:** [Search](/reference/post-search)
