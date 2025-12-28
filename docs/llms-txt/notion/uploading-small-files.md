# Uploading small files

Learn how to send and attach files up to 20 MB using the Notion API.

## The Direct Upload method

The Direct Upload method lets you securely upload private files to Notion-managed storage via the API. Once uploaded, these files can be reused and attached to pages, blocks, or database properties.

This guide walks you through the upload lifecycle:

1. Create a file upload object
2. Send the file content to Notion
3. Attach the file to content in your workspace

💡 **Tip**: Upload once, attach many times. You can reuse the same `file_upload` ID across multiple blocks or pages.

---

## Step 1: Create a File Upload object

Before uploading any content, start by creating a [File Upload object](/reference/file-upload). This returns a unique `id` and `upload_url` used to send the file.

**🧠 Tip:** Save the `id` — You’ll need it to upload the file in Step 2 and attach it in Step 3.

### Example requests

This snippet sends a `POST` request to create the upload object.

```bash
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{}'
```

```python
import json
import requests

payload = {
    "filename": file_name,
    "content_type": "image/png"
}

file_create_response = requests.post("https://api.notion.com/v1/file_uploads", json=payload, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
    "Notion-Version": "2022-06-28"
})

if file_create_response.status_code != 200:
    raise Exception(
        f"File creation failed with status code {file_create_response.status_code}: {file_create_response.text}"
    )

file_upload_id = json.loads(file_create_response.text)["id"]
```

### Example Response

```json
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "last_edited_time": "2025-04-09T22:26:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "upload_url": "https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send",
  "archived": false,
  "status": "pending",
  "filename": null,
  "content_type": null,
  "content_length": null,
  "request_id": "b7c1fd7e-2c84-4f55-877e-d3ad7db2ac4b"
}
```

---

## Step 2: Upload file contents

Next, use the `upload_url` or File Upload object `id` from Step 1 to send the binary file contents to Notion.

**Tips**:

