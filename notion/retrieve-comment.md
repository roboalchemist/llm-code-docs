# Source: https://developers.notion.com/reference/retrieve-comment

### [](https://developers.notion.com/reference/retrieve-comment#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ## 📘
> Reminder: Turn on integration comment capabilities
> Integration capabilities for reading and inserting comments are off by default.
> This endpoint requires an integration to have read comment capabilities. Attempting to call this endpoint without read comment capabilities will return an HTTP response with a 403 status code. 
> For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities). To update your integration settings, visit the [integration dashboard](https://www.notion.so/my-integrations).
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
object
object
string
id
string
parent
object
type
string
block_id
string
discussion_id
string
created_time
string
last_edited_time
string
created_by
object
object
string
id
string
rich_text
array of objects
rich_text
object
type
string
text
object
text object
annotations
object
annotations object
plain_text
string
href
string
display_name
object
type
string
resolved_name
string
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
