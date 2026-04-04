# post-v1camerasidptzpatrolstartslot

Source: https://developer.ui.com/protect/v6.2.83/post-v1camerasidptzpatrolstartslot

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Start a camera PTZ patrol

POST`/v1/cameras/{id}/ptz/patrol/start/{slot}`

Start a camera PTZ patrol

path Parameters

id

required

string

The primary key of camera

slot

required

string

The slot number (0-4) of the patrol that is currently running, or null if no patrol is running

## Responses

204

Response 204: No schema content available