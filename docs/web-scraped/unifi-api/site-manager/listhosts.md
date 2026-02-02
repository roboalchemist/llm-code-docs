# listhosts

Source: https://developer.ui.com/site-manager/v1.0.0/listhosts

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Hosts

GET`/v1/hosts`

Retrieves a list of all hosts associated with the UI account making the API call.

**Note**: The structure of `userData` and `reportedState` fields may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

query Parameters

pageSize

string

Number of items to return per page

nextToken

string

Token for pagination to retrieve the next set of results

## Responses

200401429500502

Response Schema: application/json

code

any

Error code from upstream

dataExpand

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