# get-v1chimes

Source: https://developer.ui.com/protect/v6.2.83/get-v1chimes

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get all chimes

GET`/v1/chimes`

Get detailed information about all chimes

## Responses

200

Response Schema: application/json

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/chimes" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
[  {    "id": "string",    "modelKey": "string",    "state": "CONNECTED",    "name": "string",    "mac": "string",    "cameraIds": [      "string"    ],    "ringSettings": [      {        "cameraId": "string",        "repeatTimes": 0,        "ringtoneId": "string",        "volume": 0      }    ]  }]
```