# patch-v1camerasid

Source: https://developer.ui.com/protect/v6.2.83/patch-v1camerasid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Patch camera settings

PATCH`/v1/cameras/{id}`

Patch the settings for a specific camera

path Parameters

id

required

string

The primary key of camera

request Body

name

string

The name of the camera

osdSettingsExpand

object

On Screen Display settings.

ledSettingsExpand

object

LED settings.

lcdMessageExpand

object (lcdMessage)

Message that's set on the LCD screen (for doorbells and/or other devices with LCD screens). To upload image assets for the LCD screen, use the `/files/{fileType}` endpoint.

micVolumeExpand

object

videoMode

string

Current video mode of the camera

hdrTypeExpand

object

High Dynamic Range (HDR) mode setting.

smartDetectSettingsExpand

object

Smart detection settings for the camera.

## Responses

200

Response Schema: application/json

id

required

string

The primary key of camera

modelKey

required

string

The model key of the camera

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

isMicEnabled

required

boolean

Whether or not the microphone on camera is enabled

osdSettingsExpand

required

object

On Screen Display settings.

ledSettingsExpand

required

object

LED settings.

lcdMessageExpand

required

object

micVolume

required

number

Mic volume: a number from 0-100.

activePatrolSlotExpand

required

object

videoMode

required

string

Current video mode of the camera

hdrType

required

string

High Dynamic Range (HDR) mode setting.

featureFlagsExpand

required

object

smartDetectSettingsExpand

required

object

Smart detection settings for the camera.