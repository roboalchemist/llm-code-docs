# Source: https://developers.notion.com/reference/get-user

Retrieves a [User](https://developers.notion.com/reference/user) using the ID specified.
### [](https://developers.notion.com/reference/get-user#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ## 📘
> Integration capabilities
> This endpoint requires an integration to have user information capabilities. Attempting to call this API without user information capabilities will return an HTTP response with a 403 status code. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
user_id
string
required
Identifier for a Notion user
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
json
# 
400
object
* * *
Did this page help you?
Yes
No
