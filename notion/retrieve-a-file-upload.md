# Source: https://developers.notion.com/reference/retrieve-a-file-upload

## Retrieve a file upload

**GET** `https://api.notion.com/v1/file_uploads/{file_upload_id}`

Use this API to get the details of a [File Upload](/reference/file-upload) object.

## Headers

**Notion-Version** (string, required)
The [API version](/reference/versioning) to use for this request. The latest version is `2025-09-03`.

## Responses

### 200 - Success
Response body: json

### 400 - Bad Request
Response body: object

## Example

### cURL Request
```bash
curl --request GET \
  --url https://api.notion.com/v1/file_uploads/file_upload_id \
  --header 'accept: application/json'
```

### Response (200)
```json
{
  "id": "b52b8ed6-e029-4707-a671-832549c09de3",
  "object": "file_upload",
  "created_time": "2025-03-15T20:53:00.000Z",
  "last_edited_time": "2025-03-15T20:57:00.000Z",
  "expiry_time": "2025-03-15T21:53:00.000Z",
  "upload_url": null,
  "archived": false,
  "status": "uploaded",
  "filename": "test.txt",
  "content_type": "text/plain",
  "content_length": 1024
}
```

Updated 4 months ago
