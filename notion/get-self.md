# Source: https://developers.notion.com/reference/get-self

Retrieves the bot [User](https://developers.notion.com/reference/user) associated with the API token provided in the authorization header. The bot will have an `owner` field with information about the person who authorized the integration.
### [](https://developers.notion.com/reference/get-self#errors)
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
> ## 📘
> Integration capabilities
> This endpoint is accessible from by integrations with any level of capabilities. The [user object](https://developers.notion.com/reference/user) returned will adhere to the limitations of the integration's capabilities. For more information on integration capabilities, see the [capabilities guide](https://developers.notion.com/reference/capabilities).
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
name
string
avatar_url
string
type
string
bot
object
owner
object
owner object
# 
400
object
* * *
Did this page help you?
Yes
No
