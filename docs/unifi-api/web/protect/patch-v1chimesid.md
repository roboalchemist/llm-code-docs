# patch-v1chimesid

Source: https://developer.ui.com/protect/v6.2.83/patch-v1chimesid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Patch chime settings

PATCH`/v1/chimes/{id}`

Patch the settings for a specific chime

path Parameters

id

required

string

The primary key of chime

request Body

name

string

The name of the chime

cameraIdsExpand

Array of string

The list of (doorbell-only) cameras which this chime is paired to.

ringSettingsExpand

Array of object

List of custom ringtone settings for (doorbell-only) cameras paired to this chime.

## Responses

200

Response Schema: application/json

id

required

string

The primary key of chime

modelKey

required

string

The model key of the chime

state

required

string

Connection state of the device.

nameExpand

required

object

mac

required

string

The MAC address of the device

cameraIdsExpand

required

Array of string

The list of (doorbell-only) cameras which this chime is paired to.

ringSettingsExpand

required

Array of object (ringSettings)

List of custom ringtone settings for (doorbell-only) cameras paired to this chime.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X PATCH "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/chimes/{id}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"name\": \"string\",  \"cameraIds\": [    \"string\"  ],  \"ringSettings\": [    {      \"cameraId\": \"string\",      \"repeatTimes\": 0,      \"ringtoneId\": \"string\",      \"volume\": 0    }  ]}"
```

Response Sample

200

```
{  "id": "string",  "modelKey": "string",  "state": "CONNECTED",  "name": "string",  "mac": "string",  "cameraIds": [    "string"  ],  "ringSettings": [    {      "cameraId": "string",      "repeatTimes": 0,      "ringtoneId": "string",      "volume": 0    }  ]}
```