- The only required field is the file contents under the `file` key.
- Unlike other Notion APIs, the Send File Upload endpoint expects a Content-Type of multipart/form-data, not application/json.
- Include a boundary in the `Content-Type` header [for the Send File Upload API] as described in [RFC 2388](https://datatracker.ietf.org/doc/html/rfc2388) and [RFC 1341](https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html). Most HTTP clients (e.g., `fetch`, `ky`) handle this automatically if you include `FormData` with your file and don't pass an explicit `Content-Type` header.

### Example requests

This uploads the file directly from your local system.

```bash
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Notion-Version: 2022-06-28' \
  -H 'multipart/form-data; boundary="----WebKitFormBoundary1a0MvzQ9oLr00NnA"'

--data-binary @filename
```

```python
import json
import requests

payload = {
    "filename": file_name,
    "content_type": "image/png"
}

file_create_response = requests.post("https://api.notion.com/v1/file_uploads", json=payload, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "multipart/form-data; boundary=\"----WebKitFormBoundary1a0MvzQ9oLr00NnA\"",
    "Notion-Version": "2022-06-28"
})

if file_create_response.status_code != 200:
    raise Exception(
        f"File creation failed with status code {file_create_response.status_code}: {file_create_response.text}"
    )
```
```

# The Direct Upload Method

The **Direct Upload** method lets you securely upload private files to Notion-managed storage via the API. Once uploaded, these files can be reused and attached to pages, blocks, or database properties.

This guide walks you through the upload lifecycle:

1. Create a file upload object
2. Send the file content to Notion
3. Attach the file to content in your workspace

💡 **Tip**: Upload once, attach many times. You can reuse the same `file_upload` ID across multiple blocks or pages.

---

## Step 1: Create a File Upload Object

Be sure to set the `filename` field when creating a file upload object. This will make the file appear in the "Downloads" section of your workspace.

```javascript
// Open a read stream for the file
const fileStream = fs.createReadStream(filePath)

// Create form data with the (named) file contents under the `file` key.
const form = new FormData()
form.append('file', fileStream, {
  filename: path.basename(filePath)
})

// HTTP POST to the Send File Upload API.
const response = await fetch(
  `https://api.notion.com/v1/file_uploads/${fileUploadId}/send`,
  {
    method: 'POST',
    body: form,
    headers: {
      'Authorization': `Bearer ${notionToken}`,
      'Notion-Version': notionVersion,
    }
  }
)

// Rescue validation errors. Possible HTTP 400 cases include:
// - content length greater than the 20MB limit
// - FileUpload not in the `pending` status (e.g. `expired`)
// - invalid or unsupported file content type
if (!response.ok) {
  const errorBody = await response.text()
  console.log("Error response body:", errorBody)
  throw new Error(`HTTP error with status: ${response.status}`)
}

const data = await response.json()
// ...
```

### Reminder

Files must be attached within **1 hour** of upload or they’ll be automatically moved to an `archived` status.

## Step 3: Attach the File to a Page or Block

Once the file’s `status` is `uploaded`, it can be attached to any location that supports file objects using the File Upload object `id`.

This step uses standard Notion API endpoints; there’s no special upload-specific API for attaching. Just pass a file object with a type of `file_upload` and include the `id` that you received earlier in Step 1.

You can use the file upload `id` with the following APIs:

1. [Create a page](https://developers.notion.com/reference/post-page)
   - Attach files to a database property with the `files` type
   - Include uploaded files in `children` blocks (e.g., file/image blocks inside a new page)
2. [Update page properties](https://developers.notion.com/reference/patch-page)
   - Update existing `files` properties on a database page
   - Set page `icon` or `cover`
3. [Append block children](https://developers.notion.com/reference/patch-block-children)
   - Add a new block to a page — like a file, image, audio, video, or PDF block that uses an uploaded file
4. [Update a block](https://developers.notion.com/reference/update-a-block)
   - Change the file attached to an existing file block (e.g., convert an image with an external URL to one that uses a file uploaded via the API)

### Example: Add an Image Block to a Page

This example uses the [Append block children](https://developers.notion.com/reference/patch-block-children) API to create a new image block in a page and attach the uploaded file.

```bash
curl --request PATCH \
  --url "https://api.notion.com/v1/blocks/$PAGE_OR_BLOCK_ID/children" \
  -H "Authorization: Bearer ntn_*****" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  --data '{ "children": [{"type": "image", "image": {"caption": [], "type": "file_upload", "file_upload": {"id": "$FILE_UPLOAD_ID"}}}] }'
```

```python
# Append image to desired block (this could be a page,
# or a block within a page)
url = f"https://api.notion.com/v1/blocks/{append_block_id}/children"

payload = {
    "children": [
        {
            "object": "block",
            "type": "image",
            "image": {
                "type": "file_upload",
                "file_upload": {
                    "id": file_upload_id
                }
            }
        }
    ]
}

response = requests.patch(url, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
    "Notion-Version": "2022-06-28"
}, data=json.dumps(payload))

if response.status_code != 200:
    raise Exception(
        f"Block append failed with status code {response.status_code}: {response.text}")
```

### Example: Add a File Block to a Page

This example uses the [Append block children](https://developers.notion.com/reference/patch-block-children) API to create a new file block in a page and attach the uploaded file.

```bash
curl --request PATCH \
  --url "https://api.notion.com/v1/blocks/$PAGE_OR_BLOCK_ID/children" \
  -H "Authorization: Bearer ntn_*****" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  --data '{ "children": [{"type": "file", "file": {"type": "file_upload", "file_upload": {"id": "$FILE_UPLOAD_ID"}}}] }'
```

### Example: Attach a File Property to a Page in a Database

This example uses the [Update page properties](https://developers.notion.com/reference/patch-page) API to add the uploaded file to a `files` property on a page that lives in a Notion data source.

```bash
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$PAGE_ID" \
  -H "Authorization: Bearer ntn_****" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  --data '{ "properties": {"Attachments": {"type": "files", "files": [{"type": "file_upload", "file_upload": {"id": "$FILE_UPLOAD_ID"}, "name": "logo.png"}] }}}'
```

### Example: Set a Page Cover

This example uses the [Update page properties](https://developers.notion.com/reference/patch-page) API to add the uploaded file as a page cover.

```bash
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$PAGE_ID" \
  -H "Authorization: Bearer ntn_****" \
  -H "Content-Type: application/json" \
  -H "Notion-Version: 2022-06-28" \
  --data '{ "cover": {"type": "file_upload", "file_upload": {"id": "$FILE_UPLOAD_ID"}}}'
