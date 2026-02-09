# listsdwanconfigs

Source: https://developer.ui.com/site-manager/v1.0.0/listsdwanconfigs

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# List SD-WAN Configs

GET`/v1/sd-wan-configs`

Retrieves a list of all SD-WAN configurations associated with the UI account making the API call.

## Responses

200401429500502

Response Schema: application/json

dataExpand

Array of object

Generic response data, specific schema depends on the endpoint

httpStatusCode

integer

HTTP status code

traceId

string

Request trace identifier