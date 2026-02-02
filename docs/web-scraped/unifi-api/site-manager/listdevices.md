# listdevices

Source: https://developer.ui.com/site-manager/v1.0.0/listdevices

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

List Devices
GET
/v1/devices

Retrieves a list of UniFi devices managed by hosts where the UI account making the API call is the owner or a super admin.

Note: The structure of the devices.uidb field may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

query Parameters
hostIds[]
Expand
Array of string
List of host IDs to filter the results
time
string
Last processed timestamp of devices in RFC3339 format
pageSize
string
Number of items to return per page
nextToken
string
Token for pagination to retrieve the next set of results
Responses
200
400
401
429
500
502

Response Schema: application/json

code
any
Error code from upstream
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
nextToken
string
Pagination token for fetching the next set of results
Example - Call
cURL
Go
Node.js
Python
curl -L -g "https://api.ui.com/v1/devices?hostIds[]=900A6F00301100000000074A6BA90000000007A3387E0000000063EC9853%3A123456789%2C900A6F00301100000000074A6BA90000000007A3387E0000000063EC9853%3A987654321&time=2025-10-30T01%3A52%3A51Z&pageSize=10&nextToken=602232A870250000000006C514FF00000000073DD8DB000000006369FDA2%3A1467082514" \
-H "Accept: application/json" \
-H "X-API-Key: <X-API-Key>"
Request
Base URL
API Key
Show Optional Parameters
Send API Request
Response
Click the Send API Request button above to see the response here!