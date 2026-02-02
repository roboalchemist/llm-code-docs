# getsdwanconfigbyid

Source: https://developer.ui.com/site-manager/v1.0.0/getsdwanconfigbyid

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

Get SD-WAN Config by ID
GET
/v1/sd-wan-configs/{id}

Retrieves detailed information about a specific SD-WAN configuration by ID.

path Parameters
id
required
string
Unique identifier of the SD-WAN configuration
Responses
200
401
404
429
500
502

Response Schema: application/json

data
Expand
object
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
curl -L -g "https://api.ui.com/v1/sd-wan-configs/{id}" \
-H "Accept: application/json" \
-H "X-API-Key: <X-API-Key>"
Request
Base URL
API Key
id
Send API Request
Response
Click the Send API Request button above to see the response here!