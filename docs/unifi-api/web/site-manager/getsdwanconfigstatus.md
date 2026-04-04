# getsdwanconfigstatus

Source: https://developer.ui.com/site-manager/v1.0.0/getsdwanconfigstatus

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get SD-WAN Config Status

GET`/v1/sd-wan-configs/{id}/status`

Retrieves the status of a specific SD-WAN configuration, including deployment progress, errors, and associated hubs.

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