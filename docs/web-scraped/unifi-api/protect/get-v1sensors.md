# get-v1sensors

Source: https://developer.ui.com/protect/v6.2.83/get-v1sensors

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get all sensors

GET`/v1/sensors`

Get detailed information about all sensors

## Responses

200

Response Schema: application/json

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/sensors" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

200

```
[  {    "id": "string",    "modelKey": "string",    "state": "CONNECTED",    "name": "string",    "mac": "string",    "mountType": "door",    "batteryStatus": {      "percentage": null,      "isLow": true    },    "stats": {      "light": {        "value": 0,        "status": "neutral"      },      "humidity": {        "value": 0,        "status": "neutral"      },      "temperature": {        "value": 0,        "status": "neutral"      }    },    "lightSettings": {      "isEnabled": true,      "margin": 0,      "lowThreshold": null,      "highThreshold": null    },    "humiditySettings": {      "isEnabled": true,      "margin": 0,      "lowThreshold": null,      "highThreshold": null    },    "temperatureSettings": {      "isEnabled": true,      "margin": 0,      "lowThreshold": null,      "highThreshold": null    },    "isOpened": true,    "openStatusChangedAt": null,    "isMotionDetected": true,    "motionDetectedAt": null,    "motionSettings": {      "isEnabled": true,      "sensitivity": 0    },    "alarmTriggeredAt": null,    "alarmSettings": {      "isEnabled": true    },    "leakDetectedAt": null,    "externalLeakDetectedAt": null,
```