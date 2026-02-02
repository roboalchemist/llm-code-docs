# getadopteddevicedetails

Source: https://developer.ui.com/network/v10.1.68/getadopteddevicedetails

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Adopted Device Details

GET`/v1/sites/{siteId}/devices/{deviceId}`

Retrieve detailed information about a specific adopted device, including firmware versioning, uplink state, details about device features and interfaces (ports, radios) and other key attributes.

path Parameters

siteId

required

string

deviceId

required

string

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