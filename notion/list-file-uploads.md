# Source: https://developers.notion.com/reference/list-file-uploads

status
string
enum
Filter file uploads by specifying the status. Supported values are `pending`, `uploaded`, `expired`, `failed`.
pending uploaded expired failed
Allowed:
`pending``uploaded``expired``failed`
start_cursor
string
If supplied, this endpoint will return a page of results starting after the cursor provided. If not supplied, this endpoint will return the first page of results.
page_size
int32
Defaults to 100
The number of items from the full list desired in the response. Maximum: 100
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
object
# 
400
object
* * *
Did this page help you?
Yes
No
