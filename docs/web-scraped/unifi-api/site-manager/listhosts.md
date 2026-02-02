# listhosts

Source: https://developer.ui.com/site-manager/v1.0.0/listhosts

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

List Hosts
GET
/v1/hosts

Retrieves a list of all hosts associated with the UI account making the API call.

Note: The structure of userData and reportedState fields may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

query Parameters
pageSize
string
Number of items to return per page
nextToken
string
Token for pagination to retrieve the next set of results
Responses
200
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
curl -L "https://api.ui.com/v1/hosts?pageSize=10&nextToken=602232A870250000000006C514FF00000000073DD8DB000000006369FDA2%3A1467082514" \
-H "Accept: application/json" \
-H "X-API-Key: <X-API-Key>"
Request
Base URL
API Key
Show Optional Parameters
Send API Request
Response
Click the Send API Request button above to see the response here!