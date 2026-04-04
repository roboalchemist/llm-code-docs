# patch-v1viewersid

Source: https://developer.ui.com/protect/v6.2.83/patch-v1viewersid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Patch viewer settings

PATCH`/v1/viewers/{id}`

Patch the settings for a specific viewer

path Parameters

id

required

string

The primary key of viewer

request Body

name

string

The name of the model

liveviewExpand

object

## Responses

200

Response Schema: application/json

id

required

string

The primary key of viewer

modelKey

required

string

The model key of the viewer

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

liveviewExpand

required

object

streamLimit

required

number

Count of maximum supported parallel live streams.