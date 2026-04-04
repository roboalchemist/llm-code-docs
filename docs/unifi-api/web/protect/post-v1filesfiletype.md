# post-v1filesfiletype

Source: https://developer.ui.com/protect/v6.2.83/post-v1filesfiletype

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Upload device asset file

POST`/v1/files/{fileType}`

Upload a new device asset file

path Parameters

fileType

required

string

Device asset file type

request Body

## Responses

200

Response Schema: application/json

name

required

string

Unique ID for the asset file

type

required

string

Device asset file type

originalName

string

Original filename of the uploaded file

path

required

string

Path to the file on the filesystem

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X POST "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/files/{fileType}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "name": "string",  "type": "animations",  "originalName": "string",  "path": "string"}
```