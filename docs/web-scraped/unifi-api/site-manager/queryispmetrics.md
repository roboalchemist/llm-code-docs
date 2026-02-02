# queryispmetrics

Source: https://developer.ui.com/site-manager/v1.0.0/queryispmetrics

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

Query ISP Metrics
POST
/v1/isp-metrics/{type}/query

Retrieves ISP metrics data based on specific query parameters. 5-minute interval metrics are available for at least 24 hours, and 1-hour interval metrics are available for at least 30 days.

Note: If the UI account lacks access to all requested sites, a 502 error is returned. If partial access is granted, the response will include status: partialSuccess.

path Parameters
type
required
string
Specifies whether metrics are returned using `5m` or `1h` intervals
request Body
sites
Expand
Array of object
Responses
200
400
401
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
curl -L -g "https://api.ui.com/v1/isp-metrics/{type}/query" \
-H "Accept: application/json" \
-H "X-API-Key: <X-API-Key>" \
-H "Content-Type: application/json" \
-d "{
  \"sites\": [
    {
      \"beginTimestamp\": \"2024-06-30T13:35:00Z\",
      \"hostId\": \"900A6F00301100000000074A6BA90000000007A3387E0000000063EC9853:123456789\",
      \"endTimestamp\": \"2024-06-30T15:35:00Z\",
      \"siteId\": \"661900ae6aec8f548d49fd54\"
    }
  ]
}"
Request
Base URL
API Key
type
Send API Request
Response
Click the Send API Request button above to see the response here!