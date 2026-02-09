# get-v1subscribeevents

Source: https://developer.ui.com/protect/v6.2.83/get-v1subscribeevents

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get Protect event messages

GET`/v1/subscribe/events`

A WebSocket subscription that broadcasts Protect events

## Responses

200

Response Schema: application/json

type

required

string

addupdate

itemExpand

required

object (event)