# get-v1sensorsid

Source: https://developer.ui.com/protect/v6.2.83/get-v1sensorsid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get sensor details

GET`/v1/sensors/{id}`

Get detailed information about a specific sensor

path Parameters

id

required

string

The primary key of sensor

## Responses

200

Response Schema: application/json

id

required

string

The primary key of sensor

modelKey

required

string

The model key of the sensor

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

mountType

required

string

Mounting type of the sensor.

batteryStatusExpand

required

object

[DEPRECATED] Use wirelessConnectionState.batteryStatus instead. Battery status.

statsExpand

required

object

Sensor statistics.

lightSettingsExpand

required

object

Ambient light sensor settings.

humiditySettingsExpand

required

object

Relative humidity sensor settings.

temperatureSettingsExpand

required

object

Temperature sensor settings.

isOpened

required

boolean

Whether the door/window/garage is opened.

openStatusChangedAt

required

numbernull

Unix timestamp when the door/window/garage was last opened or closed, nullable.

isMotionDetected

required

boolean

Whether sensor is currently detecting the motion.

motionDetectedAt

required

numbernull

Unix timestamp when the last motion was detected.

motionSettingsExpand

required

object

Motion sensor settings.

alarmTriggeredAt

required

numbernull

Unix timestamp when the smoke or carbon monoxide alarm was triggered, nullable.

alarmSettingsExpand

required

object

Smoke and carbon monoxide alarm sensor settings.

leakDetectedAt

required

numbernull

Unix timestamp when the sensor detected a water leak, nullable.

externalLeakDetectedAt

required

numbernull

Unix timestamp when the sensor detected an external water leak, nullable.

leakSettingsExpand

required

object

Leak sensor settings.

tamperingDetectedAt

required

numbernull

Unix timestamp when the sensor detected tampering, nullable.

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

Response Sample

200

```
{  "id": "string",  "modelKey": "string",  "state": "CONNECTED",  "name": "string",  "mac": "string",  "mountType": "door",  "batteryStatus": {    "percentage": null,    "isLow": true  },  "stats": {    "light": {      "value": 0,      "status": "neutral"    },    "humidity": {      "value": 0,      "status": "neutral"    },    "temperature": {      "value": 0,      "status": "neutral"    }  },  "lightSettings": {    "isEnabled": true,    "margin": 0,    "lowThreshold": null,    "highThreshold": null  },  "humiditySettings": {    "isEnabled": true,    "margin": 0,    "lowThreshold": null,    "highThreshold": null  },  "temperatureSettings": {    "isEnabled": true,    "margin": 0,    "lowThreshold": null,    "highThreshold": null  },  "isOpened": true,  "openStatusChangedAt": null,  "isMotionDetected": true,  "motionDetectedAt": null,  "motionSettings": {    "isEnabled": true,    "sensitivity": 0  },  "alarmTriggeredAt": null,  "alarmSettings": {    "isEnabled": true  },  "leakDetectedAt": null,  "externalLeakDetectedAt": null,  "leakSettings": {
```