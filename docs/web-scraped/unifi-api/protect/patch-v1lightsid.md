# patch-v1lightsid

Source: https://developer.ui.com/protect/v6.2.83/patch-v1lightsid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Patch light settings

PATCH`/v1/lights/{id}`

Patch the settings for a specific light

path Parameters

id

required

string

The primary key of light

request Body

name

string

The name of the model

isLightForceEnabled

boolean

Whether the light has its main LED currently force-enabled.

lightModeSettingsExpand

object

Settings for when and how your light gets activated

lightDeviceSettingsExpand

object

Hardware settings for light device.

## Responses

200

Response Schema: application/json

id

required

string

The primary key of light

modelKey

required

string

The model key of the light

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

lightModeSettingsExpand

required

object

Settings for when and how your light gets activated

lightDeviceSettingsExpand

required

object

Hardware settings for light device.

isDark

required

boolean

Whether the light is currently sensing that it's in a dark scene.

isLightOn

required

boolean

Whether the light has its main LED currently enabled.

isLightForceEnabled

required

boolean

Whether the light has its main LED currently force-enabled.

lastMotion

required

numbernull

Unix timestamp of the last time the PIR motion-detection was triggered.

isPirMotionDetected

required

boolean

Whether the light PIR is currently detecting motion

cameraExpand

required

object

Which camera is configured to be paired to this light.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g -X PATCH "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/lights/{id}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>" \-H "Content-Type: application/json" \-d "{  \"name\": \"string\",  \"isLightForceEnabled\": true,  \"lightModeSettings\": {    \"mode\": \"string\",    \"enableAt\": \"string\"  },  \"lightDeviceSettings\": {    \"isIndicatorEnabled\": true,    \"pirDuration\": 0,    \"pirSensitivity\": 0,    \"ledLevel\": 0  }}"
```

Response Sample

200

```
{  "id": "string",  "modelKey": "string",  "state": "CONNECTED",  "name": "string",  "mac": "string",  "lightModeSettings": {    "mode": "string",    "enableAt": "string"  },  "lightDeviceSettings": {    "isIndicatorEnabled": true,    "pirDuration": 0,    "pirSensitivity": 0,    "ledLevel": 0  },  "isDark": true,  "isLightOn": true,  "isLightForceEnabled": true,  "lastMotion": null,  "isPirMotionDetected": true,  "camera": "string"}
```