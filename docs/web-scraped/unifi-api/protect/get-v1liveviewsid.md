# get-v1liveviewsid

Source: https://developer.ui.com/protect/v6.2.83/get-v1liveviewsid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get live view details

GET`/v1/liveviews/{id}`

Get detailed information about a specific live view

path Parameters

id

required

string

The primary key of liveview

## Responses

200

Response Schema: application/json

id

required

string

The primary key of liveview

modelKey

required

string

The model key of the liveview

name

required

string

The name of this live view.

isDefault

required

boolean

Whether this live view is the default one for all viewers.

isGlobal

required

boolean

Whether this live view is global and available system-wide to all users

owner

required

string

The primary key of user

layout

required

number

The number of slots this live view contains. Which as a consequence also affects the layout of the live view.

slotsExpand

required

Array of object

List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/liveviews/{id}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
{  "id": "string",  "modelKey": "string",  "name": "string",  "isDefault": true,  "isGlobal": true,  "owner": "string",  "layout": 0,  "slots": [    {      "cameras": [        "string"      ],      "cycleMode": "motion",      "cycleInterval": 0    }  ]}
```