```

**✅ You’ve successfully uploaded and attached a file using Notion’s Direct Upload method.**

---

## File Lifecycle and Reuse

When a file is first uploaded, it has an `expiry_time`, one hour from the time of creation, during which it must be attached.

Once attached to any page, block, or database in your workspace:

- The `expiry_time` is removed.
- The file becomes a permanent part of your workspace.
- The `status` remains `uploaded`.

Even if the original content is deleted, the `file_upload` ID remains valid and can be reused to attach the file again.

Currently, there is no way to delete or revoke a file upload after it has been created.

---

## Downloading an Uploaded File

Attaching a file upload gives you access to a temporary download URL via the Notion API.

These URLs expire after 1 hour.

To refresh access, re-fetch the page, block, or database where the file is attached.

📌 **Tip:** A file becomes persistent and reusable after the first successful attachment — no need to re-upload.

---

## Tips and Troubleshooting

- **URL expiration**: Notion-hosted files expire after 1 hour. Always re-fetch file objects to refresh links.
- **Attachment deadline**: Files must be attached within 1 hour of upload, or they’ll expire.
- **Size limit**: This guide only supports files up to 20 MB. Larger files require a [multi-part upload](https://developers.notion.com/docs/sending-larger-files).
- **Block type compatibility**: Files can be attached to image, file, video, audio, or pdf blocks — and to `files` properties on pages.

The **Direct Upload** method lets you securely upload private files to Notion-managed storage via the API. Once uploaded, these files can be reused and attached to pages, blocks, or database properties.

This guide walks you through the upload lifecycle:

1. Create a file upload object
2. Send the file content to Notion
3. Attach the file to content in your workspace

💡 **Tip**: Upload once, attach many times. You can reuse the same `file_upload` ID across multiple blocks or pages.

---

## Step 1: Create a File Upload Object

Be sure to set the `filename` field when creating a file upload object. This will make the file appear in the "Downloads" section of your workspace.

```javascript
// Open a read stream for the file
const fileStream = fs.createReadStream(filePath)

// Create form data with the (named) file contents under the `file` key.
const form = new FormData()
form.append('file', fileStream, {
  filename: path.basename(filePath)
})

// HTTP POST to the Send File Upload API.
const response = await fetch(
  `https://api.notion.com/v1/file_uploads/${fileUploadId}/send`,
  {
    method: 'POST',
    body: form,
    headers: {
      'Authorization': `Bearer ${notionToken}`,
      'Notion-Version': notionVersion,
    }
  }
)

// Rescue validation errors. Possible HTTP 400 cases include:
// - content length greater than the 20MB limit
// - FileUpload not in the `pending` status (e.g. `expired`)
// - invalid or unsupported file content type
if (!response.ok) {
  const errorBody = await response.text()
  console.log("Error response body:", errorBody)
  throw new Error(`HTTP error with status: ${response.status}`)
}

const data = await response.json()
// ...
```

### Reminder

Files must be attached within **1 hour** of upload or they’ll be automatically moved to an `archived` status.
```

# Creating a File Upload Object

To create a file upload object, you'll need to make a `POST` request to the `/v1/file_uploads` endpoint. Include the necessary headers and data in your request.

**🧠 Tip:** Save the `id` — you'll need it to upload the file in Step 2 and attach it in Step 3.

## Example Requests

This snippet sends a `POST` request to create the upload object.

### cURL

```bash
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{}'
```

### python

```python
import json
import requests

payload = {
    "filename": file_name,
    "content_type": "image/png"
}

file_create_response = requests.post("https://api.notion.com/v1/file_uploads", json=payload, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
    "Notion-Version": "2022-06-28"
})

if file_create_response.status_code != 200:
    raise Exception(
        f"File creation failed with status code {file_create_response.status_code}: {file_create_response.text}"
    )

file_upload_id = json.loads(file_create_response.text)['id']
```

## Example Response

```json
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "last_edited_time": "2025-04-09T22:26:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "upload_url": "https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send",
  "archived": false,
  "status": "pending",
  "filename": null,
  "content_type": null,
  "content_length": null,
  "request_id": "b7c1fd7e-2c84-4f55-877e-d3ad7db2ac4b"
}
```

## Step 2: Upload File Contents

Next, use the `upload_url` or File Upload object `id` from Step 1 to send the binary file contents to Notion.

