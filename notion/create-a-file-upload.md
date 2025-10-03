# Source: https://developers.notion.com/reference/create-a-file-upload

For a successful request, the response is a [File Upload](https://developers.notion.com/reference/file-upload) object with a `status` of `"pending"`.
The maximum allowed length of `filename` string is 900 bytes, including any file extension included in the file name or inferred based on the `content_type`. However, we recommend using shorter names for performance and easier file management and lookup using the [List file uploads](https://developers.notion.com/reference/list-file-uploads) API.
mode
string
enum
Defaults to single_part
How the file is being sent. Use `multi_part` for files larger than 20MB. Use `external_url` for files that are temporarily hosted publicly elsewhere. Default is `single_part`.
single_part multi_part external_url
Allowed:
`single_part``multi_part``external_url`
filename
string
Name of the file to be created. Required when `mode` is `multi_part` or `external_url`. Otherwise optional, and used to override the filename. Must include an extension, or have one inferred from the `content_type` parameter.
content_type
string
MIME type of the file to be created. Recommended when sending the file in multiple parts. Must match the content type of the file that's sent, and the extension of the `filename` parameter if any.
number_of_parts
int32
When `mode` is `multi_part`, the number of parts you are uploading. Must be between 1 and 1,000. This must match the number of parts as well as the final `part_number` you send.
external_url
string
When `mode` is `external_url`, provide the HTTPS URL of a publicly accessible file to import into your workspace.
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
json
# 
403
object
object
string
status
integer
Defaults to 0
code
string
message
string
* * *
Did this page help you?
Yes
No
