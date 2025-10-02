# Source: https://developers.notion.com/reference/complete-a-file-upload

## Complete a file upload

**POST** `https://api.notion.com/v1/file_uploads/{file_upload_id}/complete`

Use this API to finalize a `mode=multi_part` [file upload](/reference/file-upload) after all of the parts have been sent successfully.

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
curl --request POST \
  --url https://api.notion.com/v1/file_uploads/file_upload_id/complete \
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
  "archived": false,
  "status": "uploaded",
  "filename": "test.txt",
  "content_type": "text/plain",
  "content_length": 1024
}
```

Updated 5 months ago
