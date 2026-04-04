# adoptdevice

Source: https://developer.ui.com/network/v10.1.68/adoptdevice

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Adopt Devices

POST`/v1/sites/{siteId}/devices`

Adopt a device to a site.

path Parameters

siteId

required

string

request Body

macAddress

required

string

ignoreDeviceLimit

required

boolean

## Responses

200

Response Schema: application/json

id

required

string

macAddress

required

string

ipAddress

required

string

name

required

string

model

required

string

supported

required

boolean

state

required

string

firmwareVersion

string

firmwareUpdatable

required

boolean

adoptedAt

string

provisionedAt

string

configurationId

required

string

uplinkExpand

object

Uplink interface is device's connection to the parent device in the network topology

featuresExpand

required

object

interfacesExpand

required

object