**Tips**:

- The only required field is the file contents under the `file` key.
- Unlike other Notion APIs, the Send File Upload endpoint expects a Content-Type of multipart/form-data, not application/json.
- Include a boundary in the `Content-Type` header [for the Send File Upload API] as described in [RFC 2388](https://datatracker.ietf.org/doc/html/rfc2388) and [RFC 1341](https://www.w3.org/Protocols/rfc1341/7_2_Multipart.html). Most HTTP clients (e.g., `fetch`, `ky`) handle this automatically if you include `FormData` with your file and don't pass an explicit `Content-Type` header.

### Example Requests

This uploads the file directly from your local system.

#### curl

```bash
curl --request POST \
  --url 'https://api.notion.com/v1/file_uploads/a3f9d3e2-1abc-42de-b904-badc0ffee000/send' \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Notion-Version: 2022-06-28' \
  -H 'Content-Type: multipart/form-data' \
  -F "file=@path/to-file.gif"
```

#### javascript

```javascript
// Open a read stream for the file
const fileStream = fs.createReadStream(filePath)

// Create form data with the (named) file contents under the `file` key.
const form = new FormData()
form.append('file', fileStream, {
.filename: path.basename(filePath)
})

// HTTP POST to the Send File Upload API.
const response = await fetch(
	`https://api.notion.com/v1/file_uploads/${fileUploadId}/send`,
	{
		method: 'POST',
		body: form,
		headers: {
			'Authorization': `Bearer ${notionToken}`,
			'Notion-Version': notionVersion,
		}
	}
)

// Rescue validation errors. Possible HTTP 400 cases include:
// - content length greater than the 20MB limit
// - FileUpload not in the `pending` status (e.g. `expired`)
// - invalid or unsupported file content type
if (!response.ok) {
	const errorBody = await response.text()
	console.log('Error response body:', errorBody)
	throw new Error(`HTTP error with status: ${response.status}`)
}

const data = await response.json()
// ...
```

#### Python

```python
file_name = "test.png"

with open(file_name, "rb") as f:
	# Provide the MIME content type of the file as the 3rd argument.
	# files = {
	#     "file": (file_name, f, "image/png")
	# }

	# response = requests.post(
	#     f"https://api.notion.com/v1/file_uploads/{file_upload_id}/send",
	#     headers={
	#         "Authorization": f"Bearer {NOTION_KEY}",
	#         "Notion-Version": "2022-06-28"
	#     },
	#     files=files
	# )

	# if response.status_code != 200:
	#     raise Exception(
	#         f"File upload failed with status code {response.status_code}: {response.text}"
	# )
```

### Example Response

```json
{
  "object": "file_upload",
  "id": "a3f9d3e2-1abc-42de-b904-badc0ffee000",
  "created_time": "2025-04-09T22:26:00.000Z",
  "last_edited_time": "2025-04-09T22:27:00.000Z",
  "expiry_time": "2025-04-09T23:26:00.000Z",
  "archived": false,
  "status": "uploaded",
  "filename": "Really funny.gif",
  "content_type": "image/gif",
  "content_length": "4435",
  "request_id": "91a4ee8c-61f6-4c27-bd41-09aa35299929"
}
```

> **Reminder**
>
> Files must be attached within **1 hour** of upload or they’ll be automatically moved to an `archived` status.

## Step 3: Attach the File to a Page or Block

Once the file’s `status` is `uploaded`, it can be attached to any location that supports file objects using the File Upload object `id`.

This step uses standard Notion API endpoints; there’s no special upload-specific API for attaching. Just pass a file object with a type of `file_upload` and include the `id` that you received earlier in Step 1.

You can use the file upload `id` with the following APIs:

1. [Create a page](/reference/post-page)
   - Attach files to a database property with the `files` type
   - Include uploaded files in `children` blocks (e.g., file/image blocks inside a new page)
2. [Update page properties](/reference/patch-page)
   - Update existing `files` properties on a database page
   - Set page `icon` or `cover`
3. [Append block children](/reference/patch-block-children)
   - Add a new block to a page — like a file, image, audio, video, or PDF block that uses an uploaded file
4. [Update a block](/reference/update-a-block)
   - Change the file attached to an existing file block (e.g., convert an image with an external URL to one that uses a file uploaded via the API)

### Example: Add an Image Block to a Page

This example uses the [Append block children](/reference/patch-block-children) API to create a new image block in a page and attach the uploaded file.

#### cURL

```bash
curl --request PATCH \
	--url "https://api.notion.com/v1/blocks/$PAGE_OR_BLOCK_ID/children" \
	-H "Authorization: Bearer ntn_*****" \
	-H 'Content-Type: application/json' \
	-H 'Notion-Version: 2022-06-28' \
	--data '{
		"children": [
			{
				"type": "image",
				"image": {
					"caption": [],
					"type": "file_upload",
					"file_upload": {
						"id": "'"$FILE_UPLOAD_ID'"
					}
				}
			}
		]
	}'
