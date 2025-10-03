# Source: https://developers.notion.com/reference/refresh-a-token

> ## 📘
> For step-by-step instructions on how to use this endpoint to refresh an access token, check out the [Authorization guide](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up).
_Note: Each Public API endpoint can return several possible error codes. To see a full description of each type of error code, see the[Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation._
grant_type
string
required
Defaults to "refresh_token"
A constant string: "refresh_token"
refresh_token
string
required
A unique token that Notion generates to refresh your token, generated when a user initiates the OAuth flow.
Authorization
string
Defaults to Basic $BASE64_ENCODED_ID_AND_SECRET
# 
200
object
access_token
string
refresh_token
string
bot_id
string
duplicated_template_id
string
owner
object
workspace
boolean
Defaults to true
workspace_icon
string
workspace_id
string
workspace_name
string
# 
400
object
error
string
error_description
string
* * *
Did this page help you?
Yes
No
