# executeportaction

Source: https://developer.ui.com/network/v10.1.68/executeportaction

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Execute Port Action

POST`/v1/sites/{siteId}/devices/{deviceId}/interfaces/ports/{portIdx}/actions`

Perform an action on a specific device port. The request body must include the action name and any applicable input arguments.

path Parameters

portIdx

required

integer

siteId

required

string

deviceId

required

string

request Body

action

required

string

POWER\_CYCLE

## Responses

200

Response 200: No schema content available