```

#### Python

```python
# Append image to desired block (this could be a page,
# or a block within a page)
url = f"https://api.notion.com/v1/blocks/{append_block_id}/children"

payload = {
    "children": [
        {
            "object": "block",
            "type": "image",
            "image": {
                "type": "file_upload",
                "file_upload": {
                    "id": file_upload_id
                }
            }
        }
    ]
}

response = requests.patch(url, headers={
    "Authorization": f"Bearer {NOTION_KEY}",
    "accept": "application/json",
    "content-type": "application/json",
    "Notion-Version": "2022-06-28"
}, data=json.dumps(payload))

if response.status_code != 200:
    raise Exception(
        f"Block append failed with status code {response.status_code}: {response.text}")
```

### Example: Add a File Block to a Page

This example uses the [Append block children](/reference/patch-block-children) API to create a new file block in a page and attach the uploaded file.

#### cURL

```bash
curl --request POST \
  --url "https://api.notion.com/v1/blocks/$PAGE_OR_BLOCK_ID/children" \
  -H "Authorization: Bearer ntn_*****" \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
	  "children": [
		  {
			  "type": "file",
			  "file": {
				  "type": "file_upload",
				  "file_upload": {
					  "id": "'"$FILE_UPLOAD_ID"'
				  }
			  }
		  }
	  ]
  }'
```

### Example: Attach a File Property to a Page in a Database

This example uses the [Update page properties](/reference/patch-page) API to add the uploaded file to a `files` property on a page that lives in a Notion data source.

#### cURL

```bash
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$PAGE_ID" \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
    "properties": {
      "Attachments": {
        "type": "files",
        "files": [
          {
            "type": "file_upload",
            "file_upload": { "id": "9a8b7c6d-1e2f-4a3b-9e0f-a1b2c3d4e5f6" },
            "name": "logo.png"
          }
        ]
      }
    }
  }'
```

### Example: Set a Page Cover

This example uses the [Update page properties](/reference/patch-page) API to add the uploaded file as a page cover.

#### cURL

```bash
curl --request PATCH \
  --url "https://api.notion.com/v1/pages/$PAGE_ID" \
  -H 'Authorization: Bearer ntn_****' \
  -H 'Content-Type: application/json' \
  -H 'Notion-Version: 2022-06-28' \
  --data '{
	  "cover": {
		  "type": "file_upload",
		  "file_upload": {
			  "id": "'"$FILE_UPLOAD_ID"'
		  }
	  }
  }'
```

**✅ You’ve successfully uploaded and attached a file using Notion’s Direct Upload method.**

---

## File Lifecycle and Reuse

When a file is first uploaded, it has an `expiry_time`, one hour from the time of creation, during which it must be attached.

Once attached to any page, block, or database in your workspace:

- The `expiry_time` is removed.
- The file becomes a permanent part of your workspace.
- The `status` remains `uploaded`.

Even if the original content is deleted, the `file_upload` ID remains valid and can be reused to attach the file again.

Currently, there is no way to delete or revoke a file upload after it has been created.

```

# Attaching a File Upload

Attaching a file upload gives you access to a temporary download URL via the Notion API.

These URLs expire after 1 hour.

To refresh access, re-fetch the page, block, or database where the file is attached.

📌 **Tip:** A file becomes persistent and reusable after the first successful attachment — no need to re-upload.

## Tips and Troubleshooting

