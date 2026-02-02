# getispmetrics

Source: https://developer.ui.com/site-manager/v1.0.0/getispmetrics

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

Get ISP Metrics
GET
/v1/isp-metrics/{type}

Retrieves ISP metrics data for all sites linked to the UI account's API key. 5-minute interval metrics are available for at least 24 hours, and 1-hour interval metrics are available for at least 30 days.

path Parameters
type
required
string
Specifies whether metrics are returned using `5m` or `1h` intervals
query Parameters
beginTimestamp
string
The earliest timestamp to retrieve data from (RFC3339 format)
endTimestamp
string
The latest timestamp to retrieve data up to (RFC3339 format)
duration
string
Specifies the time range of metrics to retrieve, starting from when the request is made. Supports `24h` for 5-minute metrics, and `7d` or `30d` for 1-hour metrics. This parameter **cannot** be used with `beginTimestamp` or `endTimestamp`.
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
curl -L -g "https://api.ui.com/v1/isp-metrics/{type}?beginTimestamp=2024-06-30T13%3A35%3A00Z&endTimestamp=2024-06-30T15%3A35%3A00Z&duration={duration}" \
-H "Accept: application/json" \
-H "X-API-Key: <X-API-Key>"
Request
Base URL
API Key
type
Show Optional Parameters
Send API Request
Response
Click the Send API Request button above to see the response here!