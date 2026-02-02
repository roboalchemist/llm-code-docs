# listsdwanconfigs

Source: https://developer.ui.com/site-manager/v1.0.0/listsdwanconfigs

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

List SD-WAN Configs
GET
/v1/sd-wan-configs

Retrieves a list of all SD-WAN configurations associated with the UI account making the API call.

Responses
200
401
429
500
502

Response Schema: application/json

data
Expand
Array of object
Generic response data, specific schema depends on the endpoint
httpStatusCode
integer
HTTP status code
traceId
string
Request trace identifier
Example - Call
cURL
Go
Node.js
Python
curl -L "https://api.ui.com/v1/sd-wan-configs" \
-H "Accept: application/json" \
-H "X-API-Key: <X-API-Key>"
Request
Base URL
API Key
Send API Request
Response
Click the Send API Request button above to see the response here!