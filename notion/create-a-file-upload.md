# Source: https://developers.notion.com/reference/create-a-file-upload

## Create a file upload

**POST** `https://api.notion.com/v1/file_uploads`

Use this API to initiate the process of [uploading a file](/reference/file-upload) to your Notion workspace.

For a successful request, the response is a [File Upload](/reference/file-upload) object with a `status` of `"pending"`.

The maximum allowed length of `filename` string is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](/reference/list-file-uploads) API.

## Body Params

### mode
**string** (enum)

Defaults to `single_part`

How the file is being sent. Use `multi_part` for files larger than 20MB. Use `external_url` for files that are temporarily hosted publicly elsewhere. Default is `single_part`.

**Allowed values:**
- `single_part`
- `multi_part`
- `external_url`

### filename
**string**

Name of the file to be created. Required when `mode` is `multi_part` or `external_url`. Otherwise optional, and used to override the filename. Must include an extension, or have one inferred from the `content_type` parameter.

### content_type
**string**

MIME type of the file to be created. Recommended when sending the file in multiple parts. Must match the content type of the file that's sent, and the extension of the `filename` parameter if any.

### number_of_parts
**int32**

When `mode` is `multi_part`, the number of parts you are uploading. Must be between 1 and 1,000. This must match the number of parts as well as the final `part_number` you send.

### external_url
**string**

When `mode` is `external_url`, provide the HTTPS URL of a publicly accessible file to import into your workspace.

## Headers

### Notion-Version
**string** (required)

The [API version](/reference/versioning) to use for this request. The latest version is `2025-09-03`.

## Responses

### 200
Successful request returns a File Upload object.

### 403
Response body contains error information:
- `object`: string
- `status`: integer (defaults to 0)
- `code`: string
- `message`: string

## Example

### cURL Request
```bash
curl --request POST \
  --url https://api.notion.com/v1/file_uploads \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '
{
  "mode": "single_part"
}'
```

### Response (200)
```json
{
  "id": "b52b8ed6-e029-4707-a671-832549c09de3",
  "object": "file_upload",
  "created_time": "2025-03-15T20:53:00.000Z",
  "last_edited_time": "2025-03-15T20:53:00.000Z",
  "expiry_time": "2025-03-15T21:53:00.000Z",
  "upload_url": "<<baseUrl>>/v1/file_uploads/b52b8ed6-e029-4707-a671-832549c09de3/send",
  "archived": false,
  "status": "pending",
  "filename": "test.txt",
  "content_type": "text/plain",
  "content_length": 1024
}
```

---

**Updated:** 3 months ago

**Related:**
- [List comments](/reference/list-comments)
- [Send a file upload](/reference/send-a-file-upload)
