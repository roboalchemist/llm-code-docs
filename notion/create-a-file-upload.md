# Source: https://developers.notion.com/reference/create-a-file-upload

For a successful request, the response is a [File Upload](https://developers.notion.com/reference/file-upload) object with a `status` of `"pending"`.
The maximum allowed length of `filename` string is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](https://developers.notion.com/reference/list-file-uploads) API.
