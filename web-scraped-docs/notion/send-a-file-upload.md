# Source: https://developers.notion.com/reference/send-a-file-upload

For this endpoint, use a `Content-Type` of `multipart/form-data`, and provide your file contents under the `file` key.
> ## 📘
> The use of multipart form data is unique to this endpoint. Other Notion APIs, including [Create a file upload](https://developers.notion.com/reference/create-a-file-upload) and [Complete a file upload](https://developers.notion.com/reference/complete-a-file-upload), use JSON parameters.
> Include a `boundary` with the `Content-Type` header of your request as per [RFC 2388](https://datatracker.ietf.org/doc/html/rfc2388). Most request libraries (e.g. `fetch`, `ky`) automatically handle this as long as you provide a form data object but don't overwrite the `Content-Type` explicitly.
> For more tips and examples, view the [file upload guide](https://developers.notion.com/reference/uploading-small-files#step-2-upload-file-contents).
When `mode=multi_part`, each part must include a form field `part_number` to indicate which part is being sent. Parts may be sent concurrently up to standard Notion API [rate limits](https://developers.notion.com/reference/request-limits), and may be sent out of order as long as all parts (1, ..., `part_number`) are successfully sent before calling the [complete file upload API](https://developers.notion.com/reference/complete-a-file-upload).
The maximum allowed length of a file name is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](https://developers.notion.com/reference/list-file-uploads) API.
