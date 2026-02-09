# get-v1subscribedevices

Source: https://developer.ui.com/protect/v6.2.83/get-v1subscribedevices

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get update messages about devices

GET`/v1/subscribe/devices`

A WebSocket subscription which broadcasts all changes happening to Protect-managed hardware devices

## Responses

200

Response Schema: application/json

type

required

string

addupdateremove

itemExpand

required

object (device)