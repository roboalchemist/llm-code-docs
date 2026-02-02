# get-v1nvrs

Source: https://developer.ui.com/protect/v6.2.83/get-v1nvrs

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get NVR details

GET`/v1/nvrs`

Get detailed information about the NVR

## Responses

200

Response Schema: application/json

id

required

string

The primary key of nvr

modelKey

required

string

The model key of the nvr

nameExpand

required

object

doorbellSettingsExpand

required

object

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/nvrs" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "id": "string",  "modelKey": "string",  "name": "string",  "doorbellSettings": {    "defaultMessageText": "string",    "defaultMessageResetTimeoutMs": 0,    "customMessages": [      "string"    ],    "customImages": [      {        "preview": "string",        "sprite": "string"      }    ]  }}
```