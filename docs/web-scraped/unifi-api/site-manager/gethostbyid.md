# gethostbyid

Source: https://developer.ui.com/site-manager/v1.0.0/gethostbyid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Host by ID

GET`/v1/hosts/{id}`

Retrieves detailed information about a specific host by ID.

**Note**: The structure of the `userData` and `reportedState` fields may vary depending on the UniFi OS or Network Server version. The example provided is based on UniFi OS 4.1.13.

path Parameters

id

required

string

Unique identifier of the host

## Responses

200401404429500502

Response Schema: application/json

dataExpand

object

Generic response data, specific schema depends on the endpoint

httpStatusCode

integer

HTTP status code

traceId

string

Request trace identifier