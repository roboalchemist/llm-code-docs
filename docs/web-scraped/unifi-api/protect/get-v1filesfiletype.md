# get-v1filesfiletype

Source: https://developer.ui.com/protect/v6.2.83/get-v1filesfiletype

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get device asset files

GET`/v1/files/{fileType}`

Get a list of all device asset files

path Parameters

fileType

required

string

Device asset file type

## Responses

200

Response Schema: application/json

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/files/{fileType}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
[  {    "name": "string",    "type": "animations",    "originalName": "string",    "path": "string"  }]
```