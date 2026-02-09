# getsdwanconfigbyid

Source: https://developer.ui.com/site-manager/v1.0.0/getsdwanconfigbyid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get SD-WAN Config by ID

GET`/v1/sd-wan-configs/{id}`

Retrieves detailed information about a specific SD-WAN configuration by ID.

path Parameters

id

required

string

Unique identifier of the SD-WAN configuration

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