# executeadopteddeviceaction

Source: https://developer.ui.com/network/v10.1.68/executeadopteddeviceaction

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Execute Adopted Device Action

POST`/v1/sites/{siteId}/devices/{deviceId}/actions`

Perform an action on an specific adopted device. The request body must include the action name and any applicable input arguments.

path Parameters

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

RESTART

## Responses

200

Response 200: No schema content available