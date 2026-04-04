# get-v1camerasidsnapshot

Source: https://developer.ui.com/protect/v6.2.83/get-v1camerasidsnapshot

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Get camera snapshot

GET`/v1/cameras/{id}/snapshot`

Get a snapshot image from a specific camera

path Parameters

id

required

string

The primary key of camera

query Parameters

highQuality

string

Whether to force 1080P or higher resolution snapshot

## Responses

200

Response Schema: image/jpeg

Example - Call

cURLGoNode.jsPythonAnsible

Example call uses [UniFi Connector](/protect/v6.2.83/connectorpost) which requires FW version >= 5.0.3

```
curl -L -g "https://api.ui.com/v1/connector/consoles/{consoleId}/proxy/protect/integration/v1/cameras/{id}/snapshot?highQuality={highQuality}" \-H "Accept: application/json" \-H "X-API-Key: <X-API-Key>"
```

Response Sample

No example responses available