- **URL expiration**: Notion-hosted files expire after 1 hour. Always re-fetch file objects to refresh links.
- **Attachment deadline**: Files must be attached within 1 hour of upload, or they’ll expire.
- **Size limit**: This guide only supports files up to 20 MB. Larger files require a [multi-part upload](/docs/sending-larger-files).
- **Block type compatibility**: Files can be attached to image, file, video, audio, or PDF blocks — and to `files` properties on pages.

---

### Step 1: Create a File Upload object

#### Example requests

```http
POST /v1/files?parent=page1
Content-Type: multipart/form-data; boundary=

------WebKitFormBoundaryS9Ic8MmFkTjBnVX
Content-Disposition: form-data; name="file"; filename="notion.png"

image/png,
width=1024,
height=768,

------WebKitFormBoundaryS9Ic8MmFkTjBnVX--
```

#### Example Response

```json
{
  "id": "669880000000000000",
  "name": "notion.png",
  "parent": "page1",
  "created": "2023-03-12T19:26:34.162Z",
  "updated": "2023-03-12T19:26:34.162Z",
  "size": 10485760,
  "type": "image/png"
}
```

### Step 2: Upload file contents

#### Example requests

```http
POST /v1/files?parent=page1
Content-Type: multipart/form-data; boundary=

------WebKitFormBoundaryS9Ic8MmFkTjBnVX
Content-Disposition: form-data; name="file"; filename="notion.png"

image/png,
width=1024,
height=768,

------WebKitFormBoundaryS9Ic8MmFkTjBnVX--
```

#### Example response

```json
{
  "id": "669880000000000000",
  "name": "notion.png",
  "parent": "page1",
  "created": "2023-03-12T19:26:34.162Z",
  "updated": "2023-03-12T19:26:34.162Z",
  "size": 10485760,
  "type": "image/png"
}
```

### Step 3: Attach the file to a page or block

#### Example: add an image block to a page

```http
POST /v1/pages/page1/attachments
Content-Type: application/json
Accept: application/json

{
  "resource": {
    "type": "page",
    "id": "669880000000000000"
  },
  "data": {
    "type": "file",
    "properties": {
      "filename": "notion.png",
      "src": "https://example.com/notion.png"
    }
  }
}
```

#### Example: add a file block to a page

```http
POST /v1/pages/page1/attachments
Content-Type: application/json
Accept: application/json

{
  "resource": {
    "type": "page",
    "id": "669880000000000000"
  },
  "data": {
    "type": "file",
    "properties": {
      "filename": "notion.png",
      "src": "https://example.com/notion.png"
    }
  }
}
```

#### Example: attach a file property to a page in a database

```http
POST /v1/databases/database1/pages/page1/attachments
Content-Type: application/json
Accept: application/json

{
  "resource": {
    "type": "page",
    "id": "669880000000000000"
  },
  "data": {
    "type": "file",
    "properties": {
      "filename": "notion.png",
      "src": "https://example.com/notion.png"
    }
  }
}
```

#### Example: Set a page cover

```http
POST /v1/pages/page1/attachments
Content-Type: application/json
Accept: application/json

{
  "resource": {
    "type": "page",
    "id": "669880000000000000"
  },
  "data": {
    "type": "file",
    "properties": {
      "filename": "cover.jpg",
      "src": "https://example.com/cover.jpg"
    }
  }
}
```

### File lifecycle and reuse

File attachments remain valid for one day after being created. If you want to reuse an attachment, delete the original, then create a new file with the same name.

### Downloading an uploaded file

Attaching a file upload gives you access to a temporary download URL via the Notion API.

These URLs expire after 1 hour.

To refresh access, re-fetch the page, block, or database where the file is attached.

📌 **Tip:** A file becomes persistent and reusable after the first successful attachment — no need to re-upload.

### Tips and troubleshooting

- **URL expiration**: Notion-hosted files expire after 1 hour. Always re-fetch file objects to refresh links.
- **Attachment deadline**: Files must be attached within 1 hour of upload, or they’ll expire.
- **Size limit**: This guide only supports files up to 20 MB. Larger files require a [multi-part upload](/docs/sending-larger-files).
- **Block type compatibility**: Files can be attached to image, file, video, audio, or PDF blocks — and to `files` properties on pages.

---

Updated 3 months ago

---

## What’s Next

Now that you know how to upload a file, let’s walk through how to retrieve a file via the API:

- [Retrieving existing files in your workspace](/docs/retrieving-files)
```