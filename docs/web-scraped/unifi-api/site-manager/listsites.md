# listsites

Source: https://developer.ui.com/site-manager/v1.0.0/listsites

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List Sites

GET`/v1/sites`

Retrieves a list of all sites (from hosts running the UniFi Network application) associated with the UI account making the API call.

**Note**: The structure of the `meta` and `statistics` fields may vary depending on the UniFi Network version. The example provided is based on UniFi OS 4.1.13.

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